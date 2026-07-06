# VAkK_3.48 — Bhājanaloka: Meru and the First Mountain Ring

## 1. Sanskrit — Devanāgarī

```sanskrit
समन्ततस्तु त्रिगुणं तत्र मेरुर्युगन्धरः ।
ईशाधारः खदिरकः सुदर्शनगिरिस्तथा ॥ VAkK_3.48 ॥
```

## 2. Sanskrit — IAST

```iast
samantatas tu triguṇaṃ tatra merur yugandharaḥ /
īśādhāraḥ khadirakaḥ sudarśanagiris tathā // VAkK_3.48 //
```

## 3. Source Caution

The source reading is:

```iast
samantatastu triguṇaṃ tatra merūryugandharaḥ /
īśādhāraḥ khadirakaḥ sudarśanagiristathā // VAkK_3.48 //
```

Sandhi has been lightly separated:

```iast
samantataḥ tu triguṇam tatra meruḥ yugandharaḥ /
īśādhāraḥ khadirakaḥ sudarśana-giriḥ tathā //
```

The mountain name appears in the source as `īśādhāraḥ`. This should be checked against Pradhan, the bhāṣya, and standard cosmological lists, where the form may require verification. First-pass work preserves the source reading while marking the item for later review.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| samantatas tu | samantataḥ tu | but on all sides; all around |
| triguṇam | tri-guṇam | threefold, triple, three times as much |
| tatra | tatra | there, in that support-field |
| merur | meruḥ | Meru, the central mountain |
| yugandharaḥ | yugandharaḥ | Yugandhara, enclosing mountain/range |
| īśādhāraḥ | īśādhāraḥ | mountain name; preserve source reading, verify later |
| khadirakaḥ | khadirakaḥ | Khadiraka, mountain name |
| sudarśanagiriḥ | sudarśana-giriḥ | Sudarśana mountain |
| tathā | tathā | likewise, and also |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| samantataḥ | indeclinable | spatial adverb: “on all sides / all around” |
| tu | particle | marks transition or contrast |
| tri-guṇam | accusative singular neuter / adverbial | measure-relation: “threefold / triple” |
| tatra | indeclinable | locative frame: “there” |
| meruḥ | nominative singular masculine | first named mountain, central axis |
| yugandharaḥ | nominative singular masculine | second named mountain/range |
| īśādhāraḥ | nominative singular masculine | mountain name, source reading preserved |
| khadirakaḥ | nominative singular masculine | mountain name |
| sudarśana-giriḥ | nominative singular masculine | mountain name with `giri` explicitly stated |
| tathā | indeclinable | connective: “likewise / and also” |

## 6. Literal Translation

But there, all around, threefold: Meru, Yugandhara, Īśādhāra, Khadiraka, and likewise Sudarśana mountain.

## 7. Philosophical Translation

Within the measured support-field, the world-container now receives its first articulated structure: Meru and the surrounding mountain formations. The prior support-plane becomes a placed cosmological field, with central and enclosing determinations.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| samantataḥ | all around | circumferential or enclosing spatial determination |
| triguṇa | threefold / triple | proportional measure or relation |
| Meru | Meru | central mountain, axial cosmological determination |
| Yugandhara | Yugandhara | first enclosing mountain/range in the Meru system |
| Īśādhāra | Īśādhāra | named mountain/range; source form to be verified |
| Khadiraka | Khadiraka | named mountain/range |
| Sudarśana-giri | Sudarśana mountain | named mountain/range, explicitly marked as `giri` |

## 9. Doctrinal Determination

VAkK_3.48 begins the articulation of the support-field into named cosmological places. VAkK_3.45–3.47 established the wind, water, and gold foundation, together with vertical and lateral measures. This verse now introduces Meru and the first set of mountain formations.

The significant transition is:

```text
measured support-field
    → named cosmological structure
```

The container-world is no longer only layered and measured. It begins to receive internal differentiation through centrality and enclosure.

## 10. Logical Determination

```text
support
    → expanse
        → placement
            → central/enclosing articulation
```

Meru functions as the first central determination in the world-container. The surrounding named mountains begin the logic of circumferential structure. The term `samantataḥ` is important: the world now has an “around,” not merely a “below” and a “breadth.”

This produces a new spatial logic:

```text
below
    vertical support
        lateral expanse
            center and circumference
```

## 11. Interpretive Note

First-pass interpretation should remain structural. We do not yet need to decide the symbolic value of Meru or map it into Yoga, Sāṃkhya, or Hegel. The immediate function of the verse is simpler and stronger: the measured support becomes internally organized.

The verse introduces the transition from the foundation of the container-world into its first cosmographic differentiation. From this point forward, the cosmology will unfold as a layered and ringed order: mountains, seas, continents, hells, celestial bodies, gods, and temporal measures.

For Organon purposes, this is the beginning of placed world-structure:

```text
foundation-field
    → axial center
        → enclosing rings
```

## 12. OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

vak:VAkK_3_48 a vak:Karika ;
    rdfs:label "VAkK 3.48" ;
    vak:belongsToChapter vak:Lokanirdesa ;
    vak:belongsToBlock vak:VAK_3c ;
    vak:continuesFrom vak:VAkK_3_47 ;
    vak:hasTopic loka:MeruMountainSystem ;
    vak:describes loka:Meru , loka:Yugandhara , loka:Isadhara , loka:Khadiraka , loka:SudarsanaGiri .

loka:MeruMountainSystem a owl:Class ;
    rdfs:label "Meru mountain system" ;
    rdfs:comment "The first named mountain-structure within the container-world after the support-fields are measured." .

loka:CosmologicalMountain a owl:Class ;
    rdfs:label "cosmological mountain" ;
    rdfs:comment "A named mountain or range in the bhājanaloka structure." .

loka:Meru a loka:CosmologicalMountain ;
    rdfs:label "Meru" ;
    rdfs:comment "The central mountain in the cosmological world-structure." .

loka:Yugandhara a loka:CosmologicalMountain ;
    rdfs:label "Yugandhara" .

loka:Isadhara a loka:CosmologicalMountain ;
    rdfs:label "Īśādhāra" ;
    rdfs:comment "Source reading preserved; verify form in Pass 2." .

loka:Khadiraka a loka:CosmologicalMountain ;
    rdfs:label "Khadiraka" .

loka:SudarsanaGiri a loka:CosmologicalMountain ;
    rdfs:label "Sudarśana-giri" .

loka:surrounds a owl:ObjectProperty ;
    rdfs:label "surrounds" ;
    rdfs:comment "Circumferential relation in the Meru mountain system." .

loka:hasProportionalMeasure a owl:DatatypeProperty ;
    rdfs:label "has proportional measure" ;
    rdfs:range xsd:string .

loka:MeruMountainSystem loka:hasProportionalMeasure "triguṇa, all around; precise referent to be verified in Pass 2" .
```

## 13. Commit Note

```text
Add VAkK_3.48 first-pass analysis.

Continues VAK_3c container-world foundations.
Introduces Meru and the first named surrounding mountains after the measured wind/water/gold support-field.
Preserves source reading īśādhāraḥ while marking the mountain name for Pass 2 verification.
```
