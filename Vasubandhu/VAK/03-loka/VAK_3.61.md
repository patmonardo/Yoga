# VAK_3.61 — Bhājanaloka: Seasonal Increase and Decrease of Night and Day

## 1. Sanskrit — Devanāgarī

```sanskrit
प्रावृण्मासे द्वितीयेऽन्त्यनवम्यां वर्धते निशा ।
हेमन्तानां चतुर्थे तु हीयतेऽहर्विपर्ययात् ॥ VAkK_3.61 ॥
```

## 2. Sanskrit — IAST

```iast
prāvṛṇmāse dvitīye 'ntyanavamyāṃ vardhate niśā /
hemantānāṃ caturthe tu hīyate 'har viparyayāt // VAkK_3.61 //
```

## 3. Source Caution

The source reading is:

```iast
prāvṛṇmāse dvitīye 'ntyanavamyāṃ vardhate niśā /
hemantānāṃ caturthe tu hīyate aharviparyayāt // VAkK_3.61 //
```

Sandhi has been lightly separated:

```iast
prāvṛṇ-māse dvitīye antya-navamyām vardhate niśā /
hemantānām caturthe tu hīyate ahaḥ viparyayāt //
```

`antya-navamī` is provisionally read as the final ninth lunar day within the second rainy-season month. The precise calendrical reference should be checked against the bhāṣya.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| prāvṛṇmāse | prāvṛṇ-māse | in the rainy-season month |
| dvitīye | dvitīye | in the second |
| 'ntyanavamyām | antya-navamyām | on the final ninth day; provisional |
| vardhate | vardhate | increases, grows |
| niśā | niśā | night |
| hemantānām | hemantānām | of the winter-season months |
| caturthe | caturthe | in the fourth |
| tu | tu | but / however |
| hīyate | hīyate | decreases, diminishes |
| ahaḥ | ahaḥ | day |
| viparyayāt | viparyayāt | by reversal; conversely |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| prāvṛṇ-māse | locative singular masculine | temporal location: in the rainy-season month |
| dvitīye | locative singular | specifies the second month |
| antya-navamyām | locative singular feminine | specifies a calendrical day |
| vardhate | present middle, 3rd singular | “increases” |
| niśā | nominative singular feminine | subject: night |
| hemantānām | genitive plural masculine/neuter | of the winter months; seasonal specification |
| caturthe | locative singular | in the fourth |
| hīyate | present passive/middle, 3rd singular | “decreases” |
| ahaḥ | nominative/accusative singular neuter | day |
| viparyayāt | ablative singular masculine | by reversal, from the contrary case |

## 6. Literal Translation

In the second month of the rainy season, on the final ninth day, the night increases. In the fourth of the winter months, however, the day decreases, by reversal.

## 7. Philosophical Translation

After establishing simultaneous local day-moments, the text marks the annual variation of night and day. Night begins to increase from a specified point in the rainy season; by the reverse seasonal relation, day diminishes from a specified point in winter.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| prāvṛṣ / prāvṛṭ | rainy season | seasonal register; here in compound `prāvṛṇ-māsa` |
| māsa | month | calendrical unit |
| dvitīya | second | ordinal determination |
| antya-navamī | final ninth day | lunar-day marker; provisional |
| vardhate | increases | growth of night-duration |
| niśā | night | temporal half of the day-night cycle |
| hemanta | winter | seasonal register |
| caturtha | fourth | ordinal determination |
| hīyate | decreases | diminution of day-duration |
| ahaḥ | day | temporal half of the day-night cycle |
| viparyaya | reversal | contrary correspondence of day and night |

## 9. Doctrinal Determination

VAkK_3.60 established that sunrise, midday, sunset, and midnight occur simultaneously for different positions in the world-system. VAkK_3.61 now adds seasonal variation.

```text
local temporal differentiation
    → seasonal increase/decrease
```

The world-container is therefore ordered not only spatially and diurnally, but calendrically.

## 10. Logical Determination

This verse introduces cyclic opposition.

```text
night increases
    ↔
day decreases
```

The determinate world is a field of reciprocal temporal magnitudes. Increase on one side is decrease on the opposed side.

## 11. Interpretive Note

The important first-pass point is the logic of temporal contraries. The verse does not merely report a calendrical fact. It shows that day and night form a reciprocal measure-system.

```text
niśā / ahaḥ
    = opposed temporal magnitudes
```

This belongs to the larger bhājanaloka determination: the container-world has its own order of measure, alternation, and reversal.

## 12. Organon Interpretation

Light contact point:

```text
Temporal measure appears as reciprocal variation.
```

This is a clean cosmological example of determinate opposition: one temporal magnitude grows as the other is reduced. The empirical field is already logically articulated as relation, not mere sequence.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_61
    a vak:Karika ;
    rdfs:label "VAK 3.61" ;
    vak:sourceReference "VAkK_3.61" ;
    vak:continues vak:VAK_3_60 ;
    vak:hasTopic vak:SeasonalDayNightVariation ;
    vak:belongsTo vak:BhajanalokaBlock .

vak:SeasonalDayNightVariation
    a logic:TemporalMeasure ;
    rdfs:label "seasonal increase and decrease of night and day" ;
    vak:hasOpposedMagnitude vak:NightDuration ;
    vak:hasOpposedMagnitude vak:DayDuration .

vak:NightDuration
    a logic:TemporalMagnitude ;
    rdfs:label "niśā" ;
    vak:hasCanonicalTranslation "night" .

vak:DayDuration
    a logic:TemporalMagnitude ;
    rdfs:label "ahaḥ" ;
    vak:hasCanonicalTranslation "day" .
```

## 14. Commit Note

Committed VAK_3.61 / VAkK_3.61.

Established:
- seasonal increase of night and reciprocal decrease of day.
- `niśā` and `ahaḥ` as opposed temporal magnitudes.
- `viparyaya` as reversal / contrary correspondence.
- bhājanaloka as a calendrical field of measure and temporal opposition.
