"""Regression tests for kārikā anchors in paired Bhāṣya studies."""

import argparse
import os
from pathlib import Path
import re
import sys
import unittest

from audit_karika_sections import CHAPTER_DIRS, CHAPTER_ENDS


ORGANON_DIR = Path(__file__).resolve().parents[1]
CHAPTER = int(os.environ.get("ORGANON_VOLUME", "1"))
if CHAPTER not in CHAPTER_DIRS:
    raise ValueError(f"Unsupported ORGANON_VOLUME: {CHAPTER}")
STUDY_DIR = Path(
    os.environ.get(
        "ORGANON_STUDY_DIR",
        ORGANON_DIR / CHAPTER_DIRS[CHAPTER],
    )
)
START = int(os.environ.get("ORGANON_START", "1"))
END = int(os.environ.get("ORGANON_END", str(CHAPTER_ENDS[CHAPTER])))
TRANSLATION_MATCH = os.environ.get(
    "ORGANON_TRANSLATION_MATCH", "prefix" if CHAPTER == 4 else "exact"
)
if TRANSLATION_MATCH not in {"exact", "prefix"}:
    raise ValueError(
        "ORGANON_TRANSLATION_MATCH must be 'exact' or 'prefix'"
    )


def section(text: str, pattern: str) -> str:
    match = re.search(pattern, text, re.M)
    if not match:
        return ""
    tail = text[match.end() :]
    end = re.search(r"^## ", tail, re.M)
    return tail[: end.start()] if end else tail


def subsection(text: str, title: str) -> str:
    match = re.search(
        r"^### " + re.escape(title) + r"\s*$", text, re.M | re.I
    )
    if not match:
        return ""
    tail = text[match.end() :]
    end = re.search(r"^#{2,3} ", tail, re.M)
    return tail[: end.start()] if end else tail


def verse_text(text: str, chapter: int, verse: int) -> str:
    marker_pattern = rf"//\s*{chapter}\.0?{verse}\s*//"
    marker = re.search(marker_pattern, text)
    if not marker:
        return ""
    iast_block = re.search(r"```iast\s*(.*?)```", text, re.S | re.I)
    if iast_block:
        joined = iast_block.group(1)
    else:
        lines = text[: marker.end()].splitlines()
        joined = " ".join(
            quoted
            for line in lines
            if line.strip().startswith(">")
            if (
                quoted := re.sub(
                    marker_pattern, "", line.strip().lstrip(">")
                ).strip()
            )
        )
    joined = " ".join(re.sub(marker_pattern, "", joined).split())
    return re.sub(r"a-ā", "ā", joined).replace("-", "")


def normalized_block(text: str) -> str:
    return " ".join(
        line.strip().lstrip(">").strip()
        for line in text.splitlines()
        if line.strip().lstrip(">").strip()
    )


def quoted_block(text: str) -> str:
    return normalized_block(
        "\n".join(
            line for line in text.splitlines() if line.strip().startswith(">")
        )
    )


def anchor_translation(anchor: str, chapter: int, verse: int) -> str:
    explicit = subsection(anchor, "Bhāṣya-informed study translation")
    if explicit:
        return (
            quoted_block(explicit)
            if chapter == 3
            else normalized_block(explicit)
        )

    marker = re.search(rf"//\s*{chapter}\.0?{verse}\s*//", anchor)
    if not marker:
        return ""
    translation = []
    for line in anchor[marker.end() :].splitlines():
        stripped = line.strip()
        if stripped.startswith(">"):
            translation.append(stripped)
        elif translation and stripped:
            break
    return normalized_block("\n".join(translation))


class KarikaBhasyaAlignmentTests(unittest.TestCase):
    def test_bhasya_anchors_match_karika_verse_and_informed_translation(self):
        for verse in range(START, END + 1):
            stem = f"VAK_{CHAPTER}.{verse:02d}"
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
            )
            anchor = section(
                bhasya, r"^## 1\. Kārikā Anchor\s*$"
            )
            if CHAPTER == 3:
                informed_translation = quoted_block(informed_translation)
            else:
                informed_translation = normalized_block(informed_translation)
            anchor_translation_text = anchor_translation(
                anchor, CHAPTER, verse
            )

            with self.subTest(verse=verse):
                self.assertTrue(anchor, f"{stem} is missing its Kārikā Anchor")
                self.assertTrue(
                    informed_translation,
                    f"{stem} is missing its Bhāṣya-informed study translation",
                )
                self.assertEqual(
                    verse_text(anchor, CHAPTER, verse),
                    verse_text(karika_iast, CHAPTER, verse),
                    f"{stem} Bhāṣya anchor Sanskrit differs from the kārikā study",
                )
                self.assertTrue(
                    anchor_translation_text,
                    f"{stem} is missing its Bhāṣya anchor translation",
                )
                if TRANSLATION_MATCH == "prefix":
                    self.assertTrue(
                        informed_translation.startswith(anchor_translation_text),
                        f"{stem} kārikā study translation does not begin with "
                        "the Bhāṣya anchor translation",
                    )
                else:
                    self.assertEqual(
                        anchor_translation_text,
                        informed_translation,
                        f"{stem} Bhāṣya anchor translation differs from the "
                        "kārikā study's Bhāṣya-informed translation",
                    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chapter", type=int, choices=CHAPTER_DIRS)
    parser.add_argument("--study-dir", type=Path)
    parser.add_argument("--start", type=int)
    parser.add_argument("--end", type=int)
    parser.add_argument(
        "--translation-match", choices=("exact", "prefix")
    )
    args, unittest_args = parser.parse_known_args()

    if args.chapter is not None:
        CHAPTER = args.chapter
        if args.study_dir is None and "ORGANON_STUDY_DIR" not in os.environ:
            STUDY_DIR = ORGANON_DIR / CHAPTER_DIRS[CHAPTER]
        if args.end is None and "ORGANON_END" not in os.environ:
            END = CHAPTER_ENDS[CHAPTER]
        if "ORGANON_TRANSLATION_MATCH" not in os.environ:
            TRANSLATION_MATCH = "prefix" if CHAPTER == 4 else "exact"
    if args.study_dir is not None:
        STUDY_DIR = args.study_dir
    if args.start is not None:
        START = args.start
    if args.end is not None:
        END = args.end
    if args.translation_match is not None:
        TRANSLATION_MATCH = args.translation_match
    if START < 1 or END < START:
        parser.error("--start must be positive and --end must not precede --start")

    unittest.main(argv=[sys.argv[0], *unittest_args])
