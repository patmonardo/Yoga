# VAK_2.45

## 1. Sanskrit (Devanāgarī)

> आयुर्जीवितमाधार ऊष्मविज्ञायोर्हि यः ।
>
> लक्षणानि पुनर्जातिर्जरा स्थितिरनित्यता ॥ २.४५ ॥

## 2. Sanskrit (IAST)

> āyur jīvitam ādhāra ūṣmavijñāyor hi yaḥ /
>
> lakṣaṇāni punar jātir jarā sthitir anityatā // 2.45 //

## 3. Lexical Analysis

```text
āyur               → āyuḥ
jīvitam            → jīvitam
ādhāra             → ādhāraḥ
ūṣmavijñāyor       → ūṣma-vijñānayoḥ
lakṣaṇāni          → lakṣaṇāni
jātir jarā sthitir → jātiḥ jarā sthitiḥ
anityatā           → anityatā
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| āyuḥ | nominative neuter singular | lifespan |
| jīvitam | nominative neuter singular | life-continuity |
| ādhāraḥ | nominative masculine singular | support |
| ūṣma-vijñānayoḥ | genitive dual compound | of vital heat and Cognition |
| lakṣaṇāni | nominative neuter plural | marks of the conditioned |
| jātiḥ | nominative feminine singular | arising |
| jarā | nominative feminine singular | aging or alteration |
| sthitiḥ | nominative feminine singular | persistence |
| anityatā | nominative feminine singular | impermanence |

## 4. Scientific English Rendering

> Lifespan is life-continuity: that which supports vital heat and Cognition.
> The marks, in turn, are arising, aging, persistence, and impermanence.

The Bhāṣya reports the Vaibhāṣika account of life as a distinct real
support, then argues that no additional life-substance is required. Life is
the persistence-duration projected for a homogeneous continuum by karma.

## 5. Interpretation

This verse supplies the distinction required by the cessation-attainment
argument. Cessation of consciousness and associated mental factors does not
itself mean death, because life-continuity is not defined as their momentary
manifest operation. It is the karmically projected duration of a homogeneous
continuum, supporting vital heat and Cognition within its proper range.

The Bhāṣya therefore distinguishes:

```text
Life-continuity:
    projected duration of the living continuum

Consciousness-operation:
    a present operation which may be prevented for an interval

Death:
    cessation at the exhaustion of lifespan;
    other causal losses can accompany it, while violent or unequal
    conditions can end a life prematurely
```

The four marks likewise need not be four substances acting from outside a
Dharma. They are the temporal structure of a conditioned stream:

```text
Arising:
    what was absent becomes present

Persistence:
    connected continuation

Aging:
    difference of earlier and later phases

Impermanence:
    interruption of that continuation
```

The Kośa-wide synthesis remains: Vijñāna is Discriminative Cognition joining
and governing Perception and Conception. Its governing unity is not
identical with one momentary citta profile. The life analysis specifies how
the embodied wheel continues through temporal transformations, including
intervals in which current cognitive operation is prevented.

## 6. Logical Determination

The critical life account:

```text
KarmicProjection(S, duration)
    and HomogeneousContinuum(S)
    → LifeContinuity(S, duration)

LifeContinuity(S, duration)
    supports VitalHeat and Cognition
    without requiring an additional life-entity
```

The death distinction:

```text
LifeSpanExhausted(S)
    → Death(S)

LossOfEnjoymentResult or unequal harmful conditions
    may accompany a death;
    they do not replace the stated role of lifespan exhaustion
```

The stream account of marks:

```text
Arising(Stream)       := begins after prior absence
Persistence(Stream)   := causally connected continuation
Aging(Stream)         := earlier phase differs from later phase
Impermanence(Stream)  := continuation is interrupted
```

## 7. Interpretive Note

The Bhāṣya preserves a dispute over whether life is a distinct real Dharma.
The critical account does not deny life; it denies that life must be another
substance beyond the projected duration of the continuum. Its examples are
the projected ripening time of crops and the projected duration of an arrow
in flight.

The source distinguishes life tied to a continuum from life said to persist
as a single arisen determination in other cases. It also records a
fourfold analysis of self- and other-condition in death. The transcription's
long illustrative lists and quotations are textually imperfect; the paired
Bhāṣya study retains the scope without silently restoring them.

The detailed critique of reified primary and secondary marks develops into
VAK 2.46 and is not decided here.

## 8. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_45
    a vak:Karika ;
    rdfs:label "VAK 2.45" ;
    vak:hasTopic vak:LifeContinuity,
        vak:ConditionedMarks ;
    vak:belongsTo vak:Indriyanirdesa .

vak:LifeContinuity
    vak:grounds vak:VitalHeat,
        vak:Cognition ;
    vak:isDerivedFrom vak:KarmicallyProjectedDuration .

vak:ConditionedMarks
    vak:hasMember vak:Arising,
        vak:Persistence,
        vak:Aging,
        vak:Impermanence .
```
