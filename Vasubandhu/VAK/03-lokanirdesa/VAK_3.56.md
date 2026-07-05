# VAK_3.56 — Bhājanaloka: The Eight Intermediate Islands

## 1. Sanskrit — Devanāgarī

```sanskrit
देहा विदेहाः कुरवः कौरवाश्चामरावराः ।
अष्टौ तदन्तरद्वीपा गाठा उत्तरमन्त्रिणः ॥ VAkK_3.56 ॥
```

## 2. Sanskrit — IAST

```iast
dehā videhāḥ kuravaḥ kauravāś cāmarāvarāḥ /
aṣṭau tadantaradvīpā gāṭhā uttaramantriṇaḥ // VAkK_3.56 //
```

## 3. Source Caution

The source reading is:

```iast
dehā videhāḥ kuravaḥ kauravāścāmarāvarāḥ /
aṣṭau tadantaradvīpā gāṭhā uttaramantriṇaḥ // VAkK_3.56 //
```

Sandhi has been lightly separated:

```iast
dehāḥ videhāḥ kuravaḥ kauravāḥ ca amarāvarāḥ /
aṣṭau tat-antara-dvīpāḥ gāṭhāḥ uttara-mantriṇaḥ //
```

Several names in this verse should be checked against Pradhan and the bhāṣya in Pass 2. In particular, the source reading `cāmarāvarāḥ` may conceal a pair such as `cāmara` and `avara-cāmara`, and `gāṭhā` may be a variant or OCR/transmission issue. First-pass work preserves the source reading and treats the verse as naming the eight intermediate islands.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| dehā | dehāḥ | Dehas, name of an intermediate island/group |
| videhāḥ | videhāḥ | Videhas, name of an intermediate island/group |
| kuravaḥ | kuravaḥ | Kurus, name of an intermediate island/group |
| kauravāḥ | kauravāḥ | Kauravas, name of an intermediate island/group |
| cāmarāvarāḥ | cāmara-avarāḥ / cāmara-avara-cāmarāḥ? | source compound; likely includes Cāmara and a paired Avara/Avaracāmara name; verify |
| aṣṭau | aṣṭau | eight |
| tadantaradvīpāḥ | tat-antara-dvīpāḥ | intermediate islands belonging between those continents |
| gāṭhā | gāṭhāḥ | name preserved from source; verify |
| uttaramantriṇaḥ | uttara-mantriṇaḥ | name preserved from source; verify |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| dehāḥ | nominative plural masculine | named item in the eight intermediate islands |
| videhāḥ | nominative plural masculine | named item in the eight intermediate islands |
| kuravaḥ | nominative plural masculine | named item in the eight intermediate islands |
| kauravāḥ | nominative plural masculine | named item in the eight intermediate islands |
| cāmarāvarāḥ | nominative plural masculine compound | compact name-sequence, to be verified |
| aṣṭau | numeral | total count: eight |
| tat-antara-dvīpāḥ | nominative plural masculine | subject/predicate: “the intermediate islands of those” |
| gāṭhāḥ | nominative plural masculine | named item, to be verified |
| uttara-mantriṇaḥ | nominative plural masculine | named item, to be verified |

## 6. Literal Translation

Dehas, Videhas, Kurus, Kauravas, Cāmara-Avaras, Gāṭhas, and Uttaramantriṇas: these are the eight intermediate islands between them.

## 7. Philosophical Translation

After the four main continents have been given by measure and shape, the Kośa adds their intermediate islands. These eight `antaradvīpas` occupy the between-spaces of the continent-system, filling out the regional articulation of the world-container.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| antaradvīpa | intermediate island | secondary island-region between the principal dvīpas |
| Deha | Deha | named intermediate island/group |
| Videha | Videha | named intermediate island/group |
| Kuru | Kuru | named intermediate island/group, paired with Kaurava |
| Kaurava | Kaurava | named intermediate island/group |
| Cāmara / Avara | Cāmara / Avara | compact source sequence requiring Pass 2 verification |
| Gāṭha | Gāṭha | source reading preserved; verify |
| Uttaramantriṇa | Uttaramantriṇa | source reading preserved; verify |

## 9. Doctrinal Determination

VAkK_3.56 completes the continent-field by adding the eight intermediate islands. VAkK_3.53–3.55 described the four principal dvīpas by shape and measure. This verse introduces the subordinate regions that lie between them.

The transition is:

```text
four principal dvīpas
    → eight intermediate dvīpas
```

The continent-system therefore becomes not merely fourfold but interstitially articulated. The world-field now includes principal regions and between-regions.

## 10. Logical Determination

```text
principal land-forms
    → interstitial regions
        → regional completion of the dvīpa-field
```

The significant term is `antara`: between. The verse gives the logic of mediation within the continent-system. The four main forms do not exhaust the regional field. The between-spaces are themselves named and determined.

This creates a two-level land-structure:

```text
main dvīpas
    secondary / intermediate dvīpas
```

## 11. Interpretive Note

This verse is philologically delicate. The source gives a compact and perhaps variant name-list. First-pass work should not force the list into a standardized form without checking the bhāṣya and a critical edition.

The stable structural point is enough for this pass: the Kośa recognizes eight `antaradvīpas`, intermediate islands belonging to the four-continent system. This completes the basic continent morphology and prepares the transition to mountains, lakes, hells, and vertical subterranean regions in the following verses.

For Organon purposes, VAkK_3.56 marks the emergence of the between-region:

```text
form
    → interval
        → named intermediate place
```

## 12. OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_56 a vak:Karika ;
    rdfs:label "VAK 3.56" ;
    vak:sourceSiglum "VAkK_3.56" ;
    vak:belongsToChapter vak:Lokanirdesa ;
    vak:belongsToBlock vak:VAK_3c ;
    vak:continuesFrom vak:VAK_3_55 ;
    vak:hasTopic loka:IntermediateIslands ;
    vak:describes loka:AntaradvipaSeries .

loka:Antaradvipa a owl:Class ;
    rdfs:label "antaradvīpa" ;
    rdfs:comment "An intermediate island-region between the principal continents." .

loka:AntaradvipaSeries a owl:Class ;
    rdfs:label "eight intermediate islands" ;
    rdfs:comment "The eight intermediate islands named in VAkK_3.56; names require Pass 2 verification." .

loka:hasCount a owl:DatatypeProperty ;
    rdfs:label "has count" .

loka:hasNameList a owl:DatatypeProperty ;
    rdfs:label "has name list" .

loka:AntaradvipaSeries loka:hasCount "aṣṭau" ;
    loka:hasNameList "dehāḥ, videhāḥ, kuravaḥ, kauravāḥ, cāmarāvarāḥ, gāṭhāḥ, uttaramantriṇaḥ; verify segmentation in Pass 2" .
```

## 13. Commit Note

```text
Add VAK_3.56 first-pass analysis.

Adds the eight intermediate islands after the four principal dvīpas.
Preserves compact source readings cāmarāvarāḥ, gāṭhā, and uttaramantriṇaḥ for Pass 2 verification.
Uses uppercase VAK artifact filename while preserving VAkK as textual source siglum.
```
