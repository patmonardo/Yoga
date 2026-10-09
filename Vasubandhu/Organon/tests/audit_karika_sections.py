"""Inventory section headings in the Dhatu Karika studies."""

import argparse
from collections import defaultdict
from pathlib import Path
import re


STUDY_DIR = Path(__file__).resolve().parents[1] / "01-dhatu"
KARIKA_FILENAME = re.compile(r"^VAK_1\.(\d{2})\.md$")
HEADING = re.compile(r"^\s{0,3}(#{2,6})\s+(.+?)\s*#*\s*$")
FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
SECTION_ORDER = (
    "Sanskrit (Devanāgarī)",
    "Sanskrit (IAST)",
    "Lexical Analysis",
    "Grammar",
    "Translation",
    "Philosophical Translation",
    "Technical Vocabulary",
    "Logical Determination",
    "Interpretive Note",
    "OWL++ Seed",
)
REQUIRED_SECTIONS = SECTION_ORDER[:5]
SECTION_ALIASES = {
    "Sanskrit (Devanagari)": "Sanskrit (Devanāgarī)",
    "Grammar and Classification": "Grammar",
    "Grammar and Eightfold View": "Grammar",
    "Literal Translation": "Translation",
    "Conventional Translation": "Translation",
    "Philosophical Translation and Techne Reading": "Philosophical Translation",
    "Interpretation": "Interpretive Note",
    "Vocabulary": "Technical Vocabulary",
}
TRANSLATION_ORDER = (
    "Literal Translation",
    "Bhāṣya-informed study translation",
)
TRANSLATION_ALIASES = {
    "Close syntactic construe": "Literal Translation",
    "Close translation": "Literal Translation",
    "Literal": "Literal Translation",
    "Conventional translation": "Literal Translation",
    "Bhāṣya-informed translation": "Bhāṣya-informed study translation",
    "Bhāṣya-informed": "Bhāṣya-informed study translation",
    "Commentary-informed translation": "Bhāṣya-informed study translation",
}


def headings_in(path: Path) -> tuple[str, ...]:
    headings = []
    fence_char = None
    fence_size = 0

    for line in path.read_text(encoding="utf-8").splitlines():
        fence = FENCE.match(line)
        if fence:
            marker = fence.group(1)
            if fence_char is None:
                fence_char = marker[0]
                fence_size = len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_size:
                fence_char = None
                fence_size = 0
            continue
        if fence_char is not None:
            continue

        match = HEADING.match(line)
        if match:
            level = len(match.group(1))
            headings.append(f"{'#' * level} {match.group(2).strip()}")

    return tuple(headings)


def heading_level(heading: str) -> int:
    return len(heading.split(maxsplit=1)[0])


def heading_title(heading: str) -> str:
    return re.sub(r"^\d+\.\s*", "", heading.split(maxsplit=1)[1]).strip()


def canonical_section(title: str) -> str:
    return SECTION_ALIASES.get(title, title)


def canonical_translation(title: str) -> str:
    return TRANSLATION_ALIASES.get(title, title)


def check_headings(headings: tuple[str, ...]) -> list[str]:
    errors = []
    sections = [heading for heading in headings if heading_level(heading) == 2]
    canonical = []
    for heading in sections:
        title = heading_title(heading)
        section = canonical_section(title)
        if section not in SECTION_ORDER:
            errors.append(f"noncanonical section heading: {heading}")
            continue
        canonical.append((heading, section))

    present = [section for _, section in canonical]
    for required in REQUIRED_SECTIONS:
        if present.count(required) == 0:
            errors.append(f"missing required section: {required}")
        elif present.count(required) > 1:
            errors.append(f"duplicate section: {required}")
    for optional in SECTION_ORDER[len(REQUIRED_SECTIONS) :]:
        if present.count(optional) > 1:
            errors.append(f"duplicate section: {optional}")

    positions = [SECTION_ORDER.index(section) for _, section in canonical]
    if positions != sorted(positions):
        errors.append("sections are not in Pattern 3 order")

    for heading, section in canonical:
        match = re.match(r"##\s+(\d+)\.\s+", heading)
        if not match:
            errors.append(f"section lacks its canonical number: {heading}")
        elif int(match.group(1)) != SECTION_ORDER.index(section) + 1:
            errors.append(
                f"section number does not match Pattern 3 order: {heading}"
            )

    if present.count("Translation") != 1:
        errors.append("expected exactly one Translation section")
        return errors

    translation_subsections = []
    in_translation = False
    for heading in headings:
        if heading_level(heading) == 2:
            if in_translation:
                break
            if canonical_section(heading_title(heading)) == "Translation":
                in_translation = True
        elif heading_level(heading) == 3 and in_translation:
            title = heading_title(heading)
            canonical_title = canonical_translation(title)
            if canonical_title not in TRANSLATION_ORDER:
                errors.append(f"noncanonical translation subsection: {heading}")
            else:
                translation_subsections.append(canonical_title)

    if translation_subsections != list(TRANSLATION_ORDER):
        errors.append("translation subsections are not in the required order")
    for required in TRANSLATION_ORDER:
        if translation_subsections.count(required) == 0:
            errors.append(f"missing translation subsection: {required}")
        elif translation_subsections.count(required) > 1:
            errors.append(f"duplicate translation subsection: {required}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail on deviations from the Pattern 3 section order",
    )
    args = parser.parse_args()

    studies = {}
    missing_bhasya = []
    violations = {}

    for path in sorted(STUDY_DIR.glob("VAK_1.*.md")):
        match = KARIKA_FILENAME.match(path.name)
        if not match:
            continue
        verse = int(match.group(1))
        headings = headings_in(path)
        studies[verse] = (path, headings)
        if args.check:
            errors = check_headings(headings)
            if errors:
                violations[verse] = errors
        if not (STUDY_DIR / f"VAK_1.{verse:02d}_bhasya.md").is_file():
            missing_bhasya.append(verse)

    patterns = defaultdict(list)
    for verse, (_, headings) in studies.items():
        patterns[headings].append(verse)

    expected_verses = set(range(1, 49))
    missing_karikas = sorted(expected_verses - studies.keys())

    print(f"Dhatu Karika studies found: {len(studies)}")
    if args.check:
        print("Checking against the Pattern 3 section order.")
    else:
        print("Headings are grouped exactly as written; no template is enforced.")
        print(f"Distinct heading patterns: {len(patterns)}")

        for number, (headings, verses) in enumerate(
            sorted(patterns.items(), key=lambda item: (-len(item[1]), item[1][0])),
            start=1,
        ):
            print(f"\nPattern {number} ({len(verses)} studies):")
            for heading in headings:
                print(f"  {heading}")
            print("  Verses: " + ", ".join(f"1.{verse:02d}" for verse in verses))

    if missing_karikas:
        print(
            "\nMissing Karika files: "
            + ", ".join(f"1.{verse:02d}" for verse in missing_karikas)
        )
    if missing_bhasya:
        print(
            "\nMissing paired Bhasya files: "
            + ", ".join(f"1.{verse:02d}" for verse in missing_bhasya)
        )

    if args.check:
        if violations:
            print(f"\nPattern 3 section check: {len(violations)} nonconforming studies")
            for verse, errors in sorted(violations.items()):
                print(f"  VAK_1.{verse:02d}:")
                for error in errors:
                    print(f"    - {error}")
            return 1
        print("\nPattern 3 section check: all studies conform.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
