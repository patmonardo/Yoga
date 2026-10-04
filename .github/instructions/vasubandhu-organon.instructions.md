---
description: "Governing framework for all Vasubandhu/Abhidharmakosa Organon work: Skandha-Ayatana-Dhatu read as Being-Essence-Concept, not flat lists. Use when: translating, QA'ing, or extending any VAK/Kosa/Organon material under Vasubandhu/."
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
  Place Organon synthesis in a separate, explicitly marked section.
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

Preserve who is speaking. Attribute positions to the Vaibhāṣikas, Vasubandhu,
other teachers, or an unnamed opponent only when the text does so. In
extended Dharma Talks, do not flatten a sequence of objections and replies
into one unqualified “Kośa position.”

## Terminology

- `rūpa` -> **Form**, never **Matter**. Matter is opposed to Form in this
  Organon framework, not an equivalent rendering; translating Form as Matter
  reverses the project's conceptual path.
- `dhātu` -> **Domain**
- `bhūta` / `mahābhūta` -> **Element**
- `āyatana` -> **Essence** (the capacity/field determination; not the
  Concept)
- `indriya` -> **Faculty**, not “organ” for Faculty-status. Use “organ”
  only for an anatomical part explicitly meant by the Sanskrit.
- `skandha` -> **aggregate** in conventional translation; **Being** in the
  Organon reading.
- `citta` -> **consciousness** in conventional translation. Do not make it a
  hidden substance behind events; Universal Citta is an Organon determination.
