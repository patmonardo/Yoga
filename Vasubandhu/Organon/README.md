# The Organon Kośa

This directory contains the official Organon study of Vasubandhu's
*Abhidharmakośabhāṣya* (VAK), called here the **Kośa**.

The numbered directory and file sequence is part of the exposition. It
preserves the systematic movement of the Kośa from Dhātu through Jñāna and
Samāpatti.

## Pre-Techne

[Volume I technical expressions](../Essays/technical-expressions-vol-i.md)
governs Dhātu–Indriya; [Volume II technical expressions](../Essays/technical-expressions-vol-ii.md)
governs Loka–Karma. Each sets source-bound translation controls beside its
Organon determinations. The [combined Pre-Techne](../Essays/technical-expressions-vol-i-ii.md)
retains the extended architectural argument behind the two references.

[Volume III technical expressions](../Essays/technical-expressions-vol-iii.md)
begins the controlled vocabulary for Anuśaya–Mārga and Jñāna–Samāpatti.
Its chapter-level determinations are applied and revised one kārikā at a
time.

[Dharma Principle Dossier](../Essays/dharmadhatu-dossier.md) gathers the chapter's
Dharmadhātu witnesses in a source-first study sequence and keeps its Pure
Māyā inquiry explicitly separate from the Kośa's stated classifications.

## Editorial Principles

- Work proceeds one kārikā at a time.
- The kārikā and `_bhasya` files in this Organon directory are the immediate
  research corpus; the underlying source texts remain textual witnesses.
- Canonical filenames use the project form `VAK_1.01.md` and
  `VAK_1.01_bhasya.md`.
- GRETIL-style labels such as `VAkK_1.1` are not displayed in the official
  study.
- Textual witness, philological analysis, translation, Abhidharma doctrine,
  and Organon interpretation are kept visibly distinct.
- The literal translation is distinguished from the readable study
  translation.
- In section 5, both the close (or literal) rendering and the
  **Bhāṣya-informed study translation** are translations of the kārikā.
  Each must be readable continuously as English for the verse. The close
  rendering follows the verse's wording and syntax, marking supplied words.
  The Bhāṣya-informed rendering is the preferred reading translation: it resolves
  ellipsis and technical referents with the paired Bhāṣya while preserving
  the verse's order, claims, and argumentative voice. It must not turn into
  a summary of what the Bhāṣya says or a list of its explanations.
- Put the translation text alone under each translation label, preferably
  as one block quotation. Explain lexical choices, supplied subjects,
  textual uncertainty, and the Bhāṣya's reasoning in Grammar, Technical
  Vocabulary, or the paired Bhāṣya study. Do not append commentary within
  a translation subsection. Keep Organon reconstruction in the interpretive
  sections.
- Draft and settle the Bhāṣya-informed kārikā translation in the kārikā
  study, one verse at a time, using the corresponding Sanskrit Bhāṣya to
  determine compressed wording. Copy the settled translation exactly into
  the paired Bhāṣya's Kārikā Anchor during that verse's review. The literal
  rendering stays a syntactic check in the kārikā study. The Bhāṣya's
  continuous conventional translation translates the commentary passage
  in its own right.
- Every kārikā study uses the same ten numbered stage headings, in the same
  order: Sanskrit (Devanāgarī), Sanskrit (IAST), Lexical
  Analysis, Grammar, Translation, Philosophical Translation,
  Technical Vocabulary, Logical Determination, Interpretive Note, and OWL++
  Seed.
- Lexical Analysis begins with one table of `Pada`, `Morphology`, and
  `Force in this passage`. Keep useful sandhi or textual notes after the
  table; a separate prefatory Padaccheda block is unnecessary.
- In chapter 8, Grammar is an NLTK feature grammar (`nltk-fcfg`) plus a
  dependency grammar (`nltk-dep`). Logical Determination is NLTK FOL/lambda
  (`nltk-sem`, `nltk-fol` by `# THEORY`, `nltk-valuation`). Check them with
  `tests/audit_nltk_blocks.py`; claim only what was run.
- Only `Literal Translation` and `Bhāṣya-informed study translation` are
  subsection headings. Verse-specific divisions inside the other stages are
  bold editorial signposts, not additional report sections.
- Speculative interpretation does not silently enter the primary
  translation.
- Metaphysical subject-negation is not used as an organizing doctrine or a
  recurring interpretive disclaimer. Where a source invokes it, register it
  briefly as an anti-adhyāsa warning, accept its local caution, and proceed to
  the positive technical determination of the passage.
- OWL++ seeds are retained as a formal knowledge layer and reviewed only
  after the textual and conceptual analysis.
- Uncertainty, source problems, and bhāṣya-dependent decisions are marked
  explicitly.
- Each study remains provisional until it has been read and critically
  reviewed.

## Bhāṣya Method

Number every top-level Bhāṣya section consecutively. The opening and closing
sections are:

1. `Kārikā Anchor`
2. `Continuous Sanskrit` (or `Continuous Sanskrit Witness` when needed)
3. `Continuous Conventional Translation`
4. A section tracing the Bhāṣya's argument, such as `Movement of the Commentary`
5. Further source-specific analysis, translation decisions, and Organon study,
   each with the next section number
6. `Review Status`, with the next and final section number

Thus `## 1. Kārikā Anchor` begins every reviewed Bhāṣya study, and the
numbers continue without gaps to `Review Status`. The middle is determined
by the passage; the list above does not impose a fixed total of six sections.

Under the one anchor heading, place the Sanskrit kārikā first, then one
English block quote: the exact **Bhāṣya-informed study translation** from
section 5 of the paired kārikā study. Do not add a `Literal Translation` or
`Bhāṣya-informed study translation` subheading inside the anchor. Put any
explanation of the translation after the quote, or in the Bhāṣya analysis.
The anchor gives the reader the verse and its settled reading; the continuous
conventional translation gives the Bhāṣya prose.

Check the chapter's technical expressions during each verse review. Establish
the Sanskrit term's local force, the English used in translation, and any
Organon determination in their respective layers. Add or revise a controlled
expression when the passage requires it; do not stamp a chapter-wide gloss
onto each occurrence.

## Chapter Sequence

1. Dhātu
2. Indriya
3. Loka
4. Karma
5. Anuśaya
6. Mārga
7. Jñāna
8. Samāpatti

The official study begins with `01-dhatu/VAK_1.01.md` and advances in strict
textual sequence.
