# VAkK 4.39

## Sanskrit

### Devanāgarī

> पातनीयेन चेत्येके सद्धर्मान्तर्धितोऽपरे ।  
> धनर्णवत्तु काश्मीरैरापन्नस्येष्यते द्वयम् ॥ ४.३९ ॥

### IAST

> **patanīyena cety eke saddharmāntardhito ’pare |**  
> **dhanarṇavat tu kāśmīrair āpannasyeṣyate dvayam || 4.39 ||**

The verse records competing doctrinal positions concerning whether a grave monastic offense destroys prātimokṣa restraint.

## Padaccheda

```text
patanīyena ca iti eke |
sat-dharma-antardhitaḥ apare |
dhana-ṛṇavat tu kāśmīraiḥ |
āpannasya iṣyate dvayam ||
```

Expanded sense:

```text
eke:
    prātimokṣa restraint is lost through a downfall offense

apare:
    it is lost through disappearance of the true Dharma

kāśmīrāḥ:
    the offender possesses both restraint and grave offense
```

## Grammar

| Form | Analysis | Meaning |
|---|---|---|
| **patanīyena** | instrumental singular | through an offense causing downfall |
| **eke** | nominative plural | some authorities |
| **saddharmāntardhitaḥ** | ablative construction | through disappearance of the true Dharma |
| **apare** | nominative plural | others |
| **dhana-ṛṇavat** | comparative compound | like one possessing wealth and debt |
| **kāśmīraiḥ** | instrumental plural | according to the Kashmir authorities |
| **āpannasya** | genitive singular | of one who has fallen into an offense |
| **iṣyate** | passive present | is maintained |
| **dvayam** | neuter singular | both, the pair |

## Literal translation

> **Some say that prātimokṣa restraint is also abandoned through an offense entailing downfall; others say through the disappearance of the true Dharma. The Kashmir authorities, however, maintain that the offender possesses both, as one may possess both wealth and debt.**

## Doctrinal determination

### 1. Downfall-loss theory

```text
patanīya offense
    → loss of prātimokṣa restraint
```

On this view, the grave offense terminates the standing disciplinary form itself.

### 2. True-Dharma disappearance theory

```text
true Dharma present
    → valid disciplinary transmission possible

true Dharma disappeared
    → prātimokṣa support no longer sustained
```

This adds a collective and historical support condition to the individual bearer.

### 3. Kashmir Vaibhāṣika theory

The Kashmir authorities reject simple cancellation:

```text
previous restraint remains
    +
grave contrary karmic determination is acquired
```

The analogy is:

```text
wealth
    +
debt
```

A liability does not make the asset nonexistent, and the asset does not cancel the liability merely by coexisting with it.

## Possession and conformity

The verse distinguishes:

```text
possession of restraint
    ≠
conformity to restraint
```

The fallen practitioner may still possess the previously acquired restraint while acting in radical contradiction to it.

Thus:

```text
grave contradiction
    does not necessarily entail
ontological cancellation
```

## Dharma coexistence

The continuum can bear opposed determinations:

```text
wholesome restraint
unwholesome grave offense
```

Each has its own:

```text
cause
acquisition
causal efficacy
possible result
```

The experiential continuum is therefore not a single moral status flag.

## Relation to kleśa

A powerful kleśa may overwhelm present governance while the standing restraint remains:

```text
restraint persists
kleśa becomes active
grave karma is produced
```

This confirms that ordinary restraint does not eliminate latent afflictive susceptibility. The noble Path must transform the root of conflict rather than merely add another standing counter-form.

## Logical determination

Three models are recorded:

```text
Position 1:
    downfall offense → restraint lost

Position 2:
    disappearance of true Dharma → restraint lost

Kashmir position:
    downfall offense → restraint remains + contrary offense acquired
```

The Kashmir position distinguishes:

```text
negation of conformity
    from
negation of possession
```

## Light Organon interpretation

The verse distinguishes an internally contradicted form from an abolished form:

```text
abolition:
    the determination no longer exists

contradiction:
    the determination exists
    together with activity opposed to it
```

The fallen monastic is not returned to innocent pre-vow non-possession. The history of formation remains recorded.

## Typed feature structure

```text
[ FALLEN-PRACTITIONER
  RESTRAINT-POSSESSED      true
  GRAVE-OFFENSE            committed
  CONTRARY-KARMA           acquired
  CONFORMITY-TO-RESTRAINT  false
  SCHOOL                   Kashmir-Vaibhasika ]
```

Alternative model:

```text
[ FALLEN-PRACTITIONER
  RESTRAINT-POSSESSED      false
  LOSS-CONDITION           downfall-offense ]
```

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_39
    a vak:Karika ;
    rdfs:label "VAK 4.39" ;
    vak:continues vak:VAK_4_38 ;
    vak:hasTopic vak:DisputedLossOfPratimoksha .

vak:DownfallLossTheory
    vak:assertsLossCondition vak:DownfallOffense .

vak:TrueDharmaDisappearanceTheory
    vak:assertsLossCondition vak:DisappearanceOfTrueDharma .

vak:KashmirVaibhasikaTheory
    vak:asserts vak:CoexistenceOfRestraintAndGraveOffense .

vak:RestraintPossession
    vak:isDistinctFrom vak:ConformityToRestraint .
```

## Determinate result

VAkK 4.39 records that some authorities regard a grave downfall as destroying restraint, others add the disappearance of the true Dharma, while the Kashmir Vaibhāṣikas maintain that the offender bears both the old restraint and the new grave offense.

Its central principle is:

```text
a contrary karmic determination
need not erase an earlier one;
experience may preserve both
as distinct and effective dharmic records
```
