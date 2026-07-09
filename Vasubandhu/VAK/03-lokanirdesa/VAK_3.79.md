# VAK_3.79 — Time-Measure: Lifespan of the Lower Kāma-Devas

## 1. Sanskrit — Devanāgarī

```sanskrit
नृणां वर्षाणि पञ्चाशदहोरात्रो दिवौकसाम् ।
कामेऽधराणां तेनायुः पञ्चवर्षशतानि तु ॥ VAkK_3.79 ॥
```

## 2. Sanskrit — IAST

```iast
nṛṇāṃ varṣāṇi pañcāśad ahorātro divaukasām /
kāme 'dharāṇāṃ tenāyuḥ pañcavarṣaśatāni tu // VAkK_3.79 //
```

## 3. Source Caution

The source reading is:

```iast
nṛṇāṃ varṣāṇi pañcāśadahorātro divaukasām /
kāme 'dharāṇāṃ tenāyuḥ pañcavarṣaśatāni tu // VAkK_3.79 //
```

Sandhi has been lightly separated:

```iast
nṛṇām varṣāṇi pañcāśat ahorātraḥ divaukasām /
kāme adharāṇām tena āyuḥ pañca-varṣa-śatāni tu //
```

`kāme 'dharāṇām` is provisionally read as “of the lower [devas] in the kāma realm.” The verse appears to establish the time-conversion for the lower kāma-devas: fifty human years equal one day-and-night of the heavenly dwellers, and by that measure their lifespan is five hundred years.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| nṛṇām | nṛṇām | of humans |
| varṣāṇi | varṣāṇi | years |
| pañcāśat | pañcāśat | fifty |
| ahorātraḥ | ahas-rātraḥ / ahorātraḥ | day-and-night |
| divaukasām | divaukasām | of heavenly dwellers |
| kāme | kāme | in the kāma realm |
| adharāṇām | adharāṇām | of the lower ones |
| tena | tena | by that, by that measure |
| āyuḥ | āyuḥ | lifespan |
| pañca-varṣa-śatāni | pañca-varṣa-śatāni | five hundred years |
| tu | tu | but / indeed |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| nṛṇāṃ varṣāṇi pañcāśat | genitive plural + nominative/accusative plural phrase | fifty human years |
| ahorātraḥ | nominative singular masculine | one day-and-night |
| divaukasām | genitive plural | of the heavenly dwellers |
| kāme 'dharāṇām | locative + genitive plural | of the lower ones in the kāma realm |
| tena | instrumental singular | by that measure |
| āyuḥ | nominative/accusative singular neuter | lifespan |
| pañca-varṣa-śatāni | nominative/accusative plural neuter | five hundred years |

## 6. Literal Translation

Fifty human years are one day-and-night of the heavenly dwellers. By that measure, the lifespan of the lower ones in the kāma realm is five hundred years.

## 7. Philosophical Translation

The Kośa now introduces relative time-scale. For the lower kāma-devas, fifty human years count as a single divine day-and-night; measured in that divine time, their lifespan is five hundred years.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| nṛ | human | reference measure for comparison |
| varṣa | year | human temporal unit |
| pañcāśat | fifty | conversion factor from human to divine time |
| ahorātra | day-and-night | complete daily temporal unit |
| divaukas | heavenly dweller | deva inhabitant |
| kāma | desire realm | field of desire-enjoying devas |
| adhara | lower | lower class within kāma-deva sequence |
| āyuḥ | lifespan | duration of embodied existence |
| pañca-varṣa-śata | five hundred years | lifespan measured by the divine unit |

## 9. Doctrinal Determination

VAkK_3.78 began the time block by giving human lifespans across the continents. VAkK_3.79 now gives the first deva lifespan conversion.

```text
human time
    → 50 human years
        = one day-and-night of lower kāma-devas

lower kāma-deva lifespan
    → 500 divine years by that measure
```

The text therefore does not merely lengthen lifespan; it changes the time-scale by which lifespan is counted.

## 10. Logical Determination

This verse introduces relative temporal measure.

```text
one field's long duration
    = another field's day-and-night
```

The world-field determines not only body-scale but time-scale. A deva does not merely live longer inside the same temporal order; the deva-world has its own proportional time-measure.

## 11. Interpretive Note

This is the first clear shift from simple lifespan to comparative time. The phrase `nṛṇāṃ varṣāṇi pañcāśat` makes human time the comparative base, while `ahorātraḥ divaukasām` converts that base into a divine daily unit.

```text
human years
    → divine day-and-night
    → divine lifespan
```

The Kośa is now measuring temporal experience by realm.

## 12. Organon Interpretation

Light contact point:

```text
A world-field determines its own clock.
```

For this pass, we simply observe the Kośa’s presentation. Loka is not only spatial location and body-measure; it is also a time-regime. Different world-levels do not merely contain beings of different size, but beings whose durations are counted on different scales.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_79
    a vak:Karika ;
    rdfs:label "VAK 3.79" ;
    vak:sourceReference "VAkK_3.79" ;
    vak:continues vak:VAK_3_78 ;
    vak:hasTopic vak:KamaDevaLifespanMeasure ;
    vak:belongsTo vak:TimeMeasureBlock .

vak:KamaDevaLifespanMeasure
    a logic:TemporalMeasure ;
    rdfs:label "lifespan measure of the lower kāma-devas" ;
    vak:hasConversion vak:HumanToDivineDayNight ;
    vak:hasLifespan "500 divine years" .

vak:HumanToDivineDayNight
    a logic:TemporalConversion ;
    rdfs:label "fifty human years equal one divine day-and-night" ;
    vak:hasHumanMeasure "50 years" ;
    vak:hasDivineMeasure "1 day-and-night" .

vak:TimeRegime
    a logic:WorldMeasure ;
    rdfs:label "realm-specific time-regime" .
```

## 14. Commit Note

Committed VAK_3.79 / VAkK_3.79.

Established:
- fifty human years equal one day-and-night of the lower kāma-devas.
- their lifespan is five hundred divine years by that measure.
- the time block now introduces relative temporal scale, not merely longer lifespan.
- a world-field determines its own clock.
