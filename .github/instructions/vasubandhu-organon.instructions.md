---
description: "Governing framework for all Vasubandhu/Abhidharmakosa Organon work: Skandha-Ayatana-Dhatu read as Being-Essence-Concept, not flat lists. Use when: translating, QA'ing, or extending any VAK/Kosa/Organon material under Vasubandhu/."
applyTo: "Vasubandhu/**"
---

# Vasubandhu Organon Framework

Before doing any translation, QA, or philosophical extension work under this
folder, treat these two files as load-bearing, not optional background:

- `Vasubandhu/Essays/dharma-skandha.md` — the governing thesis: Dharma
  comprehends itself as `<Skandha, Ayatana, Dhatu>`, the Hegelian movement
  Being -> Essence -> Concept.
- `Vasubandhu/Essays/dhatu-classification-engine.rs` — the same thesis typed
  as a non-compiling Rust sketch. Read the comments as the executable form
  of the claims dharma-skandha.md makes in prose.

## Non-negotiable framing

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

Keep these separate in every Bhasya file: the conventional translation
must answer to the Sanskrit and the commentary alone; the Organon/
philosophical reading (Being-Essence-Concept, Citta/Buddha Mind,
Samkhya-Yoga correspondences) belongs in its own clearly marked section.
Do not let the speculative reconstruction leak into the close translation,
and do not water down the speculative reading to make it sound like
literal translation.

## Terminology (until superseded by a dedicated vocabulary pass)

- `dhatu` -> **Domain**
- `bhuta` / `mahabhuta` -> **Element**
- `ayatana` -> **Sphere** (provisional; capacity/field dyad, not
  "sense-base" — "sense-base" belongs to the indriya chapter's own
  vocabulary, not ayatana in general)
- `indriya` -> **Faculty**; never translate it as "organ." Use "organ"
  only when the Sanskrit refers to an anatomical part, not for Faculty-status.
- `skandha` -> **aggregate** (conventional translation); **Being** (Organon
  reading)
