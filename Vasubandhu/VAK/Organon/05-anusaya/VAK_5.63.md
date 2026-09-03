# VAK_5.63

## 1. Sanskrit (Devanāgarī)

```sanskrit
सकृत् क्षयो विसंयोगलाभस्तेषां पुनः पुनः ।
प्रतिपक्षोदयफलप्राप्तीन्द्रियविवृद्धिषु ॥ ५.६३ ॥
```

## 2. Sanskrit (IAST)

```text
sakṛt kṣayo visaṃyoga-lābhas teṣāṃ punaḥ punaḥ |
pratipakṣodaya-phala-prāptīndriya-vivṛddhiṣu || 5.63 ||
```

VAK 5.63 asks whether progress through further Path-stages repeatedly destroys
an already destroyed affliction. Its answer distinguishes the single event of
destruction from repeated acquisition of disconnection.

## 3. Padaccheda and Lexical Analysis

```text
sakṛt | kṣayaḥ | visaṃyoga-lābhaḥ | teṣām | punaḥ punaḥ |
pratipakṣa-udaya | phala-prāpti | indriya-vivṛddhiṣu
```

| Form | Morphology | Contextual sense |
|---|---|---|
| `sakṛt` | indeclinable adverb | once, on one occasion |
| `kṣayaḥ` | nominative singular masculine | destruction or exhaustion of the affliction |
| `visaṃyoga-lābhaḥ` | nominative singular masculine compound | acquisition of disconnection from the affliction |
| `teṣām` | genitive plural masculine | of those afflictions |
| `punaḥ punaḥ` | repeated adverbial expression | again and again, on repeated occasions |
| `pratipakṣa-udaya` | member of locative series | arising of the counteragent, here the liberation path |
| `phala-prāpti` | member of locative series | attainment of a fruit of śramaṇa-hood |
| `indriya-vivṛddhiṣu` | locative plural feminine | upon development or transition of the faculties |

The final compound is a locative series naming occasions of repeated
`visaṃyoga-lābha`. `Punaḥ punaḥ` modifies acquisition of disconnection, not
destruction of the affliction.

## 4. Grammar

The verse places two nominative constructions in contrast:

```text
kṣayaḥ
    sakṛt

visaṃyoga-lābhaḥ teṣām
    punaḥ punaḥ
```

The genitive `teṣām` relates the disconnection to the afflictions whose
destruction has just been asserted. The locative series specifies when a
renewed acquisition may occur:

```text
pratipakṣodaye
phala-prāptau
indriya-vivṛddhiṣu
```

The Bhāṣya counts six possible occasions under these three headings: the
liberation-path occasion, the four fruits of śramaṇa-hood, and transition of
the faculties. Its `yathāyogam` qualifies the distribution: not every
disconnection is acquired at all six.

## 5. Translation

### Literal Translation

> Their destruction occurs once; acquisition of disconnection from them,
> however, occurs repeatedly—upon arising of the counteragent, attainment of
> a fruit, and development of the faculties.

### Bhāṣya-informed study translation

> Each affliction is destroyed only once, by the Path that abandons it. Yet
> the same disconnection from that affliction can be acquired repeatedly, as
> appropriate, on six possible occasions: with the arising of the liberation
> path, with attainment of each of the four fruits of śramaṇa-hood, and with a
> transition or development of the spiritual faculties.

Some disconnections are acquired on all six occasions and others on as few as
two. The repeated acquisition must therefore remain indexed to the relevant
affliction and Path-condition.

## 6. Philosophical Translation

> Progress does not destroy the same defect again and again. A determinate
> affliction meets its proper abandoning Path once and is exhausted. What can
> recur is the practitioner's acquisition of the already established
> disconnection under a new Path-condition, fruit, or faculty-status. The
> negated determination, the attained relation of freedom from it, and the
> successive designation of that relation are therefore distinct without
> requiring multiple destructions of one and the same affliction.

This is not a claim that freedom is repeatedly lost and recovered. It is a
distinction between one cessation and the subject's path-relative acquisitions
of that same disconnection.

## 7. Technical Vocabulary

**`Sakṛt kṣaya` — destruction once**

Each kleśa has its own `prahāṇa-mārga`, and that path destroys it. Further
special Path-stages do not perform a second destruction of what is already
destroyed.

**`Visaṃyoga` — disconnection**

Separation from the affliction, previously related to
`pratisaṃkhyānirodha`. It is not synonymous with the event of the affliction's
`kṣaya`.

**`Visaṃyoga-lābha` — acquisition of disconnection**

The repeatable attainment-relation. The Bhāṣya insists that it is the same
disconnection (`sa eva visaṃyogaḥ`) acquired under different Path-conditions,
not several destructions of the same affliction.

**`Pratipakṣodaya` — arising of the counteragent**

Although VAK 5.61 classified `pratipakṣa` fourfold, the Bhāṣya explicitly
restricts its meaning here to `vimukti-mārga`, the path of liberation. The
term's extension is controlled by its present relation.

**`Phala-prāpti` — attainment of fruit**

Attainment of one of the four `śrāmaṇya-phalas`. Each relevant fruit-condition
can ground a renewed acquisition of an already established disconnection.

**`Indriya-vivṛddhi` / `indriya-saṃcāra` — development or transition of the faculties**

