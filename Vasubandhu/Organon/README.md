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

In the Organon synthesis, Sāṃkhya is a **Rational Overlord** for the
Kośa inquiry: its ordered account of Manas, Buddhi, Ahaṃkāra, and the
Faculties governs systematic comparison and tests the placement of the
Kośa's determinations. The Kośa Sanskrit and Bhāṣya still determine
what each local passage says; the governing comparison belongs to the
Organon layer and is stated there explicitly.

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
### Dhātu notebook

Generate an editable Jupyter notebook containing all 48 Dhātu kārikās:

```sh
python Vasubandhu/Organon/tests/export_dhatu_notebook.py
```

The exporter strictly validates every study before writing
[notebooks/dhatu-nltk.ipynb](notebooks/dhatu-nltk.ipynb). It extracts the
Sanskrit IAST, Lexical Analysis, translations, Technical Vocabulary, and all
five NLTK blocks without changing the studies. Each study has editable block
strings followed by an executable parse/model check. The notebook uses the
existing audit helpers, so run it from inside this repository with a Jupyter
Python 3 kernel containing NLTK. No NLTK corpus downloads are needed.

Run setup, then any study's two code cells, or choose **Run All**.
`studies[48]`, for example, exposes the parse tree, derived `sem`, `theories`,
`valuation`, `model`, dependency grammar, and theory `results`. The final
countermodel cell copies 1.48's valuation and adds a third knower of Sound,
making the verse false without changing the original. Checks are finite-model
evaluations, not theorem proofs; dependency checking is vocabulary coverage,
not dependency parsing.

The Markdown studies remain authoritative. Notebook edits do not update them.
The exporter refuses to overwrite an existing notebook; use `--output PATH`
for a separate snapshot or `--force` to deliberately replace one. Save your
experiments separately before regenerating. Generated notebooks have no saved
execution outputs.

### Dhātu Grammar–Logic contract

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

### Indriya Grammar–Logic and translation QA

Apply the Dhātu pilot contract to one Indriya kārikā at a time. Section 3
records normalized Sanskrit tokens; section 4 parses them once with an
NLTK feature grammar and derives a closed, truth-valued root SEM;
section 8 reuses that expression in FOL and tests source-supported
Bhāṣya claims and rejected readings in a finite valuation. Check the
feature chart's stated spans and test that count, case, and scope
features actually constrain the parse. Dependency blocks record token
coverage, not a second semantic derivation.

Grammar and logic are part of translation review. For each verse,
compare the derived predications with both verse translations and the
paired Sanskrit Bhāṣya. Correct the translation and its exact Bhāṣya
anchor together when the parse or source exposes a mismatch. Review
the local technical expressions at the same time, keeping source
wording, Bhāṣya specification, and Organon interpretation distinct.
Finite-model satisfaction checks internal behavior; it does not alone
establish textual fidelity or infer a causal relation that the passage
does not state. Run the scoped strict audit:

    python Vasubandhu/Organon/tests/audit_nltk_blocks.py --chapter 2 --start 1 --end 56 --strict

The 2.07 extension resolves the bodily-feeling ellipsis from the Bhāṣya
and scopes agreeable mental Pleasure-Faculty to the third dhyāna.
Its rejected theories test dropping that qualification and confusing
mental with bodily feeling. The commentary's absence argument is kept
separate from the verse-derived classification rules.

The 2.08 extension resolves the agreeable mental feeling resumed from
2.07, specifies the Bhāṣya's range of “elsewhere,” and keeps bodily and
mental neutral feeling under one Faculty. Non-difference is scoped to
remaining neutral; “for the most part” is recorded without becoming a
universal causal rule.

The 2.09 extension separates the nine types' three Path-designations
from outflow-status. Its partition is three exclusively without
outflows, ten exclusively with outflows, and nine admitting either
status; the painful pair is a dual, not a locative. The paired Bhāṣya
retains the full dispute over the five beginning with faith.

The 2.10 extension distinguishes being maturation from producing it,
resolves distress as the resumed subject, and preserves the prose's
concentration-projected life exception. The two partitions are
1 + 12 + 9 and 1 + 10 + 11. The extended lifespan discussion remains
a reported argument, not a practice validated by the finite model.

