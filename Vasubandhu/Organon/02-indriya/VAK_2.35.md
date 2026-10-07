# VAK_2.35

## 1. Sanskrit (Devanāgarī)

> विप्रयुक्तास्तु संस्काराः प्राप्त्यप्राप्ती सभागता ।
>
> आसंज्ञिकं समापत्ती जीवितं लक्षणानि च ॥ २.३५ ॥

## 2. Sanskrit (IAST)

> viprayuktās tu saṃskārāḥ prāptyaprāptī sabhāgatā /
>
> āsaṃjñikaṃ samāpattī jīvitaṃ lakṣaṇāni ca // 2.35 //

VAK 2.36 begins by adding groups of names and related formations to this
catalogue. The Bhāṣya's detailed inquiry into *prāpti* begins there.

## 3. Lexical Analysis

```text
viprayuktās tu  → viprayuktāḥ tu
saṃskārāḥ       → saṃskārāḥ
prāptyaprāptī   → prāpti-aprāptī
sabhāgatā       → sabhāgatā
āsaṃjñikam      → āsaṃjñikam
samāpattī       → samāpattī
jīvitam         → jīvitam
lakṣaṇāni ca    → lakṣaṇāni ca
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| viprayuktāḥ | nominative masculine plural participle | dissociated or not associated |
| tu | particle | introduces a new class |
| saṃskārāḥ | nominative masculine plural | conditioned formations |
| prāpti-aprāptī | nominative feminine dual | acquisition and non-acquisition |
| sabhāgatā | nominative feminine singular | commonality |
| āsaṃjñikam | nominative neuter singular | non-percipient condition |
| samāpattī | nominative feminine dual | the two attainments |
| jīvitam | nominative neuter singular | life-continuity |
| lakṣaṇāni | nominative neuter plural | conditioned marks |
| ca | conjunction | and |

## 4. Scientific English Rendering

> The conditioned formations dissociated from consciousness are acquisition
> and non-acquisition, commonality, the non-percipient condition, the two
> attainments, life-continuity, and the conditioned marks.

The following verse completes the list with groups of names and related
formations. The Bhāṣya calls the class dissociated because its members are
neither associated with consciousness and mental factors nor of the nature
of Form.

## 5. Interpretation

This verse begins a new class after the account of consciousness and its
associated mental factors. “Dissociated” does not mean unconditioned,
causally isolated, or irrelevant to a cognitive continuum. It identifies
formations not joined to consciousness through the fivefold association
defined in VAK 2.34 and not classified as Form.

The leading dyad, *prāpti:aprāpti*, distinguishes a Dharma's present
manifestation from its status in a continuum. A Dharma may be acquired or
not acquired without being manifest as a factor in the present cognition.
VAK 2.36 tests the ground of this distinction: whether it requires a
separate real Dharma or is a designation based on the continuum's causal
capacity and transformation.

The Kośa's governing synthesis remains: Vijñāna is Discriminative Cognition
joining and governing Perception and Conception. Their unity is
Inconceivable as homogeneous operation, with its Idea disclosed in the
Cognition Base. Vijñāna governs Mind and guides Dharma Base. *Avijñapti*
is the same Dharma classified in Form Base and Dharma Base, with Vijñāna
bearing a *prati* relation to it. The present classification makes visible
conditions that structure a continuum without reducing them to the
consciousness-event then manifest.

## 6. Logical Determination

```text
ConditionedFormation(D)
and
not AssociatedWithConsciousness(D)
and
not Form(D)
    → DissociatedFormation(D)
```

The initial pair must be distinguished from simple absence:

```text
PresentlyManifest(S, D)
    is not identical to
AcquiredByContinuum(S, D)
```

The verse only introduces the catalogue. It does not yet establish the
ontological status of each member, and it does not yet define the two
attainments or the other formations in the list.

## 7. Interpretive Note

The running transcription at 62.14 contains an anomalous double negative:
*na cittena asaṃprayuktā*. The Sanskrit witness is unchanged. The Bhāṣya's
class-name and contrast with Form require the contextual rendering “not
associated with consciousness.”

The beginning of VAK 2.36, *nāmakāyādayaś ca iti*, completes this
cross-verse catalogue. The repository treats VAK 2.35 as the introduction
and VAK 2.36 as the detailed examination of acquisition and
non-acquisition.

## 8. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_35
    a vak:Karika ;
    rdfs:label "VAK 2.35" ;
    vak:hasTopic vak:DissociatedFormations ;
    vak:belongsTo vak:Indriyanirdesa .

vak:DissociatedFormation
    vak:notAssociatedWith vak:Consciousness ;
    vak:notClassifiedAs vak:Form .

vak:AcquisitionAndNonAcquisition
    a vak:DissociatedFormation ;
    vak:hasMembers vak:Acquisition,
        vak:NonAcquisition .
```
