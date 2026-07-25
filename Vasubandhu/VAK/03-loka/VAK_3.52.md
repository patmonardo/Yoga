# VAK_3.52 — Bhājanaloka: Inner Sea, Remaining Cold Seas, and the Outer Ocean

## 1. Sanskrit — Devanāgarī

```sanskrit
आभ्यन्तरः समुद्रोऽसौ त्रिगुणः स तु पार्श्वतः ।
अर्धार्धेनापराः शीताः शेषं बाह्यो महोदधेः ॥ VAkK_3.52 ॥
```

## 2. Sanskrit — IAST

```iast
ābhyantaraḥ samudro 'sau triguṇaḥ sa tu pārśvataḥ /
ardhārdhenāparāḥ śītāḥ śeṣaṃ bāhyo mahodadheḥ // VAkK_3.52 //
```

## 3. Source Caution

The source reading is:

```iast
ābhyantaraḥ samudro 'sau triguṇaḥ sa tu pārśvataḥ /
ardhārdhenāparāḥ śītāḥ śeṣaṃ bāhyo mahodadheḥ // VAkK_3.52 //
```

Sandhi has been lightly separated:

```iast
ābhyantaraḥ samudraḥ asau triguṇaḥ saḥ tu pārśvataḥ /
ardha-ardhena aparāḥ śītāḥ śeṣaṃ bāhyaḥ mahodadheḥ //
```

The precise syntactic relation of `śeṣaṃ bāhyo mahodadheḥ` should be checked in Pass 2. First-pass analysis takes it to mean that the remaining expanse belongs to, or is constituted by, the outer great ocean.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| ābhyantaraḥ | ābhyantaraḥ | inner, internal |
| samudro 'sau | samudraḥ asau | that sea |
| triguṇaḥ | tri-guṇaḥ | threefold, triple |
| sa tu | saḥ tu | but that; as for that |
| pārśvataḥ | pārśvataḥ | at the side, laterally, by flank/side |
| ardhārdhena | ardha-ardhena | by half and half; by successive halving |
| aparāḥ | aparāḥ | the others, the remaining ones |
| śītāḥ | śītāḥ | cold seas/waters |
| śeṣam | śeṣam | remainder, what remains |
| bāhyaḥ | bāhyaḥ | outer, external |
| mahodadheḥ | mahā-udadheḥ | of the great ocean |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| ābhyantaraḥ | nominative singular masculine | qualifies `samudraḥ`: “inner” |
| samudraḥ asau | nominative singular masculine phrase | subject: “that sea” |
| tri-guṇaḥ | nominative singular masculine | predicate: “threefold / triple” |
| pārśvataḥ | indeclinable | lateral or side-measure relation |
| ardha-ardhena | instrumental singular compound | means of reduction: “by half and half” |
| aparāḥ śītāḥ | nominative plural feminine | the other cold seas |
| śeṣam | nominative/accusative singular neuter | remainder |
| bāhyaḥ | nominative singular masculine | outer; likely qualifies an implied ocean/sea |
| mahā-udadheḥ | genitive singular masculine | “of the great ocean” |

## 6. Literal Translation

That inner sea is threefold at the side. The other cold seas are by half and half. The remainder is the outer great ocean.

## 7. Philosophical Translation

The first inner sea is determined laterally as triple. The remaining cold seas proceed by successive halving. What remains beyond this ordered inner sequence is the outer great ocean.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| ābhyantara | inner | internal to the mountain-ring system |
| samudra | sea | water-interval between cosmological mountains |
| triguṇa | threefold / triple | proportional side-measure of the inner sea |
| pārśvataḥ | laterally / from the side | side-measure determination |
| ardha-ardha | half and half | successive proportional diminution |
| aparāḥ śītāḥ | other cold seas | remaining cold sea-intervals after the first |
| śeṣa | remainder | what is left after the measured inner sequence |
| bāhya mahodadhi | outer great ocean | external ocean beyond the mountain-ring and inner-sea system |

## 9. Doctrinal Determination

VAkK_3.52 completes the immediate measurement of the inner seas introduced in VAkK_3.51. The first inner sea is described as threefold laterally; the remaining cold seas diminish by halves. Beyond the series lies the outer great ocean.

The sequence is:

```text
first inner sea
    → triple lateral measure
        → remaining cold seas by halving
            → outer great ocean
```

This completes the structural block begun with the mountain heights and intervals.

## 10. Logical Determination

```text
center
    → mountain-rings
        → inner intervals
            → diminishing cold seas
                → outer oceanic remainder
```

The world-container receives a double water-structure: ordered inner seas and an outer great ocean. The inner seas are serial and proportional; the outer ocean is the remaining expanse beyond that articulated series.

This gives a clean distinction:

```text
interior measure
    vs.
outer remainder
```

## 11. Interpretive Note

VAkK_3.52 is a completion verse for the first VAK_3c sub-block. With it, the Kośa has established:

```text
wind support
water/gold support
lateral extent
Meru
seven golden mountains
outer iron Cakravāḍa
Meru’s submerged and emergent measure
mountain-halving sequence
inner cold seas
outer great ocean
```

This completes the foundational container-world arrangement before the text turns to Jambūdvīpa and the other continents in VAkK_3.53.

For Organon purposes, the verse marks the emergence of the outer remainder as oceanic limit: the measured interior gives way to the unarticulated external expanse.

## 12. OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

vak:VAK_3_52 a vak:Karika ;
    rdfs:label "VAK 3.52" ;
    vak:sourceSiglum "VAkK_3.52" ;
    vak:belongsToChapter vak:Lokanirdesa ;
    vak:belongsToBlock vak:VAK_3c ;
    vak:continuesFrom vak:VAK_3_51 ;
    vak:hasTopic loka:InnerAndOuterSeas ;
    vak:describes loka:InnerSea , loka:ColdSeaSeries , loka:OuterGreatOcean .

loka:InnerSea a owl:Class ;
    rdfs:label "ābhyantara samudra" ;
    rdfs:comment "The inner sea in the mountain-ring system, determined as threefold laterally." .

loka:ColdSeaSeries a owl:Class ;
    rdfs:label "śītāḥ aparāḥ" ;
    rdfs:comment "The remaining cold seas, determined by successive halving." .

loka:OuterGreatOcean a owl:Class ;
    rdfs:label "bāhya mahodadhi" ;
    rdfs:comment "The outer great ocean or oceanic remainder beyond the measured inner series." .

loka:hasLateralMeasureRule a owl:DatatypeProperty ;
    rdfs:label "has lateral measure rule" ;
    rdfs:range xsd:string .

loka:hasRemainderAs a owl:ObjectProperty ;
    rdfs:label "has remainder as" .

loka:InnerSea loka:hasLateralMeasureRule "triguṇaḥ pārśvataḥ" .
loka:ColdSeaSeries loka:hasReductionRule "ardhārdhena" .
loka:MountainRingSystem loka:hasRemainderAs loka:OuterGreatOcean .
```

## 13. Commit Note

```text
Add VAK_3.52 first-pass analysis.

Completes the immediate mountain-ring and inner-sea measurement sequence.
Adds the first inner sea as laterally triple, remaining cold seas by halving, and the outer great ocean as remainder.
Uses uppercase VAK artifact filename while preserving VAkK as textual source siglum.
Marks śeṣaṃ bāhyo mahodadheḥ for Pass 2 syntactic verification.
```
