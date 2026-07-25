# VAK_3.57 — Bhājanaloka: Himavān, Gandhamādana, and the Northern Lake

## 1. Sanskrit — Devanāgarī

```sanskrit
इहोत्तरेण कीटाद्रि नवकाद्धिमवांस्ततः ।
पञ्चाशद्विस्तृतायामं सरोऽर्वाग्गन्धमादनात् ॥ VAkK_3.57 ॥
```

## 2. Sanskrit — IAST

```iast
ihottareṇa kīṭādri navakād dhimavān tataḥ /
pañcāśadvistṛtāyāmaṃ saro 'rvāg gandhamādanāt // VAkK_3.57 //
```

## 3. Source Caution

The source reading is:

```iast
ihottareṇa kīṭādri navakāddhimavān tataḥ /
pañcāśadvistṛtāyāmaṃ saro 'rvāggandhamādanāt // VAkK_3.57 //
```

Sandhi has been lightly separated:

```iast
iha uttareṇa kīṭādri navakāt himavān tataḥ /
pañcāśat-vistṛta-āyāmaṃ saraḥ arvāk gandhamādanāt //
```

The expression `kīṭādri navakāt` is difficult in the present source and should be checked against Pradhan and the bhāṣya in Pass 2. First-pass work preserves the source reading and treats the verse as locating Himavān and a fifty-by-fifty lake on this side of Gandhamādana.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| ihottareṇa | iha uttareṇa | here, to the north |
| kīṭādri | kīṭa-adri / kīṭādri | mountain-name or mountain-class; verify |
| navakāt | navakāt | from the set of nine; after nine; verify |
| himavān | himavān | Himavān, Himalayan mountain-region |
| tataḥ | tataḥ | then, thereafter |
| pañcāśadvistṛtāyāmam | pañcāśat-vistṛta-āyāmam | fifty in breadth and length |
| saraḥ | saraḥ | lake |
| arvāk | arvāk | on this side of, before, southward of |
| gandhamādanāt | gandhamādanāt | from / before Gandhamādana mountain |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| iha uttareṇa | adverbial phrase | locates the described region “to the north here” |
| kīṭādri navakāt | ablative/compound phrase | source expression; likely “after/from the nine Kīṭa mountains,” to be verified |
| himavān | nominative singular masculine | subject or located mountain: Himavān |
| tataḥ | indeclinable | sequential connector: “then / thereafter” |
| pañcāśat-vistṛta-āyāmam | accusative singular neuter compound | qualifies `saraḥ`: “fifty in breadth and length” |
| saraḥ | nominative/accusative singular neuter | lake |
| arvāk gandhamādanāt | ablative phrase | “on this side of Gandhamādana” |

## 6. Literal Translation

Here, to the north, after the nine Kīṭa mountains, is Himavān; then a lake, fifty in breadth and length, on this side of Gandhamādana.

## 7. Philosophical Translation

After the continent and intermediate-island system, the text locates a northern mountain-lake complex: Himavān appears beyond a set of nine mountains, and before Gandhamādana lies a lake measured as fifty in both breadth and length.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| iha uttareṇa | here to the north | northern orientation within the Jambūdvīpa field |
| kīṭādri | Kīṭa mountain / mountain-set | source reading requiring Pass 2 verification |
| navaka | set of nine | serial mountain grouping |
| Himavān | Himavān | northern mountain-region |
| saraḥ | lake | measured lake-region |
| pañcāśat | fifty | measure of breadth and length |
| vistṛta | breadth / width | horizontal extension |
| āyāma | length | longitudinal extension |
| Gandhamādana | Gandhamādana | mountain beyond/relative to the lake |
| arvāk | on this side of | relative locative relation |

## 9. Doctrinal Determination

VAkK_3.57 shifts from the principal and intermediate dvīpa-system to a more specific regional complex: northern mountains and a measured lake. The field is no longer only continent morphology; it is now detailed geographic placement within or relative to the continent-system.

The stable first-pass sequence is:

```text
northward orientation
    → mountain-series
        → Himavān
            → measured lake
                → Gandhamādana boundary/reference
```

## 10. Logical Determination

```text
continent-field
    → regional orientation
        → named mountains
            → measured lake
```

The verse introduces a finer level of placement. The container-world has already received support, mountains, seas, continents, and intermediate islands. Now individual named regional structures appear in sequence.

The important logical transition is:

```text
dvīpa morphology
    → intra-dvīpa / regional geography
```

## 11. Interpretive Note

This verse needs Pass 2 care. The compound or sequence `kīṭādri navakāt` is not yet secure in this source, and the precise relationship among the nine mountains, Himavān, the lake, and Gandhamādana should be checked in the bhāṣya.

For first-pass purposes, however, the verse clearly marks a shift into more detailed placement. The lake is measured by two dimensions, breadth and length, and it is located relative to Gandhamādana. This continues the Kośa’s dominant pattern: every world-region is determined through orientation, measure, and relation.

## 12. OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_57 a vak:Karika ;
    rdfs:label "VAK 3.57" ;
    vak:sourceSiglum "VAkK_3.57" ;
    vak:belongsToChapter vak:Lokanirdesa ;
    vak:belongsToBlock vak:VAK_3c ;
    vak:continuesFrom vak:VAK_3_56 ;
    vak:hasTopic loka:NorthernMountainLakeComplex ;
    vak:describes loka:Himavan , loka:Gandhamadana , loka:MeasuredLake .

loka:NorthernMountainLakeComplex a owl:Class ;
    rdfs:label "northern mountain-lake complex" ;
    rdfs:comment "The region described through Himavān, a measured lake, and Gandhamādana in VAkK_3.57." .

loka:Himavan a loka:CosmologicalMountain ;
    rdfs:label "Himavān" .

loka:Gandhamadana a loka:CosmologicalMountain ;
    rdfs:label "Gandhamādana" .

loka:MeasuredLake a owl:Class ;
    rdfs:label "saraḥ" ;
    rdfs:comment "A lake measured as fifty in breadth and length, located on this side of Gandhamādana." .

loka:hasBreadth a owl:DatatypeProperty ;
    rdfs:label "has breadth" .

loka:hasLength a owl:DatatypeProperty ;
    rdfs:label "has length" .

loka:isThisSideOf a owl:ObjectProperty ;
    rdfs:label "is this side of" .

loka:MeasuredLake loka:hasBreadth "pañcāśat" ;
    loka:hasLength "pañcāśat" ;
    loka:isThisSideOf loka:Gandhamadana .
```

## 13. Commit Note

```text
Add VAK_3.57 first-pass analysis.

Moves from dvīpa and antaradvīpa layout to northern mountain-lake placement.
Preserves the difficult source sequence kīṭādri navakāt for Pass 2 verification.
Adds Himavān, a fifty-by-fifty lake, and Gandhamādana as relative regional determinations.
```
