# VAK 6.32

## Sanskrit

### Devanāgarī

फले फलविशिष्टस्य लाभो मार्गस्य नास्त्यतः ।  
नाप्रयुक्तो विशेषाय फलस्थः प्रतिपन्नकः ॥ ६.३२ ॥

### IAST

**phale phala-viśiṣṭasya lābho mārgasya nāsty ataḥ |**  
**nāprayukto viśeṣāya phalasthaḥ pratipannakaḥ || 6.32 ||**

## Source Caution

The verse distinguishes two statuses that must not be conflated:

```text
phalastha
    one established in a fruit

pratipannaka
    one actively proceeding toward a fruit
```

The key expression is **phalaviśiṣṭasya mārgasya**: a path superior to, or further distinguished beyond, the fruit already attained.

The verse does not deny further progress to one established in a fruit. It states that the mere possession of the present fruit does not itself include attainment of the superior path leading beyond it.

## Padaccheda

```text
phale
phala-viśiṣṭasya
lābhaḥ
mārgasya
na asti
ataḥ

na
aprayuktaḥ
viśeṣāya
phalasthaḥ
pratipannakaḥ
```

## Grammar

- **phale** — locative singular neuter: “in the fruit” or “while established in the fruit.”
- **phala-viśiṣṭasya** — genitive singular masculine, qualifying **mārgasya**: “of the path distinguished beyond the fruit,” hence “of the path superior to the attained fruit.”
- **lābhaḥ** — nominative singular masculine: “attainment” or “acquisition.”
- **mārgasya** — genitive singular masculine: “of the path.”
- **na asti** — “does not exist” or “is not present.”
- **ataḥ** — indeclinable: “therefore,” “for this reason.”
- **na aprayuktaḥ** — “not one who is unengaged”; in the sentence as a whole, the fruit-abider who is not exerting himself toward distinction is not a candidate.
- **viśeṣāya** — dative singular masculine: “for distinction,” “toward a higher attainment,” or “for further excellence.”
- **phalasthaḥ** — nominative singular masculine: “one established in a fruit.”
- **pratipannakaḥ** — nominative singular masculine: “one who has entered upon the way,” “a candidate progressing toward a fruit.”

## Literal Translation

In the fruit there is no attainment of a path superior to that fruit. Therefore, one established in a fruit who is not applied toward further distinction is not a candidate progressing onward.

## Philosophical Translation

Possession of a noble fruit does not by itself include the superior path leading beyond that fruit. Consequently, a person established in a fruit is called a candidate for a higher fruit only when actively engaged in the effort toward further distinction.

## Fruit and Superior Path

The verse states:

```text
present fruit
    does not automatically contain
superior path
```

A fruit is the established result of a completed path-phase. A superior path is the new active process by which the practitioner advances beyond that attainment.

Thus:

```text
fruit
    accomplished position

superior path
    new undertaking
    directed beyond that position
```

The relation is not automatic succession. A new path must be entered.

## Phalastha

```text
phalastha
    established in fruit
```

This designation concerns possession of an attained result.

The practitioner has completed the path corresponding to that fruit and now occupies the resulting noble status.

```text
completed path
    ↓
attained fruit
    ↓
fruit-abider
```

But this status alone does not determine whether the practitioner is presently advancing toward the next fruit.

## Pratipannaka

```text
pratipannaka
    one who has entered upon
    and is proceeding along
    a path toward fruit
```

The term is dynamic rather than merely positional.

A practitioner is not called a candidate for a higher fruit simply because a lower fruit has been attained. Candidate-status requires active engagement in the path that leads beyond the present fruit.

```text
fruit-abider
    + application toward higher distinction
        = candidate for the next fruit
```

Without this application:

```text
fruit-abider
    remains established in the present fruit
    but is not presently a pratipannaka
```

## Prayoga and Viśeṣa

The crucial determination is:

```text
prayoga
    application
    active engagement
    directed effort

viśeṣa
    further distinction
    higher attainment
```

The verse therefore defines progress through an oriented activity:

```text
present attainment
    → application toward distinction
    → superior path
    → higher fruit
```

The higher status is not produced merely by elapsed time or by the passive continuation of the present fruit.

## Position and Transition

VAK 6.31 established the practitioner in fruit at the sixteenth moment.

VAK 6.32 now prevents that establishment from being confused with immediate candidacy for every subsequent fruit.

```text
sixteenth moment
    establishment in a determinate fruit

subsequent progress
    requires entry into a superior path
```

The verse therefore distinguishes:

```text
state
    being established in fruit

transition
    undertaking the superior path
```

This is the central structural determination.

## Doctrinal Determination

```text
FruitAbider {
    status:
        EstablishedInPresentFruit

    possesses:
        PresentFruit

    doesNotNecessarilyPossess:
        SuperiorPath
}

HigherFruitCandidate {
    currentStatus:
        FruitAbider

    requiredCondition:
        AppliedTowardFurtherDistinction

    undertakes:
        SuperiorPath

    progressesToward:
        HigherFruit
}
```

The distinction between fruit-abider and candidate is determined by whether the superior path has become active.

## Logical Determination

The movement is:

```text
path
    → fruit
```

But the next movement is not:

```text
fruit
    → higher fruit automatically
```

It is:

```text
fruit
    → renewed application
    → superior path
    → higher fruit
```

The fruit is therefore a real completion, not merely a passing point inside an undifferentiated continuum. Because it is a completion, a new mediation is required for further progress.

This gives the verse a precise logical form:

```text
result of one process
    is not identical with
beginning of the next process
```

The next process begins only when the practitioner is actively oriented toward **viśeṣa**, further distinction.

## Interpretive Note

The verse gives a positive determination of **pratipannaka**.

A candidate is not merely someone located below a future fruit. A candidate is someone in whom the path toward that fruit is presently operative.

```text
pratipannaka
    = path-active person
```

This prevents the pudgala classification from becoming a static rank-order. The same practitioner can be described differently according to whether the emphasis falls on:

```text
attained result
    phalastha

active progression
    pratipannaka
```

The classification is therefore functional and path-relative.

## OWL++ Seed

```text
Class: FruitAbider
Class: FruitCandidate
Class: PresentFruit
Class: HigherFruit
Class: SuperiorPath
Class: ApplicationTowardDistinction

ObjectProperty: establishedIn
ObjectProperty: progressesToward
ObjectProperty: undertakes
ObjectProperty: requiresApplication
ObjectProperty: superiorTo

FruitAbider
    establishedIn PresentFruit

SuperiorPath
    superiorTo PresentFruit

FruitCandidate
    undertakes SuperiorPath

FruitCandidate
    progressesToward HigherFruit

FruitCandidate
    requiresApplication ApplicationTowardDistinction
```

## Determinate Summary

```text
One established in a fruit:

    possesses the completed result
    of the preceding path

    does not thereby automatically possess
    the superior path leading onward

Therefore:

    without active application
    toward further distinction,

    the fruit-abider is not called
    a candidate for a higher fruit
```

VAK 6.32 distinguishes attained position from active transition: **phalastha** names one established in a fruit, while **pratipannaka** names one in whom the superior path toward further distinction is presently operative.
