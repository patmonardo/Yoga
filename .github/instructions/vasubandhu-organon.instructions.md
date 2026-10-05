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
- Preserve the Bhāṣya's actual scope and argument. Most units clarify a
  kārikā briefly; some become extended dialectical “Dharma Talks.” For those,
  retain the full sequence of questions, positions, objections, replies, and
  unresolved issues. “Dharma Talk” is our editorial description, not a
  genre-name attributed to Vasubandhu.
- For especially dense sequences, keep Organon applications concise and
  source-bound: use existing technical concepts as established, without
  expanding them into new cross-tradition mappings or ontological claims
  unless asked. Prioritize careful paired study of each kārikā and Bhāṣya.
- Establish the conventional translation from the Sanskrit and Bhāṣya.
  In Bhāṣya studies, place philosophical interpretation in a separate
  section titled **Interpretation**, not **Organon Reading**.
- Use **Lexical Analysis** as the section heading for word division,
  morphology, and lexical meanings; do not prefix it with *Padaccheda*.
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
  one dharma. Keep this synthesis separate from conventional translation;
  see `Vasubandhu/VAK/06-marga/VAK_6.04.md` and
  `Vasubandhu/VAK/05-anusaya/VAK_5.29.md`.
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

## Conventional translation vs. Organon reading

Keep these separate in every Bhāṣya study. The conventional translation
answers to the Sanskrit and commentary. The Organon reading—including
Being–Essence–Concept, Citta/Buddha Mind, the Dharma–Bhava Chakra coupling,
and Sāṃkhya–Yoga correspondences—belongs in its own clearly marked section.
Do not let reconstruction leak into the close translation or make the
Organon reading sound like literal Bhāṣya doctrine.

For the Organon account of *vijñāna*, use Kantian Transcendental Philosophy
as the project-level frame for Principle Science; do not identify
*vijñāna* with *citta* or attribute the synthesis historically to
Vasubandhu. Keep advanced philosophical interpretation in the paired
Bhāṣya's **Interpretation** section. A kārikā study may retain a concise
Interpretive Note and state the defined `<Base, Essence, Principle>`
projections without expanding the philosophical synthesis.

Preserve who is speaking. Attribute positions to the Vaibhāṣikas, Vasubandhu,
other teachers, or an unnamed opponent only when the text does so. In
extended Dharma Talks, do not flatten a sequence of objections and replies
into one unqualified “Kośa position.”

## Current project terminology

The controlled Organon mapping is **Skandha = Base, Āyatana = Essence,
Dhātu = Principle**; *rūpa* is **Form**, so *rūpa-skandha* is **Form Base**.
Render the complete census as **five Bases, twelve Essences, and eighteen
Principles**. This formula is mandatory in Organon prose, translations,
summaries, and tables: do not render it as “five aggregates, twelve bases,
and eighteen elements.” Preserve the Sanskrit terms in lexical analysis,
while using the controlled Base–Essence–Principle terminology for the
systematic count.
In the eighteenfold cognitive matrix, the eighteen Dhātus are precisely
eighteen cognitive Principles; do not reduce them to a flat list of elements
or domains.
Keep Dharma untranslated in these compound labels: *dharmaskandha* is
Dharma Base, *dharmāyatana* is Dharma Essence, and *dharmadhātu* is Dharma
Principle. In the Organon, the Defined Concept of each Dharma is
`<Base, Essence, Principle>`; the three labels name distinct projections of
that one Dharma, not separate Dharmas or redundant names. “Dharma Essence”
means the Essence projection of a Dharma, not an Essence nested inside an
Essence. Do not conflate *dharmāyatana* with *dharmaskandha*; retain their
distinct classifications while understanding both within the complete
Defined Concept. In conventional translation, follow the source's local use
of the Sanskrit compounds rather than imposing this Organon formulation.

