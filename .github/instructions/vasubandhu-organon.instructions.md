---
description: "Governing framework for all Vasubandhu/Abhidharmakosa Organon work: Skandha-Ayatana-Dhatu read as Base-Essence-Principle, not flat lists. Use when: translating, QA'ing, or extending any VAK/Kosa/Organon material under Vasubandhu/."
applyTo: "Vasubandhu/**"
---

# Vasubandhu Organon Framework

Before doing any translation, QA, or philosophical extension work under this
folder, consult these load-bearing project documents:

- `Vasubandhu/Essays/dharma-skandha.md` — the governing thesis: Dharma
  comprehends itself as `<Skandha, Ayatana, Dhatu>`; it also states the
  central Dharma-Chakra and Bhava-Chakra architecture.
- `Vasubandhu/Essays/dhatu-classification-engine.rs` — a research sketch of
  the Dhātu classification and its cross-mappings, not a complete model of
  the Dharma Chakra.
- `Vasubandhu/Essays/dharma-wheel-index-model.rs` — a research data model
  for representing aspects of the wheel in an index. The model is not the
  Dharma Chakra itself or a final ontology.

## Indriyanirdeśa working method

- For the current Indriyanirdeśa pass, upgrade one verse at a time. Treat
  each kārikā and its Bhāṣya as a paired unit; upgrade both together.
  Every verse contributes to the movement.
- Read VAK 1.24–1.28 as the specification and demonstration of the Dhātu
  classification machine: 1.24 distinguishes the named Essences; 1.25
  locates further scriptural designations within established
  classifications; 1.26 distinguishes measures of a teaching-collection;
  1.27 states characteristic-based assignment; 1.28 demonstrates a
  cross-mapping of a six-Principle teaching. From 1.29 onward, follow the
  chapter's examination of how the classification works and is applied.
  This is an editorial map, not a genre or title attributed to the source.
  Do not label 1.24–1.28 as only a Form System.
- Preserve the Bhāṣya's actual scope and argument. Most units clarify a
  kārikā briefly; some become extended dialectical “Dharma Talks.” For those,
  retain the full sequence of questions, positions, objections, replies, and
  unresolved issues. “Dharma Talk” is our editorial description, not a
  genre-name attributed to Vasubandhu.
- For especially dense sequences, keep Organon applications concise and
  source-bound: use existing technical concepts as established, without
  expanding them into new cross-tradition mappings or ontological claims
  unless asked. Prioritize careful paired study of each kārikā and Bhāṣya.
- Establish the Scientific English rendering from the Sanskrit and Bhāṣya,
  using the controlled Base–Essence–Principle vocabulary below. In Bhāṣya
  studies, place the Techne interpretation in a separate section titled
  **Interpretation**. Do not fall back to conventional Buddhist English
  terminology when it conflicts with the Scientific mapping.
- Use exactly one **Lexical Analysis** section per kārikā study. Do not add
  a separate *Padaccheda* section or additional lexical-analysis sections.
- Follow VAK 1.17 as the fixed format: one concise word-division block and
  one table with this exact header:
  `Pada | Morphology | Force in this passage`. Use that same header for the
  Lexical Analysis table in every study. Do not add separate **Sentence
  words**, **External sandhi**, or compound-analysis subsections, additional
  lexical tables, or extended lexical commentary. Add only a brief
  clarification when a form requires it. Do not upgrade this format unless
  explicitly requested.
- Use the technical vocabulary below consistently, without letting it erase
  grammatical, textual, or school-level distinctions.

## Central architecture

- The Dharma Chakra is the central idea of the Kośa, not a side note,
  optional metaphor, or merely an eventual index. **The Kośa is the Dharma
  Chakra**: its determinations articulate an Empirical Relation.
- In each turning, the Principle rooted in the sublated Principle is held
  invariant at the hub. Differentiated moments occupy the spokes; their
  relations close the movement at the rim. Do not turn the hub into another
  changing empirical moment.
- The Dharma Chakra spans *saṃvṛti* and *paramārtha* as two determinations of
  the same reality, not two worlds or substances. **Absolute Insight** is the
  project's name for second-order apprehension of the whole wheel: it
  preserves first-order access without reproducing contamination while
  understanding what analysis discloses. Do not make it a third truth,
  equate *paramārtha* with one universal Absolute, or collapse the hub into
  one dharma. Keep this synthesis in the separate Techne interpretation,
  not in source-text transcription or Lexical Analysis;
  see `Vasubandhu/VAK/06-marga/VAK_6.04.md` and
  `Vasubandhu/VAK/05-anusaya/VAK_5.29.md`.
