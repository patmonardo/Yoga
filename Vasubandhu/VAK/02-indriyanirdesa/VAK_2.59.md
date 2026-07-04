# VAK_2.59 — Temporal Fruit-Taking and Fruit-Giving

## 1. Sanskrit — Devanāgarī

```text
वर्तमानाः फलं पञ्च गृह्णन्ति द्वौ प्रयच्छतः ।
वर्तमानाभ्यतीतौ द्वौ एकोऽतीतः प्रयच्छति ॥ VAkK_2.59 ॥
```

## 2. Sanskrit — IAST

```text
varttamānāḥ phalaṃ pañca gṛṇhanti dvau prayacchataḥ /
varttamānābhyatītau dvau eko 'tītaḥ prayacchati // VAkK_2.59 //
```

## 3. Padaccheda

| Text | Padaccheda | Basic Sense |
|---|---|---|
| varttamānāḥ | varttamānāḥ | present ones |
| phalaṃ | phalaṃ | fruit |
| pañca | pañca | five |
| gṛṇhanti | gṛṇhanti | take, receive |
| dvau | dvau | two |
| prayacchataḥ | prayacchataḥ | give, produce |
| varttamānābhyatītau | varttamāna-abhyatītau | present and past |
| dvau | dvau | two |
| ekaḥ | ekaḥ | one |
| atītaḥ | atītaḥ | past |
| prayacchati | prayacchati | gives, produces |

## 4. Literal Translation

```text
Present ones, five, take fruit; two give fruit.
Two, present and past, give; one past gives.
```

## 5. Philosophical Translation

```text
The hetu-phala engine is temporally constrained.
Different ground-types take and give results according to present and past status.
Fruit-production is therefore governed by temporal position, not by an abstract causal relation alone.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| vartamāna | present | Current temporal status |
| atīta | past | Past temporal status |
| phalaṃ gṛhṇanti | take fruit | Receive or appropriate result-potential; review later |
| prayacchati | gives | Gives/produces result |
| pañca | five | Five hetus in present relation |
| dvau | two | Two hetus in specific giving relation |
| eka | one | One hetu in past relation |

## 7. Logical Determination

VAK_2.59 gives temporal operation rules.

```text
HetuOperation:
    takeFruit
    giveFruit
    temporalStatus = present | past
```

This is not merely causation, but scheduled causation:

```text
which ground can take fruit?
which ground can give fruit?
at what temporal status?
```

## 8. Organon Interpretation

```text
TemporalGroundRule:
    groundType
    operation = takeFruit | giveFruit
    validTime = present | past
```

The Dataset requires time-indexed ground-result transitions.

## 9. Commit History

```text
VAK_2.59 opened.
Method: kārikā-first speculative seed.
Theme: temporal rules for fruit-taking and fruit-giving.
Technical count mechanics marked for later Bhāṣya review.
```
