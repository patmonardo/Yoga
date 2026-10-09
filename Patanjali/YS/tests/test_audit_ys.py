"""Focused regression checks for the YS source inventory and live audit."""

import unittest

from audit_ys import (
    BHASYA_HEADINGS,
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

    def test_heading_reader_ignores_fenced_examples(self):
        sample = "## 1. Sanskrit (Devanāgarī)\n```md\n## Wrong\n```\n"
        self.assertEqual(headings(sample), SUTRA_HEADINGS[:1])
        self.assertEqual(len(BHASYA_HEADINGS), 5)


if __name__ == "__main__":
    unittest.main()
