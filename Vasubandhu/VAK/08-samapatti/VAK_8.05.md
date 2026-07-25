# VAK_8.05 — The Threefold Classification of the Eight Fundamental Attainments

## Sanskrit

### Devanāgarī

```text
इति मौलं समापत्तिद्रव्यमष्टविधं त्रिधा ।
सप्त आस्वादनवच्छुद्धानास्रवाणि अष्टमं द्विधा ॥ ८.५ ॥
```

### IAST

```text
iti maulaṃ samāpattidravyam aṣṭavidhaṃ tridhā /
sapta āsvādanavacchuddhānāsravāṇi aṣṭamaṃ dvidhā // VAK_8.05 //
```

## Source Caution

The source joins several compounds tightly:

```text
samāpatti-dravyam
āsvādana-vat
śuddha
anāsrava
```

This pass reads the verse as classifying the eight principal attainments according to mode rather than according to level.

The phrase `sapta ... aṣṭamaṃ dvidhā` is decisive:

```text
first seven attainments
    threefold

eighth attainment
    twofold
```

The exact reason for the exceptional twofold status of the eighth is carried into the next verse and bhāṣya discussion.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| iti | indeclinable | thus; in this way |
| maulam | nominative/accusative singular neuter of `maula` | fundamental; principal |
| samāpatti-dravyam | compound | the substantial set or determinate body of attainments |
| aṣṭavidham | nominative/accusative singular neuter | eightfold |
| tridhā | indeclinable | in three ways; threefold |
| sapta | nominative plural | seven |
| āsvādana-vat | compound | accompanied by savoring; associated with enjoyment |
| śuddha | compound member | pure; purified |
| anāsravāṇi | nominative plural neuter | without outflows; uncontaminated |
| aṣṭamam | nominative/accusative singular neuter | the eighth |
| dvidhā | indeclinable | twofold |

## Grammar

The first half summarizes the principal field:

```text
maulaṃ samāpatti-dravyam
    the fundamental body of meditative attainments

aṣṭavidham
    is eightfold

tridhā
    and is classified in three ways
```

The second half distributes the classification:

```text
sapta
    seven [of the eight]

āsvādanavat-śuddha-anāsravāṇi
    are savoring-associated,
    pure,
    and uncontaminated

 aṣṭamam dvidhā
    the eighth is twofold
```

The threefold series is therefore:

```text
āsvādanavat
śuddha
anāsrava
```

The verse leaves the reader to understand that the eighth lacks one of these three modes.

## Literal Translation

Thus the fundamental substance of meditative attainment is eightfold and threefold. Seven are accompanied by savoring, pure, and uncontaminated; the eighth is twofold.

## Philosophical Translation

The principal field of samāpatti consists of eight attainments. These are not exhausted by their vertical order, for they must also be classified according to the mode in which they are appropriated or realized. The first seven may occur as savoring-associated, as pure, or as uncontaminated. The eighth admits only two of these modes.

## Technical Vocabulary

### maula

```text
maula
    root-level
    fundamental
    principal
```

The term distinguishes the main attainments from their neighboring or preparatory states.

```text
principal attainment
    maula

preparatory threshold
    sāmantaka
```

### samāpatti-dravya

```text
samāpatti
    meditative attainment

dravya
    determinate existent
    substantial item
    real constituent of the classified field
```

The compound does not imply a permanent substance. It indicates that the eight attainments are counted as determinate members of the system.

### āsvādanavat

```text
āsvādana
    savoring
    tasting
    enjoyment
    relishing appropriation

āsvādanavat
    accompanied by savoring
```

This is not mere neutral experience of an attainment. The attainment is appropriated through attachment or relish.

### śuddha

```text
śuddha
    pure
    purified
    wholesome without supramundane liberation
```

The pure mode is distinguished both from attachment-laden savoring and from the uncontaminated supramundane mode.

### anāsrava

```text
an-āsrava
    without outflows
    uncontaminated
```

This is the liberative mode of attainment, no longer functioning as a support for renewed contamination.

## Doctrinal Determination

VAK 8.05 introduces a second axis of classification.

### Vertical axis — eight levels

```text
four dhyānas
    +
four formless attainments
    =
eight principal attainments
```

### Modal axis — three ways of occurrence

```text
savoring-associated
pure
uncontaminated
```

This gives a matrix rather than a simple list.

| Attainment range | Savoring-associated | Pure | Uncontaminated |
|---|---:|---:|---:|
| First seven | yes | yes | yes |
| Eighth | exceptional | yes/no according to next determination | yes/no according to next determination |

The kārikā does not yet fully unpack the eighth. It merely marks it as `dvidhā`.

## Logical Determination

The first four verses organized the field by ascending level:

```text
lower attainment
    →
higher attainment
```

VAK 8.05 cuts across that sequence with a new division:

```text
same attainment
    can appear under different modal determinations
```

Thus the system now has two dimensions:

```text
Level
    which attainment is it?

Mode
    how is that attainment possessed or realized?
```

The same meditative level is therefore not doctrinally identical in every case.

```text
attainment + savoring
    conditioned appropriation

attainment + purity
    wholesome stabilization

attainment + non-outflow
    liberative realization
```

This is the first major cross-classification of Chapter 8.

## Organon Light

The immediate doctrinal point should remain primary: the eight attainments do not form a one-dimensional ladder.

They form a structured field with at least two independent predicates:

```text
attainment-level
modal-quality
```

In platform language:

```text
SamapattiInstance
    hasLevel oneOf(EightPrincipalAttainments)
    hasMode oneOf(Savoring, Pure, Uncontaminated)
```

with a constraint:

```text
EighthAttainment
    admits only two modes
```

This is exactly the kind of restriction that later belongs naturally in a SHACL layer, but the present pass records only the kārikā-level architecture.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix sam: <http://127.0.0.1:3000/samapatti#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_8_05
    a vak:Karika ;
    rdfs:label "VAK 8.05" ;
    vak:determines sam:EightPrincipalAttainments,
                   sam:ThreefoldModalClassification,
                   sam:EighthAttainmentRestriction .

sam:EightPrincipalAttainments
    a sam:AttainmentSet ;
    sam:memberCount 8 .

sam:ThreefoldModalClassification
    a sam:ModalDivision ;
    sam:hasMember sam:SavoringAssociated,
                  sam:Pure,
                  sam:Uncontaminated .

sam:FirstSevenAttainments
    sam:admitsMode sam:SavoringAssociated,
                   sam:Pure,
                   sam:Uncontaminated .

sam:EighthAttainmentRestriction
    a sam:CardinalityConstraint ;
    sam:appliesTo sam:NeitherPerceptionNorNonPerception ;
    sam:allowedModeCount 2 .
```

## Commit History

```text
2026-07-25 — Initial kārikā-pass analysis.
```
