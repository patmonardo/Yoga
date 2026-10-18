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
| caturvidhaḥ | nominative masculine | fourfold; construes with odor |
| gandhaḥ | nominative masculine | odor |
| spṛśyam | nominative neuter | the tangible |
| ekādaśātmakam | bahuvrīhi; nominative neuter | having eleven as its nature |

*Rūpa* here is one of the five meanings. Not the Form Base of 1.09.

**Grammar tokens.** Verse-order IAST with sandhi opened. *Caturvidhaḥ*
precedes *gandhaḥ*, as in the lexical table. Compounds remain whole leaves; no covert token
is required.

```text
# tokens: rūpam dvidhā viṃśatidhā śabdaḥ tu aṣṭavidhaḥ rasaḥ ṣoḍhā caturvidhaḥ gandhaḥ spṛśyam ekādaśātmakam
```

## 4. Grammar

Five nominal clauses count within the meanings named in 1.09.
Adverbial *dvidhā*, *viṃśatidhā*, and *ṣoḍhā* do not agree like
adjectives. *Aṣṭavidhaḥ* and *caturvidhaḥ* agree with masculine sound
and odor; neuter *ekādaśātmakam* agrees with the tangible.

```nltk-fcfg
% start S
# tokens: rūpam dvidhā viṃśatidhā śabdaḥ tu aṣṭavidhaḥ rasaḥ ṣoḍhā caturvidhaḥ gandhaḥ spṛśyam ekādaśātmakam
S[SEM=<(?v & ?s & ?t & ?o & ?b)>] -> VISIBLE[SEM=?v] SOUND[SEM=?s] TASTE[SEM=?t] ODOR[SEM=?o] TANGIBLE[SEM=?b]
VISIBLE[SEM=<(?two(?meaning) & ?twenty(?meaning))>] -> N[K=visible,CASE=nom,SEM=?meaning] ADV[K=binary,SEM=?two] ADV[K=enumerated,SEM=?twenty]
SOUND[SEM=<?count(?meaning)>] -> N[K=sound,CASE=nom,NUM=?n,GEN=?g,SEM=?meaning] CONTRAST COUNT[K=eight,CASE=nom,NUM=?n,GEN=?g,SEM=?count]
TASTE[SEM=<?count(?meaning)>] -> N[K=taste,CASE=nom,SEM=?meaning] ADV[K=six,SEM=?count]
ODOR[SEM=<?count(?meaning)>] -> COUNT[K=four,CASE=nom,NUM=?n,GEN=?g,SEM=?count] N[K=odor,CASE=nom,NUM=?n,GEN=?g,SEM=?meaning]
TANGIBLE[SEM=<?count(?meaning)>] -> N[K=tangible,CASE=nom,NUM=?n,GEN=?g,SEM=?meaning] COUNT[K=eleven,CASE=nom,NUM=?n,GEN=?g,SEM=?count]
N[K=visible,CASE=nom,NUM=sg,GEN=n,SEM=<visible_meaning>] -> 'rūpam'
ADV[K=binary,SEM=<\x.TwofoldAnalysis(x)>] -> 'dvidhā'
ADV[K=enumerated,SEM=<\x.EnumeratedKinds(x,twenty)>] -> 'viṃśatidhā'
N[K=sound,CASE=nom,NUM=sg,GEN=m,SEM=<sound_meaning>] -> 'śabdaḥ'
CONTRAST -> 'tu'
COUNT[K=eight,CASE=nom,NUM=sg,GEN=m,SEM=<\x.EnumeratedKinds(x,eight)>] -> 'aṣṭavidhaḥ'
N[K=taste,CASE=nom,NUM=sg,GEN=m,SEM=<taste_meaning>] -> 'rasaḥ'
ADV[K=six,SEM=<\x.EnumeratedKinds(x,six)>] -> 'ṣoḍhā'
COUNT[K=four,CASE=nom,NUM=sg,GEN=m,SEM=<\x.EnumeratedKinds(x,four)>] -> 'caturvidhaḥ'
N[K=odor,CASE=nom,NUM=sg,GEN=m,SEM=<odor_meaning>] -> 'gandhaḥ'
N[K=tangible,CASE=nom,NUM=sg,GEN=n,SEM=<tangible_meaning>] -> 'spṛśyam'
COUNT[K=eleven,CASE=nom,NUM=sg,GEN=n,SEM=<\x.ElevenfoldConstitution(x)>] -> 'ekādaśātmakam'
```

