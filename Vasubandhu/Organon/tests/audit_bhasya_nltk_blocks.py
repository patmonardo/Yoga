#!/usr/bin/env python3
"""Audit selected executable Grammar and Logic blocks in Indriya Bhāṣya studies."""

import argparse
from pathlib import Path

from audit_nltk_blocks import check_grammar, check_logic


def audit(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    grammar_marker = "### Grammar of the Bhāṣya determination"
    logic_marker = "### Logic of the Bhāṣya argument"
    if grammar_marker not in text or logic_marker not in text:
        return ["missing Bhāṣya Grammar or Logic heading"]
    grammar_part = text.split(grammar_marker, 1)[1].split(logic_marker, 1)[0]
    logic_part = text.split(logic_marker, 1)[1].split("## 5. Review Status", 1)[0]
    token_lines = [line for line in grammar_part.splitlines() if line.startswith("# tokens:")]
    if not token_lines:
        return ["missing normalized Bhāṣya tokens"]
    synthetic = (
        "## 3. Lexical Analysis\n\n```text\n"
        + token_lines[0]
        + "\n```\n\n## 4. Grammar\n"
        + grammar_part
        + "\n## 8. Logical Determination\n"
        + logic_part
        + "\n## 9. Interpretive Note\n"
    )
    grammar_result, grammar_errors = check_grammar(synthetic, strict=True)
    logic_result, logic_errors = check_logic(synthetic, strict=True)
    print(f"{path.name} grammar: {grammar_result} logic: {logic_result}")
    return grammar_errors + logic_errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--study", type=Path, required=True)
    args = parser.parse_args()
    errors = audit(args.study)
    for error in errors:
        print(f"  ERROR: {error}")
    print(f"{len(errors)} failing")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
