# VAK_2.18 — What Possession Entails

## 1. Sanskrit (Devanāgarī)

```sanskrit
चतुर्भिः सुखकायाभ्यां पञ्चभिश्चक्षुरादिमान् ।
सौमनस्यी च दुःखी तु सप्तभिः स्त्रीन्द्रियादिमान् ॥ २.१८ ॥
```

## 2. Sanskrit (IAST)

```text
caturbhiḥ sukhakāyābhyāṃ pañcabhiś cakṣurādimān /
saumanasyī ca duḥkhī tu saptabhiḥ strīndriyādimān // 2.18 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| caturbhiḥ | instrumental plural numeral | with four [Faculties], necessarily possessed |
| sukha-kāyābhyām | instrumental dual neuter compound | through pleasure or body, distributively, not jointly |
| pañcabhiḥ | instrumental plural numeral | with five [Faculties] |
| cakṣur-ādi-mān | nominative singular masculine possessive compound | one possessing eye or another of the locally specified four |
| saumanasyī | nominative singular masculine possessive adjective | one possessing gladness; shares the five-count |
| ca | coordinating particle | and |
| duḥkhī | nominative singular masculine possessive adjective | one possessing Pain-Faculty |
| tu | contrastive particle | however |
| saptabhiḥ | instrumental plural numeral | with seven [Faculties] |
| strī-indriya-ādi-mān | nominative singular masculine possessive compound | one possessing Female-Faculty and so forth; count completed in 2.19 |

The dual distributes four over two cases. It does not make pleasure and body one set of four.

**Grammar tokens.** External sandhi is opened; compounds remain intact.
The final subject has no numeral in this verse. Its eight-count is
supplied only in the cross-verse continuation.

```text
# tokens: caturbhiḥ sukha-kāyābhyām pañcabhiḥ cakṣurādimān saumanasyī ca duḥkhī tu saptabhiḥ strīndriyādimān
```

## 4. Grammar

The opening dual distributes the four-count over two separate possession
cases. The eye-group and gladness share five, but not the same members.
Pain takes seven. The final possessor subject continues into 2.19's
eight. Necessarily possesses is carried from the ongoing question and
repeated in the prose; none of the counts excludes extra Faculties.

```nltk-fcfg
% start S
# tokens: caturbhiḥ sukha-kāyābhyām pañcabhiḥ cakṣurādimān saumanasyī ca duḥkhī tu saptabhiḥ strīndriyādimān
S[SEM=<(?four & ?five & ?seven & ?tail)>] -> FOURCLAUSE[SEM=?four] FIVECLAUSE[SEM=?five] SEVENCLAUSE[SEM=?seven] TAIL[CONTINUED=next_verse,SEM=?tail]
FOURCLAUSE[SEM=<(NecessaryCount(pleasure_f,?count) & NecessaryCount(body_f,?count))>] -> FOUR[CASE=ins,CNT=4,SEM=?count] PAIR[CASE=ins,NUM=du,READING=distributive]
FIVECLAUSE[SEM=<(EyeGroupCount(?count) & NecessaryCount(?glad,?count))>] -> FIVE[CASE=ins,CNT=5,SEM=?count] EYES[CASE=nom,GEN=m] GLAD[CASE=nom,GEN=m,SEM=?glad] AND
SEVENCLAUSE[SEM=<NecessaryCount(?pain,?count)>] -> PAIN[CASE=nom,GEN=m,SEM=?pain] BUT SEVEN[CASE=ins,CNT=7,SEM=?count]
FOUR[CASE=ins,CNT=4,SEM=<four>] -> 'caturbhiḥ'
PAIR[CASE=ins,NUM=du,READING=distributive] -> 'sukha-kāyābhyām'
FIVE[CASE=ins,CNT=5,SEM=<five>] -> 'pañcabhiḥ'
EYES[CASE=nom,GEN=m] -> 'cakṣurādimān'
GLAD[CASE=nom,GEN=m,SEM=<gladness_f>] -> 'saumanasyī'
AND -> 'ca'
PAIN[CASE=nom,GEN=m,SEM=<pain_f>] -> 'duḥkhī'
BUT -> 'tu'
SEVEN[CASE=ins,CNT=7,SEM=<seven>] -> 'saptabhiḥ'
TAIL[CONTINUED=next_verse,SEM=<FemaleAndOthersSubject>] -> 'strīndriyādimān'
```

```nltk-dep
'caturbhiḥ' -> 'sukha-kāyābhyām'
'pañcabhiḥ' -> 'cakṣurādimān' | 'saumanasyī' | 'ca'
'saptabhiḥ' -> 'duḥkhī' | 'tu' | 'strīndriyādimān'
```

The dependency block checks vocabulary coverage, not dependency parsing;
the final subject is attached for coverage only, not as a seven-count
case. Its predicate is outside this verse.

| Span | Constituent | Result |
|---|---|---|
| [0, 2) | `FOURCLAUSE` | two distributive four-count cases |
| [2, 6) | `FIVECLAUSE` | eye-group and gladness five-counts |
| [6, 9) | `SEVENCLAUSE` | pain seven-count |
| [9, 10) | `TAIL` | subject continued into the next verse |
| [0, 10) | `S` | numbered verse without silently inserting eight |

## 5. Translation

### Literal Translation

> With four, in the cases of pleasure and body. One possessing the eye and
> so forth, with five, and one possessing gladness. One possessing pain,
> however, with seven. One possessing the female faculty and so forth.

### Bhāṣya-informed study translation

> One possessing Pleasure-Faculty or Body-Faculty necessarily possesses
> four Faculties; one possessing eye or another of that group, five;
> one possessing gladness also, five; one possessing pain, however,
> seven. One possessing Female-Faculty and so forth [necessarily
> possesses eight].

## 6. Philosophical Translation

> The necessary companions are fixed by the faculty possessed. There is no single rule for the remainder.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| samanvāgata | possessing | not occurring now |
| cakṣur-ādi | eye and so forth | ear, nose, tongue; separate cases |
| strī-indriya-ādi | female and so forth | male, distress, the five; another range |
| dvitīya-dhyāna-ja | born in the second dhyāna | the test |
| tṛtīya-dhyāna-alābhin | not attained the third | possession without attainment |
| kliṣṭa | afflicted | the third-level pleasure in the answer |

## 8. Logical Determination

**Kārikā, derived.** The verse gives four, five, and seven, followed by
the next clause's subject. The eight-count and its different member-sets
are identified as a cross-verse prose elaboration.

```nltk-sem
necessary_count : \f.\n.NecessaryCount(f,n)
eye_count : EyeGroupCount(five)
continued_subject : FemaleAndOthersSubject
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(NecessaryCount(pleasure_f,four) & NecessaryCount(body_f,four) & EyeGroupCount(five) & NecessaryCount(gladness_f,five) & NecessaryCount(pain_f,seven) & FemaleAndOthersSubject)