At the Āyatana level, Essence is the **Entry** into an Essential Relation of
an Impure Dharma; this relation comprises all products of Reflective Mind.
**Mind-Essence** is Reflective Science at this level. Keep this determination
distinct from Dhātu / Determinate Science. This is a project-level
determination, not a lexical claim about *āyatana*.

The **Nāma-skandha view** groups the four non-Rūpa Skandhas as the
project-level dyad **Jñāna-skandha : Vijñāna-skandha**. **Jñāna-skandha**
is ordinary knowledge—the existing Skandhas Vedanā, Saṃjñā, and Saṃskāra;
Vijñāna-skandha remains its special Principle member. These are project
views, not source-defined compounds or additional Skandhas. Do not confuse
Jñāna-skandha with the source's teaching-body use of *dharmaskandha*. A
top-level Dharma View may wrap Dharma-āyatana and Dharma-dhātu as one
meta-system, while preserving them as distinct Essence and Principle slots
in the core matrix.

Reflectively, **Mind-Essence** is the Seer as Reflector, and **Dharma-Essence**
is the Seen. Classify *artha* under the Seen; treat *viṣaya* as a specific
moment of the Seen. This is an Organon-level relation, not a lexical
definition. In the sensory schema, preserve the distinction between a
cognitive Condition and an achieved Object.

Older studies and models still contain previous labels, including Being,
Domain, Concept, and Essence Base. During the Indriyanirdeśa pass, use the
current mapping in new work but do not perform a broad migration. Complete
the chapter first; then inventory the terminology and update the affected
materials systematically.

## Conventional vocabulary

- `rūpa` -> **Form**, never **Matter**. Matter is opposed to Form in this
  Organon framework, not an equivalent rendering; translating Form as Matter
  reverses the project's conceptual path.
- `dhātu` -> **element** in conventional translation; **Principle** in the
  Organon reading
- `vijñāna` -> **Principle** in the current Indriyanirdeśa project
  terminology; do not render it as “Cognition” or “consciousness.” This
  does not change the fixed compound **Mind-Cognition Principle**
  (*manovijñānadhātu*).
- `citta` -> **consciousness** in conventional translation; keep it distinct
  from Principle (*vijñāna*) and Mind (*manas*)
- `vijñānaskandha` -> **principle-base**; `viṣaya` -> **condition** in the
  1.16 study. Preserve the source terms and the local Bhāṣya gloss.
- `viṣaya` -> **Condition** in the current 1.16 project translation; retain
  “object” for *ālambana* where that is the source term.
- `manas` -> the **Produced Cognitive Instrument** in the project architecture;
  equipped with Mind Essence (*mana-āyatana*) and Mind Principle
  (*manodhātu*). Its production/ownership relation remains open for
  project discussion; this is not a conventional lexical gloss.
- `mana-āyatana` -> **Mind Essence**; `manodhātu` -> **Mind Principle** in the
  Organon reading and project-level **Ordinary Logic**. These are distinct
  determinations within Manas's cognitive equipment, not synonyms for Manas.
- `manovijñānadhātu` -> **Mind-Cognition Principle**, distinct from
  *manodhātu* / **Mind Principle**; project-level **Transcendental Logic**,
  determined as Abstract Reason (Syllogistic Reasoning). Preserve the
  conventional reading separately.
- `dharmadhātu` -> **Dharma Principle**, not Essence Principle.
- `bhūta` / `mahābhūta` -> **Element**
- `āyatana` -> **Essence**; in the Organon reading, the Entry into an
  Essential Relation of an Impure Dharma, comprising all products of
  Reflective Mind; Mind-Essence is Reflective Science at this level. Keep
  distinct from Dhātu / Determinate Science and from the Concept.
- `indriya` -> **Faculty**, always. Never translate *indriya* as “organ.”
  Reserve “organ” for a separately named anatomical part, not as a gloss
  for *indriya*.
- `skandha` -> **aggregate** in conventional translation; **Base** in the
  Organon reading.
- `citta` -> **consciousness** in conventional translation. Do not make it a
  hidden substance behind events; Universal Citta is an Organon determination.
