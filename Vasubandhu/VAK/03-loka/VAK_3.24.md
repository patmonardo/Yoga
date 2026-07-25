# VAK_3b — VAkK_3.24

## Sanskrit — Devanāgarī

स भविष्यत् भवफलं कुरुते कर्म तद् भवः ।
प्रतिसंधिः पुनर्जातिः जरामरणमा विदः ॥ VAkK_3.24 ॥

## Sanskrit — IAST

sa bhaviṣyat bhavaphalaṃ kurute karma tat bhavaḥ /
pratisaṃdhiḥ punarjātiḥ jarāmaraṇamā vidaḥ // VAkK_3.24 //

## Source Caution

The source line is compact and is preserved here as read:

```text
sa bhaviṣyat bhavaphalaṃ kurute karma tat bhavaḥ /
pratisaṃdhiḥ punarjātiḥ jarāmaraṇamā vidaḥ // VAkK_3.24 //
```

The expression `jarāmaraṇamā vidaḥ` should be treated as provisional until checked against the Bhāṣya and manuscript/edition witnesses.

## Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| sa | saḥ | he / that one; the one so conditioned |
| bhaviṣyat | bhaviṣyat | future; about to be |
| bhavaphalam | bhava-phalam | fruit of becoming / existence-result |
| kurute | kurute | makes; performs; produces |
| karma | karma | action / karma |
| tat | tat | that |
| bhavaḥ | bhavaḥ | becoming / existence |
| pratisaṃdhiḥ | pratisaṃdhiḥ | reconnection; relinking |
| punaḥ | punaḥ | again; next; in turn |
| jātiḥ | jātiḥ | birth |
| jarāmaraṇam | jarā-maraṇam | aging-and-death |
| ā vidaḥ | ā vidaḥ | up to / until knowing? provisional source reading |

## Grammar

```text
saḥ
    = that one; the one described in the preceding verse as pursuing enjoyment

bhaviṣyat bhava-phalam
    = future fruit of becoming / future existence-result

kurute karma
    = makes / performs karma

tat bhavaḥ
    = that is bhava, becoming/existence

pratisaṃdhiḥ punaḥ jātiḥ
    = reconnection, again, is birth

jarā-maraṇam ā vidaḥ
    = aging-and-death ... up to vidaḥ
    = provisional until checked against the Bhāṣya
```

## Literal Translation

That one performs karma whose fruit is future becoming; that is becoming. Reconnection, in turn, is birth. Aging-and-death extends up to `vidaḥ`.

## Philosophical Translation

The one driven by appropriation produces karma that has future becoming as its fruit; this karmic production is the limb called becoming. The renewed junction of the series is birth. Aging-and-death names the subsequent decay-and-termination of the newly arisen life-series, with the final phrase to be clarified against the Bhāṣya.

## Technical Vocabulary

| Sanskrit | Working translation | Note |
|---|---|---|
| bhaviṣyat | future | Future-oriented result or becoming |
| bhava | becoming / existence | The tenth limb of dependent co-arising |
| phala | fruit / result | Here, the result of karma as future becoming |
| karma | action / karma | Action that projects future becoming |
| pratisaṃdhi | reconnection / relinking | The renewed junction of the series |
| jāti | birth | The eleventh limb |
| jarā | aging | Decline of the conditioned life-series |
| maraṇa | death | Termination of the conditioned life-series |
| jarāmaraṇa | aging-and-death | The twelfth limb |

## Doctrinal Determination

VAkK_3.24 completes the initial list of the twelve limbs introduced in 3.20.

It gives the last three limbs:

```text
10. bhava
11. jāti
12. jarāmaraṇa
```

The movement is:

```text
upādāna
    ↓
karma producing future becoming
    ↓
bhava
    ↓
pratisaṃdhi / jāti
    ↓
jarāmaraṇa
```

Here bhava is not merely a static existence. It is karmic becoming insofar as it projects a future result.

## Logical Determination

The verse marks the turn from present appropriation into future existence.

```text
upādāna
    = appropriative pursuit

bhava
    = karmic production of future becoming

jāti
    = renewed arising / reconnection

jarāmaraṇa
    = decay and termination of the arisen series
```

The logic is:

```text
appropriation
    becomes karmic projection
        becomes renewed birth
            becomes aging-and-death
```

This completes the 2 / 8 / 2 architecture:

```text
Prior limit:
    avidyā
    saṃskāra

Middle:
    vijñāna
    nāmarūpa
    ṣaḍāyatana
    sparśa
    vittiḥ
    tṛṣṇā
    upādāna
    bhava

Later limit:
    jāti
    jarāmaraṇa
```

## Interpretive Note

This verse is the hinge where the middle section produces the later limit. The middle is not merely experienced; it acts. Craving becomes appropriation, appropriation becomes karma, and karma projects future becoming.

The Bhāṣya should be used to clarify whether `bhava` here is primarily action, existence, or karmic potential for future existence. The kārikā points toward all three, but its immediate phrase is karmic: `kurute karma`.

## Organon Interpretation

Speculatively, this verse closes the first cycle of the saṃsāric wheel.

```text
appropriative pursuit
    ↓
projective action
    ↓
future becoming
    ↓
renewed instantiation
    ↓
aging-and-death
```

For Organon, this is the passage from drive to projection:

```text
upādāna
    = capture / appropriation

bhava
    = generated future-state

jāti
    = new instantiation of the series

jarāmaraṇa
    = decay of the instantiated series
```

This remains interpretive and must survive contact with the Bhāṣya.

## OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_24
    a vak:Karika ;
    rdfs:label "VAkK 3.24" ;
    vak:continues vak:VAK_3_23 ;
    vak:hasTopic vak:DependentCoArising ;
    vak:explicatesLimb vak:Bhava ;
    vak:explicatesLimb vak:Jati ;
    vak:explicatesLimb vak:Jaramarana .

vak:Bhava
    a vak:DependentCoArisingLimb ;
    rdfs:label "bhava" ;
    vak:hasCanonicalTranslation "becoming" ;
    vak:belongsToSection vak:MadhyaSection ;
    logic:follows vak:Upadana ;
    logic:precedes vak:Jati ;
    vak:hasFunction vak:FutureProjection .

vak:Jati
    a vak:DependentCoArisingLimb ;
    rdfs:label "jāti" ;
    vak:hasCanonicalTranslation "birth" ;
    vak:belongsToSection vak:AparantaSection ;
    logic:follows vak:Bhava ;
    logic:precedes vak:Jaramarana .

vak:Jaramarana
    a vak:DependentCoArisingLimb ;
    rdfs:label "jarāmaraṇa" ;
    vak:hasCanonicalTranslation "aging-and-death" ;
    vak:belongsToSection vak:AparantaSection ;
    logic:follows vak:Jati .

vak:FutureProjection
    a logic:Function ;
    rdfs:label "future projection" ;
    rdfs:comment "The function by which karma produces a future becoming-result." .
```

## Commit Note

Committed VAK_3b / VAkK_3.24.

Established:
- bhava is karmic becoming oriented toward future result.
- jāti is glossed through pratisaṃdhi, reconnection or relinking.
- jarāmaraṇa completes the later limit.
- The source expression `jarāmaraṇamā vidaḥ` is preserved as provisional pending Bhāṣya review.

Logical determination:
VAkK_3.24 completes the first enumeration of the twelvefold dependent co-arising sequence. Upādāna produces karma whose fruit is future becoming; that becoming issues in birth, and birth entails aging-and-death.