The 2.11 extension separates the opening completion of 2.10's ten from
the ethical classification. Its four groups contain 8 + 1 + 5 + 8
Faculty-types. Wholesome distress and threefold neutral feeling remain
explicit; ethical indeterminacy is not neutral feeling.

The 2.12 extension checks cumulative realm exclusions and the 19–15–8
ranges. The pleasant dual excludes both pleasure and gladness.
Possible realm-connection is distinct from instance-occurrence and
the bearer's circumstances; the stainless triad is unconnected.

The 2.13 extension checks the 4 + 1 + 9 + 5 + 3 abandonment partition
and the five's outflow-qualified instances. Pain belongs to the nine,
not the threefold group; the five's abandonable class is specifically
cultivation-abandonable. Gerundive status is not completed abandonment.

The 2.14 extension checks initial acquisition as maturation: 2 in
non-spontaneous Desire-realm birth, 6/7/8 in its spontaneous cases,
6 in the Form realm, and 1 in the Formless realm. Presence at
relinking is not equivalent to inclusion in that count.

The 2.15 extension preserves its uncertain opening and checks terminal
realm-counts separately from 2.16's gradual-death and wholesome-final-
consciousness qualifications. The sensory five differ from the five
beginning with faith; cessation is not initial maturation in reverse.

The 2.16 extension retains the death completion and checks fruit
attainment by route and temporal scope. A nine-count can span successive
Path-stages; the eleven answer in 2.17 concerns one person's repeated
attainments, not simultaneous feelings. Equal counts need not have
equal Faculty composition.

The 2.17 extension separates the carried eleven-person attainment
report from necessary possession. Any one of neutral feeling, life,
and Mind entails all three, not exactly three or continuous occurrence.
The damaged realization-Faculty exclusions remain provisional rather
than becoming formal axioms.

The 2.18 extension checks necessary possession closures of four,
five, and seven, with eight supplied from 2.19's opening. Equal counts
can have different companions; faith's eight does not include the
pain-seven. Possession of third-level pleasure is not attainment of
the third dhyāna or simultaneous manifestation with gladness.

The 2.19 extension checks two eleven-member necessary possession sets
with a shared ten, and the prospective Faculty's thirteen. It does not
constrain the whole thirteen to one uninterrupted Path-moment;
omission from a necessary list is not universal non-possession.

The 2.20 extension checks the two minimum eights, whose intersection
is neutral feeling, life, and Mind. Likewise carries the count, not
severed roots. Wholesome has the local faith-group reference; the
finite model is not a proof over every possible possession configuration.

The 2.21 extension distinguishes the complete both-sex nineteen from
the attached trainee's nineteen. Tests check the twenty-two-Faculty
census, exclusion of all three versus one sex and two stainless
Faculties, and both remaining realization alternatives. Completeness
does not mean all twenty-two; a maximum count does not rank realization.

The 2.22 extension changes relation from possession to necessary
co-arising. It checks soundless Desire-Realm 8/9/10, sound's 9/10/11,
and removal of odor and taste for the Form-Realm 6/7/8. Another
Faculty adds to body rather than replacing it. The full Sanskrit
discussion preserves predominance, seed, and counting-unit objections.

The 2.23 extension enters the mental-factor classification. Reciprocal
accompaniment is not every factor with every consciousness. Marks
accompany all arising conditioned dharmas; acquisition has the narrower
sentient designation and does not replace marks. Five counts classes,
not factors per episode.

The 2.24 extension requires all ten great-ground kinds together in
each consciousness-moment, not ten alternatives or a stream-wide
distribution. It tests each member's necessity, allows further factors,
and keeps feeling's three modes alternative. Reportive kila and the
damaged reflection-gloss remain distinct from the modeled assertion.

The 2.25 extension expands the root-pair into non-greed and non-hatred
and checks ten wholesome kinds alongside the universal ten. Non-delusion
is not counted again, twenty is not an exclusive total, and the narrower
scope is preserved. The attention/equanimity exchange remains a recorded
objection and deferral, not a reconciliation supplied by the model.

The 2.26 extension separates the six affliction kinds, the quoted
ten-recitation's five separate factors plus five afflicted modes,
and the unwholesome pair. Only in afflicted consciousness restricts
range, not total inventory. The distraction dissent and the
sluggishness/agitation co-presence versus predominance remain explicit.

