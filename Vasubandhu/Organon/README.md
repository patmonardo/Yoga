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
- The chapter 1 Grammar–Logic pilots (1.01–1.48) annotate the normalized
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
  Use `--start 27 --end 27 --strict` for the assignment function: every
  designation from another sūtra has an own-characteristic determined
  before assignment and fitting an established place. Attended scope
  strictly contains principal scope; non-percipient beings take ten
  Essences without Odor and Taste; Mind Essence assignment is not occurring
  Cognition; the sixty-two Principles are not enumerated.
  Use `--start 28 --end 28 --strict` for the worked demonstration: an
  opening named the Space Principle with a reported (*kila*) nature, Impure
  Cognition as the Cognition Principle, and birth-support over all six with
  the subject supplied by the prose. The six map four/one/one into the
  eighteen; unconditioned space is not this Space Principle, Pure is not
  unconditioned, and *cittasthaṃ* stays unresolved. This completes the
  1.24–1.28 classification engine: naming, closure, measure, assignment,
  and demonstration.
  Use `--start 29 --end 29 --strict` for the first application of the
  engine to the eighteen: three biconditional counts (one visible, ten
  resistant, eight only-indeterminate) checked extensionally on the finite
  valuation. The prose theory encodes both tetralemmas: obstruction and
  Condition-resistance cross-classify nineteen items (the Dharma Principle
  split into associated and non-associated portions), and support-resistance
  nests inside Condition-resistance. The verse formula is scoped to the
  eighteen; the Form Base is excluded as visible by the prose clause.
  Use `--start 30 --end 30 --strict` for the ethical and realm cuts: the
  ten others are threefold on stated grounds, all eighteen are connected
  with the Desire Realm, and fourteen with the Form Realm (a biconditional,
  so the nose and tongue Faculties stay). The prose theory makes
  Principle recursive — a Realm is a Principle of Principles (constituted
  by the eighteen it admits, not one of them), and a Base is no Principle:
  the Form Base gathers exactly
  the ten Form-bearing Principles and is none of them, and the Form Realm
  is not the Visible Form Principle though both are *rūpa-dhātu*.
  Use `--start 31 --end 31 --strict` for the Formless and the Impure–Pure
  cut: three Principles connected with the Formless, the fifteen dropped
  being exactly the ten Form-natured Principles and the five Cognitions
  taking them. Impure and Pure are predicated through instances: the three
  have both (Path for all three, the unconditioned for the Dharma Principle
  alone), the fifteen only Impure. The Dharma Principle is not the Dharma
  Essence; the Formless Realm is a Principle of Principles constituted by
  the three.
  Use `--start 32 --end 32 --strict` for vitarka and vicāra: restrictive
  *hi* (a `RESTR` feature) makes the five Cognition Principles exclusively
  "with both"; *tri-prakāra* gives the last three at least three kinds; the
  ten have only "without both". The prose relates kinds to portions and
  levels and finds the fourth kind (vicāra alone with vitarka) inside the
  Dharma Principle, so a level with both has four kinds.
  Use `--start 33 --end 33 --strict` for *avikalpaka*: the instrumental
  restricts the negation to examining and recollective vikalpa, so the five
  keep intrinsic vikalpa (vitarka). Examining is exactly unconcentrated
  mental prajñā; recollective is exactly mental smṛti. The five's own prajñā
  and smṛti are not mental and so not vikalpa.
  Use `--start 34 --end 34 --strict` for the two cuts: *sālambana*
  (Support, glossed as grasping a Condition) over the seven consciousness
  Principles and the associated half of the Dharma Principle; and
  Appropriation over instances, where `CNT` checks 7, 8 + 1 = 9, and 9.
  The cuts are disjoint: nothing that takes a Support is Appropriated.
  Use `--start 35 --end 35 --strict` for Element and Element-dependent:
  the class *rūpin* carries `CNT=10`, *śeṣāḥ … nava* takes ten less one,
  and *daśa* matches it. Great Elements are instances only of the Tangible;
  avijñapti is Element-dependent but not Accumulated; Buddhadeva's thesis
  is a rejected theory.
  Use `--start 36 --end 36 --strict` for the outer four: the verse settles
  *dahyate* (passive) and *tulayati* (active) and disputes *dagdhṛ*
  (agent) and *tulya* (gerundive, the weighed). Swapped `VA`/`VB`
  features force the dispute onto the converse voices.
  Use `--start 37 --end 37 --strict` for the modes of genesis: number
  agreement binds *vipākajaḥ* to *na śabdaḥ* across the line break, and
  each mode is predicated through instances. Maturation and continuity are
  tied to their Grounds (*hetu*); Sound's effort blocks maturation; the
  unconditioned instance of the Dharma Principle has no mode.
  Use `--start 38 --end 38 --strict` for the close of the causal
  sequence: counts for the four, the one, and the three; *ekaḥ* as
  uniqueness of the *dravya*-bearer (the unconditioned core); momentary as
  the first Pure moment without a continuity Ground; and a genitive-dual
  pair applied to separate and joint acquisition under *syāt*.
