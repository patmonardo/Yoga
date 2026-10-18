"""Executable grammar, semantic scope, and countermodels for VAK 1.01–1.03."""

from pathlib import Path
import re
import unittest

from nltk.grammar import FeatureGrammar
from nltk.parse import FeatureChartParser
from nltk.sem import Assignment, Expression, Model, Valuation

from audit_nltk_blocks import BLOCK, check_grammar, check_logic, load_valuation, section


STUDIES = Path(__file__).resolve().parents[1] / "01-dhatu"


def study(number):
    return (STUDIES / f"VAK_1.{number:02d}.md").read_text(encoding="utf-8")


def grammar_block(text):
    return next(body for kind, body in BLOCK.findall(section(text, 4))
                if kind == "nltk-fcfg")


def parse(text):
    block = grammar_block(text)
    tokens = re.search(r"^# tokens: (.*)$", block, re.M).group(1).split()
    return list(FeatureChartParser(FeatureGrammar.fromstring(block)).parse(tokens))


def valuation_and_formula(number):
    text = study(number)
    blocks = dict(BLOCK.findall(section(text, 8)))
    valuation = load_valuation(blocks["nltk-valuation"])
    formula = Expression.fromstring(next(
        line for line in blocks["nltk-fol"].splitlines()
        if line.strip() and not line.startswith("#")
    ))
    return valuation, formula


def satisfies(valuation, formula):
    model = Model(valuation.domain, valuation)
    return model.satisfy(formula, Assignment(model.domain))


