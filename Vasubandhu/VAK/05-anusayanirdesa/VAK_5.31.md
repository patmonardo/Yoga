# VAK 5.31

## Sanskrit

निरोधमार्गदृग्घेयाः सर्वे स्वाधिकगोचराः ।
अनास्रवास्त्रिधात्वन्त्यत्रयानास्रवगोचराः ॥ ५.३१ ॥

## IAST

nirodhamārgadṛggheyāḥ sarve svādhikagocarāḥ |
anāsravās tridhātvantyatrayānāsravagocarāḥ || 5.31 ||

## Padaccheda

```text
nirodha-mārga-dṛk-heyāḥ
sarve
sva-adhika-gocarāḥ
anāsravāḥ
tri-dhātu-antya-traya-anāsrava-gocarāḥ
```

Normalized:

```text
nirodha-mārga-dṛk-heyāḥ sarve sva-adhika-gocarāḥ |
anāsravāḥ tri-dhātu-antya-traya-anāsrava-gocarāḥ ||
```

## Grammar

- `nirodhamārgadṛggheyāḥ` — nominative plural: dharmas to be abandoned through seeing cessation and through seeing the path.
- `sarve` — all.
- `svādhikagocarāḥ` — having as their object-range their own category together with the additional appropriate category; the compact compound continues the object-matrix established in 5.29–5.30.
- `anāsravāḥ` — undefiled or non-outflowing dharmas.
- `tridhātvantyatrayānāsravagocarāḥ` — objects of the last three consciousness-categories of the three domains and of undefiled consciousness.

## Literal translation

All dharmas abandoned through seeing cessation and the path are objects of their own corresponding consciousness together with the additional appropriate consciousness. Undefiled dharmas are objects of the last three consciousness-categories of the three domains and of undefiled consciousness.

## Philosophical translation

The defilements removed by insight into cessation and the path remain cognitively accessible within the consciousness appropriate to their own class and within the further standpoint capable of taking them as object. Undefiled dharmas, by contrast, are knowable through the final three consciousness-categories of each domain and through undefiled cognition itself.

## Analysis

Verses 5.29–5.30 classified the object-range of dharmas abandoned through seeing suffering, seeing origin, and cultivation. Verse 5.31 completes the matrix with the dharmas abandoned through seeing cessation and seeing the path.

The first half indicates that these dharmas are not confined to one isolated cognitive standpoint:

```text
nirodha-dṛg-heya
mārga-dṛg-heya
    → own corresponding cognition
    → additional appropriate cognition
```

The precise expansion of `svādhika` belongs to the full Bhāṣya matrix, but the kārikā-level result is clear: these objects have an enlarged admissible cognitive range.

The second half gives a different rule for undefiled dharmas:

```text
anāsrava-dharma
    → final three consciousness-categories
      across the three domains
    → undefiled consciousness
```

Thus pure or undefiled objects are not objects of every consciousness indiscriminately. Their knowability is itself conditioned by the type and level of cognition.

## Technical vocabulary

```text
nirodha-dṛg-heya
    abandoned through seeing cessation

mārga-dṛg-heya
    abandoned through seeing the path

gocara
    object-range
    sphere within which cognition can take something as object

anāsrava
    undefiled
    free from outflows

svādhika
    one's own plus the further admissible category
```

## Doctrinal determination

The verse completes a fivefold practical classification of objects by mode of abandonment:

```text
seeing suffering
seeing origin
seeing cessation
seeing path
cultivation
```

But the classification is not merely about removal. Each class is also mapped to the consciousnesses capable of taking it as object.

Therefore:

```text
mode of abandonment
    and
mode of cognition
```

are distinct but coordinated determinations.

The verse also prevents a crude equation of purity with universal accessibility:

```text
undefiled
    ≠
object of every cognition
```

Even an undefiled dharma requires an adequately qualified cognitive standpoint.

## Logical determination

The sequence 5.29–5.31 establishes an epistemic relation matrix:

```text
ObjectClass
    × Domain
    × AbandonmentMode
    × CognitionCategory
    → admissible object-relation
```

The copular relation is therefore not simply:

```text
cognition knows object
```

but:

```text
this cognition-category
under this domain-condition
can take this object-class
as its object
```

The relation is typed.

This is crucial for a practical extension of the Dialectical Copula. The copula must carry at least three powers:

```text
relate
qualify the relation
validate the standpoint from which the relation holds
```

The verse therefore gives a model of determinate predication in which the legitimacy of the relation depends upon the power of the knowing side.

## Organon note

The strongest architectural result is:

```text
canTakeAsObject
    is not a universal relation
```

It must be constrained by:

```text
cognition type
domain
object class
abandonment mode
purity status
```

For the Dialectical Copula, this means that a predicative edge should not merely connect a subject and object. It should also record the capacity under which the connection is valid.

```text
Copula
    = relation
    + standpoint
    + admissibility condition
```

That is the practical power added to knowledge.

## OWL++ seed

```text
Class: CognitionCategory
Class: ObjectClass
Class: AbandonmentMode
Class: Domain

ObjectProperty: canTakeAsObject
    Domain: CognitionCategory
    Range: ObjectClass

ObjectProperty: validUnderDomain
    Domain: canTakeAsObject
    Range: Domain

ObjectProperty: abandonedBy
    Domain: Dharma
    Range: AbandonmentMode

Class: UndefiledDharma
    SubClassOf: Dharma

Rule:
    CognitionCategory(?c)
    ObjectClass(?o)
    validStandpointFor(?c, ?o)
    -> canTakeAsObject(?c, ?o)
```

## Bhāṣya questions

1. How exactly does the Bhāṣya expand `svādhikagocarāḥ` for cessation- and path-abandoned dharmas in each domain?
2. What are the “last three” consciousness-categories designated by `antyatraya`?
3. Why are undefiled dharmas excluded from the object-range of the earlier consciousness-categories?
4. Does the Bhāṣya distinguish mere cognitive access from liberating cognition in this matrix?
5. How does this object-classification connect to the subsequent distinction between contaminated cognition with and without active anuśaya?

## Commit

```text
Add VAK 5.31 analysis
```
