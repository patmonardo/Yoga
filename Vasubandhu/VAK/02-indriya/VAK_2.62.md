# VAK_2.62 — Definitions of the Four Pratyayas

## 1. Sanskrit — Devanāgarī

```text
चित्तचैत्ता अचरमा उत्पन्नाः समनन्तरः ।
आलम्बनं सर्वधर्माः कारणाख्योऽधिपः स्मृतः ॥ VAkK_2.62 ॥
```

## 2. Sanskrit — IAST

```text
cittacaittā acaramā utpannāḥ samanantaraḥ /
ālambanaṃ sarvadharmāḥ kāraṇākhyo 'dhipaḥ smṛtaḥ // VAkK_2.62 //
```

## 3. Padaccheda

| Text | Padaccheda | Basic Sense |
|---|---|---|
| cittacaittāḥ | citta-caittāḥ | citta and caittas |
| acaramāḥ | acaramāḥ | not final, not last |
| utpannāḥ | utpannāḥ | arisen |
| samanantaraḥ | samanantaraḥ | immediately antecedent |
| ālambanaṃ | ālambanam | object-support |
| sarvadharmāḥ | sarva-dharmāḥ | all dharmas |
| kāraṇākhyaḥ | kāraṇa-ākhyaḥ | called kāraṇa |
| adhipaḥ | adhipaḥ | dominant condition |
| smṛtaḥ | smṛtaḥ | remembered, said |

## 4. Literal Translation

```text
Citta and caittas, arisen and not final, are the immediately antecedent condition.
All dharmas are object-support. What is called kāraṇa is remembered as the dominant condition.
```

## 5. Philosophical Translation

```text
The four conditions are defined.
A prior arisen citta-caitta event, when not final, serves as the immediately antecedent condition.
All dharmas can serve as object-support.
The kāraṇa ground is recast as dominant condition.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| samanantara-pratyaya | immediately antecedent condition | Sequential citta-caitta condition |
| acarama | not final | Not the final citta; condition for further arising |
| utpanna | arisen | Already arisen condition |
| ālambana | object-support | Object-support condition |
| sarvadharma | all dharmas | Scope of possible object-support |
| kāraṇa | conditioning ground | Recast here as dominant condition |
| adhipati | dominant condition | Governing/dominant condition |

## 7. Logical Determination

VAK_2.62 defines the condition-types:

```text
Samanantara:
    prior arisen non-final citta-caitta event

Ālambana:
    all dharmas as object-support

Adhipati:
    kāraṇa as dominant condition
```

This is sequential and intentional condition-logic.

```text
citta-caitta sequence
    -> next citta-caitta event

object-support
    -> appearance content

dominant condition
    -> enabling force
```

## 8. Relation to Yoga Sūtra IV.11

This verse directly illuminates:

```text
hetu-phala-āśraya-ālambana
```

Here `ālambana` is no longer vague objecthood. It is a formal condition-type.

## 9. Organon Interpretation

```text
ConditionTypes:
    sequentialCondition
    objectSupportCondition
    dominantCondition
```

For the Dataset:

```text
an event requires:
    prior event condition
    object-support condition
    dominant enabling condition
```

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .

vak:SamanantaraPratyaya a vak:Pratyaya ;
    vak:requiresPriorEvent vak:CittaCaittaEvent .

vak:AlambanaPratyaya a vak:Pratyaya ;
    vak:hasScope vak:SarvaDharma .

vak:AdhipatiPratyaya a vak:Pratyaya ;
    vak:relatedHetu vak:KaranaHetu .
```

## 11. Commit History

```text
VAK_2.62 opened.
Method: kārikā-first speculative seed.
Theme: definitions of samanantara, ālambana, and adhipati conditions.
Zero-padded file naming maintained: VAK_2.62.
```
