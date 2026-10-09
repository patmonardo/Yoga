"""Audit the YS source, paired study scaffolds, and drafted sūtra anchors.

Run: python3 Patanjali/YS/tests/audit_ys.py
"""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / "Sources" / "Yoga.txt"
CHAPTERS = {1: "01-prajna", 2: "02-kriya", 3: "03-jnana", 4: "04-dharma"}
ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV"}
DEVANAGARI = str.maketrans("०१२३४५६७८९", "0123456789")
MARKER = re.compile(r"॥\s*([१-४])\.([०-९]+)॥")
FILENAME = re.compile(r"YS-(I|II|III|IV)\.(\d{2})(_bhasya)?\.md$")
SOURCE_QUOTE = re.compile(r"^>\s*(.+?॥\s*[१-४]\.[०-९]+॥)\s*$", re.M)
SUTRA_HEADINGS = (
    "1. Sanskrit (Devanāgarī)",
    "2. Sanskrit (IAST)",
    "3. Lexical Analysis",
    "4. Grammar",
    "5. Translation",
    "6. Logical Determination",
    "7. Interpretive Note",
)
BHASYA_HEADINGS = (
    "1. Sūtra Anchor",
    "2. Commentary",
    "3. Project Determination",
    "4. Review Status",
)


def normalized(text: str) -> str:
    return " ".join(re.sub(r"\s*॥", "॥", text).split())


def headings(text: str) -> tuple[str, ...]:
    """Return level-two headings outside fenced code blocks."""
    found = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None and line.startswith("## "):
            found.append(line[3:].strip())
    return tuple(found)


def source_inventory(text: str) -> dict[tuple[int, int], str]:
    """Collect sūtras across wrapped lines, stripping chapter matter at markers."""
    inventory = {}
    start = 0
    for match in MARKER.finditer(text):
        chapter = int(match.group(1).translate(DEVANAGARI))
        verse = int(match.group(2).translate(DEVANAGARI))
        # A source sūtra may wrap. Earlier colophons/headings end in ॥.
        prefix = text[start : match.start()]
        # The source places parenthetical variant readings after some markers;
        # they belong to the preceding sūtra, not the following anchor.
        prefix = re.sub(r"^\s*\([^)]*\)\s*", "", prefix)
        body = prefix.rsplit("॥", 1)[-1].strip() + " " + match.group(0)
        key = (chapter, verse)
        if key in inventory:
            raise ValueError(f"duplicate source marker {chapter}.{verse}")
        inventory[key] = normalized(body)
        start = match.end()
    return inventory


def audit() -> list[str]:
    errors = []
    try:
        source = source_inventory(SOURCE.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return [f"source: {exc}"]

    if not source:
        return ["source: no numbered sūtras found"]
    expected = set()
    for chapter in CHAPTERS:
        numbers = sorted(verse for number, verse in source if number == chapter)
        if not numbers or numbers != list(range(1, numbers[-1] + 1)):
            errors.append(f"source chapter {chapter}: numbering has a gap")
        for verse in numbers:
            stem = f"YS-{ROMAN[chapter]}.{verse:02d}"
            folder = ROOT / CHAPTERS[chapter]
            for suffix in ("", "_bhasya"):
                expected.add(folder / f"{stem}{suffix}.md")

            study = folder / f"{stem}.md"
            commentary = folder / f"{stem}_bhasya.md"
            if not study.is_file() or not commentary.is_file():
                continue
            a = study.read_text(encoding="utf-8")
            b = commentary.read_text(encoding="utf-8")
            if bool(a.strip()) != bool(b.strip()):
                errors.append(f"{stem}: only one file in the pair is drafted")
            if not a.strip():
                continue
            quote = SOURCE_QUOTE.search(a)
            if not quote:
                errors.append(f"{stem}: missing Devanāgarī source quotation")
            elif normalized(quote.group(1)) != source[chapter, verse]:
                errors.append(f"{stem}: source quotation differs from Yoga.txt")
            if not re.search(rf"^# YS {ROMAN[chapter]}\.{verse}\b", a, re.M):
                errors.append(f"{stem}: study title has wrong verse number")
            if not re.search(rf"^# YS {ROMAN[chapter]}\.{verse}\b", b, re.M):
                errors.append(f"{stem}: commentary title has wrong verse number")
            if headings(a) != SUTRA_HEADINGS:
                errors.append(f"{stem}: sūtra headings differ from the required order: {headings(a)}")
            if headings(b) != BHASYA_HEADINGS:
                errors.append(f"{stem}: Bhāṣya headings differ from the required order: {headings(b)}")
            bhasya_quote = SOURCE_QUOTE.search(b)
            if not bhasya_quote or normalized(bhasya_quote.group(1)) != source[chapter, verse]:
                errors.append(f"{stem}: commentary source anchor differs from Yoga.txt")

    actual = set()
    for folder in CHAPTERS.values():
        for path in (ROOT / folder).glob("*.md"):
            if FILENAME.fullmatch(path.name):
                actual.add(path)
            else:
                errors.append(f"unexpected study filename: {path.relative_to(ROOT)}")
    for path in sorted(expected - actual):
        errors.append(f"missing study file: {path.relative_to(ROOT)}")
    for path in sorted(actual - expected):
        errors.append(f"study file has no source marker: {path.relative_to(ROOT)}")
    drafted = sum(
        bool((ROOT / CHAPTERS[ch] / f"YS-{ROMAN[ch]}.{v:02d}.md").read_text(encoding="utf-8").strip())
        for ch, v in source
        if (ROOT / CHAPTERS[ch] / f"YS-{ROMAN[ch]}.{v:02d}.md").is_file()
    )
    print(f"YS source: {len(source)} sūtras; study files: {len(actual)}/{len(expected)}; drafted pairs: {drafted}")
    return errors


if __name__ == "__main__":
    problems = audit()
    for problem in problems:
        print(f"ERROR: {problem}", file=sys.stderr)
    raise SystemExit(bool(problems))
