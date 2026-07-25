# VAK_3.53 — Bhājanaloka: Jambūdvīpa and Its Cart-Shaped Measure

## 1. Sanskrit — Devanāgarī

```sanskrit
लक्षत्रयं सहस्राणि विंशतिर्द्वे च तत्र तु ।
जम्बूद्वीपो द्विसाहस्रस्त्रिपार्श्वः शकटाकृतिः ॥ VAkK_3.53 ॥
```

## 2. Sanskrit — IAST

```iast
lakṣatrayaṃ sahasrāṇi viṃśatir dve ca tatra tu /
jambūdvīpo dvisāhasras tripārśvaḥ śakaṭākṛtiḥ // VAkK_3.53 //
```

## 3. Source Caution

The source reading is:

```iast
lakṣatrayaṃ sahasrāṇi viṃśatirdve ca tatra tu /
jambūdvīpo dvisāhasrastripārśvaḥ śakaṭākṛtiḥ // VAkK_3.53 //
```

Sandhi has been lightly separated for analysis:

```iast
lakṣa-trayam sahasrāṇi viṃśatiḥ dve ca tatra tu /
jambū-dvīpaḥ dvi-sāhasraḥ tri-pārśvaḥ śakaṭa-ākṛtiḥ //
```

The opening numerical expression likely continues the measure of the outer ocean or available field from VAkK_3.52. Its precise syntactic attachment should be checked against Pradhan and the bhāṣya in Pass 2.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| lakṣatrayam | lakṣa-trayam | three lakṣas |
| sahasrāṇi | sahasrāṇi | thousands |
| viṃśatiḥ | viṃśatiḥ | twenty |
| dve | dve | two |
| ca | ca | and |
| tatra | tatra | there, in that world-field |
| tu | tu | but, now |
| jambūdvīpaḥ | jambū-dvīpaḥ | Jambūdvīpa, the southern continent/island |
| dvisāhasraḥ | dvi-sāhasraḥ | two-thousand in measure |
| tripārśvaḥ | tri-pārśvaḥ | three-sided, having three sides |
| śakaṭākṛtiḥ | śakaṭa-ākṛtiḥ | cart-shaped, wagon-shaped |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| lakṣa-trayam | nominative/accusative singular neuter | numerical measure: three lakṣas |
| sahasrāṇi viṃśatiḥ dve ca | numerical phrase | twenty-two thousand; exact attachment to be verified |
| tatra tu | adverbial-particle phrase | introduces the next determination within the world-field |
| jambū-dvīpaḥ | nominative singular masculine | subject of the second hemistich |
| dvi-sāhasraḥ | nominative singular masculine | numerical predicate: two-thousand |
| tri-pārśvaḥ | nominative singular masculine | shape predicate: three-sided |
| śakaṭa-ākṛtiḥ | nominative singular masculine/feminine compound | form predicate: cart-shaped |

## 6. Literal Translation

There, however, three lakṣas and twenty-two thousand. Jambūdvīpa is two-thousand, three-sided, and cart-shaped.

## 7. Philosophical Translation

After the inner seas and outer ocean have been determined, the text turns to the continent-field. Jambūdvīpa is introduced as a measured and shaped land-region: two thousand in measure, three-sided, and cart-shaped.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| lakṣa | hundred-thousand | large-scale cosmological measure |
| sahasra | thousand | numerical measure |
| Jambūdvīpa | Jambūdvīpa | southern continent/island in the four-continent system |
| dvīpa | island / continent / region-bearing landmass | articulated land-region within the container-world |
| dvi-sāhasra | two-thousand | measure assigned to Jambūdvīpa |
| tri-pārśva | three-sided | shape determination |
| śakaṭākṛti | cart-shaped | morphological determination of the continent |

## 9. Doctrinal Determination

VAkK_3.53 begins the explicit continent-measure section. The prior verses built the support-field, Meru, mountain-rings, inner seas, and outer ocean. Now the `dvīpa` system begins with Jambūdvīpa.

The important turn is:

```text
mountains and seas
    → land-regions / dvīpas
```

Jambūdvīpa is not merely named; it is measured and shaped. The continent appears as a determinate region within the already bounded and measured container-world.

## 10. Logical Determination

```text
outer oceanic field
    → continent-region
        → measure
            → shape
```

The world-container now shifts from support and enclosure to inhabited or region-bearing land. The logic is no longer only vertical and circumferential. It becomes morphological: the dvīpa has a form.

The verse introduces the logic of land-form:

```text
region
    → side-structure
        → shape-configuration
```

## 11. Interpretive Note

This verse begins a new sub-block within the expanded VAK_3c thread. VAkK_3.45–3.52 established the container foundation; VAkK_3.53 begins the articulation of the continent system.

The first continent is Jambūdvīpa, and its form is `śakaṭākṛti`, cart-shaped. This is a strong first-pass sign that the Kośa’s cosmology proceeds by determinate geometry: measures, sides, and shapes.

The opening numerical phrase should be left somewhat restrained until Pass 2, since its exact attachment needs the bhāṣya.

## 12. OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

vak:VAK_3_53 a vak:Karika ;
    rdfs:label "VAK 3.53" ;
    vak:sourceSiglum "VAkK_3.53" ;
    vak:belongsToChapter vak:Lokanirdesa ;
    vak:belongsToBlock vak:VAK_3c ;
    vak:continuesFrom vak:VAK_3_52 ;
    vak:hasTopic loka:Jambudvipa ;
    vak:describes loka:JambudvipaMeasure , loka:JambudvipaShape .

loka:Dvipa a owl:Class ;
    rdfs:label "dvīpa" ;
    rdfs:comment "Island, continent, or region-bearing landmass in the cosmological world-field." .

loka:Jambudvipa a loka:Dvipa ;
    rdfs:label "Jambūdvīpa" ;
    rdfs:comment "The first continent-region described in the continent-measure sequence." .

loka:JambudvipaMeasure a owl:Class ;
    rdfs:label "Jambūdvīpa measure" ;
    rdfs:comment "The two-thousand measure assigned to Jambūdvīpa in VAkK_3.53." .

loka:JambudvipaShape a owl:Class ;
    rdfs:label "Jambūdvīpa shape" ;
    rdfs:comment "Jambūdvīpa as three-sided and cart-shaped." .

loka:hasMeasure a owl:DatatypeProperty ;
    rdfs:label "has measure" ;
    rdfs:range xsd:string .

loka:hasShape a owl:DatatypeProperty ;
    rdfs:label "has shape" ;
    rdfs:range xsd:string .

loka:Jambudvipa loka:hasMeasure "dvi-sāhasra" ;
    loka:hasShape "tri-pārśva; śakaṭākṛti" .
```

## 13. Commit Note

```text
Add VAK_3.53 first-pass analysis.

Begins the continent-measure sequence after the mountain-ring and ocean foundation.
Introduces Jambūdvīpa as two-thousand, three-sided, and cart-shaped.
Uses uppercase VAK artifact filename while preserving VAkK as textual source siglum.
Marks the opening numerical expression for Pass 2 syntactic verification.
```
