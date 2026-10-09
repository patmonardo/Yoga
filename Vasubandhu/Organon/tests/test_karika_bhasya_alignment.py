"""Regression tests for kārikā anchors in paired Bhāṣya studies."""

from pathlib import Path
import re
import unittest


STUDY_DIR = Path(__file__).resolve().parents[1] / "01-dhatu"


def section(text: str, pattern: str) -> str:
    match = re.search(pattern, text, re.M)
    if not match:
        return ""
    tail = text[match.end() :]
    end = re.search(r"^## ", tail, re.M)
    return tail[: end.start()] if end else tail


def subsection(text: str, title: str) -> str:
    match = re.search(r"^### " + re.escape(title) + r"\s*$", text, re.M)
    if not match:
        return ""
    tail = text[match.end() :]
    end = re.search(r"^#{2,3} ", tail, re.M)
    return tail[: end.start()] if end else tail


def verse_text(text: str, verse: int) -> str:
    marker = re.search(r"//\s*1\." + f"{verse:02d}" + r"\s*//", text)
    if not marker:
        return ""
    lines = text[: marker.end()].splitlines()
    return "\n".join(line for line in lines if line.strip().startswith(">")).strip()


class KarikaBhasyaAlignmentTests(unittest.TestCase):
    def test_bhasya_anchors_match_karika_verse_and_informed_translation(self):
        for verse in range(1, 49):
            stem = f"VAK_1.{verse:02d}"
            karika = (STUDY_DIR / f"{stem}.md").read_text(encoding="utf-8")
            bhasya = (STUDY_DIR / f"{stem}_bhasya.md").read_text(
                encoding="utf-8"
            )
            karika_iast = section(
                karika, r"^## 2\. Sanskrit \(IAST\)\s*$"
            )
            translation = section(karika, r"^## 5\. Translation\s*$")
            informed_translation = subsection(
                translation, "Bhāṣya-informed study translation"
            ).strip()
            anchor = section(
                bhasya, r"^## 1\. Kārikā Anchor\s*$"
            )
            anchor_translation = subsection(
                anchor, "Bhāṣya-informed study translation"
            ).strip()

            with self.subTest(verse=verse):
                self.assertTrue(anchor, f"{stem} is missing its Kārikā Anchor")
                self.assertTrue(
                    informed_translation,
                    f"{stem} is missing its Bhāṣya-informed study translation",
                )
                self.assertEqual(
                    verse_text(anchor, verse),
                    verse_text(karika_iast, verse),
                    f"{stem} Bhāṣya anchor Sanskrit differs from the kārikā study",
                )
                self.assertEqual(
                    anchor_translation,
                    informed_translation,
                    f"{stem} Bhāṣya anchor translation differs from the "
                    "kārikā study's Bhāṣya-informed translation",
                )


if __name__ == "__main__":
    unittest.main()
