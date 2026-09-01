# VAK_3.61

## 1. Sanskrit (Devanāgarī)

> प्रावृण्मासे द्वितीयेऽन्त्यनवम्यां वर्धते निशा ।
>
> हेमन्तानां चतुर्थे तु हीयतेऽहर्विपर्ययात् ॥ ३.६१ ॥

## 2. Sanskrit (IAST)

> prāvṛṇmāse dvitīye 'ntyanavamyāṃ vardhate niśā /
>
> hemantānāṃ caturthe tu hīyate 'har viparyayāt // 3.61 //

## 3. Lexical Analysis

```text
prāvṛṭ-māse                → prāvṛṇmāse
dvitīye                    → dvitīye
antya-navamyām             → 'ntyanavamyāṃ
vardhate                   → vardhate
niśā                       → niśā
hemantānām                 → hemantānāṃ
caturthe                   → caturthe
tu                         → tu
hīyate                     → hīyate
ahaḥ                       → 'har
viparyayāt                 → viparyayāt
```

| Form | Morphology | Lexical force here |
|---|---|---|
| prāvṛṇmāse | locative masculine singular compound | in a rainy-season month |
| dvitīye | locative singular ordinal | in the second month |
| antyanavamyām | locative feminine singular compound | on the ninth day of the latter/second fortnight |
| vardhate | third-person singular present middle | increases, grows |
| niśā | nominative feminine singular | night-duration |
| hemantānām | genitive plural | of the winter months |
| caturthe | locative singular ordinal | in the fourth month |
| hīyate | third-person singular present middle/passive | diminishes, decreases |
| ahaḥ | nominative neuter singular | day-duration |
| viparyayāt | ablative masculine singular | by inverse relation, conversely |

The Bhāṣya corrects a tempting but imprecise reading of `antyanavamī`: it is
not simply a “final ninth day,” but the ninth day of the second fortnight.

## 4. Grammar

The first clause fixes a calendrical trigger and its process:

```text
prāvṛṇ-māse dvitīye
    antya-navamyām
    niśā vardhate
```

The Bhāṣya resolves this as Bhādrapada, second fortnight, ninth day.

The second clause carries forward `antyanavamyām`:

```text
hemantānāṃ caturthe [māse]
    [antyanavamyām]
    sā [niśā] hīyate
```

The Bhāṣya identifies this as Phālguna, second fortnight, ninth day. The final
phrase supplies the inverse dependency:

```text
ahaḥ
    [niśāyāḥ] viparyayāt
```

Day varies oppositely to night; it is not the independent subject of only the
second seasonal clause.

## 5. Translation

### Close syntactic construe

> In the second month of the rains, on the ninth day of the latter fortnight,
> night increases. In the fourth winter month, however, it decreases; day is
> the inverse.

### Bhāṣya-informed study translation

> On the ninth day of the second fortnight of Bhādrapada, night begins to
> increase and day correspondingly decreases. On the ninth day of the second
> fortnight of Phālguna, night begins to decrease and day correspondingly
> increases.

The named months, interpretation of the fortnight and lunar day, carried-
forward date in the second clause, and explicit two-way inverse relation are
Bhāṣya determinations.

## 6. Philosophical Translation

> The synchronized World System now acquires calendrical dynamics. Two opposed
> temporal magnitudes vary within one day–night whole: as one increases, the
> other decreases. Named calendar coordinates mark the points at which the
> direction of variation reverses. Time is therefore modeled neither as a row
> of isolated dates nor as undifferentiated flow, but as a cyclic process whose
> state, direction, and reciprocal magnitudes can be determined at indexed
> transition points.

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| Bhādrapada | Bhādrapada | second rainy-season month in the Bhāṣya's calendar |
| Phālguna | Phālguna | fourth winter month in the Bhāṣya's calendar |
| pakṣa | fortnight | calendrical subdivision used to resolve `antya` |
| antyanavamī | ninth day of the second fortnight | transition-day within each named month |
| niśā / rātri | night | one magnitude within the day–night whole |
| ahaḥ / divasa | day | reciprocally varying magnitude |
| vardhate | increases | positive direction of variation |
| hīyate | decreases | negative direction of variation |
| viparyaya | inverse relation / reversal | rule coupling day and night changes |

