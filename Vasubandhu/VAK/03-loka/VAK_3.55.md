# VAK_3.55 — Bhājanaloka: Godānīya and Kuru as Circular and Square Continents

## 1. Sanskrit — Devanāgarī

```sanskrit
गोदानीयः सहस्राणि सप्त सार्धानि मण्डलः ।
सार्धे द्वे मध्यमस्याष्टौ चतुरस्रः कुरुः समः ॥ VAkK_3.55 ॥
```

## 2. Sanskrit — IAST

```iast
godānīyaḥ sahasrāṇi sapta sārdhāni maṇḍalaḥ /
sārdhe dve madhyamasya aṣṭau caturasraḥ kuruḥ samaḥ // VAkK_3.55 //
```

## 3. Source Caution

The source reading is:

```iast
godānīyaḥ sahasrāṇi sapta sārdhāni maṇḍalaḥ /
sārdhe dve madhyamasya aṣṭau caturasraḥ kuruḥ samaḥ // VAkK_3.55 //
```

Sandhi has been lightly separated:

```iast
godānīyaḥ sahasrāṇi sapta sārdhāni maṇḍalaḥ /
sārdhe dve madhyamasya aṣṭau caturasraḥ kuruḥ samaḥ //
```

The expression `sārdhe dve madhyamasya aṣṭau` is compact and should be checked against Pradhan and the bhāṣya in Pass 2. First-pass analysis treats the verse as completing the four-continent shape sequence: Godānīya is circular, while Kuru is square and equal-sided.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| godānīyaḥ | godānīyaḥ | Godānīya, western continent |
| sahasrāṇi | sahasrāṇi | thousands |
| sapta | sapta | seven |
| sārdhāni | sārdhāni | with a half; half-added |
| maṇḍalaḥ | maṇḍalaḥ | circular, round, disk-shaped |
| sārdhe | sārdhe | in/with a half-added measure; exact syntax to verify |
| dve | dve | two |
| madhyamasya | madhyamasya | of the middle; exact referent to verify |
| aṣṭau | aṣṭau | eight |
| caturasraḥ | caturasraḥ | square, four-cornered |
| kuruḥ | kuruḥ | Kuru, northern continent |
| samaḥ | samaḥ | equal, even, symmetrical |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| godānīyaḥ | nominative singular masculine | subject: Godānīya |
| sahasrāṇi sapta sārdhāni | numerical phrase | seven thousand with a half; provisionally seven thousand five hundred |
| maṇḍalaḥ | nominative singular masculine | predicate: circular/round |
| sārdhe dve | numerical phrase | two and a half; exact role to be verified |
| madhyamasya | genitive singular masculine/neuter | “of the middle”; referent to be verified |
| aṣṭau | numeral | eight; exact attachment to be verified |
| caturasraḥ | nominative singular masculine | predicate: square |
| kuruḥ | nominative singular masculine | subject: Kuru |
| samaḥ | nominative singular masculine | predicate: equal, symmetrical |

## 6. Literal Translation

Godānīya is seven thousand and a half, circular. Two and a half of the middle, eight; Kuru is square and equal.

## 7. Philosophical Translation

The continent sequence is completed by Godānīya and Kuru. Godānīya is given as a circular continent with its measure. Kuru is described as square and equal, presenting a symmetrical land-form within the four-continent system.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| Godānīya | Godānīya | western continent in the four-continent system |
| Kuru | Kuru | northern continent in the four-continent system |
| maṇḍala | circular / round / disk-shaped | shape determination of Godānīya |
| caturasra | square / four-cornered | shape determination of Kuru |
| sama | equal / symmetrical | equality of sides or balanced form |
| sahasra | thousand | numerical unit |
| sārdha | with a half | fractional augmentation of a measure |
| madhyama | middle | compact measure-term requiring Pass 2 verification |

## 9. Doctrinal Determination

VAkK_3.55 completes the four-continent morphology begun with Jambūdvīpa and Prāgvideha.

The sequence now stands:

```text
Jambūdvīpa
    cart-shaped / three-sided

Prāgvideha
    half-moon-shaped

Godānīya
    circular

Kuru
    square and equal
```

The continent-system is therefore a geometry of differentiated land-forms. Each dvīpa is defined not merely by position but by shape and measure.

## 10. Logical Determination

```text
continent morphology
    → cart-form
        → half-moon form
            → circular form
                → square/equal form
```

The four-continent system is now a set of determinate geometries. The world-container has moved from foundation and boundary to region-bearing form.

The logical importance of this verse is closure of the morphology sequence:

```text
four directions
    → four dvīpas
        → four shapes
```

## 11. Interpretive Note

First-pass work should keep the arithmetic restrained here. The stable result is morphological: Godānīya is `maṇḍalaḥ`, circular, and Kuru is `caturasraḥ samaḥ`, square and equal.

The exact handling of the compact numerical sequence belongs to Pass 2, where the bhāṣya can clarify the measure-relations. For now, this file records the continent-shape closure and marks the measure-expression for verification.

For Organon purposes, VAkK_3.55 completes the transition:

```text
support-field
    → bounded cosmological field
        → continent regions
            → determinate geometrical forms
```

## 12. OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_55 a vak:Karika ;
    rdfs:label "VAK 3.55" ;
    vak:sourceSiglum "VAkK_3.55" ;
    vak:belongsToChapter vak:Lokanirdesa ;
    vak:belongsToBlock vak:VAK_3c ;
    vak:continuesFrom vak:VAK_3_54 ;
    vak:hasTopic loka:GodaniyaAndKuru ;
    vak:describes loka:Godaniya , loka:Kuru , loka:GodaniyaShape , loka:KuruShape .

loka:Godaniya a loka:Dvipa ;
    rdfs:label "Godānīya" ;
    rdfs:comment "The western continent, described as circular." .

loka:Kuru a loka:Dvipa ;
    rdfs:label "Kuru" ;
    rdfs:comment "The northern continent, described as square and equal." .

loka:GodaniyaShape a owl:Class ;
    rdfs:label "Godānīya shape" ;
    rdfs:comment "Godānīya as maṇḍala, circular or disk-shaped." .

loka:KuruShape a owl:Class ;
    rdfs:label "Kuru shape" ;
    rdfs:comment "Kuru as caturasra and sama, square and equal." .

loka:Godaniya loka:hasShape "maṇḍala" ;
    loka:hasMeasureNote "sapta sahasrāṇi sārdhāni; verify in Pass 2" .

loka:Kuru loka:hasShape "caturasra; sama" ;
    loka:hasMeasureNote "sārdhe dve madhyamasya aṣṭau; verify in Pass 2" .
```

## 13. Commit Note

```text
Add VAK_3.55 first-pass analysis.

Completes the four-continent morphology sequence.
Adds Godānīya as circular and Kuru as square/equal.
Uses uppercase VAK artifact filename while preserving VAkK as textual source siglum.
Marks compact numerical expressions for Pass 2 bhāṣya verification.
```
