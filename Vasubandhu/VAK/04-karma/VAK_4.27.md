# VAK_4.27

## Sanskrit — Devanāgarī

```sanskrit
यावज्जीवं समादानमहोरात्रं च संवृतेः ।
नासंवरोऽस्त्यहोरात्रं न किलैवं प्रगृह्यते ॥
```

## Sanskrit — IAST

```iast
yāvajjīvaṃ samādānam ahorātraṃ ca saṃvṛteḥ |
nāsaṃvaro 'sty ahorātraṃ na kilaivaṃ pragṛhyate ||
```

## Source reference and caution

Source: `VAkK_4.27`.

The verse determines the duration for which restraint and non-restraint are undertaken.

```text
4.26
    how restraint is acquired

4.27
    for how long it is acquired
```

The source reads `saṃvṛteḥ`; in context this refers to restraint and should not be confused with the philosophical use of `saṃvṛti` as convention.

## Padaccheda

```text
yāvat-jīvam
samādānam
aho-rātram
ca
saṃvṛteḥ

na
asaṃvaraḥ
asti
aho-rātram

na
kila
evam
pragṛhyate
```

| Form | Analysis | Working meaning |
|---|---|---|
| `yāvajjīvam` | indeclinable adverbial compound | for as long as life lasts |
| `samādānam` | neuter singular | undertaking; assumption |
| `ahorātram` | accusative singular used adverbially | for a day and night |
| `saṃvṛteḥ` | genitive singular | of restraint |
| `asaṃvaraḥ` | nominative singular | non-restraint |
| `kila` | reportive particle | according to the established account |
| `pragṛhyate` | passive of `pra-grah` | is formally undertaken |

## Literal translation

> The undertaking of restraint is for life or for one day and night. Non-restraint does not exist for merely a day and night, because it is not undertaken in that manner.

## Philosophical translation

> Prātimokṣa restraint may be intentionally assumed either as a lifelong discipline or as a complete day-and-night observance. Non-restraint, however, is not recognized as a temporary one-day institution, because it is not formally taken up under such a limited determination.

## Technical analysis

### `samādāna`

`samādāna` is the intentional taking-up of restraint.

```text
formal undertaking
    → acquisition
    → continuing possession
```

### `yāvajjīvam`

The restraint is assumed for as long as life lasts.

```text
lifelong undertaking
    → lifelong restraint-form
```

### `ahorātram`

The compound denotes one complete day-and-night period, the duration of the temporary upavāsa observance.

```text
day-night undertaking
    → day-night restraint-form
```

### No one-day non-restraint

The verse does not deny that harmful action can occur for one day. It denies that such action thereby constitutes a formally limited one-day `asaṃvara`.

```text
a day of harmful action
    ≠
one-day asaṃvara
```

Non-restraint is a standing practical orientation rather than a temporary ritual institution.

## Typed feature structure

```text
[ RESTRAINT-TYPE  prātimokṣa
  UNDERTAKING     intentional
  DURATION        lifetime | day-night ]
```

But not:

```text
[ FORM            asaṃvara
  DURATION        day-night
  ACQUISITION     bounded undertaking ]
```

## Doctrinal determination

1. Prātimokṣa restraint may be undertaken for life.
2. Temporary upavāsa restraint is undertaken for one day and night.
3. Non-restraint is not acquired as an explicitly one-day form.
4. Temporary harmful conduct must not be confused with temporary `asaṃvara`.

## Logical determination

The temporal extent belongs internally to the undertaking itself.

```text
undertaking
    is generated together with its duration
```

A finite vow is nevertheless complete because its limit is self-determined.

```text
finite duration
    does not make the form unreal
```

The asymmetry between restraint and non-restraint is grounded in their different modes of genesis, not in a merely external moral opposition.

## Relation to VAK_4.25–4.26

```text
VAK_4.25
    manifest action and persistent form are separable

VAK_4.26
    the three restraints have distinct modes of acquisition

VAK_4.27
    prātimokṣa undertaking includes its temporal determination
```

## Light Organon interpretation

Time is an internal moment of practical form. The undertaking is not first complete and then externally assigned a duration.

```text
lifelong restraint
    self-determines as life-long

upavāsa restraint
    self-determines as day-and-night
```

`asaṃvara` is not the perfectly symmetrical inversion of every feature of restraint. Structural opposition does not entail external feature-by-feature symmetry.

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_27
    a vak:Karika ;
    rdfs:label "VAK 4.27" ;
    vak:continues vak:VAK_4_26 ;
    vak:hasTopic vak:DurationOfUndertaking .

vak:LifelongRestraint
    rdfs:subClassOf vak:PratimokshaRestraint ;
    vak:hasDuration vak:Lifetime .

vak:DayNightRestraint
    rdfs:subClassOf vak:PratimokshaRestraint ;
    vak:hasDuration vak:OneDayAndNight .

vak:NonRestraint
    vak:doesNotHaveRecognizedDuration vak:OneDayAndNight .
```

## Verse summary

```text
VAK_4.27

Restraint may be undertaken:
    for life
    or for one day and night.

Non-restraint is not acquired
as a one-day form.

The duration of restraint
is internal to the undertaking
that generates it.
```
