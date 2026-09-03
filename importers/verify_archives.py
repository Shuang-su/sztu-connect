"""Verify vendored source archives offline, without extracting or running them.

Git tree IDs establish equality with the recorded upstream tree, not author
identity, software safety, or the authenticity of any exported chat content.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import tarfile
from typing import Any


MAX_ARCHIVE_BYTES = 100 * 1024 * 1024
MAX_UNPACKED_BYTES = 256 * 1024 * 1024
MAX_MEMBERS = 10_000
CHUNK_BYTES = 1024 * 1024


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(CHUNK_BYTES), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _parts(value: str) -> tuple[str, ...]:
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        raise ValueError("invalid archive or registry path")
    parts = tuple(value.split("/"))
    if any(part in {"", ".", ".."} or ":" in part for part in parts):
        raise ValueError("absolute or non-canonical archive or registry path")
    return parts


def local_file(root: Path, relative: str) -> Path:
    parts = _parts(relative)
    candidate = root.joinpath(*parts)
    for index in range(1, len(parts) + 1):
        if root.joinpath(*parts[:index]).is_symlink():
            raise ValueError("registry paths must not traverse symlinks")
    if not candidate.resolve().is_relative_to(root.resolve()):
        raise ValueError("registry path escapes importer directory")
    if not candidate.is_file():
        raise ValueError("registry file is missing")
    return candidate


def git_tree_id(files: dict[str, dict[str, Any]]) -> str:
    tree: dict[str, Any] = {}
    for name, entry in files.items():
        parts = _parts(name)
        parent = tree
        for part in parts[:-1]:
            node = parent.setdefault(part, {})
            if not isinstance(node, dict):
                raise ValueError("file and directory paths overlap")
            parent = node
        if parts[-1] in parent:
            raise ValueError("duplicate file or directory path")
        parent[parts[-1]] = (entry["mode"], entry["git_blob"])

    def digest_tree(node: dict[str, Any]) -> str:
        body = bytearray()
        ordered = sorted(
            node.items(),
            key=lambda item: item[0].encode("utf-8")
            + (b"/" if isinstance(item[1], dict) else b""),
        )
        for name, value in ordered:
            mode, oid = ("40000", digest_tree(value)) if isinstance(value, dict) else value
            body.extend(mode.encode("ascii") + b" " + name.encode("utf-8") + b"\x00")
            body.extend(bytes.fromhex(oid))
        return hashlib.sha1(b"tree " + str(len(body)).encode() + b"\x00" + body).hexdigest()

    return digest_tree(tree)


def inspect_archive(path: Path, prefix: str) -> dict[str, Any]:
    """Read a bounded GitHub tarball without extraction; accept no links."""
    if len(_parts(prefix)) != 1:
        raise ValueError("archive prefix must be one directory")
    if path.stat().st_size > MAX_ARCHIVE_BYTES:
        raise ValueError("archive exceeds the ordinary Git size limit")
    files: dict[str, dict[str, Any]] = {}
    directories: set[str] = set()
    seen: set[str] = set()
    expanded_bytes = 0
    with tarfile.open(path, "r:gz") as archive:
        for index, member in enumerate(archive, 1):
            if index > MAX_MEMBERS:
                raise ValueError("too many archive members")
            name = member.name.removesuffix("/") if member.isdir() else member.name
            parts = _parts(name)
            if parts[0] != prefix or (len(parts) == 1 and not member.isdir()):
                raise ValueError("member outside the recorded archive prefix")
            if name in seen:
                raise ValueError("duplicate archive member")
            seen.add(name)
            relative = "/".join(parts[1:])
            if member.mode & 0o7000:
                raise ValueError("special permission bits in archive")
            if member.isdir():
                if relative:
                    directories.add(relative)
                continue
            if not member.isfile() or member.sparse is not None:
                raise ValueError("links, sparse files and special archive members are unsupported")
            if member.size < 0:
                raise ValueError("negative member size")
            expanded_bytes += member.size
            if expanded_bytes > MAX_UNPACKED_BYTES:
                raise ValueError("archive expands beyond the inspection budget")
            blob = hashlib.sha1(b"blob " + str(member.size).encode() + b"\x00")
            checksum = hashlib.sha256()
            handle = archive.extractfile(member)
            if handle is None:
                raise ValueError("missing regular-file payload")
            size = 0
            with handle:
                for chunk in iter(lambda: handle.read(CHUNK_BYTES), b""):
                    blob.update(chunk)
                    checksum.update(chunk)
                    size += len(chunk)
            if size != member.size:
                raise ValueError("truncated archive member")
            mode = "100755" if member.mode & 0o111 else "100644"
            files[relative] = {
                "mode": mode, "git_blob": blob.hexdigest(),
                "sha256": checksum.hexdigest(), "size_bytes": size,
            }
    if not files:
        raise ValueError("archive has no files")
    for directory in directories:
        if directory in files or any(
            str(parent) in files for parent in PurePosixPath(directory).parents
        ):
            raise ValueError("directory overlaps a file")
    return {"git_tree": git_tree_id(files), "file_count": len(files),
            "expanded_bytes": expanded_bytes, "files": files}


def verify_registry(registry_path: Path) -> dict[str, Any]:
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    if not isinstance(registry, dict) or registry.get("schema_version") != 1:
        raise ValueError("unsupported registry version")
    if not isinstance(registry.get("tools"), list):
        raise ValueError("registry tools must be a list")
    root = registry_path.parent
    results: list[dict[str, Any]] = []
    for tool in registry["tools"]:
        if not isinstance(tool, dict) or not isinstance(tool.get("id"), str):
            raise ValueError("registry tool must have a string id")
        source = tool.get("source_archive")
        if source is None:
            continue
        result: dict[str, Any] = {"id": tool["id"], "ok": False}
        try:
            if not isinstance(source, dict):
                raise ValueError("source archive must be an object")
            if not re.fullmatch(r"[0-9a-f]{40}", tool["commit"]):
                raise ValueError("source must be pinned to a full commit")
            if not re.fullmatch(r"[0-9a-f]{40}", tool["git_tree"]):
                raise ValueError("source must record a full upstream Git tree")
            if not re.fullmatch(r"[0-9a-f]{64}", source["sha256"]):
                raise ValueError("source must record a SHA-256 digest")
            path = local_file(root, source["path"])
            if path.stat().st_size > MAX_ARCHIVE_BYTES:
                raise ValueError("archive exceeds the ordinary Git size limit")
            if path.stat().st_size != source["size_bytes"]:
                raise ValueError("archive size mismatch")
            if sha256_file(path) != source["sha256"]:
                raise ValueError("archive SHA-256 mismatch")
            inspected = inspect_archive(path, source["prefix"])
            if inspected["git_tree"] != tool["git_tree"]:
                raise ValueError("archive content differs from the recorded upstream Git tree")
            if not isinstance(source["license_copies"], list) or not source["license_copies"]:
                raise ValueError("source must retain its upstream license")
            for license_entry in source["license_copies"]:
                original = inspected["files"][license_entry["archive_member"]]
                copy = local_file(root, license_entry["path"])
                if original["sha256"] != sha256_file(copy):
                    raise ValueError("license copy differs from upstream archive")
            result.update(ok=True, sha256=source["sha256"],
                          git_tree=inspected["git_tree"],
                          file_count=inspected["file_count"],
                          expanded_bytes=inspected["expanded_bytes"])
        except (OSError, ValueError, KeyError, TypeError, EOFError, tarfile.TarError) as error:
            # Errors include names and failure kinds, never archived file content.
            result["error"] = type(error).__name__ if isinstance(error, (KeyError, TypeError)) else str(error)
        results.append(result)
    return {"ok": bool(results) and all(item["ok"] for item in results),
            "archives": results, "network_used": False, "upstream_code_executed": False}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path,
                        default=Path(__file__).resolve().with_name("registry.json"))
    args = parser.parse_args()
    try:
        result = verify_registry(args.registry)
    except (OSError, ValueError, KeyError, TypeError) as error:
        result = {"ok": False, "error": type(error).__name__}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
