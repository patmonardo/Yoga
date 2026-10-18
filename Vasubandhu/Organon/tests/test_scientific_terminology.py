"""Regression tests for Scientific terminology across the kārikā Organon.

The vocabulary scan covers every chapter. The per-verse checks pin doctrinal
decisions (not exact sentences) in the Dhātu chapter.
"""

from pathlib import Path
import re
import tempfile
import unittest

from audit_karika_sections import check_headings, headings_in


REPO_ROOT = Path(__file__).resolve().parents[3]
ORGANON_DIR = Path(__file__).resolve().parents[1]
STUDY_DIR = ORGANON_DIR / "01-dhatu"
INSTRUCTIONS = (
    REPO_ROOT
    / ".github"
    / "instructions"
    / "vasubandhu-organon.instructions.md"
)
LEGACY_TERMS = (
    # Capitalised Element(s) is the mandated rendering of bhūta.
    ("lowercase element", re.compile(r"\belement(?:s|al)?\b")),
    # dhātu is never Element; "Element Principle" (a Principle of an
    # Element) is allowed because Principle still renders dhātu.
    (
        "dhatu compound rendered as Element",
        re.compile(
            r"\b(?:eye|ear|nose|tongue|body|mind|form|visible|sound|odou?r"
            r"|taste|tangible|dharma|cognition|earth|water|fire|wind"
            r"|eighteen|six)[- ]Elements?\b",
            re.I,
        ),
    ),
    ("sense-base", re.compile(r"\bsense[- ]bases?\b", re.I)),
    (
        "āyatana rendered as a contact-base",
        re.compile(r"\b(?:contact[- ]bases?|bases?\s+of\s+contact)\b", re.I),
    ),
    ("Essence Base", re.compile(r"\bEssence[ ]Bases?\b", re.I)),
    ("Essence Principle", re.compile(r"\bEssence[ ]Principles?\b", re.I)),
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
    ("aggregate for a non-skandha whole", re.compile(r"\baggregates?\b", re.I)),
    ("first-pass wording", re.compile(r"\bfirst[- ]pass\b", re.I)),
    ("reference to the VAK folder", re.compile(r"Vasubandhu/VAK/")),
)
OBSOLETE_HEADING = re.compile(
    r"^## (?:\d+\. )?.*\bOrganon\s+(?:Reading|Study|Contact Point|Note|Light)\b",
    re.M,
)
REQUIRED_MAPPINGS = (
    "`skandha` -> **Base**",
    "`āyatana` -> **Essence**",
    "`dhātu` -> **Principle**; then, by context only, **Realm**",
    "`bhūta` -> **Element**; `mahābhūta` -> **Great Element**",
    "`bhautika` -> **Element-dependent**",
    "*prajñā* as **Science of Principles**",
)


def all_studies():
    return sorted(ORGANON_DIR.glob("0*/VAK_*.md"))


def read(name):
    return (STUDY_DIR / name).read_text(encoding="utf-8")


def is_declared_logical_handle(text, match):
    headings = list(re.finditer(r"^## \d+\. (.+)$", text[:match.start()], re.M))
    if not headings or headings[-1].group(1) not in ("Interpretation", "Interpretive Note"):
        return False
    start = text.rfind("\n\n", 0, match.start()) + 2
    end = text.find("\n\n", match.end())
    paragraph = text[start:end if end != -1 else len(text)]
    return "logical handle" in paragraph and "Dharma Āyatana" in paragraph


class ScientificTerminologyTests(unittest.TestCase):
    def test_all_studies_use_scientific_vocabulary(self):
        failures = []
        for path in all_studies():
            text = path.read_text(encoding="utf-8")
            for label, pattern in LEGACY_TERMS:
                for match in pattern.finditer(text):
                    if label == "Essence Base" and is_declared_logical_handle(text, match):
                        continue
                    line = text.count("\n", 0, match.start()) + 1
                    failures.append(
                        f"{path.relative_to(ORGANON_DIR)}:{line}: "
                        f"{label} ({match.group(0)!r})"
                    )
        if failures:
            self.fail(f"{len(failures)} legacy terms:\n" + "\n".join(failures))

    def test_essence_base_requires_an_explicit_interpretive_handle(self):
        declaration = (
            "**Essence Base** is the project's logical handle for Dharma Āyatana."
        )
        for heading, paragraph, expected in (
            ("Interpretation", declaration, True),
            ("Interpretive Note", declaration, True),
            ("Translation", declaration, False),
            ("Interpretation", "Dharma Āyatana means Essence Base.", False),
            ("Interpretation", "Essence Base is a logical handle.", False),
            ("Interpretation", declaration + "\n\nAn Essence Base is a skandha.", False),
        ):
            text = f"## 9. {heading}\n\n{paragraph}"
            match = list(dict(LEGACY_TERMS)["Essence Base"].finditer(text))[-1]
            with self.subTest(text=text):
                self.assertEqual(is_declared_logical_handle(text, match), expected)

    def test_no_obsolete_organon_section_headings(self):
        """Interpretive Bhāṣya sections are headed "Interpretation"."""
        failures = []
        for path in all_studies():
            text = path.read_text(encoding="utf-8")
            for match in OBSOLETE_HEADING.finditer(text):
                failures.append(f"{path.relative_to(ORGANON_DIR)}: {match.group(0)}")
        if failures:
            self.fail(
                f"{len(failures)} obsolete headings (rename to Interpretation):\n"
                + "\n".join(failures[:20])
            )

    def test_vak_1_12_four_dhatus_are_principles(self):
        for name in ("VAK_1.12.md", "VAK_1.12_bhasya.md"):
            with self.subTest(study=name):
                text = read(name)
                self.assertIn("Earth Principle", text)
                self.assertNotRegex(text, r"principled (?:earth|water|fire|wind)")

    def test_vak_1_41_glosses_prajna_as_science_of_principles(self):
        self.assertTrue(
            any(
                "| *dhīḥ* |" in line and "*prajñā* (Science of Principles)" in line
                for line in read("VAK_1.41.md").splitlines()
            ),
            "VAK 1.41 must gloss *dhīḥ* as *prajñā* (Science of Principles)",
        )

    def test_vak_1_42_keeps_science_of_principles_and_dharma_scope(self):
        text = read("VAK_1.42_bhasya.md")
        self.assertIn("Science of Principles", text)
        self.assertNotIn("only Essences", text)

    def test_vak_1_43_and_1_44_render_visaya_as_condition(self):
        self.assertRegex(read("VAK_1.43.md"), r"\| a-prāpta-viṣayam \|[^\n]*Condition")
        self.assertRegex(read("VAK_1.44.md"), r"\| tulya-viṣaya-grahaṇam \|[^\n]*Condition")

    def test_vak_1_45_to_1_47_avoid_field_vocabulary(self):
        for verse in ("1.45", "1.46", "1.47"):
            for name in (f"VAK_{verse}.md", f"VAK_{verse}_bhasya.md"):
                with self.subTest(study=name):
                    self.assertNotRegex(
                        read(name),
                        r"\bfield\b|field-support|Principle Pipeline|Pure Principle",
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
