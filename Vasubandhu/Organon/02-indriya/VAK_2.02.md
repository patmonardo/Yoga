# VAK_2.02 — Own Meaning, and the Body-Portion

## 1. Sanskrit (Devanāgarī)

```sanskrit
स्वार्थोपलब्ध्याधिपत्यात् सर्वस्य च षडिन्द्रियम् ।
स्त्रीत्वपुंस्त्वाधिपत्यात्तु कायात् स्त्रीपुरुषेन्द्रिये ॥ २.२ ॥
```

## 2. Sanskrit (IAST)

```text
svārthopalabdhyādhipatyāt sarvasya ca ṣaḍindriyam /
strītvapuṃstvādhipatyāt tu kāyāt strīpuruṣendriye // 2.2 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sva-artha-upalabdhi-ādhipatyāt | ablative of cause | because of governing efficacy in apprehending one's own meaning |
| sarvasya | genitive | of everything |
| ca | conjunction | and; mind's range |
| ṣaṭ indriyam | numeral and nominative neuter singular predicate | the six are each Faculty |
| strītva-puṃstva-ādhipatyāt | ablative of cause | because of governing female-being and male-being |
| tu | particle | but |
| kāyāt | ablative | from the body-faculty, as its portion in the Bhāṣya |
| strī-puruṣa-indriye | nominative dual | the female and male faculties |

**Grammar tokens.** External sandhi is opened at *ṣaḍindriyam*;
the two causal compounds and the final dual remain whole. The five
sensory faculties and mind are Bhāṣya-resolved semantic referents, not
supplied Sanskrit tokens.

```text
# tokens: sva-artha-upalabdhi-ādhipatyāt sarvasya ca ṣaṭ indriyam strītva-puṃstva-ādhipatyāt tu kāyāt strī-puruṣa-indriye
```

## 4. Grammar

The first causal ablative assigns governance of apprehension to each of
the five with respect to its own *artha*. *Sarvasya ca* widens the range
for mind; it does not describe one episode apprehending everything at
once. The singular *indriyam* predicates Faculty distributively of six.
The second ablative gives the ordered female/male governing relation;
*kāyāt* is resolved by the Bhāṣya as a portion of the body-faculty.
The two clauses compose directly into a closed `SEM`.

```nltk-fcfg
% start S
# tokens: sva-artha-upalabdhi-ādhipatyāt sarvasya ca ṣaṭ indriyam strītva-puṃstva-ādhipatyāt tu kāyāt strī-puruṣa-indriye
S[SEM=<(?six & ?body)>] -> SIX[SEM=?six] BODY[SEM=?body]
SIX[SEM=<(all x.(SensoryFaculty(x) -> exists y.(OwnMeaning(x,y) & GovernsApprehensionOf(x,y))) & all y.(Meaning(y) -> GovernsApprehensionOf(mind,y)) & all x.((SensoryFaculty(x) | (x = mind)) -> Faculty(x)))>] -> OWN[CASE=abl,ROLE=own_apprehension] ALL[CASE=gen,SCOPE=all_meanings] CA SIX_NUM[CNT=6] FAC[NUM=sg,DISTRIBUTIVE=true]
OWN[CASE=abl,ROLE=own_apprehension] -> 'sva-artha-upalabdhi-ādhipatyāt'
ALL[CASE=gen,SCOPE=all_meanings] -> 'sarvasya'
CA -> 'ca'
SIX_NUM[CNT=6] -> 'ṣaṭ'
FAC[NUM=sg,DISTRIBUTIVE=true] -> 'indriyam'
BODY[SEM=<(Governs(female_faculty,female_being) & Governs(male_faculty,male_being) & PortionOf(female_faculty,body_faculty) & PortionOf(male_faculty,body_faculty) & Faculty(female_faculty) & Faculty(male_faculty))>] -> SEXGOV[CASE=abl,ORDER=female_male] TU FROM[CASE=abl,REL=portion] SEXDUAL[CASE=nom,NUM=du,ORDER=female_male]
SEXGOV[CASE=abl,ORDER=female_male] -> 'strītva-puṃstva-ādhipatyāt'
TU -> 'tu'
FROM[CASE=abl,REL=portion] -> 'kāyāt'
SEXDUAL[CASE=nom,NUM=du,ORDER=female_male] -> 'strī-puruṣa-indriye'
```

```nltk-dep
'indriyam' -> 'ṣaṭ' | 'sva-artha-upalabdhi-ādhipatyāt' | 'sarvasya' | 'ca'
'strī-puruṣa-indriye' -> 'strītva-puṃstva-ādhipatyāt' | 'tu' | 'kāyāt'
```

**Feature chart checkpoints.** The nine normalized tokens form `SIX`
[0, 5), `BODY` [5, 9), and one root [0, 9). Changing the six-count,
mind's all-meaning scope, the ordered dual, or the ablative body source
blocks the parse. The `SEM` gives a range for mind, not simultaneous
apprehension; the Bhāṣya's portion relation resolves *kāyāt*.

## 5. Translation

### Literal Translation

> Because of governing efficacy in the apprehension of their own meaning,
> and of all, the six are faculty. But because of governing efficacy over
> female-being and male-being, the female and male faculties are from the
> body.

### Bhāṣya-informed study translation

> The five are Faculties by governing apprehension of their own meanings;
> mind is a Faculty by governing apprehension of all meanings. The female
> and male Faculties are separately designated within the body-faculty
> because they govern female-being and male-being.

## 6. Philosophical Translation

> The six are Faculties through governing apprehension of Meaning. The
> female and male Faculties are named within the body-faculty through a
> different governing relation.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| sva-artha | own meaning | the five each have a respective Meaning; not the project Object |
| upalabdhi | apprehension | not a rank below cognition |
| ādhipatya | governing efficacy | superior power, adhikaṃ prabhutvam |
| sarvasya | of all meanings | mind's quantified range; not all at once |
| ṣaḍindriya | the six faculties | five and mind |
| kāyāt | from the body-faculty | a portion; not another entity |
| strītva | female-being | form, voice, movement, intention |
| puṃstva | male-being | form, voice, movement, intention |
| saṃkleśa / vyavadāna | defilement / purification | the Kośa Path; not this verse's predicate |

## 8. Logical Determination

**Kārikā, derived.** The root `SEM` says each sensory Faculty governs
apprehension of a respective meaning, mind governs apprehension across
the range of meanings, and all six are Faculties. The paired Bhāṣya
resolves *kāyāt* as the same body-faculty's portion. Its objection then
tests why a meaning that contributes to apprehension lacks the Faculty's
superior governing efficacy. That reasoning is a separate prose theory.

```nltk-sem
six : all x.(SensoryFaculty(x) -> exists y.(OwnMeaning(x,y) & GovernsApprehensionOf(x,y))) & all y.(Meaning(y) -> GovernsApprehensionOf(mind,y)) & all x.((SensoryFaculty(x) | (x = mind)) -> Faculty(x))
body : Governs(female_faculty,female_being) & Governs(male_faculty,male_being) & PortionOf(female_faculty,body_faculty) & PortionOf(male_faculty,body_faculty) & Faculty(female_faculty) & Faculty(male_faculty)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.(SensoryFaculty(x) -> exists y.(OwnMeaning(x,y) & GovernsApprehensionOf(x,y))) & all y.(Meaning(y) -> GovernsApprehensionOf(mind,y)) & all x.((SensoryFaculty(x) | (x = mind)) -> Faculty(x))) & (Governs(female_faculty,female_being) & Governs(male_faculty,male_being) & PortionOf(female_faculty,body_faculty) & PortionOf(male_faculty,body_faculty) & Faculty(female_faculty) & Faculty(male_faculty))

