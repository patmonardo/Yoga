# Organon QA

The structural audit and paired Kārikā/Bhāṣya alignment test accept a chapter
and verse range, so the same checks can be applied to different study volumes.

```sh
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
exact Karman template to every chapter 4 study:

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

The Karman check requires those top-level sections in that order, with those
numbers, and rejects every other top-level section. It does not inspect
subsections (`###` and deeper) or headings inside fenced code blocks. Chapter 4
selects the strict Karman profile automatically; `--profile generic` cannot
disable it in check mode. Legacy chapter 4 studies that do not match the
template are reported as nonconforming, with no per-verse exceptions. A
section body may be empty; the audit locks the section headings, not their
content.

Chapters 2, 3, and 5–8 remain on the generic profile pending separate damage
assessment. Without `--check`, the audit inventories exact top-level heading
patterns without enforcing them. Add repeated `--require-section` or
`--forbid-section` options for additional scoped checks.

The paired-alignment test defaults to exact translation parity. Chapter 4
uses prefix matching because its Bhāṣya anchors contain the paired translation
while the Kārikā translation may continue with editorial study notes; override
this with `--translation-match exact|prefix` when needed. The
scientific-terminology regression module remains specific to the reviewed
Dhātu studies and their controlled mappings.
