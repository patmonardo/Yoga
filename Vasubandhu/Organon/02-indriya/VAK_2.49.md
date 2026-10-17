# VAK_2.49 — Six Causes

## 1. Sanskrit (Devanāgarī)

> कारणं सहभूश्चैव सभागः संप्रयुक्तकः ।
>
> सर्वत्रगो विपाकाख्यः षड्विधो हेतुरिष्यते ॥ २.४९ ॥

## 2. Sanskrit (IAST)

> kāraṇaṃ sahabhūś caiva sabhāgaḥ saṃprayuktakaḥ /
>
> sarvatrago vipākākhyaḥ ṣaḍvidho hetur iṣyate // 2.49 //

## 3. Lexical Analysis

| Pada | Force |
|---|---|
| kāraṇam | conditioning cause |
| sahabhūḥ | co-arisen |
| sabhāgaḥ | homogeneous |
| saṃprayuktakaḥ | associated |
| sarvatragaḥ | pervasive |
| vipāka-ākhyaḥ | called maturation |
| ṣaḍvidhaḥ hetuḥ | cause, sixfold |
| iṣyate | is held |

## 4. Grammar

```text
% start S
S[CAUSE=six] -> Conditioning | CoArisen | Homogeneous | Associated | Pervasive | Maturation
S[CAUSE=conditioning] -> NonObstruction[TOWARD=arising, OTHER=self]
S[CAUSE=conditioning, PRINCIPAL=true] -> AlsoProduce
```

Six causes held, not proved.  
Conditioning is non-obstruction toward what arises.  
Principal also produces. Not agency.

## 5. Translation

### Literal Translation

Conditioning, and co-arisen, homogeneous, associated, pervasive, and that called maturation: cause is held to be sixfold.

### Bhāṣya-informed study translation

> Cause is held to be sixfold: conditioning, co-arisen, homogeneous, associated, pervasive, and maturation. Conditioning is all other than itself, by non-obstruction toward what is arising. A principal conditioning cause can also produce. Non-obstruction is not productive agency. The conditioning cause has been explained.

## 6. Philosophical Translation

> Six causes held, not proved. Conditioning is non-obstruction toward what arises. Principal also produces. Not agency. Pratyaya is not this list.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| kāraṇa-hetu | conditioning cause | non-obstruction; principal also produces |
| avighna | non-obstruction | toward what is arising |
| kāraka | productive agency | refused for the broad field |
| kāraṇa-paraṃparā | succession of causes | the other account |

## 8. Logical Determination

```text
six
    named
    one defined
broad
    other than itself
    non-obstruction of what arises
    ≠ productive
principal
    also produces
    eye and form, food, seed
agency
    not transferred by non-obstruction
succession
    others
    not the definition
pratyaya
    not this list
```

## 9. Interpretive Note

The first clause of the next verse is this definition. The co-arisen cause is the next study. Not opened.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_49 a vak:Karika ; vak:hasTopic vak:SixCauses .
vak:KaranaHetu vak:broad vak:NonObstruction .
```
