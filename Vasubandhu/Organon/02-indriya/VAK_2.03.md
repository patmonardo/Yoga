# VAK_2.03 — Class, Defilement, Purification

## 1. Sanskrit (Devanāgarī)

```sanskrit
निकायस्थितिसंक्लेशव्यवदानाधिपत्यतः ।
जीवितं वेदनाः पञ्च श्रद्धाद्याश्चेन्द्रियं मताः ॥ २.३ ॥
```

## 2. Sanskrit (IAST)

```text
nikāyasthitisaṃkleśavyavadānādhipatyataḥ /
jīvitaṃ vedanāḥ pañca śraddhādyāś cendriyaṃ matāḥ // 2.3 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| nikāya-sthiti | compound member | persistence of the living class |
| saṃkleśa | compound member | defilement |
| vyavadāna | compound member | purification |
| ādhipatyataḥ | ablative | because of governing efficacy |
| jīvitam | nominative neuter singular | life |
| vedanāḥ | nominative feminine plural | feelings |
| pañca | numeral, nominative plural | five: counts the feelings |
| śraddhā-ādyāḥ | nominative plural | those beginning with faith |
| ca | conjunction | and |
| indriyam | nominative neuter singular predicate | Faculty, read distributively |
| matāḥ | nominative plural participle | are held: the coordinated subjects together |

The compound gives three fields. The second line gives three groups, in that order.

**Grammar tokens.** The long causal compound remains one Sanskrit
token; its three fields are separated in `SEM`. External sandhi is
opened at *śraddhādyāś cendriyam*. The verse states five feelings; the
Bhāṣya, not the verse, specifies five beginning with faith.

```text
# tokens: nikāya-sthiti-saṃkleśa-vyavadāna-ādhipatyataḥ jīvitam vedanāḥ pañca śraddhā-ādyāḥ ca indriyam matāḥ
```

## 4. Grammar

The initial causal ablative gives three governed fields in order:
class-persistence, defilement, purification. The second line gives their
three bearer groups in the same order. The grammar unifies those orders
and makes the three governing relations explicit. *Pañca* counts only
*vedanāḥ*. Singular *indriyam* predicates Faculty distributively;
plural *matāḥ* agrees with the coordinated subjects and marks the
classification as held.

```nltk-fcfg
% start S
# tokens: nikāya-sthiti-saṃkleśa-vyavadāna-ādhipatyataḥ jīvitam vedanāḥ pañca śraddhā-ādyāḥ ca indriyam matāḥ
S[SEM=<(?fields & ?faculties)>] -> FIELDS[CASE=abl,ORDER=life_feeling_faith,SEM=?fields] GROUPS[ORDER=life_feeling_faith,SEM=?faculties]
FIELDS[CASE=abl,ORDER=life_feeling_faith,SEM=<(Governs(life_faculty,class_persistence) & all x.(FeelingFaculty(x) -> Governs(x,defilement)) & all x.(FaithSeriesFaculty(x) -> Governs(x,purification)))>] -> 'nikāya-sthiti-saṃkleśa-vyavadāna-ādhipatyataḥ'
GROUPS[ORDER=life_feeling_faith,SEM=<(Faculty(life_faculty) & all x.(FeelingFaculty(x) -> Faculty(x)) & all x.(FaithSeriesFaculty(x) -> Faculty(x)))>] -> LIFE[CASE=nom,NUM=sg,GEN=n] FEELGROUP[CASE=nom,NUM=pl,GEN=f,CNT=5] FAITH[CASE=nom,NUM=pl] CA FAC[CASE=nom,NUM=sg,GEN=n,DISTRIBUTIVE=true] HELD[NUM=pl,EVID=held]
LIFE[CASE=nom,NUM=sg,GEN=n] -> 'jīvitam'
FEELGROUP[CASE=nom,NUM=pl,GEN=f,CNT=5] -> FEEL[CASE=nom,NUM=pl,GEN=f] NUM[CNT=5]
FEEL[CASE=nom,NUM=pl,GEN=f] -> 'vedanāḥ'
NUM[CNT=5] -> 'pañca'
FAITH[CASE=nom,NUM=pl] -> 'śraddhā-ādyāḥ'
CA -> 'ca'
FAC[CASE=nom,NUM=sg,GEN=n,DISTRIBUTIVE=true] -> 'indriyam'
HELD[NUM=pl,EVID=held] -> 'matāḥ'
```

```nltk-dep
'matāḥ' -> 'jīvitam' | 'vedanāḥ' | 'śraddhā-ādyāḥ' | 'indriyam' | 'nikāya-sthiti-saṃkleśa-vyavadāna-ādhipatyataḥ'
'vedanāḥ' -> 'pañca'
'śraddhā-ādyāḥ' -> 'ca'
```

**Feature chart checkpoints.** The eight tokens form `FIELDS` [0, 1),
`GROUPS` [1, 8), and one root [0, 8). The `ORDER` feature links the
field triple to its bearer triple; changing it or the numeral's count
blocks the parse. `DISTRIBUTIVE=true` records the singular class noun's
force, while `EVID=held` records *matāḥ* outside the truth conditions.
The Bhāṣya confirms the ordered distribution; token order alone does
not establish it.

## 5. Translation

### Literal Translation

> Because of governing efficacy over class-persistence, defilement, and
> purification, life, the five feelings, and those beginning with faith are
> held to be faculty.

### Bhāṣya-informed study translation

> Life, the five feelings, and those beginning with faith are held to be
> Faculties through governing, respectively, class-persistence, defilement,
> and purification.

## 6. Philosophical Translation

> Facultyhood is explained here through governing class-persistence,
> defilement, and purification, beyond the apprehension treated in 2.02.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| nikāyasthiti | class-persistence | Bhāṣya: nikāyasabhāga-sthiti |
| jīvita | life-faculty | standing, not creation |
| vedanā | feeling | not the affliction |
| saṃkleśa | defilement | the Kośa Path, one side |
| vyavadāna | purification | the Kośa Path, the other side |
| anuśete | lies latent | relation of affliction to feeling; not identity |
| śraddhā | faith | first of the five |
| vīrya | vigor | |
| smṛti | mindfulness | |
| samādhi | concentration | |
| prajñā | discriminative comprehension | not discernment |
| viṣkambha | checking | not final abandonment |
| āvāhana | drawing forward | the path brought on |

## 8. Logical Determination

**Kārikā, derived.** The root `SEM` assigns life to class-persistence,
each feeling Faculty to defilement, and each member of the faith-series
to purification. It also predicates Faculty of each bearer. The
Bhāṣya specifies three feeling tones and two coordinated operations of
the five beginning with faith. Those specifications are separate
theories; neither feeling nor checking is identified with what it can
occasion or prepare.

```nltk-sem
fields : Governs(life_faculty,class_persistence) & all x.(FeelingFaculty(x) -> Governs(x,defilement)) & all x.(FaithSeriesFaculty(x) -> Governs(x,purification))
faculties : Faculty(life_faculty) & all x.(FeelingFaculty(x) -> Faculty(x)) & all x.(FaithSeriesFaculty(x) -> Faculty(x))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(Governs(life_faculty,class_persistence) & all x.(FeelingFaculty(x) -> Governs(x,defilement)) & all x.(FaithSeriesFaculty(x) -> Governs(x,purification))) & (Faculty(life_faculty) & all x.(FeelingFaculty(x) -> Faculty(x)) & all x.(FaithSeriesFaculty(x) -> Faculty(x)))

