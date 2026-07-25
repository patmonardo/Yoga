# VAkK 8.15

## Sanskrit

तृतीयाद्यावदूर्ध्वाधोऽनास्रवानन्तरं शुभम् ।
उत्पद्यते तथा शुद्धात् क्लिष्टं चापि स्वभूमिकम् ॥ VAkK_8.15 ॥

## IAST

tṛtīyādyāvad ūrdhvādho 'nāsravānantaraṃ śubham /
utpadyate tathā śuddhāt kliṣṭaṃ cāpi svabhūmikam // VAkK_8.15 //

## Source Caution

The source file reads `kliṭaṃ`; this is normalized here to `kliṣṭaṃ`, which is required by the sense and by the standard technical opposition between pure and defiled attainment.

## Padaccheda

- tṛtīya-ādi-āvat
- ūrdhva-adhaḥ
- anāsrava-anantaram
- śubham
- utpadyate
- tathā
- śuddhāt
- kliṣṭam
- ca
- api
- sva-bhūmikam

## Grammar

- **tṛtīyādyāvat** — “as far as the third and following,” indicating the relevant range of attainments.
- **ūrdhvādhaḥ** — adverbial compound, “upward and downward.”
- **anāsravānantaram** — accusative/adverbial relation, “immediately after an uncontaminated [attainment].”
- **śubham** — nominative singular neuter, “a wholesome [attainment/state].”
- **utpadyate** — 3rd person singular middle, “arises.”
- **śuddhāt** — ablative singular, “after/from a pure [attainment].”
- **kliṣṭam** — nominative singular neuter, “a defiled [attainment/state].”
- **svabhūmikam** — nominative singular neuter, “belonging to its own level.”

## Literal Translation

After an uncontaminated attainment, a wholesome state arises upward or downward, as far as the third and following levels. Likewise, after a pure attainment, a defiled state belonging to its own level may also arise.

## Philosophical Translation

An uncontaminated attainment can be followed by a wholesome attainment located above or below it within the permitted range. A pure attainment can be followed either by another pure state or by a defiled state of the same level. The system is therefore governed not only by a hierarchy of levels but also by lawful rules of immediate succession.

## Technical Vocabulary

- **anāsrava** — uncontaminated, free from outflows.
- **śubha** — wholesome.
- **śuddha** — pure but still worldly.
- **kliṣṭa** — defiled.
- **svabhūmika** — belonging to the same ground or level.
- **anantara** — immediately subsequent; without an intervening state.

## Doctrinal Determination

This verse introduces the succession-law among modes of attainment.

The important distinctions are:

1. An uncontaminated attainment does not terminate the sequence. It may be followed by a wholesome attainment above or below it, within the stated range.
2. A pure attainment is less secure. From it, one may pass not only to another wholesome configuration but also to a defiled attainment of the same level.
3. Defilement here does not necessarily mean descent to a lower cosmological level. One can remain on the same ground while the mode of possession deteriorates.

Thus level and purity are independent axes:

- one may change level while remaining wholesome;
- one may remain at the same level while becoming defiled.

## Logical Determination

The chapter now moves from static classification to transition logic.

A state is no longer defined only by:

- its level,
- its factors,
- and its mode,

but also by the states that may immediately follow it.

This gives a directed relation among attainments:

```text
uncontaminated
    → wholesome above
    → wholesome below

pure
    → pure
    → defiled on the same level
```

The same node in the hierarchy therefore has several lawful outgoing transitions. Samāpatti is becoming a system of determinate states and admissible transformations.

## Organon Light

The verse gives a preliminary logic of mediation.

A determination is not fully known when its internal content alone is listed. It must also be known through:

- what can precede it,
- what can follow it,
- how it rises,
- how it descends,
- and how its qualitative mode can change without changing its level.

This is especially important for a qualitative logic of staged purity. Purity is not a permanent substance attached to a level. It is a determinate mode that can be preserved, surpassed, or lost according to lawful transitions.

## OWL++ Seed

```text
Class: Attainment
Class: UncontaminatedAttainment
Class: PureAttainment
Class: DefiledAttainment
Class: WholesomeAttainment

ObjectProperty: immediatelyPrecedes
ObjectProperty: hasLevel
ObjectProperty: mayTransitionTo

Rule:
UncontaminatedAttainment
    mayTransitionTo WholesomeAttainment
    at an admissible higher or lower level.

Rule:
PureAttainment
    mayTransitionTo DefiledAttainment
    only when both share the same level.
```

## Commit History

- Initial Sanskrit-first analysis of VAkK 8.15.