The Bhāṣya glosses the verse's “increase” as transition of the spiritual
faculties. This supplies the sixth possible occasion.

**`Yathāyogam` — as appropriate**

The crucial prose restriction. Six is the maximum occasion-set; depending on
the disconnection, actual acquisition may range from all six occasions down
to two.

**`Parijñā-saṃjñā` — designation as parijñā**

The same disconnection receives the designation `parijñā` in its respective
states. This sentence transitions into the ninefold parijñā analysis beginning
with the following verse.

## 8. Logical Determination

For each affliction:

```text
ExistsExactlyOne(
    DestructionEvent(kleśa, itsPrahāṇaMārga)
)
```

But acquisition is repeatable:

```text
AcquireDisconnection(practitioner, sameVisaṃyoga, pathOccasion)
```

where the possible occasions are:

```text
{VimuktiMārga,
 FirstŚrāmaṇyaFruit,
 SecondŚrāmaṇyaFruit,
 ThirdŚrāmaṇyaFruit,
 FourthŚrāmaṇyaFruit,
 IndriyaSaṃcāra}
```

Applicability is constrained:

```text
MayAcquireAt(visaṃyoga, occasion)
    only if AppropriateTo(visaṃyoga, occasion)

2 ≤ Count(ApplicableOccasions(visaṃyoga)) ≤ 6
```

Three levels must remain distinct:

```text
ObjectLevel:       Destroyed(kleśa)
AttainmentLevel:   Acquired(practitioner, visaṃyoga)
DesignationLevel:  BearsName(visaṃyogaAtState, Parijñā)
```

Therefore:

```text
Repeated(AcquisitionOfDisconnection)
    ⇏ Repeated(DestructionOfKleśa)

Same(visaṃyoga)
    is compatible with
Distinct(acquisitionOccasions)
```

## 9. Interpretive Note

**Question and categorical answer.** The Bhāṣya asks whether movement through
special Path-stages produces further abandonment of the afflictions. “No”
fixes the doctrinal problem before the kārikā's distinction is unfolded.

**One destruction, repeated acquisition.** The same kleśa is not resurrected
for each later stage. Nor does each stage produce a numerically new cessation.
What changes is the acquisition-status of the same disconnection in relation
to a developing practitioner.

**Contextual narrowing of terminology.** `Pratipakṣa` named a fourfold genus
in 5.61 but means `vimukti-mārga` here. A durable study must preserve this
local extension rather than imposing one global gloss on every occurrence.

**Six is conditional.** The prose's `yathāyogam` blocks a mechanical sixfold
rule. Some disconnections receive acquisition at six occasions, others at
progressively fewer, down to two.

**Transition to parijñā.** The same disconnection, in these various states,
receives the name `parijñā`. The next block therefore studies a named Path-
attainment structure, not a fresh series of affliction-destructions.

**Organon interpretation.** A semantic representation must distinguish the
irreversible target-event from repeatable subject-stage relations:

```text
DisconnectionAcquisition
    acquiredBy Practitioner
    concernsSameDisconnection
    occursAt PathOccasion
    hasFacultyState
    mayBearDesignation Parijñā
    supportedBy SourceSpan
```

This formalization preserves the source's levels and is not vocabulary
attributed to Vasubandhu.

## 10. OWL++ Seed

```text
Class: Affliction
Class: DestructionEvent
Class: Disconnection
Class: DisconnectionAcquisition
Class: Practitioner
Class: PathOccasion
Class: LiberationPathOccasion
    SubClassOf: PathOccasion
Class: SramanyaFruitAttainment
    SubClassOf: PathOccasion
Class: FacultyTransition
    SubClassOf: PathOccasion
Class: PathDesignation

ObjectProperty: destroysAffliction
    Domain: DestructionEvent
    Range: Affliction

ObjectProperty: concernsDisconnection
    Domain: DisconnectionAcquisition
    Range: Disconnection

ObjectProperty: acquiredBy
    Domain: DisconnectionAcquisition
    Range: Practitioner

ObjectProperty: occursAt
    Domain: DisconnectionAcquisition
    Range: PathOccasion

ObjectProperty: bearsDesignation
    Domain: Disconnection
    Range: PathDesignation

Constraint: Affliction(?k)
    hasMaximumDestructionEventCount 1

Rule: AppropriateTo(?v, ?occasion)
      AND PractitionerAt(?p, ?occasion)
    -> MayAcquireDisconnection(?p, ?v, ?occasion)

Constraint: RepeatedDisconnectionAcquisition(?v)
    doesNotEntail RepeatedAfflictionDestruction(?k)

Constraint: ApplicableOccasionCount(?v, ?n)
    requires 2 <= ?n <= 6

Assertion: PratipaksaInVAK563 refersTo VimuktiMarga
Assertion: PhalaInVAK563 refersTo FourSramanyaFruits
Assertion: IndriyaVivrddhiInVAK563 refersTo IndriyaSamcara

View: RepeatedDisconnectionAcquisitionMap
    Preserves: AfflictionIdentity, SingleDestruction, SameDisconnection,
               AcquisitionOccasion, Fruit, FacultyTransition,
               PathDesignation, SourceProvenance
```

The seed records the exact asymmetry: affliction-destruction is singular,
while acquisition of the same disconnection is path-conditionally repeatable.
