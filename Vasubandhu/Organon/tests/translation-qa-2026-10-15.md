# Translation QA: Organon chapters 1–4

The preferred reader-facing translation of the kārikā is the
**Bhāṣya-informed study translation** in its Organon kārikā study. The close
or literal rendering serves as a syntactic check. Neither translation
subsection should become commentary. Once reviewed, the Bhāṣya-informed
kārikā translation is intended for the paired Bhāṣya study. That transfer
is a later pass; the literal rendering is not transferred by default.

Run `python3 Vasubandhu/Organon/tests/audit_translation_boundaries.py` from
the repository root to reproduce the structural inventory below. This audit
does not compare English with Sanskrit or decide whether a sentence is a
faithful translation; that requires review one kārikā at a time.

| Chapter | Kārikā studies | Bhāṣya-informed with prose after quoted translation | Bhāṣya-informed without a quoted boundary | Other detected issues |
|---|---:|---:|---:|---|
| 1 Dhātu | 48 | 2 | 45 | 45 close renderings unquoted |
| 2 Indriya | 73 | 0 | 72 | 72 close renderings unquoted; 2.41 lacks section 5 |
| 3 Loka | 102 | 98 | 0 | 2 close renderings have prose after the quote |
| 4 Karma | 127 | 121 | 0 | 4 close renderings have prose after the quote |

An earlier QA pass compared the kārikā study's informed translation against
English already in the paired Bhāṣya file and called the differences “anchor
mismatches.” That was the wrong measure before the kārikā translations had
been settled and transferred. The alignment test now leaves that comparison
off by default. Chapter 2 verse 2.41 has no section 5 and therefore fails
the informed-translation presence check.

The unquoted count marks an *ambiguous boundary*, not automatically bad
English. A paragraph can be a translation without a block quote. The
chapter 3–4 prose-after-quote count identifies text that follows the
translation inside the same subsection. Those notes belong elsewhere.

Clear content failures still to review:

- [VAK 2.01](../02-indriya/VAK_2.01.md): the Bhāṣya-informed section lists
  and explains the faculties and their functions. It reads as a commentary
  digest rather than one continuous rendering of the verse.
- [VAK 3.01](../03-loka/VAK_3.01.md) and
  [VAK 4.01](../04-karma/VAK_4.01.md): a quoted translation is followed by
  an editorial note within the same translation subsection, obscuring the
  boundary of the translation itself.

The optional historical paired-wording comparison cannot certify that a
translation subsection contains translation alone. Before this QA pass the
test also recognized only one exact subsection heading, so 126 Karma studies
were reported as missing a translation. Semantic fidelity and the correct
amount of Bhāṣya expansion still require source review.

## Dhātu translation pass

The 21 Dhātu sections assessed as recoverable by trimming have now been
shortened in their **Bhāṣya-informed** subsections only: 1.04, 1.10, 1.13,
1.15, 1.21, 1.24–1.27, 1.30, 1.32–1.36, 1.38–1.41, 1.45, and 1.48. Their
literal renderings and paired Bhāṣya studies were not edited. The eight
sections previously assessed as needing a fresh translation—1.01, 1.07,
1.08, 1.42–1.44, 1.46, and 1.47—have now received new Bhāṣya-informed
kārikā translations. Their extended Bhāṣya arguments remain in the paired
studies; transferring the settled kārikā translations to those studies is a
later pass.

The two subsection headings in all 48 Dhātu kārikā studies are now fixed to
`Literal Translation` and `Bhāṣya-informed study translation`. The scoped
test enforces those exact names. The chapter 1 top-level heading audit also
passes after correcting the 1.16 section sequence and the 1.28 lexical
heading.

## Indriya first assessment

All 73 kārikā studies have a Bhāṣya-informed subsection, but 2.41 has no
standard section 5 and therefore needs structural repair. In a text scan,
63 informed subsections contain multiple paragraphs. By word count, 11 are
at most 80 words, 28 are 81–150, 22 are 151–250, and 12 exceed 250 words.
These are triage measures, not judgments of translation accuracy.

The recurring issue is Bhāṣya explanation inside the kārikā translation.
Clear examples are 2.01 (the four sensory-faculty functions explained at
length), 2.24 (ten mental-factor definitions and a further analogy), and
2.41 (a debate on same-class followed by prose on the non-reflective).
The shorter 2.48 still reaches into the next verse; 2.37 explicitly says
that its final sentences are commentary rather than the verse. Length alone
does not settle the case: 2.19 largely tracks the verse's two possession
counts while supplying the members named in the Bhāṣya.

Review each verse with its paired Sanskrit Bhāṣya. Preserve its claims and
order in a smooth translation; use the Bhāṣya to resolve ellipsis and names,
and keep examples, debates, and forward pointers in the commentary. The
Bhāṣya files remain for the later transfer pass.
