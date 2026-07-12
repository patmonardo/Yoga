# VAkK 4.41

## Sanskrit

### Devanāgarī

> असंवरः संवराप्तिमृत्युद्विव्यञ्जनोदयैः ।  
> वेगादानक्रियार्थायुर्मूलच्छेदैस्तु मध्यमा ॥ ४.४१ ॥

### IAST

> **asaṃvaraḥ saṃvarāptimṛtyudvivyañjanodayaiḥ |**  
> **vegādānakriyārthāyurmūlacchedais tu madhyamā || 4.41 ||**

The first half gives the conditions for losing **asaṃvara**, persistent non-restraint. The second gives the conditions for losing the middle avijñapti, neither complete restraint nor complete non-restraint.

## Padaccheda

```text
asaṃvaraḥ
saṃvara-āpti-mṛtyu-dvi-vyañjana-udayaiḥ |

vega-ādāna-kriyā-artha-āyus-mūla-cchedaiḥ
tu
madhyamā ||
```

## Literal translation

> **Non-restraint is lost through acquisition of restraint, death, and the arising of both sexual characteristics. The intermediate avijñapti, however, is lost through the severance of its force, undertaking, activity, purpose, lifespan, or root.**

The second compound is compressed; its finer distribution remains to be confirmed in the Bhāṣya.

## Doctrinal determination

### Loss of non-restraint

The decisive condition is **saṃvarāpti**, acquisition of restraint:

```text
asaṃvara
    persistent harmful orientation

saṃvara
    persistent restrained orientation

acquisition of restraint
    → abandonment of non-restraint
```

This differs from VAkK 4.39. Restraint may coexist with a particular grave offense, but complete restraint and complete non-restraint cannot coexist in the same practical respect.

Death terminates the present living bearer of non-restraint, while the karma produced under it may remain causally effective. The arising of both sexual characteristics is treated as a transformation of the bodily basis qualifying the bearer.

### The middle avijñapti

The **madhyamā avijñapti** is a persistent karmic form that is neither a comprehensive vow nor a comprehensive anti-vow. It may belong to a determinate project, act, offering, harmful undertaking, or limited promise.

Its persistence depends upon a narrower causal complex:

```text
vega
    force, momentum, continuing impulse

ādāna
    taking up, undertaking

kriyā
    continuing activity

artha
    purpose, object, intended end

āyus
    lifespan of the bearer

mūla
    supporting causal root
```

When one of these sustaining conditions is severed, the intermediate avijñapti ceases.

## Philosophical translation

> **Persistent non-restraint ceases when a genuinely contrary restraint is acquired, when its living bearer dies, or when the bodily basis qualifying that bearer is transformed. More limited avijñapti formations possess a correspondingly conditional persistence: they cease when the impulse that sustains them is exhausted, the undertaking is relinquished, the activity stops, its purpose is completed or destroyed, the bearer’s life ends, or the supporting causal root is severed.**

## Logic of Experience

The verse identifies two distinct modes of cessation.

### Contrary replacement

```text
NON-RESTRAINT
    + ACQUISITION(RESTRAINT)
        → RESTRAINT
        → NON-RESTRAINT relinquished
```

### Dependency severance

```text
INTERMEDIATE-AVIJNAPTI
    depends upon
        force
        undertaking
        activity
        purpose
        life
        root

severance of a sustaining dependency
    → avijñapti relinquished
```

Thus the mode by which a dharma is sustained determines the mode by which it ceases. A complete harmful form may be displaced by an incompatible standing form, while a limited karmic form ends when its sustaining project-complex is exhausted or severed.

## Transition algebra

By this point the Karma chapter has distinguished:

```text
VOLUNTARY-RELINQUISHMENT
BEARER-TERMINATION
BASIS-TRANSFORMATION
ROOT-DESTRUCTION
TERM-EXPIRATION
CONTRARY-ACQUISITION
GROUND-CHANGE
FALLING-AWAY
FUNCTION-COMPLETION
SUCCESSOR-ARISING
FORCE-EXHAUSTION
ACTIVITY-TERMINATION
PURPOSE-COMPLETION
```

A System of Dharma as Logic of Experience must therefore record not merely that a determination is present or absent, but what sustains it, what is incompatible with it, and whether its cessation means failure, conversion, exhaustion, or completion.

## Typed feature structures

```text
[ NON-RESTRAINT
  STATUS possessed
  LOSS-CONDITIONS
    [ restraint-acquisition
      death
      bodily-basis-transformation ] ]
```

```text
[ INTERMEDIATE-AVIJNAPTI
  STATUS possessed
  DEPENDENCIES
    [ force
      undertaking
      activity
      purpose
      lifespan
      causal-root ]
  LOSS-RULE
    severance-of-required-dependency ]
```

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_41
    a vak:Karika ;
    rdfs:label "VAK 4.41" ;
    vak:continues vak:VAK_4_40 ;
    vak:hasTopic vak:LossOfNonRestraintAndIntermediateAvijnapti .

vak:NonRestraint
    vak:mayBeLostThrough vak:AcquisitionOfRestraint ;
    vak:mayBeLostThrough vak:Death ;
    vak:mayBeLostThrough vak:TransformationOfBodilyBasis .

vak:IntermediateAvijnapti
    vak:mayBeLostThrough vak:ExhaustionOfForce ;
    vak:mayBeLostThrough vak:TerminationOfUndertaking ;
    vak:mayBeLostThrough vak:TerminationOfActivity ;
    vak:mayBeLostThrough vak:TerminationOfPurpose ;
    vak:mayBeLostThrough vak:Death ;
    vak:mayBeLostThrough vak:SeveranceOfSupportingRoot .
```

## Determinate result

VAkK 4.41 establishes:

```text
non-restraint:
    lost through acquisition of restraint,
    death,
    or transformation of bodily basis

intermediate avijñapti:
    lost when its force, undertaking,
    activity, purpose, life,
    or supporting root is severed
```

Its central principle is:

```text
the mode by which a dharma is sustained
determines the mode by which it ceases
```