- The Absolute Base spans and combines Rūpa-skandha and Dharma-skandha. This
  unity is Absolute Dharma itself, discriminating all Dharmas through Form
  and Law. Preserve both determinations within the unity; do not flatten
  them into one inventory or treat the Absolute Base as a third Base.
- The Loka–Karma volume is the **Bhava Chakra**. Keep it distinct from the
  Dharma Chakra while reading their mating.
- The core dyads are `Vijñapti:Avijñapti` for Dhātu and
  `Prāpti:Aprāpti` for Indriya. These are distinct relations coupled
  **Dyad → Dyad** as LogoGenesis (learning), not four interchangeable terms
  or a simple one-way causal sequence. *Avijñapti* is the bridge: it is
  classified in both the Form Base and Dharma Base, not duplicated as two
  Dharmas.
- In the project's Organon architecture, the ten Samyama-bhūmis describe
  Path-related operation of mental factors; Buddha Dharma is the 11th Bhūmi.
  This is a project-level synthesis, not a literal translation or a claim
  that a specific Bhāṣya passage enumerates an 11th level.
- Skandha, Ayatana, and Dhatu are **not** three parallel inventories of the
  same content counted differently (5 / 12 / 18). They are one movement
  held at increasing grades of self-relation. Reading them as flat lists to
  memorize is the failure mode this project exists to correct.