# THEORY prose_closures
# EXPECT prose_closures T
all x.all y.all z.((Possesses(x,y) & Requires(y,z)) -> Possesses(x,z))
all x.(Requires(pleasure_f,x) <-> (CoreThree(x) | x = pleasure_f))
all x.(Requires(body_f,x) <-> (CoreThree(x) | x = body_f))
all x.(Requires(gladness_f,x) <-> (CoreThree(x) | x = pleasure_f | x = gladness_f))
all x.(Requires(pain_f,x) <-> PainSeven(x))
(SecondDhyanaBorn(second_person) & -ThirdDhyanaAttained(second_person) & Possesses(second_person,pleasure_f) & AfflictedThirdLevelPleasure(second_person))

# THEORY cross_verse_eights
# EXPECT cross_verse_eights T
all x.(Requires(female_f,x) <-> (PainSeven(x) | x = female_f))
all x.(Requires(distress_f,x) <-> (PainSeven(x) | x = distress_f))
all x.(Requires(faith_f,x) <-> (CoreThree(x) | FaithFive(x)))

# THEORY rejected_gladness_without_pleasure
# EXPECT rejected_gladness_without_pleasure F
exists x.(Possesses(x,gladness_f) & -Possesses(x,pleasure_f))

# THEORY rejected_faith_entails_pain
# EXPECT rejected_faith_entails_pain F
all x.(Possesses(x,faith_f) -> Possesses(x,pain_f))

