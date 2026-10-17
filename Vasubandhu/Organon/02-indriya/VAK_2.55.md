# VAK_2.55 — Times of the Causes

## 1. Sanskrit (Devanāgarī)

```sanskrit
सर्वत्रगः सभागश्च द्वयध्वगौ त्र्यध्वगास्त्रयः ।
संस्कृतं सविसंयोगं फलं नासंस्कृतस्य ते ॥ २.५५ ॥
```

## 2. Sanskrit (IAST)

```text
sarvatragaḥ sabhāgaś ca dvayadhvagau tryadhvagās trayaḥ /
saṃskṛtaṃ savisaṃyogaṃ phalaṃ nāsaṃskṛtasya te // 2.55 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sarvatragaḥ sabhāgaḥ | masculine nominative singular adjectives | pervasive and homogeneous |
| dvayadhvagau | masculine nominative dual compound adjective | ranging over two times |
| tryadhvagāḥ trayaḥ | masculine nominative plural compound adjective + masculine nominative plural numeral | three, ranging over three times |
| saṃskṛtam | neuter nominative singular adjective | the conditioned |
| savisaṃyogam | neuter nominative singular compound adjective | together with disconnection |
| phalam | neuter nominative singular | fruit |
| nāsaṃskṛtasya te | genitive singular compound adjective + nominative plural pronoun | those are not of the unconditioned |

## 4. Grammar

```text
% start S
S[CAUSE=pervasive|homogeneous] -> Time[PAST=true, PRESENT=true]
S[CAUSE=co-arisen|associated|maturation] -> Time[THREE=true]
S[CAUSE=conditioning] -> Time[ALL=true, DISSOCIATED=true]
S[FRUIT=true] -> Conditioned | Disconnection
```

Pervasive and homogeneous are past and present.  
Co-arisen, associated, maturation are three times.  
Conditioning is all times and not in time.  
Disconnection is a fruit of the Path and not its product.

## 5. Translation

### Literal Translation

> The pervasive and homogeneous range over two times; three causes range
> over three. The conditioned, together with disconnection, is fruit;
> those causes are not fruits of the unconditioned.
### Bhāṣya-informed study translation

> The pervasive and homogeneous causes span two times, past and present;
> the co-arisen, associated, and maturation causes span all three. Fruit
> is conditioned dharma together with disconnection; those causes are not
> fruits of the unconditioned.
## 6. Philosophical Translation

> Pervasive and homogeneous are past and present. The three are three times. Conditioning is all times and not in time. Disconnection is a fruit of the Path and not its product. Entity or absence is not settled.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| adhvan | time | past, present, future |
| visaṃyoga | disconnection | fruit, not product |
| pratisaṃkhyā | Discrimination | the cessation's name |
| prapaṇa | bringing to | not production |
| prāpti | acquisition | what is produced |

## 8. Logical Determination

```text
pervasive, homogeneous
    past, present
co-arisen, associated, maturation
    three times
conditioning
    all times, and not in time
product
    → conditioned
disconnection
    fruit of the Path
    not caused by the Path
entity or absence
    not settled
```

## 9. Interpretive Note

**Translation note.** The Bhāṣya identifies disconnection as cessation by
discriminative comprehension. The Path produces acquisition and brings one
to disconnection, but is not its cause. The status of the unconditioned
within the cause-and-fruit matrix is debated rather than settled.

The assignment of which fruit to which cause is the next verse. The debate is recorded, not closed.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_55 a vak:Karika ; vak:hasTopic vak:TemporalScope .
vak:Disconnection vak:produced false .
```
