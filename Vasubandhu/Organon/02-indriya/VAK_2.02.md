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

The first causal ablative specifies governing *upalabdhi* of each
faculty's own *artha*. *Sarvasya ca* widens the scope for mind, as the
Bhāṣya states; it does not assert a single apprehension of everything.
The numeral *ṣaṭ* ranges over the five and mind, while singular
*indriyam* predicates Faculty distributively. The second causal
ablative pairs female-being and male-being with the two faculties.
*Kāyāt* gives their bodily source; *tu* marks the turn to that distinct
reason for separate designation.

```nltk-fcfg
% start S
# tokens: sva-artha-upalabdhi-ādhipatyāt sarvasya ca ṣaṭ indriyam strītva-puṃstva-ādhipatyāt tu kāyāt strī-puruṣa-indriye
S[SEM=<(?a & ?b)>] -> SIX[SEM=?a] BODY[SEM=?b]
SIX[SEM=<(?own(?five) & (?all & ?faculty(?six)))>] -> OWN[CASE=abl,SEM=?own] ALL[CASE=gen,SEM=?all] CA NUM[CNT=6,FIVE=?five,SIX=?six] FAC[NUM=sg,SEM=?faculty]
BODY[SEM=<(?gov(?f)(?m) & (?from(?f) & (?from(?m) & ?fac)))>] -> SEXGOV[CASE=abl,SEM=?gov] TU FROM[CASE=abl,SEM=?from] SEXDUAL[NUM=du,F=?f,M=?m,SEM=?fac]
OWN[CASE=abl,SEM=<\P.all x.(P(x) -> exists y.(OwnMeaning(x,y) & GovernsApprehensionOf(x,y)))>] -> 'sva-artha-upalabdhi-ādhipatyāt'
ALL[CASE=gen,SEM=<all y.(Meaning(y) -> GovernsApprehensionOf(mind,y))>] -> 'sarvasya'
CA -> 'ca'
NUM[CNT=6,FIVE=<\x.SensoryFaculty(x)>,SIX=<\x.(SensoryFaculty(x) | (x = mind))>] -> 'ṣaṭ'
FAC[NUM=sg,SEM=<\P.all x.(P(x) -> Faculty(x))>] -> 'indriyam'
SEXGOV[CASE=abl,SEM=<\f.\m.(Governs(f,female_being) & Governs(m,male_being))>] -> 'strītva-puṃstva-ādhipatyāt'
TU -> 'tu'
FROM[CASE=abl,SEM=<\x.PortionOf(x,body_faculty)>] -> 'kāyāt'
SEXDUAL[NUM=du,F=<female_faculty>,M=<male_faculty>,SEM=<(Faculty(female_faculty) & Faculty(male_faculty))>] -> 'strī-puruṣa-indriye'
```

```nltk-dep
'indriyam' -> 'ṣaṭ' | 'sva-artha-upalabdhi-ādhipatyāt' | 'sarvasya' | 'ca'
'strī-puruṣa-indriye' -> 'strītva-puṃstva-ādhipatyāt' | 'tu' | 'kāyāt'
```

**Feature chart checkpoints.** The spans index the nine normalized
tokens. `CNT=6` fixes the class in the first clause, while `FIVE` and
`SIX` carry different semantic scopes. The dual's `F` and `M` features
bind each governed determination to its faculty. The source relation
from *kāyāt* applies to both.

| Span | Constituent | Derived content |
|---|---|
| [0, 5) | `SIX` | own-Meaning apprehension for the five; all-Meaning range for mind; six Faculties |
| [5, 9) | `BODY` | two ordered governing relations and two body-portion relations |
| [0, 9) | `S` | conjunction of both clauses |

The dependency block marks local heads. It does not itself derive
`SEM`. The Bhāṣya explains *kāyāt* as a portion of the body-faculty;
the case alone does not establish that relation.

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

