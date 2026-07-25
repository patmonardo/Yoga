# VAkK 4.38

## Sanskrit

### Devanāgarī

> प्रातिमोक्षदमस्त्यागः शिक्षानिक्षेपणाच्च्युतेः ।  
> उभयव्यञ्जनोत्पत्तेर्मूलच्छेदान्निशात्ययात् ॥ ४.३८ ॥

### IAST

> **prātimokṣadamas tyāgaḥ śikṣānikṣepaṇāc cyuteḥ |**  
> **ubhayavyañjanotpatter mūlacchedān niśātyayāt || 4.38 ||**

The first expression resolves by sandhi as:

```text
prātimokṣa-damaḥ + tyāgaḥ
    → prātimokṣa-damas tyāgaḥ
```

The verse begins the section on abandonment or loss of restraints.

## Padaccheda

```text
prātimokṣa-damaḥ
tyāgaḥ

śikṣā-nikṣepaṇāt
cyuteḥ |

ubhaya-vyañjana-utpatteḥ

mūla-cchedāt

niśā-atyayāt ||
```

Expanded syntax:

```text
prātimokṣadamas tyāgaḥ
    śikṣānikṣepaṇāt
    cyuteḥ
    ubhayavyañjanotpatteḥ
    mūlacchedāt
    niśātyayāt
```

The abandonment of prātimokṣa restraint occurs through laying down the training, death, the arising of both sexual characteristics, severance of the roots, and the passing of the night. These causes do not necessarily apply identically to every subtype of prātimokṣa restraint; the passing of the night applies to the one-day upavāsa restraint.

## Grammar

| Form | Analysis | Meaning |
|---|---|---|
| **prātimokṣa-damaḥ** | nominative singular masculine | prātimokṣa discipline or restraint |
| **tyāgaḥ** | nominative singular masculine | abandonment, relinquishment, loss |
| **śikṣā-nikṣepaṇāt** | ablative singular | through laying down the training |
| **cyuteḥ** | ablative singular feminine | through death, falling away |
| **ubhaya-vyañjana-utpatteḥ** | ablative singular feminine | through the arising of both sexual characteristics |
| **mūla-cchedāt** | ablative singular | through cutting off the roots |
| **niśā-atyayāt** | ablative singular | through the passing of the night |

## Literal translation

> **Prātimokṣa restraint is abandoned through laying down the training, through death, through the arising of both sexual characteristics, through severance of the roots, and through the passing of the night.**

The final cause, the passing of the night, pertains to the temporally limited upavāsa restraint.

## Philosophical translation

> **The discipline of individual liberation ceases under determinate conditions: it may be deliberately relinquished, lose its living bearer at death, become incompatible with a transformed bodily basis, lose the wholesome roots that sustain it, or simply reach the completion of its stipulated term. The disappearance of restraint is therefore not a single undifferentiated event; it is a state transition whose ground must be precisely recorded.**

## Doctrinal determination

### Laying down the training

**śikṣānikṣepaṇa** is the deliberate relinquishment of the discipline. This is stronger than a breach. A breach is failure under an acknowledged rule; laying down the training terminates the standing relation itself.

```text
undertaking
    → acquisition of restraint

laying down the training
    → abandonment of restraint
```

### Death

**cyuti** terminates the present living basis that bears prātimokṣa restraint. The karmic results of prior observance or violation may continue, but possession of that disciplinary status ceases.

```text
active restraint-status
    ceases

historical karmic efficacy
    may continue
```

### Arising of both sexual characteristics

**ubhayavyañjanotpatti** concerns a transformation of the bodily basis relevant to the disciplinary category under which restraint was received. The technical point concerns compatibility between vow-type and qualifying bodily basis; the exact institutional consequences require the Bhāṣya.

### Severance of the roots

**mūlaccheda** most likely means severance of the roots of good. The standard wholesome roots are non-greed, non-hatred, and non-delusion. Their radical destruction removes the causal support upon which restraint depends.

```text
particular transgression
    damages observance

mūlaccheda
    destroys the wholesome basis
    supporting restraint
```

### Passing of the night

**niśātyaya** applies to upavāsa. Here cessation is not failure but fulfillment of the vow's own temporal measure.

```text
duration completed
    → restraint ceases
```

## Five modes of loss

| Cause | Type of loss |
|---|---|
| **śikṣānikṣepaṇa** | voluntary normative relinquishment |
| **cyuti** | cessation of the present bearer |
| **ubhayavyañjanotpatti** | transformation of qualifying bodily basis |
| **mūlaccheda** | destruction of wholesome causal support |
| **niśātyaya** | completion of stipulated duration |

These span distinct dimensions:

```text
intention
bearer
body
causal ground
time
```

## Logical determination

A possessed restraint can terminate through changes in different constitutive relations:

```text
1. acknowledgment
2. bearer
3. bodily qualification
4. causal ground
5. temporal measure
```

Formally:

```text
RESTRAINT-PRESENT
    iff

commitment-valid
and bearer-living
and basis-compatible
and roots-intact
and term-unexpired
```

Loss is not one homogeneous negation. Each condition negates a different relation constituting the restraint's actuality.

## Logic of Experience

A System of Dharma must record not merely what exists but how a determination is acquired, supported, borne, measured, and lost.

```text
DHARMA-RECORD
    acquired-by
    borne-by
    sustained-by
    scoped-by
    lost-by
```

VAkK 4.38 supplies an explicit termination schema. A dharma does not disappear abstractly; it ceases through a determinate alteration in commitment, bearer, basis, ground, or time.

## Typed feature structure

```text
[ PRATIMOKSHA-RESTRAINT
  STATUS          possessed
  BEARER          living-continuum
  BASIS           compatible-body-basis
  WHOLESOME-ROOTS intact
  TERM            active ]
```

Loss transitions:

```text
[ LOSS-CONDITION
  TYPE voluntary
  EVENT laying-down-training ]

[ LOSS-CONDITION
  TYPE bearer-cessation
  EVENT death ]

[ LOSS-CONDITION
  TYPE basis-transformation
  EVENT arising-of-both-sexual-characteristics ]

[ LOSS-CONDITION
  TYPE ground-destruction
  EVENT severance-of-wholesome-roots ]

[ LOSS-CONDITION
  TYPE term-completion
  EVENT passing-of-night
  APPLIES-TO upavāsa ]
```

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_38
    a vak:Karika ;
    rdfs:label "VAK 4.38" ;
    vak:continues vak:VAK_4_37 ;
    vak:hasTopic vak:LossOfPratimokshaRestraint .

vak:PratimokshaRestraint
    vak:mayBeLostThrough vak:LayingDownTraining ;
    vak:mayBeLostThrough vak:Death ;
    vak:mayBeLostThrough vak:ArisingOfBothSexualCharacteristics ;
    vak:mayBeLostThrough vak:SeveranceOfWholesomeRoots .

vak:UpavasaRestraint
    rdfs:subClassOf vak:PratimokshaRestraint ;
    vak:mayBeLostThrough vak:PassingOfNight .
```

## Determinate result

VAkK 4.38 establishes that prātimokṣa restraint can be lost through laying down the training, death, transformation of the qualifying bodily basis, severance of the wholesome roots, and completion of the upavāsa term.

Its central principle is:

```text
a dharma ceases
not through abstract disappearance,

but through a determinate change
in commitment, bearer, basis,
ground, or temporal measure
```
