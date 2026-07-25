# VAK_7.11 — Pure and Impure Knowledge of Another Mind

## Sanskrit

### Devanāgarī

```text
तथा परमनोज्ञानं निर्मलं समलं पुनः ।
ज्ञेयस्वलक्षणाकारमेकैकद्रव्यगोचरम् ॥ ७.११ ॥
```

### IAST

```text
tathā paramanojñānaṃ nirmalaṃ samalaṃ punaḥ /
jñeya-svalakṣaṇākāram ekaika-dravya-gocaram // VAK_7.11 //
```

## Source Caution

The verse continues the analysis of cognitive aspects from VAK 7.10. It distinguishes pure and impure forms of knowledge of another mind. The first `tathā` refers back to the preceding account of the sixteen truth-aspects; the second half then specifies the narrower form of impure cognition.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| tathā | indeclinable | likewise; in the same manner |
| para-mano-jñānam | nominative singular neuter | knowledge of another's mind |
| nirmalam | nominative singular neuter | pure; undefiled |
| samalam | nominative singular neuter | impure; defiled |
| punaḥ | indeclinable | again; on the other hand |
| jñeya-svalakṣaṇa-ākāram | nominative singular neuter | having the specific characteristic of the knowable as its aspect |
| ekaika-dravya-gocaram | nominative singular neuter | ranging over one individual entity at a time |

## Grammar

The verse gives a twofold determination of `paramanojñāna`:

```text
pure knowledge of another mind
    likewise bears the truth-aspects

impure knowledge of another mind
    takes the specific characteristic of the knowable as its aspect
    and ranges over one individual object at a time
```

The predicate of the first half is compressed through `tathā`: pure knowledge of another mind is to be understood in the same manner as the pure knowledges just described with respect to the truth-aspects.

The second half gives two determinations of the impure form:

```text
ākāra
    the specific characteristic of what is known

gocara
    one individual entity at a time
```

## Literal Translation

Likewise is pure knowledge of another's mind. The impure form, however, has the specific characteristic of the knowable as its aspect and has one individual entity at a time as its object-domain.

## Philosophical Translation

Pure knowledge of another mind participates in the disciplined aspect-structure of pure cognition. Its impure form, by contrast, apprehends the particular character of a determinate mental event and ranges only over one individual object at a time.

## Technical Vocabulary

### paramanojñāna

```text
para-mano-jñāna
    = knowledge of another mind
    = cognition whose object is another mental continuum
```

The verse does not treat it as a single undifferentiated power. It is internally divided according to purity.

### nirmala / samala

```text
nirmala
    pure
    undefiled

samala
    impure
    defiled
```

The distinction affects both the mode and range of cognition.

### svalakṣaṇa

```text
svalakṣaṇa
    = specific characteristic
    = the particular mark belonging to the knowable itself
```

The impure knowledge does not apprehend another mind through the universal truth-aspects. It grasps the determinate particularity of the mental event known.

### ekaika-dravya-gocara

```text
ekaika
    one by one

dravya
    individual entity or event

gocara
    object-domain
```

The cognition is therefore singular in range:

```text
one cognition
    one determinate object
    one momentary mental event
```

## Doctrinal Determination

The verse distinguishes two forms of knowledge of another mind.

| Form | Aspect | Object-range |
|---|---|---|
| pure | truth-aspects | disciplined by pure cognition |
| impure | specific characteristic of the knowable | one individual entity at a time |

The impure form is precise but narrow. It does not know an abstract class called “mind.” It knows a determinate mental event in its own specific character.

The pure form belongs to the path-structure already articulated through the truth-aspects. Its purity does not make it vague or unlimited; it places the cognition within the pure architecture of knowing.

## Logical Determination

The verse applies two grounding criteria from VAK 7.08:

```text
ākāra
    under what aspect is the object known?

gocara
    what is the range of the cognition?
```

The division is therefore grounded as follows:

```text
pure other-mind knowledge
    grounded by pure aspect-structure

impure other-mind knowledge
    grounded by particular aspect
    and singular object-range
```

This remains grounded Reflection. The text states where the difference lies:

```text
there—
    in purity or impurity

that—
    determines aspect and range
```

No further transcendental reconstruction is imposed in this first pass.

## Organon Light

VAK 7.11 shows that even an apparently extraordinary cognition is scientifically bounded.

```text
knowledge of another mind
    is not one unrestricted faculty

it is divided by
    purity
    aspect
    object-range
```

This is important for the chapter's method. A cognition is not defined by its name alone. It must be represented through the determinate relations that make it what it is.

For the Organon Dataset, `paramanojñāna` therefore requires at least:

```text
purity-status
aspect-type
object-kind
object-cardinality
```

The theological interpretation concerning regulated experience and the bounds imposed by impure dharmas remains a live hypothesis, but the present verse itself gives the narrower doctrinal result: impure cognition is confined to the specific character of one determinate object at a time.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_11
    a vak:Karika ;
    rdfs:label "VAK 7.11" ;
    vak:determines jna:PureOtherMindKnowledge,
                   jna:ImpureOtherMindKnowledge,
                   jna:SpecificCharacteristicAspect,
                   jna:SingleEntityObjectRange .

jna:PureOtherMindKnowledge
    a jna:OtherMindKnowledge ;
    jna:hasPurityStatus jna:Pure .

jna:ImpureOtherMindKnowledge
    a jna:OtherMindKnowledge ;
    jna:hasPurityStatus jna:Impure ;
    jna:hasAspect jna:SpecificCharacteristicAspect ;
    jna:hasObjectRange jna:SingleEntityObjectRange .
```

## Commit History

```text
2026-07-23 — Initial kārikā-pass analysis.
```