# THEORY prose_three_tones
# EXPECT prose_three_tones T
all x.(FeelingFaculty(x) -> exists t.(FeelingTone(t) & ToneOf(x,t)))
LatentIn(attachment,pleasant_tone) & LatentIn(aversion,painful_tone) & LatentIn(ignorance,neutral_tone)

# THEORY prose_purification_operations
# EXPECT prose_purification_operations T
all x.(FaithSeriesFaculty(x) -> (Faculty(x) & Governs(x,purification)))
ChecksAfflictions(faith_group) & DrawsPathForward(faith_group)

# THEORY prose_feeling_not_affliction
# EXPECT prose_feeling_not_affliction T
all x.(FeelingFaculty(x) -> -Affliction(x))

# THEORY rejected_feeling_is_affliction
# EXPECT rejected_feeling_is_affliction F
all x.(FeelingFaculty(x) -> Affliction(x))

# THEORY rejected_checking_is_abandonment
# EXPECT rejected_checking_is_abandonment F
all x.(ChecksAfflictions(x) -> AbandonsAfflictions(x))

# THEORY rejected_life_creates_class
# EXPECT rejected_life_creates_class F
all x.(Governs(x,class_persistence) -> CreatesClass(x))
```

The Bhāṣya's cited sūtra relates attachment, aversion, and ignorance
to pleasant, painful, and neutral feeling by *anuśete*; `LatentIn`
records that relation without asserting identity or production. The
five beginning with faith both check afflictions and bring the Path
forward; the source gives no order between those operations. The false
theories test three specific mistakes: feeling as affliction, checking
as final abandonment, and class-persistence as creation.

```nltk-valuation
life_faculty => life_d
class_persistence => class_standing
defilement => defilement_d
purification => purification_d
pleasant_tone => pleasant_d
painful_tone => painful_d
neutral_tone => neutral_d
attachment => attachment_d
aversion => aversion_d
ignorance => ignorance_d
faith_group => faith_group_d
FeelingFaculty => {pleasure,pain,gladness,distress,equanimity}
FaithSeriesFaculty => {faith,vigor,mindfulness,concentration,comprehension}
FeelingTone => {pleasant_d,painful_d,neutral_d}
ToneOf => {(pleasure,pleasant_d),(gladness,pleasant_d),(pain,painful_d),(distress,painful_d),(equanimity,neutral_d)}
Governs => {(life_d,class_standing),(pleasure,defilement_d),(pain,defilement_d),(gladness,defilement_d),(distress,defilement_d),(equanimity,defilement_d),(faith,purification_d),(vigor,purification_d),(mindfulness,purification_d),(concentration,purification_d),(comprehension,purification_d)}
Faculty => {life_d,pleasure,pain,gladness,distress,equanimity,faith,vigor,mindfulness,concentration,comprehension}
LatentIn => {(attachment_d,pleasant_d),(aversion_d,painful_d),(ignorance_d,neutral_d)}
ChecksAfflictions => {faith_group_d}
DrawsPathForward => {faith_group_d}
Affliction => {attachment_d,aversion_d,ignorance_d}
AbandonsAfflictions => {}
CreatesClass => {}
```

The finite valuation has five feeling Faculties, three tones, and five
members of the faith-series. The verse explicitly counts feelings;
the Bhāṣya specifies the faith count and the cited three-tone scheme.
The model witnesses these claims without proving exhaustive membership.
The other three of the eight mentioned in 2.01 enter at 2.04.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): Life governs the standing of the class, not its
arising. The five feelings govern the tones on which affliction lies.
Those beginning with faith govern purification by checking the afflictions
and drawing the path forward. Each is faculty by that efficacy.

2.01 named defilement and purification as the last distribution. 2.02 revised the six and the body-portion. This verse gives the predicate of the rest that are in view: life, the five feelings, and five of the eight.

The sūtra uses three tones. The verse counts five faculties. Pleasure and gladness are pleasant. Pain and distress are painful. Equanimity is neither. The tones are not a second list of faculties.

Pleasant feeling is not attachment. Painful feeling is not aversion. Neutral feeling is not ignorance. The citation does not say every feeling produces its affliction, and it does not tell a story about neutrality hiding ignorance.

The five check and draw. The two operations are coordinated. The text does not say checking must finish before the path begins, and it does not assign a separate operation to each of the five.

Interpretation: Defilement and purification are the Kośa Path. The faculties that govern them are its controllers. Life governs the standing of the class beside that path. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_03
    a vak:Karika ;
    rdfs:label "VAK 2.03" ;
    vak:hasTopic vak:ClassDefilementPurification ;
    vak:belongsTo vak:Indriyanirdesa .

vak:LifeFaculty vak:governs vak:ClassPersistence .
vak:FeelingFive vak:governs vak:Defilement .
vak:FiveBeginningWithFaith vak:governs vak:Purification .
vak:Feeling vak:notIdenticalWith vak:Affliction .
vak:Purification vak:checks vak:Affliction ;
    vak:drawsForward vak:Path .

organon:KosaPath
    organon:namedBy vak:Defilement, vak:Purification ;
    organon:controlledBy vak:FeelingFive, vak:FiveBeginningWithFaith ;
    organon:notTheVerseEnglish true .
```
