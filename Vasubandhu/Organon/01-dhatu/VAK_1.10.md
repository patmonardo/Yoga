# VAK_1.10 — Counts Within the Meanings

## 1. Sanskrit (Devanāgarī)

> रूपं द्विधा विंशतिधा शब्दस्त्वष्टविधः रसः ।
>
> षोढा चतुर्विधो गन्धः स्पृश्यमेकादशात्मकम् ॥ १.१० ॥॥

## 2. Sanskrit (IAST)

> rūpaṃ dvidhā viṃśatidhā śabdas tv aṣṭavidhaḥ rasaḥ /
>
> ṣoḍhā caturvidho gandhaḥ spṛśyam ekādaśātmakam // 1.10 //

## 3. Lexical Analysis

```text
rūpam            → visible form; one meaning, not the form-base
dvidhā            → twofold
viṃśatidhā       → twentyfold
śabdas tu        → and sound; tu turns
aṣṭavidhaḥ       → eightfold
rṣoḍhā           → sixfold; construes with rasaḥ
caturvidhaḥ       → fourfold; construes with gandhaḥ
spṛśyam          → the tangible
ekādaśa-ātmakam  → having eleven as its nature
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| rūpam | nominative neuter | visible form |
| dvidhā | adverb | in two ways |
| viṃśatidhā | adverb | in twenty ways; the same, counted |
| śabdaḥ | nominative | sound |
| tu | particle | turns to the next |
| aṣṪvidhaḥ | nominative | eightfold |
| rasaḥ | nominative | taste |
| ṣoḍhā | adverb | sixfold |
| gandhaḥ | nominative | odor |
| caturvidhaḥ | nominative | fourfold |
| spṛśyam | nominative | the tangible |
| ekādaśa-ātmakam | nominative | eleven as its nature |

*Rūpa* here is one of the five meanings. Not the form-base of 1.09.

## 4. Grammar

```text
rūpam        dvidhā, and viṃśatidhā
śabdaḥ        aṣṪvidhaḥ
rasaḥ         ṣoḍhā
gandhaḥ       caturvidhaḥ
spṛśyam      ekādaśa-ātmakam
```

Five counts. The twentyfold is the same visible form, not a second meaning
and not a second base.

## 5. Translation

### Literal Translation

Visible form is twofold and twentyfold. Sound, however, is eightfold.
Taste is sixfold. Odor is fourfold. The tangible has eleven as its nature.

### Bhāṣya-informed study translation

Visible form is twofold, color and configuration, and the same is counted
as twenty. Sound is eightfold. Taste is sixfold. Odor is fourfold. The
tangible has eleven as its nature: the four great elements, and seven
further. The counts are the verse. How a principle takes one or many is
the prose.

## 6. Philosophical Translation

Again, one line of counts. The commentary supplies the dyad.

1.09 named five meanings. This verse counts inside them. Visible form is
not the form-base. It is one meaning, twofold as color and configuration.
Both sides stay. The twenty are that same meaning enumerated: four colors,
eight configurations, and eight further — cloud, smoke, dust, mist,
shadow, sunlight, light, darkness. Some add a single-colored sky and make
twenty-one. The verse does not.

Sound is four by cause and by sentient designation, then eight by
agreeable and disagreeable. Taste is six. Odor is four; the treatise says
three. The tangible is eleven. Hunger and thirst are absent in the
form-realm. The rest are there.

*Vid* in the prose is the sense of knowing, not the sense of existence.
One substance known both as color and as configuration is not two
substances. That sentence is not written into the count.

The five organ-meanings are explained, and how they are taken. *Avijñapti*
is next. Not this verse.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| rūpa | visible form | one meaning; not the form-base |
| varṇa | color | blue, yellow, red, white |
| saṃsthāna | configuration | long through uneven; eight |
| viṃśatidhā | twentyfold | the same meaning, counted |
| śabda | sound | eightfold |
| rasa | taste | sixfold |
| gandha | odor | fourfold; the treatise says three |
| spṛśya | tangible | eleven as its nature |
| mahābhūta | great element | four of the eleven; defined later |
| vid | knowing | not existence; the prose |
| āyatana | essence | the field of the count; not a new list |
| vijñāna | principle | what takes one or many; not a member |
| rūpadhātu | form-realm | where hunger and thirst are absent |

## 8. Logical Determination

```text
1.09  five meanings named
1.10  each counted

visible form
    color : configuration
    twenty of the same
    not twenty-one

sound      4 × agreeable / disagreeable = 8
taste      6
odor       4 in the verse; 3 in the treatise
tangible   4 elements + 7 = 11

counts ≠ a second base
vid = knowing, not existence
avijñapti not opened
```

## 9. Interpretive Note

The hinge is *dvidhā*, then *viṃśatidhā*. Interpretation of *vid* is in
the Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_10 a vak:Karika ;
    vak:hasTopic vak:CountsWithinMeanings ;
    vak:belongsTo vak:Dhatunirdesa .

vak:VisibleForm vak:twofold vak:Color, vak:Configuration ;
    vak:twentyfold true ;
    vak:isFormBase false .
vak:Sound vak:eightfold true .
vak:Taste vak:sixfold true .
vak:Odor vak:fourfold true .
vak:Tangible vak:hasNatureCount 11 .
vak:Vid vak:sense vak:Knowing ;
    vak:notSense vak:Existence .
```
