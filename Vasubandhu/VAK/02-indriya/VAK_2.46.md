# VAK_2.46 — Jāti as Generative Mark and Meta-Marks

## 1. Sanskrit — Devanāgarī

```text
जातिजात्यादयस्तेषां तेऽष्टधर्मैकवृत्तयः ।
जन्यस्य जनिका जातिर्न हेतुप्रत्ययैर्विना ॥ VAkK_2.46 ॥
```

## 2. Sanskrit — IAST

```text
jātijātyādayas teṣāṃ te 'ṣṭadharmaikavṛttayaḥ /
janyasya janikā jātir na hetupratyayair vinā // VAkK_2.46 //
```

Source form:

```text
jātijātyādayasteṣāṃ te 'ṣṭadharmaikavṛttayaḥ /
janyasya janikā jātirna hetupratyayairvinā // VAkK_2.46 //
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| jāti-jāti-ādayaḥ | jātijātyādayaḥ | masculine nominative plural | jāti-of-jāti and the others / meta-marks |
| teṣām | teṣām | genitive plural | of these |
| te | te | pronoun, nominative plural | these |
| aṣṭa-dharma-eka-vṛttayaḥ | aṣṭadharmaikavṛttayaḥ | masculine nominative plural compound | operating in one occurrence of eight dharmas; technical |
| janyasya | janyasya | genitive singular | of what is to be generated / born |
| janikā | janikā | feminine nominative singular | generating / producer |
| jātiḥ | jātiḥ | feminine nominative singular | arising / birth |
| na | na | particle | not |
| hetu-pratyayaiḥ | hetupratyayaiḥ | instrumental plural compound | by causes and conditions |
| vinā | vinā | indeclinable | without |

## 4. Literal Translation

```text
Jāti-of-jāti and the others belong to these; they operate in one occurrence of eight dharmas.
Jāti is the generator of what is to be generated, not without causes and conditions.
```

## 5. Philosophical Translation

```text
The marks themselves have derivative meta-marks.
Arising is the generative mark of what comes to be, but it never operates apart from causes and conditions.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| jāti | arising / birth | Generative mark |
| jāti-jāti | arising of arising | Meta-mark; technical review needed |
| aṣṭadharmaikavṛtti | one occurrence involving eight dharmas | Dense Sarvāstivāda mark theory; later review required |
| janya | generated / to-be-born | That which is brought forth |
| janikā | generative | Producing or birth-giving function |
| hetu | cause / ground | Cause-ground; developed in 2.49ff |
| pratyaya | condition | Condition; developed in 2.61ff |
| vinā | without | Negation of independent generation |

## 7. Logical Determination

VAK_2.46 defines jāti as a generative mark.

```text
jāti
    = janikā janyasya
    = generator of what is generated
```

But it immediately blocks independent generation:

```text
jāti
    does not operate without hetu and pratyaya.
```

Logical protocol:

```text
if a conditioned item arises,
then jāti functions as its generative mark,
but only together with cause and condition.
```

This anticipates the later cause-condition system.

## 8. Relation to the Feature Logic

The mark-layer is not isolated.

```text
Lakṣaṇa
    requires
Hetu-Pratyaya
```

So the lifecycle marks already point forward to the causal and conditional engine.

## 9. Organon Interpretation

Organon reading:

```text
ArisingRule:
    target = generated item
    mark = jāti
    requires = hetu + pratyaya
```

Engineering implication:

```text
No lifecycle transition occurs without dependency conditions.
```

This is the bridge from lifecycle metadata to causal dependency graph.

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .

vak:Jati a vak:ConditionedMark ;
    vak:hasFunction vak:GeneratesGenerated ;
    vak:requires vak:Hetu, vak:Pratyaya .

vak:JatiJati a vak:ConditionedMetaMark .
vak:ConditionedMetaMark a rdfs:Class .
```

## 11. Commit History

```text
VAK_2.46 opened.
Method: kārikā-first speculative seed.
Theme: jāti as generative mark and mark-layer dependence on causes and conditions.
Technical mark theory marked for later Bhāṣya review.
Organon mapping: lifecycle transition requires cause-condition dependency graph.
Zero-padded file naming maintained: VAK_2.46.
```
