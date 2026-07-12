# VAkK 4.40

## Sanskrit

### Devanāgarī

> भूमिसंचारहानिभ्यां ध्यानाप्तं त्यज्यते शुभम् ।  
> तथारूप्याप्तमार्यं तु फलाप्त्युत्पत्तिहानिभिः ॥ ४.४० ॥

### IAST

> **bhūmisaṃcārahānibhyāṃ dhyānāptaṃ tyajyate śubham |**  
> **tathārūpyāptam āryaṃ tu phalāptyutpattihānibhiḥ || 4.40 ||**

The project source has a difficult reading in the second line. The working normalization `phalāpti-utpatti-hānibhiḥ` remains provisional pending the Bhāṣya. The general subject is secure: the loss of meditation-acquired wholesome dharmas and noble uncontaminated dharmas.

## Padaccheda

```text
bhūmi-saṃcāra-hānibhyām
dhyāna-āptam
tyajyate
śubham |

tathā
ārūpya-āptam |

āryam
tu
phala-āpti-utpatti-hānibhiḥ ||
```

## Grammar

| Form | Analysis | Meaning |
|---|---|---|
| **bhūmi-saṃcāra-hānibhyām** | ablative dual | through transition of ground and through falling away |
| **dhyāna-āptam** | neuter singular | acquired through dhyāna |
| **tyajyate** | passive present | is relinquished |
| **śubham** | neuter singular | wholesome dharma |
| **ārūpya-āptam** | neuter singular | acquired through a formless attainment |
| **āryam** | neuter singular | noble, Path-related |
| **phalāpti** | compound member | attainment of a fruit |
| **utpatti** | compound member | arising |
| **hāni** | compound member | loss, falling away |

## Literal translation

> Wholesome dharmas acquired through dhyāna are relinquished through transition to another ground and through falling away; those acquired through the formless attainments are relinquished in the same manner. Noble dharmas, however, are relinquished through attainment of a fruit, through the arising of another state, and through loss.

The fine distribution of the second line remains provisional.

## Philosophical translation

> Meditative wholesome forms endure only while the cognitive ground that generates them remains operative. They cease either when that ground is lost or when the practitioner passes into another ground. Noble uncontaminated forms possess a different developmental lifecycle: they are relinquished when their Path-function is fulfilled in a fruit, when a succeeding noble determination arises, or when a reversible attainment is lost.

## Doctrinal determination

The verse distinguishes three classes:

```text
1. dhyānāpta śubha
   wholesome dharmas acquired through dhyāna

2. ārūpyāpta śubha
   wholesome dharmas acquired through formless attainment

3. ārya dharma
   noble uncontaminated dharmas acquired through the Path
```

Meditative wholesome dharmas are indexed to a determinate **bhūmi**. They are lost either through:

```text
bhūmisaṃcāra
    transition to another meditative ground

hāni
    falling away from the attainment
```

This introduces an essential distinction:

```text
loss by regression
    attainment deteriorates

loss by advancement
    another ground becomes operative
```

The latter is not failure. A dharma can cease because a higher or succeeding ground has arisen.

The noble dharma has a different lifecycle. Its ground is not merely a meditative state but a determinate Path-stage. It may cease because:

```text
fruit-attainment
    its function is completed

successor-arising
    another noble determination becomes operative

falling-away
    where the attainment is reversible
```

Thus a Path-dharma can cease precisely because it has succeeded.

## Ground-dependent persistence

The verse establishes:

```text
GROUND-POSSESSED
    → GROUND-DEPENDENT-DHARMA-POSSESSED

GROUND-LOST OR SUPERSEDED
    → DEPENDENT-DHARMA-RELINQUISHED
```

A meditative restraint is therefore not restraint in the abstract. It is restraint-of-this-bhūmi. Likewise, noble restraint is restraint-of-this-Path-stage.

The record must include:

```text
TYPE
GROUND
STAGE
ACQUISITION-EVENT
CURRENT-STATUS
LOSS-EVENT
SUCCESSOR-STATE
```

## Three restraint lifecycles

```text
prātimokṣa restraint
    ground: formal undertaking and embodied status
    loss: relinquishment, death, basis-change,
          root-severance, term completion

dhyāna-born restraint
    ground: meditative bhūmi
    loss: ground-transition or falling away

uncontaminated restraint
    ground: noble Path-stage
    loss: fruit-attainment, succeeding noble arising,
          or possible falling away
```

The kind of ground determines the kind of cessation.

## Logical determination

A System of Dharma must distinguish at least:

```text
1. destruction of support
2. regression or falling away
3. expiration of a stipulated term
4. fulfillment and supersession
```

The fourth is decisive here:

```text
means
    ceases when its end is attained
```

The cessation of a Path-to-fruit at fruit-attainment is not external negation. It is the completed activity of the Path-form.

Formally:

```text
Dharma D is grounded in stage G.

If G is lost:
    D is lost.

If G is superseded by G2:
    D ceases as the operative dharma of G.

If D fulfills its function in result R:
    D is relinquished upon acquisition of R.
```

## Light Organon interpretation

The dharma's limit is its determinate ground. Because it is the dharma of this ground, departure from that ground terminates its current actuality.

But the limit is productive:

```text
the lower form's completion
    is transition into the higher

the Path's completion
    is attainment of the fruit
```

The negation of the earlier form may therefore be either abstract loss or determinate supersession. The latter preserves the accomplished result while relinquishing the completed operation.

This makes the Path an active sequence rather than a static collection of attainments:

```text
stage A arises
    → performs its function
    → stage B arises
    → A is relinquished in its former status
```

## Typed feature structures

```text
[ MEDITATION-ACQUIRED-WHOLESOME
  GROUND-TYPE       dhyāna-bhūmi
  STATUS            possessed
  LOSS-CONDITIONS
    [ ground-transition
      falling-away ] ]
```

```text
[ FORMLESS-ACQUIRED-WHOLESOME
  GROUND-TYPE       ārūpya-bhūmi
  STATUS            possessed
  LOSS-CONDITIONS
    [ ground-transition
      falling-away ] ]
```

```text
[ NOBLE-DHARMA
  GROUND-TYPE       noble-path-stage
  LOSS-CONDITIONS
    [ fruit-attainment
      successor-arising
      falling-away-where-possible ] ]
```

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_40
    a vak:Karika ;
    rdfs:label "VAK 4.40" ;
    vak:continues vak:VAK_4_39 ;
    vak:hasTopic vak:LossOfMeditativeAndNobleDharmas .

vak:DhyanaAcquiredWholesome
    vak:dependsOn vak:DhyanaGround ;
    vak:mayBeLostThrough vak:GroundTransition ;
    vak:mayBeLostThrough vak:FallingAway .

vak:FormlessAcquiredWholesome
    vak:dependsOn vak:FormlessGround ;
    vak:mayBeLostThrough vak:GroundTransition ;
    vak:mayBeLostThrough vak:FallingAway .

vak:NobleDharma
    vak:dependsOn vak:NoblePathStage ;
    vak:mayBeRelinquishedThrough vak:FruitAttainment ;
    vak:mayBeRelinquishedThrough vak:SuccessorArising ;
    vak:mayBeLostThrough vak:FallingAwayWherePossible .
```

## Determinate result

VAkK 4.40 establishes:

```text
dhyāna-acquired wholesome dharmas:
    lost through change of meditative ground
    or falling away

formless-acquired wholesome dharmas:
    lost in the same manner

noble dharmas:
    relinquished through fruit-attainment,
    succeeding arising,
    or possible falling away
```

Its central principle is:

```text
the ground that generates a dharma
also determines its mode of cessation;

a dharma may cease through regression,
but it may also cease because
its function has been completed
and a higher determination has arisen
```