**Kārikā, derived.** The parse assigns each of the sensory five governance
of its own-Meaning apprehension, gives mind governance over the range of all Meanings, and
predicates Faculty of those six. It then assigns the two sexed
governing relations and reads *kāyāt* through the Bhāṣya's specified
body-portion relation. The logical projection states a range for mind,
not simultaneous apprehension by an episode.

```nltk-sem
own : \P.all x.(P(x) -> exists y.(OwnMeaning(x,y) & GovernsApprehensionOf(x,y)))
all_meanings : all y.(Meaning(y) -> GovernsApprehensionOf(mind,y))
six : \x.(SensoryFaculty(x) | (x = mind))
faculty : \P.all x.(P(x) -> Faculty(x))
sexed_governance : \f.\m.(Governs(f,female_being) & Governs(m,male_being))
from_body : \x.PortionOf(x,body_faculty)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.(SensoryFaculty(x) -> exists y.(OwnMeaning(x,y) & GovernsApprehensionOf(x,y))) & (all y.(Meaning(y) -> GovernsApprehensionOf(mind,y)) & all x.((SensoryFaculty(x) | (x = mind)) -> Faculty(x))) & ((Governs(female_faculty,female_being) & Governs(male_faculty,male_being)) & (PortionOf(female_faculty,body_faculty) & (PortionOf(male_faculty,body_faculty) & (Faculty(female_faculty) & Faculty(male_faculty))))))

# THEORY prose
# EXPECT prose T
all x.(SensoryFaculty(x) -> exists y c.(OwnMeaning(x,y) & Meaning(y) & Condition(c) & PresentsMeaning(c,y) & ContributesToApprehension(c)))
all x.(SensoryFaculty(x) -> (CommonCauseAcrossField(x) & ApprehensionConformsTo(x) & SuperiorEfficacy(x)))
all x.((x = mind) -> (CommonCauseAcrossField(x) & ApprehensionConformsTo(x) & SuperiorEfficacy(x)))
all x.((x = visible_form) -> (Condition(x) & ContributesToApprehension(x)))
-SuperiorEfficacy(visible_form)
-Faculty(visible_form)
-DifferentSubstanceFromBody(female_faculty)
-DifferentSubstanceFromBody(male_faculty)

# THEORY rejected_condition_suffices
# EXPECT rejected_condition_suffices F
all x.(Condition(x) -> SuperiorEfficacy(x))

# THEORY rejected_all_at_once
# EXPECT rejected_all_at_once F
all i.(MindEpisode(i) -> ApprehendsEveryMeaningAtOnce(i))

# THEORY rejected_distinct_substances
# EXPECT rejected_distinct_substances F
exists x.((x = female_faculty) & DifferentSubstanceFromBody(x))
exists x.((x = male_faculty) & DifferentSubstanceFromBody(x))
```

The `prose` theory represents the Bhāṣya's answer to the objection that
*arthas* also contribute causally. The model keeps a sensory Condition
and the Meaning it presents in separate roles; that separation is an
Organon projection, not an additional Sanskrit distinction asserted by
this sentence. The Condition contributes to apprehension but lacks the
superior efficacy attributed to the faculty.
The common-cause and conformity claims are stated as the Bhāṣya's
tests, not as universal definitions of all causes. The last two prose
claims keep the separately named bodily portions from becoming distinct
substances. The rejected all-at-once theory demonstrates that mind's
range does not entail simultaneity.

```nltk-valuation
mind => manas
female_faculty => stri_indriya
male_faculty => purusa_indriya
body_faculty => kaya_indriya
female_being => stritva
male_being => pumstva
visible_form => rupa
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

The valuation is a finite witness, not a census or a proof from Sanskrit.
The first Bhāṣya objection also distinguishes cognition from later
avoidance of danger and denies that seeing is a second operation beside
visual cognition. Those arguments remain in the paired Bhāṣya study;
the verse's `SEM` does not silently contain them.

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
