# VAK_3.54 — Bhājanaloka: Prāgvideha and the Half-Moon Shape

## 1. Sanskrit — Devanāgarī

```sanskrit
सार्धत्रियोजनं त्वेकं प्राग्विदेहोऽर्धचन्द्रवत् ।
पार्श्वत्रयं तथास्यैकं सार्धं त्रिशतयोजनम् ॥ VAkK_3.54 ॥
```

## 2. Sanskrit — IAST

```iast
sārdhatriyojanaṃ tv ekaṃ prāgvideho 'rdhacandravat /
pārśvatrayaṃ tathāsyaikaṃ sārdhaṃ triśatayojanam // VAkK_3.54 //
```

## 3. Source Caution

The source reading is:

```iast
sārdhatriyojanaṃ tvekaṃ prāgvideho 'rdhacandravat /
pārśvatrayaṃ tathāsya ekaṃ sārdhaṃ triśatayojanam // VAkK_3.54 //
```

Sandhi has been lightly separated:

```iast
sārdha-tri-yojanam tu ekam prāg-videhaḥ ardha-candra-vat /
pārśva-trayam tathā asya ekam sārdham tri-śata-yojanam //
```

The numerical expression is compact and should be checked against Pradhan and the bhāṣya in Pass 2. First-pass analysis treats the verse as giving a special one-side measure and a three-side measure for Prāgvideha, together with its half-moon shape.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| sārdhatriyojanam | sārdha-tri-yojanam | three and a half yojanas; numerical phrase to verify |
| tu | tu | but, now |
| ekam | ekam | one; one side |
| prāgvidehaḥ | prāg-videhaḥ | Prāgvideha, the eastern continent |
| ardhacandravat | ardha-candra-vat | like a half-moon, crescent-shaped |
| pārśvatrayam | pārśva-trayam | the set of three sides |
| tathā | tathā | likewise, so also |
| asya | asya | of this, of it |
| ekam | ekam | one; one measure or one side |
| sārdham | sārdham | with a half; half-added |
| triśatayojanam | tri-śata-yojanam | three hundred yojanas, with half-added; provisionally three hundred and fifty yojanas |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| sārdha-tri-yojanam | nominative/accusative singular neuter | numerical measure, likely of one side |
| ekam | nominative/accusative singular neuter | “one,” likely one side or one measure |
| prāg-videhaḥ | nominative singular masculine | subject: Prāgvideha |
| ardha-candra-vat | indeclinable/adjectival compound | shape predicate: “like a half-moon” |
| pārśva-trayam | nominative/accusative singular neuter | the three sides |
| asya | genitive singular | “of this,” referring to Prāgvideha |
| sārdham tri-śata-yojanam | numerical expression | measure: three hundred with half, to be verified |

## 6. Literal Translation

One side is three and a half yojanas; Prāgvideha is like a half-moon. Likewise, its three sides: one is three hundred and a half yojanas.

## 7. Philosophical Translation

Prāgvideha, the eastern continent, is introduced through shape and side-measure. Unlike the cart-shaped Jambūdvīpa, it is half-moon-shaped. Its sides are measured asymmetrically, with one special side and the remaining side-structure requiring commentarial verification.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| Prāgvideha | eastern Videha / Prāgvideha | eastern continent in the four-continent system |
| yojana | yojana | cosmological unit of length |
| sārdha | with a half | fractional augmentation of a measure |
| eka | one | one side or one measure |
| pārśva | side | side-structure of the continent |
| pārśvatraya | three sides | tripartite side-measure |
| ardha-candra-vat | like a half-moon | crescent or half-moon form |

## 9. Doctrinal Determination

VAkK_3.54 continues the continent-measure sequence begun in VAkK_3.53. Jambūdvīpa was described as cart-shaped and three-sided. This verse introduces Prāgvideha and assigns it the form of a half-moon.

The transition is:

```text
Jambūdvīpa
    → cart-shaped continent

Prāgvideha
    → half-moon-shaped continent
```

The continent system is therefore not homogeneous. Each dvīpa is defined by measure and shape.

## 10. Logical Determination

```text
continent-region
    → side-measure
        → geometric form
```

VAkK_3.54 reinforces the morphology of the dvīpa-system. A continent is not simply a landmass. It is a measured form with sides and shape.

The important first-pass determination is:

```text
Prāgvideha = eastern dvīpa as half-moon form
```

This begins the comparative geometry of the continents.

## 11. Interpretive Note

The numerical syntax should be handled cautiously. This is exactly where the bhāṣya pass will matter. For first-pass purposes, we preserve the source reading and mark the measure for later verification rather than forcing a premature arithmetic resolution.

The stable interpretive result is clear enough: Prāgvideha is the next dvīpa after Jambūdvīpa, and its defining morphology is `ardha-candra-vat`, “like a half-moon.”

For Organon purposes, this verse extends the logic of form from Jambūdvīpa to Prāgvideha:

```text
land-region
    → measured sides
        → determinate shape
```

## 12. OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_54 a vak:Karika ;
    rdfs:label "VAK 3.54" ;
    vak:sourceSiglum "VAkK_3.54" ;
    vak:belongsToChapter vak:Lokanirdesa ;
    vak:belongsToBlock vak:VAK_3c ;
    vak:continuesFrom vak:VAK_3_53 ;
    vak:hasTopic loka:Pragvideha ;
    vak:describes loka:PragvidehaMeasure , loka:PragvidehaShape .

loka:Pragvideha a loka:Dvipa ;
    rdfs:label "Prāgvideha" ;
    rdfs:comment "The eastern continent, described as half-moon-shaped." .

loka:PragvidehaShape a owl:Class ;
    rdfs:label "Prāgvideha shape" ;
    rdfs:comment "Prāgvideha as ardha-candra-vat, like a half-moon." .

loka:PragvidehaMeasure a owl:Class ;
    rdfs:label "Prāgvideha measure" ;
    rdfs:comment "The compact side-measure expression of VAkK_3.54, to be verified in Pass 2." .

loka:hasShape a owl:DatatypeProperty ;
    rdfs:label "has shape" .

loka:hasMeasureNote a owl:DatatypeProperty ;
    rdfs:label "has measure note" .

loka:Pragvideha loka:hasShape "ardha-candra-vat" ;
    loka:hasMeasureNote "sārdha-tri-yojana and sārdha tri-śata-yojana expressions; verify in Pass 2" .
```

## 13. Commit Note

```text
Add VAK_3.54 first-pass analysis.

Continues the continent-measure sequence.
Introduces Prāgvideha as the eastern dvīpa, half-moon-shaped and measured by compact side expressions.
Uses uppercase VAK artifact filename while preserving VAkK as textual source siglum.
Marks numerical syntax for Pass 2 bhāṣya verification.
```
