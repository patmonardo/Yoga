"""Extract the 48 Dhatu studies into an editable, executable Jupyter notebook."""

import argparse
import json
from pathlib import Path
from textwrap import dedent

from audit_nltk_blocks import (
    BLOCK, ORGANON_DIR, check_grammar, check_logic, section,
)


DEFAULT_OUTPUT = ORGANON_DIR / "notebooks" / "dhatu-nltk.ipynb"
BLOCK_NAMES = {
    "nltk-fcfg": "fcfg_text",
    "nltk-dep": "dependency_text",
    "nltk-sem": "sem_text",
    "nltk-fol": "fol_text",
    "nltk-valuation": "valuation_text",
}

SETUP = dedent(r'''
    from pathlib import Path
    import re
    import sys

    from nltk.grammar import DependencyGrammar, FeatureGrammar
    from nltk.parse import FeatureChartParser
    from nltk.sem import Assignment, Expression, Model, Valuation

    # Use the same loader and strict checks as the source studies.
    for parent in (Path.cwd(), *Path.cwd().parents):
        candidates = (parent, parent / "Vasubandhu" / "Organon")
        organon = next(
            (p for p in candidates if (p / "tests" / "audit_nltk_blocks.py").is_file()),
            None,
        )
        if organon is not None:
            break
    else:
        raise FileNotFoundError("Run this notebook from inside the Yoga repository.")
    sys.path.insert(0, str(organon / "tests"))
    from audit_nltk_blocks import check_grammar, check_logic, load_valuation


    def satisfies(valuation, formula):
        """Evaluate one formula in a valuation, including an edited copy."""
        if isinstance(formula, str):
            formula = Expression.fromstring(formula)
        model = Model(valuation.domain, valuation)
        return model.satisfy(formula, Assignment(model.domain))


    def run_study(fcfg_text, dependency_text, sem_text, fol_text, valuation_text):
        """Check the edited blocks and expose the parse, theories, and model."""
        token_line = re.search(r"^# tokens: (.*)$", fcfg_text, re.M)
        if token_line is None:
            raise ValueError("The feature grammar needs a '# tokens:' line.")
        text = "## 3. Lexical Analysis\n" + token_line.group(0) + "\n"
        text += "## 4. Grammar\n"
        text += "```nltk-fcfg\n" + fcfg_text + "```\n"
        text += "```nltk-dep\n" + dependency_text + "```\n"
        text += "## 8. Logical Determination\n"
        text += "```nltk-sem\n" + sem_text + "```\n"
        text += "```nltk-fol\n" + fol_text + "```\n"
        text += "```nltk-valuation\n" + valuation_text + "```\n"
        grammar_summary, grammar_errors = check_grammar(text, strict=True)
        logic_summary, logic_errors = check_logic(text, strict=True)
        if grammar_errors or logic_errors:
            raise ValueError("\n".join(grammar_errors + logic_errors))

        tokens = token_line.group(1).split()
        grammar = FeatureGrammar.fromstring(fcfg_text)
        tree = next(FeatureChartParser(grammar).parse(tokens))
        theories = {}
        current = "default"
        for line in fol_text.splitlines():
            if line.startswith("# THEORY"):
                current = line.split()[2]
                theories.setdefault(current, [])
            elif line.strip() and not line.startswith("#"):
                theories.setdefault(current, []).append(Expression.fromstring(line))
        valuation = load_valuation(valuation_text)
        results = dict(item.split("=") for item in logic_summary.split())
        print(grammar_summary)
        print(logic_summary)
        return {
            "tokens": tokens,
            "grammar": grammar,
            "dependencies": DependencyGrammar.fromstring(dependency_text),
            "tree": tree,
            "sem": tree.label()["SEM"].simplify(),
            "theories": theories,
            "valuation": valuation,
            "model": Model(valuation.domain, valuation),
            "results": results,
        }


    studies = {}
''').lstrip()

EXPERIMENT = dedent('''
    original = studies[48]
    changed = Valuation(list(original["valuation"].items()))
    # Give Sound a third knower without changing the original valuation.
    changed["Knows"] = set(changed["Knows"]) | {("ecog_d", "sound_d")}
    before = satisfies(original["valuation"], original["sem"])
    after = satisfies(changed, original["sem"])
    print("Original verse:", before, "| With a third knower of Sound:", after)
    assert before is True and after is False
''').lstrip()