- 1.39 counts the inner by subtraction (*hitvā* takes a class whose remainder
  must match *dvādaśa*), and reads *sabhāga* / *tat-sabhāga* per instance:
  the negative relative clause *yaḥ na sva-karma-kṛt* carries POL=neg into
  the work predicate, and the Dharma Principle is the constant the rest
  exclude.
- 1.40 counts fifteen plus three under the masculine plural *heyāḥ*, then
  shifts to the neuter singular *dṛṣṭi-heyam*, whose three negated subjects
  must agree with it; abandonment by seeing is modelled per instance as
  afflicted, not Form, and born from the Mind Essence.
- 1.41 lets case carry quantity: the nominative *cakṣuḥ* quantifies over the
  whole Eye Principle, the partitive genitive *dharma-dhātoḥ* over a part,
  and the dual *pradeśau* closes view to those two; the ablative
  *a-tīraṇāt* grounds the exclusion of five-born discriminative
  comprehension.
- 1.42 binds active *paśyati* and passive *dṛśyate* to one ROOT, so the
  passive ground quantifies away the agent of the same relation; *tat* in
  *tat-āśritam* takes its REF from the subject, and *kila* carries
  EVID=reported for the Sautrāntika reserve.
- 1.43 makes *anyathā* a predicate operator (`\P x.-P(x)`) that returns the
  converse of *a-prāpta-viṣayam* for the triad, whose CNT must match the
  collective dvandva; reaching is modelled as arising without an interval,
  not touch, and the instrumental duals carry *api*'s inclusive reading.
- 1.44 makes *ca* the carrier of the past predicate (`\P y.P(y)` applied to
  *atītaḥ*), so the five derive a co-born and a past Basis while the last
  has only the past one; *sahajaḥ* takes the elided *āśrayaḥ* by agreement,
  *taiḥ* agrees in number with *pañcānām*, and the four alternatives keep
  Basis (*āśraya*) apart from the immediately preceding Condition.
- 1.45 shares NUM across its two sentences so that plural *taiḥ* takes the
  name from *cakṣuḥ-ādayaḥ*; *ataḥ* carries the Basis relation into the
  naming clause, and the second ablative makes the Basis unshared. The
  Bhāṣya's *āśrayī-bhavitum* / *ālambanī-bhavati* fixes Basis against Support.
- 1.46 reads each word as a role in a seeing situation and each comparative
  as a plane relation; *ca* lends *vijñānam* the predicate of *rūpam*, the
  pronoun *asya* must match *vijñānam*'s REF, and *sarvataḥ* is a relation
  operator asserting all three alternatives, applied through the dual
  *ubhe* to both members. Plane constants are `dh1`–`dh4`, since NLTK reads
  `d1` as a variable.
- 1.47 builds the Bhāṣya's general rule (*utsarga*) and exception
  (*apavāda*) into the parse: *kāya-vijñānam* is subtracted from the domain
  of *sarvam* and given its own predicate; *tathā* carries the 1.46 rule to
  *śrotram*, and *a-niyatam* asserts Mind on the body's plane, above, and
  below.
- 1.48 closes the chapter with three quantifiers: *dvi-vijñeyāḥ* asserts
  exactly two knowers (own Cognition and Mind-Cognition); *nityāḥ* is
  restricted to unconditioned dharmas; *dharma-ardham* is partitive (some
  of the Dharma Principle is Faculty, some is not), and *ca* joins the
  twelve internal (CNT=12) to *indriyam*, which stays neuter singular.
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
