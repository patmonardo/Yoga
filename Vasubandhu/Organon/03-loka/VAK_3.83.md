# VAK_3.83

## 1. Sanskrit (Devanāgarī)

> अर्धं प्रतापनेऽवीचावन्तःकल्पं परं पुनः ।
>
> कल्पं तिरश्चां प्रेतानां मासाह्ना शतपञ्चकम् ॥ ३.८३ ॥

## 2. Sanskrit (IAST)

> ardhaṃ pratāpane 'vīcāv antaḥkalpaṃ paraṃ punaḥ /
>
> kalpaṃ tiraścāṃ pretānāṃ māsāhnā śatapañcakam // 3.83 //

The compressed final compound is presented as `māsāhnā`, following the
Bhāṣya's citation and explanation: with a day-and-night whose magnitude is one
human month. The immediate metrical witness has an unstable letter-order at
this point, but the intended temporal conversion is secure.

## 3. Lexical Analysis

```text
ardham                → ardhaṃ
pratāpane             → pratāpane
avīcau                → 'vīcau (after avagraha) → 'vīcāv (before a-)
antar-kalpam          → antaḥkalpam
param                 → param
punaḥ                 → punaḥ
kalpam                → kalpaṃ
tiraścām              → tiraścāṃ
pretānām              → pretānāṃ
māsa-ahnā             → māsāhnā
śata-pañcakam         → śatapañcakam
```

| Form | Morphology | Lexical force here |
|---|---|---|
| ardham | nominative/accusative neuter singular | half, resolved as half an antarakalpa |
| pratāpane | locative masculine singular | in the Pratāpana great naraka |
| avīcau | locative masculine singular | in Avīci |
| antaḥkalpam | nominative/accusative neuter singular compound | one intermediate kalpa |
| param | nominative/accusative neuter singular | maximum, upper limit in the animal clause |
| punaḥ | indeclinable | in turn; introduces a distinct determination |
| kalpam | nominative/accusative neuter singular | one kalpa, resolved here as one antarakalpa |
| tiraścām | genitive plural | of animals |
| pretānām | genitive plural | of pretas |
| māsāhnā | instrumental singular compound | by a day-and-night equal to one human month |
| śatapañcakam | nominative/accusative neuter singular | five hundreds, five hundred years |

The Bhāṣya is required to supply the omitted unit after `ardham`, the modal
force of `param`, and the complete calendar relation compressed into
`māsāhnā`.

## 4. Grammar

The first two clauses assign fixed lifespans to the remaining principal hot
narakas:

```text
pratāpane
    [āyuḥ-pramāṇam]
    ardham [antar-kalpasya]

avīcau
    [āyuḥ-pramāṇam]
    antaḥ-kalpam
```

> In Pratāpana the lifespan is half an antarakalpa; in Avīci it is one
> antarakalpa.

The animal clause has a different modal structure:

```text
tiraścām
    param [āyuḥ]
    punaḥ antaḥ-kalpam
```

> For animals, in turn, the maximum lifespan is one antarakalpa.

The Bhāṣya explicitly precedes this with `niyamo nāsti`, “there is no fixed
rule.” Consequently `param` qualifies the kalpa as an upper bound; it does not
assign every animal a kalpa-long life.

The final clause establishes a preta conversion and lifespan:

```text
pretānām
    [manuṣyāṇāṃ] māsaḥ = [ekaṃ] ahorātram
    tena [māsāhnā]
    [āyuḥ] śata-pañcakam [varṣāṇām]
```

> For pretas, one human month is a day-and-night; reckoned by that unit, their
> lifespan is five hundred years.

## 5. Translation

### Close syntactic construe

> In Pratāpana it is one half; in Avīci, one antarakalpa. For animals, in
> turn, the maximum is a kalpa. For pretas, reckoned by a month-long
> day-and-night, it is five hundred.

### Bhāṣya-informed study translation

> Lifespan in the Pratāpana great naraka is half an antarakalpa, and in Avīci
> it is one antarakalpa. Animals have no single fixed lifespan; their maximum
> is one antarakalpa, attained by exceptional great nāgas such as Nanda and
> Upananda. For pretas, one human month constitutes one day-and-night, and
> measured by that calendar their lifespan is five hundred preta years.

The antarakalpa supplied after `ardham`, the absence of a fixed animal
lifespan, the great-nāga examples, and the explicit human-to-preta conversion
are Bhāṣya determinations.

## 6. Philosophical Translation

> A World-domain need not determine duration through one logical form. It can
> assign a fixed constant, permit variable lifespans under a determinate upper
> bound, or construct a realm-specific clock through conversion from another
> domain. The lower destinies are therefore not undifferentiated immensities:
> each carries a precise temporal policy appropriate to its class of
> embodiment.

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| Pratāpana | Pratāpana | seventh principal hot naraka; lifespan ½ antarakalpa |
| Avīci | Avīci | eighth principal hot naraka; lifespan 1 antarakalpa |
| antarakalpa | intermediate kalpa | fixed naraka unit and maximum animal lifespan |
| tiryañc | animal | destiny with variable lifespan rather than one fixed value |
| niyama | fixed determination / uniform rule | explicitly absent for animal lifespan |
| paramāyus | maximum lifespan | upper bound of 1 antarakalpa for animals |
| kalpastha | remaining for a kalpa | description supporting the exceptional great-nāga maximum |
| preta | preta | destiny with a month-to-day temporal conversion |
| māsa | month | one human month supplies one preta day-night |
| ahorātra | day-and-night | basic unit of the preta calendar |
| śatapañcaka | five hundred | local-year count of the preta lifespan |

