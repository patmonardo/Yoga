"""Check that the opening Indriya parses constrain count and Meaning scope."""

from pathlib import Path
import re
import unittest

from nltk.grammar import FeatureGrammar
from nltk.parse import FeatureChartParser
from nltk.sem import Assignment, Model

from audit_nltk_blocks import BLOCK, check_grammar, check_logic, load_valuation, section


STUDIES = Path(__file__).resolve().parents[1] / "02-indriya"


def study(number: int) -> str:
    return (STUDIES / f"VAK_2.{number:02d}.md").read_text(encoding="utf-8")


def grammar_and_tokens(text: str):
    block = next(body for kind, body in BLOCK.findall(section(text, 4))
                 if kind == "nltk-fcfg")
    tokens = re.search(r"^# tokens: (.*)$", block, re.M).group(1).split()
    return FeatureGrammar.fromstring(block), tokens


class IndriyaPilotTests(unittest.TestCase):
    def test_strict_parse_and_model(self):
        for number in range(1, 49):
            with self.subTest(verse=number):
                text = study(number)
                self.assertEqual(check_grammar(text, strict=True)[1], [])
                self.assertEqual(check_logic(text, strict=True)[1], [])

    def test_count_features_reject_wrong_readings(self):
        changes = (
            (1, "GROUP[CASE=gen,NUM=pl,CNT=4,SEM=<other_four>]",
             "GROUP[CASE=gen,NUM=pl,CNT=5,SEM=<other_four>]"),
            (2, "NUM[CNT=6,FIVE=", "NUM[CNT=5,FIVE="),
            (3, "NUM[CNT=5] -> 'pañca'", "NUM[CNT=3] -> 'pañca'"),
        )
        for number, old, new in changes:
            with self.subTest(verse=number):
                text = study(number)
                self.assertIn(old, text)
                changed = text.replace(old, new, 1)
                grammar, tokens = grammar_and_tokens(changed)
                self.assertEqual(list(FeatureChartParser(grammar).parse(tokens)), [])

    def test_minds_all_range_and_each_sensory_meaning_are_tested(self):
        text = study(2)
        grammar, tokens = grammar_and_tokens(text)
        verse = list(FeatureChartParser(grammar).parse(tokens))[0].label()["SEM"].simplify()
        blocks = dict(BLOCK.findall(section(text, 8)))
        valuation = load_valuation(blocks["nltk-valuation"])
        model = Model(valuation.domain, valuation)
        self.assertTrue(model.satisfy(verse, Assignment(model.domain)))

        valuation["Meaning"] = valuation["Meaning"] | {("uncovered_meaning",)}
        model = Model(valuation.domain, valuation)
        self.assertFalse(model.satisfy(verse, Assignment(model.domain)))

        valuation["Meaning"] = valuation["Meaning"] - {("uncovered_meaning",)}
        valuation["OwnMeaning"] = {
            pair for pair in valuation["OwnMeaning"] if pair[0] != "eye"
        }
        model = Model(valuation.domain, valuation)
        self.assertFalse(model.satisfy(verse, Assignment(model.domain)))

    def test_2_04_order_and_second_account_marker(self):
        text = study(4)
        grammar, tokens = grammar_and_tokens(text)
        verse = list(FeatureChartParser(grammar).parse(tokens))[0].label()["SEM"].simplify()
        blocks = dict(BLOCK.findall(section(text, 8)))
        valuation = load_valuation(blocks["nltk-valuation"])
        model = Model(valuation.domain, valuation)
        self.assertTrue(model.satisfy(verse, Assignment(model.domain)))

        valuation["GovernsAttainmentOf"] = {
            pair for pair in valuation["GovernsAttainmentOf"]
            if pair != ("first_f", "second_f")
        }
        model = Model(valuation.domain, valuation)
        self.assertFalse(model.satisfy(verse, Assignment(model.domain)))

        marker = "REASON[CASE=abl,ALT=other_account,SEM=?reason]"
        self.assertIn(marker, text)
        altered = text.replace(marker, "REASON[CASE=abl,ALT=open_list,SEM=?reason]", 1)
        grammar, tokens = grammar_and_tokens(altered)
        self.assertEqual(list(FeatureChartParser(grammar).parse(tokens)), [])

    def test_2_05_both_extent_directions_and_anaphor(self):
        text = study(5)
        grammar, tokens = grammar_and_tokens(text)
        verse = list(FeatureChartParser(grammar).parse(tokens))[0].label()["SEM"].simplify()
        blocks = dict(BLOCK.findall(section(text, 8)))
        valuation = load_valuation(blocks["nltk-valuation"])
        model = Model(valuation.domain, valuation)
        self.assertTrue(model.satisfy(verse, Assignment(model.domain)))
        self.assertEqual(len(valuation["FacultyHere"]), 22)
        self.assertEqual(
            [len(valuation[name]) for name in
             ("BasisOfConsciousness", "Differentiates", "Sustains",
              "Defiles", "EquipsPurification", "Purifies")],
            [6, 2, 1, 5, 5, 3],
        )

        valuation["FacultyHere"] = valuation["FacultyHere"] | {("speech",)}
        model = Model(valuation.domain, valuation)
        self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        valuation["FacultyHere"] = valuation["FacultyHere"] - {("speech",)}

        valuation["BasisOfConsciousness"] = (
            valuation["BasisOfConsciousness"] | {("extra_basis_power",)}
        )
        model = Model(valuation.domain, valuation)
        self.assertFalse(model.satisfy(verse, Assignment(model.domain)))

        marker = "DIFF[CASE=nom,REF=basis_six,SEM="
        self.assertIn(marker, text)
        altered = text.replace(marker, "DIFF[CASE=nom,REF=other_basis,SEM=", 1)
        grammar, tokens = grammar_and_tokens(altered)
        self.assertEqual(list(FeatureChartParser(grammar).parse(tokens)), [])

    def test_2_06_parallel_courses_and_fourteen_count(self):
        text = study(6)
        grammar, tokens = grammar_and_tokens(text)
        verse = list(FeatureChartParser(grammar).parse(tokens))[0].label()["SEM"].simplify()
        blocks = dict(BLOCK.findall(section(text, 8)))
        valuation = load_valuation(blocks["nltk-valuation"])
        model = Model(valuation.domain, valuation)
        self.assertTrue(model.satisfy(verse, Assignment(model.domain)))
        self.assertEqual(len(valuation["EngagementFaculty"]), 14)
        self.assertEqual(len(valuation["WithdrawalFaculty"]), 8)
        self.assertFalse(valuation["EngagementFaculty"] & valuation["WithdrawalFaculty"])

        valuation["ExperienceSlot"] = {("engagement_course",)}
        model = Model(valuation.domain, valuation)
        self.assertFalse(model.satisfy(verse, Assignment(model.domain)))

        changed = text.replace("CNT=14,SEM=?count]", "CNT=8,SEM=?count]", 1)
        self.assertNotEqual(changed, text)
        grammar, tokens = grammar_and_tokens(changed)
        self.assertEqual(list(FeatureChartParser(grammar).parse(tokens)), [])

    def test_2_08_scope_neutral_modes_and_classification(self):
        text = study(8)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [3, 4, 5])
        verse = tree.label()["SEM"].simplify()
        blocks = dict(BLOCK.findall(section(text, 8)))
        valuation = load_valuation(blocks["nltk-valuation"])
        model = Model(valuation.domain, valuation)
        self.assertTrue(model.satisfy(verse, Assignment(model.domain)))

        for predicate, pairs in (
            ("ClassifiedAs", tuple(valuation["ClassifiedAs"] - {
                ("third_pleasure", "pleasure_faculty"),
            })),
            ("HasMode", tuple(valuation["HasMode"])),
            ("UnifiedBecause", tuple(valuation["UnifiedBecause"])),
        ):
            for pair in pairs:
                with self.subTest(predicate=predicate, removed=pair):
                    original = valuation[predicate]
                    valuation[predicate] = original - {pair}
                    model = Model(valuation.domain, valuation)
                    self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
                    valuation[predicate] = original

        valuation["Elsewhere"] = valuation["Elsewhere"] | {("third_pleasure",)}
        model = Model(valuation.domain, valuation)
        self.assertFalse(model.satisfy(verse, Assignment(model.domain)))

        for old, new in (
            ("ELSEWHERE[SCOPE=outside_third,SEM=<",
             "ELSEWHERE[SCOPE=all_levels,SEM=<"),
            ("THAT[CASE=nom,NUM=sg,GEN=f,REF=agreeable_mental,SEM=<",
             "THAT[CASE=nom,NUM=sg,GEN=f,REF=bodily_feeling,SEM=<"),
            ("BOTH[CASE=nom,NUM=sg,GEN=f,CNT=2,SEM=<",
             "BOTH[CASE=nom,NUM=sg,GEN=f,CNT=1,SEM=<"),
            ("REASON[CASE=abl,RESPECT=remaining_neutral,SEM=<",
             "REASON[CASE=nom,RESPECT=remaining_neutral,SEM=<"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(
                    list(FeatureChartParser(changed).parse(changed_tokens)), [],
                )

        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.08_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))


    def test_2_09_partition_path_order_and_dual(self):
        text = study(9)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [3, 2, 4, 2])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        triad = {item[0] for item in valuation["RealizationFaculty"]}
        form = {item[0] for item in valuation["FormFaculty"]}
        outflow_only = form | {"life", "pain", "distress"}
        nine = {item[0] for item in valuation["NineType"]}
        self.assertEqual((len(triad), len(outflow_only), len(nine)), (3, 10, 9))
        self.assertEqual(len(triad | outflow_only | nine), 22)
        self.assertTrue({(item,) for item in outflow_only} <= valuation["WithOutflowsOnly"])
        self.assertTrue(valuation["FaithGroup"] <= valuation["NineType"])
        for name in ("CanHaveOutflows", "CanBeWithoutOutflows"):
            self.assertEqual(valuation[name], valuation["NineType"])
        self.assertEqual(valuation["NamedOn"], {
            ("nine_types", "seeing_path", "shall_know"),
            ("nine_types", "cultivation_path", "knowledge"),
            ("nine_types", "no_more_training_path", "one_who_has_known"),
        })

        for old, new in (
            ("PAIR[CASE=nom,NUM=du,GEN=n,CNT=2,SEM=<",
             "PAIR[CASE=loc,NUM=sg,GEN=n,CNT=2,SEM=<"),
            ("NINE[CNT=9,REF=nine_types,SEM=<",
             "NINE[CNT=8,REF=nine_types,SEM=<"),
            ("AMALA[CASE=nom,NUM=sg,GEN=n,SEM=<",
             "AMALA[CASE=nom,NUM=pl,GEN=n,SEM=<"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])

        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.09_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))


    def test_2_10_two_partitions_life_exception_and_anaphor(self):
        text = study(10)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [2, 6, 4, 2])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        received = [{"life"}, {x[0] for x in valuation["TwelveType"]},
                    {x[0] for x in valuation["NeverMaturation"]}]
        productive = [{"distress"}, {x[0] for x in valuation["TenType"]},
                      {x[0] for x in valuation["NeverProduces"]}]
        self.assertEqual([len(group) for group in received], [1, 12, 9])
        self.assertEqual([len(group) for group in productive], [1, 10, 11])
        for groups in (received, productive):
            self.assertEqual(len(set.union(*groups)), 22)
        self.assertEqual(set.union(*received), set.union(*productive))
        self.assertEqual(
            valuation["NeverMaturation"],
            valuation["FinalEightType"] | {("distress",)},
        )
        self.assertNotIn(("concentration_life_event",), valuation["IsMaturation"])
        self.assertIn(("concentration_life_event",), valuation["LifeInstance"])
        self.assertIn(("distress",), valuation["CanProduce"])
        self.assertNotIn(("distress",), valuation["CanBeMaturation"])
        self.assertIn(("mind",), valuation["CanProduce"])

        for old, new in (
            ("THAT[CASE=nom,NUM=sg,GEN=n,REF=distress,SEM=<",
             "THAT[CASE=nom,NUM=sg,GEN=n,REF=life,SEM=<"),
            ("PRODUCES[CASE=nom,NUM=sg,GEN=n,AXIS=has_result,SEM=<",
             "PRODUCES[CASE=nom,NUM=sg,GEN=n,AXIS=is_result,SEM=<"),
            ("TWELVE[CNT=12,SEM=<", "TWELVE[CNT=10,SEM=<"),
            ("EIGHT[CASE=abl,CNT=8] ->", "EIGHT[CASE=nom,CNT=8] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])

        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.10_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        self.assertIn("> niṣṭhitam ānuṣaṅgikam //", section(bhasya, 2))
        self.assertIn("> anyad avipākam iti siddham /", section(bhasya, 2))


    def test_2_11_ethical_partition_and_previous_ten(self):
        text = study(11)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [2, 2, 2, 5, 2])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        groups = [valuation["WholesomeEightType"], {("distress",)},
                  valuation["ThreefoldType"], valuation["RemainderType"]]
        self.assertEqual([len(group) for group in groups], [8, 1, 5, 8])
        self.assertEqual(len(set.union(*groups)), 22)
        self.assertEqual(
            valuation["ThreefoldType"],
            valuation["OtherFeelingType"] | {("mind",)},
        )
        self.assertEqual(len(valuation["PreviousTenType"]), 10)
        self.assertNotEqual(valuation["PreviousTenType"], groups[0])
        for predicate in ("CanBeWholesome", "CanBeUnwholesome", "CanBeIndeterminate"):
            self.assertIn(("neutral",), valuation[predicate])
        self.assertIn(("distress",), valuation["CanBeWholesome"])
        self.assertNotIn(("distress",), valuation["CanBeIndeterminate"])

        verse = tree.label()["SEM"].simplify()
        valuation["CompletesPreviousTen"] = False
        model = Model(valuation.domain, valuation)
        self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        for old, new in (
            ("CARRY[SCOPE=previous_ten,SEM=<",
             "CARRY[SCOPE=wholesome_eight,SEM=<"),
            ("EIGHT[CASE=nom,NUM=sg,GEN=n,CNT=8,SEM=<",
             "EIGHT[CASE=nom,NUM=sg,GEN=n,CNT=10,SEM=<"),
            ("FEELING[CASE=nom,NUM=sg,GEN=f,REF=other_four] ->",
             "FEELING[CASE=nom,NUM=sg,GEN=f,REF=all_five] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])

        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.11_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))


    def test_2_12_cumulative_realm_exclusions(self):
        text = study(12)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [3, 5, 6])
        verse = tree.label()["SEM"].simplify()
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        ranges = [
            {faculty for faculty, realm in valuation["CanConnect"] if realm == name}
            for name in ("desire", "form", "formless")
        ]
        self.assertEqual([len(group) for group in ranges], [19, 15, 8])
        self.assertTrue(ranges[2] < ranges[1] < ranges[0])
        self.assertEqual(ranges[2], {x[0] for x in valuation["FormlessRemainder"]})
        self.assertFalse({x[0] for x in valuation["Stainless"]} & set.union(*ranges))
        self.assertEqual({x[0] for x in valuation["PleasantFaculty"]}, {"pleasure", "gladness"})
        self.assertEqual(len(ranges[1] & {x[0] for x in valuation["FormFaculty"]}), 5)
        model = Model(valuation.domain, valuation)
        self.assertTrue(model.satisfy(verse, Assignment(model.domain)))
        original = valuation["CanConnect"]
        for pair in (("gladness", "formless"), ("shall_know", "form"), ("male", "form")):
            with self.subTest(extra=pair):
                valuation["CanConnect"] = original | {pair}
                model = Model(valuation.domain, valuation)
                self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        for pair in (("mind", "formless"), ("pain", "desire"), ("gladness", "form")):
            with self.subTest(missing=pair):
                valuation["CanConnect"] = original - {pair}
                model = Model(valuation.domain, valuation)
                self.assertFalse(model.satisfy(verse, Assignment(model.domain)))

        for old, new in (
            ("PLEASANT[CASE=acc,NUM=du,CNT=2,SEM=<",
             "PLEASANT[CASE=acc,NUM=sg,CNT=1,SEM=<"),
            ("PAINFUL[CASE=acc,NUM=du,CNT=2,SEM=<",
             "PAINFUL[CASE=loc,NUM=sg,CNT=2,SEM=<"),
            ("STAINLESS[CASE=acc,SEM=<", "STAINLESS[CASE=nom,SEM=<"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])

        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.12_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))


    def test_2_13_abandonment_partition_and_faith_instances(self):
        text = study(13)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [2, 2, 2, 4, 2])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        groups = [valuation["FourType"], {("distress",)}, valuation["NineType"],
                  valuation["FaithType"], valuation["RealizationType"]]
        self.assertEqual([len(group) for group in groups], [4, 1, 9, 5, 3])
        self.assertEqual(len(set.union(*groups)), 22)
        self.assertIn(("pain",), valuation["NineType"])
        self.assertNotIn(("pain",), valuation["FourType"])
        self.assertEqual(valuation["ByCultivation"], valuation["WithOutflows"])
        self.assertEqual(valuation["NotToAbandon"], valuation["WithoutOutflows"])
        self.assertFalse(valuation["ByCultivation"] & valuation["NotToAbandon"])
        self.assertEqual(
            valuation["FaithInstance"],
            valuation["WithOutflows"] | valuation["WithoutOutflows"],
        )
        self.assertEqual(
            valuation["CanSeeing"], valuation["FourType"] | {("distress",)},
        )
        self.assertEqual(
            valuation["CanNotAbandon"],
            valuation["FourType"] | valuation["FaithType"] | valuation["RealizationType"],
        )
        for old, new in (
            ("TWOHEYA[CASE=nom,NUM=sg,GEN=f,SEM=<",
             "TWOHEYA[CASE=nom,NUM=sg,GEN=n,SEM=<"),
            ("CULTIVATION[CASE=ins,SEM=<", "CULTIVATION[CASE=loc,SEM=<"),
            ("NINE[CNT=9,SEM=<", "NINE[CNT=8,SEM=<"),
            ("ALSO[SCOPE=additional_status] ->",
             "ALSO[SCOPE=exclusive_status] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.13_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))


    def test_2_14_initial_maturation_counts_and_scope(self):
        text = study(14)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [7, 7, 2, 2])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        cases = (
            ("desire_nonspontaneous", 2), ("desire_spontaneous_none", 6),
            ("desire_spontaneous_one", 7), ("desire_spontaneous_both", 8),
            ("form_initial", 6), ("formless_initial", 1),
        )
        sets = {
            case: {faculty for faculty, context in valuation["InitiallyMatures"]
                   if context == case}
            for case, _ in cases
        }
        for case, count in cases:
            with self.subTest(case=case):
                self.assertEqual(len(sets[case]), count)
                self.assertIn("life", sets[case])
                self.assertFalse({"mind", "neutral"} & sets[case])
        self.assertEqual(sets["desire_nonspontaneous"], {"body", "life"})
        self.assertEqual(sets["formless_initial"], {"life"})
        self.assertEqual(sets["form_initial"], sets["desire_spontaneous_none"])
        self.assertEqual(
            sets["desire_spontaneous_both"] - sets["desire_spontaneous_none"],
            {"female", "male"},
        )
        self.assertEqual(valuation["AtRelinking"], {("mind",), ("neutral",)})
        self.assertTrue(valuation["AtRelinking"] <= valuation["Afflicted"])
        self.assertFalse(valuation["MaturationAtRelinking"])
        verse = tree.label()["SEM"].simplify()
        valuation["InitialMaturationScope"] = False
        model = Model(valuation.domain, valuation)
        self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        for old, new in (
            ("THEM[CASE=ins,REF=spontaneous] ->",
             "THEM[CASE=ins,REF=nonspontaneous] ->"),
            ("TWO[CNT=2,SEM=<", "TWO[CNT=6,SEM=<"),
            ("HIGHERR[CASE=loc,SEM=<", "HIGHERR[CASE=nom,SEM=<"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.14_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))


    def test_2_15_terminal_sets_and_wholesome_addition(self):
        text = study(15)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [7, 2, 5])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        base = {
            case: {faculty for faculty, context in valuation["CeasesAt"] if context == case}
            for case in ("formless_terminal", "form_terminal", "gradual_terminal")
        }
        self.assertEqual([len(group) for group in base.values()], [3, 8, 4])
        self.assertEqual(base["gradual_terminal"], {"body", "life", "mind", "neutral"})
        sensory = {x[0] for x in valuation["SensoryFive"]}
        faith = {x[0] for x in valuation["FaithFive"]}
        self.assertEqual((len(sensory), len(faith)), (5, 5))
        self.assertFalse(sensory & faith)
        self.assertEqual(base["form_terminal"], base["formless_terminal"] | sensory)
        for case, expected in (("formless_terminal", 8), ("form_terminal", 13)):
            actual = {faculty for faculty, context in valuation["CeasesWholesomely"]
                      if context == case}
            self.assertEqual(actual, base[case] | faith)
            self.assertEqual(len(actual), expected)
        desire_sets = [
            base["form_terminal"], base["form_terminal"] | {"male"},
            base["form_terminal"] | {"male", "female"},
        ]
        self.assertEqual([len(group) for group in desire_sets], [8, 9, 10])
        self.assertEqual([len(group | faith) for group in desire_sets], [13, 14, 15])
        self.assertEqual(len(base["gradual_terminal"] | faith), 9)
        for old, new in (
            ("OPENING[WITNESS=uncertain,SUPPLIED=prose,SEM=<",
             "OPENING[WITNESS=settled,SUPPLIED=prose,SEM=<"),
            ("FORMR[CASE=loc,SEM=<", "FORMR[CASE=nom,SEM=<"),
            ("TEN[CNT=10,SEM=<", "TEN[CNT=8,SEM=<"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.15_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))


    def test_2_16_routes_and_person_level_union(self):
        text = study(16)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [3, 4, 2, 2])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        for name, count in (
            ("CommonSix", 6), ("StreamNine", 9), ("ArhatFixedEight", 8),
            ("SequentialMundaneSeven", 7), ("SequentialSupraEight", 8),
            ("SharpMundaneEight", 8), ("SharpSupraNine", 9),
        ):
            with self.subTest(group=name):
                self.assertEqual(len(valuation[name]), count)
        self.assertEqual(
            valuation["StreamNine"],
            valuation["CommonSix"] | {
                ("neutral",), ("shall_know_faculty",), ("knowledge_faculty",),
            },
        )
        self.assertNotEqual(valuation["SequentialSupraEight"], valuation["SharpMundaneEight"])
        self.assertEqual(
            valuation["SharpMundaneEight"],
            valuation["SequentialMundaneSeven"] | {("gladness",)},
        )
        self.assertEqual(
            valuation["SharpSupraNine"],
            valuation["SharpMundaneEight"] | {("knowledge_faculty",)},
        )
        fixed = {x[0] for x in valuation["ArhatFixedEight"]}
        events = {x[0] for x in valuation["ArhatAttainment"]}
        history = set()
        self.assertEqual({person for _, person in valuation["ByPerson"]}, {"person"})
        for event in events:
            feelings = {feeling for attainment, feeling in valuation["UsesFeeling"]
                        if attainment == event}
            self.assertEqual(len(feelings), 1)
            self.assertEqual(len(fixed | feelings), 9)
            history |= fixed | feelings
        self.assertEqual(len(history), 11)
        self.assertEqual(history - fixed, {"pleasure", "gladness", "neutral"})
        for old, new in (
            ("AND[SCOPE=addition] ->", "AND[SCOPE=replacement] ->"),
            ("EXTREMES[CASE=gen,NUM=du,CNT=2,SEM=<",
             "EXTREMES[CASE=gen,NUM=pl,CNT=3,SEM=<"),
            ("COUNTS[CASE=ins,COUNTS=seven_eight_nine,SEM=<",
             "COUNTS[CASE=nom,COUNTS=seven_eight_nine,SEM=<"),
            ("TWO[CASE=gen,NUM=du,CNT=2,REF=middle,SEM=<",
             "TWO[CASE=gen,NUM=du,CNT=2,REF=extreme,SEM=<"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.16_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))


    def test_2_17_reciprocal_possession_and_extra_faculties(self):
        text = study(17)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [6, 3])
        verse = tree.label()["SEM"].simplify()
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        model = Model(valuation.domain, valuation)
        self.assertTrue(model.satisfy(verse, Assignment(model.domain)))
        original = valuation["Possesses"]
        persons = {person for person, _ in original}
        triad = {"neutral", "life", "mind"}
        for person in persons:
            actual = {faculty for owner, faculty in original if owner == person}
            self.assertTrue(triad <= actual)
            for faculty in triad:
                with self.subTest(person=person, missing=faculty):
                    valuation["Possesses"] = original - {(person, faculty)}
                    model = Model(valuation.domain, valuation)
                    self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        valuation["Possesses"] = original
        self.assertTrue(any(faculty not in triad for _, faculty in original))
        self.assertIn(("formless_person", "mind"), original)
        self.assertNotIn(("formless_person", "eye"), original)
        self.assertIn(("formless_person", "neutral"), original)
        self.assertNotIn(("formless_person", "neutral"), valuation["OccurringNow"])
        for old, new in (
            ("ANYONE[CASE=nom,NUM=sg,GEN=m,READING=any_one,SEM=<",
             "ANYONE[CASE=nom,NUM=sg,GEN=m,READING=all_at_once,SEM=<"),
            ("ALLTHREE[CASE=nom,NUM=sg,GEN=m,CNT=3,SEM=<",
             "ALLTHREE[CASE=nom,NUM=sg,GEN=m,CNT=11,SEM=<"),
            ("ONE[CASE=gen,CNT=1,REF=person,SEM=<",
             "ONE[CASE=gen,CNT=1,REF=moment,SEM=<"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.17_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))


    def test_2_18_necessary_companion_sets(self):
        text = study(18)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [2, 4, 3, 1])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        requires = valuation["Requires"]
        closures = {
            given: {companion for source, companion in requires if source == given}
            for given, _ in requires
        }
        triad = {"neutral", "life", "mind"}
        for given in ("pleasure", "body"):
            self.assertEqual(closures[given], triad | {given})
        for given in ("eye", "ear", "nose", "tongue"):
            self.assertEqual(closures[given], triad | {"body", given})
        self.assertEqual(closures["gladness"], triad | {"pleasure", "gladness"})
        seven = {"body", "life", "mind", "pain", "pleasure", "gladness", "neutral"}
        self.assertEqual(closures["pain"], seven)
        for given in ("female", "male", "distress"):
            self.assertEqual(closures[given], seven | {given})
        faith = {x[0] for x in valuation["FaithFive"]}
        for given in faith:
            self.assertEqual(closures[given], faith | triad)
            self.assertEqual(len(closures[given]), 8)
        self.assertNotEqual(closures["eye"], closures["gladness"])
        self.assertNotEqual(closures["faith"], closures["distress"])
        self.assertNotIn("distress", closures["pain"])
        self.assertIn(("second_dhyana_person", "pleasure"), valuation["Possesses"])
        self.assertFalse(valuation["ThirdDhyanaAttained"])
        for old, new in (
            ("PAIR[CASE=ins,NUM=du,READING=distributive] ->",
             "PAIR[CASE=ins,NUM=du,READING=joint] ->"),
            ("FIVE[CASE=ins,CNT=5,SEM=<", "FIVE[CASE=ins,CNT=7,SEM=<"),
            ("TAIL[CONTINUED=next_verse,SEM=<",
             "TAIL[CONTINUED=current_seven,SEM=<"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.18_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))


    def test_2_19_realization_possession_sets(self):
        text = study(19)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [1, 3, 3])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        common = {x[0] for x in valuation["CommonTen"]}
        self.assertEqual(len(common), 10)
        sets = {
            given: {companion for source, companion in valuation["Requires"]
                    if source == given}
            for given in ("knowledge", "one_who_has_known", "shall_know")
        }
        for given in ("knowledge", "one_who_has_known"):
            self.assertEqual(sets[given], common | {given})
            self.assertEqual(len(sets[given]), 11)
        self.assertEqual(sets["knowledge"] & sets["one_who_has_known"], common)
        self.assertEqual(sets["shall_know"], common | {"body", "pain", "shall_know"})
        self.assertEqual(len(sets["shall_know"]), 13)
        self.assertNotIn("distress", sets["shall_know"])
        self.assertNotIn("body", sets["knowledge"])
        self.assertIn(("knowledge_person", "body"), valuation["Possesses"])
        self.assertIn(("prospective_person", "pain"), valuation["Possesses"])
        self.assertNotIn(("prospective_person", "pain"), valuation["OccurringNow"])
        for old, new in (
            ("TWOCASES[CASE=nom,NUM=sg,GEN=m,READING=alternative] ->",
             "TWOCASES[CASE=nom,NUM=sg,GEN=m,READING=joint] ->"),
            ("THIRTEEN[CASE=ins,CNT=13,SEM=<",
             "THIRTEEN[CASE=ins,CNT=11,SEM=<"),
            ("CARRY[CONTINUED=previous_subject,SEM=<",
             "CARRY[CONTINUED=current_subject,SEM=<"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.19_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))


    def test_2_20_distinct_minimum_eights(self):
        text = study(20)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [5, 4])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        sets = {
            case: {faculty for context, faculty in valuation["MinimumMember"]
                   if context == case}
            for case in ("rootless_minimum", "formless_minimum")
        }
        rootless, formless = sets.values()
        self.assertEqual((len(rootless), len(formless)), (8, 8))
        self.assertEqual(rootless & formless, {"neutral", "life", "mind"})
        self.assertEqual(rootless - formless, {"body", "pain", "pleasure", "gladness", "distress"})
        self.assertEqual(formless - rootless, {x[0] for x in valuation["FaithFive"]})
        self.assertFalse(formless & {x[0] for x in valuation["RealizationFaculty"]})
        self.assertEqual(valuation["LocalWholesome"], valuation["FaithFive"])
        actual = {faculty for _, faculty in valuation["Possesses"]}
        self.assertTrue(rootless < actual)
        self.assertEqual(actual - rootless, {"eye"})
        for old, new in (
            ("LIKEWISE[REF=minimum_eight,SEM=<",
             "LIKEWISE[REF=severed_roots,SEM=<"),
            ("EIGHT[CASE=ins,CNT=8,SEM=<", "EIGHT[CASE=ins,CNT=3,SEM=<"),
            ("SECONDSET[CASE=ins,RANGE=faith_five,SEM=<",
             "SECONDSET[CASE=ins,RANGE=all_wholesome,SEM=<"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.20_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))


    def test_2_21_maximum_inventories_and_alternative_exclusions(self):
        text = study(21)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [5, 3])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        faculties = {x[0] for x in valuation["Faculty"]}
        stainless = {x[0] for x in valuation["Stainless"]}
        self.assertEqual(faculties, {
            "eye", "ear", "nose", "tongue", "body", "female", "male",
            "life", "mind", "pain", "pleasure", "gladness", "distress",
            "neutral", "faith", "vigor", "mindfulness", "concentration",
            "comprehension", "shall_know", "knowledge", "one_who_has_known",
        })
        self.assertEqual(stainless, {"shall_know", "knowledge", "one_who_has_known"})
        worldly = {x[0] for x in valuation["WorldlyMember"]}
        self.assertEqual(worldly, faculties - stainless)
        self.assertEqual(len(worldly), 19)
        self.assertTrue({"female", "male"} <= worldly)
        for predicate, retained, excluded_sex in (
            ("ProspectiveMember", "shall_know", "female"),
            ("KnowledgeMember", "knowledge", "male"),
        ):
            with self.subTest(inventory=predicate):
                members = {x[0] for x in valuation[predicate]}
                self.assertEqual(
                    members, faculties - ((stainless - {retained}) | {excluded_sex}),
                )
                self.assertEqual(len(members), 19)
                self.assertEqual(members & stainless, {retained})
                self.assertEqual(len(members & {"female", "male"}), 1)
                self.assertEqual(len(members & worldly), 18)
                other_sex = ({"female", "male"} - {excluded_sex}).pop()
                swapped = (members - {other_sex}) | {excluded_sex}
                self.assertEqual(len(swapped), 19)
                self.assertEqual(swapped & stainless, {retained})
                # Excluding just one stainless Faculty would leave twenty.
                wrong = faculties - {excluded_sex, "one_who_has_known"}
                self.assertEqual(len(wrong), 20)
        verse = tree.label()["SEM"].simplify()
        self.assertTrue(Model(valuation.domain, valuation).satisfy(
            verse, Assignment(valuation.domain),
        ))
        valuation["StillAttached"] = set()
        self.assertFalse(Model(valuation.domain, valuation).satisfy(
            verse, Assignment(valuation.domain),
        ))
        for old, new in (
            ("NINETEEN[CASE=ins,CNT=19,SEM=<",
             "NINETEEN[CASE=ins,CNT=22,SEM=<"),
            ("FIRSTEXCLUSION[CASE=ins,STAINLESS=3,SEM=<",
             "FIRSTEXCLUSION[CASE=ins,STAINLESS=2,SEM=<"),
            ("NOBLE[CASE=nom,GEN=m,SUBJECT=second] ->",
             "NOBLE[CASE=nom,GEN=m,SUBJECT=first] ->"),
            ("SECONDEXCLUSION[CASE=ins,SEX=1,STAINLESS=2,SEM=<",
             "SECONDEXCLUSION[CASE=ins,SEX=1,STAINLESS=1,SEM=<"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.21_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))


    def test_2_22_coarising_counts_and_scope(self):
        text = study(22)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [5, 2, 2])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        members = {
            name: {x[0] for x in valuation[name]}
            for name in ("BaseMember", "BodyMember", "OtherMember", "SoundOtherMember")
        }
        base = members["BaseMember"]
        self.assertEqual(base, {
            "earth", "water", "fire", "wind", "visible", "odor", "taste",
            "dependent_tangible",
        })
        self.assertEqual(members["BodyMember"], base | {"body"})
        self.assertEqual(members["OtherMember"], base | {"body", "eye"})
        self.assertEqual(members["SoundOtherMember"], base | {"body", "eye", "sound"})
        self.assertEqual([len(group) for group in members.values()], [8, 9, 10, 11])
        for sense in ("eye", "ear", "nose", "tongue"):
            with self.subTest(sense=sense):
                clusters = (base, base | {"body"}, base | {"body", sense})
                self.assertEqual([len(c) for c in clusters], [8, 9, 10])
                self.assertEqual([len(c | {"sound"}) for c in clusters], [9, 10, 11])
                self.assertEqual([len(c - {"odor", "taste"}) for c in clusters], [6, 7, 8])
        self.assertEqual(valuation["Soundless"], valuation["DesireRule"])
        verse = tree.label()["SEM"].simplify()
        original = valuation["Soundless"]
        for case in ("soundless_base", "soundless_body", "soundless_eye"):
            valuation["Soundless"] = original - {(case,)}
            model = Model(valuation.domain, valuation)
            self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        for old, new in (
            ("NINE[CASE=nom,CNT=9,SEM=<", "NINE[CASE=nom,CNT=8,SEM=<"),
            ("TEN[CASE=nom,CNT=10,SEM=<", "TEN[CASE=nom,CNT=9,SEM=<"),
            ("OTHER[CASE=nom,RANGE=four_senses,MODE=addition] ->",
             "OTHER[CASE=nom,RANGE=all_faculties,MODE=addition] ->"),
            ("OTHER[CASE=nom,RANGE=four_senses,MODE=addition] ->",
             "OTHER[CASE=nom,RANGE=four_senses,MODE=replacement] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.22_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        witness = section(bhasya, 2)
        self.assertIn("bījatas teṣu", witness)
        self.assertIn("arthastu parīkṣyaḥ", witness)
        self.assertIn("Form, consciousness, mental factors", section(bhasya, 3))


    def test_2_23_accompaniment_scopes_and_classification(self):
        text = study(23)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [4, 2, 2, 3])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        consciousnesses = {x[0] for x in valuation["Consciousness"]}
        factors = {x[0] for x in valuation["Factor"]}
        accompanies = valuation["Accompanies"]
        self.assertEqual({c for _, c in accompanies}, consciousnesses)
        self.assertEqual({f for f, _ in accompanies}, factors)
        self.assertLess(len(accompanies), len(consciousnesses) * len(factors))
        arising = valuation["ArisingConditioned"]
        marks = valuation["MarksAccompany"]
        acquisition = valuation["AcquisitionAccompanies"]
        self.assertEqual(arising, marks)
        self.assertEqual(acquisition, valuation["SentientDesignated"])
        self.assertTrue(acquisition < marks)
        self.assertFalse(arising & valuation["Unconditioned"])
        self.assertEqual(len(valuation["ClassName"]), 5)
        self.assertEqual(len(factors), 2)
        verse = tree.label()["SEM"].simplify()
        for predicate, item in (
            ("Accompanies", ("factor_a", "consciousness_a")),
            ("MarksAccompany", ("external_form",)),
            ("AcquisitionAccompanies", ("sentient_form",)),
        ):
            with self.subTest(missing=predicate):
                original = valuation[predicate]
                valuation[predicate] = original - {item}
                model = Model(valuation.domain, valuation)
                self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
                valuation[predicate] = original
        for old, new in (
            ("OR[READING=scope_distinction] ->", "OR[READING=optional] ->"),
            ("ALL[CASE=nom,NUM=sg,SCOPE=arising_conditioned] ->",
             "ALL[CASE=nom,NUM=sg,SCOPE=consciousness_only] ->"),
            ("FIVE[CNT=5] ->", "FIVE[CNT=10] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.23_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))


    def test_2_24_all_ten_in_each_moment(self):
        text = study(24)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [11, 1])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        kinds = {x[0] for x in valuation["GreatGroundKind"]}
        self.assertEqual(kinds, {
            f"{name}_kind" for name in (
                "feeling", "volition", "reflection", "wish", "contact",
                "comprehension", "mindfulness", "attention", "resolution",
                "concentration",
            )
        })
        moments = {x[0] for x in valuation["ConsciousnessMoment"]}
        original = valuation["Present"]
        self.assertEqual(original, {(c, f) for c in moments for f in kinds})
        verse = tree.label()["SEM"].simplify()
        for pair in original:
            with self.subTest(missing=pair):
                valuation["Present"] = original - {pair}
                model = Model(valuation.domain, valuation)
                self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        valuation["Present"] = original | {("moment_a", "additional_factor")}
        model = Model(valuation.domain, valuation)
        self.assertTrue(model.satisfy(verse, Assignment(model.domain)))
        for moment in moments:
            self.assertEqual(len({
                mode for c, mode in valuation["FeelingMode"] if c == moment
            }), 1)
        for old, new in (
            ("AND[READING=conjunction] ->", "AND[READING=alternative] ->"),
            ("EVERY[CASE=loc,SCOPE=every_moment] ->",
             "EVERY[CASE=loc,SCOPE=somewhere_in_stream] ->"),
            ("TEN[CNT=10,SEM=<", "TEN[CNT=9,SEM=<"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.24_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        self.assertIn("viṣayanimittodrūha", section(bhasya, 2))
        self.assertIn("it is said", section(bhasya, 3))
        self.assertIn("Faculty, Condition, and Cognition", section(bhasya, 3))


    def test_2_25_wholesome_ten_and_root_pair(self):
        text = study(25)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [11, 1, 1])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        wholesome = {x[0] for x in valuation["WholesomeKind"]}
        universal = {x[0] for x in valuation["UniversalKind"]}
        self.assertEqual(wholesome, {
            f"{name}_kind" for name in (
                "faith", "heedfulness", "pliancy", "equanimity", "shame",
                "caution", "nongreed", "nonhatred", "nonharming", "vigor",
            )
        })
        self.assertEqual(len(universal), 10)
        self.assertFalse(wholesome & universal)
        original = valuation["Present"]
        actual = {f for c, f in original if c == "wholesome_moment"}
        self.assertEqual(actual, wholesome | universal)
        self.assertEqual(len(actual), 20)
        self.assertEqual(valuation["nondelusion"], valuation["comprehension"])
        self.assertNotIn(valuation["nondelusion"], wholesome)
        self.assertNotEqual(valuation["equanimity"], valuation["neutral_feeling"])
        verse = tree.label()["SEM"].simplify()
        for kind in wholesome:
            with self.subTest(missing=kind):
                valuation["Present"] = original - {("wholesome_moment", kind)}
                model = Model(valuation.domain, valuation)
                self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        valuation["Present"] = original | {("wholesome_moment", "additional_factor")}
        model = Model(valuation.domain, valuation)
        self.assertTrue(model.satisfy(verse, Assignment(model.domain)))
        for old, new in (
            ("ROOTPAIR[CNT=2,SEM=<", "ROOTPAIR[CNT=3,SEM=<"),
            ("HEEDFUL[PRIVATIVE=true,SEM=<", "HEEDFUL[PRIVATIVE=false,SEM=<"),
            ("WHOLESOME[CASE=loc,SCOPE=wholesome_consciousness] ->",
             "WHOLESOME[CASE=loc,SCOPE=all_consciousness] ->"),
            ("ALWAYS[SCOPE=every_moment] ->", "ALWAYS[SCOPE=sometimes] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.25_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        self.assertIn("one Cognitive Condition", section(bhasya, 3))
        self.assertIn("Not a demonstrated solution", section(bhasya, 7))


    def test_2_26_six_ten_and_unwholesome_pair(self):
        text = study(26)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [9, 4])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        six = {x[0] for x in valuation["AfflictionKind"]}
        separate = {x[0] for x in valuation["SeparateFive"]}
        modes = {x[0] for x in valuation["AfflictedMode"]}
        ten = {x[0] for x in valuation["RecitedTen"]}
        pair = {x[0] for x in valuation["UnwholesomeKind"]}
        self.assertEqual(six, {
            f"{name}_kind" for name in (
                "delusion", "heedlessness", "laziness", "faithlessness",
                "sluggishness", "agitation",
            )
        })
        self.assertEqual(pair, {"shamelessness_kind", "lack_caution_kind"})
        self.assertEqual((len(separate), len(modes), len(ten)), (5, 5, 10))
        self.assertFalse(separate & modes)
        self.assertEqual(ten, separate | modes)
        self.assertEqual(six - ten, {"sluggishness_kind"})
        self.assertEqual(ten - six, modes)
        self.assertEqual(valuation["ModeOf"], {
            ("lost_mindfulness", "mindfulness_kind"),
            ("distraction", "concentration_kind"),
            ("unclear_comprehension", "comprehension_kind"),
            ("improper_attention", "attention_kind"),
            ("false_resolution", "resolution_kind"),
        })
        self.assertTrue(valuation["UnwholesomeMoment"] < valuation["AfflictedMoment"])
        original = valuation["Present"]
        verse = tree.label()["SEM"].simplify()
        required = {
            (c[0], f) for c in valuation["AfflictedMoment"] for f in six
        } | {("unwholesome_moment", f) for f in pair}
        self.assertTrue(required < original)
        for occurrence in required:
            with self.subTest(missing=occurrence):
                valuation["Present"] = original - {occurrence}
                model = Model(valuation.domain, valuation)
                self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        valuation["Present"] = original | {("unwholesome_moment", "additional_factor")}
        model = Model(valuation.domain, valuation)
        self.assertTrue(model.satisfy(verse, Assignment(model.domain)))
        for old, new in (
            ("SIX[CNT=6,SEM=<", "SIX[CNT=10,SEM=<"),
            ("ALWAYS[SCOPE=every] ->", "ALWAYS[SCOPE=sometimes] ->"),
            ("BUT[READING=scope_contrast] ->", "BUT[READING=replacement] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.26_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        self.assertIn("Some hold distraction", section(bhasya, 3))
        self.assertIn("revised lists are not supplied", section(bhasya, 7))


    def test_2_27_membership_not_bundle_and_restricted_association(self):
        text = study(27)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [3, 1])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        kinds = {x[0] for x in valuation["LimitedKind"]}
        self.assertEqual(kinds, {
            f"{name}_kind" for name in (
                "anger", "resentment", "crookedness", "envy", "spite",
                "concealment", "stinginess", "deception", "intoxication",
                "harmfulness",
            )
        })
        verse = tree.label()["SEM"].simplify()
        original = valuation["LimitedKind"]
        for kind in kinds:
            with self.subTest(missing=kind):
                valuation["LimitedKind"] = original - {(kind,)}
                model = Model(valuation.domain, valuation)
                self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        valuation["LimitedKind"] = original
        self.assertEqual(
            {f for f, _ in valuation["AssociatedAffliction"]}, kinds,
        )
        for _, associated in valuation["AssociatedAffliction"]:
            for predicate in ("Ignorance", "CultivationAbandonable", "MentalSphere"):
                self.assertIn((associated,), valuation[predicate])
        self.assertTrue(any(
            (companion,) not in valuation["Ignorance"]
            for _, companion in valuation["OtherCompanion"]
        ))
        self.assertEqual(len(valuation["UnfixedExample"]), 4)
        self.assertLess(len(valuation["Present"]), len(kinds))
        # Membership alone imposes no episode-composition constraint.
        valuation["Present"] = {
            ("illustrative_bundle", kind) for kind in kinds
        }
        model = Model(valuation.domain, valuation)
        self.assertTrue(model.satisfy(verse, Assignment(model.domain)))
        for old, new in (
            ("SEVEN[CASE=nom,NUM=pl,CNT=7,SEM=<",
             "SEVEN[CASE=nom,NUM=pl,CNT=6,SEM=<"),
            ("THREE[CASE=nom,NUM=pl,CNT=3,SEM=<",
             "THREE[CASE=nom,NUM=pl,CNT=4,SEM=<"),
            ("AND[READING=enumeration] ->", "AND[READING=cooccurrence] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.27_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        self.assertNotIn("Only with ignorance is read", section(bhasya, 3))
        self.assertIn("abandonable through cultivation", section(bhasya, 3))


    def test_2_28_twenty_two_and_conditional_regret(self):
        text = study(28)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [5, 3])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        universal = {x[0] for x in valuation["UniversalKind"]}
        wholesome = {x[0] for x in valuation["WholesomeKind"]}
        examination = {x[0] for x in valuation["ExaminationKind"]}
        base = {x[0] for x in valuation["BaseMember"]}
        self.assertEqual((len(universal), len(wholesome)), (10, 10))
        self.assertEqual(examination, {"initial_examination", "sustained_examination"})
        self.assertFalse(universal & wholesome)
        self.assertFalse((universal | wholesome) & examination)
        self.assertEqual(base, universal | wholesome | examination)
        self.assertEqual(len(base), 22)
        actual = {
            moment: {f for c, f in valuation["Present"] if c == moment}
            for moment in ("base_moment", "regret_moment")
        }
        self.assertEqual(actual["base_moment"], base)
        self.assertEqual(actual["regret_moment"], base | {"regret_kind"})
        self.assertEqual(len(actual["regret_moment"]), 23)
        self.assertNotIn("consciousness", base)
        self.assertIn(("unwholesome_regret_moment",), valuation["RegretPresent"])
        self.assertNotIn(("unwholesome_regret_moment",), valuation["WholesomeDesireMoment"])
        verse = tree.label()["SEM"].simplify()
        for predicate, pair in (
            ("BaseCount", ("base_moment", "count_twenty_two")),
            ("InitialExamination", ("base_moment",)),
            ("SustainedExamination", ("regret_moment",)),
            ("LocalCount", ("regret_moment", "count_twenty_three")),
        ):
            with self.subTest(missing=predicate):
                original = valuation[predicate]
                valuation[predicate] = original - {pair}
                model = Model(valuation.domain, valuation)
                self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
                valuation[predicate] = original
        valuation["Present"] |= {("regret_moment", "later_addition")}
        model = Model(valuation.domain, valuation)
        self.assertTrue(model.satisfy(verse, Assignment(model.domain)))
        for old, new in (
            ("REASON[CASE=abl,PAIR=included] ->",
             "REASON[CASE=abl,PAIR=outside_count] ->"),
            ("TWENTYTWO[CNT=22,SEM=<", "TWENTYTWO[CNT=24,SEM=<"),
            ("EXTRA[MODE=addition] ->", "EXTRA[MODE=replacement] ->"),
            ("SOMETIMES[SCOPE=some_cases] ->",
             "SOMETIMES[SCOPE=every_case] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.28_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        self.assertIn("| Wholesome | the unwholesome | the wholesome |", section(bhasya, 8))
        self.assertIn("| Unwholesome | the wholesome | the unwholesome |", section(bhasya, 8))
        self.assertIn("Alternatively", section(bhasya, 3))
        self.assertIn("six Contact Essences", section(bhasya, 3))


    def test_2_29_twenty_and_single_additions(self):
        text = study(29)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [6, 5])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        groups = [
            {x[0] for x in valuation[name]}
            for name in ("UniversalKind", "AfflictionKind", "UnwholesomeKind",
                         "ExaminationKind")
        ]
        self.assertEqual([len(group) for group in groups], [10, 6, 2, 2])
        base = {x[0] for x in valuation["BaseMember"]}
        self.assertEqual(base, set.union(*groups))
        self.assertEqual(len(base), 20)
        self.assertEqual(valuation["ViewMember"], valuation["BaseMember"])
        self.assertIn(("comprehension_kind",), valuation["ViewMember"])
        self.assertIn(("delusion_kind",), valuation["BaseMember"])
        self.assertEqual(valuation["ViewRealizedAs"], {
            ("view_unwholesome_desire", "comprehension_kind"),
        })
        four = {x[0] for x in valuation["FourAffliction"]}
        self.assertEqual(four, {
            "attachment_kind", "hostility_kind", "conceit_kind", "doubt_kind",
        })
        additions = four | {x[0] for x in valuation["SecondaryExample"]} | {"regret_kind"}
        self.assertEqual(len(additions), 6)
        for addition in additions:
            with self.subTest(addition=addition):
                self.assertNotIn(addition, base)
                self.assertEqual(len(base | {addition}), 21)
        self.assertEqual(len(base | four), 24)
        self.assertEqual(
            {x[0] for x in valuation["AttachmentMember"]}, base | {"attachment_kind"},
        )
        self.assertEqual(
            {x[0] for x in valuation["RegretMember"]}, base | {"regret_kind"},
        )
        verse = tree.label()["SEM"].simplify()
        original = valuation["LocalCount"]
        for pair in original:
            with self.subTest(missing=pair):
                valuation["LocalCount"] = original - {pair}
                model = Model(valuation.domain, valuation)
                self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        for old, new in (
            ("TWENTY[CNT=20,SEM=<", "TWENTY[CNT=21,SEM=<"),
            ("FOUR[CNT=4,READING=alternatives] ->",
             "FOUR[CNT=4,READING=joint] ->"),
            ("SECONDARY[CASE=ins,READING=one] ->",
             "SECONDARY[CASE=ins,READING=all] ->"),
            ("TWENTYONE[CNT=21,SEM=<", "TWENTYONE[CNT=24,SEM=<"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.29_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        self.assertIn("But should there not be twenty-one", section(bhasya, 3))
        self.assertIn("special form of discriminative comprehension", section(bhasya, 3))


    def test_2_30_indeterminate_counts_and_torpor(self):
        text = study(30)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [6, 7])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        groups = {
            name: {x[0] for x in valuation[name]}
            for name in (
                "UniversalKind", "AfflictionKind", "ExaminationKind",
                "UnwholesomeKind", "ObscuredMember", "UnobscuredMember",
                "RegionalRegretMember", "TorporUnobscuredMember",
            )
        }
        self.assertEqual(
            [len(groups[name]) for name in
             ("UniversalKind", "AfflictionKind", "ExaminationKind")], [10, 6, 2],
        )
        obscured = groups["ObscuredMember"]
        unobscured = groups["UnobscuredMember"]
        self.assertEqual(obscured, groups["UniversalKind"] | groups["AfflictionKind"]
                         | groups["ExaminationKind"])
        self.assertEqual(unobscured, groups["UniversalKind"] | groups["ExaminationKind"])
        self.assertEqual((len(obscured), len(unobscured)), (18, 12))
        self.assertFalse(obscured & groups["UnwholesomeKind"])
        regret = groups["RegionalRegretMember"]
        torpor = groups["TorporUnobscuredMember"]
        self.assertEqual(regret, unobscured | {"regret_kind"})
        self.assertEqual(torpor, unobscured | {"torpor_kind"})
        self.assertEqual((len(regret), len(torpor)), (13, 13))
        self.assertEqual(regret & torpor, unobscured)
        prior = load_valuation(dict(BLOCK.findall(section(study(28), 8)))["nltk-valuation"])
        wholesome = {x[0] for x in prior["BaseMember"]}
        for before, after in (
            (obscured, 19), (unobscured, 13), (wholesome, 23),
            (wholesome | {"regret_kind"}, 24),
        ):
            self.assertEqual(len(before | {"torpor_kind"}), after)
        self.assertTrue(valuation["TorporPresent"] < valuation["StatedCase"])
        verse = tree.label()["SEM"].simplify()
        original = valuation["AddsOne"]
        for increment in original:
            with self.subTest(missing=increment):
                valuation["AddsOne"] = original - {increment}
                model = Model(valuation.domain, valuation)
                self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        for old, new in (
            ("OTHER[REF=unobscured] ->", "OTHER[REF=any_other] ->"),
            ("EIGHTEEN[CNT=18,SEM=<", "EIGHTEEN[CNT=20,SEM=<"),
            ("TWELVE[CNT=12,SEM=<", "TWELVE[CNT=13,SEM=<"),
            ("REASON[CASE=abl,READING=compatibility] ->",
             "REASON[CASE=abl,READING=presence] ->"),
            ("THAT[REF=torpor] ->", "THAT[REF=regret] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.30_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        self.assertIn("Teachers of the outer regions", section(bhasya, 3))
        self.assertIn("On their account", section(bhasya, 3))
        self.assertIn("Not examples supplied by the prose", section(bhasya, 7))


    def test_2_31_cumulative_exclusions_not_level_identity(self):
        text = study(31)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [6, 3, 5])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        exclusions = valuation["Excludes"]
        by_level = {
            level: {f for source, f in exclusions if source == level}
            for level in ("first_level", "intermediate_level", "higher_levels")
        }
        first = by_level["first_level"]
        middle = by_level["intermediate_level"]
        higher = by_level["higher_levels"]
        self.assertEqual(first, {"regret_kind", "torpor_kind", "unwholesome_category"})
        self.assertEqual(middle, first | {"initial_examination"})
        self.assertEqual(higher, middle | {
            "sustained_examination", "deception_kind", "crookedness_kind",
        })
        self.assertEqual(len({
            valuation["first"], valuation["intermediate"], valuation["beyond"],
        }), 3)
        exceptions = {x[0] for x in valuation["FirstException"]}
        anger_group = {x[0] for x in valuation["AngerGroup"]}
        self.assertEqual(exceptions, {
            "crookedness_kind", "intoxication_kind", "deception_kind",
        })
        self.assertEqual(
            {x[0] for x in valuation["FirstAngerGroupExclusion"]},
            anger_group - exceptions,
        )
        self.assertEqual(len(anger_group), 10)
        self.assertNotIn("intoxication_kind", higher)
        for source, previous in valuation["CarriesExclusions"]:
            self.assertTrue(by_level[previous] <= by_level[source])
        verse = tree.label()["SEM"].simplify()
        for missing in (
            ("first_level", "regret_kind"),
            ("intermediate_level", "initial_examination"),
            ("higher_levels", "sustained_examination"),
        ):
            valuation["Excludes"] = exclusions - {missing}
            model = Model(valuation.domain, valuation)
            self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        for old, new in (
            ("FROM[REF=desire_distribution] ->",
             "FROM[REF=causal_reason] ->"),
            ("FROM[REF=intermediate] ->", "FROM[REF=first] ->"),
            ("ALSO[READING=further_exclusion] ->",
             "ALSO[READING=all_three_exceptions] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.31_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        self.assertIn("he did not know and made an evasion", section(bhasya, 3))
        self.assertNotIn("Not a collation", section(bhasya, 3))
        self.assertIn("does not complete the encounter", section(bhasya, 7))


    def test_2_32_scoped_pair_and_fourfold_comparisons(self):
        text = study(32)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [2, 3, 4, 3])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        for universe, left, right in (
            ("ComparisonExample", "FaithExample", "AffectionExample"),
            ("PersonExample", "PersonAffectionExample", "PersonRespectExample"),
        ):
            with self.subTest(comparison=universe):
                domain = valuation[universe]
                a, b = valuation[left], valuation[right]
                quadrants = (a - b, b - a, a & b, domain - (a | b))
                self.assertEqual([len(q) for q in quadrants], [1, 1, 1, 1])
                self.assertEqual(set.union(*quadrants), domain)
        formless = valuation["FormlessWholesome"]
        self.assertTrue(formless <= valuation["FaithPresent"])
        self.assertTrue(formless <= valuation["ShamePresent"])
        self.assertFalse(formless & valuation["PersonAffection"])
        self.assertFalse(formless & valuation["PersonRespect"])
        verse = tree.label()["SEM"].simplify()
        for predicate in ("DefinedAs", "ScopedAs", "RealmRange"):
            original = valuation[predicate]
            for pair in original:
                with self.subTest(missing=pair):
                    valuation[predicate] = original - {pair}
                    model = Model(valuation.domain, valuation)
                    self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
            valuation[predicate] = original
        for old, new in (
            ("THOSE[NUM=du,REF=affection_respect] ->",
             "THOSE[NUM=du,REF=faith_shame_unrestricted] ->"),
            ("REALMS[CASE=loc,NUM=du] ->", "REALMS[CASE=loc,NUM=pl] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.32_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        for witness in ("avadyeṣvabhayadarśiatā", "tasmānna saiva premetyapare",
                        "pudgalālambane śraddhāhriyau"):
            self.assertIn(witness, section(bhasya, 2))
        self.assertIn("not being governed by fear", section(bhasya, 3))
        self.assertIn("provisional construal", section(bhasya, 3))


    def test_2_33_attributed_positions_and_definition_loci(self):
        text = study(33)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [2, 2, 6])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        self.assertEqual(valuation["DefinedAs"], {
            ("initial_examination", "coarseness_definition"),
            ("sustained_examination", "subtlety_definition"),
            ("conceit_factor", "elevation_definition"),
            ("intoxication_factor", "takeover_definition"),
        })
        allows = valuation["AllowsCoPresence"]
        denies = valuation["DeniesCoPresence"]
        self.assertEqual(len(allows), 2)
        self.assertEqual(len(denies), 1)
        self.assertFalse(allows & denies)
        self.assertEqual(allows | denies, valuation["Position"])
        self.assertEqual(valuation["LevelFive"], denies)
        self.assertFalse(valuation["MomentFive"])
        self.assertEqual(valuation["AttachmentTo"], {
            ("intoxication_factor", "own_qualities_condition"),
        })
        self.assertIn(("intoxication_factor", "consciousness_locus"), valuation["Locus"])
        self.assertNotIn(("intoxication_factor", "own_qualities_condition"), valuation["Locus"])
        self.assertEqual(valuation["ComparisonWith"], {
            ("conceit_factor", "comparison_other"),
        })
        verse = tree.label()["SEM"].simplify()
        for predicate in ("DefinedAs", "AttachmentTo", "Locus"):
            original = valuation[predicate]
            required = {pair for pair in original
                        if predicate != "Locus" or pair[0] == "intoxication_factor"}
            for pair in required:
                with self.subTest(missing=pair):
                    valuation[predicate] = original - {pair}
                    model = Model(valuation.domain, valuation)
                    self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
            valuation[predicate] = original
        for old, new in (
            ("STATEPAIR[NUM=du,ORDER=respective] ->",
             "STATEPAIR[NUM=du,ORDER=reversed] ->"),
            ("CONSCIOUSNESS[CASE=gen] ->", "CONSCIOUSNESS[CASE=loc] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.33_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        for witness in ("vāksaṃskārā", "na kṣaṇataḥ", "saṃprahaṛśaṇaviśeṣo"):
            self.assertIn(witness, section(bhasya, 2))
        self.assertIn("initial\nand sustained examination", section(bhasya, 3))
        self.assertIn("With reference to the level, not to the moment", section(bhasya, 3))
        self.assertNotIn("Not a restored reading", section(bhasya, 3))
        self.assertIn("vak:takesOver vak:Consciousness", section(text, 10))


    def test_2_34_five_equalities_and_distinct_instances(self):
        text = study(34)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [5, 5])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        self.assertEqual({x[0] for x in valuation["EqualityMode"]}, {
            "basis_mode", "condition_mode", "manner_mode", "time_mode", "instance_mode",
        })
        associated = valuation["Associated"]
        self.assertEqual(len(associated), 2)
        self.assertTrue(all(c != f for c, f in associated))
        instances = valuation["InstanceOf"]
        self.assertEqual(len({token for token, _ in instances}), 3)
        for kind in {kind for _, kind in instances}:
            self.assertEqual(len({token for token, k in instances if k == kind}), 1)
        self.assertEqual(
            {valuation["citta_name"], valuation["manas_name"], valuation["vijnana_name"]},
            {"consciousness_designation", "mind_designation", "cognition_designation"},
        )
        formula = next(
            line for line in section(text, 8).splitlines()
            if line.startswith("all c f.(Associated")
        )
        model = Model(valuation.domain, valuation)
        self.assertTrue(model.evaluate(formula, Assignment(model.domain)))
        for predicate in ("Basis", "Condition", "Manner", "Time", "OneInstanceEach"):
            original = valuation[predicate]
            for relation in original:
                with self.subTest(missing=relation, predicate=predicate):
                    valuation[predicate] = original - {relation}
                    model = Model(valuation.domain, valuation)
                    self.assertFalse(model.evaluate(formula, Assignment(model.domain)))
            valuation[predicate] = original
        verse = tree.label()["SEM"].simplify()
        for predicate in ("HasBasis", "HasCondition", "HasManner", "AssociationModes",
                          "SameReference"):
            original = valuation[predicate]
            for relation in original:
                with self.subTest(verse_missing=relation):
                    valuation[predicate] = original - {relation}
                    model = Model(valuation.domain, valuation)
                    self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
            valuation[predicate] = original
        for old, new in (
            ("ONE[READING=contextual_reference] ->",
             "ONE[READING=unrestricted_interchange] ->"),
            ("HAVING[CASE=nom,NUM=pl,CNT=3] ->",
             "HAVING[CASE=nom,NUM=pl,CNT=2] ->"),
            ("FIVE[CNT=5] ->", "FIVE[CNT=4] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.34_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        self.assertIn("wholesome and unwholesome Principles", section(bhasya, 3))
        self.assertIn("one of each mental factor", section(bhasya, 3))
        self.assertNotIn("apprehend an object", section(bhasya, 3))
        self.assertNotIn("contextual reading", section(bhasya, 3))


    def test_2_35_entries_pairs_and_cross_verse_continuation(self):
        text = study(35)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [3, 7])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        entries = valuation["DissociatedEntry"]
        verse_entries = {
            (valuation[name],) for name in (
                "acquisition", "nonacquisition", "commonality", "asamjnika",
                "attainment_one", "attainment_two", "life", "marks",
            )
        }
        self.assertEqual(len(verse_entries), 8)
        self.assertEqual(entries - verse_entries, {("name_groups_heading",)})
        self.assertEqual(entries, valuation["FormationEntry"])
        self.assertEqual(entries, valuation["ConditionedEntry"])
        self.assertFalse(valuation["AssociatedWithConsciousness"])
        self.assertFalse(valuation["FormNature"])
        self.assertEqual(entries - valuation["SingleEntry"], {
            ("marks_heading",), ("name_groups_heading",),
        })
        self.assertNotEqual(valuation["asamjnika"], valuation["attainment_one"])
        self.assertNotEqual(valuation["asamjnika"], valuation["attainment_two"])
        self.assertNotEqual(valuation["attainment_one"], valuation["attainment_two"])
        verse = tree.label()["SEM"].simplify()
        for entry in verse_entries:
            with self.subTest(missing=entry):
                valuation["DissociatedEntry"] = entries - {entry}
                model = Model(valuation.domain, valuation)
                self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        valuation["DissociatedEntry"] = verse_entries
        model = Model(valuation.domain, valuation)
        self.assertTrue(model.satisfy(verse, Assignment(model.domain)))
        valuation["DissociatedEntry"] = entries | {("additional_entry",)}
        model = Model(valuation.domain, valuation)
        self.assertTrue(model.satisfy(verse, Assignment(model.domain)))
        for old, new in (
            ("ACQUISITIONPAIR[CASE=nom,NUM=du,CNT=2] ->",
             "ACQUISITIONPAIR[CASE=nom,NUM=sg,CNT=1] ->"),
            ("ATTAINMENTS[CASE=nom,NUM=du,CNT=2] ->",
             "ATTAINMENTS[CASE=nom,NUM=sg,CNT=1] ->"),
            ("MARKS[CASE=nom,NUM=pl] ->", "MARKS[CASE=nom,NUM=sg] ->"),
            ("AND[CONTINUATION=next_verse] ->",
             "AND[CONTINUATION=closed_list] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.35_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        self.assertIn("na cittena asaṃprayuktā", section(bhasya, 2))
        self.assertIn("nāmakāyādayaś ceti", section(bhasya, 2))
        self.assertIn("contextual reading of the defective double negative", section(bhasya, 3))
        self.assertIn("nature of Form", section(bhasya, 3))


    def test_2_36_senses_scope_and_applicability_not_actual_possession(self):
        text = study(36)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [3, 3, 3])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        self.assertEqual(valuation["Sense"], {
            ("acquisition_term", "obtaining_sense"),
            ("acquisition_term", "possession_sense"),
        })
        self.assertEqual(valuation["PairRange"], {
            ("acquisition_nonacquisition_pair", "own_conditioned_range"),
            ("acquisition_nonacquisition_pair", "two_cessation_range"),
        })
        self.assertEqual(valuation["Cessation"], {
            ("discriminative_cessation",), ("nondiscriminative_cessation",),
        })
        eligible = valuation["OwnConditioned"] | valuation["Cessation"]
        self.assertEqual(valuation["AcquisitionApplicable"], eligible)
        self.assertEqual(valuation["NonAcquisitionApplicable"], eligible)
        self.assertTrue(valuation["NonPossessed"] <= eligible)
        self.assertTrue(valuation["NonPossessed"].isdisjoint(valuation["Possessed"]))
        self.assertIn(("unpossessed_own_dharma",), eligible)
        self.assertEqual(valuation["OutsideRange"], {
            ("space",), ("another_person_dharma",), ("nonsentient_item",),
        })
        self.assertTrue(valuation["OutsideRange"].isdisjoint(eligible))
        self.assertIn(("space",), valuation["Unconditioned"])
        verse = tree.label()["SEM"].simplify()
        for predicate in ("ContinuesPriorList", "Sense", "PairRange"):
            original = valuation[predicate]
            for relation in original:
                with self.subTest(missing=relation):
                    valuation[predicate] = original - {relation}
                    model = Model(valuation.domain, valuation)
                    self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
            valuation[predicate] = original
        for old, new in (
            ("CLOSE[REF=prior_list] ->", "CLOSE[REF=definition] ->"),
            ("PAIR[CASE=nom,NUM=du] ->", "PAIR[CASE=nom,NUM=sg] ->"),
            ("OWN[CASE=gen,NUM=pl,REF=own_continuum] ->",
             "OWN[CASE=gen,NUM=pl,REF=other_continuum] ->"),
            ("CESSATIONS[CASE=gen,NUM=du,CNT=2] ->",
             "CESSATIONS[CASE=gen,NUM=pl,CNT=3] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.36_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        witness = section(bhasya, 2)
        for argument in (
            "saptabhī ratnaiḥ", "jātijātirvā", "tadvigamāvigamāt",
            "kiṃ punaridaṃ bījaṃ nāma", "tāvat bhavyastāni bhāvayitum",
            "dravyameva tu vaibhāṣikāḥ", "eṣa hi naḥ siddhānta",
        ):
            with self.subTest(argument=argument):
                self.assertIn(argument, witness)
        rendering = section(bhasya, 3)
        self.assertIn("uncontaminated dharmas", rendering)
        self.assertIn("arising-of-arising", rendering)
        self.assertIn("departure or non-departure", rendering)
        self.assertIn("contextual negative reading", rendering)
        self.assertIn("The Vaibhāṣikas, however, declare both real", rendering)


    def test_2_37_temporal_product_correspondence_and_combined_four(self):
        text = study(37)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [2, 2, 2, 2])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        times = {"past", "future", "present"}
        self.assertEqual(valuation["Time"], {(time,) for time in times})
        self.assertEqual(valuation["TemporalOption"], {
            (dharma_time, acquisition_time)
            for dharma_time in times for acquisition_time in times
        })
        for predicate, classes in (
            ("EthicalMatch", {"wholesome", "unwholesome", "indeterminate"}),
            ("RealmMatch", {"desire_realm", "form_realm", "formless_realm"}),
        ):
            self.assertEqual(valuation[predicate], {(value, value) for value in classes})
        allowed = valuation["AllowedAcquisition"]
        expected = {
            "nondiscriminative_cessation": {
                "desire_realm", "form_realm", "formless_realm",
            },
            "discriminative_cessation": {
                "form_realm", "formless_realm", "uncontaminated_class",
            },
            "path_truth": {"uncontaminated_class"},
        }
        self.assertEqual(allowed, {
            (kind, option) for kind, options in expected.items() for option in options
        })
        union = set().union(*expected.values())
        self.assertEqual(len(union), 4)
        self.assertEqual(valuation["AggregateOption"], {(value,) for value in union})
        self.assertEqual(valuation["AcquisitionClass"], valuation["AggregateOption"])
        self.assertEqual(valuation["UnincludedKind"], {(kind,) for kind in expected})
        self.assertNotIn(("uncontaminated_class",), valuation["Realm"])
        self.assertNotIn(("path_truth",), valuation["Unconditioned"])
        self.assertNotIn(("space",), valuation["UnincludedKind"])
        self.assertIn(("space",), valuation["Unconditioned"])
        verse = tree.label()["SEM"].simplify()
        for predicate in ("TemporalOption", "EthicalMatch", "RealmMatch", "AggregateOption"):
            original = valuation[predicate]
            for relation in original:
                with self.subTest(missing=relation):
                    valuation[predicate] = original - {relation}
                    model = Model(valuation.domain, valuation)
                    self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
            valuation[predicate] = original
        for old, new in (
            ("THREE[CNT=3] ->", "THREE[CNT=2] ->"),
            ("CORRESPONDING[MATCH=respectively] ->",
             "CORRESPONDING[MATCH=unrestricted] ->"),
            ("SAME[MATCH=same_realm] ->", "SAME[MATCH=any_realm] ->"),
            ("UNINCLUDED[CASE=gen,NUM=pl,REF=uncontaminated] ->",
             "UNINCLUDED[CASE=gen,NUM=pl,REF=unacquired] ->"),
            ("FOUR[CNT=4] ->", "FOUR[CNT=3] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.37_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        self.assertIn("sā kilaiṣā prāptiḥ", section(bhasya, 2))
        rendering = section(bhasya, 3)
        self.assertIn("it is said", rendering)
        self.assertIn("respectively wholesome, unwholesome, and indeterminate", rendering)
        self.assertIn("uncontaminated only", rendering)
        self.assertIn("Taken together, this is fourfold", rendering)
        self.assertIn("2.38 explicitly", section(bhasya, 4))


    def test_2_38_status_abandonment_cases_and_temporal_exceptions(self):
        text = study(38)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [2, 3, 4])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        status = {
            ("contaminated_case", "neither_status"),
            ("nondiscriminative_cessation", "neither_status"),
            ("discriminative_ordinary", "neither_status"),
            ("discriminative_trainee", "trainee"),
            ("discriminative_beyond", "beyond_training"),
        }
        abandonment = {
            ("nondiscriminative_cessation", "cultivation_abandonable"),
            ("discriminative_ordinary", "cultivation_abandonable"),
            ("discriminative_trainee", "not_abandonable_class"),
            ("discriminative_beyond", "not_abandonable_class"),
            ("path_truth", "not_abandonable_class"),
        }
        self.assertEqual(valuation["AcquisitionStatus"], status)
        self.assertEqual(valuation["AcquisitionAbandonment"], abandonment)
        self.assertEqual(valuation["NeitherStatusCase"], {(case,) for case, _ in status})
        self.assertEqual(valuation["NonAbandonableCase"], {
            (case,) for case, _ in abandonment
        })
        self.assertEqual(valuation["StatusAggregate"], {
            ("trainee",), ("beyond_training",), ("neither_status",),
        })
        self.assertEqual(valuation["AbandonmentAggregate"], {
            ("cultivation_abandonable",), ("not_abandonable_class",),
        })
        self.assertEqual(valuation["StatusClass"], valuation["StatusAggregate"])
        self.assertEqual(valuation["AbandonmentClass"], valuation["AbandonmentAggregate"])
        exceptions = {"superknowledge_one", "superknowledge_two", "creation_consciousness"}
        self.assertEqual(valuation["MainException"], {(case,) for case in exceptions})
        self.assertEqual(valuation["UnobscuredIndeterminate"], {
            (case,) for case in exceptions | {"ordinary_unobscured"}
        })
        self.assertEqual(valuation["TemporalOption"], {
            (case, time) for case in exceptions
            for time in ("prior_time", "coarisen_time", "subsequent_time")
        } | {("ordinary_unobscured", "coarisen_time")})
        verse = tree.label()["SEM"].simplify()
        for predicate in ("StatusAggregate", "AbandonmentAggregate"):
            original = valuation[predicate]
            for relation in original:
                with self.subTest(missing=relation):
                    valuation[predicate] = original - {relation}
                    model = Model(valuation.domain, valuation)
                    self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
            valuation[predicate] = original
        original = valuation["TemporalOption"]
        for relation in (("ordinary_unobscured", "prior_time"),
                         ("ordinary_unobscured", "subsequent_time")):
            with self.subTest(forbidden=relation):
                valuation["TemporalOption"] = original | {relation}
                model = Model(valuation.domain, valuation)
                self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        valuation["TemporalOption"] = original - {("ordinary_unobscured", "coarisen_time")}
        model = Model(valuation.domain, valuation)
        self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        for old, new in (
            ("THREE[CNT=3] ->", "THREE[CNT=2] ->"),
            ("TWO[CNT=2] ->", "TWO[CNT=3] ->"),
            ("COARISEN[ONLY=true] ->", "COARISEN[ONLY=false] ->"),
            ("EXCEPTIONS[CASE=abl,REF=specified_group] ->",
             "EXCEPTIONS[CASE=ins,REF=specified_group] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.38_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        for argument in (
            "śaikṣāṇāṃ dharmāṇāṃ", "darśanabhāvanāheyānāṃ",
            "tasyotsargasyāyam apavādaḥ", "durbalatvāt",
            "kiṃ sarvasyaivānivṛtāvyākṛtasya", "abhyastasyecchanti",
        ):
            with self.subTest(argument=argument):
                self.assertIn(argument, section(bhasya, 2))
        rendering = section(bhasya, 3)
        self.assertIn("abandonable through cultivation", rendering)
        self.assertNotIn("abandoned through cultivation", rendering)
        self.assertIn("They also accept", rendering)
        self.assertIn("greatly habituated deportment-based cases", rendering)
        self.assertIn("not a claim that abandonment has", section(bhasya, 5))


    def test_2_39_form_restrictions_and_nonacquisition_times(self):
        text = study(39)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [3, 4, 3, 3])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        self.assertEqual(valuation["AcquisitionOption"], {
            ("obscured_manifest_range", "coarisen_time"),
            ("desire_form_general_range", "coarisen_time"),
            ("desire_form_general_range", "subsequent_time"),
        })
        self.assertEqual(valuation["NonAcquisitionOption"], {
            (dharma_time, nonacquisition_time)
            for dharma_time in ("past_time", "future_time")
            for nonacquisition_time in ("past_time", "present_time", "future_time")
        })
        self.assertEqual(valuation["PastFuture"], {("past_time",), ("future_time",)})
        self.assertEqual(valuation["Time"], {
            ("past_time",), ("present_time",), ("future_time",),
        })
        examples = valuation["NonAcquisition"]
        self.assertEqual(len(examples), 2)
        self.assertEqual(valuation["Unobscured"], examples)
        self.assertEqual(valuation["Indeterminate"], examples)
        self.assertFalse(valuation["Unwholesome"])
        self.assertEqual(valuation["ProvisionalPresentOption"], {
            ("present_time", "present_time"),
        })
        verse = tree.label()["SEM"].simplify()
        self.assertNotIn("ProvisionalPresentOption", str(verse))
        valuation["ProvisionalPresentOption"] = set()
        model = Model(valuation.domain, valuation)
        self.assertTrue(model.satisfy(verse, Assignment(model.domain)))
        for predicate in ("AcquisitionOption", "NonAcquisitionOption",
                          "Unobscured", "Indeterminate"):
            original = valuation[predicate]
            for relation in original:
                with self.subTest(missing=relation):
                    valuation[predicate] = original - {relation}
                    model = Model(valuation.domain, valuation)
                    self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
            valuation[predicate] = original
        original = valuation["AcquisitionOption"]
        for forbidden in (
            ("obscured_manifest_range", "prior_time"),
            ("obscured_manifest_range", "subsequent_time"),
            ("desire_form_general_range", "prior_time"),
        ):
            with self.subTest(forbidden=forbidden):
                valuation["AcquisitionOption"] = original | {forbidden}
                model = Model(valuation.domain, valuation)
                self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        for old, new in (
            ("ALSO[INHERITS=coarisen_only] ->", "ALSO[INHERITS=three_times] ->"),
            ("NOT[POL=negative] ->", "NOT[POL=positive] ->"),
            ("THAT[REF=nonacquisition] ->", "THAT[REF=acquisition] ->"),
            ("PASTFUTURE[CASE=gen,NUM=du,CNT=2] ->",
             "PASTFUTURE[CASE=gen,NUM=pl,CNT=3] ->"),
            ("THREE[CNT=3] ->", "THREE[CNT=2] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.39_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        self.assertNotIn("provisional", translation)
        self.assertNotIn("present dharma", translation)
        witness = section(bhasya, 2)
        for argument in ("kim anivṛtāvyākṛtasyaiva", "daurbalyasiddheḥ",
                         "kim aprāpter api", "nāratyaprāptiḥ"):
            self.assertIn(argument, witness)
        rendering = section(bhasya, 3)
        self.assertIn("even when intense", rendering)
        self.assertIn("provisional reading of the damaged gloss", rendering)
        self.assertIn("manifest and\nnonmanifest Form", rendering)


    def test_2_40_realm_product_qualified_absence_and_mutual_possession(self):
        text = study(40)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [2, 4, 2])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        realms = {"desire_realm", "form_realm", "formless_realm"}
        classes = realms | {"uncontaminated_class"}
        self.assertEqual(valuation["Realm"], {(realm,) for realm in realms})
        self.assertEqual(valuation["DharmaClass"], {(kind,) for kind in classes})
        self.assertEqual(valuation["NonAcquisitionRealm"], {
            (kind, realm) for kind in classes for realm in realms
        })
        self.assertEqual(valuation["RelinquishmentGround"], {
            ("nonacquisition_term", "acquiring_that_dharma_ground"),
            ("nonacquisition_term", "level_transition_ground"),
        })
        self.assertEqual(valuation["Person"], {("ordinary_person",), ("buddha",)})
        self.assertEqual(valuation["HasAttained"], {("buddha", "buddha_attainment")})
        self.assertEqual(valuation["OrdinaryByAbsence"], {("ordinary_person",)})
        self.assertEqual(valuation["NobleDharma"], {
            ("buddha_attainment",), ("disciple_lineage_attainment",),
            ("solitary_lineage_attainment",),
        })
        self.assertEqual(valuation["Secures"], {
            ("primary_acquisition_token", "base_dharma_token"),
            ("primary_acquisition_token", "higher_acquisition_token"),
            ("higher_acquisition_token", "primary_acquisition_token"),
        })
        verse = tree.label()["SEM"].simplify()
        for predicate in ("NonAcquisitionRealm", "HeldIdentification",
                          "RelinquishmentGround"):
            original = valuation[predicate]
            for relation in original:
                with self.subTest(missing=relation):
                    valuation[predicate] = original - {relation}
                    model = Model(valuation.domain, valuation)
                    self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
            valuation[predicate] = original
        valuation["Realm"] = valuation["Realm"] | {("uncontaminated_class",)}
        model = Model(valuation.domain, valuation)
        self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        for old, new in (
            ("CLASSES[CASE=gen,NUM=pl,CNT=4] ->",
             "CLASSES[CASE=gen,NUM=pl,CNT=3] ->"),
            ("ALSO[INHERITS=threefold_realm] ->",
             "ALSO[INHERITS=threefold_time] ->"),
            ("HELD[VOICE=reported] ->", "HELD[VOICE=settled] ->"),
            ("GROUNDS[CASE=abl,CNT=2,REF=that_dharma] ->",
             "GROUNDS[CASE=abl,CNT=2,REF=path_only] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.40_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        witness = section(bhasya, 2)
        for argument in (
            "vinā lābhenālābhaḥ", "buddho 'pi", "ity apare",
            "yathā sautrāntikānām",
        ):
            self.assertIn(argument, witness)
        for argument in (
            "aprāpter aprāptir utpadyate", "parasparasamanvāgamāt",
            "ṣaḍ bhavanti", "aṣṭādaśa", "dvitīyasya prāṇinaḥ",
            "kliṣṭasya kliṣṭasya vā",
        ):
            self.assertIn(argument, witness)
        rendering = section(bhasya, 3)
        for phrase in (
            "The Sautrāntika account", "Others say", "making six",
            "make eighteen", "What a festival of acquisitions",
            "non-acquisition of that non-acquisition",
        ):
            self.assertIn(phrase, rendering)
        self.assertIn("does not confer noble status", section(bhasya, 5))


    def test_2_41_same_class_alternatives_and_maturation_not_attainment(self):
        text = study(41)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [2, 4, 1, 2])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        result = valuation["nonreflective_result"]
        attainment = valuation["nonreflective_attainment"]
        self.assertNotEqual(result, attainment)
        self.assertEqual(valuation["Maturation"], {(result,)})
        self.assertEqual(valuation["MaturationOf"], {(result, attainment)})
        self.assertEqual(valuation["CessationOf"], {
            (result, valuation["consciousness_and_factors"]),
        })
        self.assertEqual(valuation["IncludedIn"], {
            (valuation["nonreflective_beings"], valuation["great_fruit_gods"]),
        })
        self.assertLess(valuation["NonreflectiveMember"], valuation["GreatFruitMember"])
        self.assertEqual(valuation["ReflectiveAt"], {
            (valuation["birth_boundary"],), (valuation["death_boundary"],),
        })
        self.assertNotIn((valuation["intervening_interval"],), valuation["ReflectiveAt"])
        self.assertEqual(valuation["RebirthAfter"], {
            (valuation["nonreflective_beings"], valuation["desire_realm"]),
        })
        expected = {
            "same_class_rebirth": (True, False),
            "entering_certainty": (False, True),
            "destiny_transition": (True, True),
            "neither_case": (False, False),
        }
        self.assertEqual({
            ((valuation[case],) in valuation["DeathRebirth"],
             (valuation[case],) in valuation["ClassChange"])
            for case in expected
        }, set(expected.values()))
        for case, (death_rebirth, class_change) in expected.items():
            self.assertEqual((valuation[case],) in valuation["DeathRebirth"], death_rebirth)
            self.assertEqual((valuation[case],) in valuation["ClassChange"], class_change)
        verse = tree.label()["SEM"].simplify()
        for predicate in ("Defines", "CessationOf", "Among", "Maturation", "IncludedIn"):
            original = valuation[predicate]
            for relation in original:
                with self.subTest(missing=relation):
                    valuation[predicate] = original - {relation}
                    model = Model(valuation.domain, valuation)
                    self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
            valuation[predicate] = original
        for old, new in (
            ("RESULT[CASE=nom,REF=result_not_attainment] ->",
             "RESULT[CASE=nom,REF=attainment] ->"),
            ("RIPENING[CASE=nom,REF=result] ->",
             "RIPENING[CASE=nom,REF=causal_attainment] ->"),
            ("THEY[CASE=nom,NUM=pl,REF=beings] ->",
             "THEY[CASE=nom,NUM=pl,REF=attainments] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.41_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        self.assertNotIn("non-reflective attainment is", translation)
        witness = section(bhasya, 2)
        for argument in (
            "pratisattvaṃ sarveṣu", "dharmasabhāgatā punaḥ",
            "dvitīyā niyāmam", "tṛtīyā gatisaṃcārāt",
            "sāmānyapadārtho", "sa eko 'py anekasmin",
            "na tūktaṃ dravyāntaram", "nadītoyasaṃnirodhavat",
            "asaṃjñisamāpatteḥ", "bhavanty upapattikāle cyutikāle",
            "apūrvānupacayāc", "yathottarakauravāṇāṃ",
        ):
            with self.subTest(argument=argument):
                self.assertIn(argument, witness)
        rendering = section(bhasya, 3)
        self.assertIn("Bases, Essences, and Principles", rendering)
        self.assertIn("Maturation\nof what? Of the non-reflective attainment", rendering)
        self.assertIn("Some among the Great Fruit gods", rendering)
        self.assertIn("Desire Realm, nowhere else", rendering)
        self.assertIn("spent", rendering)


    def test_2_42_present_acquisition_past_possession_and_result_timing(self):
        text = study(42)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [2, 2, 1, 1, 2, 2, 2])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        attainment = valuation["attainment"]
        result = valuation["result"]
        self.assertNotEqual(attainment, result)
        self.assertEqual(valuation["Wholesome"], {(attainment,)})
        self.assertEqual(valuation["Indeterminate"], {(result,)})
        self.assertEqual(valuation["MaturationOf"], {(result, attainment)})
        self.assertEqual(valuation["MaturationTiming"], {
            (attainment, valuation["next_rebirth"]),
        })
        self.assertEqual(valuation["AcquisitionTime"], {
            (attainment, valuation["present"]),
        })
        self.assertEqual(valuation["AtLevel"], {
            (attainment, valuation["fourth_dhyana"]),
        })
        self.assertEqual(valuation["PossessesInstance"], {
            (valuation["first_moment"], valuation["present"]),
            (valuation["second_moment"], valuation["past"]),
            (valuation["second_moment"], valuation["present"]),
        })
        self.assertFalse(valuation["Eligible"])
        self.assertFalse(valuation["CultivatesFuture"])
        self.assertFalse(valuation["AcquiredWithLevel"])
        self.assertEqual(valuation["ReportedNecessaryRegaining"], {
            (valuation["fallen_practitioner"], attainment),
        })
        self.assertEqual(valuation["ReportedRebirth"], {
            (valuation["fallen_practitioner"], valuation["nonreflective_beings"]),
        })
        verse = tree.label()["SEM"].simplify()
        for predicate in ("CessationOf", "AtLevel", "EnteredWithWish",
                          "Wholesome", "MaturationTiming", "AcquisitionTime"):
            original = valuation[predicate]
            for relation in original:
                with self.subTest(missing=relation):
                    valuation[predicate] = original - {relation}
                    model = Model(valuation.domain, valuation)
                    self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
            valuation[predicate] = original
        for predicate, relation in (
            ("AcquisitionTime", (attainment, valuation["past"])),
            ("MaturationTiming", (attainment, "later_existence")),
            ("Eligible", (valuation["noble"], attainment)),
        ):
            original = valuation[predicate]
            valuation[predicate] = original | {relation}
            model = Model(valuation.domain, valuation)
            self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
            valuation[predicate] = original
        for old, new in (
            ("LIKEWISE[CARRIES=cessation_only] ->",
             "LIKEWISE[CARRIES=all_result_properties] ->"),
            ("FINAL[CASE=loc,REF=fourth] ->", "FINAL[CASE=loc,REF=third] ->"),
            ("ONLY[EXCLUSIVE=true] ->", "ONLY[EXCLUSIVE=false] ->"),
            ("ONETIME[CASE=nom,REF=present_not_once] ->",
             "ONETIME[CASE=nom,REF=once_only] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.42_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        witness = section(bhasya, 2)
        for argument in (
            "etāvat tathāśabdenānvākṛṣyate", "pañcaskandhako vipākaḥ",
            "kilāvaśyaṃ punar", "niyāmaṃ nāvakrāmati",
            "mahābhisaṃskārasādhyatvād", "prātimokṣasaṃvaraḥ",
            "atītayā 'pi samanvāgato", "nānāgatā bhāvyate",
        ):
            self.assertIn(argument, witness)
        rendering = section(bhasya, 3)
        self.assertIn("comprises five Bases", rendering)
        self.assertIn("not of unfixed timing", rendering)
        self.assertIn("it is said", rendering)
        self.assertIn("also possesses the past instance", rendering)
        self.assertNotIn("Same-class", section(bhasya, 9))


    def test_2_43_timing_application_and_crossverse_accounts(self):
        text = study(43)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [4, 1, 1, 1, 3, 3])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        attainment = valuation["attainment"]
        self.assertEqual(valuation["MaturationOption"], {
            (attainment, valuation["next_rebirth"]),
            (attainment, valuation["later_existence"]),
        })
        self.assertEqual(valuation["UnfixedMaturation"], {(attainment,)})
        self.assertEqual(valuation["CanFailToMature"], {(attainment,)})
        self.assertEqual(valuation["Wholesome"], {(attainment,)})
        self.assertFalse(valuation["EthicallyIndeterminate"])
        self.assertEqual(valuation["ResultBaseCount"], {
            (attainment, valuation["four_bases"]),
        })
        self.assertEqual(valuation["RestrictedTo"], {(attainment, valuation["noble"])})
        self.assertEqual(valuation["AcquisitionRule"], {
            (attainment, valuation["application"]),
        })
        for predicate in ("PastAcquired", "FutureCultivated", "DispassionAcquisitionRule"):
            self.assertFalse(valuation[predicate])
        self.assertEqual(valuation["EarlierProduction"], {(valuation["western_account"],)})
        self.assertEqual(valuation["MasteryWithoutPriorProduction"], {
            (valuation["mastery_reply"],),
        })
        self.assertEqual(valuation["AcquisitionAt"], {
            (valuation["buddha"], valuation["knowledge_of_exhaustion"]),
        })
        self.assertEqual(valuation["ReportedMomentCount"], {
            (valuation["kashmir_account"], valuation["thirty_four"]),
        })
        self.assertEqual(16 + 2 * 9, 34)
        verse = tree.label()["SEM"].simplify()
        self.assertNotIn("EarlierProduction", str(verse))
        self.assertNotIn("ReportedMomentCount", str(verse))
        for predicate in (
            "CessationOf", "Purpose", "AtLevel", "Wholesome",
            "MaturationOption", "UnfixedMaturation", "RestrictedTo", "AcquisitionRule",
        ):
            original = valuation[predicate]
            for relation in original:
                with self.subTest(missing=relation):
                    valuation[predicate] = original - {relation}
                    model = Model(valuation.domain, valuation)
                    self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
            valuation[predicate] = original
        valuation["MaturationOption"] = valuation["MaturationOption"] | {
            (attainment, "present_life"),
        }
        model = Model(valuation.domain, valuation)
        self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        for old, new in (
            ("LIKEWISE[CARRIES=cessation_only] ->",
             "LIKEWISE[CARRIES=all_properties] ->"),
            ("ABIDING[PURPOSE=peaceful_abiding] ->",
             "ABIDING[PURPOSE=escape] ->"),
            ("TWO[CNT=2] ->", "TWO[CNT=3] ->"),
            ("UNFIXED[AXIS=maturation] ->", "UNFIXED[AXIS=ethics] ->"),
            ("APPLICATION[FORM=tas] ->", "APPLICATION[FORM=instrumental] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.43_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        self.assertIn("or may not occur", translation)
        witness = section(bhasya, 2)
        for argument in (
            "śāntavihārasaṃjñāpūrvakeṇa", "catuḥskandhako vipākaḥ",
            "cittabalena tadbhāvanāt", "bodhilabhyā muneḥ",
            "sthaviropaguptasyāpīdaṃ", "catustriṃśatā kila",
            "ṣoḍaśabhir", "cāṣṭādaśabhir", "navānantaryavimukti",
            "na tu āsrava mārgāvyutthānāt", "bahirdeśakāḥ",
            "pūrvam eva tu varṇayanti kāśmīrāḥ",
        ):
            self.assertIn(argument, witness)
        rendering = section(bhasya, 3)
        self.assertIn("comprises four Bases", rendering)
        self.assertIn("Western teachers say", rendering)
        self.assertIn("The Kāśmīra teachers maintain", rendering)
        self.assertIn("damaged clause", rendering)
        self.assertIn("first half of 2.44", section(bhasya, 7))


    def test_2_44_singular_awakening_shared_basis_and_first_production(self):
        text = study(44)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [5, 2, 3])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        cessation = valuation["cessation"]
        nonreflective = valuation["nonreflective"]
        self.assertEqual(valuation["Attainment"], {(cessation,), (nonreflective,)})
        self.assertEqual(valuation["AcquiredWithAwakening"], {
            (valuation["sage"], cessation),
        })
        bases = {"desire_realm_basis", "form_realm_basis"}
        self.assertEqual(valuation["BasisRealm"], {(basis,) for basis in bases})
        self.assertEqual(valuation["CanAriseWithBasis"], {
            (attainment, basis) for attainment in (cessation, nonreflective)
            for basis in bases
        })
        self.assertEqual(valuation["AtLevel"], {
            (cessation, valuation["summit"]),
            (nonreflective, valuation["fourth_dhyana"]),
        })
        self.assertEqual(valuation["FirstProductionAmong"], {
            (cessation, valuation["humans"]),
        })
        self.assertEqual(valuation["LaterProductionAmong"], {
            (cessation, valuation["form_realm"]),
        })
        self.assertEqual(valuation["RequiresPriorLoss"], {
            (valuation["main_account"], cessation),
        })
        self.assertEqual(valuation["ConsciousInAttainment"], {
            (valuation["vasumitra_account"],),
        })
        self.assertEqual(valuation["PastConditionAccount"], {
            (valuation["vaibhasika_account"],),
        })
        self.assertEqual(valuation["MutualSeedAccount"], {
            (valuation["earlier_teachers"],),
        })
        verse = tree.label()["SEM"].simplify()
        for predicate in (
            "AcquiredWithAwakening", "DeniesPriorProduction", "ReportedCount",
            "CanAriseWithBasis", "FirstProductionAmong",
        ):
            original = valuation[predicate]
            for relation in original:
                with self.subTest(missing=relation):
                    valuation[predicate] = original - {relation}
                    model = Model(valuation.domain, valuation)
                    self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
            valuation[predicate] = original
        valuation["FirstProductionAmong"] = valuation["FirstProductionAmong"] | {
            (cessation, valuation["form_realm"]),
        }
        model = Model(valuation.domain, valuation)
        self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        for old, new in (
            ("AWAKENINGACQUIRED[CASE=nom,NUM=sg,REF=cessation] ->",
             "AWAKENINGACQUIRED[CASE=nom,NUM=pl,REF=both] ->"),
            ("REASON[FORM=tas,CNT=34] ->", "REASON[FORM=tas,CNT=33] ->"),
            ("REALMBASIS[CASE=loc,CNT=2] ->", "REALMBASIS[CASE=loc,CNT=3] ->"),
            ("INITIALLY[SCOPE=first_production] ->",
             "INITIALLY[SCOPE=all_production] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.44_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        self.assertNotIn("[the attainments]", translation)
        self.assertIn("the attainment of cessation is acquired", translation)
        witness = section(bhasya, 2)
        for argument in (
            "pañcavyavacāraḥ", "divye manomaye", "nikāyāntarīyā",
            "prāthamakalpikaṃ", "anyonyabījakaṃ", "bhadantavasumitras",
            "bhadantaghoṣaka", "sati hi vijñāne", "avidyāsaṃsparśajaṃ",
            "mahābhūtasamatāpādanāt", "tad etan na varṇayanti",
        ):
            self.assertIn(argument, witness)
        rendering = section(bhasya, 3)
        for phrase in (
            "With Cognition", "body equipped with Faculties",
            "Great Elements into equilibrium", "They do not accept this account",
            "because contact in the production of feeling",
            "predicate damaged", "problematic\nrealm reading",
        ):
            self.assertIn(phrase, rendering)


    def test_2_45_life_support_four_marks_and_death_alternatives(self):
        text = study(45)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [6, 6])
        self.assertEqual(tokens[-4:], ["jātiḥ", "jarā", "sthitiḥ", "anityatā"])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        self.assertEqual(valuation["Supports"], {
            (valuation["lifespan"], valuation["warmth"]),
            (valuation["lifespan"], valuation["cognition"]),
        })
        self.assertEqual(valuation["Mark"], {
            (valuation[name],) for name in ("arising", "aging", "persistence", "impermanence")
        })
        expected = {
            "lifespan_only": (True, False),
            "merit_only": (False, True),
            "both_exhausted": (True, True),
            "neither_exhausted": (False, False),
        }
        self.assertEqual(valuation["DeathCase"], {
            (valuation[case],) for case in expected
        })
        for case, (lifespan, merit) in expected.items():
            self.assertEqual((valuation[case],) in valuation["LifespanExhausted"], lifespan)
            self.assertEqual((valuation[case],) in valuation["MeritExhausted"], merit)
        self.assertEqual(valuation["FailureToAvoidHarm"], {
            (valuation["neither_exhausted"],),
        })
        self.assertEqual(valuation["DistinctLifeEntity"], {
            (valuation["real_entity_account"],),
        })
        self.assertEqual(valuation["ProjectedDuration"], {
            (valuation["projected_duration_account"],),
        })
        verse = tree.label()["SEM"].simplify()
        self.assertNotIn("DistinctLifeEntity", str(verse))
        for predicate in ("Identifies", "Supports", "Mark"):
            original = valuation[predicate]
            for relation in original:
                with self.subTest(missing=relation):
                    valuation[predicate] = original - {relation}
                    model = Model(valuation.domain, valuation)
                    self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
            valuation[predicate] = original
        for old, new in (
            ("PAIR[CASE=gen,NUM=du,CNT=2] ->",
             "PAIR[CASE=gen,NUM=sg,CNT=1] ->"),
            ("RELATIVE[CASE=nom,REF=lifespan] ->",
             "RELATIVE[CASE=nom,REF=karma] ->"),
            ("MARKWORD[CASE=nom,NUM=pl] ->", "MARKWORD[CASE=nom,NUM=sg] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.45_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        self.assertIn("ūṣmavijñānayor", section(text, 2))
        self.assertNotIn("ūṣmavijñāyor", section(text, 2))
        witness = section(bhasya, 2)
        for argument in (
            "nikāyasabhāgasya sthitikālāvedhaḥ", "kṣipteṣuḥ",
            "dravyāntaram evāyur", "caturthī viṣamāparihāreṇa",
            "jñānaprasthāne", "samāpannānāṃ rūpārūpyāvacarāṇāṃ",
            "duddhānāṃ", "asty akālamṛtyuḥ", "uktaṃ jīvitam",
            "sthitiṃ jarāṃ cābhisamasya", "ataś catvāry eva",
        ):
            self.assertIn(argument, witness)
        rendering = section(bhasya, 3)
        self.assertIn("Life Faculty", rendering)
        self.assertIn("Formless", rendering)
        self.assertIn("protected cases", rendering)
        self.assertIn("Others suppose", rendering)
        self.assertIn("second naming", section(bhasya, 5))


    def test_2_46_nine_members_eight_one_targets_and_causal_restriction(self):
        text = study(46)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [2, 2, 6])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        primary = {value for value, in valuation["Primary"]}
        secondary = {value for value, in valuation["Secondary"]}
        members = {value for value, in valuation["GroupMember"]}
        self.assertEqual(len(primary), 4)
        self.assertEqual(len(secondary), 4)
        self.assertTrue(primary.isdisjoint(secondary))
        self.assertEqual(members, primary | secondary | {"base_dharma"})
        secondary_of = {
            (valuation[f"{name}_secondary"], valuation[name])
            for name in ("arising", "persistence", "aging", "impermanence")
        }
        self.assertEqual(valuation["SecondaryOf"], secondary_of)
        operations = valuation["OperatesOn"]
        self.assertEqual(operations, {
            (mark, target) for mark in primary for target in members if mark != target
        } | secondary_of)
        self.assertEqual(len(operations), 36)
        for mark in primary:
            self.assertEqual(len({target for source, target in operations if source == mark}), 8)
        for mark in secondary:
            self.assertEqual(len({target for source, target in operations if source == mark}), 1)
        self.assertEqual(valuation["Generates"], {(valuation["arising"], "ready_case")})
        self.assertEqual(valuation["CauseConditionConjunction"], {("ready_case",)})
        self.assertEqual(valuation["Candidate"], {("ready_case",), ("unready_case",)})
        self.assertEqual(valuation["DistinctMarkEntities"], {
            (valuation["vaibhasika_account"],),
        })
        self.assertEqual(valuation["StreamInterpretation"], {
            (valuation["sautrantika_account"],),
        })
        verse = tree.label()["SEM"].simplify()
        for predicate in ("SecondaryOf", "OperatesOn", "CauseConditionConjunction"):
            original = valuation[predicate]
            for relation in original:
                with self.subTest(missing=relation):
                    valuation[predicate] = original - {relation}
                    model = Model(valuation.domain, valuation)
                    self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
            valuation[predicate] = original
        valuation["Generates"] = valuation["Generates"] | {
            (valuation["arising"], "unready_case"),
        }
        model = Model(valuation.domain, valuation)
        self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        for old, new in (
            ("OFTHESE[CASE=gen,REF=primary_marks] ->",
             "OFTHESE[CASE=gen,REF=all_dharmas] ->"),
            ("EIGHTONE[PRIMARY=8,SECONDARY=1] ->",
             "EIGHTONE[PRIMARY=1,SECONDARY=8] ->"),
            ("WITHOUT[REQUIRES=conjunction] ->",
             "WITHOUT[REQUIRES=arising_alone] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.46_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        witness = section(bhasya, 2)
        for argument in (
            "ātmanā navamo", "kukkuṭī", "iti sautrāntikāḥ",
            "nikāyasabhāgacittaṃ", "abhūtvābhāva utpādaḥ",
            "mahāpuruṣalakṣaṇāni", "kāritrakālabhedāt",
            "harītakīṃ", "rūpasyotpāda", "iti vaibhāṣikāḥ",
            "uktāni lakṣaṇāni",
        ):
            self.assertIn(argument, witness)
        rendering = section(bhasya, 3)
        self.assertIn("six\nEssences", rendering)
        self.assertIn("Earth Principle", rendering)
        self.assertIn("maintain the Vaibhāṣikas", rendering)
        self.assertIn("barley", rendering)
        self.assertIn("sandalwood", rendering)


    def test_2_47_collections_classifications_and_continuation(self):
        text = study(47)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [2, 2, 1])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        groups = {"name_group_kind", "sentence_group_kind", "syllable_group_kind"}
        self.assertEqual(valuation["GroupKind"], {(group,) for group in groups})
        self.assertEqual(valuation["CollectionOf"], {
            ("name_group_kind", "designation_kind"),
            ("sentence_group_kind", "sentence_kind"),
            ("syllable_group_kind", "syllable_kind"),
        })
        self.assertEqual(valuation["RealmOption"], {
            (group, realm) for group in groups for realm in ("desire_realm", "form_realm")
        })
        for predicate in ("SentientClassed", "HomogeneousOutflow", "Indeterminate",
                          "Unobscured"):
            self.assertEqual(valuation[predicate], {(group,) for group in groups})
        self.assertEqual(valuation["ContinuesTo"], {
            (valuation["likewise"], valuation["next_verse_same_class"]),
        })
        self.assertEqual(valuation["Possesses"], {
            (valuation["signifier"], valuation["illustrative_group"]),
        })
        self.assertEqual(valuation["AllowsFormless"], {(valuation["other_teachers"],)})
        self.assertEqual(valuation["CallsInexpressible"], {(valuation["other_teachers"],)})
        verse = tree.label()["SEM"].simplify()
        for predicate in (
            "CollectionOf", "RealmOption", "SentientClassed",
            "HomogeneousOutflow", "Indeterminate", "ContinuesTo",
        ):
            original = valuation[predicate]
            for relation in original:
                with self.subTest(missing=relation):
                    valuation[predicate] = original - {relation}
                    model = Model(valuation.domain, valuation)
                    self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
            valuation[predicate] = original
        for old, new in (
            ("GROUPS[CASE=nom,NUM=pl,CNT=3] ->",
             "GROUPS[CASE=nom,NUM=pl,CNT=2] ->"),
            ("COLLECTIONS[CASE=nom,NUM=pl,MATCH=respectively] ->",
             "COLLECTIONS[CASE=nom,NUM=pl,MATCH=interchangeably] ->"),
            ("REALMSENTIENT[CASE=nom,NUM=pl,REALMS=2] ->",
             "REALMSENTIENT[CASE=nom,NUM=pl,REALMS=3] ->"),
            ("LIKEWISE[REF=next_verse_selected_classes] ->",
             "LIKEWISE[REF=all_properties] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.47_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        for argument in (
            "lipyavayavāḥ", "utpādayaty āhosvit prakāśayati",
            "paścimo vijñaptikṣaṇa", "arthasahajaṃ",
            "apatyānāṃ pitṛbhir", "asaṃskṛtānāṃ",
            "iti vaibhāṣikāḥ", "yaś ca dyotayati", "tathā // 2.47",
        ):
            self.assertIn(argument, section(bhasya, 2))
        rendering = section(bhasya, 3)
        self.assertIn("nine meanings", rendering)
        self.assertIn("last item is the running", rendering)
        self.assertIn("the one who signifies possesses them", rendering)
        self.assertIn("not all dharmas", rendering.lower())
        self.assertIn("does not transfer the two-Realm restriction", section(bhasya, 6))


    def test_2_48_result_sorts_selective_inheritance_and_section_close(self):
        text = study(48)
        grammar, tokens = grammar_and_tokens(text)
        tree = list(FeatureChartParser(grammar).parse(tokens))[0]
        self.assertEqual([len(child.leaves()) for child in tree], [6, 4, 2])
        valuation = load_valuation(dict(BLOCK.findall(section(text, 8)))["nltk-valuation"])
        twofold = {valuation[name] for name in ("same_class", "acquisition", "marks")}
        outflow_only = {valuation[name] for name in (
            "non_reflective_attainment", "cessation_attainment", "non_acquisition",
        )}
        all_kinds = twofold | outflow_only
        self.assertEqual(valuation["VerseKind"], {(kind,) for kind in all_kinds})
        self.assertEqual(valuation["OutflowOnlyKind"], {(kind,) for kind in outflow_only})
        self.assertEqual(valuation["ResultOption"], {
            (kind, valuation[result])
            for kind in twofold for result in ("outflow", "maturation")
        } | {(kind, valuation["outflow"]) for kind in outflow_only})
        self.assertEqual(len(valuation["ResultOption"]), 9)
        self.assertEqual(valuation["RealmOption"], {
            (valuation["same_class"], valuation[realm])
            for realm in ("desire", "form", "formless")
        })
        self.assertEqual(valuation["SentientClassed"], {(kind,) for kind in all_kinds})
        self.assertEqual(valuation["NonSentientClassed"], {(valuation["marks"],)})
        for predicate in ("HomogeneousOutflow", "Unobscured", "Indeterminate"):
            self.assertEqual(valuation[predicate], {(valuation["same_class"],)})
        self.assertEqual(valuation["AlreadyExplained"], {
            (valuation["non_reflective_result"],), (valuation["life"],),
        })
        self.assertNotEqual(
            valuation["non_reflective_result"], valuation["non_reflective_attainment"],
        )
        self.assertEqual(valuation["Closes"], {
            (valuation["unit"], valuation["dissociated_formations"]),
        })
        self.assertEqual(valuation["QuestionOf"], {
            (valuation["next_unit"], valuation["causes_conditions"]),
        })
        self.assertEqual(valuation["Answers"], set())
        verse = tree.label()["SEM"].simplify()
        model = Model(valuation.domain, valuation)
        self.assertTrue(model.satisfy(verse, Assignment(model.domain)))
        for predicate in ("ResultOption", "HomogeneousOutflow", "Unobscured",
                          "Indeterminate"):
            original = valuation[predicate]
            for relation in original:
                with self.subTest(predicate=predicate, missing=relation):
                    valuation[predicate] = original - {relation}
                    model = Model(valuation.domain, valuation)
                    self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
            valuation[predicate] = original
        original = valuation["SentientClassed"]
        valuation["SentientClassed"] = original - {(valuation["same_class"],)}
        model = Model(valuation.domain, valuation)
        self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        valuation["SentientClassed"] = original
        original = valuation["ResultOption"]
        for kind in outflow_only:
            with self.subTest(incorrect_maturation=kind):
                valuation["ResultOption"] = original | {(kind, valuation["maturation"])}
                model = Model(valuation.domain, valuation)
                self.assertFalse(model.satisfy(verse, Assignment(model.domain)))
        valuation["ResultOption"] = original
        for old, new in (
            ("PRONOUN[CASE=nom,NUM=sg,REF=same_class] ->",
             "PRONOUN[CASE=nom,NUM=sg,REF=name_groups] ->"),
            ("ALSO[FORCE=additional] ->", "ALSO[FORCE=exclusive] ->"),
            ("ACQUISITIONS[CASE=nom,NUM=pl] ->",
             "ACQUISITIONS[CASE=nom,NUM=dual] ->"),
            ("TWOWAYS[SORTS=2] ->", "TWOWAYS[SORTS=1] ->"),
            ("MARKS[CASE=nom,NUM=pl] ->", "MARKS[CASE=acc,NUM=pl] ->"),
            ("AND[SCOPE=twofold] ->", "AND[SCOPE=unqualified] ->"),
            ("COMPOUND[CASE=nom,NUM=pl,ATTAINMENTS=2,NONACQUISITION=1] ->",
             "COMPOUND[CASE=nom,NUM=pl,ATTAINMENTS=1,NONACQUISITION=1] ->"),
        ):
            with self.subTest(feature=old):
                self.assertIn(old, text)
                changed, changed_tokens = grammar_and_tokens(text.replace(old, new, 1))
                self.assertEqual(list(FeatureChartParser(changed).parse(changed_tokens)), [])
        translation = section(text, 5).split(
            "### Bhāṣya-informed study translation\n", 1,
        )[1].strip()
        bhasya = (STUDIES / "VAK_2.48_bhasya.md").read_text(encoding="utf-8")
        self.assertTrue(section(bhasya, 1).strip().endswith(translation))
        for passage in (
            "kāmarūpārūpyāvacarī", "dvidheti vartate prāptivat",
            "naiḥṣyandikā eva", "śeṣam eṣāṃ vaktavyam uktam",
            "cāsaṃjñikajīvitayor", "samanvāgamavacanāt",
            "sattvāsattvākhyatoktā", "sarvasaṃskṛtasahabhūtvāt",
            "uktā viprayuktāḥ",
        ):
            self.assertIn(passage, section(bhasya, 2))
        rendering = section(bhasya, 3)
        self.assertIn("Desire, Form, and Formless Realms", rendering)
        self.assertIn("the non-reflective result and life", rendering)
        self.assertIn("statement of possession", rendering)
        self.assertIn("all conditioned dharmas", rendering)
        self.assertIn("The dissociated formations have been explained.", rendering)
        self.assertNotIn("next question", rendering)
        self.assertIn("does not transfer the two-Realm limit", section(bhasya, 4))
        self.assertIn("Nor does closing this discussion close the", section(bhasya, 6))


if __name__ == "__main__":
    unittest.main()
