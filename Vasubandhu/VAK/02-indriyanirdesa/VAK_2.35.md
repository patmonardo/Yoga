# VAK_2.35 — Viprayukta-Saṃskāra Structural Operators

## 1. Sanskrit — Devanāgarī

```text
विप्रयुक्तास्तु संस्काराः प्राप्त्यप्राप्ती सभागता ।
आसंज्ञिकं समापत्ती जीवितं लक्षणानि च ॥ VAkK_2.35 ॥
```

## 2. Sanskrit — IAST

```text
viprayuktās tu saṃskārāḥ prāptyaprāptī sabhāgatā /
āsaṃjñikaṃ samāpattī jīvitaṃ lakṣaṇāni ca // VAkK_2.35 //
```

Source form:

```text
viprayuktāstu saṃskārāḥ prāptyaprāptī sabhāgatā /
āsaṃjñikaṃ samāpattī jīvitaṃ lakṣaṇāni ca // VAkK_2.35 //
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| viprayuktāḥ | vi-prayuktāḥ | masculine nominative plural | dissociated / not directly associated |
| tu | tu | particle | but / now |
| saṃskārāḥ | saṃskārāḥ | masculine nominative plural | formations / conditioned operators |
| prāpti-aprāptī | prāpti-aprāptī | feminine nominative dual | acquisition and non-acquisition |
| sabhāgatā | sabhāgatā | feminine nominative singular | sameness of class / commonality |
| āsaṃjñikam | āsaṃjñikam | neuter nominative singular | non-ideational state / asaṃjñika |
| samāpattī | samāpattī | feminine nominative dual | two attainments / absorptions |
| jīvitam | jīvitam | neuter nominative singular | life / living continuity |
| lakṣaṇāni | lakṣaṇāni | neuter nominative plural | marks / determinations |
| ca | ca | indeclinable | and |

## 4. Literal Translation

```text
The dissociated formations are acquisition and non-acquisition, sabhāgatā,
the āsaṃjñika, the two samāpattis, life, and the marks.
```

## 5. Philosophical Translation

```text
A new feature-family is introduced: formations dissociated from citta and caitta.
These are structural operators of conditioned experience: acquisition, non-acquisition,
class-commonality, non-ideational status, absorptive attainments, life-continuity,
and conditioned marks.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| viprayukta | dissociated | Not citta, not caitta, yet still conditioned formation |
| saṃskāra | formation / operator | Conditioned structure or formative factor |
| prāpti | acquisition / attainment / configuration-link | Relation of having or attaining |
| aprāpti | non-acquisition / non-attainment | Counter-relation to prāpti |
| sabhāgatā | class-commonality | Shared type-status among beings or series |
| āsaṃjñika | non-ideational | Connected with absence/suspension of saṃjñā; details later |
| samāpatti | attainment / absorption | Meditative attainment or settled state |
| jīvita | life-continuity | Continuity-support of the living series |
| lakṣaṇa | mark / determination | Conditioned marks unfolded in VAK_2.45ff |

## 7. Logical Determination

VAK_2.35 opens the structural-operator block.

```text
Citta-Caitta
    = associated appearance-functions

Viprayukta-saṃskāra
    = structural operators not reducible to citta-caitta association
```

The dominant protocol is Disjunctive Feature-Division:

```text
conditioned formations divide into:
    associated mental factors
    dissociated structural operators
```

This block is required because conditioned experience needs more than faculty and mental features. It needs structural relations such as acquisition, commonality, continuity, attainment, and lifecycle marks.

## 8. Relation to Indriya and Citta-Caitta

```text
Indriya
    = Real-side governing givenness

Citta-Caitta
    = Ideal-side appearance configuration

Viprayukta-saṃskāra
    = structural mediation between givenness and appearance
```

These are not merely psychological items. They are state-operators and relation-operators in the conditioned series.

## 9. Organon Interpretation

Organon reading:

```text
ViprayuktaFeatureSet:
    prāpti
    aprāpti
    sabhāgatā
    āsaṃjñika
    samāpatti
    jīvita
    lakṣaṇa
```

Engineering analogy:

```text
not raw data
not agent feature
but lifecycle / state / relation operators
```

This is the structural-operator layer of the Semantic Dataset.

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:ViprayuktaSamskara a rdfs:Class ;
    rdfs:label "viprayukta-saṃskāra" ;
    rdfs:comment "A dissociated formation functioning as a structural operator in conditioned experience." .

vak:Prapti a vak:ViprayuktaSamskara .
vak:Aprapti a vak:ViprayuktaSamskara .
vak:Sabhagata a vak:ViprayuktaSamskara .
vak:Asamjnika a vak:ViprayuktaSamskara .
vak:Samapatti a vak:ViprayuktaSamskara .
vak:Jivita a vak:ViprayuktaSamskara .
vak:Laksana a vak:ViprayuktaSamskara .
```

## 11. Commit History

```text
VAK_2.35 opened.
Method: kārikā-first speculative seed.
Theme: viprayukta-saṃskāras as structural operators.
Logical protocol recorded: disjunctive feature-division beyond citta-caitta.
Organon mapping: structural operator layer of the Semantic Dataset.
Zero-padded file naming maintained: VAK_2.35.
```