class DhatuPilotTests(unittest.TestCase):
    def test_pilot_passes_strict_audit_and_semantic_typecheck(self):
        for number in (1, 2, 3):
            with self.subTest(verse=number):
                text = study(number)
                self.assertEqual(check_grammar(text, strict=True)[1], [])
                self.assertEqual(check_logic(text, strict=True), ("verse=T", []))
                semantics = parse(text)[0].label()["SEM"].simplify()
                semantics.typecheck()
                self.assertEqual(semantics.free(), set())
                self.assertEqual(str(semantics.type), "t")

    def test_agreement_changes_are_rejected(self):
        changes = (
            (1, "ADJ[CASE=nom,NUM=sg,GEN=m,SEM=",
             "ADJ[CASE=nom,NUM=pl,GEN=m,SEM="),
            (2, "ADJ[K=stainless,CASE=nom,NUM=sg,GEN=f,SEM=",
             "ADJ[K=stainless,CASE=nom,NUM=sg,GEN=m,SEM="),
            (3, "WORK[CASE=nom,NUM=sg,GEN=m,READING=conjecture,SEM=",
             "WORK[CASE=nom,NUM=sg,GEN=n,READING=conjecture,SEM="),
        )
        for number, before, after in changes:
            with self.subTest(verse=number):
                text = study(number)
                self.assertIn(before, text)
                self.assertEqual(parse(text.replace(before, after)), [])

    def test_supplied_prajna_cannot_be_silently_omitted(self):
        block = grammar_block(study(2))
        tokens = re.search(r"^# tokens: (.*)$", block, re.M).group(1).split()
        tokens.remove("∅-prajñā")
        grammar = FeatureGrammar.fromstring(block)
        self.assertEqual(list(FeatureChartParser(grammar).parse(tokens)), [])

    def test_annotation_and_dependency_mismatches_fail(self):
        text = study(1)
        changed = text.replace("# tokens: yaḥ", "# tokens: tasmai", 1)
        self.assertIn("token annotation", " ".join(check_grammar(changed, strict=True)[1]))
        changed = text.replace("'tasmai' -> 'yathārtha-śāstre'",
                               "'tasmai' -> 'not_a_token'")
        errors = " ".join(check_grammar(changed, strict=True)[1])
        self.assertIn("dependency token mismatch", errors)
        self.assertIn("not_a_token", errors)

    def test_changed_semantics_cannot_keep_old_section_8(self):
        text = study(3).replace(
            r"NEG[SEM=<\P.\x.-P(x)>]", r"NEG[SEM=<\P.\x.P(x)>]"
        )
        errors = check_grammar(text, strict=True)[1]
        self.assertIn("derived SEM", " ".join(errors))

    def test_root_sem_must_be_reused_in_theory_not_just_sem_block(self):
        text = study(1).replace(
            "# EXPECT verse T\nexists x.", "# EXPECT verse T\n-exists x."
        )
        self.assertIn("reused", " ".join(check_grammar(text, strict=True)[1]))

    def test_malformed_section_8_is_reported_not_ignored(self):
        text = study(1).replace(
            "# derived by the section 4 parse\n",
            "# derived by the section 4 parse\nBogus(\n",
        )
        self.assertIn("nltk-sem:", " ".join(check_grammar(text, strict=True)[1]))
        self.assertIn("nltk-sem:", " ".join(check_logic(text, strict=True)[1]))

    def test_empty_theory_does_not_pass_vacuously(self):
        text = re.sub(
            r"```nltk-fol\n.*?```",
            "```nltk-fol\n# THEORY verse\n# EXPECT verse T\n```",
            study(1), flags=re.S,
        )
        self.assertIn("empty theory", " ".join(check_logic(text, strict=True)[1]))

    def test_false_theory_missing_expectation_and_undeclared_symbol_fail(self):
        text = study(1)
        false = text.replace("BowedTo => {(author,teacher)}", "BowedTo => {}")
        self.assertIn("expected T, got F", " ".join(check_logic(false, strict=True)[1]))
        expected_false = false.replace("# EXPECT verse T", "# EXPECT verse F")
        self.assertEqual(check_logic(expected_false, strict=True), ("verse=F", []))
        missing = text.replace("# EXPECT verse T\n", "")
        self.assertIn("# EXPECT", " ".join(check_logic(missing, strict=True)[1]))
        undeclared = text.replace("BowedTo => {(author,teacher)}\n", "")
        self.assertIn("undeclared symbols", " ".join(check_logic(undeclared, strict=True)[1]))

    def test_homage_and_rescue_require_the_same_teacher(self):
        valuation, formula = valuation_and_formula(1)
        for predicate in ("DarknessDestroyedEveryWay", "DarknessDestroyedRegardingAll"):
            changed = Valuation(list(valuation.items()))
            changed[predicate] = set()
            self.assertFalse(satisfies(changed, formula), predicate)
        changed = Valuation(list(valuation.items()))
        changed["BowedTo"] = {("author", "another_teacher")}
        self.assertFalse(satisfies(changed, formula))

    def test_conventional_abhidharma_and_source_direction(self):
        valuation, formula = valuation_and_formula(2)
        for member in ("path", "work"):
            changed = Valuation(list(valuation.items()))
            changed["Abhidharma"] = valuation["Abhidharma"] - {(member,)}
            self.assertFalse(satisfies(changed, formula), member)
        changed = Valuation(list(valuation.items()))
        changed["SourceFor"] = {("work", "source")}
        self.assertFalse(satisfies(changed, formula))
        self.assertFalse(satisfies(
            valuation, Expression.fromstring("all x.(Abhidharma(x) -> Stainless(x))")
        ))

    def test_necessity_is_not_sufficiency_or_a_denial_of_all_means(self):
        valuation, formula = valuation_and_formula(3)
        self.assertTrue(satisfies(
            valuation, Expression.fromstring("exists x.HasMeansFor(x,pacification,afflictions)")
        ))
        self.assertFalse(satisfies(valuation, Expression.fromstring(
            "all x.(Discriminates(x,dharmas) -> HasMeansFor(x,pacification,afflictions))"
        )))
        changed = Valuation(list(valuation.items()))
        changed["HasMeansFor"] = valuation["HasMeansFor"] | {("unprepared", "pacification", "afflictions")}
        self.assertFalse(satisfies(changed, formula))

    def test_kila_does_not_assert_an_unreported_teaching_event(self):
        semantics = parse(study(3))[0].label()["SEM"].simplify()
        self.assertIn("ReportsTaught", {str(p) for p in semantics.predicates()})
        self.assertNotIn("Taught", {str(p) for p in semantics.predicates()})
        valuation, formula = valuation_and_formula(3)
        valuation["ReceivedReport"] = set()
        self.assertFalse(satisfies(valuation, formula))


if __name__ == "__main__":
    unittest.main()
