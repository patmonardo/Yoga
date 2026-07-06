# VAkK_3.45 — Bhājanaloka: the Wind-Maṇḍala

## 1. Sanskrit — Devanāgarī

```sanskrit
तत्र भाजनलोकस्य संनिवेशमुशन्त्यधः ।
लक्षषोडशकोद्वेधमसंख्यं वायुमण्डलम् ॥ VAkK_3.45 ॥
```

## 2. Sanskrit — IAST

```iast
tatra bhājanalokasya saṃniveśam uśanty adhaḥ /
lakṣaṣoḍaśakodvedham asaṃkhyaṃ vāyumaṇḍalam // VAkK_3.45 //
```

## 3. Source Caution

The source reading is:

```iast
tatra bhājanalokasya saṃniveśamuśantyadhaḥ /
lakṣaṣoḍaśakodvedhamasaṃkhyaṃ vāyumaṇḍalam // VAkK_3.45 //
```

Sandhi has been lightly separated for analysis. The compound `lakṣaṣoḍaśakodvedham` is treated here as:

```iast
lakṣa-ṣoḍaśaka-udvedham
```

meaning “having an elevation/thickness of sixteen lakṣas.” This should be checked against Pradhan and the bhāṣya in Pass 2.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| tatra | tatra | there; in that context |
| bhājanalokasya | bhājana-lokasya | of the container-world; of the receptacle-world |
| saṃniveśam | saṃniveśam | arrangement, disposition, placement, configuration |
| uśanty | uśanti | they declare, they describe, they maintain |
| adhaḥ | adhaḥ | below, beneath |
| lakṣaṣoḍaśakodvedham | lakṣa-ṣoḍaśaka-udvedham | having a vertical extent of sixteen lakṣas |
| asaṃkhyam | asaṃkhyam | innumerable, incalculable, immeasurable |
| vāyumaṇḍalam | vāyu-maṇḍalam | wind-disk, wind-maṇḍala, wind-support-field |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| tatra | indeclinable | locative frame: “there / in that context” |
| bhājanalokasya | genitive singular masculine | qualifies `saṃniveśam`: “of the container-world” |
| saṃniveśam | accusative singular masculine | object of `uśanti`: “the arrangement” |
| uśanti | 3rd plural present | verbal predicate: “they declare / describe” |
| adhaḥ | indeclinable | spatial determination: “below” |
| lakṣa-ṣoḍaśaka-udvedham | accusative singular masculine/neuter compound | qualifies `vāyumaṇḍalam`: “with sixteen-lakṣa elevation” |
| asaṃkhyam | accusative singular masculine/neuter | qualifies `vāyumaṇḍalam`: “incalculable” |
| vāyumaṇḍalam | accusative singular neuter | appositional object: the first foundation described |

## 6. Literal Translation

There, they describe below the arrangement of the container-world: an incalculable wind-maṇḍala, having an elevation of sixteen lakṣas.

## 7. Philosophical Translation

At this point, the Kośa turns to the disposition of the world-container. Beneath it is posited the wind-maṇḍala: the first supporting field of the cosmological order, immeasurable in extent and vertically determined as sixteen lakṣas.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| bhājanaloka | container-world / receptacle-world | the outer world-field that supports beings and their experience |
| saṃniveśa | arrangement / configuration | determinate placement of the world-structure |
| adhaḥ | below | first spatial determination of the cosmological field |
| vāyumaṇḍala | wind-maṇḍala | foundational support-plane beneath the world-container |
| udvedha | elevation / vertical extent / thickness | quantified vertical determination |
| asaṃkhya | incalculable | measure pushed beyond ordinary enumeration |

## 9. Doctrinal Determination

VAkK_3.45 begins the explicit exposition of `bhājanaloka`, the container-world. The previous block described the internal field of conditioned human existence: dependent arising, contact, feeling, craving, appropriation, becoming, food, intermediate existence, death, and rebirth. This verse now shifts to the external support-field in which such embodied existence is situated.

The first determination of this container-world is not earth, mountain, sea, or continent, but `vāyumaṇḍala`: a wind-support. The world begins from a supporting force-field rather than from a visible object.

## 10. Logical Determination

```text
inner conditioned sequence
    → external container
        → foundational support-field
```

The logical movement is from:

```text
santāna / bhava / upapatti
    conditioned stream and rebirth
```

to:

```text
bhājanaloka / saṃniveśa
    arranged receptacle-world
```

This is the first explicit determination of world as container. The verse does not yet present the visible cosmos. It gives the beneath, the support, the invisible base. The world as appearance requires a prior support-field.

## 11. Interpretive Note

For first-pass purposes, `bhājanaloka` should not be reduced to mythology or physical geography. It is the outer support-structure of the Rational–Empirical Field. The Kośa has already shown how beings move through birth, death, contact, feeling, and nutriment. Now it shows the receptacle in which that conditioned existence is housed.

The important philosophical point is the transition:

```text
lived conditioned sequence
    → container-world
```

In Hegelian terms, this is the passage from determinate inner process into determinate Existence. In Organon terms, it is the first macro-container for the empirical field.

Yoga and Sāṃkhya correspondences should remain latent here. They belong to Pass 3, not to this first-pass kārikā file.

## 12. OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

vak:VAkK_3_45 a vak:Karika ;
    rdfs:label "VAkK 3.45" ;
    vak:belongsToChapter vak:Lokanirdesa ;
    vak:beginsBlock vak:VAK_3c ;
    vak:hasTopic loka:Bhajanaloka ;
    vak:describes loka:VayuMandala .

loka:Bhajanaloka a owl:Class ;
    rdfs:label "bhājanaloka" ;
    rdfs:comment "The container-world or receptacle-world that supports the field of embodied existence." .

loka:Samnivesa a owl:Class ;
    rdfs:label "saṃniveśa" ;
    rdfs:comment "Arrangement, configuration, or determinate placement of the container-world." .

loka:VayuMandala a owl:Class ;
    rdfs:label "vāyumaṇḍala" ;
    rdfs:comment "The wind-maṇḍala described as the foundational support-field beneath the container-world." .

loka:hasVerticalExtent a owl:DatatypeProperty ;
    rdfs:label "has vertical extent" ;
    rdfs:domain loka:VayuMandala ;
    rdfs:range xsd:string .

loka:isBelow a owl:ObjectProperty ;
    rdfs:label "is below" ;
    rdfs:comment "Spatial support relation in the cosmological arrangement." .

loka:VayuMandala vak:canonicalTranslation "wind-maṇḍala" ;
    loka:hasVerticalExtent "sixteen lakṣas" ;
    loka:isBelow loka:Bhajanaloka .
```

## 13. Commit Note

```text
Add VAkK_3.45 first-pass analysis.

Begins VAK_3c container-world block.
Establishes bhājanaloka as outer support-field and vāyumaṇḍala as first cosmological foundation.
Keeps Yoga/Sāṃkhya/Hegel correspondences restrained for later Pass 3.
```
