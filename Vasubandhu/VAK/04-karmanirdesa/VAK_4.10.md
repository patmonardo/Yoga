# VAK_4.10 — Initiating and Continuing Action-Origination

## 1. Sanskrit — Devanāgarī

```sanskrit
समुत्थानं द्विधा हेतुतत्क्षणोत्थानसंज्ञितम् ।
प्रवर्तकं तयोः आद्यं द्वितीयमनुवर्तकम् ॥
```

## 2. Sanskrit — IAST

```iast
samutthānaṃ dvidhā hetu-tat-kṣaṇotthāna-saṃjñitam |
pravartakaṃ tayor ādyaṃ dvitīyam anuvartakam ||
```

## 3. Source Caution

External source siglum: VAkK_4.10.

The compound is compressed. The intended twofold division is provisionally read as:

```text
hetu-samutthāna
    causal origination

tat-kṣaṇa-samutthāna
    origination in the very moment of action
```

The first is called `pravartaka`, the initiator; the second, `anuvartaka`, the continuator. VAK_4.11 elaborates their distribution.

## 4. Padaccheda

| Form | Analysis | Working determination |
|---|---|---|
| samutthānam | neuter nominative singular | originating condition |
| dvidhā | adverb | twofold |
| hetu | compound member | cause; ground |
| tat-kṣaṇa | compound | that very moment |
| utthāna | from ud-√sthā | arising |
| saṃjñitam | past passive participle | designated; named |
| pravartakam | neuter nominative singular | initiating |
| tayoḥ | genitive dual | of those two |
| ādyam | neuter nominative singular | the first |
| dvitīyam | neuter nominative singular | the second |
| anuvartakam | neuter nominative singular | continuing; sustaining |

## 5. Grammar

### `samutthānaṃ dvidhā`

> Origination is twofold.

The term introduced in VAK_4.08–4.09 is now internally differentiated.

### `hetu-tat-kṣaṇotthāna-saṃjñitam`

> It is designated as causal origination and origination in that very moment.

The first concerns the condition that gives rise to the action; the second concerns the mental occurrence accompanying the action at the moment of performance.

### `pravartakaṃ tayor ādyam`

> Of the two, the first is the initiator.

`Pravartaka` derives from `pra-√vṛt`: to set going, initiate, or bring into operation.

### `dvitīyam anuvartakam`

> The second is the continuator.

`Anuvartaka` derives from `anu-√vṛt`: to follow, continue, or sustain.

## 6. Literal Translation

> Origination is twofold, designated as causal origination and origination in that very moment. Of the two, the first is the initiator; the second is the continuator.

## 7. Philosophical Translation

> The mental origination of action has two distinct functions. A causal condition sets the action into operation, while a second condition occurring in the moment of performance accompanies and sustains its execution.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| samutthāna | originating condition | activation from which action proceeds |
| hetu-samutthāna | causal origination | initiating causal condition |
| tat-kṣaṇa-samutthāna | contemporaneous origination | condition present in the moment of action |
| pravartaka | initiator | setting into operation |
| anuvartaka | continuator | accompanying and sustaining |

## 9. Doctrinal Determination

```text
samutthāna
├── hetu-samutthāna
│   └── pravartaka
└── tat-kṣaṇa-samutthāna
    └── anuvartaka
```

Action has a condition that initiates it and another that accompanies and continues it. One isolated prior intention does not mechanically account for the whole performed act.

## 10. Temporal Determination

```text
initial activation
    → continuing mental accompaniment
        → performed bodily/verbal action
```

The distinction is temporal but also functional: beginning and continuing are different causal roles.

## 11. Logical Determination

```text
pravartaka
    explains transition into activity

anuvartaka
    explains persistence within activity
```

The chapter is preparing to ask whether the ethical character of the initiating and continuing conditions always agrees.

## 12. Relation to Volition

VAK_4.01 identified mental karma as `cetanā`. The present verse indicates that the mental production of bodily and verbal activity has initiating and continuative functions. Direct identification of both technical forms with separate volitions should await the Bhāṣya.

## 13. Interpretive Note

The origin of an action is not exhausted by the condition that first starts it. A deed must also be sustained during its occurrence.

## 14. Light Organon Interpretation

```text
pravartaka
    transition from non-performance into performance

anuvartaka
    preservation of action through its performed moments
```

Deeper identification with Projection or Absolute Ground remains deferred.

## 15. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_10
    a vak:Karika ;
    rdfs:label "VAK 4.10" ;
    vak:continues vak:VAK_4_09 ;
    vak:hasTopic vak:TwofoldSamutthana ;
    vak:hasTopic vak:InitiatingCondition ;
    vak:hasTopic vak:ContinuingCondition .

vak:Samutthana
    vak:hasMode vak:HetuSamutthana ;
    vak:hasMode vak:TatKsanaSamutthana .

vak:HetuSamutthana
    a vak:InitiatingCondition ;
    vak:hasFunction vak:Pravartaka .

vak:TatKsanaSamutthana
    a vak:ContemporaneousCondition ;
    vak:hasFunction vak:Anuvartaka .
```

## 16. Verse Summary

```text
VAK_4.10

The originating condition of action is twofold.

First:
    causal origination
    hetu-samutthāna

Its function:
    pravartaka
    it initiates the action.

Second:
    origination in the very moment
    tat-kṣaṇa-samutthāna

Its function:
    anuvartaka
    it accompanies and continues the action.
```

## 17. Commit Note

Committed VAK_4.10.

Established:
- action-origination is twofold.
- causal origination initiates.
- contemporaneous origination continues.
- the exact distribution is elaborated in VAK_4.11.