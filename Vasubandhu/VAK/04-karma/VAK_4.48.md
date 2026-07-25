# VAkK 4.48

## Sanskrit

### Devanāgarī

> अधोऽपि मध्यमस्त्येके ध्यानान्तरविपाकतः ।  
> अपूर्वाचरमः पाकस्त्रयाणां चेष्यते यतः ॥ ४.४८ ॥

### IAST

> **adho ’pi madhyam asty eke dhyānāntara-vipākataḥ |**  
> **apūrvācaramaḥ pākaḥ trayāṇāṃ ceṣyate yataḥ || 4.48 ||**

## Padaccheda

```text
adhaḥ api madhyamaḥ asti eke |
dhyāna-antara-vipākataḥ |
apūrva-acaramaḥ pākaḥ |
trayāṇām ca iṣyate yataḥ ||
```

The understood term after **madhyamaḥ** is the middle member of the preceding triad: **aduḥkhāsukha-vedya**, karma to be experienced as neither pain nor pleasure.

## Literal translation

> **Some hold that the middle kind exists even below, because it is the maturation of the intermediate dhyāna; for the maturation of the three is accepted as neither first nor last.**

The second half is unusually compressed and remains provisional pending the Bhāṣya.

## Doctrinal determination

VAkK 4.47 gave the principal distribution:

```text
first through third dhyāna
    → pleasantly experienced maturation

beyond the third dhyāna
    → neither-painful-nor-pleasant maturation

unwholesome desire-domain karma
    → painfully experienced maturation
```

VAkK 4.48 records a qualification attributed to **eke**, “some authorities”:

```text
neutral maturation
    may also occur below the fourth dhyāna

proposed case
    intermediate dhyāna
```

The **madhyama**, “middle,” is the middle feeling-result:

```text
sukha
aduḥkhāsukha
duḥkha
```

The verse therefore does not create a fourth category. It disputes the exact extension of one member of the established triad.

## Source caution

The expression:

```text
apūrvācaramaḥ pākaḥ trayāṇāṃ ceṣyate yataḥ
```

literally says that the maturation of the three is accepted as “not first and not last.” The precise doctrinal distribution of **apūrva** and **acarama**, and how it supports the intermediate-dhyāna claim, must be settled in the Bhāṣya pass.

## Philosophical translation

> **Some authorities extend neutral-feeling maturation below the level assigned to it by the principal rule. They regard it as a possible maturation of the intermediate dhyāna, since the three modes of felt maturation are not understood as rigidly confined to initial or terminal positions in the meditative sequence.**

## Logic of Experience

VAkK 4.47 supplied a general mapping:

```text
MEDITATIVE-LEVEL
    → FELT-MATURATION
```

VAkK 4.48 introduces a disputed boundary case:

```text
GENERAL RULE
    above third dhyāna
        → neutral maturation

MINORITY QUALIFICATION
    intermediate dhyāna
        → neutral maturation also
```

A useful feature structure is:

```text
[ FELT-MATURATION-CLASS
  VALUE neither-painful-nor-pleasant
  PRIMARY-RANGE above-third-dhyāna
  ALTERNATIVE-RANGE
      [ intermediate-dhyāna
        DOCTRINAL-STATUS disputed ] ]
```

The classification remains stable while the extension of one class is disputed.

## Organon interpretation

The verse distinguishes:

```text
INTENSION
    neutral maturation

EXTENSION
    the levels at which it occurs
```

Thus a class definition need not already contain its complete extension rule. The kārikā preserves the determinate concept while marking the point at which reflective mediation by the Bhāṣya is required.

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix karma: <http://127.0.0.1:3000/karma#> .
@prefix dhyana: <http://127.0.0.1:3000/dhyana#> .
@prefix doctrine: <http://127.0.0.1:3000/doctrine#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_48
    a vak:Karika ;
    rdfs:label "VAK 4.48" ;
    vak:continues vak:VAK_4_47 ;
    vak:hasTopic karma:NeutralFeltMaturation ;
    vak:recordsPosition doctrine:IntermediateDhyanaNeutralMaturationView .

doctrine:IntermediateDhyanaNeutralMaturationView
    a doctrine:DisputedPosition ;
    doctrine:asserts karma:IntermediateDhyanaNeutralMaturation ;
    doctrine:attributedTo doctrine:SomeAuthorities .

karma:IntermediateDhyanaNeutralMaturation
    karma:hasFeltMaturation karma:NeitherPainfulNorPleasant ;
    karma:hasProductionLevel dhyana:IntermediateDhyana ;
    doctrine:status doctrine:RequiresBhashyaReview .
```

## Determinate result

VAkK 4.48 establishes:

```text
some authorities maintain
that neither-painful-nor-pleasant maturation
also occurs below the fourth dhyāna

specifically
    as maturation of the intermediate dhyāna
```

Its methodological result is:

```text
the triadic classification is stable
but the precise extension of its middle member
is doctrinally disputed
```
