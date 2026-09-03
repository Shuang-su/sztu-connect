"""Offline integrity and failure-path tests; no third-party code is executed."""

import copy
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile
import unittest
from unittest.mock import patch

from importers import verify_archives as verifier


ROOT = Path(__file__).resolve().parents[1]


class ImporterArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.archive = self.root / "source.tar.gz"
        self.registry_path = self.root / "registry.json"

    def write_archive(self, members=None):
        if members is None:
            members = [("snapshot/LICENSE", b"Synthetic fixture license\n"),
                       ("snapshot/src/example.txt", b"Not executable source\n")]
        with tarfile.open(self.archive, "w:gz") as archive:
            for entry in members:
                if isinstance(entry, tarfile.TarInfo):
                    archive.addfile(entry)
                else:
                    name, data = entry
                    member = tarfile.TarInfo(name)
                    member.size = len(data)
                    member.mode = 0o644
                    archive.addfile(member, io.BytesIO(data))

    def fixture_registry(self):
        self.write_archive()
        (self.root / "LICENSE.upstream").write_bytes(b"Synthetic fixture license\n")
        return {
            "schema_version": 1,
            "tools": [{
                "id": "fixture", "commit": "1" * 40,
                "git_tree": verifier.inspect_archive(self.archive, "snapshot")["git_tree"],
                "source_archive": {
                    "path": "source.tar.gz", "prefix": "snapshot",
                    "size_bytes": self.archive.stat().st_size,
                    "sha256": verifier.sha256_file(self.archive),
                    "license_copies": [{"archive_member": "LICENSE",
                                        "path": "LICENSE.upstream"}],
                },
            }],
        }

    def verify_fixture(self, registry):
        self.registry_path.write_text(json.dumps(registry), encoding="utf-8")
        return verifier.verify_registry(self.registry_path)

    def test_archived_sources_match_upstream_trees_and_license_copies(self):
        result = verifier.verify_registry(ROOT / "importers/registry.json")
        self.assertTrue(result["ok"], result)
        self.assertEqual({item["id"]: item["file_count"] for item in result["archives"]},
                         {"ciphertalk": 927, "wechatmsg": 264})
        self.assertFalse(result["network_used"])
        self.assertFalse(result["upstream_code_executed"])

    def test_catalog_is_distinct_from_local_archives_and_installer_checks(self):
        registry = json.loads((ROOT / "importers/registry.json").read_text())
        ids = [tool["id"] for tool in registry["tools"]]
        self.assertEqual(len(ids), len(set(ids)))
        for tool in registry["tools"]:
            with self.subTest(tool=tool["id"]):
                self.assertFalse(tool["compatibility"]["runtime_tested"])
                if tool["role"].startswith("catalog-only"):
                    self.assertIsNone(tool["source_archive"])
                for asset in tool["downloads"]:
                    self.assertFalse(asset["local_payload_archived"])
                    self.assertEqual(asset["verification"], "upstream-api-digest-only")
                    self.assertIn("/releases/download/" + tool["release"]["tag"] + "/",
                                  asset["url"])
                    self.assertNotIn("/latest/", asset["url"])

    def test_git_checkout_preserves_source_and_license_bytes(self):
        registry = json.loads((ROOT / "importers/registry.json").read_text())
        paths = []
        for tool in registry["tools"]:
            source = tool.get("source_archive")
            if source:
                paths.append("importers/" + source["path"])
                paths.extend("importers/" + item["path"] for item in source["license_copies"])
        result = subprocess.run(["git", "check-attr", "-z", "text", "filter", "--", *paths],
                                cwd=ROOT, capture_output=True, text=True, check=True)
        attributes = result.stdout.rstrip("\x00").split("\x00")
        self.assertEqual(len(attributes), len(paths) * 2 * 3)
        for index in range(0, len(attributes), 3):
            path, attribute, value = attributes[index:index + 3]
            self.assertEqual(value, "unset", (path, attribute, value))

    def test_archive_hash_detects_changed_payload(self):
        registry = self.fixture_registry()
        with self.archive.open("r+b") as handle:
            handle.seek(-5, 2)
            handle.write(b"wrong")
        result = self.verify_fixture(registry)
        self.assertFalse(result["ok"])
        self.assertIn("SHA-256 mismatch", result["archives"][0]["error"])

    def test_git_tree_detects_change_even_if_archive_checksum_is_updated(self):
        registry = self.fixture_registry()
        self.write_archive([("snapshot/LICENSE", b"Synthetic fixture license\n"),
                            ("snapshot/src/example.txt", b"Altered file\n")])
        source = registry["tools"][0]["source_archive"]
        source.update(size_bytes=self.archive.stat().st_size,
                      sha256=verifier.sha256_file(self.archive))
        result = self.verify_fixture(registry)
        self.assertFalse(result["ok"])
        self.assertIn("upstream Git tree", result["archives"][0]["error"])

    def test_license_copy_cannot_be_replaced(self):
        registry = self.fixture_registry()
        (self.root / "LICENSE.upstream").write_bytes(b"Different license\n")
        result = self.verify_fixture(registry)
        self.assertFalse(result["ok"])
        self.assertIn("license copy differs", result["archives"][0]["error"])

    def test_registry_requires_a_full_pin_and_retained_license(self):
        base = self.fixture_registry()
        for field, value in [("commit", "main"), ("git_tree", "1" * 7)]:
            registry = copy.deepcopy(base)
            registry["tools"][0][field] = value
            self.assertFalse(self.verify_fixture(registry)["ok"])
        base["tools"][0]["source_archive"]["license_copies"] = []
        self.assertFalse(self.verify_fixture(base)["ok"])

    def test_unsafe_duplicate_and_conflicting_members_are_rejected(self):
        cases = [
            [("snapshot/../escape", b"x")], [("/snapshot/absolute", b"x")],
            [("snapshot/back\\slash", b"x")], [("other/file", b"x")],
            [("snapshot/a//b", b"x")], [("snapshot/C:drive", b"x")],
            [("snapshot/a", b"x"), ("snapshot/a", b"y")],
            [("snapshot/a", b"x"), ("snapshot/a/b", b"y")],
            [("snapshot/a/b", b"x"), ("snapshot/a", b"y")],
        ]
        for members in cases:
            with self.subTest(members=[item[0] for item in members]):
                self.write_archive(members)
                with self.assertRaises(ValueError):
                    verifier.inspect_archive(self.archive, "snapshot")

    def test_links_and_special_members_are_rejected_without_extraction(self):
        for kind in [tarfile.SYMTYPE, tarfile.LNKTYPE, tarfile.CHRTYPE, tarfile.FIFOTYPE]:
            member = tarfile.TarInfo("snapshot/link")
            member.type = kind
            member.linkname = "../outside"
            self.write_archive([member])
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                verifier.inspect_archive(self.archive, "snapshot")
        self.assertEqual(sorted(path.name for path in self.root.iterdir()), ["source.tar.gz"])

    def test_directory_permissions_and_file_directory_overlap_are_rejected(self):
        directory = tarfile.TarInfo("snapshot/a/")
        directory.type = tarfile.DIRTYPE
        directory.mode = 0o4755
        self.write_archive([directory, ("snapshot/file", b"x")])
        with self.assertRaisesRegex(ValueError, "permission"):
            verifier.inspect_archive(self.archive, "snapshot")
        directory.mode = 0o755
        self.write_archive([directory, ("snapshot/a", b"x")])
        with self.assertRaises(ValueError):
            verifier.inspect_archive(self.archive, "snapshot")

    def test_limits_are_enforced_before_large_reads(self):
        self.write_archive()
        for setting in ["MAX_ARCHIVE_BYTES", "MAX_UNPACKED_BYTES", "MAX_MEMBERS"]:
            with self.subTest(setting=setting), patch.object(verifier, setting, 1):
                with self.assertRaises(ValueError):
                    verifier.inspect_archive(self.archive, "snapshot")
        registry = self.fixture_registry()
        with patch.object(verifier, "MAX_ARCHIVE_BYTES", 1), \
                patch.object(verifier, "sha256_file", side_effect=AssertionError("read too early")):
            self.assertFalse(self.verify_fixture(registry)["ok"])

    def test_registry_paths_cannot_escape_or_follow_links(self):
        (self.root / "file").write_bytes(b"fixture")
        (self.root / "link").symlink_to(self.root / "file")
        (self.root / "directory-link").symlink_to(self.root, target_is_directory=True)
        for value in ["../file", "/file", "file/../file", "link", "directory-link/file"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                verifier.local_file(self.root, value)

    def test_git_ordering_and_executable_mode_match_git_hash_object(self):
        blob = hashlib.sha1(b"blob 1\x00x").hexdigest()

        def git_hash(body):
            result = subprocess.run(["git", "hash-object", "-t", "tree", "--stdin"],
                                    input=body, capture_output=True, check=True)
            return result.stdout.decode().strip()

        subtree = git_hash(b"100755 script\x00" + bytes.fromhex(blob))
        expected = git_hash(b"100644 a.c\x00" + bytes.fromhex(blob)
                            + b"40000 a\x00" + bytes.fromhex(subtree)
                            + b"100644 a0\x00" + bytes.fromhex(blob))
        files = {
            "a0": {"mode": "100644", "git_blob": blob},
            "a/script": {"mode": "100755", "git_blob": blob},
            "a.c": {"mode": "100644", "git_blob": blob},
        }
        self.assertEqual(verifier.git_tree_id(files), expected)
        files["a/script"]["mode"] = "100644"
        self.assertNotEqual(verifier.git_tree_id(files), expected)

    def test_malformed_registry_cli_returns_json_failure(self):
        for registry in [[], {"schema_version": 99}, {"schema_version": 1, "tools": [None]},
                         {"schema_version": 1, "tools": []}]:
            self.registry_path.write_text(json.dumps(registry), encoding="utf-8")
            result = subprocess.run([sys.executable, str(ROOT / "importers/verify_archives.py"),
                                     "--registry", str(self.registry_path)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertFalse(json.loads(result.stdout)["ok"])
            self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
