"""Inventory or validate Bhāṣya section headings against the Organon Method."""

import argparse
from collections import Counter
from pathlib import Path
import re

from audit_karika_sections import (
    CHAPTER_DIRS,
    CHAPTER_ENDS,
    ORGANON_DIR,
    heading_title,
    headings_in,
)


NUMBERED = re.compile(r"^## (\d+)\. (.+)$")


def check_headings(headings: tuple[str, ...]) -> list[str]:
    errors = []
    if not headings:
        return ["no top-level Bhāṣya sections"]

    for index, heading in enumerate(headings, start=1):
        match = NUMBERED.fullmatch(heading)
        if not match:
            errors.append(f"section {index} lacks a number: {heading}")
        elif int(match.group(1)) != index:
            errors.append(f"section {index} has number {match.group(1)}: {heading}")

    titles = [heading_title(heading) for heading in headings]
    required = {
        0: "Kārikā Anchor",
        2: "Continuous Conventional Translation",
    }
    for index, title in required.items():
        if len(titles) <= index or titles[index] != title:
            errors.append(f"section {index + 1} must be {title}")
    if len(titles) < 2 or not titles[1].startswith("Continuous Sanskrit"):
        errors.append("section 2 must be Continuous Sanskrit")
    if len(headings) < 5:
        errors.append("Bhāṣya needs argument, study, and review sections after the opening three")
    if titles[-1] != "Review Status":
        errors.append("final section must be numbered Review Status")
    return errors


def check_anchor(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## 1\. Kārikā Anchor\s*$", text, re.M)
    if not match:
        return []  # The heading check reports the missing first section.
    next_section = re.search(r"^## ", text[match.end():], re.M)
    anchor = text[match.end():match.end() + next_section.start()] if next_section else text[match.end():]
    errors = []
    if re.search(r"^###\s+", anchor, re.M):
        errors.append("Kārikā Anchor must have no translation subheading")
    quoted_groups = re.findall(r"(?:^>.*(?:\n|$))+", anchor, re.M)
    if len(quoted_groups) != 2:
        errors.append("Kārikā Anchor needs one Sanskrit quote and one English quote")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chapter", type=int, choices=CHAPTER_DIRS, default=1)
    parser.add_argument("--study-dir", type=Path)
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int)
    parser.add_argument("--check", action="store_true", help="fail on missing files or Method violations")
    args = parser.parse_args()

    end = args.end if args.end is not None else CHAPTER_ENDS[args.chapter]
    if args.start < 1 or end < args.start:
        parser.error("--start must be positive and --end must not precede --start")
    study_dir = args.study_dir.resolve() if args.study_dir else ORGANON_DIR / CHAPTER_DIRS[args.chapter]

    patterns = Counter()
    failures = 0
    checked = 0
    for verse in range(args.start, end + 1):
        path = study_dir / f"VAK_{args.chapter}.{verse:02d}_bhasya.md"
        if not path.is_file():
            failures += 1
            if args.check:
                print(f"{path.name}: missing file")
            continue
        checked += 1
        headings = headings_in(path)
        patterns[headings] += 1
        if args.check:
            errors = check_headings(headings) + check_anchor(path)
            if errors:
                failures += 1
                for error in errors:
                    print(f"{path.name}: {error}")

    if args.check:
        print(f"Chapter {args.chapter} Bhāṣya: {checked} checked, {failures} failing")
    else:
        print(f"Chapter {args.chapter} Bhāṣya: {checked} files, {failures} missing")
        print(f"Distinct section patterns: {len(patterns)}")
        for headings, count in patterns.most_common():
            print(f"  {count} file(s): {' | '.join(headings)}")
    return 1 if args.check and failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
