# VAK_4.23

## Sanskrit — Devanāgarī

```sanskrit
विज्ञप्त्या तु पुनः सर्वे कुर्वन्तो मध्ययान्विताः ।
अतीतया क्षणादूर्ध्वमात्यागान्नास्त्यजातया ॥
```

## Sanskrit — IAST

```iast
vijñaptyā tu punaḥ sarve kurvanto madhyayānvitāḥ |
atītayā kṣaṇād ūrdhvam atyāgān nāsty ajātayā ||
```

## Source reference and caution

Source: `VAkK_4.23`.

The verse shifts from the temporal possession of **avijñapti** to the temporal possession of **vijñapti**, manifest bodily or verbal action.

The governing sequence is:

```text
while performing an action:
    all agents possess present vijñapti

after the first moment:
    they possess past vijñapti

future vijñapti:
    is not possessed
```

The phrase `madhyayā anvitaḥ` means “endowed with the middle temporal mode,” where the middle of the three times is the present.

## Padaccheda

```text
vijñaptyā
tu
punaḥ
sarve
kurvantaḥ
madhyayā
anvitāḥ

atītayā
kṣaṇāt
ūrdhvam

atyāgāt
na
asti
ajātayā
```

| Form | Analysis | Working meaning |
|---|---|---|
| `vijñaptyā` | instrumental feminine singular | with manifest action |
| `tu` | particle | but |
| `punaḥ` | adverb | again; in turn |
| `sarve` | nominative plural | all |
| `kurvantaḥ` | present participle | while acting |
| `madhyayā` | instrumental feminine singular | with the middle temporal mode |
| `anvitāḥ` | nominative plural | endowed with |
| `atītayā` | instrumental feminine singular | with past vijñapti |
| `kṣaṇād ūrdhvam` | ablative phrase | after the first moment |
| `atyāgāt` | ablative singular | because of non-abandonment |
| `nāsti` | negated verb | there is not |
| `ajātayā` | instrumental feminine singular | with future, not-yet-arisen vijñapti |

## Literal translation

> But all who are acting are endowed through vijñapti with the middle temporal mode. After the first moment they are endowed with past vijñapti. There is no possession of future vijñapti.

The final causal phrase is compressed and its exact attachment should be verified in the Bhāṣya. The secure doctrinal conclusion is:

```text
present vijñapti while acting
past vijñapti after the moment
no future vijñapti
```

## Philosophical translation

> Whenever an agent is presently performing a bodily or verbal action, the corresponding manifest action exists in the present. Once that moment has passed, the agent is also related to it as past action. Unlike certain forms of avijñapti, however, manifest action is not possessed in a future, not-yet-arisen mode.

## Technical analysis

### `sarve kurvantaḥ`

“All who are acting.” This statement applies across the ethical classifications already discussed: one established in restraint, one established in non-restraint, and one established in neither. Every agent who presently performs a manifest bodily or verbal action possesses present `vijñapti`.

### `madhyayā`

The three temporal modes are past, present, and future. The middle one is the present. Thus `madhyayā anvitaḥ` means “endowed with present vijñapti.”

```text
present doing
    → present manifest action
```

### After the first moment

`atītayā kṣaṇād ūrdhvam` means “after the moment, with past vijñapti.”

```text
present performance
    → past performed action
```

### No future vijñapti

`nāsty ajātayā` means there is no possession of the not-yet-arisen, future vijñapti. A future bodily or verbal performance has not yet manifested and therefore cannot yet function as `vijñapti`.

```text
not-yet-performed action
    ≠
manifest action
```

### Contrast with avijñapti

The preceding verses showed that avijñapti may possess different temporal ranges according to its type. VAK_4.23 gives the simpler rule for vijñapti:

```text
while acting:
    present

after acting:
    past

before acting:
    no future vijñapti possession
```

The distinction between vijñapti and avijñapti is therefore not merely visible versus invisible. It is also a difference in temporal grammar.

## Typed feature structure

```text
[ ACTION-TYPE    vijñapti
  AGENT          acting
  TEMPORAL-MODE  present ]
```

After the moment:

```text
[ ACTION-TYPE    vijñapti
  AGENT          prior-actor
  TEMPORAL-MODE  past ]
```

But not:

```text
[ ACTION-TYPE    vijñapti
  TEMPORAL-MODE  future ]
```

Transition rule:

```text
ACTING
    → present-vijñapti

MOMENT-PASSES
    → past-vijñapti

NOT-YET-ACTING
    ↛ future-vijñapti-possession
```

## Doctrinal determination

1. Every presently acting agent possesses present vijñapti.
2. After the first moment, the performed action is possessed as past.
3. The agent does not possess future vijñapti.

This completes an important part of the temporal comparison between manifest and non-manifest action.

## Relation to VAK_4.19–4.22

```text
VAK_4.19
    temporal possession of prātimokṣa avijñapti

VAK_4.20
    temporal possession of non-restraint,
    meditation-born restraint,
    and uncontaminated restraint

VAK_4.21
    present mind-following restraint
    and occasional avijñapti

VAK_4.22
    contrary occasional avijñapti
    under powerful faith or defilement

VAK_4.23
    temporal possession of manifest action
```

Thus VAK_4.19–4.23 forms a coherent temporal-feature block.

## Light Organon interpretation

Manifest action has a sharply bounded temporal form:

```text
while it is being performed:
    it is present

once performed:
    it is past

before performance:
    it is not yet manifest action
```

Unlike a standing operative determination, manifestation cannot be possessed in advance as manifestation.

```text
vijñapti
    is temporally indexed
    to actual expression
```

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_23
    a vak:Karika ;
    rdfs:label "VAK 4.23" ;
    vak:continues vak:VAK_4_22 ;
    vak:hasTopic vak:TemporalPossessionOfVijnapti ;
    vak:closesBlock vak:TemporalPossessionBlock .

vak:PresentActor
    vak:isEndowedWith vak:PresentVijnapti .

vak:PriorActor
    vak:isEndowedWith vak:PastVijnapti .

vak:FutureVijnapti
    vak:isNotPossessedBy vak:AgentBeforePerformance .

vak:Vijnapti
    vak:requires vak:ActualManifestPerformance .
```

## Verse summary

```text
VAK_4.23

Every agent presently acting
possesses present vijñapti.

After the first moment,
the action is also past.

But future vijñapti
is not yet possessed,
because it has not yet become
manifest performance.

Thus vijñapti has the temporal grammar:

    doing
        → present

    done
        → past

    not yet done
        → not yet vijñapti
```
