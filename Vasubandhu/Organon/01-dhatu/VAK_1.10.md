# VAK_1.10 — Counts Within the Meanings

## 1. Sanskrit (Devanāgarī)

```sanskrit
रूपं द्विधा विंशतिधा शब्दस्त्वष्टविधः रसः ।
षोढा चतुर्विधो गन्धः स्पृश्यमेकादशात्मकम् ॥ १.१० ॥
```

## 2. Sanskrit (IAST)

```text
rūpaṃ dvidhā viṃśatidhā śabdas tv aṣṭavidhaḥ rasaḥ /
ṣoḍhā caturvidho gandhaḥ spṛśyam ekādaśātmakam // 1.10 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| rūpam | nominative neuter singular | visible Form; one meaning, not the Form Base |
| dvidhā | adverb | twofold |
| viṃśatidhā | adverb | twentyfold; the same, counted |
| śabdaḥ | nominative masculine | sound |
| tu | particle | turns to the next |
| aṣṭavidhaḥ | nominative masculine | eightfold |
| rasaḥ | nominative masculine | taste |
| ṣoḍhā | adverb | sixfold; construes with taste |
| gandhaḥ | nominative masculine | odor |
| caturvidhaḥ | nominative masculine | fourfold; construes with odor |
| spṛśyam | nominative neuter | the tangible |
| ekādaśātmakam | bahuvrīhi; nominative neuter | having eleven as its nature |

*Rūpa* here is one of the five meanings. Not the Form Base of 1.09.

## 4. Grammar

```text
rūpam        dvidhā, and viṃśatidhā
śabdaḥ       aṣṭavidhaḥ
rasaḥ        ṣoḍhā
gandhaḥ      caturvidhaḥ
spṛśyam      ekādaśātmakam
```

Five counts. The twentyfold is the same visible Form, not a second meaning and not a second Base.

## 5. Translation

### Literal Translation

> Visible Form is twofold and twentyfold. Sound, however, is eightfold.
> Taste is sixfold. Odor is fourfold. The tangible has eleven as its nature.

### Bhāṣya-informed study translation

> Visible Form is twofold, color and configuration, and is further counted
> in twenty kinds. Sound has eight kinds, taste six, and odor four. The
> tangible has eleven kinds: the four Great Elements and seven derived
> tangibles.

## 6. Philosophical Translation

1.09 named five meanings. This verse counts inside them.

Visible Form is not the Form Base. It is one meaning, twofold as color and configuration. Both sides stay. The twenty are that same meaning enumerated: four colors, eight configurations, and eight further — cloud, smoke, dust, mist, shadow, sunlight, light, darkness. Some add a single-colored sky and make twenty-one. The verse does not.

Sound is four by cause and by sentient designation, then eight by agreeable and disagreeable. Taste is six. Odor is four; the treatise says three. The tangible is eleven. Hunger and thirst are absent in the Form Principle. The rest are there.

*Vid* in the prose is the sense of knowing, not the sense of existence. One substance known both as color and as configuration is not two substances. That sentence is not written into the count.

The five meanings are explained, and how they are taken. *Avijñapti* is next. Not this verse.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| rūpa | visible Form | one meaning; not the Form Base |
| varṇa | color | blue, yellow, red, white |
| saṃsthāna | configuration | long through uneven; eight |
| viṃśatidhā | twentyfold | the same meaning, counted; not twenty-one |
| śabda | sound | eightfold |
| rasa | taste | sixfold |
| gandha | odor | fourfold; the treatise says three |
| spṛśya | tangible | eleven as its nature |
| mahābhūta | Great Element | four of the eleven; defined later |
| vid | knowing | not existence; the prose |
| āyatana | Essence | the field of the count; not a new list |
| vijñāna | Cognition | what takes one or many; not a member |
| rūpadhātu | Form Principle | where hunger and thirst are absent |

## 8. Logical Determination

```text
1.09  five meanings named
1.10  each counted

visible Form
    color : configuration
    twenty of the same
    not twenty-one

sound      4 × agreeable / disagreeable = 8
taste      6
odor       4 in the verse; 3 in the treatise
tangible   4 Great Elements + 7 = 11

counts are not a second Base
vid = knowing, not existence
Cognition takes one or many
avijñapti not opened
```

## 9. Interpretive Note

The hinge is *dvidhā*, then *viṃśatidhā*. Color and configuration stay one meaning. The twenty do not found a second Base. The sky is not in the verse. *Vid* is knowing. The cognition arises from one substance or from many. That is not a second system.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_10 a vak:Karika ;
    vak:hasTopic vak:CountsWithinMeanings ;
    vak:belongsTo vak:Dhatunirdesa .

vak:VisibleForm vak:twofold vak:Color, vak:Configuration ;
    vak:count 20 ;
    vak:notCount 21 .

vak:Sound vak:count 8 .
vak:Taste vak:count 6 .
vak:Odor vak:count 4 .
vak:Tangible vak:count 11 .

vak:Vid vak:sense vak:Knowing ;
    vak:not vak:Existence .
```
