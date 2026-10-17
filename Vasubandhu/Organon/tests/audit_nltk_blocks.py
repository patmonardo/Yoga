"""Validate the NLTK fenced blocks in Organon kārikā studies.

Section 4 (Grammar) must hold one ``nltk-fcfg`` block and one ``nltk-dep``
block. The feature grammar carries a ``# tokens:`` line and must parse those
tokens exactly once. Section 8 (Logical Determination) may hold ``nltk-sem``,
``nltk-fol`` and ``nltk-valuation`` blocks. Every formula must parse, every
predicate and constant must be declared in the valuation, and each
``# THEORY name`` is reported as true (T) or false (F) in the valuation.
Requires NLTK. Usage:

    python Vasubandhu/Organon/tests/audit_nltk_blocks.py --chapter 8 \
        --start 1 --end 43 [--grammar-only | --logic-only]
"""

import argparse
from pathlib import Path
import re
import sys

from nltk.grammar import DependencyGrammar, FeatureGrammar
from nltk.parse import FeatureChartParser
from nltk.sem import Assignment, Expression, Model, Valuation

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_karika_sections import CHAPTER_DIRS, CHAPTER_ENDS, ORGANON_DIR  # noqa: E402

BLOCK = re.compile(r"```(nltk-[a-z]+)\n(.*?)```", re.S)


def section(text: str, number: int) -> str:
    match = re.search(rf"^## {number}\. .*?(?=^## \d+\. |\Z)", text, re.S | re.M)
    return match.group(0) if match else ""


def formulas(block: str):
    for line in block.splitlines():
        if line.strip() and not line.startswith("#"):
            yield line.strip()


def check_grammar(text: str) -> tuple[str, list[str]]:
    blocks = BLOCK.findall(section(text, 4))
    fcfg = [body for kind, body in blocks if kind == "nltk-fcfg"]
    dep = [body for kind, body in blocks if kind == "nltk-dep"]
    if len(fcfg) != 1 or len(dep) != 1:
        return "", ["section 4 needs exactly one nltk-fcfg and one nltk-dep block"]
    try:
        grammar = FeatureGrammar.fromstring(fcfg[0])
        DependencyGrammar.fromstring(dep[0])
    except Exception as exc:
        return "", [f"grammar load: {str(exc)[:100]}"]
    tokens = re.search(r"^# tokens: (.*)$", fcfg[0], re.M)
    if not tokens:
        return "", ["nltk-fcfg lacks a '# tokens:' line"]
    count = len(list(FeatureChartParser(grammar).parse(tokens.group(1).split())))
    return f"parses {count}", ([] if count == 1 else [f"expected 1 parse, got {count}"])


def check_logic(text: str) -> tuple[str, list[str]]:
    errors, theories, valuation, current = [], {}, None, "default"
    for kind, body in BLOCK.findall(section(text, 8)):
        try:
            if kind == "nltk-valuation":
                valuation = Valuation.fromstring(body)
            elif kind == "nltk-fol":
                for line in body.splitlines():
                    if line.startswith("# THEORY"):
                        current = line.split()[2]
                        theories.setdefault(current, [])
                    elif line.strip() and not line.startswith("#"):
                        theories.setdefault(current, []).append(
                            Expression.fromstring(line.strip())
                        )
            elif kind == "nltk-sem":
                for line in formulas(body):
                    Expression.fromstring(
                        line.split(" : ", 1)[1].strip() if " : " in line else line
                    ).simplify()
            else:
                errors.append(f"unknown block {kind}")
        except Exception as exc:
            errors.append(f"{kind}: {str(exc)[:100]}")
    if not theories:
        errors.append("no nltk-fol theory")
    if valuation is None:
        errors.append("no nltk-valuation block")
    if errors:
        return "", errors
    model, assignment = Model(valuation.domain, valuation), Assignment(valuation.domain)
    result = {}
    for name, rules in theories.items():
        try:
            result[name] = "T" if all(model.satisfy(r, assignment) for r in rules) else "F"
        except Exception as exc:
            errors.append(f"theory {name}: {str(exc)[:100]}")
    return " ".join(f"{k}={v}" for k, v in result.items()), errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--chapter", type=int, default=8, choices=sorted(CHAPTER_DIRS))
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int)
    parser.add_argument("--grammar-only", action="store_true")
    parser.add_argument("--logic-only", action="store_true")
    args = parser.parse_args()
    end = args.end or CHAPTER_ENDS[args.chapter]
    folder = ORGANON_DIR / CHAPTER_DIRS[args.chapter]
    failing = 0
    for number in range(args.start, end + 1):
        path = folder / f"VAK_{args.chapter}.{number:02d}.md"
        text = path.read_text(encoding="utf-8")
        parts, errors = [], []
        for label, run, skip in (
            ("grammar", check_grammar, args.logic_only),
            ("logic", check_logic, args.grammar_only),
        ):
            if skip:
                continue
            summary, errs = run(text)
            parts.append(f"{label}: {summary}" if summary else label)
            errors += errs
        failing += bool(errors)
        print(f"{args.chapter}.{number:02d}", *parts, "ERR " + "; ".join(errors) if errors else "ok")
    print(f"{failing} failing")
    return 1 if failing else 0


if __name__ == "__main__":
    raise SystemExit(main())