The two transition specifications are:

| Calendar index | Night direction | Day direction |
|---|---|---|
| Bhādrapada, second fortnight, day 9 | increasing | decreasing |
| Phālguna, second fortnight, day 9 | decreasing | increasing |

## 8. Logical Determination

### Reciprocal magnitudes within one whole

```text
day-duration + night-duration = one day–night whole
```

Accordingly:

```text
night ↑  → day ↓
night ↓  → day ↑
```

`Viparyaya` expresses coupled inverse variation, not merely the succession of
two contrary events.

### Transition points change direction, not existence

```text
at Bhādrapada index:
    direction(night) := increasing
    direction(day)   := decreasing

at Phālguna index:
    direction(night) := decreasing
    direction(day)   := increasing
```

The calendar event changes the trend-state of each magnitude. Day and night
continue throughout; what reverses is their direction of change.

### Calendar as an address system for process-state

```text
month
    + fortnight
        + lunar day
            → indexed transition event
```

The date is a three-field temporal address. Its semantic value lies in the
process transition associated with it, not in the labels considered alone.

### Conservation under reciprocal redistribution

The text does not formulate an algebraic conservation law, but its inverse
relation supports the restrained model:

```text
increase in one member
    ↔ corresponding decrease in its complement
```

This is redistribution within a paired temporal whole. The exact daily
increment is supplied only by 3.62 and should not be imported prematurely.

## 9. Interpretive Note

VAK 3.61 extends 3.60 from locale-indexed state to calendar-indexed process.
The two verses together yield:

```text
region index
    → which temporal phase is locally present

calendar index
    → in which direction its duration is changing
```

This is methodically important. A complete world-state is not specified by a
time label alone. It requires both current phase and trend. “Night” may be
present while night-duration is either increasing or decreasing; state and
derivative are distinct determinations.

For the Semantic pipeline:

```ts
interface IndexedTemporalProcess {
  calendarAddress: {
    month: "Bhadrapada" | "Phalguna";
    fortnight: 2;
    lunarDay: 9;
  };
  nightTrend: "increasing" | "decreasing";
  dayTrend: "decreasing" | "increasing";
  relation: "inverse";
}
```

This is explanatory notation, not Vasubandhu's vocabulary. It exposes the
method behind the calendar data: a temporal address selects a transition in a
coupled cyclic process.

The Agential relevance is quieter than in the hell verses but still real. The
calendar is a shared environmental state-machine within which embodied Agents
coordinate activity. Loka supplies not merely locations but the changing
temporal conditions under which action becomes situated—another necessary
precondition for Karma's practical analysis.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:VAK_3_61
    a vak:Karika ;
    vak:describes loka:SeasonalDayNightProcess ;
    vak:hasCommentarialDetermination loka:CalendarTransitionIndexes .

loka:BhadrapadaTransition
    loka:hasFortnight 2 ;
    loka:hasLunarDay 9 ;
    loka:setsNightTrend loka:Increasing ;
    loka:setsDayTrend loka:Decreasing .

loka:PhalgunaTransition
    loka:hasFortnight 2 ;
    loka:hasLunarDay 9 ;
    loka:setsNightTrend loka:Decreasing ;
    loka:setsDayTrend loka:Increasing .

loka:SeasonalDayNightProcess
    loka:hasMagnitude loka:NightDuration,
        loka:DayDuration ;
    loka:hasRelation loka:InverseVariation ;
    loka:hasTransition loka:BhadrapadaTransition,
        loka:PhalgunaTransition .

organon:CalendarIndexedStateTransition
    a organon:ProjectInterpretation ;
    organon:requires organon:Month,
        organon:Fortnight,
        organon:LunarDay ;
    organon:changes organon:ProcessTrend ;
    organon:preserves organon:CoupledTemporalWhole .
```
