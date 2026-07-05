# VAK_3.51 — Bhājanaloka: Mountain Heights and the First Inner Sea

## 1. Sanskrit — Devanāgarī

```sanskrit
अर्धार्धहानिरष्टासु समोच्छ्रायघनाश्च ते ।
शीताः सप्तान्तराण्येषामाद्याशीतिसहस्रिका ॥ VAkK_3.51 ॥
```

## 2. Sanskrit — IAST

```iast
ardhārdhahānir aṣṭāsu samocchrāyaghanāś ca te /
śītāḥ saptāntarāṇy eṣām ādyāśītisahasrikā // VAkK_3.51 //
```

## 3. Source Caution

The source reading is:

```iast
ardhārdhahāniraṣṭāsu samocchrāyaghanāśca te /
śītāḥ saptāntarāṇyeṣāṃ ādyāśītisahasrikā // VAkK_3.51 //
```

Sandhi has been lightly separated for analysis. The term `aṣṭāsu` appears to refer to the eight mountains counted with Meru, or the eight height-determinations in the sequence. The exact referent should be checked against Pradhan and the bhāṣya in Pass 2.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| ardhārdhahāniḥ | ardha-ardha-hāniḥ | reduction by half and half; successive halving |
| aṣṭāsu | aṣṭāsu | among eight; in eight cases |
| samocchrāyaghanāḥ | sama-ucchrāya-ghanāḥ | having equal height and thickness/massiveness |
| ca | ca | and |
| te | te | they |
| śītāḥ | śītāḥ | cold; cool; here cold seas/waters |
| sapta | sapta | seven |
| antarāṇi | antarāṇi | intervals, spaces between |
| eṣām | eṣām | of these |
| ādyā | ādyā | the first |
| aśītisahasrikā | aśīti-sahasrikā | eighty-thousand-fold / eighty thousand in measure |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| ardha-ardha-hāniḥ | nominative singular feminine | predicate-noun: “there is successive halving” |
| aṣṭāsu | locative plural feminine | locative domain: “among the eight” |
| sama-ucchrāya-ghanāḥ | nominative plural masculine | qualifies `te`: “they have equal height and thickness” |
| te | nominative plural masculine | refers to the mountains |
| śītāḥ | nominative plural feminine | cold waters/seas; subject of the second hemistich |
| sapta antarāṇi | nominative/accusative plural neuter phrase | seven intervening spaces |
| eṣām | genitive plural | “of these,” referring to the mountains |
| ādyā | nominative singular feminine | the first of the cold intervals/seas |
| aśīti-sahasrikā | nominative singular feminine | numerical predicate: “eighty thousand” |

## 6. Literal Translation

Among the eight there is a reduction by half and half; and they are equal in height and thickness. The seven cold intervals between them: the first is eighty thousand.

## 7. Philosophical Translation

The mountain sequence is measured by progressive halving, while each mountain is internally equal in height and mass. Between them are seven cold intervening seas; the first of these is eighty thousand in measure.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| ardha-ardha-hāni | successive halving | proportional reduction through the mountain sequence |
| aṣṭa | eight | the measured mountain series, likely Meru plus seven golden mountains |
| samocchrāya | equal height | vertical equality within each mountain’s own measure |
| ghana | thickness / massiveness / solidity | dimensional density of the mountains |
| śīta | cold / cool | cold inner sea or water-interval |
| antara | interval / intervening space | space between mountains |
| aśīti-sahasrika | eighty-thousand in measure | measure of the first interval/sea |

## 9. Doctrinal Determination

VAkK_3.51 continues the measured account of the Meru mountain system. VAkK_3.50 measured Meru as eighty thousand submerged and eighty thousand above water. This verse now extends measure to the surrounding mountain sequence.

The rule is:

```text
successive halving
```

The mountains diminish by halves, while each retains equality of height and thickness. Between them are seven cold seas or intervals, the first being eighty thousand.

## 10. Logical Determination

```text
central height
    → proportional reduction
        → intervallic differentiation
```

The world-structure now becomes serial. It is not merely a center and boundary, but an ordered progression. The mountain-rings are differentiated by ratio, and the spaces between them become determinate intervals.

This introduces a logic of proportion:

```text
Meru
    → half
        → half again
            → serially ordered rings
```

and a logic of interval:

```text
mountain
    → sea-interval
        → mountain
```

## 11. Interpretive Note

This verse is especially important for the first-pass spine because it shows that the Kośa’s cosmology is not arbitrary enumeration. It is a measured field of proportions and intervals. The container-world is becoming an ordered structure through height, thickness, reduction, and intervening waters.

For Organon purposes, the key first-pass determination is:

```text
world-container as serial proportional field
```

Pass 2 should verify whether `aṣṭāsu` explicitly includes Meru plus the seven golden mountains, and how the bhāṣya glosses the seven cold intervals.

## 12. OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

vak:VAK_3_51 a vak:Karika ;
    rdfs:label "VAK 3.51" ;
    vak:sourceSiglum "VAkK_3.51" ;
    vak:belongsToChapter vak:Lokanirdesa ;
    vak:belongsToBlock vak:VAK_3c ;
    vak:continuesFrom vak:VAK_3_50 ;
    vak:hasTopic loka:MountainProportionAndInnerSeas ;
    vak:describes loka:SuccessiveHalving , loka:ColdInnerSeaInterval .

loka:SuccessiveHalving a owl:Class ;
    rdfs:label "ardhārdha-hāni" ;
    rdfs:comment "Successive reduction by halves across the mountain sequence." .

loka:ColdInnerSeaInterval a owl:Class ;
    rdfs:label "śīta antara" ;
    rdfs:comment "A cold interval or sea between cosmological mountains." .

loka:hasReductionRule a owl:DatatypeProperty ;
    rdfs:label "has reduction rule" ;
    rdfs:range xsd:string .

loka:hasFirstIntervalMeasure a owl:DatatypeProperty ;
    rdfs:label "has first interval measure" ;
    rdfs:range xsd:string .

loka:MountainRingSystem loka:hasReductionRule "ardhārdha-hāni" ;
    loka:hasFirstIntervalMeasure "aśīti-sahasrika" .
```

## 13. Commit Note

```text
Add VAK_3.51 first-pass analysis.

Continues VAK_3c container-world block.
Adds proportional halving of the eight mountain sequence and introduces the seven cold intervals/seas.
Uses uppercase VAK artifact filename while preserving VAkK as textual source siglum.
Marks aṣṭāsu and śīta-antara interpretation for Pass 2 verification.
```