```nltk-dep
'rūpam' -> 'dvidhā' | 'viṃśatidhā'
'śabdaḥ' -> 'tu' | 'aṣṭavidhaḥ'
'rasaḥ' -> 'ṣoḍhā'
'gandhaḥ' -> 'caturvidhaḥ'
'spṛśyam' -> 'ekādaśātmakam'
```

**Close construe.** Visible Form is twofold and twentyfold; sound,
however, eightfold; taste sixfold; odor fourfold; the tangible
has eleven as its nature.

The same visible meaning receives two distinct analyses: color and
configuration, then twenty enumerated kinds. The grammar does not
multiply two by twenty or introduce another Base. *Ekādaśātmakam*
specifies constitution, rather than merely another adverbial count.
Numeral constants are labels; the roster tests below verify cardinality
where the Bhāṣya supplies an explicit list.

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

Sound is four by cause and by sentient designation, then eight by agreeable and disagreeable. Taste is six. Odor is four; the treatise says three. The tangible is eleven. Hunger and thirst are absent in the Form Realm. The rest are there.

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
| rūpadhātu | Form Realm | where hunger and thirst are absent |

## 8. Logical Determination

**Kārikā, derived.** Constants designate the five meaning classifications,
not Faculties, Cognitions, or individual sensory episodes.

```nltk-sem
# derived by the section 4 parse
((TwofoldAnalysis(visible_meaning) & EnumeratedKinds(visible_meaning,twenty)) & EnumeratedKinds(sound_meaning,eight) & EnumeratedKinds(taste_meaning,six) & EnumeratedKinds(odor_meaning,four) & ElevenfoldConstitution(tangible_meaning))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((TwofoldAnalysis(visible_meaning) & EnumeratedKinds(visible_meaning,twenty)) & EnumeratedKinds(sound_meaning,eight) & EnumeratedKinds(taste_meaning,six) & EnumeratedKinds(odor_meaning,four) & ElevenfoldConstitution(tangible_meaning))
# THEORY prose
# EXPECT prose T
BinaryAspect(visible_meaning,color) & BinaryAspect(visible_meaning,configuration)
all x.(TangibleConstituent(x) <-> (GreatElement(x) | DerivedTangible(x)))
# THEORY rejected_visible_means_form_base
# EXPECT rejected_visible_means_form_base F
visible_meaning = form_base
```

```nltk-valuation
visible_meaning => visible_class
sound_meaning => sound_class
taste_meaning => taste_class
odor_meaning => odor_class
tangible_meaning => tangible_class
form_base => form_collection
twenty => count_twenty
eight => count_eight
six => count_six
four => count_four
color => color_aspect
configuration => configuration_aspect
TwofoldAnalysis => {visible_class}
EnumeratedKinds => {(visible_class,count_twenty),(sound_class,count_eight),(taste_class,count_six),(odor_class,count_four)}
ElevenfoldConstitution => {tangible_class}
BinaryAspect => {(visible_class,color_aspect),(visible_class,configuration_aspect)}
VisibleKind => {blue,yellow,red,white,long,short,round,circular,raised,lowered,even,uneven,cloud,smoke,dust,mist,shadow,sunlight,light,darkness}
TasteKind => {sweet,sour,salty,pungent,bitter,astringent}
GreatElement => {earth,water,fire,wind}
DerivedTangible => {smoothness,roughness,heaviness,lightness,cold,hunger,thirst}
TangibleConstituent => {earth,water,fire,wind,smoothness,roughness,heaviness,lightness,cold,hunger,thirst}
```

**Model checks.** The derived formula pins the verse's counts; it does
not calculate cardinalities from numeral labels. Separate tests count
the commentary's twenty visible kinds, six tastes, and eleven tangible
constituents. The two aspects are not twenty extra meanings. Form Base
and visible meaning have distinct denotations in this model.

**Bhāṣya determination.** Some teachers enumerate a single-colored sky
as a twenty-first visible kind; a cited treatise gives three odors.
Neither alternative replaces this verse's twenty and four. Sound's eight
comes from its fourfold classification divided by agreeable/disagreeable;
no eight-member roster is invented here. The damaged configuration line
remains unresolved. Knowing one substance in two respects does not
establish two substances: the prose's *vid* is knowing, not existence.

**Organon interpretation.** The earlier overview follows. Faculty,
meaning, and the Cognition supported in relation to them remain distinct
roles; this count does not define their unity as identity.

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