# THEORY rejected_possession_requires_third_attainment
# EXPECT rejected_possession_requires_third_attainment F
all x.(Possesses(x,pleasure_f) -> ThirdDhyanaAttained(x))
```

```nltk-valuation
pleasure_f => pleasure
body_f => body
gladness_f => gladness
pain_f => pain
female_f => female
distress_f => distress
faith_f => faith
second_person => second_dhyana_person
four => count_four
five => count_five
seven => count_seven
NecessaryCount => {(pleasure,count_four),(body,count_four),(gladness,count_five),(pain,count_seven)}
EyeGroupCount => {count_five}
FemaleAndOthersSubject => True
CoreThree => {neutral,life,mind}
PainSeven => {body,life,mind,pain,pleasure,gladness,neutral}
FaithFive => {faith,vigor,mindfulness,concentration,comprehension}
Requires => {(pleasure,neutral),(pleasure,life),(pleasure,mind),(pleasure,pleasure),(body,neutral),(body,life),(body,mind),(body,body),(eye,neutral),(eye,life),(eye,mind),(eye,body),(eye,eye),(ear,neutral),(ear,life),(ear,mind),(ear,body),(ear,ear),(nose,neutral),(nose,life),(nose,mind),(nose,body),(nose,nose),(tongue,neutral),(tongue,life),(tongue,mind),(tongue,body),(tongue,tongue),(gladness,neutral),(gladness,life),(gladness,mind),(gladness,pleasure),(gladness,gladness),(pain,body),(pain,life),(pain,mind),(pain,pain),(pain,pleasure),(pain,gladness),(pain,neutral),(female,body),(female,life),(female,mind),(female,pain),(female,pleasure),(female,gladness),(female,neutral),(female,female),(male,body),(male,life),(male,mind),(male,pain),(male,pleasure),(male,gladness),(male,neutral),(male,male),(distress,body),(distress,life),(distress,mind),(distress,pain),(distress,pleasure),(distress,gladness),(distress,neutral),(distress,distress),(faith,faith),(faith,vigor),(faith,mindfulness),(faith,concentration),(faith,comprehension),(faith,neutral),(faith,life),(faith,mind),(vigor,faith),(vigor,vigor),(vigor,mindfulness),(vigor,concentration),(vigor,comprehension),(vigor,neutral),(vigor,life),(vigor,mind),(mindfulness,faith),(mindfulness,vigor),(mindfulness,mindfulness),(mindfulness,concentration),(mindfulness,comprehension),(mindfulness,neutral),(mindfulness,life),(mindfulness,mind),(concentration,faith),(concentration,vigor),(concentration,mindfulness),(concentration,concentration),(concentration,comprehension),(concentration,neutral),(concentration,life),(concentration,mind),(comprehension,faith),(comprehension,vigor),(comprehension,mindfulness),(comprehension,concentration),(comprehension,comprehension),(comprehension,neutral),(comprehension,life),(comprehension,mind)}
Possesses => {(second_dhyana_person,neutral),(second_dhyana_person,life),(second_dhyana_person,mind),(second_dhyana_person,pleasure),(second_dhyana_person,gladness),(faith_person,neutral),(faith_person,life),(faith_person,mind),(faith_person,faith),(faith_person,vigor),(faith_person,mindfulness),(faith_person,concentration),(faith_person,comprehension)}
SecondDhyanaBorn => {second_dhyana_person}
ThirdDhyanaAttained => {}
AfflictedThirdLevelPleasure => {second_dhyana_person}
```

`Requires` means necessary co-possession, not causal production or
simultaneous manifestation. Its reflexive entries count the given
Faculty itself. The faith-person is an illustrative countermodel to
deriving the pain-seven from faith, not an exhaustive biography.
The afflicted third-level pleasure is the source's short answer;
no latent mechanism is supplied. Cardinality tests check every
closure and distinguish the different eight-member sets.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): Possession is not uniform. Pleasure and body each
require four. The eye and the rest, and gladness, require five. Pain
requires seven. The female faculty and those gathered with it require
eight. The five beginning with faith require a different eight. The
necessary companions are fixed by the faculty possessed; there is no
single rule for the remainder.

The closures are minimums. They do not say no other faculty can be possessed.

Eye requires body, and body requires the triad. Gladness requires pleasure, and pleasure requires the triad. Two ways to five.

The second-dhyāna answer is short. It does not explain the mechanism. Latent would add a theory the sentence does not give. The claim is the afflicted third-level pleasure, possessed, the dhyāna not attained.

Distress is the next eight, not part of the seven. The faith eight does
not add to the pain seven. The prose's tu marks that distinction.

Interpretation: the set, the initiating faculty, and the relation. A number alone loses the determination. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_18
    a vak:Karika ;
    rdfs:label "VAK 2.18" ;
    vak:hasTopic vak:PossessionClosure ;
    vak:belongsTo vak:Indriyanirdesa .

vak:PleasureFaculty vak:closesOn 4 .
vak:EyeFaculty vak:closesOn 5 .
vak:GladnessFaculty vak:closesOn 5 .
vak:PainFaculty vak:closesOn 7 .

organon:VAK_2_18_Interpretation
    organon:distinguishes vak:GivenFaculty, vak:NecessaryCompanions,
        vak:PossessionCount .
```
