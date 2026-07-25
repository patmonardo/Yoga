# VAK_8.07 — Factors of the First and Second Dhyānas

## Sanskrit

### Devanāgarī

```text
पञ्चाद्ये तर्कचारौ च प्रीतिसौख्यसमाधयः ।
प्रीत्यादयः प्रसादश्च द्वितीयेऽङ्गचतुष्टयम् ॥ ८.७ ॥
```

### IAST

```text
pañcādye tarkacārau ca prītisaukhyasamādhayaḥ /
prītyādayaḥ prasādaś ca dvitīye 'ṅgacatuṣṭayam // VAK_8.07 //
```

## Source Caution

The source reads `tarka-cāra`, a compressed pair corresponding doctrinally to `vitarka-vicāra`.

This first kārikā pass therefore reads:

```text
tarka
    initial application or directed thought

cāra
    sustained examination or continued movement of thought
```

The term `prasāda` in the second dhyāna is kept as inner clarity, confidence, or serene lucidity without prematurely forcing a single English equivalent.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| pañca | numeral | five |
| ādye | locative singular | in the first |
| tarka | nominal stem | initial application; directed thought |
| cārau | dual compound member | tarka and vicāra |
| ca | indeclinable | and |
| prīti | noun | rapture; joy |
| saukhya | noun | pleasure; ease |
| samādhayaḥ | nominative plural | concentrations; collectedness |
| prīti-ādayaḥ | nominative plural | prīti and the remaining factors beginning with it |
| prasādaḥ | nominative singular | clarity; serene confidence |
| dvitīye | locative singular | in the second |
| aṅga-catuṣṭayam | nominative singular neuter | a fourfold set of limbs |

## Grammar

The first half enumerates the five limbs of the first dhyāna:

```text
pañca ādye
    five in the first

tarka-cārau
    tarka and vicāra

prīti-saukhya-samādhayaḥ
    rapture, pleasure, and concentration
```

The second half gives the four limbs of the second dhyāna:

```text
prītyādayaḥ
    prīti and the factors beginning with it

prasādaś ca
    and clarity

dvitīye aṅga-catuṣṭayam
    the fourfold set of limbs in the second
```

Thus the second dhyāna retains:

```text
prīti
sukha
samādhi
```

and adds:

```text
prasāda
```

while `tarka` and `vicāra` are absent.

## Literal Translation

In the first there are five: tarka and vicāra, together with rapture, pleasure, and concentration. In the second there is a fourfold set of limbs: rapture and the remaining factors beginning with it, together with clarity.

## Philosophical Translation

The first dhyāna is constituted by five factors: initial and sustained directed thought, rapture, pleasure, and collectedness. In the second dhyāna, the discursive pair falls away; rapture, pleasure, and collectedness remain, now joined by an inner clarity or serene confidence.

## Technical Vocabulary

### tarka and vicāra

The first dhyāna still includes directed mental movement.

```text
tarka
    initial placing of mind upon the object

vicāra
    continued examination or sustained movement
```

These are not defects in the first dhyāna. They are constitutive factors at that level.

### prīti

```text
prīti
    rapture
    joy
    energetic delight
```

Prīti is more activating than the settled ease indicated by `sukha`.

### sukha

```text
sukha
    pleasure
    ease
    well-being
```

The verse distinguishes the energetic uplift of prīti from the more stable agreeable tone of sukha.

### samādhi

Here `samādhi` is the factor of collectedness present within the attained configuration.

It should not be collapsed into the totality of `samāpatti`.

```text
samādhi
    organizing one-pointedness

samāpatti
    complete attained configuration
```

### prasāda

```text
prasāda
    clarity
    lucidity
    serene confidence
```

In the second dhyāna, the disappearance of tarka and vicāra is not mere subtraction. Their cessation permits a more inwardly unified clarity to appear.

## Doctrinal Determination

VAkK 8.07 gives the factor-structure of the first two dhyānas.

### First dhyāna

```text
1. tarka
2. vicāra
3. prīti
4. sukha
5. samādhi
```

### Second dhyāna

```text
1. prīti
2. sukha
3. samādhi
4. prasāda
```

The transition is therefore:

```text
first dhyāna
    discursive application remains

second dhyāna
    discursive application ceases
    inner clarity appears
```

The higher state is not simply the lower state minus two factors. It has a new positive determination.

## Logical Determination

The movement from the first to the second dhyāna has a double structure:

```text
negation
    tarka and vicāra fall away

positive emergence
    prasāda appears
```

So the transition is not:

```text
five factors
    → three factors
```

but:

```text
five-factor configuration
    → four-factor configuration
```

because one new factor replaces the discursive pair at the level of structural function.

This is the first clear example in the chapter where simplification produces a more inwardly unified determination rather than mere impoverishment.

## Organon Light

The first-pass point is exact and limited:

```text
first dhyāna
    unity mediated through directed thought

second dhyāna
    unity no longer dependent on directed thought
    and marked by inner clarity
```

The form realm therefore contains distinct modes of apprehension. The second dhyāna is not yet the formless apprehender as such; it is a more purified form of meditative apprehension within the rūpa domain.

The broader grahya–grahaṇa–grahītṛ reconstruction remains reserved for the later Organon pass.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix sam: <http://127.0.0.1:3000/samapatti#> .
@prefix dhy: <http://127.0.0.1:3000/dhyana#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_8_07
    a vak:Karika ;
    rdfs:label "VAK 8.07" ;
    vak:determines dhy:FirstDhyanaFiveFactors,
                   dhy:SecondDhyanaFourFactors .

dhy:FirstDhyanaFiveFactors
    a dhy:FactorConfiguration ;
    dhy:hasFactor dhy:Tarka,
                  dhy:Vicara,
                  dhy:Priti,
                  dhy:Sukha,
                  dhy:Samadhi .

dhy:SecondDhyanaFourFactors
    a dhy:FactorConfiguration ;
    dhy:hasFactor dhy:Priti,
                  dhy:Sukha,
                  dhy:Samadhi,
                  dhy:Prasada ;
    dhy:excludes dhy:Tarka,
                 dhy:Vicara .
```

## Commit History

```text
2026-07-25 — Initial kārikā-pass analysis.
```
