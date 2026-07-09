# VAK_3.89 — Measure: From Muhūrta to Kalpa

## 1. Sanskrit — Devanāgarī

```sanskrit
त्रयो मुहूर्त्ताहोरात्रमासाः द्वादशमासकः ।
संवत्सरः सोनरात्रः कल्पो बहुविधः स्मृतः ॥ VAkK_3.89 ॥
```

## 2. Sanskrit — IAST

```iast
trayo muhūrttāhorātra-māsāḥ dvādaśa-māsakaḥ /
saṃvatsaraḥ sonarātraḥ kalpo bahuvidhaḥ smṛtaḥ // VAkK_3.89 //
```

## 3. Source Caution

The source reading is:

```iast
trayo muhūrttāhorātramāsāḥ dvādaśamāsakaḥ /
saṃvatsaraḥ sonarātraḥ kalpo bahuvidhaḥ smṛtaḥ // VAkK_3.89 //
```

The transmitted line is compressed and likely requires checking against the bhāṣya and printed editions. The phrase beginning with `trayo muhūrtta-` is especially difficult as printed. In context, the verse continues the time-unit ladder opened in VAkK_3.88. The structural sequence is provisionally read as:

```text
kṣaṇa
    → tatkṣaṇa
        → lava
            → muhūrta
                → ahorātra
                    → māsa
                        → saṃvatsara
                            → kalpa
```

The second pāda is clearer: a year is made of twelve months, with the day-night relation included; kalpa is remembered as manyfold.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| trayo | trayaḥ / triṃśat? | transmitted `trayo`; numerical reading uncertain |
| muhūrttāhorātra-māsāḥ | muhūrtta-ahorātra-māsāḥ | muhūrta, day-and-night, and month sequence |
| dvādaśa-māsakaḥ | dvādaśa-māsakaḥ | consisting of twelve months |
| saṃvatsaraḥ | saṃvatsaraḥ | year |
| sonarātraḥ | sa-ahorātraḥ / sa-ūna-rātraḥ? | with day-night / with deficient nights; uncertain |
| kalpaḥ | kalpaḥ | kalpa, aeon |
| bahuvidhaḥ | bahu-vidhaḥ | manyfold, of many kinds |
| smṛtaḥ | smṛtaḥ | remembered, taught, traditionally held |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| trayo | nominative plural masculine | transmitted numeral; exact force uncertain |
| muhūrtta-ahorātra-māsāḥ | compound / nominative plural | time-units in the sequence |
| dvādaśa-māsakaḥ | nominative singular masculine | consisting of twelve months; qualifies `saṃvatsaraḥ` |
| saṃvatsaraḥ | nominative singular masculine | year |
| sonarātraḥ | nominative singular masculine | qualifier of the year; reading uncertain |
| kalpaḥ | nominative singular masculine | kalpa |
| bahuvidhaḥ | nominative singular masculine | manyfold |
| smṛtaḥ | past passive participle | is remembered / is traditionally stated |

## 6. Literal Translation

[From] muhūrta, day-and-night, and months: a year consists of twelve months, with [its] day-and-night relation. The kalpa is remembered as manyfold.

## 7. Philosophical Translation

The time-unit ladder now reaches ordinary calendar time. From the smaller units, the sequence rises through muhūrta, day-and-night, month, and year. The year is made of twelve months. Beyond this, the kalpa is introduced as a manyfold cosmic duration.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| muhūrta | muhūrta | sub-day time-unit |
| ahorātra | day-and-night | complete daily cycle |
| māsa | month | calendar unit composed from days/night cycles |
| dvādaśa | twelve | year-constituting number of months |
| saṃvatsara | year | twelve-month temporal unit |
| kalpa | kalpa / aeon | large cosmic duration-unit |
| bahuvidha | manyfold | indicates that kalpa has multiple kinds |
| smṛta | remembered / taught | doctrinally transmitted classification |

## 9. Doctrinal Determination

VAkK_3.88 completed the distance ladder with yojana and began the micro-time ladder from kṣaṇa upward. VAkK_3.89 continues that time ladder into ordinary and cosmic duration.

```text
kṣaṇa
    → tatkṣaṇa
        → lava
            → muhūrta
                → ahorātra
                    → māsa
                        → saṃvatsara
                            → kalpa
```

The verse ends by saying that kalpa is manyfold. This prepares the next verses, which distinguish kinds of kalpa through world-dissolution and world-formation.

## 10. Logical Determination

This verse completes the ascent from minimal time to cosmic time.

```text
moment
    → sub-day unit
        → day-and-night
            → month
                → year
                    → kalpa
```

Time is not merely duration in general. It is a ladder of nested measures.

## 11. Interpretive Note

This verse is the temporal counterpart to the distance ladder. Just as paramāṇu unfolds into yojana, kṣaṇa unfolds into kalpa.

```text
space-series
    → paramāṇu to yojana

time-series
    → kṣaṇa to kalpa
```

The closing phrase `kalpo bahuvidhaḥ smṛtaḥ` is important. The kalpa is not a single simple unit. It has kinds, and the Kośa will immediately begin classifying them.

## 12. Organon Interpretation

Light contact point:

```text
Kalpa is not vague vastness; it is the upper register of a measured time-ladder.
```

For this pass, we stay close to the Kośa. The world-field becomes fully calculable because both space and time are scaled from analytic minima to cosmic maxima.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_89
    a vak:Karika ;
    rdfs:label "VAK 3.89" ;
    vak:sourceReference "VAkK_3.89" ;
    vak:continues vak:VAK_3_88 ;
    vak:hasTopic vak:TimeMeasureLadder ;
    vak:hasTopic vak:KalpaClassificationOpening ;
    vak:belongsTo vak:MeasureBlock .

vak:TimeMeasureLadder
    a logic:MeasureSeries ;
    rdfs:label "time measure ladder from kṣaṇa to kalpa" ;
    vak:beginsFrom vak:Ksana ;
    vak:hasUnit vak:Muhurta ;
    vak:hasUnit vak:Ahoratra ;
    vak:hasUnit vak:Masa ;
    vak:hasUnit vak:Samvatsara ;
    vak:hasUpperMeasure vak:Kalpa .

vak:Muhurta
    a logic:TimeMeasure ;
    rdfs:label "muhūrta" .

vak:Ahoratra
    a logic:TimeMeasure ;
    rdfs:label "ahorātra" ;
    vak:hasCanonicalTranslation "day-and-night" .

vak:Masa
    a logic:TimeMeasure ;
    rdfs:label "māsa" ;
    vak:hasCanonicalTranslation "month" .

vak:Samvatsara
    a logic:TimeMeasure ;
    rdfs:label "saṃvatsara" ;
    vak:hasCanonicalTranslation "year" ;
    vak:hasMonthCount 12 .

vak:KalpaClassificationOpening
    a logic:DoctrinalOpening ;
    rdfs:label "kalpa is manyfold" ;
    vak:opensTo vak:KalpaTypes .
```

## 14. Commit Note

Committed VAK_3.89 / VAkK_3.89.

Established:
- the time-unit ladder proceeds from moment-scale units into muhūrta, day-and-night, month, and year.
- the year is determined as twelve months.
- kalpa is introduced as manyfold.
- the next verses should classify kalpas through world-contraction and world-expansion.
