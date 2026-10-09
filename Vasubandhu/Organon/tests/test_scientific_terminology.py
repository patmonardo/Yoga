"""Regression tests for Scientific terminology in the Dhatu studies."""

from pathlib import Path
import re
import tempfile
import unittest

from audit_karika_sections import check_headings, headings_in


REPO_ROOT = Path(__file__).resolve().parents[3]
STUDY_DIR = Path(__file__).resolve().parents[1] / "01-dhatu"
INSTRUCTIONS = (
    REPO_ROOT
    / ".github"
    / "instructions"
    / "vasubandhu-organon.instructions.md"
)
REVIEWED_VERSES = range(29, 48)
LEGACY_TERMS = (
    ("dhatu rendered as element", re.compile(r"\belement(?:s|al)?\b", re.I)),
    ("sense-base", re.compile(r"\bsense[- ]bases?\b", re.I)),
    (
        "āyatana rendered as a contact-base",
        re.compile(r"\b(?:contact[- ]bases?|bases?\s+of\s+contact)\b", re.I),
    ),
    ("Essence Base", re.compile(r"\bEssence\s+Bases?\b", re.I)),
    ("Essence Principle", re.compile(r"\bEssence\s+Principles?\b", re.I)),
    (
        "legacy Essence Principle identifier",
        re.compile(r"\bEssencePrinciple\b", re.I),
    ),
    (
        "obsolete Mental-Cognition compound",
        re.compile(
            r"\bMental[- ]Cognition\s+Principles?\b"
            r"|\bMentalCognitionPrinciple\b",
            re.I,
        ),
    ),
    (
        "obsolete Organon framing",
        re.compile(
            r"\bOrganon\s+(?:rendering|reading|interpretation)\b"
            r"|Philosophical and Organon Study",
            re.I,
        ),
    ),
)
REQUIRED_MAPPINGS = (
    "`skandha` -> **Base**",
    "`āyatana` -> **Essence**",
    "`dhātu` -> **Principle**",
    "`bhūta` / `mahābhūta` -> **Great Principle**",
    "`bhautika` -> **Principle-dependent**",
    "*prajñā* as **Science of Principles**",
)


def reviewed_studies():
    for verse in REVIEWED_VERSES:
        stem = f"VAK_1.{verse}"
        yield STUDY_DIR / f"{stem}.md"
        yield STUDY_DIR / f"{stem}_bhasya.md"


