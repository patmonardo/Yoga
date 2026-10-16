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
python Vasubandhu/Organon/tests/test_karika_bhasya_alignment.py \
  --chapter 4 --start 1 --end 16
python -m unittest discover \
  -s Vasubandhu/Organon/tests -p 'test_*.py'
```

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

The paired-alignment test normally checks that the kārikā study has a
Bhāṣya-informed translation. It does not require that translation, or the
literal rendering, to be copied into the Bhāṣya study. Historical paired
wording can be inspected explicitly with `--translation-match exact|prefix`;
these optional comparisons do not define the editorial rule. For chapter 3,
the optional comparison uses the quoted translation blocks and ignores prose
following them. The scientific-terminology regression module remains specific
to the reviewed Dhātu studies and their controlled mappings.