def cell(kind: str, source: str, identifier: str) -> dict:
    result = {
        "cell_type": kind,
        "id": identifier,
        "metadata": {},
        "source": source.splitlines(keepends=True),
    }
    if kind == "code":
        result.update(execution_count=None, outputs=[])
    return result


def build_notebook(study_dir: Path = ORGANON_DIR / "01-dhatu") -> dict:
    cells = [
        cell("markdown", dedent("""\
            # Dhātu: executable Grammar and Logic

            All 48 kārikās, extracted from the Organon studies. The Markdown
            studies remain authoritative; this notebook is an editable snapshot.
            Run with a Jupyter Python 3 kernel containing **NLTK**,
            from inside the Yoga repository. No NLTK corpus downloads are needed.
            Choose **Run All**, or run setup and then any individual study.

            Each study has editable source blocks followed by a checking cell.
            `studies[48]` (for example) exposes `tree`, `sem`, `theories`,
            `valuation`, `model`, `dependencies`, and `results`.
            These are finite-model checks, not general theorem proofs.
            The dependency grammar is loaded, but only its vocabulary is checked;
            this is not a dependency parse.

            Edit a valuation to explore countermodels. The checking cells enforce
            the source `# EXPECT` values; for intentional counterexamples use
            `satisfies(changed_valuation, formula)` as demonstrated at the end.
            Re-running setup clears `studies`; re-run the desired study cells.
            Regeneration replaces notebook edits, so save experiments separately.
            """), "introduction"),
        cell("code", SETUP, "setup"),
    ]
    for number in range(1, 49):
        path = study_dir / f"VAK_1.{number:02d}.md"
        text = path.read_text(encoding="utf-8")
        errors = check_grammar(text, strict=True)[1] + check_logic(text, strict=True)[1]
        if errors:
            raise ValueError(f"{path.name}: " + "; ".join(errors))
        blocks = BLOCK.findall(section(text, 4)) + BLOCK.findall(section(text, 8))
        for kind in BLOCK_NAMES:
            if sum(found == kind for found, _ in blocks) != 1:
                raise ValueError(f"{path.name}: expected exactly one {kind} block")
        if any(kind not in BLOCK_NAMES for kind, _ in blocks):
            raise ValueError(f"{path.name}: unsupported NLTK block")
        context = text.splitlines()[0] + "\n\n"
        context += f"Source: `{path.name}` in the Organon Dhātu chapter.\n\n"
        context += "\n\n".join(section(text, n).strip() for n in (2, 3, 5, 7))
        cells.append(cell("markdown", context, f"verse-{number:02d}-context"))
        for kind, body in blocks:
            if '"""' in body:
                raise ValueError(f"{path.name}: triple quote in {kind}")
        source = "\n".join(
            f'{BLOCK_NAMES[kind]} = r"""' + body + '"""\n'
            for kind, body in blocks
        )
        cells.append(cell("code", source, f"verse-{number:02d}-blocks"))
        cells.append(cell("code", (
            f"studies[{number}] = run_study(\n"
            "    fcfg_text, dependency_text, sem_text, fol_text, valuation_text\n"
            ")\n"
            f'print(studies[{number}]["tree"].pformat())\n'
            f'print("Derived SEM:", studies[{number}]["sem"])\n'
        ), f"verse-{number:02d}-run"))
    cells.extend([
        cell("markdown", (
            "## Countermodel playground: 1.48\n\n"
            "Copy the valuation, then give Sound a third Cognition that knows it. "
            "The derived verse becomes false. Unary predicate extensions use "
            "1-tuples, e.g. `{('space_u',)}`; binary relations use pairs. "
            "Copy a relation's set before editing it so the original stays intact."
        ), "countermodel-context"),
        cell("code", EXPERIMENT, "countermodel"),
    ])
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--force", action="store_true", help="replace an existing notebook")
    args = parser.parse_args()
    if args.output.exists() and not args.force:
        parser.error(f"{args.output} already exists; use --force to replace it")
    notebook = build_notebook()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w" if args.force else "x", encoding="utf-8") as output:
        json.dump(notebook, output, ensure_ascii=False, indent=1)
        output.write("\n")
    print(f"Wrote 48 studies ({len(notebook['cells'])} cells) to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
