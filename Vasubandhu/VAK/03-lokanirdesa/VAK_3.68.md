# VAK_3.68 — Deva-World Summit: Pleasure-Grounds, Pārijāta, and Sudharmā

## 1. Sanskrit — Devanāgarī

```sanskrit
विंशत्यन्तरितान्येषां सुभूमीनि चतुर्दिशम् ।
पूर्वोत्तरे पारिजातः सुधर्मा दक्षिणावरे ॥ VAkK_3.68 ॥
```

## 2. Sanskrit — IAST

```iast
viṃśatyantaritāny eṣāṃ subhūmīni caturdiśam /
pūrvottare pārijātaḥ sudharmā dakṣiṇāvare // VAkK_3.68 //
```

## 3. Source Caution

The source reading is:

```iast
viṃśatyantaritānyeṣāṃ subhūmīni caturdiśam /
pūrvottare pārijātaḥ sudharmā dakṣiṇāvare // VAkK_3.68 //
```

Sandhi has been lightly separated:

```iast
viṃśati-antaritāni eṣām su-bhūmīni catur-diśam /
pūrva-uttare pārijātaḥ sudharmā dakṣiṇa-avare //
```

`subhūmi` is provisionally translated as “pleasant ground” or “beautiful ground.” `dakṣiṇāvara` is read as the southern-western / south-western side; the exact directional interpretation should be checked against the bhāṣya.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| viṃśatyantaritāni | viṃśati-antaritāni | separated by twenty; at intervals of twenty |
| eṣām | eṣām | of these; of the gardens / city-field features |
| subhūmīni | su-bhūmīni | pleasant grounds, beautiful grounds |
| caturdiśam | catur-diśam | in the four directions |
| pūrvottare | pūrva-uttare | in the north-east |
| pārijātaḥ | pārijātaḥ | the Pārijāta tree |
| sudharmā | sudharmā | Sudharmā; assembly hall or divine hall |
| dakṣiṇāvare | dakṣiṇa-avare | in the south-west / southern-lower quarter; provisional |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| viṃśati-antaritāni | nominative/accusative plural neuter | qualifies `su-bhūmīni`: separated by twenty |
| eṣām | genitive plural | of these, referring to the previously named deva-garden complex |
| su-bhūmīni | nominative/accusative plural neuter | subject: pleasant grounds |
| catur-diśam | adverbial accusative / compound | in the four directions |
| pūrva-uttare | locative singular | in the north-east |
| pārijātaḥ | nominative singular masculine | the Pārijāta tree is located there |
| sudharmā | nominative singular feminine | Sudharmā hall / assembly-place |
| dakṣiṇa-avare | locative singular | in the south-west; provisional |

## 6. Literal Translation

Their pleasant grounds, separated by twenty, are in the four directions. In the north-east is the Pārijāta; Sudharmā is in the south-west.

## 7. Philosophical Translation

The divine city-field is completed by pleasant grounds arranged in the four directions, spaced by intervals of twenty. The Pārijāta tree stands in the north-east, and Sudharmā, the divine hall, stands in the south-west.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| viṃśati | twenty | spacing interval |
| antarita | separated / spaced | marks measured distribution |
| su-bhūmi | pleasant ground / beautiful ground | refined enjoyment-space |
| catur-diś | four directions | directional distribution |
| pūrvottara | north-east | inter-cardinal location |
| Pārijāta | Pārijāta tree | divine tree; marker of the deva pleasure-field |
| Sudharmā | Sudharmā hall | divine assembly hall / dharma-hall; name preserved |
| dakṣiṇāvara | south-west / southern-western side | directional location; provisional |

## 9. Doctrinal Determination

VAkK_3.67 named the exterior gardens of the Trāyastriṃśa city-field. VAkK_3.68 adds a more specific directional arrangement: pleasant grounds in the four directions, with Pārijāta and Sudharmā assigned to inter-cardinal locations.

```text
Sudarśana / Vaijayanta field
    → exterior gardens
    → four directional pleasant grounds
    → Pārijāta tree
    → Sudharmā hall
```

The deva-world is now a complete civic-aesthetic field: city, palace, gardens, pleasure-grounds, tree, and assembly hall.

## 10. Logical Determination

This verse completes the transition from center to oriented totality.

```text
center
    → exterior
    → four-directional distribution
    → named symbolic supports
```

The divine city-field is not random ornamentation. It is arranged by directional measure and marked by special nodes.

## 11. Interpretive Note

Pārijāta and Sudharmā are especially important because they give the deva field both pleasure-symbol and assembly-symbol.

```text
Pārijāta
    → divine enjoyment / tree-symbol

Sudharmā
    → divine assembly / law-hall symbol
```

The word `Sudharmā` is striking for our purposes: even in the divine pleasure-world, `dharma` appears as an ordered assembly-form. But this remains within kāmadhātu and therefore within the world-field, not liberation.

## 12. Organon Interpretation

Light contact point:

```text
The divine civic field becomes an oriented totality of enjoyment and order.
```

This is an excellent example of the Kośa’s structural method. The gods are not merely named; their world is built as a measured topology of center, direction, pleasure, symbol, and institutional form.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_68
    a vak:Karika ;
    rdfs:label "VAK 3.68" ;
    vak:sourceReference "VAkK_3.68" ;
    vak:continues vak:VAK_3_67 ;
    vak:hasTopic vak:DirectionalPleasureGrounds ;
    vak:hasTopic vak:ParijataTree ;
    vak:hasTopic vak:SudharmaHall ;
    vak:belongsTo vak:DevaWorldApproachBlock .

vak:DirectionalPleasureGrounds
    a logic:AestheticEnjoymentField ;
    rdfs:label "pleasant grounds in the four directions" ;
    vak:hasInterval "twenty" ;
    vak:distributedAcross vak:FourDirections .

vak:ParijataTree
    a logic:DevaWorldSymbol ;
    rdfs:label "Pārijāta" ;
    vak:locatedIn vak:NorthEastDirection .

vak:SudharmaHall
    a logic:DevaAssemblyForm ;
    rdfs:label "Sudharmā" ;
    vak:locatedIn vak:SouthWestDirection .
```

## 14. Commit Note

Committed VAK_3.68 / VAkK_3.68.

Established:
- pleasant grounds are distributed in the four directions.
- Pārijāta is placed in the north-east.
- Sudharmā is placed in the south-west / dakṣiṇāvara, provisionally.
- the Trāyastriṃśa civic-aesthetic complex is completed as an oriented totality.