class ScientificTerminologyTests(unittest.TestCase):
    def test_vak_1_41_uses_science_of_principles_for_prajna(self):
        path = STUDY_DIR / "VAK_1.41.md"
        text = path.read_text(encoding="utf-8")
        self.assertTrue(
            any(
                "| *dhīḥ* |" in line
                and "*prajñā* (Science of Principles)" in line
                for line in text.splitlines()
            ),
            "VAK 1.41 must preserve the Bhāṣya's *prajñā* gloss as "
            "Science of Principles in Lexical Analysis",
        )

    def test_vak_1_42_uses_scientific_renderings(self):
        path = STUDY_DIR / "VAK_1.42_bhasya.md"
        text = path.read_text(encoding="utf-8")
        self.assertIn("a certain Science of Principles", text)
        self.assertIn("These are only Dharmas and only cause and", text)
        self.assertNotIn("only Essences", text)

    def test_vak_1_43_maps_visaya_to_condition(self):
        path = STUDY_DIR / "VAK_1.43.md"
        text = path.read_text(encoding="utf-8")
        self.assertIn(
            "| a-prāpta-viṣayam | nominative neuter singular compound | "
            "having a Condition not physically contacted |",
            text,
        )

    def test_vak_1_44_distinguishes_condition_from_object(self):
        karika = (STUDY_DIR / "VAK_1.44.md").read_text(encoding="utf-8")
        bhasya = (STUDY_DIR / "VAK_1.44_bhasya.md").read_text(encoding="utf-8")
        self.assertIn("apprehension of a Condition equal in extent", karika)
        self.assertRegex(
            bhasya,
            r"accumulated\s+support and accumulated object",
        )

    def test_vak_1_45_distinguishes_support_from_object(self):
        karika = (STUDY_DIR / "VAK_1.45.md").read_text(encoding="utf-8")
        commentary = (STUDY_DIR / "VAK_1.45_bhasya.md").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "dependence on both Faculty and Object",
            karika,
        )
        self.assertRegex(
            commentary,
            r"Visible Form, however, can be an Object for Mind-Cognition"
            r"\s+and another Eye-Cognition\.",
        )
        self.assertIn("support-status and specificity", commentary)
        self.assertNotIn("field-support", commentary)

    def test_vak_1_46_preserves_plane_limits_and_condition(self):
        karika = (STUDY_DIR / "VAK_1.46.md").read_text(encoding="utf-8")
        commentary = (STUDY_DIR / "VAK_1.46_bhasya.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("P(Body) ≤ P(EyeFaculty)", karika)
        self.assertRegex(
            commentary,
            r"A visible Form from the Eye's plane or a lower plane can be a"
            r"\s+Condition for Eye-Cognition\.",
        )
        self.assertIn(
            "| Eye-Cognition | Desire Realm and first meditative level |",
            commentary,
        )
        self.assertNotRegex(karika + commentary, r"\bfield\b")

    def test_vak_1_47_preserves_plane_rules_and_exception(self):
        karika = (STUDY_DIR / "VAK_1.47.md").read_text(encoding="utf-8")
        commentary = (STUDY_DIR / "VAK_1.47_bhasya.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("P(Body) ≤ P(Ear)", karika)
        self.assertIn("P(BodyCognition)", karika)
        self.assertIn("Body-Cognition belongs to its own plane", commentary)
        self.assertRegex(
            commentary,
            r"Mind may be on the same, higher, or lower plane relative to Body,"
            r"\s+Mind-Cognition, and Dharmas\.",
        )
        self.assertNotRegex(
            karika + commentary,
            r"\bfield\b|Essence Principles|Principle Pipeline|Pure Principle",
        )

    def test_reviewed_verse_pairs_exist(self):
        for path in reviewed_studies():
            with self.subTest(study=path.name):
                self.assertTrue(path.is_file(), f"Missing paired study: {path}")

    def test_reviewed_studies_use_scientific_vocabulary(self):
        for path in reviewed_studies():
            with self.subTest(study=path.name):
                text = path.read_text(encoding="utf-8")
                self.assertRegex(text, r"\bPrinciples?\b")
                for label, pattern in LEGACY_TERMS:
                    match = pattern.search(text)
                    if match:
                        line = text.count("\n", 0, match.start()) + 1
                        self.fail(
                            f"{path.relative_to(REPO_ROOT)}:{line}: "
                            f"legacy term {label!r} ({match.group(0)!r})"
                        )

    def test_governing_instructions_declare_scientific_mappings(self):
        text = INSTRUCTIONS.read_text(encoding="utf-8")
        for mapping in REQUIRED_MAPPINGS:
            with self.subTest(mapping=mapping):
                self.assertIn(mapping, text)

    def test_karika_section_structure_follows_pattern_3(self):
        for verse in range(1, 49):
            path = STUDY_DIR / f"VAK_1.{verse:02d}.md"
            with self.subTest(verse=verse):
                self.assertTrue(path.is_file(), f"Missing kārikā study: {path}")
                errors = check_headings(headings_in(path))
                self.assertEqual(errors, [], f"{path.name}: {errors}")

    def test_karika_section_check_ignores_child_headings(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "study.md"
            path.write_text(
                "\n".join(
                    f"## {number}. {section}\n### Verse-specific child"
                    for number, section in enumerate(
                        (
                            "Sanskrit (Devanāgarī)",
                            "Sanskrit (IAST)",
                            "Lexical Analysis",
                            "Grammar",
                            "Translation",
                            "Philosophical Translation",
                            "Technical Vocabulary",
                            "Logical Determination",
                            "Interpretive Note",
                            "OWL++ Seed",
                        ),
                        start=1,
                    )
                ),
                encoding="utf-8",
            )

            headings = headings_in(path)
            self.assertTrue(all(heading.startswith("## ") for heading in headings))
            self.assertEqual(check_headings(headings), [])


if __name__ == "__main__":
    unittest.main()