The 2.27 extension treats the compound seven-plus-three list as ten
class-members, not a required bundle. Prose restrictions qualify the
associated ignorance without denying other accompanying dharmas.
The countermodels do not establish mutual-exclusion rules; definitions
remain deferred and the unfixed examples remain open-ended.

The 2.28 extension checks 10 + 10 + 2 within the necessary twenty-two,
with regret conditionally making twenty-three in wholesome Desire-Realm
consciousness. Regret alone outside that scope does not entail this count.
The naming alternatives and the done/omitted ethical table remain
distinct; later additions are not ruled out by the local inventory.

The 2.29 extension checks the unwholesome Desire-Realm twenty as
10 + 6 + 2 + 2. A view qualifies already-counted discriminative
comprehension, whereas one of four afflictions, a secondary beginning
with anger, or regret adds one. Alternatives are not cumulative;
isolated ignorance does not remove the established accompaniments.

The 2.30 extension checks obscured eighteen and unobscured twelve,
then torpor's conditional +1 across the stated cases. Compatibility
is not occurrence. Thirteen through torpor differs in membership
from thirteen through the outer-region teachers' indeterminate regret;
that alternative remains attributed, not merged into the base account.

The 2.31 extension carries exclusions across distinct levels rather
than identifying the intermediate with the first dhyāna. The three
first-level anger-group exceptions remain distinct from the two
further exclusions. Initial and sustained examination drop at separate
boundaries; intoxication is not silently added to the further drop.
The Brahmā episode retains its local evidential role and title uncertainty.

The 2.32 extension resolves the final dual as person-directed affection
and respect, not unrestricted faith and moral shame. Two separate
fourfold comparisons test nonidentical ranges; the Formless restriction
does not remove the wholesome factors themselves. The restored full
Sanskrit excerpt preserves the damaged positive reversal and the
attributed alternatives rather than claiming a settled reconstruction.

The 2.33 extension pairs initial/sustained examination respectively
with coarseness/subtlety, without inferring co-presence from the dual.
The three positions remain indexed: balancing, speech-formation,
and separation with its level/moment reply. Intoxication takes over
consciousness through attachment to one's own qualities; conceit
compares with another. The full Sanskrit continuation is retained,
with the butter repair and speech quotation marked as uncertain.

The 2.34 extension preserves the contextual one-meaning naming claim
without making the three roles interchangeable everywhere. The study
translation includes Basis, Cognitive Condition, and manner as well
as fivefold association. Tests remove each shared relation and check
distinct tokens with one instance per represented kind, not one factor
total. The variegation account retains the source's Principles.

The 2.35 extension opens formations dissociated from consciousness.
Tests preserve both duals, plural marks, and the separately identified
next-verse continuation. Entry labels are not a complete count of
distinct reals. The Sanskrit's conflicting double negative remains
visible; the contextual English and model do not claim to repair it.

The 2.36 extension separates the prior list's closure, acquisition's
two senses, and the pair's scope. Tests distinguish applicability
from actual possession: an unpossessed own-continuum dharma remains
eligible, whereas space, another continuum, and the non-sentient
are outside the pair's range. The full Sanskrit dispute is restored;
the critical seed account and the Vaibhāṣika distinct-real account
remain attributed alternatives, not model-settled ontology.

The 2.37 extension checks nine general temporal combinations against
three respectively matched ethical classes and three same-Realm
matches. The fourfold range for uncontaminated dharmas is the union
of the two cessation rows and the path-truth row, not four options
for each. Tests preserve the different three-member cessation sets,
exclude space, and distinguish uncontaminated from unconditioned.
The temporal rule remains general, with exceptions opening in 2.38.

The 2.38 extension checks the three status and two abandonment
classes through their actual case relations, not unrestricted options
for every subtype. Abandonable does not mean already abandoned.
Ordinary unobscured-indeterminate acquisition is co-arisen only;
the two indeterminate superknowledges and creation-consciousness
allow prior, co-arisen, and subsequent acquisition. The craft and
habituated deportment extension remains separately attributed.