# THEORY prose_superior_efficacy
# EXPECT prose_superior_efficacy T
all x.(SensoryFaculty(x) -> (CommonCauseAcrossField(x) & ApprehensionConformsTo(x) & SuperiorEfficacy(x)))
CommonCauseAcrossField(mind) & ApprehensionConformsTo(mind) & SuperiorEfficacy(mind)

# THEORY prose_meaning_as_condition
# EXPECT prose_meaning_as_condition T
Condition(visible_form) & PresentsMeaning(visible_form,visual_meaning) & ContributesToApprehension(visible_form) & -SuperiorEfficacy(visible_form) & -Faculty(visible_form)

# THEORY prose_same_body
# EXPECT prose_same_body T
PortionOf(female_faculty,body_faculty) & PortionOf(male_faculty,body_faculty) & -DifferentSubstanceFromBody(female_faculty) & -DifferentSubstanceFromBody(male_faculty)

# THEORY rejected_condition_suffices
# EXPECT rejected_condition_suffices F
all x.(Condition(x) -> SuperiorEfficacy(x))

# THEORY rejected_all_at_once
# EXPECT rejected_all_at_once F
all i.(MindEpisode(i) -> ApprehendsEveryMeaningAtOnce(i))

# THEORY rejected_distinct_substances
# EXPECT rejected_distinct_substances F
DifferentSubstanceFromBody(female_faculty) & PortionOf(female_faculty,body_faculty)
```

```nltk-valuation
mind => manas
female_faculty => stri_indriya
male_faculty => purusa_indriya
body_faculty => kaya_indriya
female_being => stritva
male_being => pumstva
visible_form => rupa
visual_meaning => visual_meaning
SensoryFaculty => {eye,ear,nose,tongue,kaya_indriya}
Faculty => {eye,ear,nose,tongue,kaya_indriya,manas,stri_indriya,purusa_indriya}
Meaning => {visual_meaning,auditory_meaning,olfactory_meaning,gustatory_meaning,tactile_meaning,dharma_meaning}
GovernsApprehensionOf => {(eye,visual_meaning),(ear,auditory_meaning),(nose,olfactory_meaning),(tongue,gustatory_meaning),(kaya_indriya,tactile_meaning),(manas,visual_meaning),(manas,auditory_meaning),(manas,olfactory_meaning),(manas,gustatory_meaning),(manas,tactile_meaning),(manas,dharma_meaning)}
Governs => {(stri_indriya,stritva),(purusa_indriya,pumstva)}
PortionOf => {(stri_indriya,kaya_indriya),(purusa_indriya,kaya_indriya)}
OwnMeaning => {(eye,visual_meaning),(ear,auditory_meaning),(nose,olfactory_meaning),(tongue,gustatory_meaning),(kaya_indriya,tactile_meaning)}
Condition => {rupa,sabda,gandha,rasa,sprastavya}
PresentsMeaning => {(rupa,visual_meaning),(sabda,auditory_meaning),(gandha,olfactory_meaning),(rasa,gustatory_meaning),(sprastavya,tactile_meaning)}
ContributesToApprehension => {rupa,sabda,gandha,rasa,sprastavya}
CommonCauseAcrossField => {eye,ear,nose,tongue,kaya_indriya,manas}
ApprehensionConformsTo => {eye,ear,nose,tongue,kaya_indriya,manas}
SuperiorEfficacy => {eye,ear,nose,tongue,kaya_indriya,manas}
DifferentSubstanceFromBody => {}
MindEpisode => {mind_episode}
ApprehendsEveryMeaningAtOnce => {}
```

The valuation tests mind's range without treating it as an all-at-once
episode. The sensory condition and the meaning it presents have separate
roles in this Organon projection; that distinction is not another
Sanskrit word in the verse. Countermodels reject causal contribution as
sufficient for Faculty status and reject separate bodily substances.
The finite witness is not a census or proof from Sanskrit.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): The six are faculty by governing apprehension—five of
their own meaning, mind of all. The female and male faculties are not
further substances; they are the body-faculty named apart because they
govern female-being and male-being.

2.01 distributed four matters, two, defilement, and purification. This verse is the revision of the first distribution. The unnamed others keep cognition as the place of governing efficacy, and refuse a second operation called seeing. The reply is svārthopalabdhi.

Superior power is the cut against the meaning. The eye is common across visible form, and apprehension follows the eye's condition. Visible form is a condition. It does not govern. The same up to mind and dharmas. Mind's all and mind's dharmas are both kept. They are not synonyms.

Female and male receive a name inside the body-faculty. The portion is local. The governed configuration is wider: form, voice, movement, intention. That is the transmitted account. It is not a modern theory of sex.

Interpretation: Applied Indriya Theory, with the extension inside the body-faculty. Defilement and purification are the Kośa Path. The faculties that govern them are its controllers. Not the verse English. Not this verse's predicate.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_02
    a vak:Karika ;
    rdfs:label "VAK 2.02" ;
    vak:hasTopic vak:OwnMeaningAndBodyPortion ;
    vak:belongsTo vak:Indriyanirdesa .

vak:SensoryFive vak:governs vak:ApprehensionOfOwnMeaning .
vak:MindFaculty vak:governs vak:ApprehensionOfAll .
vak:Meaning vak:notA vak:Indriya .
vak:FemaleFaculty vak:partOf vak:BodyFaculty .
vak:MaleFaculty vak:partOf vak:BodyFaculty .

organon:KosaPath
    organon:namedBy vak:Defilement, vak:Purification ;
    organon:controlledBy vak:FeelingFive, vak:EightBeginningWithFaith ;
    organon:notThePredicateOf vak:VAK_2_02 .
```
