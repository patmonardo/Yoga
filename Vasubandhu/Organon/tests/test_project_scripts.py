"""Regression tests for project-wide Organon QA and PDF build commands."""

from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

from audit_karika_sections import (
    KARMAN_SECTION_ORDER,
    check_headings,
    headings_in,
)


ORGANON_DIR = Path(__file__).resolve().parents[1]
TESTS_DIR = Path(__file__).resolve().parent
EDITIONS_DIR = ORGANON_DIR / "editions"
BUILD_SCRIPT = EDITIONS_DIR / "build.sh"
AUDIT_SCRIPT = TESTS_DIR / "audit_karika_sections.py"
KARMA_DIR = ORGANON_DIR / "04-karma"


class ProjectScriptTests(unittest.TestCase):
    def test_all_karman_karika_titles_match_their_bhasya_titles(self):
        for verse in range(1, 128):
            stem = f"VAK_4.{verse:02d}"
            karika_heading = (KARMA_DIR / f"{stem}.md").read_text(
                encoding="utf-8"
            ).splitlines()[0]
            bhasya_heading = (KARMA_DIR / f"{stem}_bhasya.md").read_text(
                encoding="utf-8"
            ).splitlines()[0]
            bhasya_title = re.fullmatch(
                rf"# VAK[ _]4\.{verse:02d} Bhāṣya — (.+)", bhasya_heading
            )
            with self.subTest(verse=verse):
                self.assertIsNotNone(
                    bhasya_title, f"Unexpected Bhāṣya heading: {bhasya_heading}"
                )
                if bhasya_title is None:
                    continue
                self.assertEqual(
                    karika_heading,
                    f"# {stem} — {bhasya_title.group(1)}",
                )

    def test_karman_profile_rejects_argument_section_headings(self):
        headings = (
            "## 1. Sanskrit (Devanāgarī)",
            "## 2. Sanskrit (IAST)",
            "## 3. Lexical Analysis",
            "## 4. Grammar",
            "## 5. Translation",
            "## 6. Argument and Scope",
        )
        errors = check_headings(headings, profile="karman")
        self.assertTrue(any("argument heading" in error for error in errors))

    def test_karman_profile_locks_exact_top_level_schema(self):
        headings = tuple(
            f"## {number}. {section}"
            for number, section in enumerate(KARMAN_SECTION_ORDER, start=1)
        )
        self.assertEqual(check_headings(headings, profile="karman"), [])

        legacy_headings = (
            *headings[:5],
            "## 6. Interpretation",
            "## 7. Logical Determination",
            "## 8. Textual Notes",
        )
        errors = check_headings(legacy_headings, profile="karman")
        self.assertTrue(
            any("missing required section" in error for error in errors)
        )
        self.assertTrue(
            any("do not match the Karman template" in error for error in errors)
        )

    def test_karman_profile_accepts_empty_sections(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "study.md"
            path.write_text(
                "\n".join(
                    f"## {number}. {section}"
                    for number, section in enumerate(KARMAN_SECTION_ORDER, start=1)
                ),
                encoding="utf-8",
            )

            headings = headings_in(path)
            self.assertEqual(
                check_headings(headings, profile="karman"),
                [],
            )

    def test_karman_profile_ignores_child_headings(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "study.md"
            path.write_text(
                "\n".join(
                    f"## {number}. {section}\n### Verse-specific child"
                    for number, section in enumerate(KARMAN_SECTION_ORDER, start=1)
                ),
                encoding="utf-8",
            )

            headings = headings_in(path)
            self.assertEqual(
                check_headings(headings, profile="karman"),
                [],
            )

    def test_generic_profile_accepts_volume_specific_headings(self):
        headings = ("## Source", "## Word Division", "## Scientific Translation")
        self.assertEqual(check_headings(headings, profile="generic"), [])
        self.assertIn(
            "missing requested section: Grammar",
            check_headings(
                headings,
                profile="generic",
                additional_required=("Grammar",),
            ),
        )

    def test_karman_heading_audit_covers_selected_verse_range(self):
        result = subprocess.run(
            [
                sys.executable,
                str(AUDIT_SCRIPT),
                "--chapter",
                "4",
                "--start",
                "42",
                "--end",
                "66",
                "--check",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("25 of 25 requested", result.stdout)
        self.assertIn("Checking headings with the karman profile", result.stdout)
        self.assertIn("all requested studies conform", result.stdout)

    def test_karman_check_cannot_be_downgraded_to_generic(self):
        result = subprocess.run(
            [
                sys.executable,
                str(AUDIT_SCRIPT),
                "--chapter",
                "4",
                "--start",
                "42",
                "--end",
                "66",
                "--profile",
                "generic",
                "--check",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn(
            "chapter 4 checks require the strict karman profile", result.stderr
        )

    def test_karman_default_profile_rejects_legacy_top_level_headings(self):
        with tempfile.TemporaryDirectory() as directory:
            study_dir = Path(directory)
            (study_dir / "VAK_4.17.md").write_text(
                "\n".join(
                    (
                        "## 1. Sanskrit (Devanāgarī)",
                        "## 2. Sanskrit (IAST)",
                        "## 3. Lexical Analysis",
                        "## 4. Grammar",
                        "## 5. Translation",
                        "## 6. Interpretation",
                        "## 7. Logical Determination",
                        "## 8. Textual Notes",
                    )
                ),
                encoding="utf-8",
            )
            (study_dir / "VAK_4.17_bhasya.md").write_text("", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    str(AUDIT_SCRIPT),
                    "--chapter",
                    "4",
                    "--study-dir",
                    str(study_dir),
                    "--start",
                    "17",
                    "--end",
                    "17",
                    "--check",
                ],
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(result.returncode, 1)
        self.assertIn("Checking headings with the karman profile", result.stdout)
        self.assertIn("noncanonical section heading", result.stdout)

    def test_full_karman_audit_checks_every_verse(self):
        result = subprocess.run(
            [
                sys.executable,
                str(AUDIT_SCRIPT),
                "--chapter",
                "4",
                "--check",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("127 of 127 requested", result.stdout)
        self.assertIn("Heading check: all requested studies conform", result.stdout)

    def test_shared_builder_dry_runs_every_edition_to_root_folder(self):
        verse_counts = {
            1: 48,
            2: 73,
            3: 102,
            4: 127,
            5: 70,
            6: 79,
            7: 56,
            8: 43,
        }
        for volume, karika_count in verse_counts.items():
            for kind in ("karika", "bhasya"):
                expected_count = (
                    38 if volume == 3 and kind == "bhasya" else karika_count
                )
                with self.subTest(volume=volume, kind=kind):
                    result = subprocess.run(
                        [
                            "bash",
                            str(BUILD_SCRIPT),
                            "--volume",
                            str(volume),
                            "--kind",
                            kind,
                            "--dry-run",
                        ],
                        capture_output=True,
                        text=True,
                        check=False,
                    )
                    self.assertEqual(
                        result.returncode, 0, result.stdout + result.stderr
                    )
                    self.assertIn(f"Sources: {expected_count} ", result.stdout)
                    output = next(
                        line.removeprefix("PDF: ")
                        for line in result.stdout.splitlines()
                        if line.startswith("PDF: ")
                    )
                    self.assertEqual(Path(output).parent, EDITIONS_DIR)
                    expected_suffix = (
                        "-Karika.pdf" if kind == "karika" else "-Bhasya.pdf"
                    )
                    self.assertTrue(output.endswith(expected_suffix), output)
                    self.assertNotIn("-Nirdesa.pdf", output)

    def test_shared_builder_accepts_a_partial_verse_range(self):
        result = subprocess.run(
            [
                "bash",
                str(BUILD_SCRIPT),
                "--volume",
                "4",
                "--kind",
                "karika",
                "--start",
                "1",
                "--end",
                "16",
                "--dry-run",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Sources: 16 (VAK 4.01–4.16)", result.stdout)


if __name__ == "__main__":
    unittest.main()
