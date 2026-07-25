# VAK_7.32 — Four Fearlessnesses and Three Establishments of Mindfulness

## Sanskrit

### Devanāgarī

```text
वैशारद्यं चतुर्धा तु यथाद्यदशमे बले ।
द्वितीयसप्तमे चैव स्मृतिप्रज्ञात्मकं त्रयम् ॥ ७.३२ ॥
```

### IAST

```text
vaiśāradyaṃ caturdhā tu yathādyadaśame bale /
dvitīyasaptame caiva smṛtiprajñātmakaṃ trayam // VAK_7.32 //
```

## Source Caution

The verse correlates the Buddha’s four fearlessnesses with four of the ten powers already enumerated.

Its compressed numerical references should be read as follows:

```text
first power
    knowledge of what is possible and impossible

tenth power
    knowledge of the destruction of the cankers

second power
    knowledge of karmic result

seventh power
    knowledge of the paths leading everywhere
```

The final quarter identifies the three establishments of mindfulness as having mindfulness and prajñā as their nature.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| vaiśāradyam | nominative/accusative singular neuter | fearlessness, confident assurance |
| caturdhā | adverb | fourfold |
| tu | particle | but, now |
| yathā | indeclinable | corresponding to, in accordance with |
| ādya-daśame | locative dual | in the first and tenth |
| bale | locative singular | power |
| dvitīya-saptame | locative dual | in the second and seventh |
| ca eva | particles | and precisely |
| smṛti-prajñā-ātmakam | compound, nominative/accusative singular neuter | consisting in mindfulness and prajñā |
| trayam | nominative/accusative singular neuter | the triad |

## Grammar

The first statement is:

```text
vaiśāradyaṃ caturdhā
    fearlessness is fourfold
```

The four are then distributed by correspondence:

```text
yathā ādya-daśame bale
    corresponding to the first and tenth powers

dvitīya-saptame ca eva
    and likewise to the second and seventh
```

The final statement is independent:

```text
trayam
    the triad

smṛti-prajñā-ātmakam
    has mindfulness and prajñā as its nature
```

## Literal Translation

Fearlessness is fourfold, corresponding respectively to the first and tenth powers, and likewise to the second and seventh. The triad has mindfulness and prajñā as its nature.

## Philosophical Translation

The Buddha’s four fearlessnesses are not separate powers added to the ten. They are the public, unshakable expression of four already perfected ranges of knowledge: lawful possibility, complete liberation, karmic consequence, and the paths leading to attainment. The three establishments of mindfulness are constituted by mindfulness and discriminative knowing.

## Technical Vocabulary

### vaiśāradya

```text
vaiśāradya
    fearlessness
    confidence without hesitation
    mastery that can be declared openly
```

Fearlessness here is not emotional boldness. It is confidence grounded in unobstructed knowledge.

### smṛtyupasthāna

```text
smṛtyupasthāna
    establishment of mindfulness
    stable presence of recollective awareness
```

In this verse the triad of the Buddha’s establishments of mindfulness is reduced analytically to two constitutive factors:

```text
smṛti
    sustained non-forgetfulness

prajñā
    discriminative comprehension
```

### smṛti-prajñā-ātmaka

```text
smṛti-prajñā-ātmaka
    having mindfulness and prajñā as its nature
```

This is a concise example of the Kośa’s knowledge combinatorics: a named excellence is analyzed into its functional constituents.

## Doctrinal Determination

### Four fearlessnesses

The four fearlessnesses correspond to four Buddha-powers:

| Fearlessness | Correlative power |
|---|---|
| Perfect awakening | Knowledge of possible and impossible |
| Destruction of all cankers | Knowledge of destruction |
| Identification of obstacles | Knowledge of karmic result |
| Declaration of the path | Knowledge of paths |

The verse therefore presents fearlessness as a mode of manifestation of knowledge.

```text
power
    perfected cognitive capacity

fearlessness
    unobstructed declaration of that capacity
```

### Three establishments of mindfulness

The Buddha remains mindful and composed whether disciples:

```text
listen
fail to listen
or are divided between the two
```

The present verse does not recount those cases. It identifies their shared constitution:

```text
mindfulness
    maintains the field

prajñā
    discriminates it correctly
```

## Logical Determination

The verse gives two forms of analysis.

### Functional correspondence

```text
one established power
    can appear
    as one mode of fearlessness
```

Thus a doctrinal quality may be related to another not by identity, but by functional expression.

### Constituent analysis

```text
one named triad
    may be analyzed
    into two constitutive factors
```

The number of named forms and the number of constituting dharmas need not match.

This is a clear instance of analytical scope control:

```text
viewed by function
    four fearlessnesses

viewed by constitution
    selected powers

viewed by material factors
    mindfulness and prajñā
```

## Organon Light

The basic determination is:

> The same perfected knowledge may be analyzed as capacity, public assurance, or constituent factors according to the active scope.

This gives a modest sattva–tamas indication:

```text
sattva-side
    cognition rendered lucid and declarable

tamas-side
    the determinate support and constituent structure
```

For the present pass, this remains only a marker. The detailed diagram of cause and effect, rather than ground and grounded, belongs to a later return.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix marga: <http://127.0.0.1:3000/marga#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_32
    a vak:Karika ;
    rdfs:label "VAK 7.32" ;
    vak:determines jna:FourFearlessnesses,
                   marga:ThreeEstablishmentsOfMindfulness .

jna:FourFearlessnesses
    a jna:ManifestationOfKnowledge ;
    jna:correspondsTo jna:PossibleImpossiblePower,
                     jna:DestructionPower,
                     jna:KarmicResultPower,
                     jna:PathPower .

marga:ThreeEstablishmentsOfMindfulness
    a marga:PracticeTriad ;
    vak:hasConstituent marga:Mindfulness,
                       jna:Prajna .
```

## Commit History

```text
2026-07-23 — Initial kārikā-pass analysis for VAK_7b.
```
