# VAK_7.13 — The Sixteen Aspects and the Structure of Cognition

## Sanskrit

### Devanāgarī

```text
द्रव्यतः षोडशाकाराः प्रज्ञाकारस्तया सह ।
आकारयन्ति सालम्बाः सर्वमाकार्यते तु सत् ॥ ७.१३ ॥
```

### IAST

```text
dravyataḥ ṣoḍaśākārāḥ prajñākāraḥ tayā saha /
ākārayanti sālambāḥ sarvam ākāryate tu sat // VAK_7.13 //
```

## Source Caution

This verse is doctrinally compressed and turns on the technical meaning of `ākāra`. The first half presents the Vaibhāṣika account in which the sixteen aspects are real determinate factors and are identified with prajñā. The second half broadens the discussion from those sixteen pure aspects to cognition in general.

The bhāṣya later raises difficulty with simply identifying the aspect with prajñā, since prajñā cannot be associated with another prajñā in the ordinary way. For the present kārikā-pass, the verse is recorded in its stated form without prematurely resolving that debate.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| dravyataḥ | ablative adverbial form | substantially; as real entities |
| ṣoḍaśa-ākārāḥ | nominative plural masculine | sixteen aspects |
| prajñā | nominative singular feminine | discernment; wisdom |
| ākāraḥ | nominative singular masculine | aspect; mode of apprehension |
| tayā saha | instrumental phrase | together with it; along with that prajñā |
| ākārayanti | causative, 3rd plural | they take on an aspect; they apprehend under a form |
| sa-ālambāḥ | nominative plural masculine | those possessing an object-support |
| sarvam | nominative/accusative singular neuter | everything |
| ākāryate | causative passive | is made an object of apprehension; is apprehended under an aspect |
| tu | indeclinable | but; however |
| sat | nominative singular neuter | what exists; the existent |

## Grammar

The verse moves through three linked claims.

First:

```text
the aspects are sixteen as real determinate factors
```

Second:

```text
the aspect is prajñā
```

Third:

```text
whatever possesses an object-support apprehends under an aspect
whatever exists can be made an object of apprehension
```

`dravyataḥ` is important. The number sixteen is not merely verbal or conventional; the aspects are counted as distinct in real doctrinal determination.

`sa-ālamba` marks cognition by its possession of an object-support. The verse therefore treats cognition and object together:

```text
that which cognizes
    has an object

that which exists
    can become object
```

## Literal Translation

Substantially, the aspects are sixteen. The aspect is prajñā, together with it. Those possessing an object apprehend under an aspect; whatever exists is made an object of apprehension.

## Philosophical Translation

The sixteen truth-aspects are counted as real determinate modes of discernment. Cognition does not merely encounter an object bare; insofar as it has an object-support, it apprehends through an aspect. Conversely, whatever exists can enter cognition as something apprehended.

## Technical Vocabulary

### dravyataḥ

```text
dravyataḥ
    = in substantial determination
    = as really distinct factors
```

The verse is not merely saying that sixteen names are used. It says that the aspects are sixteen in the order of real doctrinal analysis.

### ākāra

```text
ākāra
    = aspect
    = determinate mode of apprehension
```

An aspect is not simply the external object. It is the determination under which cognition takes that object.

```text
object
    what is apprehended

aspect
    how it is apprehended
```

### prajñā

```text
prajñā
    = discernment
    = cognitive discrimination of dharmas
```

The verse identifies the aspect with prajñā. This indicates an active cognitive function rather than a passive image simply received by mind.

### ālambana

```text
ālambana
    = object-support
    = that upon which cognition depends as its object
```

A cognition with an object is `sālamba`. Its cognitive determination is therefore relational from the outset.

## Doctrinal Determination

The verse extends the previous discussion in two directions.

### The sixteen aspects

The sixteen aspects of the Four Noble Truths are not treated as a loose list. They are real determinate modes of pure discernment.

```text
four truths
    ×
four aspects each
    =
sixteen aspects
```

### Cognition in general

The verse then generalizes beyond the sixteen:

```text
all object-bearing cognition
    apprehends through an aspect

all existent dharmas
    are capable of becoming objects
```

This does not mean that every cognition apprehends every existent. It means only that object-bearing cognition is aspectual, and that existence is in principle objectifiable within the appropriate cognitive range.

## Logical Determination

The verse gives a clean twofold relation:

```text
sālamba
    cognition possesses an object

sat
    the existent is capable of being object
```

Between them stands `ākāra`:

```text
cognition
    — through aspect —
object
```

Thus cognition is not described as a blank subject facing a bare object. It is a structured relation in which:

```text
there is something known
there is a determinate way it is known
there is a cognition capable of that determination
```

At this stage the Kośa remains within reflective specification. It is clarifying the real factors and relations required for a cognition to count as this cognition rather than another.

## Organon Light

VAK 7.13 is important for the Organon Dataset because it shows that a knowledge-entry cannot be represented by object alone.

A complete representation requires at least:

```text
cognition
object-support
aspect
range of possible objects
```

The verse therefore prevents a crude model of knowledge as merely:

```text
subject → object
```

The more adequate schema is:

```text
cognition
    apprehends
object
    under an aspect
```

This remains grounded Reflection rather than genetic presentation. The Kośa is specifying what must be present wherever determinate cognition occurs.

No further transcendental mapping is imposed in this first pass.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_13
    a vak:Karika ;
    rdfs:label "VAK 7.13" ;
    vak:determines jna:SixteenAspects,
                   jna:AspectualCognition,
                   jna:ObjectSupportedCognition,
                   jna:ObjectifiableExistence .

jna:AspectualCognition
    a jna:Cognition ;
    jna:hasAspect jna:CognitiveAspect ;
    jna:hasObjectSupport jna:ObjectSupport .

jna:ObjectifiableExistence
    a jna:DoctrinalPrinciple ;
    jna:states "Whatever exists can become an object within an appropriate cognitive range." .
```

## Commit History

```text
2026-07-23 — Initial kārikā-pass analysis.
```
