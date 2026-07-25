# VAkK 8.18

## Sanskrit

द्वे त्रीणि त्रीणि चैकं च हानभागाद्यनन्तरम् ।
गत्वागम्य द्विधा भूमीरष्टौ श्लिष्टैकलङ्घिताः ॥ VAkK_8.18 ॥

## IAST

dve trīṇi trīṇi caikaṃ ca hānabhāgādyanantaram /
gatvāgamya dvidhā bhūmīr aṣṭau śliṣṭaikalaṅghitāḥ // VAkK_8.18 //

## Source Caution

The source file separates `hāna bhāgādi`; this is normalized to `hānabhāgādi`. It also reads `śliṣṭai kalaṅghitāḥ`; the compound is normalized here as `śliṣṭaika-laṅghitāḥ`, “contiguous and with one [level] crossed.”

## Padaccheda

- dve
- trīṇi
- trīṇi
- ca
- ekam
- ca
- hāna-bhāga-ādi-anantaram
- gatvā
- āgamya
- dvidhā
- bhūmīḥ
- aṣṭau
- śliṣṭa
- eka-laṅghitāḥ

## Grammar

- **dve, trīṇi, trīṇi, ekam** — neuter numerals, “two, three, three, and one.”
- **hānabhāgādyanantaram** — “immediately after [the pure attainments] beginning with the decline-tending one.”
- **gatvā** — absolutive of √gam, “having gone,” here indicating forward or ascending traversal.
- **āgamya** — absolutive of ā-√gam, “having returned,” indicating reverse or descending traversal.
- **dvidhā** — “in two ways,” referring to worldly and uncontaminated modes.
- **bhūmīḥ aṣṭau** — accusative plural, “the eight grounds,” namely the four dhyānas and four ārūpyas.
- **śliṣṭa** — contiguous, immediately adjacent.
- **eka-laṅghitāḥ** — with one level crossed over or skipped.

## Literal Translation

Immediately after the decline-tending and the other [pure attainments], there arise respectively two, three, three, and one. Having gone forward and returned in two ways through the eight grounds, [one traverses them] contiguously and by crossing one [ground].

## Philosophical Translation

The four kinds of pure attainment do not have the same range of immediate successors: their permitted continuations are respectively two, three, three, and one. Mastery then requires a complete forward and reverse traversal of all eight fundamental grounds, in both worldly and uncontaminated modes, first through adjacent succession and then by crossing over one intervening level.

## Technical Vocabulary

- **hānabhāgīya** — tending toward decline.
- **sthitibhāgīya** — tending toward maintenance of the same level.
- **viśeṣabhāgīya** — tending toward a higher level.
- **nirvedhabhāgīya** — tending toward penetration and the uncontaminated.
- **bhūmi** — ground or level of attainment.
- **anantara** — immediately successive.
- **śliṣṭa** — contiguous; proceeding through neighboring levels.
- **laṅghana** — crossing or skipping a level.
- **sāsrava / anāsrava** — worldly-contaminated / uncontaminated.

## Doctrinal Determination

The first half completes the fourfold classification introduced in VAkK 8.17 by giving the number of lawful immediate successors for each type of pure attainment:

1. after the decline-tending attainment: two;
2. after the stability-tending attainment: three;
3. after the higher-tending attainment: three;
4. after the penetration-tending attainment: one.

The second half begins the training that leads toward crossed attainment. The practitioner must master all eight fundamental grounds:

- the four dhyānas;
- the four ārūpyas;

and must traverse them:

- forward and backward;
- in worldly and uncontaminated modes;
- first by contiguous succession;
- then by crossing one level.

The verse therefore combines transition law with disciplined mobility through the whole hierarchy.

## Logical Determination

The system now becomes more than a static ladder. It has both:

- local transition rules;
- global traversal rules.

The first half specifies the number of admissible next states from each pure mode. The second specifies how the entire eight-level field is to be mastered as an ordered network.

```text
local law
    each mode has a determinate successor range

global law
    all eight grounds must be traversed
    forward and backward
    in both principal modes
    adjacently and by controlled crossing
```

This is not arbitrary jumping. Crossing becomes possible only after contiguous order has been mastered.

## Organon Light

VAkK 8.18 introduces a rudimentary logic of systematic mobility.

A level is fully mastered only when one knows:

- what may immediately follow it;
- how it stands in the whole series;
- how to ascend through the series;
- how to descend through the series;
- how worldly and uncontaminated realizations differ;
- and how an intermediate level may later be crossed without losing the order of the whole.

The decisive point is that skipping presupposes sequence. A mediated whole can support a controlled leap only because every neighboring relation has first been mastered.

## OWL++ Seed

```text
Class: PureAttainment
Class: DeclineTendingAttainment
Class: StabilityTendingAttainment
Class: HigherTendingAttainment
Class: PenetrationTendingAttainment
Class: FundamentalGround
Class: WorldlyTraversal
Class: UncontaminatedTraversal

ObjectProperty: mayImmediatelyTransitionTo
ObjectProperty: traversesGround
ObjectProperty: nextAdjacentGround
ObjectProperty: crossesOneGround
ObjectProperty: hasTraversalDirection

DataProperty: permittedSuccessorCount

DeclineTendingAttainment
    permittedSuccessorCount 2.

StabilityTendingAttainment
    permittedSuccessorCount 3.

HigherTendingAttainment
    permittedSuccessorCount 3.

PenetrationTendingAttainment
    permittedSuccessorCount 1.

Rule:
MasteryOfCrossedAttainment
    requires traversal of all eight FundamentalGrounds
    in forward and reverse order
    in worldly and uncontaminated modes.
```

## Commit History

- Initial Sanskrit-first analysis of VAkK 8.18.
