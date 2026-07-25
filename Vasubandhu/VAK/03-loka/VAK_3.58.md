# VAK_3.58 — Bhājanaloka: Avīci and the Eight Hot Hells

## 1. Sanskrit — Devanāgarī

```sanskrit
अधः सहस्रैर्विशत्या तन्मात्रोऽवीचिरस्य हि ।
तदूर्ध्वं सप्त नरकाः सर्वेऽष्टौ षोडशोत्सदाः ॥ VAkK_3.58 ॥
```

## 2. Sanskrit — IAST

```iast
adhaḥ sahasrair viśatyā tanmātro 'vīcir asya hi /
tadūrdhvaṃ sapta narakāḥ sarve 'ṣṭau ṣoḍaśotsadāḥ // VAkK_3.58 //
```

## 3. Source Caution

The source reading is:

```iast
adhaḥ sahasrairviśatyā tanmātro 'vīcirasya hi /
tadūrdhvaṃ sapta narakāḥ sarve 'ṣṭau ṣoḍaśotsadāḥ // VAkK_3.58 //
```

Sandhi has been lightly separated:

```iast
adhaḥ sahasraiḥ viśatyā tan-mātraḥ avīciḥ asya hi /
tad-ūrdhvam sapta narakāḥ sarve aṣṭau ṣoḍaśa-utsadāḥ //
```

The phrase `tanmātro 'vīcir asya hi` should be checked against Pradhan and the bhāṣya in Pass 2. First-pass analysis takes the verse to locate Avīci below by twenty thousand and to state that the seven remaining hells lie above it, making eight hells in all, each with sixteen subsidiary places.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| adhaḥ | adhaḥ | below, downward |
| sahasrairviśatyā | sahasraiḥ viśatyā | by twenty thousands; twenty thousand |
| tanmātraḥ | tat-mātraḥ | of that measure, just that much |
| avīciḥ | avīciḥ | Avīci, the lowest hot hell |
| asya | asya | of this / its; referent to verify |
| hi | hi | indeed, for |
| tadūrdhvam | tad-ūrdhvam | above that |
| sapta | sapta | seven |
| narakāḥ | narakāḥ | hells |
| sarve | sarve | all |
| aṣṭau | aṣṭau | eight |
| ṣoḍaśotsadāḥ | ṣoḍaśa-utsadāḥ | having sixteen utsadas / subsidiary hells |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| adhaḥ | indeclinable | downward location |
| sahasraiḥ viśatyā | instrumental plural + numeral | measure of downward distance: “by twenty thousand” |
| tat-mātraḥ | nominative singular masculine | “of that same measure” or “just that much” |
| avīciḥ | nominative singular masculine | subject: Avīci hell |
| asya hi | genitive + particle | compact explanatory phrase, to be verified |
| tad-ūrdhvam | indeclinable compound | “above that” |
| sapta narakāḥ | nominative plural masculine | the seven hells above Avīci |
| sarve aṣṭau | nominative plural masculine | total count: all eight |
| ṣoḍaśa-utsadāḥ | nominative plural masculine compound | each having sixteen subsidiary hells/annexes |

## 6. Literal Translation

Below by twenty thousand is Avīci, of that measure indeed. Above that are seven hells. All eight have sixteen utsadas.

## 7. Philosophical Translation

The text now turns from surface geography to subterranean placement. Avīci is located below by a measure of twenty thousand. Above it stand seven further hells, making eight in total; each is accompanied by sixteen subsidiary hell-regions.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| adhaḥ | below | downward spatial determination |
| sahasrair viśatyā | twenty thousand | vertical distance/measure |
| Avīci | Avīci | lowest hot hell, placed below |
| naraka | hell | lower painful world-region |
| tad-ūrdhvam | above that | relative vertical placement above Avīci |
| aṣṭa | eight | total number of principal hot hells |
| utsada | subsidiary hell / annex | surrounding or additional hell-region associated with each principal hell |
| ṣoḍaśa | sixteen | number of utsadas for each principal hell |

## 9. Doctrinal Determination

VAkK_3.58 opens the hell-region sequence. After the dvīpas, intermediate islands, mountains, and lake-region, the text descends below the surface world.

The structure is:

```text
Avīci below
    → seven hells above Avīci
        → eight hells total
            → sixteen utsadas for each
```

This introduces a lower vertical cosmology into the already articulated container-world.

## 10. Logical Determination

```text
surface geography
    → downward depth
        → Avīci
            → ordered vertical series of hells
                → subsidiary regions
```

The verse adds a new axis of determination. The world-container is no longer only lateral and regional. It now has a subterranean vertical order.

The important logical transition is:

```text
measured continent-world
    → measured lower world
```

## 11. Interpretive Note

This verse is a clean structural turn. The previous verses articulated the inhabited surface-field through dvīpas and regional geography. VAkK_3.58 now places the lower painful domains beneath that field.

The count is important:

```text
1 Avīci
+ 7 above
= 8 hot hells
```

and each of the eight has:

```text
16 utsadas
```

Pass 2 should verify the exact measure and phrase `tanmātro 'vīcir asya hi`, but the first-pass doctrinal shape is clear: Avīci anchors the lower world, and the seven hells above complete the eightfold sequence.

## 12. OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_58 a vak:Karika ;
    rdfs:label "VAK 3.58" ;
    vak:sourceSiglum "VAkK_3.58" ;
    vak:belongsToChapter vak:Lokanirdesa ;
    vak:belongsToBlock vak:VAK_3c ;
    vak:continuesFrom vak:VAK_3_57 ;
    vak:hasTopic loka:HotHellSeries ;
    vak:describes loka:Avici , loka:SevenHellsAboveAvici , loka:SixteenUtsadas .

loka:Naraka a owl:Class ;
    rdfs:label "naraka" ;
    rdfs:comment "Hell-region in the lower vertical cosmology." .

loka:Avici a loka:Naraka ;
    rdfs:label "Avīci" ;
    rdfs:comment "The lowest hot hell, placed below by twenty thousand." .

loka:HotHellSeries a owl:Class ;
    rdfs:label "eight hot hells" ;
    rdfs:comment "Avīci plus seven hells above it." .

loka:Utsada a owl:Class ;
    rdfs:label "utsada" ;
    rdfs:comment "A subsidiary hell-region associated with a principal hell." .

loka:hasCount a owl:DatatypeProperty ;
    rdfs:label "has count" .

loka:hasSubsidiaryCount a owl:DatatypeProperty ;
    rdfs:label "has subsidiary count" .

loka:HotHellSeries loka:hasCount "aṣṭau" ;
    loka:hasSubsidiaryCount "ṣoḍaśa utsadāḥ for each principal hell" .

loka:Avici loka:hasMeasureNote "adhaḥ sahasraiḥ viśatyā; tanmātraḥ; verify in Pass 2" .
```

## 13. Commit Note

```text
Add VAK_3.58 first-pass analysis.

Begins the lower-world hell sequence after the surface geography.
Locates Avīci below by twenty thousand and adds seven hells above it, making eight total.
Records sixteen utsadas for each principal hell.
Marks tanmātro 'vīcir asya hi for Pass 2 verification.
```
