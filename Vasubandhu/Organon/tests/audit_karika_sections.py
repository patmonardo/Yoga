"""Inventory or validate top-level headings in Organon kārikā studies."""

import argparse
from collections import defaultdict
from pathlib import Path
import re


ORGANON_DIR = Path(__file__).resolve().parents[1]
CHAPTER_DIRS = {
    1: "01-dhatu",
    2: "02-indriya",
    3: "03-loka",
    4: "04-karma",
    5: "05-anusaya",
    6: "06-marga",
    7: "07-jnana",
    8: "08-samapatti",
}
CHAPTER_ENDS = {1: 48, 2: 73, 3: 102, 4: 127, 5: 70, 6: 79, 7: 56, 8: 43}
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
KARMAN_SECTION_ORDER = SECTION_ORDER
HEADING = re.compile(r"^\s{0,3}(#{2,6})\s+(.+?)\s*#*\s*$")
FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
NUMBERED_HEADING = re.compile(r"^##\s+(\d+)\.\s+")


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
        if match and len(match.group(1)) == 2:
            headings.append(f"## {match.group(2).strip()}")

    return tuple(headings)


def heading_title(heading: str) -> str:
    title = heading.split(maxsplit=1)[1]
    return re.sub(r"^\d+\.\s*", "", title).strip()


def check_headings(
    headings: tuple[str, ...],
    profile: str = "dhatu",
    additional_required: tuple[str, ...] = (),
    additional_forbidden: tuple[str, ...] = (),
) -> list[str]:
    errors = []
    titles = [heading_title(heading) for heading in headings]

    for required in additional_required:
        if required not in titles:
            errors.append(f"missing requested section: {required}")
    for forbidden in additional_forbidden:
        if forbidden in titles:
            errors.append(f"forbidden section heading: {forbidden}")

    if profile == "generic":
        return errors

    if profile == "karman":
        for required in KARMAN_SECTION_ORDER:
            count = titles.count(required)
            if count == 0:
                errors.append(f"missing required section: {required}")
            elif count > 1:
                errors.append(f"duplicate section: {required}")

        for heading, title in zip(headings, titles):
            if title not in KARMAN_SECTION_ORDER:
                errors.append(f"noncanonical section heading: {heading}")
            if re.search(r"\bargument\b", title, re.IGNORECASE):
                errors.append(f"argument heading is not permitted: {heading}")

        if titles != list(KARMAN_SECTION_ORDER):
            errors.append("top-level sections do not match the Karman template")

        for index, heading in enumerate(headings, start=1):
            match = NUMBERED_HEADING.match(heading)
            if not match:
                errors.append(f"section lacks its number: {heading}")
            elif int(match.group(1)) != index:
                errors.append(f"section number is not sequential: {heading}")
        return errors

    for required in REQUIRED_SECTIONS:
        count = titles.count(required)
        if count == 0:
            errors.append(f"missing required section: {required}")
        elif count > 1:
            errors.append(f"duplicate section: {required}")

    if profile == "dhatu":
        canonical = []
        for heading, title in zip(headings, titles):
            if title not in SECTION_ORDER:
                errors.append(f"noncanonical section heading: {heading}")
                continue
            canonical.append((heading, title))

        positions = [SECTION_ORDER.index(title) for _, title in canonical]
        if positions != sorted(positions):
            errors.append("sections are not in Pattern 3 order")

        for heading, title in canonical:
            match = NUMBERED_HEADING.match(heading)
            if not match:
                errors.append(f"section lacks its canonical number: {heading}")
            elif int(match.group(1)) != SECTION_ORDER.index(title) + 1:
                errors.append(
                    f"section number does not match Pattern 3 order: {heading}"
                )
        for optional in SECTION_ORDER[len(REQUIRED_SECTIONS) :]:
            if titles.count(optional) > 1:
                errors.append(f"duplicate section: {optional}")
        return errors

    if titles[: len(REQUIRED_SECTIONS)] != list(REQUIRED_SECTIONS):
        errors.append("the first five sections must follow the Organon study order")

    for index, heading in enumerate(headings, start=1):
        match = NUMBERED_HEADING.match(heading)
        if not match:
            errors.append(f"section lacks its number: {heading}")
        elif int(match.group(1)) != index:
            errors.append(f"section number is not sequential: {heading}")

    return errors


