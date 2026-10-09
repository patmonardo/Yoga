# YS study checks

Run from the repository root:

```sh
python3 Patanjali/YS/tests/audit_ys.py
python3 -m unittest discover -s Patanjali/YS/tests -p 'test_*.py'
```

The audit reads `Patanjali/Sources/Yoga.txt` and checks the numbered sūtra inventory against all four chapter folders. Every sūtra must have a study file and a paired `_bhasya.md` file. Empty pairs are reserved for later study; a drafted pair must have matching numbered titles and exact Devanāgarī source quotations in both files. A one-sided draft fails.

Every drafted **sūtra study** uses these exact level-two headings, in order:

1. `Sanskrit (Devanāgarī)`
2. `Sanskrit (IAST)`
3. `Lexical Analysis`
4. `Grammar`
5. `Translation`
6. `Logical Determination`
7. `Interpretive Note`

Every drafted **our Bhāṣya** file uses:

1. `Sūtra Anchor`
2. `Commentary`
3. `Two-Path Determination`
4. `Source and Voice Boundaries`
5. `Review Status`

Prefix each with `## 1.`, `## 2.`, and so on. These are the required top-level headings; verse-specific `###` subheadings may be added inside them. The Bhāṣya here is our composition, so the VAK sections for a received continuous Sanskrit commentary and its translation do not apply.

The `_bhasya.md` files contain **our commentary**. The checker verifies source identity and document structure; it cannot certify a philosophical claim, translation, Sanskrit analysis, or attribution. Those require verse-by-verse review against the source and the developing Yoga–Kośa argument. Add focused checks here only when a textual or conceptual decision has been established clearly enough to test without freezing a provisional interpretation.
