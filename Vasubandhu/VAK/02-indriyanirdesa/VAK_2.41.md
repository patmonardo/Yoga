# VAK_2.41 — Sabhāgatā, Āsaṃjñika, and Citta-Caitta Cessation

## 1. Sanskrit — Devanāgarī

```text
सभागता सत्त्वसाम्यं आसंज्ञिकमसंज्ञिषु ।
निरोधश्चित्तचैत्तानां विपाकः ते बृहत्फलाः ॥ VAkK_2.41 ॥
```

## 2. Sanskrit — IAST

```text
sabhāgatā sattvasāmyaṃ āsaṃjñikam asaṃjñiṣu /
nirodhaś cittacaittānāṃ vipākaḥ te bṛhatphalāḥ // VAkK_2.41 //
```

Source form:

```text
sabhāgatā sattvasāmyaṃ āsaṃjñikamasaṃjñiṣu /
nirodhaścittacaittānāṃ vipākaḥ te bṛhatphalāḥ // VAkK_2.41 //
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| sabhāgatā | sabhāgatā | feminine nominative singular | class-commonality / sameness of type |
| sattva-sāmyam | sattva-sāmyam | neuter nominative singular | sameness among beings |
| āsaṃjñikam | āsaṃjñikam | neuter nominative singular | non-ideational state |
| asaṃjñiṣu | asaṃjñiṣu | locative plural | among non-ideational beings |
| nirodhaḥ | nirodhaḥ | masculine nominative singular | cessation |
| citta-caittānām | cittacaittānām | genitive plural | of citta and caittas |
| vipākaḥ | vipākaḥ | masculine nominative singular | maturation-result |
| te | te | pronoun, nominative plural | these |
| bṛhat-phalāḥ | bṛhatphalāḥ | masculine nominative plural | belonging to the Great Fruit / Bṛhatphala; or having great fruit; verify |

## 4. Literal Translation

```text
Sabhāgatā is sameness among beings.
The āsaṃjñika is among non-ideational beings.
It is cessation of citta and caittas; these are maturation-result and Bṛhatphala.
```

## 5. Philosophical Translation

```text
The structural operators are further specified.
Sabhāgatā is the commonality by which beings belong to a shared type.
Āsaṃjñika concerns the non-ideational beings and marks a cessation of citta and caittas.
This state is treated as a maturation-result connected with the Bṛhatphala level.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| sabhāgatā | class-commonality | Shared type-status among beings |
| sattva-sāmya | sameness among beings | Definition of sabhāgatā |
| āsaṃjñika | non-ideational state | Structural state associated with asaṃjñin beings |
| asaṃjñin | non-ideational being | Beings without active saṃjñā/citta-caitta operation in this context |
| nirodha | cessation | Here cessation of citta-caittas |
| citta-caitta | citta and mental factors | Appearance-side field and functions |
| vipāka | maturation-result | Result of past conditioning |
| bṛhatphala | Great Fruit | Realm/status reference; to verify later |

## 7. Logical Determination

VAK_2.41 defines two structural operators.

```text
sabhāgatā
    = sameness among beings
    = class-membership operator

āsaṃjñika
    = cessation of citta-caittas among asaṃjñin beings
    = maturation-result operator
```

Logical protocols:

```text
Membership / Disjunctive Logic:
    sabhāgatā determines common class-status.

State Logic:
    āsaṃjñika determines a condition in which citta-caitta activity is not operative.
```

## 8. Relation to Indriya and Citta-Caitta

This verse proves why viprayukta-saṃskāras are required.

```text
Citta-Caitta
    = appearance operation

Āsaṃjñika
    = structural state concerning cessation of citta-caitta operation
```

A system that only tracks citta and caittas cannot explain their suspension. Therefore a structural operator layer is required.

## 9. Organon Interpretation

Organon reading:

```text
SabhagataOperator:
    assigns class-commonality among beings

AsamjnikaOperator:
    marks citta-caitta cessation state
    resultType = vipāka
    level = Bṛhatphala
```

Engineering implication:

```text
The Dataset needs class-membership operators
and state-suspension operators.
```

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .

vak:Sabhagata a vak:ViprayuktaSamskara ;
    vak:definedAs vak:SattvaSamya .

vak:Asamjnika a vak:ViprayuktaSamskara ;
    vak:hasStateFeature vak:CittaCaittaCessation ;
    vak:hasResultType vak:Vipaka .
```

## 11. Commit History

```text
VAK_2.41 opened.
Method: kārikā-first speculative seed.
Theme: sabhāgatā as class-commonality and āsaṃjñika as citta-caitta cessation state.
Technical details marked for later Bhāṣya review.
Organon mapping: class-membership and state-suspension operators.
Zero-padded file naming maintained: VAK_2.41.
```
