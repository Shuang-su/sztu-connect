from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = Path(".work/onboarding/exploration.md")


def report_guard_example() -> str:
    guide = (ROOT / "docs/GETTING_STARTED.md").read_text(encoding="utf-8")
    candidates = [block for block in re.findall(r"```python\n(.*?)\n```", guide, re.S)
                  if "from scripts.bootstrap import local_path" in block]
    if len(candidates) != 1:
        raise AssertionError("The guide must expose one executable shared report-path check")
    return candidates[0]


def tree_snapshot(root: Path) -> dict[str, tuple[bytes | str, int]]:
    result = {}
    for item in root.rglob("*"):
        relative = item.relative_to(root).as_posix()
        if item.is_symlink():
            result[relative] = (os.readlink(item), item.lstat().st_mtime_ns)
        elif item.is_file():
            result[relative] = (item.read_bytes(), item.stat().st_mtime_ns)
    return result


class ExplorationReportBoundaryTests(unittest.TestCase):
    """Execute the documented guard; these tests do not simulate an Agent's reasoning."""

    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.sandbox = Path(temporary.name).resolve()
        self.root = self.sandbox / "技大 材料工作副本"
        self.root.mkdir()

    def guard(self) -> subprocess.CompletedProcess[str]:
        env = dict(os.environ)
        env["PYTHONPATH"] = str(ROOT)
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        # The child prints CJK paths to a pipe, independent of Windows locale.
        env["PYTHONUTF8"] = "1"
        return subprocess.run([sys.executable, "-B", "-c", report_guard_example()],
                              cwd=self.root, env=env, capture_output=True,
                              text=True, encoding="utf-8", timeout=10)

    def link(self, path: Path, target: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            path.symlink_to(target, target_is_directory=target.is_dir())
        except OSError as error:
            self.skipTest(f"Symlink creation requires OS permission: {error}")

    def assert_read_only_failure(self) -> None:
        before = tree_snapshot(self.sandbox)
        result = self.guard()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ValueError", result.stderr)
        self.assertEqual(before, tree_snapshot(self.sandbox))

    def test_missing_report_parents_are_not_created_by_check(self) -> None:
        before = tree_snapshot(self.sandbox)
        result = self.guard()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(Path(result.stdout.strip()), self.root / REPORT)
        self.assertFalse((self.root / ".work").exists())
        self.assertEqual(before, tree_snapshot(self.sandbox))

    def test_existing_report_and_original_are_unchanged(self) -> None:
        report = self.root / REPORT
        report.parent.mkdir(parents=True)
        report.write_text("合成恢复记录：尚有一个文件未读。\n", encoding="utf-8")
        original = self.root / "已提供的校园材料.txt"
        original.write_text("仅用于测试，不是真实校园材料。\n", encoding="utf-8")
        before = tree_snapshot(self.sandbox)
        result = self.guard()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(Path(result.stdout.strip()), report)
        self.assertEqual(before, tree_snapshot(self.sandbox))

    def test_report_file_link_cannot_redirect_to_original(self) -> None:
        original = self.root / "原始材料.md"
        original.write_text("合成原件，不可覆盖。\n", encoding="utf-8")
        self.link(self.root / REPORT, original)
        self.assert_read_only_failure()

    def test_report_parent_link_cannot_redirect_to_formal_records(self) -> None:
        formal = self.root / "content/events"
        formal.mkdir(parents=True)
        self.link(self.root / ".work/onboarding", formal)
        self.assert_read_only_failure()

    def test_work_link_cannot_redirect_outside_checkout(self) -> None:
        outside = self.sandbox / "其他资料"
        outside.mkdir()
        self.link(self.root / ".work", outside)
        self.assert_read_only_failure()

    def test_dangling_report_link_is_not_followed(self) -> None:
        self.link(self.root / REPORT, self.sandbox / "不存在的原件.md")
        self.assert_read_only_failure()

    @unittest.skipUnless(os.name == "nt", "Real junction creation requires Windows")
    def test_windows_junction_cannot_redirect_report(self) -> None:
        outside = self.sandbox / "其他资料"
        outside.mkdir()
        (self.root / ".work").mkdir()
        junction = self.root / ".work/onboarding"
        result = subprocess.run(["cmd", "/c", "mklink", "/J", str(junction), str(outside)],
                                capture_output=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.addCleanup(junction.rmdir)
        self.assert_read_only_failure()


if __name__ == "__main__":
    unittest.main()
