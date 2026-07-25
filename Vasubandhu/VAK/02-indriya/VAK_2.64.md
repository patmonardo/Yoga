# VAK_2.64 — Condition Application and Sequential Arising

## 1. Sanskrit — Devanāgarī

```text
चतुर्भिश्चित्तचैत्ता हि समापत्तिद्वयं त्रिभिः ।
द्वाभ्यामन्ये तु जायन्ते नेश्वरादेः क्रमादिभिः ॥ VAkK_2.64 ॥
```

## 2. Sanskrit — IAST

```text
caturbhiś cittacaittā hi samāpattidvayaṃ tribhiḥ /
dvābhyām anye tu jāyante neśvarādeḥ kramādibhiḥ // VAkK_2.64 //
```

Source form:

```text
caturbhiścattacaittā hi samāpattidvayaṃ tribhiḥ /
dvābhyāmanye tu jāyante neśvarādeḥ kramādibhiḥ // VAkK_2.64 //
```

Textual caution:

```text
The source reads `cattacaittā`; normalized here as `cittacaittā`.
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| caturbhiḥ | caturbhiḥ | instrumental plural | by four |
| citta-caittāḥ | cittacaittāḥ | nominative plural | citta and caittas |
| hi | hi | particle | indeed |
| samāpatti-dvayam | samāpattidvayam | neuter nominative singular | the two samāpattis |
| tribhiḥ | tribhiḥ | instrumental plural | by three |
| dvābhyām | dvābhyām | instrumental dual | by two |
| anye | anye | nominative plural | others |
| tu | tu | particle | but |
| jāyante | jāyante | present middle/passive, plural | arise |
| na | na | particle | not |
| īśvara-ādeḥ | īśvarādeḥ | ablative/genitive singular | from īśvara and the like |
| krama-ādibhiḥ | kramādibhiḥ | instrumental plural | by sequence and the like |

## 4. Literal Translation

```text
Citta and caittas arise by four conditions.
The two samāpattis arise by three.
Others arise by two.
They do not arise from īśvara and the like, but by sequence and the like.
```

## 5. Philosophical Translation

```text
Arising is condition-governed.
Citta-caitta events require the full fourfold condition-system.
The two samāpattis require three conditions.
Other formations arise through two.
This ordered arising is not explained by an external creator-principle, but by sequence and condition.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| caturbhiḥ | by four | Fourfold condition-system |
| citta-caitta | citta and caittas | Field and feature-functions |
| samāpatti-dvaya | the two attainments | Two special structural states from 2.42–2.43 |
| tribhiḥ | by three | Three-condition profile |
| dvābhyām | by two | Two-condition profile |
| jāyante | arise | Arising under condition-profile |
| īśvara-ādi | īśvara and the like | Rejected explanatory source |
| krama | sequence | Ordered succession |

## 7. Logical Determination

VAK_2.64 applies the condition system.

```text
CittaCaittaEvent:
    arises by four conditions

TwoSamapattiStates:
    arise by three conditions

OtherFormations:
    arise by two conditions
```

And it states a philosophical exclusion:

```text
not from īśvara and the like
but by sequence and condition-order
```

This is objective conditional logic.

## 8. Relation to the Feature Logic

The full engine is now visible:

```text
Lakṣaṇa
    marks arising and perishing

Hetu
    supplies ground

Phala
    supplies result

Pratyaya
    supplies condition-profile

Krama
    supplies sequence
```

## 9. Organon Interpretation

```text
ArisingConditionProfile:
    entityType = citta-caitta | samāpatti | other
    requiredConditionCount = 4 | 3 | 2
    arisingMode = sequential
```

Engineering implication:

```text
No event is admitted without its condition-profile.
```

This is the Objective Logic of arising.

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .

vak:CittaCaittaEvent vak:requiresConditionCount 4 .
vak:SamapattiState vak:requiresConditionCount 3 .
vak:OtherFormation vak:requiresConditionCount 2 .
vak:ConditionedArising vak:hasArisingMode vak:Krama .
```

## 11. Commit History

```text
VAK_2.64 opened.
Method: kārikā-first speculative seed.
Theme: condition application to citta-caittas, samāpattis, and other formations; sequence-based arising.
Textual caution recorded for source form `cattacaittā`.
Zero-padded file naming maintained: VAK_2.64.
```