The 2.39 extension distinguishes co-arisen-only acquisition of obscured
manifest Form from the broader Desire-Realm Form range, which excludes
prior acquisition. Non-acquisition is uniformly unobscured-indeterminate;
its past/future temporal matrix has six combinations. The damaged
present-time gloss is a separately named provisional theory, not part
of the verse translation or parse semantics. Tests check that separation
and prevent the broader Form rule from erasing the narrower restriction.

The 2.40 extension checks twelve non-acquisition Realm combinations,
qualified absence against the Buddha lineage counterexample, and both
general relinquishment grounds. The full debate through the proliferation
critique is restored, including the explicitly named Sautrāntika
alternative. Mutual possession answers the linear regress objection;
the subsequent six/eighteen growth critique remains distinct. Level
transition is not confused with attainment of the noble path.

The 2.41 extension preserves both extended Dharma presentations.
Tests check the four death/rebirth and same-class-change alternatives,
distinguish the non-reflective maturation-result from its causal
attainment, and retain the Great Fruit subset and reflective birth/death
boundaries. The full same-class debate and post-verse account through
Desire-Realm rebirth and later-experienced karma are restored. These
dense arguments require later detailed study, not compression into a
single settled ontology.

The 2.42 extension restricts “likewise” to cessation and separates the
wholesome attainment from its indeterminate, next-rebirth maturation.
Tests distinguish present-only acquisition, later past possession,
and absence of future cultivation. Fourth-dhyāna location does not
automatically acquire the attainment. The full prose is restored,
including reportive necessary regaining/rebirth and the restraint
analogy; “one time” is not read as once only.

The 2.43 extension separates two maturation timings and possible
non-maturation from ethical indeterminacy. The full cessation-attainment
prose and inherited cross-verse Buddha-acquisition dispute are restored.
Tests keep the application rule apart from the Buddha exception,
index prior-production alternatives by account, and check the
reported 16 + 2 × 9 = 34 without treating it as a settled historical
proof. The damaged non-emergence clause remains marked.

The 2.44 extension corrects the singular awakening-acquisition subject:
cessation attainment, not both attainments. Four shared Basis options
remain distinct from attainment-level and human first production.
The full resumption and entity/designation debates are restored,
including the school-dependent loss inference, beginner/mastery
distinction, reciprocal-seed proposal, Vasumitra/Ghoṣaka exchange,
and the closing rejection of designation. Damaged witness predicates
and the problematic realm reading remain marked for specialty study.

The 2.45 extension restores the life debate through its actual close
and the four-marks discussion up to the secondary-mark transition.
The Cognition compound is corrected from the running witness.
Tests conjoin all four marks and distinguish the four exhaustion
cases from the later own/other-intention classification. The
projected-duration and distinct-entity accounts remain separate;
damaged protected-case names and quoted groups remain unresolved.
The three-versus-four scriptural explanations are not merged.

The 2.46 extension checks the nine-member scheme by exact target
sets: four primaries operating on eight others each and four
secondaries operating on their corresponding primary alone.
The thirty-six relations do not count thirty-six entities.
The causal restriction is necessary, not a sufficiency claim.
The extended witness through 80.11 preserves the Sautrāntika
stream/moment critique, temporal activity objections, genitive
argument, unconditioned reply, and Vaibhāṣika doctrinal close.

The 2.47 extension restores the sound/name debate and maps the
three collections respectively. Tests check six main Realm options,
sentient/outflow/ethical classifications, signifier possession,
and the final “likewise” continuing into 2.48. The other teachers'
Formless extension stays attributed; the transfer to same-class
does not include the Desire/Form restriction. Production, revelation,
succession, and co-arising objections remain distinct steps.

The 2.48 extension completes that selective transfer: same-class
spans all three Realms and also admits maturation. Tests check
the exact nine result-sort options across six verse headings:
same-class, acquisition, and marks admit two sorts; the two
attainments and non-acquisition admit homogeneous outflow only.
The restored closing prose recalls the non-reflective result and
life, explains sentient classification by possession-language,
and gives the marks both sentient and non-sentient cases.
The discussion of dissociated formations closes, not the chapter;
the following causes-and-conditions question belongs to the transition
into 2.49, not to this unit's continuous translation.

