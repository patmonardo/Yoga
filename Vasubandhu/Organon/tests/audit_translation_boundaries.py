"""Inventory translation-section boundaries in Organon chapters 1–4.

This is a triage audit, not a judgment that a translation is faithful.
"""

from collections import Counter
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = {int(path.name[:2]): path for path in ROOT.iterdir()
            if path.is_dir() and re.match(r"0[1-4]-", path.name)}


def section(text):
    match = re.search(r"^## 5\. Translation\s*$", text, re.M)
    if not match:
        return None
    return re.split(r"^## ", text[match.end():], maxsplit=1, flags=re.M)[0]


def subsections(text):
    matches = list(re.finditer(r"^### (.+)\s*$", text, re.M))
    return [(m.group(1).strip(), text[m.end():matches[i + 1].start() if i + 1 < len(matches) else len(text)].strip())
            for i, m in enumerate(matches)]


def classify(label):
    lower = label.lower()
    if lower.startswith("bhāṣya-informed"):
        return "informed"
    if lower.startswith(("literal", "close syntactic")):
        return "close"
    return "other"


def symptoms(body):
    lines = body.splitlines()
    quoted = [i for i, line in enumerate(lines) if line.lstrip().startswith(">")]
    if not quoted:
        return ["unquoted boundary"]
    if "\n".join(lines[max(quoted) + 1:]).strip():
        return ["prose after quote"]
    return []


def main():
    for chapter, directory in sorted(CHAPTERS.items()):
        files = sorted(p for p in directory.glob("VAK_*.md")
                       if not p.stem.endswith("_bhasya"))
        counts = Counter()
        examples = {}
        for path in files:
            found = section(path.read_text(encoding="utf-8"))
            if found is None:
                counts["missing section"] += 1
                examples.setdefault("missing section", path.name)
                continue
            groups = {}
            for label, body in subsections(found):
                groups[classify(label)] = body
            for kind in ("close", "informed"):
                if kind not in groups:
                    key = f"missing {kind}"
                    counts[key] += 1
                    examples.setdefault(key, path.name)
                    continue
                for symptom in symptoms(groups[kind]):
                    key = f"{kind}: {symptom}"
                    counts[key] += 1
                    examples.setdefault(key, path.name)
        print(f"Chapter {chapter}: {len(files)} kārikā studies")
        for key, count in sorted(counts.items()):
            print(f"  {key}: {count} (e.g. {examples[key]})")
        if not counts:
            print("  no boundary symptoms")


if __name__ == "__main__":
    main()
