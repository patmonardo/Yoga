# VAK_2.40 — Relinquishing Non-Acquisition and the Regress of Acquisition

## 1. Sanskrit (Devanāgarī)

> कामाद्याप्तामलानां च मार्गस्याप्राप्तिरिष्यते ।
>
> पृथग्जनत्वं तत्प्राप्तिभूसंचाराद्विहीयते ॥ २.४० ॥

## 2. Sanskrit (IAST)

> kāmādyāptāmalānāṃ ca mārgasyāprāptir iṣyate /
>
> pṛthagjanatvaṃ tatprāptibhūsaṃcārād vihīyate // 2.40 //

## 3. Lexical Analysis

```text
kāmādyāptāmalānāṃ ca → kāma-ādi-āpta-amalānām ca
mārgasyāprāptiḥ       → mārgasya aprāptiḥ
pṛthagjanatvam        → pṛthagjana-tvam
tatprāptibhūsaṃcārāt  → tat-prāpti-bhūmi-saṃcārāt
vihīyate              → vi-hīyate
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| kāma-ādi-āpta-amalānām | genitive plural compound | of Dharmas in the three Principle-ranges and uncontaminated Dharmas |
| mārgasya | genitive singular | of the Path |
| aprāptiḥ | nominative feminine singular | non-acquisition |
| pṛthagjanatvam | nominative neuter singular | ordinary-person status |
| tat-prāpti | compound member | acquisition of that Dharma |
| bhūmi-saṃcāra | compound | transition of ground |
| vihīyate | passive verb | is relinquished |

## 4. Scientific English Rendering

> Non-acquisition is threefold also for Dharmas in the Desire, Form, and
> Formless Principle-ranges and for uncontaminated Dharmas. Non-acquisition
> of the Path is held to be ordinary-person status. It is relinquished
> through acquisition of that Path or through transition of ground.

The Bhāṣya distinguishes the two occasions: acquiring the noble Path and
changing a relevant ground are not interchangeable achievements.

## 5. Interpretation

This verse states that ordinary-person status is transformable. The
continuum does not cease to be ordinary merely because a present event is
called elevated; the relevant noble Dharma must be acquired, or the
applicable ground must change. Conversely, non-acquisition is not a
permanent nature of the person.

The ensuing Bhāṣya exposes the cost of treating *prāpti* and *aprāpti* as
independent real entities. If each entity must itself be acquired, a
second-order acquisition arises; the proposed mutual-possession solution
halts a simple regress at one point but generates an expanding proliferation
of acquisitions over successive moments.

## 6. Logical Determination

```text
OrdinaryPersonStatus(S)
    := NonAcquisition(S, NoblePath)

Acquires(S, NoblePath)
or GroundTransition(S)
    → Relinquishes(S, OrdinaryPersonStatus)
```

The reified model:

```text
RealPrapti(P, S, D)
    → requires acquisition of P
    → requires acquisition of that acquisition
```

The critical result:

```text
ContinuumCapacityAndTransformation
    explains status
    without multiplying possession-entities
```

## 7. Interpretive Note

The verse's opening completes VAK 2.39's Principle-range classification.
Its second half carries ordinary-person status into the following regress
argument. No transition to VAK 2.41 is made here.

## 8. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_40
    a vak:Karika ;
    rdfs:label "VAK 2.40" ;
    vak:hasTopic vak:RelinquishmentOfNonAcquisition ;
    vak:belongsTo vak:Indriyanirdesa .

vak:OrdinaryPersonStatus
    vak:endsThrough vak:AcquisitionOfNoblePath,
        vak:GroundTransition .
```
