"""Focused regression checks for the YS source inventory and live audit."""

import unittest

from audit_ys import (
    BHASYA_HEADINGS,
    ROOT,
    SOURCE,
    SUTRA_HEADINGS,
    audit,
    headings,
    source_inventory,
)


class YSAuditTests(unittest.TestCase):
    def test_source_numbers_are_contiguous_in_four_chapters(self):
        inventory = source_inventory(SOURCE.read_text(encoding="utf-8"))
        self.assertEqual({chapter for chapter, _ in inventory}, {1, 2, 3, 4})
        for chapter in range(1, 5):
            numbers = sorted(verse for number, verse in inventory if number == chapter)
            self.assertEqual(numbers, list(range(1, numbers[-1] + 1)))

    def test_live_studies_match_source_and_paired_scaffolds(self):
        self.assertEqual(audit(), [])

    def test_variant_after_i17_does_not_enter_i18_anchor(self):
        inventory = source_inventory(SOURCE.read_text(encoding="utf-8"))
        self.assertEqual(
            inventory[1, 18],
            "विरामप्रत्ययाभ्यासपूर्वः संस्कारशेषोऽन्यः॥ १.१८॥",
        )

    def test_heading_reader_ignores_fenced_examples(self):
        sample = "## 1. Sanskrit (Devanāgarī)\n```md\n## Wrong\n```\n"
        self.assertEqual(headings(sample), SUTRA_HEADINGS[:1])
        self.assertEqual(len(BHASYA_HEADINGS), 4)

    def test_opening_translation_keeps_project_determination(self):
        chapter = ROOT / "01-prajna"
        for suffix in ("", "_bhasya"):
            i2 = (chapter / f"YS-I.02{suffix}.md").read_text(encoding="utf-8")
            i12 = (chapter / f"YS-I.12{suffix}.md").read_text(encoding="utf-8")
            self.assertIn("Yoga is the Science of Consciousness.", i2)
            self.assertIn("Their sublation is through practice and dispassion.", i12)
            self.assertNotIn("Yoga is the restraint", i2)


if __name__ == "__main__":
    unittest.main()
