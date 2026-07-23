# VAK_7.31 — The Buddha’s Bodily Power

## Sanskrit

### Devanāgarī

```text
नारायणबलं काये संधिष्वन्ये दशाधिकम् ।
हस्त्यादिसप्तकबलं स्प्रष्टव्यायतनं च तत् ॥ ७.३१ ॥
```

### IAST

```text
nārāyaṇabalaṃ kāye saṃdhiṣv anye daśādhikam /
hastyādisaptakabalaṃ spraṣṭavyāyatanaṃ ca tat // VAK_7.31 //
```

## Source Caution

The verse turns from the Buddha’s cognitive powers to bodily power.

Its compact language preserves several interpretations:

```text
Nārāyaṇa-strength
    belongs to the Buddha’s body

according to others
    it belongs to each bodily joint

its measure
    is the seventh stage in a tenfold ascending series
    beginning with elephant-strength

its dharma classification
    is the tangible sphere
```

The numerical series and rival interpretations belong to the bhāṣya’s explanatory framework and should not be expanded beyond what is needed for this first pass.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| nārāyaṇa-balam | compound, nominative/accusative singular neuter | Nārāyaṇa-strength |
| kāye | locative singular | in the body |
| saṃdhiṣu | locative plural | in the joints, bodily articulations |
| anye | nominative plural | others [say] |
| daśa-adhikam | compound | each stage exceeding the prior by tenfold |
| hasti-ādi-saptaka-balam | compound | the seventh power in the series beginning with the elephant |
| spraṣṭavya-āyatanam | nominative/accusative singular neuter | the tangible sphere |
| ca | conjunction | and |
| tat | pronoun | that |

## Grammar

The primary construction is:

```text
nārāyaṇa-balam
    Nārāyaṇa-strength

kāye
    is in the body
```

A variant interpretation is supplied elliptically:

```text
anye
    others [say]

saṃdhiṣu
    in the bodily joints
```

The second half defines its comparative measure and dharma classification:

```text
hastyādi-saptaka-balam
    the seventh strength in a sequence beginning with elephant-strength

daśādhikam
    each level ten times the preceding

tat spraṣṭavyāyatanam ca
    and that belongs to the tangible sphere
```

## Literal Translation

Nārāyaṇa-strength is in the Buddha’s body; according to others, it is in each of his joints. It is the seventh strength in a tenfold ascending series beginning with elephant-strength, and it belongs to the tangible sphere.

## Philosophical Translation

The Buddha’s embodied power is described through an ascending series of physical strengths culminating in Nārāyaṇa-strength. Yet however extraordinary this power may be, the Kośa still classifies it soberly as a tangible dharma: it belongs to the sphere of bodily contact rather than to the ten cognitive powers previously analyzed.

## Technical Vocabulary

### nārāyaṇa-bala

```text
nārāyaṇa-bala
    Nārāyaṇa-strength
    an exceptional measure of bodily power
```

The bhāṣya treats this as the Buddha’s physical strength. Some authorities assign it to the body as a whole; others to each bodily articulation.

### saṃdhi

```text
saṃdhi
    joint
    articulation
    point of bodily connection
```

The term is especially apt here because it names bodily power at the point where separate members are joined and coordinated.

### spraṣṭavya-āyatana

```text
spraṣṭavya-āyatana
    tangible sphere
    domain of what can be contacted by touch
```

The bodily power is therefore classified within rūpa-dharma. It is not itself one of the Buddha’s ten powers of knowledge.

## Doctrinal Determination

### Cognitive power and bodily power

VAK 7.28–7.30 analyzed the Buddha’s powers as organized ranges of knowledge.

VAK 7.31 distinguishes another use of *bala*:

```text
knowledge-power
    cognitive
    unobstructed determination of a field

bodily power
    material
    classified in the tangible sphere
```

The common word *bala* does not erase the categorical difference.

### The ascending series

The verse measures bodily strength through a graded comparison:

```text
elephant-strength
    ↓ tenfold increase
higher strength
    ↓ tenfold increase
...
Nārāyaṇa-strength
```

The exact enumeration belongs to the scholastic calculus of magnitudes. The important point here is only that the Buddha’s bodily strength occupies an extreme position within a determinate series.

### Body as support

The bhāṣya preserves the view that the Buddha’s extraordinary body must be capable of supporting extraordinary cognition.

For the first kārikā pass, this should be kept modest:

```text
infinite or unobstructed knowing
    is not identified with the body

but embodied manifestation
    requires an adequate support
```

## Logical Determination

The verse introduces a distinction between two meanings of power:

```text
power as knowing
    determines an object-field

power as embodiment
    sustains effective manifestation
```

It also gives a small but useful analytical rule:

```text
same term
    does not imply
same logical category
```

Thus *bala* must be interpreted by scope and function.

### Articulation

The variant reading concerning the joints gives a light structural image:

```text
power is not only mass

power is coordinated articulation
    at the points of connection
```

This is useful but should not be overextended in the first pass.

## Organon Light

The basic determination is:

> A knowledge processor still requires a support capable of bearing and expressing its operation.

And the Kośa immediately prevents confusion:

```text
cognitive power
    belongs to knowledge

bodily power
    belongs to the tangible sphere
```

The distinction between processor, circuitry, and embodiment remains provisional.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix rupa: <http://127.0.0.1:3000/rupa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_31
    a vak:Karika ;
    rdfs:label "VAK 7.31" ;
    vak:determines rupa:NarayanaStrength,
                   rupa:BodilyPower,
                   rupa:TangibleSphereClassification .

rupa:NarayanaStrength
    a rupa:BodilyPower ;
    rupa:belongsTo rupa:TangibleSphere ;
    rupa:measuredBy rupa:AscendingStrengthSeries .

rupa:AscendingStrengthSeries
    a rupa:ComparativeMagnitudeSeries ;
    rupa:beginsWith rupa:ElephantStrength ;
    rupa:usesRatio "10" .

jna:CognitivePower
    a jna:KnowledgeCapacity ;
    vak:distinctFrom rupa:BodilyPower .
```

## Commit History

```text
2026-07-23 — Initial kārikā-pass analysis for VAK_7b.
```
