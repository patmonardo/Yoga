# VAK 6.02

## Sanskrit

### Devanāgarī

सत्यान्युक्तानि चत्वारि दुःखं समुदयस्तथा ।
निरोधमार्ग इत्येषां यथाभिसमयं क्रमः ॥ ६.२ ॥

### IAST

satyāny uktāni catvāri duḥkhaṃ samudayas tathā |
nirodho mārga ity eṣāṃ yathābhisamayaṃ kramaḥ || 6.2 ||

## Padaccheda

| Pada | Form | Determination |
|---|---|---|
| satyāni | nominative plural neuter | truths |
| uktāni | nominative plural neuter past passive participle | have been stated |
| catvāri | nominative plural neuter | four |
| duḥkham | nominative singular neuter | suffering |
| samudayaḥ | nominative singular masculine | arising; origin |
| tathā | indeclinable | likewise; and |
| nirodhaḥ | nominative singular masculine | cessation |
| mārgaḥ | nominative singular masculine | Path |
| iti | quotative particle | thus |
| eṣām | genitive plural | of these |
| yathā-abhisamayam | adverbial compound | according to direct realization |
| kramaḥ | nominative singular masculine | order; sequence |

## Grammar

The first half states:

```text
satyāni uktāni catvāri
    four truths have been stated
```

The four are then enumerated:

```text
duḥkham
samudayaḥ
nirodhaḥ
mārgaḥ
```

The final construction is:

```text
eṣāṃ kramaḥ
    the order of these

yathā-abhisamayam
    according to direct realization
```

The compound **yathābhisamayam** is crucial. It does not say merely that the truths are conventionally listed in this order. Their sequence corresponds to the order in which they are directly realized.

## Literal Translation

Four truths have been stated: suffering, origin, cessation, and Path. Their sequence is according to the order of direct realization.

## Philosophical Translation

Four truths have been established: the conditioned field of suffering, its arising ground, its cessation, and the Path. They are ordered according to the sequence in which truth is directly comprehended.

## Technical Vocabulary

### satya

**Satya** is truth, but here it does not mean merely a true proposition. The Four Truths are simultaneously what is the case and what must be directly realized.

### duḥkha

**Duḥkha** denotes the appropriated conditioned field insofar as it is unstable, afflicted, and incapable of furnishing final satisfaction.

### samudaya

**Samudaya** is arising, origination, or the ground from which the afflicted field repeatedly emerges.

```text
duḥkha
    manifested conditioned field

samudaya
    its recurrent generating ground
```

### nirodha

**Nirodha** is determinate cessation associated with disconnection from the kleśas, not merely accidental non-occurrence.

### mārga

**Mārga** is the determinate Path through which cessation becomes actual.

```text
nirodha
    what release is

mārga
    how release is actualized
```

### abhisamaya

Working translation:

```text
abhisamaya
    direct realization
    comprehensive realization
```

The truths are ordered according to the genetic order of their direct realization, not merely textbook enumeration.

## Analysis

VAK 6.01 established the Path-functions of seeing and cultivation. VAK 6.02 identifies the truth-objects of that seeing.

```text
duḥkha
    the conditioned field

samudaya
    its arising ground

nirodha
    its cessation

mārga
    the mediation of cessation
```

The order begins from the actuality of bondage, proceeds to its ground, then to cessation and its determinate mediation.

```text
cessation without knowledge of origin
    becomes imagined absence

Path without knowledge of bondage
    becomes external discipline
```

## Logical Determination

The truths form two closely related complexes:

```text
conditioned complex
    duḥkha
    samudaya

liberating complex
    nirodha
    mārga
```

Yet the movement is fourfold:

```text
1. Result
    duḥkha

2. Ground
    samudaya

3. Cessation
    nirodha

4. Mediation of cessation
    mārga
```

The Path is not merely the fourth item in a list. It is the truth that mediates the realized cessation of the first pair.

## Interpretive Note

The phrase **yathābhisamayaṃ kramaḥ** organizes the system according to the inner order of realization.

```text
The order of truth
is exhibited through
the order of its adequate knowing.
```

This is the architecture of a genuine Path of Knowing: the objects, modes, sequence, abandonments, and resulting persons will all be specified.

## Organon Note

```text
TruthComplex
├── DuhkhaTruth
├── SamudayaTruth
├── NirodhaTruth
└── MargaTruth
```

Essential relations:

```text
DuhkhaTruth
    hasGround SamudayaTruth

NirodhaTruth
    ceases DuhkhaSamudayaComplex

MargaTruth
    actualizes NirodhaTruth
```

## OWL++ Seed

```text
Class: Satya
Class: DuhkhaSatya
Class: SamudayaSatya
Class: NirodhaSatya
Class: MargaSatya
Class: Abhisamaya
Class: AbhisamayaSequence

DuhkhaSatya SubClassOf Satya
SamudayaSatya SubClassOf Satya
NirodhaSatya SubClassOf Satya
MargaSatya SubClassOf Satya

ObjectProperty: hasArisingGround
    Domain: DuhkhaSatya
    Range: SamudayaSatya

ObjectProperty: isCessationOf
    Domain: NirodhaSatya
    Range: DuhkhaSamudayaComplex

ObjectProperty: actualizesCessation
    Domain: MargaSatya
    Range: NirodhaSatya

ObjectProperty: directlyRealizes
    Domain: Abhisamaya
    Range: Satya

DataProperty: realizationPosition
    Domain: Satya
    Range: xsd:integer

Individual: VAK_6_02
    Types: Karika
    Facts:
        establishes FourTruths
        establishes AbhisamayaSequence
```

## Determinate Summary

```text
VAK 6.02

Four truths:
    duḥkha
    samudaya
    nirodha
    mārga

Their order:
    follows direct realization
    rather than arbitrary enumeration
```

The Four Truths are not merely taught. They constitute the ordered object of a direct Path of Knowing.
