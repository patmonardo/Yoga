# VAK_8.09 — Reduction of the Dhyāna Limbs by Substance

## Sanskrit

### Devanāgarī

```text
द्रव्यतो दश चैकं च प्रस्रब्धिः सुखमाद्ययोः ।
श्रद्धा प्रसादः प्रीतिस्तु सौमनस्यं द्विधागमात् ॥ ८.९ ॥
```

### IAST

```text
dravyato daśa caikaṃ ca prasrabdhiḥ sukham ādyayoḥ /
śraddhā prasādaḥ prītis tu saumanasyaṃ dvidhāgamāt // VAK_8.09 //
```

## Source Caution

The verse compresses an abhidharma reduction of the previously enumerated dhyāna limbs. The count is not simply a recounting of names. It distinguishes:

```text
named limbs
    from
substantially distinct factors
```

The reading adopted here is that, by substance, the limbs resolve to ten distinct factors, while several apparent duplications are explained through identity of underlying dharmas under different descriptions.

The phrase `dvidhāgamāt` is taken cautiously as indicating the twofold occurrence or mode of arrival of joy/pleasant-mindedness within the system.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| dravyataḥ | ablative/adverbial form of `dravya` | by substance; in terms of distinct entities |
| daśa | numeral | ten |
| ca | indeclinable | and |
| ekam | numeral | one |
| ca | indeclinable | and |
| prasrabdhiḥ | nominative singular feminine | pliancy; tranquility |
| sukham | nominative singular neuter | ease; pleasure |
| ādyayoḥ | locative/genitive dual | in the first two |
| śraddhā | nominative singular feminine | confidence; trust |
| prasādaḥ | nominative singular masculine | clarity; serene confidence |
| prītiḥ | nominative singular feminine | rapture; joy |
| tu | indeclinable | but; whereas |
| saumanasyam | nominative singular neuter | gladness; pleasant-mindedness |
| dvidhā-āgamāt | ablative compound | because of twofold occurrence or arrival |

## Grammar

The verse gives a reduction by underlying substance:

```text
dravyataḥ
    considered as distinct dharmas

daśa
    ten
```

The remaining phrases identify apparent duplications among the named limbs:

```text
prasrabdhiḥ sukham ādyayoḥ
    the sukha of the first two dhyānas
    is pliancy

śraddhā prasādaḥ
    prasāda is confidence

prītiḥ tu saumanasyam
    prīti is pleasant-mindedness
```

The phrase `dvidhāgamāt` explains why one underlying factor may receive two names according to its mode or context of occurrence.

## Literal Translation

By substance there are ten. In the first two, pleasure is pliancy; clarity is confidence; and rapture is pleasant-mindedness, because of its twofold occurrence.

## Philosophical Translation

When the dhyāna limbs are reduced to substantially distinct factors, their larger verbal inventory resolves to ten. The pleasure named in the first two dhyānas is bodily-mental pliancy, the clarity of the second is confidence, and rapture is a mode of pleasant-mindedness. Different names may therefore mark different functional appearances of the same underlying factor.

## Technical Vocabulary

### dravyataḥ

`Dravyataḥ` means that the analysis is being conducted according to substantial distinctness:

```text
one name
    may designate one factor

several names
    may designate the same factor
```

The Kośa therefore refuses to identify conceptual enumeration with ontological multiplication.

### prasrabdhi

```text
prasrabdhi
    pliancy
    relaxation of rigidity
    serviceability of body and mind
```

The `sukha` of the first two dhyānas is here analyzed as this pliant ease rather than as a separate pleasure-substance.

### prasāda and śraddhā

```text
prasāda
    clarified serenity

śraddhā
    confidence or trust
```

The second dhyāna's inner clarity is not an additional independent entity. It is confidence appearing in a specific meditative function.

### prīti and saumanasya

```text
prīti
    rapture

saumanasya
    pleasant-mindedness
```

The verse treats rapture as belonging to the affective factor of pleasant-mindedness, while recognizing distinct modes of manifestation.

## Doctrinal Determination

VAK 8.09 performs a second-order analysis of the dhyāna limbs.

### 1. Enumeration is not yet ontology

VAK 8.07–8.08 gave the named limbs of each dhyāna. VAK 8.09 asks how many distinct dharmas these names actually represent.

```text
functional names
    >
substantially distinct factors
```

### 2. Ten distinct factors underlie the larger list

The named limbs overlap because:

```text
sukha in the first two
    = prasrabdhi

prasāda
    = śraddhā

prīti
    = saumanasya
```

Thus the meditative structure is qualitatively articulated without multiplying entities unnecessarily.

### 3. One dharma may appear under different descriptions

The same underlying factor may be named according to:

```text
its affective tone
its functional role
its meditative context
```

This is a native Abhidharma example of disciplined qualitative logic.

## Logical Determination

The verse distinguishes two orders:

```text
order of predicates
    how factors are described

order of substances
    how many distinct dharmas there are
```

The relation is many-to-one:

```text
several determinate descriptions
    →
one underlying factor
```

This is not abstraction from content. It is an intensification of content-analysis:

```text
name
function
felt quality
substantial identity
```

The logical work consists in determining which differences are real distinctions of dharma and which are differences of mode or description.

## Organon Light

The immediate lesson is qualitative:

```text
Logic does not empty the dhyāna of content.
Logic discovers the heat at which
one factor appears under several names.
```

The Kośa's `dravyataḥ` analysis therefore does not reduce experience to bare quantity. It determines the qualitative identity beneath a plurality of predicates.

This insight is kept light here. The first-pass task is simply to preserve the distinction between:

```text
named limb
functional determination
substantially distinct dharma
```

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix sam: <http://127.0.0.1:3000/samapatti#> .
@prefix dhy: <http://127.0.0.1:3000/dhyana#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_8_09
    a vak:Karika ;
    rdfs:label "VAK 8.09" ;
    vak:determines sam:SubstantialReductionOfDhyanaLimbs .

sam:SubstantialReductionOfDhyanaLimbs
    a sam:DoctrinalReduction ;
    sam:distinctFactorCount 10 ;
    sam:identifies dhy:FirstSecondSukhaWithPrasrabdhi,
                   dhy:PrasadaWithSraddha,
                   dhy:PritiWithSaumanasya .

dhy:FirstSecondSukhaWithPrasrabdhi
    a sam:FactorIdentity .

dhy:PrasadaWithSraddha
    a sam:FactorIdentity .

dhy:PritiWithSaumanasya
    a sam:FactorIdentity .
```

## Commit History

```text
2026-07-25 — Initial kārikā-pass analysis.
```
