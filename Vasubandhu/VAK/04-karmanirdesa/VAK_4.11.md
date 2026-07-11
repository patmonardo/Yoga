# VAK_4.11 — Functional Distribution of Consciousness

## 1. Sanskrit — Devanāgarī

```sanskrit
प्रवर्तकं दृष्टिहेयं विज्ञानमुभयं पुनः ।
मानसं भावनाहेयं पञ्चकं त्वनुवर्तकम् ॥
```

## 2. Sanskrit — IAST

```iast
pravartakaṃ dṛṣṭiheyaṃ vijñānam ubhayaṃ punaḥ |
mānasaṃ bhāvanāheyaṃ pañcakaṃ tv anuvartakam ||
```

External source siglum: VAkK_4.11.

## 3. Source Caution

A cautious first-pass syntactic distribution is:

```text
dṛṣṭi-heyaṃ vijñānam
    pravartakam

bhāvanā-heyaṃ mānasaṃ
    ubhayam

pañcakaṃ tu
    anuvartakam
```

Thus consciousness abandoned by seeing is initiating; mental consciousness abandoned by cultivation is both initiating and continuing; the five sensory consciousnesses are continuing. The compressed syntax should be checked against the Bhāṣya.

## 4. Padaccheda

| Form | Analysis | Working determination |
|---|---|---|
| `pravartakam` | neuter nominative singular | initiating |
| `dṛṣṭi-heyam` | compound adjective | to be abandoned by seeing |
| `vijñānam` | neuter nominative singular | consciousness |
| `ubhayam` | neuter nominative singular | both |
| `punaḥ` | adverb | again; in turn |
| `mānasam` | neuter nominative singular | mental consciousness |
| `bhāvanā-heyam` | compound adjective | to be abandoned by cultivation |
| `pañcakam` | neuter nominative singular collective | the fivefold group |
| `tu` | particle | but; whereas |
| `anuvartakam` | neuter nominative singular | continuing |

## 5. Grammar

### `pravartakaṃ dṛṣṭiheyaṃ vijñānam`

```text
dṛṣṭi-heyaṃ vijñānam
    pravartakam
```

Consciousness abandoned by seeing is initiating.

### `ubhayaṃ punaḥ mānasaṃ bhāvanāheyam`

```text
bhāvanā-heyaṃ mānasaṃ
    ubhayam
```

Mental consciousness abandoned by cultivation is both initiating and continuing.

### `pañcakaṃ tv anuvartakam`

The fivefold group—the five sensory consciousnesses—is continuing.

## 6. Literal Translation

> Consciousness to be abandoned by seeing is initiating. Mental consciousness to be abandoned by cultivation is again both; the fivefold group, however, is continuing.

## 7. Philosophical Translation

> Consciousness belonging to the class abandoned through seeing functions as an initiator of action. Mental consciousness abandoned through cultivation may initiate and accompany the action. The five sensory consciousnesses function only as continuators.

## 8. Technical Vocabulary

### `dṛṣṭi-heya`

To be abandoned by seeing or direct insight.

### `bhāvanā-heya`

To be abandoned by cultivation or repeated development.

### `mānasa-vijñāna`

Mental consciousness, able to function both before and during bodily or verbal action.

### `pañcaka`

The five sensory consciousnesses.

### `pravartaka`

That which initiates or sets action in motion.

### `anuvartaka`

That which follows, accompanies, and continues action.

## 9. Doctrinal Determination

VAK_4.10 introduced two functions:

```text
pravartaka
    initiator

anuvartaka
    continuator
```

VAK_4.11 distributes consciousness among them:

```text
consciousness abandoned by seeing
    → initiating

mental consciousness abandoned by cultivation
    → initiating and continuing

five sensory consciousnesses
    → continuing
```

This is a functional map of consciousness within action.

## 10. Logical Determination

The field of continuation is broader than the field of initiation:

```text
initiation
    requires mental consciousness

continuation
    may involve mental consciousness
    or sensory consciousness
```

Consciousness is therefore not treated as one homogeneous cause. It differs by faculty, temporal function, and mode of abandonment.

## 11. Interpretive Note

The verse crosses two classifications:

```text
functional classification
    initiating / continuing

Path classification
    abandoned by seeing / abandoned by cultivation
```

The chapter thereby links Karma with future analyses of defilement and Path, while not yet developing those chapters fully.

## 12. Light Organon Interpretation

```text
mental consciousness
    can project action
    and maintain action

sensory consciousness
    participates in the maintained appearance
    but does not project the act
```

The Sanskrit functional terms remain primary:

```text
pravartaka
anuvartaka
```

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_11
    a vak:Karika ;
    rdfs:label "VAK 4.11" ;
    vak:continues vak:VAK_4_10 ;
    vak:hasTopic vak:FunctionalDistributionOfConsciousness ;
    vak:hasTopic vak:PathModesOfAbandonment .

vak:SeeingAbandonedConsciousness
    a vak:Vijnana ;
    vak:hasActionFunction vak:Pravartaka .

vak:CultivationAbandonedMentalConsciousness
    a vak:ManasaVijnana ;
    vak:hasActionFunction vak:Pravartaka ;
    vak:hasActionFunction vak:Anuvartaka .

vak:FiveSenseConsciousnesses
    a vak:VijnanaGroup ;
    vak:hasActionFunction vak:Anuvartaka .
```

## 14. Verse Summary

```text
VAK_4.11

Consciousness abandoned by seeing:
    initiating

Mental consciousness abandoned by cultivation:
    initiating and continuing

The five sensory consciousnesses:
    continuing only

Therefore:

mental consciousness can both
project and sustain action,

whereas sensory consciousness
participates only in its continuation.
```
