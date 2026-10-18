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
- In interpretive prose, **Essence Base** may be explicitly declared as the
  project's logical handle for Dharma Āyatana. It does not replace **Dharma
  Essence** in translations or name another Skandha. Terminology checks
  distinguish that declared architectural usage from legacy translation.
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
  `tests/audit_nltk_blocks.py`; claim only what was run. A `SEM` feature in
  the grammar may derive the §8 formula by the parse (see 8.13). `Pred => {}`
  means an empty extension; NLTK itself reads it as a phantom `''` element,
  so the audit loader corrects this.
- The chapter 1 Grammar–Logic pilots (1.01–1.26) annotate the normalized
  IAST token stream beneath the Lexical Analysis table. It preserves verse
  order, opens sandhi, and marks Bhāṣya-resolved ellipses with `∅-` and
  `SUPPLIED=prose`. The annotation must match the grammar's `# tokens:`
  exactly; the Sanskrit witness remains unchanged.
- In that pilot, §4 derives a closed, truth-valued `SEM` through
  `FeatureChartParser` and lambda reduction. §8 reuses it in a FOL theory,
  declares `# EXPECT verse T`, and supplies a finite valuation. Bhāṣya
  elaboration and Organon interpretation remain identifiable; the parse is
  a declared logical projection, not a claim to encode every pragmatic or
  temporal distinction. Keep āśraya distinct from other conditioning
  relations; do not introduce Object for viṣaya or ālambana.
- Validate this stronger pilot contract with
  `python Vasubandhu/Organon/tests/audit_nltk_blocks.py --chapter 1 --start 1 --end 3 --strict`.
  Extend `--end` to `6` for the Pure/Impure division, space, and the two
  cessations. The accepted and rejected theories in 1.04–1.06 have explicit
  truth expectations; taking as ālambana is not conflated with persistence,
  and attainment of cessation is not production of an unconditioned Dharma.
  Extend `--end` to `7` for the conditioned five-Base collective and its
  four resumed determinations. Shared reference is not predicate identity;
  the attributed *vastu*–cause gloss is not a hidden semantic equation.
  Extend `--end` to `8` for the Impure restriction, Bases of appropriation,
  conflict, and five further names. The Pure Path remains a Base member
  without becoming a member of a Base of appropriation.
  Extend `--end` to `9` for Form's eleven-kind roster and the five sensory
  Faculties as clarities supporting corresponding Cognitions. Here the
  parse derives the Faculty predication only; the roster is separate FOL,
  tested for distinctness, membership, and exclusion of supported Cognition.
  Extend `--end` to `10` for the five meanings' counts. Twofold analysis
  and twentyfold enumeration of visible Form stay distinct; numerical
  labels do not perform arithmetic. Tests count the supplied finite
  rosters without replacing the verse's counts by attributed alternatives.
  Extend `--end` to `11` for *avijñapti*: relative/correlative naming,
  ethical alternatives, Elemental dependence, and consciousness-state scope.
  Acquisition prevents ethical continuity alone from becoming a sufficient
  definition; the Bhāṣya's non-disclosure and origins remain separate rules.
  Extend `--end` to `12` for the four Great Elements as named Principles.
  The parse derives the roster and ordered own-characters; the compressed
  function-series is expanded in a separate prose theory. Tests distinguish
  functions from characters and Wind's impulsion from derived lightness.
  Extend `--end` to `13` for worldly designation and wind's two uses.
  Separate prose countermodels reject shadow-like cessation and the claim
  that originating Element support must persist for the continuity to persist.
  Extend `--end` to `14` for the same ten members in the Essence and Principle
  classifications and the distinct definitions of Feeling and Reflection.
  Prose checks distinguish three tones from six contact-groups and exclude
  *avijñapti* from these ten without excluding it from every classification.
  Extend `--end` to `15` for the conditioned Formations remainder and the
  shared Dharma classifications. The seven constituents are categories,
  not seven individual Dharmas; non-volitional formations are included,
  *avijñapti* stays Form, and the unconditioned remains without a Base.
  Use `--start 16 --end 19 --strict` for the Principle Processor pilot.
  It tests the Cognition classifications, immediately-past Mind office,
  joint inclusion, and paired-site classification. Its Form and Dharma
  dependencies now have their own executable studies in 1.04–1.15;
  they are not derived again by the Principle Processor pilot.
  Use `--start 20 --end 20 --strict` for the three ordered meanings and
  the threefold teaching. Prose checks preserve separate confusion,
  Faculty, and inclination axes and the unconditioned counterexample
  to defining every Principle as a homogeneous cause.
  Use `--start 21 --end 21 --strict` for Feeling and Reflection as separate
  Bases that remain mental factors. Tests distinguish principal causes,
  mediations, and roots of dispute, with the order demonstration deferred.
  Use `--start 22 --end 22 --strict` for the unconditioned's exclusion
  from Bases and four accounts of their order. Prose checks retain five
  Base kinds, the meal roles, and Realm/level correspondences without
  erasing the promise-of-three or food/vessel discrepancies.
  Use `--start 23 --end 23 --strict` for the order of the six: present
  and Element-dependent Conditions as precedence reasons, distance and
  quickness for the remainder, and sites as an alternative. Unlocalized
  Mind is not unconditioned; the three damaged clauses stay unrepaired.
  Use `--start 24 --end 24 --strict` for the naming layer of the
  classification machine: exactly one Essence is called Form (primacy)
  and exactly one Dharma (gathering of the many and the highest), with
  distinction shared. Resistance is shared by the ten; showability singles
  out Form; every Essence is dharma by own-nature, but only one is named so.
  Use `--start 25 --end 25 --strict` for the closure rule: scriptural
  designations resolve into established classifications. A relative–
  correlative parse assigns inclusion respectively per reported account
  (speech → Form Base, name → Formations Base); neither account is chosen
  and no Dharma-collection becomes a further Base.
  Use `--start 26 --end 26 --strict` for three attributed measures of a
  Dharma-collection: treatise, exposition of each topic (holders supplied
  by the prose), and counteragent to a disposition. *Tu* contrasts without
  refuting; each exposition is one collection, and counteragents pair with
  dispositions one-to-one without the pairings being listed. Avoid `e` as
  a bound variable in FOL: NLTK reserves it for event types.
  Strict mode checks token annotation, dependency vocabulary coverage,
  semantic closure, reuse in the theory, symbol declarations, and expected
  truth values. Dependency coverage is not dependency parsing: the block
  records head–dependent token types, including repeated *ca*, not
  occurrence-indexed or labelled arcs. Earlier chapters retain their
  existing audit mode until individually reviewed.
- Run the pilot's positive and negative tests with
  `python -m unittest discover -s Vasubandhu/Organon/tests -p 'test_dhatu_nltk_pilot.py'`.
  These change agreement features and finite valuations to test rejection
  of wrong readings. Satisfaction in a finite model is not proof of the
  translation or a philosophical theorem.
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