The 2.49 pass parses the six named cause-types as one closed, truth-valued
classification. Its separate Bhāṣya theories test the conditioning cause's
non-obstruction toward what actually arises and the productive efficacy of
principal examples. Countermodels reject a seventh kind, self-causation,
universal productive agency, merely possible arising treated as actual,
and collapsing the six causes into the later four conditions. The verse
names the six; the Bhāṣya begins defining the first. The 2.50 unit carries
that definition into the next verse.

The 2.50 pass keeps the carried conditioning-cause definition separate
from the new reciprocal co-arisen cause. Its verse `SEM` tests mutual result
for the four Great Elements, consciousness and its follower, and mark and
marked. The Bhāṣya's secondary-mark qualification is tested separately
as one-way causality. Countermodels reject mere simultaneity, one-way
mutual result, unrestricted co-arising among conditioned dharmas, and
self-conditioning. The paired Bhāṣya witness now includes its final
secondary-mark passage; textual defects still await collation.

The 2.51 pass parses the follower groups, two restraints, two genitive
mark relations, and the open instrumental respects. The Bhāṣya expands
those respects to ten and distinguishes consciousness as cause for 58
dharmas from 54 dharmas as causes for consciousness; the count of 14 is
refused. The model tests the wider extent of co-arising and rejects
mere simultaneity as sufficient for co-arisen causality. The paired
Bhāṣya translation was clarified; its Sanskrit witness remains partial
and uncollated.

The 2.52 pass models the ordinary homogeneous cause through similarity,
own class and level, and priority, then the Path's cross-level equal/superior
case. Its finite model rejects similarity alone, a future homogeneous cause,
and loss of Path priority. The Sanskrit witness at [087|11] says “cause of the
inferior,” contrary to the verse and [087|23]; the conflict is retained for
collation rather than silently emended. The paired Sanskrit excerpt remains
partial.

The 2.53 pass carries the equal/superior antecedent into worldly qualities
produced by application and models associated cause through identical support.
The paired Bhāṣya now has its own executable Grammar and Logic example:
its [088|20] support proposition parses once, and finite countermodels test
the different-continuum objection and the one-way link to co-arisen cause.
This is a selected-proposition pilot, not yet a full parse of the prose unit.

Run the Bhāṣya pilot with

    python Vasubandhu/Organon/tests/audit_bhasya_nltk_blocks.py --study Vasubandhu/Organon/02-indriya/VAK_2.53_bhasya.md

The 2.54 pass distinguishes the pervasive and maturation causes in the
verse, then gives the paired Bhāṣya its own selected-proposition Grammar
and Logic pass. It checks the cross-class explanation, the exclusions of
indeterminate and uncontaminated causes, and the delayed-continuum account
without conflating the reported Vaibhāṣika position with the author's reply.
Run the Bhāṣya pilot with

    python Vasubandhu/Organon/tests/audit_bhasya_nltk_blocks.py --study Vasubandhu/Organon/02-indriya/VAK_2.54_bhasya.md

The 2.55 pass resolves the dual *te* as cause and fruit and corrects the
study translation and exact Bhāṣya anchor together. The kārikā grammar
separates temporal classes, fruit membership, and the unconditioned's lack
of cause and fruit. The paired Bhāṣya pilot parses [091|04] and tests the
Path's production of acquisition against its bringing one to disconnection;
entity and absence readings remain attributed. Run it with

    python Vasubandhu/Organon/tests/audit_bhasya_nltk_blocks.py --study Vasubandhu/Organon/02-indriya/VAK_2.55_bhasya.md

The 2.56 pass parses the six principal cause–fruit assignments and tests
their referents. The paired Bhāṣya pilot parses [095|05–06], where efficacy-
fruit extends beyond the principal pair except for maturation cause in the
main reply; a distant-crop alternative remains explicitly attributed. Run

    python Vasubandhu/Organon/tests/audit_bhasya_nltk_blocks.py --study Vasubandhu/Organon/02-indriya/VAK_2.56_bhasya.md

Continue the paired verse-by-verse QA and Grammar–Logic pass first.
A dedicated later Bhāṣya pass will improve the study sections after
the continuous translation, including their organization and explanatory
quality; broader structural repairs remain specialty-pass work.

Run the opening pilot's wrong-count, scope, ordered-attainment,
membership-extent, and parallel-course countertests with

    python -m unittest discover -s Vasubandhu/Organon/tests -p 'test_indriya_nltk_pilot.py'

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
