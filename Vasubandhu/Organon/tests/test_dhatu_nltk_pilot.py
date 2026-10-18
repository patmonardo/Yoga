"""Executable grammar, scope, and countermodels for the two Dhātu pilots."""

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
        for number in range(1, 20):
            with self.subTest(verse=number):
                text = study(number)
                self.assertEqual(check_grammar(text, strict=True)[1], [])
                summary, errors = check_logic(text, strict=True)
                self.assertEqual(errors, [])
                self.assertIn("verse=T", summary.split())
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
            (16, "ACCEPTED[CASE=nom,NUM=pl,GEN=m]",
             "ACCEPTED[CASE=nom,NUM=sg,GEN=m]"),
            (17, "PAST[CASE=nom,NUM=sg,GEN=n,SEM=",
             "PAST[CASE=nom,NUM=sg,GEN=m,SEM="),
            (18, "ESSENCE[CASE=ins,NUM=sg,GEN=n,SEM=",
             "ESSENCE[CASE=ins,NUM=pl,GEN=n,SEM="),
            (4, "V[NUM=pl,PERSON=third,VOICE=middle,LOC=required,SEM=",
             "V[NUM=sg,PERSON=third,VOICE=middle,LOC=required,SEM="),
            (5, "CESSATIONS[CASE=nom,NUM=dual,GEN=m,SEM=",
             "CESSATIONS[CASE=nom,NUM=sg,GEN=m,SEM="),
            (6, "OTHER[CASE=nom,NUM=sg,GEN=m,SEM=",
             "OTHER[CASE=nom,NUM=sg,GEN=n,SEM="),
            (7, "CONDITIONED[CASE=nom,NUM=pl,GEN=m,SEM=",
             "CONDITIONED[CASE=nom,NUM=sg,GEN=m,SEM="),
            (8, "CONFLICTHEAD[CASE=nom,NUM=pl,GEN=m,SEM=",
             "CONFLICTHEAD[CASE=nom,NUM=sg,GEN=m,SEM="),
            (9, "N[CASE=nom,NUM=pl,GEN=m,K=clarity,SEM=",
             "N[CASE=nom,NUM=sg,GEN=m,K=clarity,SEM="),
            (10, "COUNT[K=eleven,CASE=nom,NUM=sg,GEN=n,SEM=",
             "COUNT[K=eleven,CASE=nom,NUM=sg,GEN=m,SEM="),
            (11, "ETHICAL[CASE=nom,NUM=sg,GEN=m,SEM=",
             "ETHICAL[CASE=nom,NUM=sg,GEN=f,SEM="),
            (11, "CORREL[CASE=nom,NUM=sg,GEN=m]",
             "CORREL[CASE=nom,NUM=sg,GEN=f]"),
            (11, "ELEMENTS[CASE=acc,NUM=pl,SEM=",
             "ELEMENTS[CASE=nom,NUM=pl,SEM="),
            (12, "FUNCTIONS[CASE=nom,NUM=pl,GEN=m,SEM=",
             "FUNCTIONS[CASE=nom,NUM=sg,GEN=m,SEM="),
            (12, "CHARACTERS[CASE=nom,NUM=pl,GEN=m,SEM=",
             "CHARACTERS[CASE=nom,NUM=pl,GEN=n,SEM="),
            (13, "CALLED[NUM=sg,PERSON=third,VOICE=passive,SEM=",
             "CALLED[NUM=pl,PERSON=third,VOICE=passive,SEM="),
            (13, "PRINCIPLE[CASE=nom,NUM=sg,GEN=m,SEM=",
             "PRINCIPLE[CASE=nom,NUM=sg,GEN=f,SEM="),
            (14, "ACCEPTED[CASE=nom,NUM=pl,GEN=m,SEM=",
             "ACCEPTED[CASE=nom,NUM=sg,GEN=m,SEM="),
            (14, "TAKING[CASE=nom,NUM=sg,GEN=f,SEM=",
             "TAKING[CASE=nom,NUM=sg,GEN=m,SEM="),
            (15, "NAMES[CASE=nom,NUM=pl,GEN=m,SEM=",
             "NAMES[CASE=nom,NUM=sg,GEN=m,SEM="),
            (15, "ACCOMP[CASE=ins,NUM=pl,SEM=",
             "ACCOMP[CASE=nom,NUM=pl,SEM="),
        )
        for number, before, after in changes:
            with self.subTest(verse=number):
                text = study(number)
                self.assertIn(before, text)
                self.assertEqual(parse(text.replace(before, after)), [])

    def test_formations_remainder_is_conditioned_and_not_only_volition(self):
        valuation, formula = valuation_and_formula(15)
        self.assertTrue(satisfies(valuation, formula))
        self.assertEqual(
            valuation["FormationsBaseMember"],
            valuation["Conditioned"] - valuation["OtherFourBaseMember"],
        )
        for member in valuation["FormationsBaseMember"]:
            changed = Valuation(list(valuation.items()))
            changed["FormationsBaseMember"] = valuation["FormationsBaseMember"] - {member}
            self.assertFalse(satisfies(changed, formula), member)
        for predicate in ("AssociatedOther", "DissociatedFormation", "Pure"):
            self.assertTrue(valuation[predicate])
            self.assertTrue(valuation[predicate] <= valuation["FormationsBaseMember"])
            self.assertFalse(valuation[predicate] & valuation["Volition"])
        self.assertFalse(valuation["Unconditioned"] & valuation["BaseMember"])
        self.assertFalse(valuation["Unconditioned"] & valuation["Conditioned"])

    def test_seven_dharma_categories_preserve_base_origins(self):
        valuation, formula = valuation_and_formula(15)
        categories = [
            valuation["FeelingBaseMember"],
            valuation["ReflectionBaseMember"],
            valuation["FormationsBaseMember"],
            valuation["Avijnapti"],
            *({member} for member in sorted(valuation["Unconditioned"])),
        ]
        self.assertEqual(len(categories), 7)
        members = set()
        for category in categories:
            self.assertTrue(category)
            self.assertFalse(members & category)
            members |= category
        self.assertGreater(len(members), 7)
        for predicate in ("DharmaEssenceMember", "DharmaPrincipleMember"):
            self.assertEqual(valuation[predicate], members)
            for member in members:
                changed = Valuation(list(valuation.items()))
                changed[predicate] = valuation[predicate] - {member}
                self.assertFalse(satisfies(changed, formula), (predicate, member))
        self.assertTrue(valuation["Avijnapti"] <= valuation["FormBaseMember"])
        self.assertFalse(valuation["CognitionBaseMember"] & valuation["ThreeBaseMember"])
        self.assertFalse(valuation["CognitionBaseMember"] & members)

    def test_same_ten_members_do_not_duplicate_or_include_avijnapti(self):
        valuation, formula = valuation_and_formula(14)
        self.assertEqual(len(valuation["SensoryFaculty"]), 5)
        self.assertEqual(len(valuation["SensoryMeaning"]), 5)
        self.assertFalse(valuation["SensoryFaculty"] & valuation["SensoryMeaning"])
        members = valuation["SensoryFaculty"] | valuation["SensoryMeaning"]
        self.assertEqual(len(members), 10)
        for predicate in (
            "FacultyOrMeaning", "TenFormEssenceMember", "TenFormPrincipleMember"
        ):
            self.assertEqual(valuation[predicate], members)
        self.assertEqual(
            valuation["FormBaseMember"], members | {(valuation["avijnapti"],)}
        )
        for predicate in ("TenFormEssenceMember", "TenFormPrincipleMember"):
            for member in members:
                changed = Valuation(list(valuation.items()))
                changed[predicate] = valuation[predicate] - {member}
                self.assertFalse(satisfies(changed, formula), (predicate, member))
        for predicate in ("Experience", "MarkTaking"):
            changed = Valuation(list(valuation.items()))
            changed[predicate] = set()
            self.assertFalse(satisfies(changed, formula), predicate)

    def test_feeling_tones_and_shared_contact_groups_are_different_axes(self):
        valuation, _ = valuation_and_formula(14)
        self.assertEqual(len(valuation["FeelingTone"]), 3)
        self.assertEqual(len(valuation["FeelingContactGroup"]), 6)
        self.assertEqual(
            valuation["FeelingContactGroup"], valuation["ReflectionContactGroup"]
        )
        self.assertIn(("mind_contact",), valuation["FeelingContactGroup"])
        self.assertFalse(valuation["FeelingTone"] & valuation["FeelingContactGroup"])
        self.assertFalse(valuation["Feeling"] & valuation["Reflection"])
        self.assertEqual(len(valuation["HasTone"]), 3)
        self.assertTrue(satisfies(valuation, Expression.fromstring(
            "all x.(Feeling(x) -> exists t.(FeelingTone(t) & HasTone(x,t)))"
        )))
        self.assertIn(
            (valuation["reflection_case"], valuation["blue_mark"]),
            valuation["TakesMark"],
        )

    def test_worldly_names_preserve_both_wind_uses_without_identity(self):
        valuation, formula = valuation_and_formula(13)
        self.assertTrue(satisfies(valuation, formula))
        self.assertEqual(len(valuation["WorldlyDesignates"]), 5)
        for pair in valuation["WorldlyDesignates"]:
            changed = Valuation(list(valuation.items()))
            changed["WorldlyDesignates"] = valuation["WorldlyDesignates"] - {pair}
            self.assertFalse(satisfies(changed, formula), pair)
        self.assertNotEqual(valuation["visible_complex"], valuation["wind_principle"])
        for name in ("earth", "water", "fire"):
            self.assertNotIn(
                (valuation[f"{name}_name"], valuation[f"{name}_principle"]),
                valuation["WorldlyDesignates"],
            )
        self.assertEqual(
            {target for label, target in valuation["WorldlyDesignates"]
             if label == valuation["wind_name"]},
            {valuation["visible_complex"], valuation["wind_principle"]},
        )

    def test_continuity_outlasts_origin_without_an_eternity_claim(self):
        valuation, _ = valuation_and_formula(13)
        continues = Expression.fromstring("Continues(continuity,later_case)")
        self.assertTrue(satisfies(valuation, continues))
        self.assertNotIn((valuation["eye_cognition"],), valuation["FormBaseMember"])
        for relation in ("OriginatingManifestation", "OriginatingElementSupport"):
            formula = Expression.fromstring(
                f"all x.all y.all t.(({relation}(x,y) & Ceased(y,t)) "
                "-> -Continues(x,t))"
            )
            self.assertFalse(satisfies(valuation, formula), relation)
            changed = Valuation(list(valuation.items()))
            changed["Continues"] = set()
            self.assertFalse(satisfies(changed, continues))
            self.assertTrue(satisfies(changed, formula), relation)
        self.assertFalse(satisfies(valuation, Expression.fromstring(
            "all t.Continues(continuity,t)"
        )))

    def test_great_elements_have_four_distinct_ordered_characters(self):
        valuation, formula = valuation_and_formula(12)
        names = ("earth", "water", "fire", "wind")
        denotations = {valuation[name] for name in names}
        self.assertEqual(len(denotations), 4)
        self.assertEqual(valuation["GreatElement"], {(name,) for name in denotations})
        self.assertEqual(len(valuation["OwnCharacter"]), 4)
        self.assertTrue(satisfies(valuation, formula))
        for pair in valuation["OwnCharacter"]:
            changed = Valuation(list(valuation.items()))
            changed["OwnCharacter"] = valuation["OwnCharacter"] - {pair}
            self.assertFalse(satisfies(changed, formula), pair)
        changed = Valuation(list(valuation.items()))
        changed["OwnCharacter"] = {
            (valuation["earth"], valuation["cohesion"]),
            (valuation["water"], valuation["hardness"]),
            (valuation["fire"], valuation["heat"]),
            (valuation["wind"], valuation["impulsion"]),
        }
        self.assertFalse(satisfies(changed, formula))
        changed = Valuation(list(valuation.items()))
        changed["GreatElement"] = valuation["GreatElement"] | {
            (valuation["lightness"],)
        }
        self.assertFalse(satisfies(changed, formula))
        changed = Valuation(list(valuation.items()))
        changed["EstablishedInSupportEtc"] = set()
        self.assertFalse(satisfies(changed, formula))

    def test_element_functions_are_separate_prose_correspondences(self):
        valuation, _ = valuation_and_formula(12)
        prose = Expression.fromstring(
            "Function(earth,support) & Function(water,gathering) & "
            "Function(fire,ripening) & Function(wind,spreading)"
        )
        self.assertTrue(satisfies(valuation, prose))
        self.assertEqual(len(valuation["Function"]), 4)
        for pair in valuation["Function"]:
            changed = Valuation(list(valuation.items()))
            changed["Function"] = valuation["Function"] - {pair}
            self.assertFalse(satisfies(changed, prose), pair)
        changed = Valuation(list(valuation.items()))
        changed["Function"] = {
            (valuation["earth"], valuation["gathering"]),
            (valuation["water"], valuation["support"]),
            (valuation["fire"], valuation["ripening"]),
            (valuation["wind"], valuation["spreading"]),
        }
        self.assertFalse(satisfies(changed, prose))
        functions = {value for _, value in valuation["Function"]}
        characters = {value for _, value in valuation["OwnCharacter"]}
        self.assertFalse(functions & characters)
        self.assertIn((valuation["lightness"],), valuation["DerivedForm"])
        self.assertNotIn(
            (valuation["wind"], valuation["lightness"]), valuation["OwnCharacter"]
        )
        self.assertNotIn((valuation["lightness"],), valuation["GreatElement"])

    def test_avijnapti_keeps_ethical_dependence_naming_and_scope_distinct(self):
        valuation, formula = valuation_and_formula(11)
        self.assertTrue(satisfies(valuation, formula))
        self.assertEqual(len(valuation["CalledAvijnapti"]), 2)
        for member, in valuation["CalledAvijnapti"]:
            self.assertIn((member,), valuation["Stream"])
            self.assertIn((member, valuation["great_elements"]), valuation["DependsOn"])
            self.assertIn(
                (member,), valuation["Wholesome"] | valuation["Unwholesome"]
            )
            changed = Valuation(list(valuation.items()))
            changed["CalledAvijnapti"] = valuation["CalledAvijnapti"] - {(member,)}
            self.assertFalse(satisfies(changed, formula), member)
            for state in ("otherwise_directed", "absent"):
                changed = Valuation(list(valuation.items()))
                changed["ScopeIncludes"] = valuation["ScopeIncludes"] - {
                    (member, valuation[state])
                }
                self.assertFalse(satisfies(changed, formula), (member, state))
        for member, in valuation["AcquisitionStream"]:
            changed = Valuation(list(valuation.items()))
            changed["DependsOn"] = valuation["DependsOn"] | {
                (member, valuation["great_elements"])
            }
            self.assertFalse(satisfies(changed, formula), member)
        self.assertFalse(satisfies(valuation, Expression.fromstring(
            "all x.(CalledAvijnapti(x) -> (Wholesome(x) & Unwholesome(x)))"
        )))
        self.assertTrue(satisfies(valuation, Expression.fromstring(
            "all x.(CalledAvijnapti(x) -> "
            "(ScopeIncludes(x,undistracted) & -InformsAnother(x)))"
        )))
        changed = Valuation(list(valuation.items()))
        changed["Origin"] = {
            (member, origin)
            for member, in valuation["CalledAvijnapti"]
            for origin in (valuation["vijnapti"], valuation["absorption"])
        }
        self.assertEqual(check_logic(
            study(11).replace(
                "Origin => {(wholesome_continuity,absorption_origin),"
                "(unwholesome_continuity,manifestation_origin)}",
                "Origin => {(wholesome_continuity,manifestation_origin),"
                "(unwholesome_continuity,absorption_origin)}",
            ), strict=True
        )[1], [])
        self.assertTrue(satisfies(changed, Expression.fromstring(
            "all x.(CalledAvijnapti(x) -> "
            "(Origin(x,vijnapti) | Origin(x,absorption)))"
        )))

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

    def test_seven_principles_are_a_roster_not_seven_substances(self):
        valuation, formula = valuation_and_formula(16)
        six = {row[0] for row in valuation["SixCognitionPrinciple"]}
        members = {row[0] for row in valuation["PrincipleMember"]}
        self.assertEqual(len(six), 6)
        self.assertNotIn(valuation["mind_principle"], six)
        self.assertEqual(members, six | {valuation["mind_principle"]})
        self.assertEqual(len(members), 7)
        for extension in (
            valuation["PrincipleMember"] - {("mind_role", "cognition_class")},
            valuation["PrincipleMember"] | {("extra_role", "cognition_class")},
        ):
            changed = Valuation(list(valuation.items()))
            changed["PrincipleMember"] = extension
            self.assertFalse(satisfies(changed, formula))
        self.assertNotEqual(valuation["cognition_base"], valuation["mind_essence"])

    def test_mind_is_temporally_restricted_without_requiring_a_successor(self):
        valuation, formula = valuation_and_formula(17)
        self.assertFalse(satisfies(valuation, Expression.fromstring(
            "all x.(Cognition(x) -> MindRole(x))"
        )))
        self.assertFalse(satisfies(valuation, Expression.fromstring(
            "all x.(MindRole(x) -> HasSuccessor(x))"
        )))
        changed = Valuation(list(valuation.items()))
        changed["MindRole"] = {("final",)}
        self.assertFalse(satisfies(changed, formula))
        for predicate in ("ImmediatelyPast", "OfSixCognitions"):
            changed = Valuation(list(valuation.items()))
            changed["MindRole"] = {("final",)}
            changed[predicate] = valuation[predicate] - {("ceased",)}
            self.assertTrue(satisfies(changed, formula), predicate)
        changed = Valuation(list(valuation.items()))
        changed["HasSuccessor"] = set()
        self.assertTrue(satisfies(changed, formula))

    def test_three_projections_cover_jointly_and_allow_overlap(self):
        valuation, formula = valuation_and_formula(18)
        changed = Valuation(list(valuation.items()))
        changed["IncludedByOwnNature"] = (
            valuation["IncludedByOwnNature"] - {("eye", "form_class")}
        )
        self.assertFalse(satisfies(changed, formula))
        self.assertIn(("avijnapti", "form_class"), valuation["IncludedByOwnNature"])
        self.assertIn(("avijnapti", "dharma_class"), valuation["IncludedByOwnNature"])
        changed["IncludedByOwnNature"] = (
            valuation["IncludedByOwnNature"] - {("avijnapti", "form_class")}
        )
        self.assertTrue(satisfies(changed, formula))
        for category in ("form_base", "mind_essence", "dharma_principle"):
            self.assertFalse(satisfies(valuation, Expression.fromstring(
                f"all x.(Dharma(x) -> IncludedByOwnNature(x,{category}))"
            )), category)
        self.assertNotIn(("unconditioned", "form_class"), valuation["IncludedByOwnNature"])
        for predicate in ("InclusionByOwnNature", "SeparateFromOtherNature"):
            changed = Valuation(list(valuation.items()))
            changed[predicate] = valuation[predicate] - {("eye",)}
            self.assertFalse(satisfies(changed, formula), predicate)

    def test_all_three_commonalities_are_required_for_the_scoped_rule(self):
        valuation, formula = valuation_and_formula(19)
        changed = Valuation(list(valuation.items()))
        changed["OnePrinciple"] = valuation["OnePrinciple"] - {("eyes",)}
        self.assertFalse(satisfies(changed, formula))
        for predicate in ("CommonKind", "CommonRange", "CommonCognition"):
            relaxed = Valuation(list(changed.items()))
            relaxed[predicate] = valuation[predicate] - {("eyes",)}
            self.assertTrue(satisfies(relaxed, formula), predicate)
        beauty_only = Valuation(list(valuation.items()))
        beauty_only["ForBeautyOfSupport"] = valuation["ForBeautyOfSupport"] | {("ornament",)}
        self.assertTrue(satisfies(beauty_only, formula))
        self.assertFalse(satisfies(beauty_only, Expression.fromstring(
            "all x.(ForBeautyOfSupport(x) -> OnePrinciple(x))"
        )))
        text = study(19)
        self.assertNotIn("ObjectOf", text)
        commentary = (
            STUDIES / "VAK_1.19_bhasya.md"
        ).read_text(encoding="utf-8")
        self.assertIn("both are supports of one Eye-Cognition", commentary)
        self.assertNotIn("commonality of kind, range, and principle", commentary)

    def test_alambana_does_not_entail_asrava_persistence(self):
        valuation, formula = valuation_and_formula(4)
        self.assertTrue(satisfies(valuation, formula))
        self.assertTrue(satisfies(valuation, Expression.fromstring(
            "exists a x.(Asrava(a) & CanTakeAsAlambana(a,x) & -PersistsIn(a,x))"
        )))
        self.assertFalse(satisfies(valuation, Expression.fromstring(
            "all a x.(CanTakeAsAlambana(a,x) -> PersistsIn(a,x))"
        )))
        changed = Valuation(list(valuation.items()))
        changed["PersistsIn"] = set()
        self.assertFalse(satisfies(changed, formula))
        changed = Valuation(list(valuation.items()))
        changed["Impure"] = valuation["Impure"] | {("path",)}
        self.assertFalse(satisfies(changed, formula))

    def test_three_unconditioned_members_and_conditioned_pure_path(self):
        valuation, formula = valuation_and_formula(5)
        members = {valuation[name] for name in (
            "space", "discriminative_cessation", "nondiscriminative_cessation"
        )}
        self.assertEqual(len(members), 3)
        self.assertEqual(valuation["Unconditioned"], {(member,) for member in members})
        self.assertTrue(satisfies(valuation, Expression.fromstring(
            "exists x.(PathTruth(x) & Conditioned(x) & Pure(x) & -Unconditioned(x))"
        )))
        changed = Valuation(list(valuation.items()))
        changed["Unconditioned"] = valuation["Unconditioned"] | {("extra",)}
        self.assertFalse(satisfies(changed, formula))
        changed = Valuation(list(valuation.items()))
        changed["NonObstruction"] = set()
        self.assertFalse(satisfies(changed, formula))
        changed = Valuation(list(valuation.items()))
        changed["Pure"] = valuation["Pure"] - {("path",)}
        self.assertFalse(satisfies(changed, formula))

    def test_cessation_is_casewise_and_deficient_conditions_are_not_discrimination(self):
        valuation, formula = valuation_and_formula(6)
        for case in ("release_one", "release_two"):
            changed = Valuation(list(valuation.items()))
            changed["Casewise"] = valuation["Casewise"] - {(case,)}
            self.assertFalse(satisfies(changed, formula), case)
        changed = Valuation(list(valuation.items()))
        changed["AttainedByDiscrimination"] = valuation["AttainedByDiscrimination"] | {("blocked",)}
        self.assertFalse(satisfies(changed, formula))
        changed = Valuation(list(valuation.items()))
        changed["AbsoluteObstructionOfFutureArising"] = set()
        self.assertFalse(satisfies(changed, formula))
        self.assertTrue(satisfies(valuation, Expression.fromstring(
            "exists x.(OtherCessation(x) & ThroughDeficiencyOfConditions(x) & "
            "-DisjunctionFromImpure(x) & Unconditioned(x))"
        )))

    def test_conditioned_collective_and_four_determinations(self):
        valuation, formula = valuation_and_formula(7)
        self.assertEqual(len(valuation["Conditioned"]), 6)
        for predicate in (
            "FiveBaseMember", "CourseDetermination", "Kathavastu",
            "HasNihsara", "HasVastu",
        ):
            changed = Valuation(list(valuation.items()))
            changed[predicate] = valuation[predicate] - {("form",)}
            self.assertFalse(satisfies(changed, formula), predicate)
        changed = Valuation(list(valuation.items()))
        changed["FiveBaseMember"] = valuation["FiveBaseMember"] | {("space_case",)}
        self.assertFalse(satisfies(changed, formula))
        self.assertFalse(satisfies(valuation, Expression.fromstring(
            "all x.(Conditioned(x) -> Impure(x))"
        )))
        changed = Valuation(list(valuation.items()))
        changed["HasVastu"] = valuation["HasVastu"] | {("outside_case",)}
        self.assertTrue(satisfies(changed, formula))
        self.assertFalse(satisfies(changed, Expression.fromstring(
            "all x.(HasVastu(x) <-> Kathavastu(x))"
        )))
        self.assertNotIn("Cause", {str(p) for p in parse(study(7))[0].label()["SEM"].predicates()})

    def test_appropriation_and_names_keep_the_impure_restriction(self):
        valuation, formula = valuation_and_formula(8)
        for predicate in (
            "AppropriationBaseMember", "WithConflict", "Suffering", "Origin",
            "DissolvingWorld", "StationOfViews", "Becoming",
        ):
            changed = Valuation(list(valuation.items()))
            changed[predicate] = set()
            self.assertFalse(satisfies(changed, formula), predicate)
        changed = Valuation(list(valuation.items()))
        changed["AppropriationBaseMember"] = (
            valuation["AppropriationBaseMember"] | {("path",)}
        )
        self.assertFalse(satisfies(changed, formula))
        self.assertFalse(satisfies(valuation, Expression.fromstring(
            "all x.(FiveBaseMember(x) -> AppropriationBaseMember(x))"
        )))
        changed = Valuation(list(valuation.items()))
        changed["Suffering"] = valuation["Suffering"] | {("outside_case",)}
        self.assertTrue(satisfies(changed, formula))
        self.assertFalse(satisfies(changed, Expression.fromstring(
            "all x.(Suffering(x) <-> Origin(x))"
        )))
        self.assertNotIn(("path",), valuation["WithConflict"])
        self.assertNotIn(("path",), valuation["StationOfViews"])

    def test_counts_within_meanings_do_not_add_a_form_base(self):
        valuation, formula = valuation_and_formula(10)
        self.assertEqual(len(valuation["VisibleKind"]), 20)
        self.assertEqual(len(valuation["TasteKind"]), 6)
        self.assertEqual(len(valuation["BinaryAspect"]), 2)
        self.assertEqual(len(valuation["GreatElement"]), 4)
        self.assertEqual(len(valuation["DerivedTangible"]), 7)
        self.assertFalse(valuation["GreatElement"] & valuation["DerivedTangible"])
        self.assertEqual(
            valuation["TangibleConstituent"],
            valuation["GreatElement"] | valuation["DerivedTangible"],
        )
        self.assertEqual(len(valuation["TangibleConstituent"]), 11)
        self.assertNotEqual(valuation["visible_meaning"], valuation["form_base"])
        for meaning, count in (
            ("visible_meaning", "twenty"), ("sound_meaning", "eight"),
            ("taste_meaning", "six"), ("odor_meaning", "four"),
        ):
            changed = Valuation(list(valuation.items()))
            changed["EnumeratedKinds"] = valuation["EnumeratedKinds"] - {
                (valuation[meaning], valuation[count])
            }
            self.assertFalse(satisfies(changed, formula), meaning)
        for predicate in ("TwofoldAnalysis", "ElevenfoldConstitution"):
            changed = Valuation(list(valuation.items()))
            changed[predicate] = set()
            self.assertFalse(satisfies(changed, formula), predicate)

    def test_form_roster_has_eleven_kinds_without_supported_cognitions(self):
        valuation, _ = valuation_and_formula(9)
        faculties = valuation["Faculty"]
        meanings = valuation["Meaning"]
        avijnapti = valuation["Avijnapti"]
        self.assertEqual((len(faculties), len(meanings), len(avijnapti)), (5, 5, 1))
        self.assertFalse(faculties & meanings)
        self.assertFalse((faculties | meanings) & avijnapti)
        self.assertEqual(valuation["FormMember"], faculties | meanings | avijnapti)
        self.assertEqual(len(valuation["FormMember"]), 11)
        self.assertFalse(valuation["FormMember"] & valuation["Cognition"])
        changed = study(9).replace(
            "FormMember => {eye,",
            "FormMember => {eyecognition, eye,",
        )
        self.assertIn("expected T, got F", " ".join(check_logic(changed, strict=True)[1]))

    def test_faculty_support_requires_correspondence_not_identity(self):
        valuation, formula = valuation_and_formula(9)
        for predicate in ("ClarityOfForm",):
            changed = Valuation(list(valuation.items()))
            changed[predicate] = valuation[predicate] - {("eye",)}
            self.assertFalse(satisfies(changed, formula))
        for predicate, pair in (
            ("Supports", ("eye", "eyecognition")),
            ("Corresponds", ("eyecognition", "eye")),
        ):
            changed = Valuation(list(valuation.items()))
            changed[predicate] = valuation[predicate] - {pair}
            self.assertFalse(satisfies(changed, formula), predicate)
        changed = Valuation(list(valuation.items()))
        changed["Supports"] = (
            valuation["Supports"] - {("eye", "eyecognition")}
        ) | {("eye", "earcognition")}
        self.assertFalse(satisfies(changed, formula))
        self.assertTrue(satisfies(valuation, Expression.fromstring(
            "exists f c.(Faculty(f) & Cognition(c) & Supports(f,c) & -(f=c))"
        )))
        self.assertFalse(satisfies(valuation, Expression.fromstring(
            "all x.(FormMember(x) -> VisibleMeaning(x))"
        )))


if __name__ == "__main__":
    unittest.main()