def selected_profile(requested: str, chapter: int) -> str:
    if requested != "auto":
        return requested
    if chapter == 1:
        return "dhatu"
    if chapter == 4:
        return "karman"
    return "generic"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--chapter",
        type=int,
        choices=CHAPTER_DIRS,
        default=1,
        help="VAK chapter number (default: 1)",
    )
    parser.add_argument(
        "--study-dir",
        type=Path,
        help="study directory (defaults to the selected Organon chapter)",
    )
    parser.add_argument("--start", type=int, default=1, help="first verse (default: 1)")
    parser.add_argument(
        "--end",
        type=int,
        help="last verse (defaults to the chapter's current verse count)",
    )
    parser.add_argument(
        "--profile",
        choices=("auto", "dhatu", "karman", "generic"),
        default="auto",
        help="heading rules to apply (default: selected from chapter)",
    )
    parser.add_argument(
        "--require-section",
        action="append",
        default=[],
        help="require a top-level section title (may be repeated)",
    )
    parser.add_argument(
        "--forbid-section",
        action="append",
        default=[],
        help="reject a top-level section title (may be repeated)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail on missing paired files or heading-rule violations",
    )
    args = parser.parse_args()

    end = args.end if args.end is not None else CHAPTER_ENDS[args.chapter]
    if args.start < 1 or end < args.start:
        parser.error("--start must be positive and --end must not precede --start")

    study_dir = (
        args.study_dir.resolve()
        if args.study_dir
        else ORGANON_DIR / CHAPTER_DIRS[args.chapter]
    )
    profile = selected_profile(args.profile, args.chapter)
    if args.check and args.chapter == 4 and profile != "karman":
        parser.error("chapter 4 checks require the strict karman profile")
    studies = {}
    missing_karikas = []
    missing_bhasya = []
    violations = {}

    for verse in range(args.start, end + 1):
        stem = f"VAK_{args.chapter}.{verse:02d}"
        path = study_dir / f"{stem}.md"
        if not path.is_file():
            missing_karikas.append(verse)
            continue

        headings = headings_in(path)
        studies[verse] = (path, headings)
        if args.check:
            errors = check_headings(
                headings,
                profile,
                tuple(args.require_section),
                tuple(args.forbid_section),
            )
            if errors:
                violations[verse] = errors
        if not (study_dir / f"{stem}_bhasya.md").is_file():
            missing_bhasya.append(verse)

    print(
        f"Chapter {args.chapter} kārikā studies found: "
        f"{len(studies)} of {end - args.start + 1} requested"
    )
    if args.check:
        print(f"Checking headings with the {profile} profile.")
    else:
        patterns = defaultdict(list)
        for verse, (_, headings) in studies.items():
            patterns[headings].append(verse)
        print("Headings are grouped exactly as written; no template is enforced.")
        print(f"Distinct heading patterns: {len(patterns)}")

        for number, (headings, verses) in enumerate(
            sorted(patterns.items(), key=lambda item: (-len(item[1]), item[1][0])),
            start=1,
        ):
            print(f"\nPattern {number} ({len(verses)} studies):")
            for heading in headings:
                print(f"  {heading}")
            print(
                "  Verses: "
                + ", ".join(f"{args.chapter}.{verse:02d}" for verse in verses)
            )

    if missing_karikas:
        print(
            "\nMissing kārikā files: "
            + ", ".join(f"{args.chapter}.{verse:02d}" for verse in missing_karikas)
        )
    if missing_bhasya:
        print(
            "\nMissing paired Bhāṣya files: "
            + ", ".join(f"{args.chapter}.{verse:02d}" for verse in missing_bhasya)
        )

    if args.check and violations:
        print(f"\nHeading check: {len(violations)} nonconforming studies")
        for verse, errors in sorted(violations.items()):
            print(f"  VAK_{args.chapter}.{verse:02d}:")
            for error in errors:
                print(f"    - {error}")

    if args.check and (
        missing_karikas or missing_bhasya or violations or not studies
    ):
        return 1
    if args.check:
        if profile == "generic":
            print("\nStructural check: all requested studies conform.")
        else:
            print("\nHeading check: all requested studies conform.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