`preta` is retained as the technical name of the destiny because a narrower
English image would exceed this temporal determination.

## 8. Logical Determination

### Fixed-duration schema

The two naraka cases are constants:

```text
Lifespan(Pratāpana) = 0.5 antarakalpa
Lifespan(Avīci)     = 1 antarakalpa
```

The Bhāṣya identifies these as `āyuḥpramāṇa`, measures of lifespan, without
introducing variability or an upper-bound qualifier.

### Bounded-variable schema

The animal case must be represented by two predicates:

```text
hasFixedLifespan(AnimalRealm) = false
maximumLifespan(AnimalRealm)  = 1 antarakalpa
```

The witness for the maximum is exceptional:

```text
great nāgas such as Nanda and Upananda
    → can remain for one antarakalpa
```

It would be a type error to convert the maximum into:

```text
lifespanEveryAnimal = 1 antarakalpa
```

### Converted-calendar schema

Let `HM` be one human month and `PD` one preta day-night:

```text
1 PD = 1 HM
30 PD = 1 preta month
12 preta months = 1 preta year
500 preta years = 1 preta lifespan
```

Assuming the same thirty-day, twelve-month calendar structure made explicit
in the preceding lifespan calculations, the complete conversion is:

```text
1 preta lifespan
    = 500 × 12 × 30 human months
    = 180,000 human months
    = 15,000 human years
```

The 15,000-year result is a derived calendrical consequence, not a figure
separately stated in the verse or its Bhāṣya.

### Modal dispatch

The verse requires a sum type rather than one universal duration field:

```text
TemporalDetermination =
    FixedDuration(value)
    | VariableWithMaximum(maximum)
    | ConvertedCalendar(conversion, localYearCount)
```

| Domain | Applicable determination |
|---|---|
| Pratāpana | fixed duration |
| Avīci | fixed duration |
| animals | variable with maximum |
| pretas | converted calendar with fixed local-year count |

## 9. Interpretive Note

VAK 3.83 gives a powerful methodological correction to simplistic world
modelling. Determinacy is not synonymous with assigning one value. A domain
can be rigorously determined by a bound even when its actual instances vary:

```text
no fixed value
    ≠ no determination

variable values + explicit maximum
    = bounded determination
```

This is the semantic force that a merely syntactic catalogue would miss. The
word `kalpa` occurs beside animals, but the Bhāṣya changes the predicate from
“has lifespan” to “has maximum lifespan.” The number and unit remain the same;
the modal operator changes their truth-condition.

The verse now supplies three temporal interfaces inside one compact statement:

```text
constant assignment
    → exact duration

constraint assignment
    → permitted variability under an upper bound

conversion assignment
    → foreign duration becomes local clock-unit
```

The Physical World is agential because correct operation depends on knowing
which interface a domain exposes. An agent that stores only `<realm, number,
unit>` will falsely universalize the animal maximum. It must also preserve the
mode under which the measure is asserted.

```ts
type TemporalDetermination =
  | { mode: "Fixed"; durationInAntarakalpas: number }
  | { mode: "Variable"; maximumInAntarakalpas: number }
  | {
      mode: "ConvertedCalendar";
      sourceUnit: "HumanMonth";
      targetUnit: "PretaDayNight";
      localLifespanYears: 500;
    };
```

This is explanatory project notation, not Vasubandhu's terminology. Its modal
tag is the minimum structure needed to preserve the Bhāṣya's distinctions.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:VAK_3_83
    a vak:Karika ;
    vak:continues vak:VAK_3_82 ;
    vak:describes loka:LowerDestinyTemporalDeterminations .

loka:PratapanaLifespan
    a organon:FixedDuration ;
    organon:hasUnit loka:Antarakalpa ;
    organon:hasMagnitude 0.5 .

loka:AviciLifespan
    a organon:FixedDuration ;
    organon:hasUnit loka:Antarakalpa ;
    organon:hasMagnitude 1 .

loka:AnimalLifespan
    a organon:BoundedVariableDuration ;
    organon:hasFixedDetermination false ;
    organon:hasMaximumUnit loka:Antarakalpa ;
    organon:hasMaximumMagnitude 1 ;
    organon:maximumExemplifiedBy loka:GreatNagas .

loka:PretaTemporalRegime
    a organon:ConvertedCalendar ;
    organon:hasSourceUnit loka:HumanMonth ;
    organon:hasSourceMagnitude 1 ;
    organon:hasTargetUnit loka:PretaDayNight ;
    organon:hasTargetMagnitude 1 ;
    organon:hasLifespanInLocalYears 500 .

organon:TemporalMeasureAssertion
    organon:requiresProperty organon:AssertionMode,
                             organon:Quantity,
                             organon:Unit .
```