- Ayatana (capacity/field dyad) is Essence at its own ceiling —
  Substance-Accident-Reciprocity, Aristotelian *hypokeimenon*/*dynamis* on
  both poles — **not yet** the Concept. Do not call Ayatana "the Concept."
- Only the reciprocating closure (the six vijnana-dhatus; `Reciprocates`
  in the Rust sketch) is Concept-level: Substance grasped as Subject,
  *ousia* as *energeia* rather than substrate.
- Dhātu is rendered **Principle** in the project's threefold terminology;
  Concept names the closure of the movement, not a translation of Dhātu.
- The Dhatu-Indriya chapter is a **practical instance of Citta**, not a
  theory about mind in general. Citta is the Universal; the
  Skandha/Ayatana/Dhatu schema is the Particular (the theory, what the
  Rust file types); Buddha Mind is the Singular — the actual, total,
  executing instance.
- VAK 1.01's `sarvathā-sarva-hata-andhakara` (darkness destroyed in every
  mode, over every object) vs. the sravaka/pratyekabuddha's remaining
  non-afflicted ignorance is the text's own statement of this Universal/
  Particular/Singular distinction: same trait, exhaustive closure vs.
  permanently outstanding closure. Treat this as textually anchored, not
  as an imported metaphor.

## Scientific translation and Techne interpretation

The project uses Scientific terminology, not conventional Buddhist English
terminology. In every English translation, summary, table, schema, and
interpretation, apply the controlled Base–Essence–Principle vocabulary
below. Preserve the Sanskrit source in its source-text block and retain
Sanskrit forms in Lexical Analysis; do not use conventional English glosses
as the default layer beneath a separate Techne reading. In particular,
never translate *dhātu* as “element,” *āyatana* as “sense-base,” or
*skandha* as “aggregate.”

Keep source-text transcription, Scientific English rendering, and Techne
interpretation structurally distinct. The English rendering itself must use
Scientific terminology. The Kant-informed Techne interpretation states the
Kośa's explicit systematic content; do not describe it as merely external
to the source or hedge it as something the Kośa does not state.

The Kośa explicitly presents Vijñāna as Discriminative Cognition joining and
governing Perception and Conception. Their unity is Inconceivable as a
homogeneous operation; its Idea is disclosed in the Vijñāna-skandha.
Vijñāna governs Manas and guides the reading of Dharma-skandha. Form-skandha
and Dharma-skandha both include the same *avijñapti* in distinct
classifications, and Vijñāna bears a *prati* relation to *avijñapti*.
Preserve these relations without collapsing their terms. Keep *vijñāna*
distinct from *citta* and *manas*. State this governing synthesis directly
in the paired Bhāṣya's **Interpretation** and concisely in kārikā notes.

For the incoming Techne of the inner instrument, use *vijñāna* as **Knowing**,
*jñāna* as **Conceiving**, *prajñā* as **Science of Principles**, and
*dhātu* as the **Principle instrument**. Render *vijñāna* as **Cognition**,
more precisely **Discriminative Cognition**, in the Scientific English
rendering; within the inner-instrument Techne, understand it as **Higher
Cognition of Scientific Knowing**. Keep the local source glosses and
grammatical force.
Keep Thinking, Conceiving, and Knowing distinct: Conceiving is **Ordinary
Knowing** (*vijñapti*), while Knowing is **Transcendental Knowing**
(*prati-vijñapti*). This is a Techne relation, not a universal lexical
substitution for every occurrence of these forms.
Keep this inner-instrument use of *jñāna* distinct from the existing
**Jñāna-skandha** project grouping of ordinary knowledge. Apply these
meanings verse by verse only where the passage supports them; do not insert
absent terms into a study.

Preserve who is speaking. Attribute positions to the Vaibhāṣikas, Vasubandhu,
other teachers, or an unnamed opponent only when the text does so. In
extended Dharma Talks, do not flatten a sequence of objections and replies
into one unqualified “Kośa position.”

## Current project terminology

The controlled Scientific mapping is **Skandha = Base, Āyatana = Essence,
Dhātu = Principle**; *rūpa* is **Form**, so *rūpa-skandha* is **Form Base**.
Render the complete census as **five Bases, twelve Essences, and eighteen
Principles**. This formula is mandatory in Scientific prose, translations,
summaries, and tables: never render it as “five aggregates, twelve bases,
and eighteen elements.” Preserve the Sanskrit terms in Lexical Analysis,
while using the controlled Base–Essence–Principle terminology throughout
the English scientific account.
In Scientific prose and interpretive tables, use the English Base, Essence, and
Principle terminology and translate their compounds (for example, **Cognition
Base**, **Mind Essence**, and **Mind-Cognition Principle**). Retain their
Sanskrit forms in source quotations and dedicated Lexical Analysis only.
In the eighteenfold cognitive matrix, the eighteen Dhātus are precisely
eighteen cognitive Principles; do not reduce them to a flat list of elements
or domains.
Keep Dharma untranslated in these compound labels: *dharmaskandha* is
Dharma Base, *dharmāyatana* is Dharma Essence, and *dharmadhātu* is Dharma
Principle. In the Techne, the Defined Concept of each Dharma is
`<Base, Essence, Principle>`; the three labels name distinct projections of
that one Dharma, not separate Dharmas or redundant names. “Dharma Essence”
means the Essence projection of a Dharma, not an Essence nested inside an
Essence. Do not conflate *dharmāyatana* with *dharmaskandha*; retain their
distinct classifications while understanding both within the complete
Defined Concept. In all English prose, use the source-local Scientific
compound specified by the mapping rather than inserting an unapproved
traditional gloss.

At the Āyatana level, Essence is the **Entry** into an Essential Relation of
an Impure Dharma; this relation comprises all products of Reflective Mind.
**Mind-Essence** is Reflective Science at this level. Keep this determination
distinct from Dhātu / Determinate Science. This is a project-level
determination, not a lexical claim about *āyatana*.

The **Nāma-skandha view** groups the four non-Rūpa Skandhas as the
project-level dyad **Jñāna-skandha : Vijñāna-skandha**. **Jñāna-skandha**
is ordinary knowledge—the existing Skandhas Vedanā, Saṃjñā, and Saṃskāra;
Vijñāna-skandha remains its special Cognition member. These are project
views, not source-defined compounds or additional Skandhas. Do not confuse
Jñāna-skandha with the source's teaching-body use of *dharmaskandha*. A
top-level Dharma View may wrap Dharma-āyatana and Dharma-dhātu as one
meta-system, while preserving them as distinct Essence and Principle slots
in the core matrix.

Reflectively, **Mind-Essence** is the Seer as Reflector, and **Dharma-Essence**
is the Seen. Classify *artha* under the Seen; treat *viṣaya* as a specific
moment of the Seen. This is a Techne-level relation, not a lexical
definition. In the sensory schema, preserve the distinction between a
cognitive Condition and an achieved Object.

Older studies and models still contain previous labels, including Being,
Domain, Concept, and Essence Base. Do not reproduce those labels in new or
upgraded English material. During the Indriyanirdeśa pass, migrate each
paired study as it is reviewed rather than making an unrelated repository-
wide migration. Complete the chapter first; then inventory other affected
materials systematically.

## Scientific vocabulary

Use these mappings in all English study text, including translations,
interpretations, tables, OWL/RDF seeds, and headings. Do not introduce a
conventional Buddhist English alternative in a “close” or “literal”
translation.

- `rūpa` -> **Form**, never **Matter**. Matter is opposed to Form in this
  Scientific framework, not an equivalent rendering; translating Form as Matter
  reverses the project's conceptual path.
- `dhātu` -> **Principle**
- `bhūta` / `mahābhūta` -> **Great Principle**; plural **Great Principles**
- `bhautika` -> **Principle-dependent**
- `vijñāna` -> **Cognition**, more precisely **Discriminative Cognition**,
  with **Discrimination** as its defining function; in the inner-instrument
  Techne, **Knowing** means Higher Cognition of Scientific Knowing. Keep it
  distinct from *citta* / consciousness and *manas* / Mind; do not substitute
  **Principle**, which is the rendering of *dhātu*. This does not change the
  fixed compound **Mind-Cognition Principle** (*manovijñānadhātu*).
- `citta` -> **consciousness**; keep it distinct
  from Cognition (*vijñāna*) and Mind (*manas*)
- `vijñānaskandha` -> **Cognition Base**; `viṣaya` -> **condition** in the
  1.16 study. Preserve the source terms and the local Bhāṣya gloss.
- `viṣaya` -> **Condition** in the current 1.16 project translation; retain
  “object” for *ālambana* where that is the source term.
- `manas` -> **Mind**; the **Produced Cognitive Instrument** in the project
  architecture, equipped with Mind Essence (*mana-āyatana*) and Mind Principle
  (*manodhātu*). Its production/ownership relation remains open for
  project discussion.
- `mana-āyatana` -> **Mind Essence**; `manodhātu` -> **Mind Principle** and project-level **Ordinary Logic**. These are distinct
  determinations within Manas's cognitive equipment, not synonyms for Manas.
- `manovijñānadhātu` -> **Mind-Cognition Principle**, distinct from
  *manodhātu* / **Mind Principle**; project-level **Transcendental Logic**,
  determined as Abstract Reason (Syllogistic Reasoning).
- `dharmadhātu` -> **Dharma Principle**, not Essence Principle.
- `āyatana` -> **Essence**; the Entry into an
  Essential Relation of an Impure Dharma, comprising all products of
  Reflective Mind; Mind-Essence is Reflective Science at this level. Keep
  distinct from Dhātu / Determinate Science and from the Concept.
- `indriya` -> **Faculty**, always. Never translate *indriya* as “organ.”
  Reserve “organ” for a separately named anatomical part, not as a gloss
  for *indriya*.
- `skandha` -> **Base**
- `citta` -> **consciousness**. Keep it distinct from Cognition (*vijñāna*)
  and Mind (*manas*); do not make it a hidden substance behind events.
  Universal Citta is a Techne determination.

## Required Scientific-terminology regression check

The specific recurring failure this instruction prevents is the re-entry of
conventional Buddhist English labels into Scientific translations, especially
rendering *dhātu* as “element” after the project has established **Principle**.
This is a blocking terminology error, not a stylistic preference.

- After changing any paired study in `Vasubandhu/Organon/01-dhatu/`, run:
  `python -m unittest discover -s Vasubandhu/Organon/tests -p 'test_scientific_terminology.py'`
- The regression test checks both the kārikā study and Bhāṣya for each reviewed
  pair beginning at VAK 1.29. It rejects legacy translations such as “element,”
  “sense-base,” “contact-base,” “Essence Base,” and “Essence Principle,” plus
  obsolete Essence Principle and Mental-Cognition identifiers in OWL seeds.
  It also verifies that the required Base–Essence–Principle mappings are declared.
- Extend the test's verse range as each next pair is upgraded. Do not weaken,
  skip, or whitelist a failing verse to make the test pass; correct the English
  study text while preserving source Sanskrit, argument, and attribution.
