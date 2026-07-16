# VAK 5.29

## Sanskrit

दुःखहेतुदृगभ्यासप्रहेयाः कामधातुजाः ।
स्वकत्रयैकरूपाप्तामलविज्ञानगोचराः ॥ ५.२९ ॥

## IAST

duḥkhahetudṛgabhyāsapraheyāḥ kāmadhātujāḥ |
svakatrayaikarūpāptāmalavijñānagocarāḥ || 5.29 ||

## Padaccheda

```text
duḥkha-dṛk-praheyāḥ
hetu-dṛk-praheyāḥ
abhyāsa-praheyāḥ
kāma-dhātu-jāḥ
svaka-traya
eka-rūpa-āpta
amala-vijñāna-gocarāḥ
```

Normalized:

```text
duḥkha-dṛk-praheyāḥ
hetu-dṛk-praheyāḥ
abhyāsa-praheyāḥ
kāmadhātujāḥ |
svaka-traya-eka-rūpāpta-amala-vijñāna-gocarāḥ ||
```

## Grammar

- `duḥkha-dṛk-praheyāḥ` — to be abandoned by seeing suffering.
- `hetu-dṛk-praheyāḥ` — to be abandoned by seeing the cause or arising of suffering.
- `abhyāsa-praheyāḥ` — to be abandoned by cultivation or repeated meditative practice.
- `kāmadhātujāḥ` — born in or belonging to the desire-domain.
- `svaka-traya` — the three consciousness-categories belonging to their own domain.
- `eka-rūpāpta` — one consciousness belonging to the form-domain.
- `amala-vijñāna` — undefiled or stainless consciousness.
- `gocarāḥ` — objects, fields, or ranges of cognition.

## Literal translation

The desire-domain dharmas to be abandoned by seeing suffering, by seeing its cause, and by cultivation are objects of the three consciousnesses belonging to their own domain, of one consciousness belonging to the form-domain, and of undefiled consciousness.

## Philosophical translation

The contaminated dharmas of the desire-domain that are removed through insight into suffering and its origin, or through cultivation, remain determinable as objects within several distinct cognitive standpoints: three contaminated modes native to their own domain, one higher-domain mode, and stainless cognition.

## Analysis

Verse 5.28 distinguished abandonment from complete disconnection. Verse 5.29 now classifies the cognitive standpoints from which the relevant dharmas can still be taken as objects.

The subject is not merely the affliction itself but the relation:

```text
cognition
    → takes as object
        → a determinate class of dharmas
```

The verse groups together three classes of desire-domain dharmas:

```text
abandoned by seeing suffering
abandoned by seeing origin
abandoned by cultivation
```

These are not cognitively sealed within the standpoint that produces them. They can become objects for:

```text
three consciousness-categories of their own domain
one consciousness-category of the form-domain
undefiled consciousness
```

Thus a contaminated dharma can be apprehended from:

```text
a contaminated standpoint within its own field
a higher contaminated standpoint
an undefiled standpoint
```

The same object therefore enters different epistemic relations without changing its identity.

## Technical vocabulary

```text
praheya
    that which is to be abandoned
    determination indexed to a specific path-operation

duḥkha-dṛk
    seeing suffering

hetu-dṛk
    seeing the cause or arising of suffering

abhyāsa
    cultivation
    repeated practical transformation

gocara
    cognitive range
    field in which an object can be taken up

amala-vijñāna
    stainless cognition
    cognition not contaminated by anuśaya
```

## Doctrinal determination

The verse distinguishes the status of a dharma from the status of the cognition that apprehends it.

```text
contaminated object
    can be apprehended by
undefiled cognition
```

Therefore:

```text
object-status
    ≠
cognition-status
```

A dharma abandoned by a path-stage does not become unintelligible. It remains available to cognition under a different relation.

This extends the result of 5.28:

```text
abandonment
    removes one operative bond

cognitive objecthood
    may remain
```

The verse therefore gives a structured account of retrospective and diagnostic cognition. One can know a defilement without being defiled by that act of knowing.

## Logical determination

The central logical form is a typed object-relation:

```text
CognitionType
    hasObjectRange
DharmaClass
```

The same `DharmaClass` may lie within the object-range of several cognition-types.

```text
one object
    → many admissible standpoints
```

This is not relativism, because the object is not altered by the standpoint. What changes is the cognitive power under which it is apprehended.

The verse therefore distinguishes:

```text
what the dharma is
from
how the dharma is known
```

That distinction is essential to any theory of reflective insight.

## Organon note

This verse gives the Platform a direct architecture for reflective diagnosis.

```text
ObjectState
    may be contaminated

EvaluatorState
    may be uncontaminated
```

The system must therefore avoid propagating the status of an object into the status of the evaluator.

```text
observesDefilement
    does not imply
isDefiledByDefilement
```

This is the beginning of a powerful distinction between:

```text
first-order participation
second-order observation
```

Absolute Insight, in the project sense, would require the second-order standpoint to preserve full access to the first-order object without reproducing its contamination.

## OWL++ seed

```text
Class: DharmaClass
Class: CognitionType
Class: ContaminatedDharma
Class: UndefiledCognition

ObjectProperty: hasObjectRange
    Domain: CognitionType
    Range: DharmaClass

ObjectProperty: belongsToDomain
    Domain: DharmaClass
    Range: Realm

ObjectProperty: abandonedBy
    Domain: DharmaClass
    Range: PathOperation

Individual: DesireRealmSufferingAbandonable
    Types: ContaminatedDharma
    belongsToDomain: KamaDhatu
    abandonedBy: SeeingSuffering

Individual: DesireRealmOriginAbandonable
    Types: ContaminatedDharma
    belongsToDomain: KamaDhatu
    abandonedBy: SeeingOrigin

Individual: DesireRealmCultivationAbandonable
    Types: ContaminatedDharma
    belongsToDomain: KamaDhatu
    abandonedBy: Cultivation

Rule:
    UndefiledCognition(?c)
    hasObjectRange(?c, ?d)
    ContaminatedDharma(?d)
    -> ReflectiveApprehension(?c, ?d)
```

## Bhāṣya questions

1. What precisely are the three `svaka` consciousness-categories counted for these desire-domain dharmas?
2. Which single form-domain cognition is intended by `eka-rūpāpta`?
3. Does `amala-vijñāna` here include all undefiled cognition or only particular path-knowledges?
4. How does the Bhāṣya distinguish objecthood from conjunction with anuśaya in this context?
5. Does this classification imply that a fully abandoned defilement remains available as an object of retrospective knowledge?

## Commit

```text
Add VAK 5.29 analysis
```
