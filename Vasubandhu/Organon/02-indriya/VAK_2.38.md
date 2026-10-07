# VAK_2.38

## 1. Sanskrit (Devanāgarī)

> त्रिधा नशैक्षाशैक्षाणामहेयानां द्विधा मता ।
>
> अव्याकृताप्तिः सहजाभिज्ञानैर्माणिकादृते ॥ २.३८ ॥

## 2. Sanskrit (IAST)

> tridhā naśaikṣāśaikṣāṇām aheyānāṃ dvidhā matā /
>
> avyākṛtāptiḥ sahajābhijñānairmāṇikād ṛte // 2.38 //

## 3. Lexical Analysis

```text
naśaikṣāśaikṣāṇām → na-śaikṣa-aśaikṣāṇām
aheyānām           → a-heyānām
avyākṛtāptiḥ       → avyākṛta-āptiḥ
sahajā              → saha-jā
abhijñānairmāṇikāt → abhijñā-nairmāṇikāt
ṛte                 → ṛte
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| naśaikṣāśaikṣāṇām | genitive plural compound | of Dharmas neither trainee nor beyond training |
| tridhā | adverb | threefold |
| aheyānām | genitive plural | of Dharmas not subject to abandonment |
| dvidhā | adverb | twofold |
| avyākṛta-āptiḥ | nominative feminine singular | acquisition of indeterminate Dharma |
| sahajā | nominative feminine singular | co-arisen |
| abhijñā-nairmāṇikāt | ablative compound | except superknowledges and magical-creation mind |
| ṛte | indeclinable | except |

## 4. Scientific English Rendering

> Acquisition of Dharmas neither trainee nor beyond training is threefold;
> acquisition of Dharmas not subject to abandonment is twofold.
> Acquisition of unobscured-indeterminate Dharmas is co-arisen, except for
> the superknowledges and magical-creation mind.

The Bhāṣya completes the first two classifications begun in VAK 2.37:
the same neither-trainee-nor-beyond-training cessation can have trainee or
beyond-training acquisition according to the Path through which it was
obtained; the non-abandonable cases distinguish cultivation-abandonable
acquisition from uncontaminated non-abandonable acquisition.

## 5. Interpretation

The verse gives an exception to the general three-time matrix. Weak
unobscured-indeterminate Dharmas have acquisition only with their
manifestation. Two indeterminate superknowledges and magical-creation mind
are excepted because special practice gives them sufficient strength for
prior, co-arisen, and subsequent acquisition.

The Bhāṣya then adds that obscured-indeterminate manifest Form also has
co-arisen-only acquisition, while Desire-Principle Form has no prior
acquisition, though co-arisen and subsequent acquisition may occur. These
are distinctions of capacity, preparation, and retention—not a claim that
all indeterminate Dharmas behave alike.

Vijñāna is Discriminative Cognition joining and governing Perception and
Conception. In the present local analysis it governs a continuum whose
acquisition-status can be weak, cultivated, momentary, or retained; the
source does not convert this into a universal rule of instruction.

## 6. Logical Determination

```text
WeakUnobscuredIndeterminate(D)
    → AcquisitionTime(S, D) = DharmaTime(D)

ExceptionalCultivatedIndeterminate(D)
    → AcquisitionTime(S, D)
      in {prior, co-arisen, subsequent}

DesirePrincipleForm(D)
    → prior acquisition is excluded
```

## 7. Interpretive Note

*Sahajā* means co-arisen in this temporal classification, not innate or
birth-acquired. The source's final compound is compressed and the
identification of the exceptions follows the Bhāṣya; its exact
segmentation remains provisional.

## 8. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_38
    a vak:Karika ;
    rdfs:label "VAK 2.38" ;
    vak:hasTopic vak:TemporalModesOfAcquisition ;
    vak:belongsTo vak:Indriyanirdesa .

vak:ExceptionalCultivatedIndeterminate
    vak:permits vak:PriorAcquisition,
        vak:CoArisenAcquisition,
        vak:SubsequentAcquisition .
```
