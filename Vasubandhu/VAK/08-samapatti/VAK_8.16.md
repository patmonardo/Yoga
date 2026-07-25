# VAkK 8.16

## Sanskrit

क्लिष्टात् स्वं शुद्धकं क्लिष्टम् एवं चाधरशुद्धकम् ।
च्युतौ तु शुद्धकात् क्लिष्टं सर्वं क्लिष्टात् तु नोत्तरम् ॥ VAkK_8.16 ॥

## IAST

kliṣṭāt svaṃ śuddhakaṃ kliṣṭam evaṃ cādharaśuddhakam /
cyutau tu śuddhakāt kliṣṭaṃ sarvaṃ kliṣṭāt tu nottaram // VAkK_8.16 //

## Source Caution

The compounds are resolved according to the succession doctrine: `adhara-śuddhakam` is a pure attainment of a lower level, and `na uttaram` excludes a higher attainment after a defiled one.

## Padaccheda

- kliṣṭāt
- svam śuddhakam
- kliṣṭam
- evam ca
- adhara-śuddhakam
- cyutau tu
- śuddhakāt
- kliṣṭam sarvam
- kliṣṭāt tu
- na uttaram

## Grammar

- **kliṣṭāt / śuddhakāt** — ablatives, “after a defiled/pure attainment.”
- **svam** — “of its own level.”
- **adharaśuddhakam** — a pure attainment belonging to a lower ground.
- **cyutau** — locative, “at death” or “upon falling away.”
- **nottaram** — `na uttaram`, “nothing higher.”

## Literal Translation

After a defiled attainment arise the pure and the defiled of its own level, and likewise a lower pure attainment. At death, after a pure attainment, any defiled attainment may arise; but after a defiled attainment, nothing higher arises.

## Philosophical Translation

Defilement permits repetition on its own ground and descent toward a lower pure state, but it does not generate ascent. At death even a pure attainment may be followed by a defiled mode, showing that purity of state is not yet irreversible liberation.

## Technical Vocabulary

- **kliṣṭa** — defiled.
- **śuddhaka** — pure but worldly.
- **adhara-bhūmi** — lower ground.
- **cyuti** — falling away; death-transition.
- **uttara** — higher.

## Doctrinal Determination

The verse completes the immediate succession rules begun in 8.15. A defiled attainment can be followed by its own pure or defiled form, or by a pure attainment below it. It cannot directly produce a higher attainment. At death, however, worldly purity does not prevent the arising of defilement.

## Logical Determination

The transition system is directionally asymmetric:

```text
defiled
    → same-level pure
    → same-level defiled
    → lower pure
    ↛ higher

pure at death
    → defiled of any admissible level
```

Ascending determination requires a cause not contained in defilement itself.

## Organon Light

A state is known not only by what it contains, but by what it can generate. Defilement lacks the immanent power of ascent; worldly purity lacks final necessity. Liberation therefore requires more than occupying a superior state.

## OWL++ Seed

```text
Rule: DefiledAttainment mayTransitionTo SameLevelPureAttainment.
Rule: DefiledAttainment mayTransitionTo SameLevelDefiledAttainment.
Rule: DefiledAttainment mayTransitionTo LowerPureAttainment.
Constraint: DefiledAttainment mayNotTransitionDirectlyTo HigherAttainment.
```

## Commit History

- Initial Sanskrit-first analysis of VAkK 8.16.