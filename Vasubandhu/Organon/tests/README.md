# Organon QA

The structural audit and paired Kārikā/Bhāṣya alignment test accept a chapter
and verse range, so the same checks can be applied to different study volumes.
For Dhātu, the paired test also enforces the exact two Translation subsection
names and table-first Lexical Analysis layout stated in the Organon README.
For the translation-boundary inventory across chapters 1–4, run
`python3 Vasubandhu/Organon/tests/audit_translation_boundaries.py` from the
repository root; see [the QA record](translation-qa-2026-10-15.md). This
inventory flags editorial symptoms and does not judge translation fidelity.

```sh
python Vasubandhu/Organon/tests/audit_karika_sections.py \
  --chapter 3 --check
python Vasubandhu/Organon/tests/audit_karika_sections.py \
  --chapter 4 --check
python Vasubandhu/Organon/tests/audit_karika_sections.py \
  --chapter 4 --start 42 --end 66 --check
python Vasubandhu/Organon/tests/audit_bhasya_sections.py \
  --chapter 5 --start 1 --end 69 --check
python Vasubandhu/Organon/tests/test_karika_bhasya_alignment.py \
  --chapter 4 --start 1 --end 16
python -m unittest discover \
  -s Vasubandhu/Organon/tests -p 'test_*.py'
```

## NLTK block audit

Chapter 8 (Samāpatti) writes Grammar and Logical Determination as NLTK
objects in fenced blocks. The heading audit ignores fenced code, so
`audit_nltk_blocks.py` validates them (it requires NLTK):

```sh
python Vasubandhu/Organon/tests/audit_nltk_blocks.py \
  --chapter 8 --start 1 --end 43
```

- Section 4: exactly one `nltk-fcfg` block (with a `# tokens:` line that
  parses exactly once) and one `nltk-dep` block.
- Section 8: `nltk-sem`, `nltk-fol` and `nltk-valuation` blocks. Every formula
  parses, every predicate and constant is declared in the valuation (NLTK
  raises `Undefined` otherwise), and each `# THEORY` is reported T or F in the
  valuation. F is legitimate for a disputed theory; the report is
  informational and only load, declaration or parse failures fail the run.

Chapters 1–7 have not yet been converted and report failures.

The heading audit applies strict Dhātu Pattern 3 rules to chapter 1 and one
exact ten-section template to every Loka and Karman kārikā study:

1. Sanskrit (Devanāgarī)
2. Sanskrit (IAST)
3. Lexical Analysis
4. Grammar
5. Translation
6. Philosophical Translation
7. Technical Vocabulary
8. Logical Determination
9. Interpretive Note
10. OWL++ Seed

The Loka and Karman checks require those top-level sections in that order,
with those numbers, and reject every other top-level section. They do not
inspect subsections (`###` and deeper) or headings inside fenced code blocks.
Chapters 3 and 4 select their strict profiles automatically; `--profile
generic` cannot disable either in check mode. A section body may be empty; the
audit locks the section headings, not their content.

Chapters 2 and 5–8 remain on the generic profile pending separate damage
assessment. Without `--check`, the audit inventories exact top-level heading
patterns without enforcing them. Add repeated `--require-section` or
`--forbid-section` options for additional scoped checks.

The Bhāṣya Method in the Organon README numbers every top-level section
consecutively, beginning with `## 1. Kārikā Anchor` and ending with a numbered
`Review Status`. It calls for the reviewed kārikā's
Bhāṣya-informed study translation to appear exactly once in the paired
Bhāṣya's Kārikā Anchor, with no translation subheading there. The literal
rendering remains in the kārikā study. The paired-alignment test's default
mode checks for the informed translation; an exact comparison can be requested
with `--translation-match exact` for pairs updated to the current method.
Historical pairs may still have older anchor layouts. The scientific-terminology
regression module remains specific to the reviewed Dhātu studies and their
controlled mappings.

`audit_bhasya_sections.py` inventories top-level Bhāṣya patterns by default.
With `--check`, it requires consecutive section numbers, the standard first
three sections, a numbered final `Review Status`, and one Sanskrit quote plus
one English quote directly under the anchor. Use a verse range to audit only
the pairs already brought up to the current Method; an unreviewed pair such
as 5.02 should fail.
