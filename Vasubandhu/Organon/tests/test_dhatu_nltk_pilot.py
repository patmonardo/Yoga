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
        for number in range(1, 49):
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
            (20, "SENSES[CASE=nom,NUM=pl,GEN=m,SEM=",
             "SENSES[CASE=nom,NUM=sg,GEN=m,SEM="),
            (20, "THREE[CASE=nom,NUM=pl,GEN=f,SEM=",
             "THREE[CASE=nom,NUM=pl,GEN=m,SEM="),
            (21, "PLACED[CASE=nom,NUM=dual,GEN=m,SEM=",
             "PLACED[CASE=nom,NUM=pl,GEN=m,SEM="),
            (21, "PAIR[CASE=nom,NUM=dual,GEN=f,SEM=",
             "PAIR[CASE=nom,NUM=sg,GEN=f,SEM="),
            (21, "OTHER[CASE=abl,NUM=pl,SEM=",
             "OTHER[CASE=ins,NUM=pl,SEM="),
            (22, "STATED[CASE=nom,NUM=sg,GEN=n,SEM=",
             "STATED[CASE=nom,NUM=sg,GEN=m,SEM="),
            (23, "REASON[CASE=abl,K=present,SEM=<",
             "REASON[CASE=ins,K=present,SEM=<"),
            (23, "GROUND[CASE=ins,SEM=<",
             "GROUND[CASE=abl,SEM=<"),
            (24, "DHARMANAME[CASE=nom,NUM=sg,GEN=n,SEM=<",
             "DHARMANAME[CASE=nom,NUM=sg,GEN=m,SEM=<"),
            (24, "PRIMACY[CASE=abl,SEM=<",
             "PRIMACY[CASE=ins,SEM=<"),
            (25, "CORREL[CASE=nom,NUM=pl,GEN=n] ->",
             "CORREL[CASE=nom,NUM=pl,GEN=m] ->"),
            (25, "AGENT[CASE=nom,NUM=sg,GEN=m,SEM=<",
             "AGENT[CASE=nom,NUM=pl,GEN=m,SEM=<"),
            (26, "COLL[CASE=nom,NUM=sg,GEN=m,SEM=<",
             "COLL[CASE=nom,NUM=sg,GEN=n,SEM=<"),
            (26, "TOPICS[CASE=gen,NUM=pl,SEM=<",
             "TOPICS[CASE=loc,NUM=pl,SEM=<"),
            (27, "GERUNDIVE[CASE=nom,NUM=pl,GEN=m,SEM=<",
             "GERUNDIVE[CASE=nom,NUM=sg,GEN=m,SEM=<"),
            (27, "AMONG[CASE=loc,NUM=pl,SEM=<",
             "AMONG[CASE=abl,NUM=pl,SEM=<"),
            (28, "SUPPORTS[CASE=nom,NUM=pl,GEN=m,SEM=<",
             "SUPPORTS[CASE=nom,NUM=sg,GEN=m,SEM=<"),
            (28, "IMPURE[CASE=nom,NUM=sg,GEN=n,SEM=<",
             "IMPURE[CASE=nom,NUM=sg,GEN=m,SEM=<"),
            (29, "NAME[CASE=nom,NUM=sg,GEN=n,SEM=<",
             "NAME[CASE=nom,NUM=sg,GEN=m,SEM=<"),
            (29, "EXCL[CASE=nom,NUM=pl,GEN=m,SEM=<",
             "EXCL[CASE=nom,NUM=sg,GEN=m,SEM=<"),
            (30, "EXCL[CASE=ins,SEM=<",
             "EXCL[CASE=abl,SEM=<"),
            (30, "OTHERS[CASE=nom,NUM=pl,GEN=m,SEM=<",
             "OTHERS[CASE=nom,NUM=sg,GEN=m,SEM=<"),
            (31, "THREE[CASE=nom,NUM=pl,GEN=m,SEM=<",
             "THREE[CASE=nom,NUM=sg,GEN=m,SEM=<"),
            (31, "IMP[CASE=nom,NUM=pl,GEN=m,SEM=<",
             "IMP[CASE=nom,NUM=pl,GEN=n,SEM=<"),
            (32, "TRI[CASE=nom,NUM=pl,GEN=m,SEM=<",
             "TRI[CASE=nom,NUM=sg,GEN=m,SEM=<"),
            (32, "HI[RESTR=yes] -> 'hi'",
             "HI[RESTR=no] -> 'hi'"),
            (33, "TAU[NUM=dual] -> 'tau'",
             "TAU[NUM=pl] -> 'tau'"),
            (33, "VY[CASE=nom,NUM=sg,GEN=f,SEM=<",
             "VY[CASE=nom,NUM=sg,GEN=m,SEM=<"),
            (34, "NUMR[CNT=7] -> 'sapta'",
             "NUMR[CNT=8] -> 'sapta'"),
            (34, "EIGHT[CNT=8,SEM=<",
             "EIGHT[CNT=7,SEM=<"),
            (35, "NUMR[CNT=10] -> 'daśa'",
             "NUMR[CNT=9] -> 'daśa'"),
            (35, "DVI[GEN=n,NUM=sg,SEM=<",
             "DVI[GEN=m,NUM=sg,SEM=<"),
            (36, "DVANDVA[CASE=gen,NUM=dual,V1=act,V2=pass]",
             "DVANDVA[CASE=gen,NUM=dual,V1=pass,V2=act]"),
            (36, "V[ROOT=dah,VOICE=pass,NUM=sg,SEM=<",
             "V[ROOT=dah,VOICE=act,NUM=sg,SEM=<"),
            (37, "PRED[NUM=sg,SEM=<",
             "PRED[NUM=du,SEM=<"),
            (37, "APRAT[NUM=pl,CNT=8,SEM=<",
             "APRAT[NUM=pl,CNT=10,SEM=<"),
            (38, "TRI[NUM=pl,CNT=3] -> 'trayaḥ'",
             "TRI[NUM=pl,CNT=4] -> 'trayaḥ'"),
            (38, "PAIR[CASE=gen,NUM=dual,SEM=<",
             "PAIR[CASE=gen,NUM=pl,SEM=<"),
        (39, "NUMR[CNT=12] -> 'dvādaśa'", "NUMR[CNT=11] -> 'dvādaśa'"),
        (39, "REL[NUM=sg,POL=neg,SEM=?w] -> YAH", "REL[NUM=sg,POL=pos,SEM=?w] -> YAH"),
        (40, "NUMR[CNT=5,SEM=<", "NUMR[CNT=6,SEM=<"),
        (40, "NP[GEN=n,NUM=sg,SEM=<\\i.Form(i)>] -> 'rūpam'", "NP[GEN=m,NUM=sg,SEM=<\\i.Form(i)>] -> 'rūpam'"),
        (41, "PRADESA[NUM=du] -> 'pradeśau'", "PRADESA[NUM=sg] -> 'pradeśau'"),
        (41, "DHI[GEN=f,NUM=sg,SEM=<", "DHI[GEN=m,NUM=sg,SEM=<"),
        (42, "V[VOICE=pass,ROOT=drs] -> 'dṛśyate'", "V[VOICE=pass,ROOT=sru] -> 'dṛśyate'"),
        (42, "NP[CASE=nom,GEN=n,NUM=sg,SEM=<\\c.Cognition(c)>] -> 'vijñānam'", "NP[CASE=acc,GEN=n,NUM=sg,SEM=<\\c.Cognition(c)>] -> 'vijñānam'"),
        (43, "TRAYA[CNT=3,GEN=n,NUM=sg] -> 'trayam'", "TRAYA[CNT=4,GEN=n,NUM=sg] -> 'trayam'"),
        (43, "UBHA[CASE=ins,NUM=du] -> 'ubhābhyām'", "UBHA[CASE=ins,NUM=pl] -> 'ubhābhyām'"),
        (44, "TAI[CASE=ins,NUM=pl] -> 'taiḥ'", "TAI[CASE=ins,NUM=sg] -> 'taiḥ'"),
        (44, "NUMR[CASE=ins,CNT=3,NUM=pl] -> 'tribhiḥ'", "NUMR[CASE=ins,CNT=4,NUM=pl] -> 'tribhiḥ'"),
        (45, "TAI[CASE=ins,NUM=pl,SEM=<\\x.Faculty(x)>] -> 'taiḥ'", "TAI[CASE=ins,NUM=sg,SEM=<\\x.Faculty(x)>] -> 'taiḥ'"),
        (45, "VIJ[CASE=nom,NUM=sg,SEM=<\\c.Cognition(c)>] -> 'vijñānam'", "VIJ[CASE=nom,NUM=pl,SEM=<\\c.Cognition(c)>] -> 'vijñānam'"),
        (46, "ASYA[REF=cog,SEM=<\\s y.CogIn(s,y)>] -> 'asya'", "ASYA[REF=form,SEM=<\\s y.CogIn(s,y)>] -> 'asya'"),
        (46, "UBHE[NUM=du,SEM=<", "UBHE[NUM=pl,SEM=<"),
        (47, "GENP[CASE=gen,CNT=3,NUM=pl,SEM=<", "GENP[CASE=gen,CNT=3,NUM=sg,SEM=<"),
        (47, "NOMN[GEN=n,NUM=sg,SEM=<\\s x.(Thinking(s) & FacIn(s,x))>] -> 'manaḥ'", "NOMN[GEN=m,NUM=sg,SEM=<\\s x.(Thinking(s) & FacIn(s,x))>] -> 'manaḥ'"),
        (48, "NUMR[CNT=12] -> 'dvādaśa'", "NUMR[CNT=5] -> 'dvādaśa'"),
        (48, "FPRED[GEN=n,NUM=sg,", "FPRED[GEN=m,NUM=sg,"),
        )
        for number, before, after in changes:
            with self.subTest(verse=number):
                text = study(number)
                self.assertIn(before, text)
                self.assertEqual(parse(text.replace(before, after)), [])

    def test_unconditioned_exclusion_and_four_grounds_are_nonvacuous(self):
        valuation, formula = valuation_and_formula(22)
        self.assertEqual(len(valuation["Unconditioned"]), 3)
        self.assertFalse(valuation["Unconditioned"] & valuation["BaseMember"])
        for predicate in ("DharmaEssenceMember", "DharmaPrincipleMember"):
            self.assertTrue(valuation["Unconditioned"] <= valuation[predicate])
        self.assertEqual(len(valuation["OrderingGround"]), 4)
        self.assertEqual(
            {order for order, _ in valuation["OrderingGround"]},
            {valuation["base_order"]},
        )
        for member in valuation["Unconditioned"]:
            changed = Valuation(list(valuation.items()))
            changed["BaseMember"] = valuation["BaseMember"] | {member}
            self.assertFalse(satisfies(changed, formula), member)
            changed = Valuation(list(valuation.items()))
            changed["CollectionMeaningInapplicable"] = (
                valuation["CollectionMeaningInapplicable"] - {member}
            )
            self.assertFalse(satisfies(changed, formula), member)
        for pair in valuation["OrderingGround"]:
            changed = Valuation(list(valuation.items()))
            changed["OrderingGround"] = valuation["OrderingGround"] - {pair}
            self.assertFalse(satisfies(changed, formula), pair)

    def test_five_base_order_meal_roles_and_level_correspondences(self):
        valuation, _ = valuation_and_formula(22)
        names = ("form", "feeling", "reflection", "formations", "cognition")
        kinds = {valuation[name] for name in names}
        self.assertEqual(len(kinds), 5)
        self.assertEqual(valuation["BaseKind"], {(kind,) for kind in kinds})
        self.assertEqual(valuation["Precedes"], {
            (valuation[left], valuation[right])
            for left, right in zip(names, names[1:])
        })
        self.assertEqual(valuation["MealRole"], {
            (valuation[name], valuation[role])
            for name, role in zip(names, ("vessel", "food", "seasoning", "maker", "eater"))
        })
        self.assertEqual(valuation["CharacterizedBy"], {
            (valuation[level], valuation[name])
            for level, name in zip(
                ("desire_realm", "dhyanas", "first_three_formless", "summit"), names
            )
        })
        for predicate, source, target in (
            ("MealRole", "feeling", "food"),
            ("CharacterizedBy", "dhyanas", "feeling"),
        ):
            formula = Expression.fromstring(f"{predicate}({source},{target})")
            changed = Valuation(list(valuation.items()))
            changed[predicate] = valuation[predicate] - {
                (valuation[source], valuation[target])
            }
            self.assertFalse(satisfies(changed, formula))

    def test_separate_bases_preserve_mental_factor_status_and_all_reasons(self):
        valuation, formula = valuation_and_formula(21)
        self.assertTrue(satisfies(valuation, formula))
        pair = {(valuation[name],) for name in ("feeling", "reflection")}
        self.assertEqual(len(pair), 2)
        self.assertEqual(valuation["SeparateBasePlacement"], pair)
        self.assertTrue(pair <= valuation["MentalFactor"])
        for predicate in (
            "CauseOfDisputeRoots", "CauseOfSamsara", "OrderReasonForSeparateBases",
            "SeparateBasePlacement", "SeparatelyFrom",
        ):
            for member in valuation[predicate]:
                changed = Valuation(list(valuation.items()))
                changed[predicate] = valuation[predicate] - {member}
                self.assertFalse(satisfies(changed, formula), (predicate, member))

    def test_principal_causes_mediations_and_roots_do_not_collapse(self):
        valuation, _ = valuation_and_formula(21)
        for predicate, targets in (
            ("PrincipalCause", ("sensual_fixation", "view_fixation")),
            ("MediatedBy", ("savor", "inversion")),
        ):
            self.assertEqual(valuation[predicate], {
                (valuation[factor], valuation[target])
                for factor, target in zip(("feeling", "reflection"), targets)
            })
            formula = Expression.fromstring(
                f"{predicate}(feeling,{targets[0]}) & "
                f"{predicate}(reflection,{targets[1]})"
            )
            changed = Valuation(list(valuation.items()))
            changed[predicate] = {
                (valuation["feeling"], valuation[targets[1]]),
                (valuation["reflection"], valuation[targets[0]]),
            }
            self.assertFalse(satisfies(changed, formula), predicate)
        self.assertEqual(len(valuation["DisputeRoot"]), 2)
        self.assertFalse(valuation["DisputeRoot"] & valuation["MentalFactor"])
        self.assertFalse(valuation["SoleCause"])
        same_person = Expression.fromstring(
            "exists x.(GreedyForSavor(x) & InvertedReflection(x) & Wanders(x))"
        )
        self.assertTrue(satisfies(valuation, same_person))
        changed = Valuation(list(valuation.items()))
        changed["InvertedReflection"] = {("another_person",)}
        self.assertFalse(satisfies(changed, same_person))

    def test_three_meanings_and_explanatory_axes_are_required(self):
        valuation, formula = valuation_and_formula(20)
        self.assertTrue(satisfies(valuation, formula))
        self.assertEqual(len(valuation["Meaning"]), 3)
        self.assertEqual(len({value for _, value in valuation["Meaning"]}), 3)
        self.assertEqual(
            valuation["Teaching"],
            {(valuation[name],) for name in ("base", "essence", "principle")},
        )
        self.assertEqual(len(valuation["Teaching"]), 3)
        for predicate in (
            "Meaning", "Threefold", "ExplainsThreeTeachings", "ThreeTeachings"
        ):
            for member in valuation[predicate]:
                changed = Valuation(list(valuation.items()))
                changed[predicate] = valuation[predicate] - {member}
                self.assertFalse(satisfies(changed, formula), (predicate, member))

    def test_learner_axes_have_three_ordered_values_without_fixed_profiles(self):
        valuation, _ = valuation_and_formula(20)
        for predicate, values in (
            ("SuitedToConfusion", ("mental_factors", "form", "form_and_consciousness")),
            ("SuitedToFaculty", ("sharp", "middling", "weak")),
            ("SuitedToInclination", ("brief", "intermediate", "extensive")),
        ):
            expected = {
                (valuation[teaching], valuation[value])
                for teaching, value in zip(("base", "essence", "principle"), values)
            }
            self.assertEqual(valuation[predicate], expected)
            self.assertEqual(len({value for _, value in expected}), 3)
            formula = Expression.fromstring(" & ".join(
                f"{predicate}({teaching},{value})"
                for teaching, value in zip(("base", "essence", "principle"), values)
            ))
            changed = Valuation(list(valuation.items()))
            changed[predicate] = {
                (valuation["base"], valuation[values[1]]),
                (valuation["essence"], valuation[values[0]]),
                (valuation["principle"], valuation[values[2]]),
            }
            self.assertFalse(satisfies(changed, formula), predicate)
        self.assertTrue(
            valuation["Unconditioned"] <= valuation["PrincipleMember"]
        )
        self.assertFalse(valuation["Unconditioned"] & valuation["HomogeneousCause"])

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

    def test_order_of_the_six_separates_reasons_grounds_and_site(self):
        valuation, formula = valuation_and_formula(23)
        self.assertTrue(satisfies(valuation, formula))
        faculties = ("eye", "ear", "nose", "tongue", "body", "mind")
        values = {valuation[name] for name in faculties}
        self.assertEqual(len(values), 6)
        precedes = valuation["Precedes"]
        self.assertEqual(len(precedes), 5)
        firsts = {a for a, _ in precedes}
        seconds = {b for _, b in precedes}
        self.assertEqual(firsts - seconds, {valuation["eye"]})
        self.assertEqual(seconds - firsts, {valuation["mind"]})
        groups = valuation["InGroup"]
        five = {x for x, g in groups if g == valuation["five_faculties"]}
        four = {x for x, g in groups if g == valuation["first_four"]}
        self.assertTrue(four < five)
        self.assertIn(valuation["body"], five - four)
        self.assertNotIn(valuation["mind"], five | four)
        for predicate, item in (
            ("PrecedesBecause", (valuation["five_faculties"], valuation["mind"], valuation["present_conditions"])),
            ("PrecedesBecause", (valuation["first_four"], valuation["body"], valuation["element_dependent_conditions"])),
            ("OrderedBy", (valuation["remaining_order"], valuation["farther_operation"])),
            ("OrderedBy", (valuation["remaining_order"], valuation["quicker_operation"])),
            ("AlternativelyOrderedBy", (valuation["six_order"], valuation["site"])),
        ):
            changed = Valuation(list(valuation.items()))
            changed[predicate] = valuation[predicate] - {item}
            self.assertFalse(satisfies(changed, formula), item)
        swapped = Valuation(list(valuation.items()))
        swapped["FartherOperation"] = valuation["QuickerOperation"]
        swapped["QuickerOperation"] = valuation["FartherOperation"]
        prose = Expression.fromstring(
            "FartherOperation(eye,ear) & QuickerOperation(nose,tongue)"
        )
        self.assertTrue(satisfies(valuation, prose))
        self.assertFalse(satisfies(swapped, prose))
        self.assertTrue(satisfies(valuation, Expression.fromstring(
            "exists x.(Unlocalized(x) & DependsOnFaculties(x) & -Unconditioned(x))"
        )))

    def test_two_names_are_unique_and_grounded_differently(self):
        valuation, formula = valuation_and_formula(24)
        self.assertTrue(satisfies(valuation, formula))
        form_base = valuation["InFormBase"]
        self.assertEqual(len(form_base), 10)
        named = valuation["HasSpecificName"]
        self.assertEqual(len(named), 9)
        self.assertEqual(form_base - named, {(valuation["form_essence"],)})
        pairs = valuation["CorrespondsTo"]
        self.assertEqual(len({a for a, _ in pairs}), 5)
        self.assertEqual(len({b for _, b in pairs}), 5)
        for extra in (
            (valuation["sound"], valuation["form_name"]),
            ("mind_ess", valuation["dharma_name"]),
        ):
            changed = Valuation(list(valuation.items()))
            changed["CalledBy"] = valuation["CalledBy"] | {extra}
            self.assertFalse(satisfies(changed, formula), extra)
        for predicate, item in (
            ("NamedForPrimacy", (valuation["form_essence"],)),
            ("GathersHighest", (valuation["dharma_essence"],)),
            ("NamedForDistinction", (valuation["dharma_essence"],)),
        ):
            changed = Valuation(list(valuation.items()))
            changed[predicate] = valuation[predicate] - {item}
            self.assertFalse(satisfies(changed, formula), predicate)
        self.assertEqual(valuation["Highest"], {(valuation["nirvana"],)})
        self.assertNotIn((valuation["nirvana"],), valuation["Base"])
        self.assertFalse(satisfies(valuation, Expression.fromstring(
            "all x.(DharmaByNature(x) -> CalledBy(x,dharma_name))"
        )))

    def test_scriptural_names_resolve_by_account_without_new_base(self):
        valuation, formula = valuation_and_formula(25)
        self.assertTrue(satisfies(valuation, formula))
        speech, name = valuation["speech_nature"], valuation["name_nature"]
        form, formations = valuation["form_base"], valuation["formations_base"]
        for c in ("collection_a", "collection_b"):
            for item in ((c, speech, form), (c, name, formations)):
                changed = Valuation(list(valuation.items()))
                changed["IncludedUnder"] = valuation["IncludedUnder"] - {item}
                self.assertFalse(satisfies(changed, formula), item)
        for predicate, item in (
            ("ReportedAccount", (speech,)),
            ("ReportedAccount", (name,)),
            ("Alternative", (speech, name)),
        ):
            changed = Valuation(list(valuation.items()))
            changed[predicate] = valuation[predicate] - {item}
            self.assertFalse(satisfies(changed, formula), item)
        swapped = Valuation(list(valuation.items()))
        swapped["IncludedUnder"] = {
            (c, a, formations if b == form else form)
            for c, a, b in valuation["IncludedUnder"]
        }
        self.assertFalse(satisfies(swapped, formula))
        self.assertFalse(satisfies(swapped, Expression.fromstring(
            "all c.(DharmaCollection(c) -> (-IncludedUnder(c,speech_nature,formations_base) & -IncludedUnder(c,name_nature,form_base)))"
        )))
        bases = {x for (x,) in valuation["Base"]}
        collections = {x for (x,) in valuation["DharmaCollection"]}
        self.assertFalse(bases & collections)
        self.assertEqual(valuation["Selected"], set())

    def test_three_measures_are_attributed_and_tu_does_not_refute(self):
        valuation, formula = valuation_and_formula(26)
        self.assertTrue(satisfies(valuation, formula))
        for predicate, item in (
            ("Holds", (valuation["some_teachers"], valuation["treatise_measure"])),
            ("Holds", (valuation["other_teachers"], valuation["exposition_measure"])),
            ("Distributive", (valuation["exposition_measure"],)),
            ("ContrastsWith", (valuation["counteragent_measure"], valuation["treatise_measure"])),
            ("ContrastsWith", (valuation["counteragent_measure"], valuation["exposition_measure"])),
            ("DescribedAs", (valuation["dharma_collection"], valuation["counteragent_measure"])),
        ):
            changed = Valuation(list(valuation.items()))
            changed[predicate] = valuation[predicate] - {item}
            self.assertFalse(satisfies(changed, formula), item)
        self.assertEqual(valuation["Refuted"], set())
        topics = {t for (t,) in valuation["Topic"]}
        expositions = valuation["ExpositionOf"]
        self.assertEqual({t for _, t in expositions}, topics)
        self.assertEqual(len({x for x, _ in expositions}), len(topics))
        counter = valuation["Counteragent"]
        self.assertEqual(len({c for c, _ in counter}), len({d for _, d in counter}))
        merged = Valuation(list(valuation.items()))
        merged["Counteragent"] = {("counter_a", d) for _, d in counter}
        self.assertTrue(satisfies(merged, Expression.fromstring(
            "exists c d f.(Counteragent(c,d) & Counteragent(c,f) & -(d = f))"
        )))
        collections = {x for (x,) in valuation["DharmaCollection"]}
        self.assertFalse(collections & {x for (x,) in valuation["Base"]})

    def test_assignment_requires_determination_and_established_place(self):
        valuation, formula = valuation_and_formula(27)
        self.assertTrue(satisfies(valuation, formula))
        for x, k in list(valuation["DeterminedBeforeAssignment"])[:4]:
            changed = Valuation(list(valuation.items()))
            changed["DeterminedBeforeAssignment"] = (
                valuation["DeterminedBeforeAssignment"] - {(x, k)}
            )
            self.assertFalse(satisfies(changed, formula), x)
        for place in ("rupa_skandha", "dharma_ayatana"):
            changed = Valuation(list(valuation.items()))
            changed["Established"] = valuation["Established"] - {(place,)}
            self.assertFalse(satisfies(changed, formula), place)
        assigned = valuation["ToBeAssigned"]
        places = lambda x: {p for y, p in assigned if y == x}
        for attended, principal in valuation["AttendedOf"]:
            self.assertTrue(places(principal) < places(attended), attended)
        nonpercipient = places("asamjnisattva")
        self.assertEqual(len(nonpercipient), 10)
        self.assertFalse(nonpercipient & {"gandha_ayatana", "rasa_ayatana"})
        self.assertEqual(valuation["CognitionOccurring"], set())
        self.assertEqual(places("sila_coll"), {"rupa_skandha"})

    def test_six_principles_map_four_one_one_without_new_principle(self):
        valuation, formula = valuation_and_formula(28)
        self.assertTrue(satisfies(valuation, formula))
        members = {x for (x,) in valuation["InSixfold"]}
        self.assertEqual(len(members), 6)
        targets = {}
        for x, t in valuation["IncludedIn"]:
            targets.setdefault(t, set()).add(x)
        self.assertEqual(sorted(len(v) for v in targets.values()), [1, 1, 4])
        self.assertEqual(targets["sprastavya_dhatu"], {"earth_m", "water_m", "fire_m", "wind_m"})
        self.assertEqual(targets["rupa_dhatu"], {"opening_m"})
        for predicate, item in (
            ("ReportedNature", ("opening_m", "aloka_tamas")),
            ("Impure", ("impure_cognition_m",)),
            ("SupportOfBirth", ("earth_m",)),
        ):
            changed = Valuation(list(valuation.items()))
            changed[predicate] = valuation[predicate] - {item}
            self.assertFalse(satisfies(changed, formula), item)
        self.assertTrue(satisfies(valuation, Expression.fromstring(
            "exists z.(Pure(z) & Cognition(z) & -Unconditioned(z) & -Named(z,cognition_principle))"
        )))
        self.assertFalse(satisfies(valuation, Expression.fromstring(
            "exists x.(Named(x,space_principle) & Unconditioned(x))"
        )))

    def test_three_counts_are_extensional_and_resistance_cross_classifies(self):
        valuation, formula = valuation_and_formula(29)
        self.assertTrue(satisfies(valuation, formula))
        self.assertEqual(len(valuation["AmongEighteen"]), 18)
        self.assertEqual(len(valuation["Visible"]), 1)
        self.assertEqual(len(valuation["Resistant"]), 10)
        self.assertEqual(len(valuation["OnlyIndeterminate"]), 8)
        self.assertTrue(valuation["OnlyIndeterminate"] < valuation["Resistant"])
        for predicate, item in (
            ("Visible", ("sabda_d",)),
            ("OnlyIndeterminate", ("sabda_d",)),
            ("Resistant", ("mano_d",)),
        ):
            changed = Valuation(list(valuation.items()))
            changed[predicate] = valuation[predicate] | {item}
            self.assertFalse(satisfies(changed, formula), item)
        not_a_base = Expression.fromstring("-AmongEighteen(form_base) & -Visible(form_base)")
        self.assertTrue(satisfies(valuation, not_a_base))
        changed = Valuation(list(valuation.items()))
        changed["Visible"] = valuation["Visible"] | {("rupa_skandha",)}
        self.assertTrue(satisfies(changed, formula))
        self.assertFalse(satisfies(changed, not_a_base))
        obstruction = valuation["ObstructionResistant"]
        condition = valuation["ConditionResistant"]
        items = valuation["Item"]
        self.assertEqual(len(items), 19)
        self.assertEqual(len(condition - obstruction), 8)
        self.assertEqual(len(obstruction - condition), 5)
        self.assertEqual(len(obstruction & condition), 5)
        self.assertEqual(len(items - obstruction - condition), 1)
        self.assertTrue(valuation["SupportResistant"] <= condition)
        self.assertEqual(condition - valuation["SupportResistant"],
                         valuation["SenseFaculty"])

    def test_realm_counts_keep_base_principle_and_realm_levels_apart(self):
        valuation, formula = valuation_and_formula(30)
        self.assertTrue(satisfies(valuation, formula))
        eighteen = valuation["AmongEighteen"]
        others = eighteen - valuation["OnlyIndeterminate"]
        self.assertEqual(len(others), 10)
        self.assertTrue(others <= valuation["Threefold"])
        realm = lambda r: {x for x, y in valuation["ConnectedWith"] if y == r}
        self.assertEqual(len(realm("kama_dhatu")), 18)
        self.assertEqual(len(realm("rupa_dhatu_realm")), 14)
        self.assertTrue({"ghrana_d", "jihva_d", "sprastavya_d"} <= realm("rupa_dhatu_realm"))
        self.assertFalse({"gandha_d", "rasa_d", "ghranavijnana_d", "jihvavijnana_d"} & realm("rupa_dhatu_realm"))
        self.assertFalse(valuation["BaseLevel"] & valuation["Principle"])
        self.assertFalse(valuation["RealmLevel"] & eighteen)
        self.assertTrue(valuation["RealmLevel"] <= valuation["Principle"])
        self.assertEqual(valuation["Principle"], eighteen | valuation["RealmLevel"])
        gathered = {x for x, base in valuation["GatheredIn"] if base == valuation["form_base"]}
        self.assertEqual(gathered, {x for (x,) in valuation["FormBearing"]})
        self.assertNotIn((valuation["form_base"],), eighteen)
        self.assertNotEqual(valuation["form_realm"], valuation["visible_form"])
        changed = Valuation(list(valuation.items()))
        changed["ConnectedWith"] = valuation["ConnectedWith"] - {("ghrana_d", "rupa_dhatu_realm")}
        self.assertFalse(satisfies(changed, formula))

    def test_formless_three_and_instance_level_purity(self):
        valuation, formula = valuation_and_formula(31)
        self.assertTrue(satisfies(valuation, formula))
        formless = {x for x, r in valuation["ConnectedWith"] if r == valuation["formless_realm"]}
        self.assertEqual(formless, {"mano_d", "dharma_d", "manovijnana_d"})
        fifteen = {x for (x,) in valuation["AmongEighteen"]} - formless
        self.assertEqual(len(fifteen), 15)
        form_natured = {x for (x,) in valuation["FormNatured"]}
        taking = {x for y, x in valuation["SupportAndCondition"] if y in form_natured}
        self.assertEqual(fifteen, form_natured | taking)
        pure_of = lambda p: {i for i, x in valuation["InstanceOf"] if x == p and (i,) in valuation["Pure"]}
        for principle in formless:
            self.assertTrue(pure_of(principle), principle)
        for principle in fifteen:
            self.assertFalse(pure_of(principle), principle)
        unconditioned = {i for (i,) in valuation["Unconditioned"]}
        self.assertTrue(unconditioned and unconditioned <= pure_of("dharma_d"))
        self.assertNotEqual(valuation["dharma_principle"], valuation["dharma_essence"])
        changed = Valuation(list(valuation.items()))
        changed["HasPureInstance"] = valuation["HasPureInstance"] | {("rupa_d",)}
        self.assertFalse(satisfies(changed, formula))
        link = Expression.fromstring(
            "all x.(HasPureInstance(x) <-> exists i.(InstanceOf(i,x) & Pure(i)))"
        )
        self.assertTrue(satisfies(valuation, link))
        changed = Valuation(list(valuation.items()))
        changed["Pure"] = valuation["Pure"] | {("rupa_d_imp",)}
        self.assertFalse(satisfies(changed, link))

    def test_kinds_run_by_portion_and_level_with_a_fourth_kind(self):
        valuation, formula = valuation_and_formula(32)
        self.assertTrue(satisfies(valuation, formula))
        groups = [valuation[p] for p in ("FiveCognition", "LastThree", "FormNatured")]
        self.assertEqual(sum(len(g) for g in groups), 18)
        self.assertEqual(groups[0] | groups[1] | groups[2], valuation["AmongEighteen"])
        kinds = lambda x: {k for y, k in valuation["Kind"] if y == x}
        self.assertEqual(len(kinds("dharma_d")), 4)
        self.assertEqual(len(kinds("mano_d")), 3)
        self.assertEqual(len(kinds("manovijnana_d")), 3)
        for (level,) in valuation["BothLevel"]:
            present = {k for _, l, k in valuation["KindAt"] if l == level}
            self.assertEqual(len(present), 4, level)
        for item in ("vitarka_i", "vicara_i"):
            self.assertNotIn("both_k", {k for i, _, k in valuation["KindAt"] if i == item})
        changed = Valuation(list(valuation.items()))
        changed["Kind"] = valuation["Kind"] | {("caksurvijnana_d", "neither_k")}
        self.assertFalse(satisfies(changed, formula))

    def test_avikalpaka_is_by_privation_of_two_kinds(self):
        valuation, formula = valuation_and_formula(33)
        self.assertTrue(satisfies(valuation, formula))
        kinds = {k for _, k in valuation["Vikalpa"]}
        self.assertEqual(len(kinds), 3)
        owned = lambda x: {p for y, p in valuation["Possesses"] if y == x}
        for (x,) in valuation["FiveCognition"]:
            self.assertIn("vitarka_i", owned(x))
            self.assertIn("prajna_sense", owned(x))
        self.assertNotIn(("prajna_sense",), valuation["Mental"])
        recollective = {p for p, k in valuation["Vikalpa"] if k == "recollective_k"}
        self.assertTrue(recollective & {p for (p,) in valuation["Concentrated"]})
        changed = Valuation(list(valuation.items()))
        changed["Vikalpa"] = valuation["Vikalpa"] | {("prajna_samahita", "examining_k")}
        self.assertFalse(satisfies(changed, formula))
        changed = Valuation(list(valuation.items()))
        changed["Possesses"] = valuation["Possesses"] | {("caksurvijnana_d", "smrti_vyagra")}
        self.assertFalse(satisfies(changed, formula))

    def test_support_and_appropriation_are_disjoint_cuts(self):
        valuation, formula = valuation_and_formula(34)
        self.assertTrue(satisfies(valuation, formula))
        support = {x for (x,) in valuation["TakesSupport"]}
        appropriated_of = {x for i, x in valuation["InstanceOf"]
                           if (i,) in valuation["Appropriated"]}
        self.assertFalse(support & appropriated_of)
        self.assertIn("dharma_samprayukta", support)
        self.assertNotIn("dharma_asamprayukta", support)
        self.assertEqual(len(appropriated_of), 9)
        changed = Valuation(list(valuation.items()))
        changed["Appropriated"] = valuation["Appropriated"] | {("sabda_present",)}
        self.assertFalse(satisfies(changed, formula))
        changed = Valuation(list(valuation.items()))
        changed["Appropriated"] = valuation["Appropriated"] - {("gandha_bound",)}
        self.assertFalse(satisfies(changed, formula))

    def test_great_elements_stay_inside_the_tangible(self):
        valuation, formula = valuation_and_formula(35)
        self.assertTrue(satisfies(valuation, formula))
        holders = {x for i, x in valuation["InstanceOf"]
                   if (i,) in valuation["GreatElement"]}
        self.assertEqual(holders, {"sprastavya_d"})
        self.assertEqual(len(valuation["GreatElement"]), 4)
        self.assertIn(("avijnapti_i",), valuation["ElementDependent"])
        self.assertNotIn(("dharma_avijnapti",), valuation["Accumulated"])
        changed = Valuation(list(valuation.items()))
        changed["ElementDependent"] = valuation["ElementDependent"] - {("sabda_i",)}
        self.assertFalse(satisfies(changed, formula))
        changed = Valuation(list(valuation.items()))
        changed["GreatElement"] = frozenset()
        self.assertFalse(satisfies(changed, formula))

    def test_dispute_takes_the_converse_voices(self):
        valuation, formula = valuation_and_formula(36)
        self.assertTrue(satisfies(valuation, formula))
        outer = set(valuation["OuterFour"])
        for role in ("Cuts", "IsCut", "IsBurned", "Weighs"):
            self.assertEqual(set(valuation[role]), outer)
        self.assertFalse(set(valuation["SenseFaculty"]) & outer)
        self.assertNotIn(("sabda_d",), outer)
        burners = {x for p, x in valuation["BurnerIn"] if p == "kecid_b"}
        self.assertEqual(burners, {"tejas_i"})
        self.assertNotIn(("tejas_i",), valuation["AmongEighteen"])
        changed = Valuation(list(valuation.items()))
        changed["Weighs"] = valuation["Weighs"] - {("gandha_d",)}
        self.assertFalse(satisfies(changed, formula))

    def test_genesis_modes_are_read_through_instances(self):
        valuation, formula = valuation_and_formula(37)
        self.assertTrue(satisfies(valuation, formula))
        modes = lambda x: {m for i, m in valuation["Born"]
                           if (i, x) in valuation["InstanceOf"]}
        self.assertEqual(modes("caksur_d"), {"vipaka_m", "upacaya_m"})
        self.assertEqual(modes("sabda_d"), {"upacaya_m", "naisyandika_m"})
        self.assertEqual(modes("dharma_d"), {"naisyandika_m", "vipaka_m"})
        self.assertIn(("dharma_asamskrta",), valuation["Unconditioned"])
        changed = Valuation(list(valuation.items()))
        changed["Born"] = valuation["Born"] | {("sabda_brahma", "vipaka_m")}
        self.assertFalse(satisfies(changed, formula))
        changed = Valuation(list(valuation.items()))
        changed["Born"] = valuation["Born"] - {("mano_vip", "vipaka_m")}
        self.assertFalse(satisfies(changed, formula))

    def test_one_dravya_and_one_moment_without_continuity(self):
        valuation, formula = valuation_and_formula(38)
        self.assertTrue(satisfies(valuation, formula))
        self.assertEqual(set(valuation["DravyaBearing"]), {("dharma_d",)})
        first = {i for i, k in valuation["InMoment"]}
        self.assertFalse(first & {i for i, _ in valuation["Born"]})
        both = {c for c, x in valuation["Acquires"] if x == "caksur_d"} & \
            {c for c, x in valuation["Acquires"] if x == "caksurvijnana_d"}
        self.assertEqual(both, {"arupya_to_kama", "arupya_to_brahmaloka"})
        changed = Valuation(list(valuation.items()))
        changed["DravyaBearing"] = valuation["DravyaBearing"] | {("rupa_d",)}
        self.assertFalse(satisfies(changed, formula))
        changed = Valuation(list(valuation.items()))
        changed["Acquires"] = valuation["Acquires"] - {
            ("dhyana2_sammukhi", "caksurvijnana_d"),
            ("dhyana2_to_adhah", "caksurvijnana_d")}
        self.assertFalse(satisfies(changed, formula))

    def test_sabhaga_is_said_of_instances_not_principles(self):
        valuation, formula = valuation_and_formula(39)
        self.assertTrue(satisfies(valuation, formula))
        failed = Valuation(list(valuation.items()))
        failed["Sabhaga"] = set(valuation["Sabhaga"]) - {("dharma_i",)}
        self.assertFalse(satisfies(failed, formula))
        lapsed = Valuation(list(valuation.items()))
        lapsed["TatSabhaga"] = set(valuation["TatSabhaga"]) - {("caksur_ceased",)}
        self.assertFalse(satisfies(lapsed, formula))

    def test_seeing_abandons_only_afflicted_mind_born_non_form(self):
        valuation, formula = valuation_and_formula(40)
        self.assertTrue(satisfies(valuation, formula))
        for instance in ("prthagjanatva_i", "apayika_karma_i", "caksurvijnana_raga_i"):
            widened = Valuation(list(valuation.items()))
            widened["DarsanaHeya"] = set(valuation["DarsanaHeya"]) | {(instance,)}
            self.assertFalse(satisfies(widened, formula), instance)

    def test_case_divides_whole_eye_from_dharma_portion(self):
        valuation, formula = valuation_and_formula(41)
        self.assertTrue(satisfies(valuation, formula))
        partial_eye = Valuation(list(valuation.items()))
        partial_eye["View"] = set(valuation["View"]) - {("caksur_tat_i",)}
        self.assertFalse(satisfies(partial_eye, formula))
        whole_dharma = Valuation(list(valuation.items()))
        whole_dharma["View"] = set(valuation["View"]) | {("vedana_i",), ("other_prajna_i",), ("five_prajna_i",)}
        self.assertFalse(satisfies(whole_dharma, formula))

    def test_passive_quantifies_away_the_agent_of_seeing(self):
        valuation, formula = valuation_and_formula(42)
        self.assertTrue(satisfies(valuation, formula))
        through_wall = Valuation(list(valuation.items()))
        through_wall["Sees"] = set(valuation["Sees"]) | {("eye_a", "wall_v")}
        self.assertFalse(satisfies(through_wall, formula))
        cognition_sees = Valuation(list(valuation.items()))
        cognition_sees["Sees"] = set(valuation["Sees"]) | {("cog_a", "moon_v")}
        self.assertFalse(satisfies(cognition_sees, formula))

    def test_anyathā_returns_the_converse_for_the_other_three(self):
        valuation, formula = valuation_and_formula(43)
        self.assertTrue(satisfies(valuation, formula))
        nose_unreached = Valuation(list(valuation.items()))
        nose_unreached["TakesUnreached"] = set(valuation["TakesUnreached"]) | {("nose_f",)}
        self.assertFalse(satisfies(nose_unreached, formula))
        one_eye_only = Valuation(list(valuation.items()))
        one_eye_only["BothEyes"] = set()
        self.assertFalse(satisfies(one_eye_only, formula))

    def test_ca_carries_the_past_basis_to_the_five(self):
        valuation, formula = valuation_and_formula(44)
        self.assertTrue(satisfies(valuation, formula))
        no_past_basis = Valuation(list(valuation.items()))
        no_past_basis["BasisOf"] = set(valuation["BasisOf"]) - {("pastmind_b", "eye_c")}
        self.assertFalse(satisfies(no_past_basis, formula))
        present_mind_basis = Valuation(list(valuation.items()))
        present_mind_basis["BasisOf"] = set(valuation["BasisOf"]) | {("mind_f", "mano_c")}
        self.assertFalse(satisfies(present_mind_basis, formula))

    def test_cognition_is_named_by_the_unshared_basis_not_the_shared_support(self):
        valuation, formula = valuation_and_formula(45)
        self.assertTrue(satisfies(valuation, formula))
        shared_eye = Valuation(list(valuation.items()))
        shared_eye["BasisOf"] = set(valuation["BasisOf"]) | {("eye_a", "eyecog_b")}
        self.assertFalse(satisfies(shared_eye, formula))
        named_by_support = Valuation(list(valuation.items()))
        named_by_support["NamedBy"] = (set(valuation["NamedBy"]) - {("eyecog_a", "eye_a")}) | {("eyecog_a", "blue_v")}
        self.assertFalse(satisfies(named_by_support, formula))

    def test_fixed_rules_and_sarvatah_need_cross_plane_seeing(self):
        valuation, formula = valuation_and_formula(46)
        self.assertTrue(satisfies(valuation, formula))
        eye_below_body = Valuation(list(valuation.items()))
        eye_below_body["Below"] = set(valuation["Below"]) | {("eye0", "body1")}
        eye_below_body["EyeIn"] = set(valuation["EyeIn"]) | {("s6", "eye0")}
        self.assertFalse(satisfies(eye_below_body, formula))
        level = {t: int(p[2]) if p.startswith("dh") else 0 for t, p in valuation["InPlane"]}
        desire_cognition = Valuation(list(valuation.items()))
        desire_cognition["CogIn"] = {(s, "cog0") for s, _ in valuation["CogIn"]}
        desire_cognition["Below"] = {(a, b) for a in level for b in level if level[a] < level[b]}
        self.assertFalse(satisfies(desire_cognition, formula))

    def test_exception_is_subtracted_from_the_general_rule(self):
        valuation, formula = valuation_and_formula(47)
        self.assertTrue(satisfies(valuation, formula))
        lowered_tangible = Valuation(list(valuation.items()))
        lowered_tangible["CondIn"] = (set(valuation["CondIn"]) - {("k3", "tang2")}) | {("k3", "tang1")}
        self.assertFalse(satisfies(lowered_tangible, formula))
        mind_fixed = Valuation(list(valuation.items()))
        mind_fixed["FacIn"] = set(valuation["FacIn"]) - {("n2", "mind1"), ("n3", "mind1")}
        self.assertFalse(satisfies(mind_fixed, formula))

    def test_two_knowers_permanent_portion_and_faculty_portion(self):
        valuation, formula = valuation_and_formula(48)
        self.assertTrue(satisfies(valuation, formula))
        third_knower = Valuation(list(valuation.items()))
        third_knower["Knows"] = set(valuation["Knows"]) | {("ecog_d", "sound_d")}
        self.assertFalse(satisfies(third_knower, formula))
        space_impermanent = Valuation(list(valuation.items()))
        space_impermanent["Permanent"] = set(valuation["Permanent"]) - {("space_u",)}
        self.assertFalse(satisfies(space_impermanent, formula))
        whole_dharma_faculty = Valuation(list(valuation.items()))
        whole_dharma_faculty["Faculty"] = set(valuation["Faculty"]) | {(x,) for x in ("space_u", "pratisamkhya_u", "apratisamkhya_u", "samjna_x")}
        self.assertFalse(satisfies(whole_dharma_faculty, formula))


if __name__ == "__main__":
    unittest.main()
