# VAK_7.27 — The Four Modes of Cultivation

## Sanskrit

### Devanāgarī

```text
प्रतिलम्भनिषेवाख्ये शुभसंस्कृतभावने ।
प्रतिपक्षविनिर्धावभावने सास्रवस्य तु ॥ ७.२७ ॥
```

### IAST

```text
pratilambhaniṣevākhye śubhasaṃskṛtabhāvane /
pratipakṣavinirdhāvabhāvane sāsravasya tu // VAK_7.27 //
```

## Source Caution

The verse defines four technical senses of *bhāvanā*:

```text
pratilambha
    acquisition

niṣevā
    practice or repeated inhabitation

pratipakṣa
    opposition by an antidote

vinirdhāva
    expulsion or removal
```

The first two apply to wholesome conditioned dharmas. The latter two apply to impure dharmas.

The bhāṣya aligns these four with the four right efforts:

```text
bring forth the wholesome not yet arisen
strengthen the wholesome already arisen
prevent the unwholesome not yet arisen
destroy the unwholesome already arisen
```

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| pratilambha | noun | acquisition, attainment |
| niṣevā | noun | practice, repeated cultivation, familiarization |
| ākhye | locative dual or descriptive compound sense | called by the names |
| śubha-saṃskṛta-bhāvane | locative singular compound | in the cultivation of wholesome conditioned dharmas |
| pratipakṣa | noun | opposition, antidotal counterforce |
| vinirdhāva | noun | expulsion, driving out, removal |
| bhāvane | locative singular | in cultivation |
| sāsravasya | genitive singular | of the impure, contaminated |
| tu | particle | but, whereas |

## Grammar

The first half states:

```text
with respect to wholesome conditioned dharmas
cultivation is called
    acquisition
    and practice
```

The second half states:

```text
with respect to impure dharmas
cultivation is
    opposition
    and expulsion
```

The verse therefore distributes the word *bhāvanā* across two positive and two negative functions.

## Literal Translation

With respect to wholesome conditioned dharmas, cultivation is called acquisition and practice; but with respect to impure dharmas, it is cultivation by opposition and expulsion.

## Philosophical Translation

Cultivation does not mean one undifferentiated act of repetition. The Path operates in four ways: it acquires wholesome capacities not yet possessed, repeatedly inhabits those already present, opposes impure tendencies through antidotal forces, and expels impurities already active in the continuum.

## Technical Vocabulary

### pratilambha

```text
pratilambha
    acquisition
    first establishment of a wholesome capacity
```

This concerns what has not yet been possessed.

### niṣevā

```text
niṣevā
    practice
    repeated inhabitation
    strengthening through use
```

This concerns what has already arisen and is made stable through continued exercise.

### pratipakṣa

```text
pratipakṣa
    opposition
    antidotal counterforce
```

An impure tendency is prevented from arising because a contrary wholesome factor occupies the field.

### vinirdhāva

```text
vinirdhāva
    expulsion
    driving out
    removal of what is already active
```

This is stronger than simple non-arising. It concerns the destruction of an impurity already present.

## Doctrinal Determination

The fourfold schema is:

| Object | Mode of cultivation | Function |
|---|---|---|
| Wholesome not yet arisen | Acquisition | Bring it into the continuum |
| Wholesome already arisen | Practice | Strengthen and stabilize it |
| Impure not yet arisen | Opposition | Prevent its arising |
| Impure already arisen | Expulsion | Remove it from the continuum |

This explains why *bhāvanā* cannot be translated merely as meditation.

It is a complete Path operation:

```text
acquire
stabilize
prevent
remove
```

### Relation to the four right efforts

The bhāṣya places the four modes under the familiar four efforts:

```text
what is wholesome and absent
    produce

what is wholesome and present
    increase

what is unwholesome and absent
    prevent

what is unwholesome and present
    abandon
```

Thus cultivation is not passive contemplation. It is active regulation of the cognitive continuum.

### Distribution among dharmas

The bhāṣya further distinguishes:

```text
wholesome but impure dharmas
    susceptible to all four modes

pure dharmas
    susceptible to acquisition and practice

defiled and neutral dharmas
    susceptible to opposition and expulsion
```

This distribution is important for later Path Analytics, but no deeper system is imposed in this first pass.

## Logical Determination

The verse defines cultivation as a fourfold transformation calculus:

```text
absence of wholesome
    → acquisition

presence of wholesome
    → stabilization

possibility of impurity
    → opposition

actual impurity
    → expulsion
```

The distinction turns on two questions:

```text
Is the factor wholesome or impure?
Is it absent or already present?
```

These two divisions generate the four operations.

## Organon Light

The basic determination is:

> The Path does not merely produce new knowledge; it regulates what may arise, what should remain, what must be prevented, and what must be removed.

This gives the crystallization image a precise technical sense:

```text
clarity is acquired
clarity is stabilized
new turbidity is prevented
existing turbidity is expelled
```

The crystal does not become pure by addition alone. It becomes pure through coordinated acquisition, stabilization, opposition, and removal.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix marga: <http://127.0.0.1:3000/marga#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_27
    a vak:Karika ;
    rdfs:label "VAK 7.27" ;
    vak:determines marga:FourModesOfCultivation .

marga:FourModesOfCultivation
    a marga:PathOperationSet ;
    marga:hasOperation marga:Acquisition,
                       marga:Practice,
                       marga:Opposition,
                       marga:Expulsion .

marga:Acquisition
    marga:actsOn jna:WholesomeNotYetArisen .

marga:Practice
    marga:actsOn jna:WholesomeAlreadyArisen .

marga:Opposition
    marga:actsOn jna:ImpureNotYetArisen .

marga:Expulsion
    marga:actsOn jna:ImpureAlreadyArisen .
```

## Commit History

```text
2026-07-23 — Initial kārikā-pass analysis for VAK_7b.
```
