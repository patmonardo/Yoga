# VAK_2.04 — The Three That Complete the Eight

## 1. Sanskrit (Devanāgarī)

```sanskrit
आज्ञास्याम्याख्यमाज्ञाख्यमाज्ञातावीन्द्रियं तथा ।
उत्तरोत्तरसंप्राप्तिनिर्वाणाद्याधिपत्यतः ॥ २.४ ॥
```

## 2. Sanskrit (IAST)

```text
ājñāsyāmyākhyam ājñākhyam ājñātāvīndriyaṃ tathā /
uttarottarasaṃprāptinirvāṇādyādhipatyataḥ // 2.4 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| ājñāsyāmi-ākhyam | nominative neuter singular | the one called “I shall know”; Faculty supplied by tathā and the Bhāṣya |
| ājñā-ākhyam | nominative neuter singular | the one called knowledge; Faculty supplied likewise |
| ājñātāvi-indriyam | nominative neuter singular | the Faculty of one who has known |
| tathā | indeclinable | likewise: each individually is a Faculty |
| uttarottara-saṃprāpti | compound member | successive attainment |
| nirvāṇa | compound member | nirvāṇa |
| ādi | compound member | and the rest; a second account |
| ādhipatyataḥ | ablative | because of governing efficacy |

The short name is anājñātam ājñāsyāmi, I shall know what is not known.

**Grammar tokens.** External sandhi is opened between the three named
items. The final causal compound stays one token; its internal order is
represented in `SEM`. No additional spoken Faculty or attainment word
is inserted.

```text
# tokens: ājñāsyāmi-ākhyam ājñā-ākhyam ājñātāvi-indriyam tathā uttarottara-saṃprāpti-nirvāṇa-ādi-ādhipatyataḥ
```

## 4. Grammar

The first two neuter singular names abbreviate faculties; the third
contains *indriyam* overtly. The Bhāṣya states that *tathā* distributes
Facultyhood to each. The causal ablative answers why they are counted:
the compound orders successive attainment, nirvāṇa, and *ādi*. The
Bhāṣya's first explanation resolves the first two as governing
attainment of the next Faculty and the third as governing
*parinirvāṇa*. The verse itself says *nirvāṇa*, which the grammar keeps.
The *ādi* feature records that another explanation follows, rather
than fabricating an unspecified fourth member of the sequence.

```nltk-fcfg
% start S
# tokens: ājñāsyāmi-ākhyam ājñā-ākhyam ājñātāvi-indriyam tathā uttarottara-saṃprāpti-nirvāṇa-ādi-ādhipatyataḥ
S[SEM=<(?each(?f)(?s)(?t) & ?reason(?f)(?s)(?t))>] -> FIRST[CASE=nom,NUM=sg,GEN=n,SEM=?f] SECOND[CASE=nom,NUM=sg,GEN=n,SEM=?s] THIRD[CASE=nom,NUM=sg,GEN=n,SEM=?t] TATHA[DISTR=each,SEM=?each] REASON[CASE=abl,ALT=other_account,SEM=?reason]
FIRST[CASE=nom,NUM=sg,GEN=n,SEM=<shall_know_faculty>] -> 'ājñāsyāmi-ākhyam'
SECOND[CASE=nom,NUM=sg,GEN=n,SEM=<knowledge_faculty>] -> 'ājñā-ākhyam'
THIRD[CASE=nom,NUM=sg,GEN=n,SEM=<has_known_faculty>] -> 'ājñātāvi-indriyam'
TATHA[DISTR=each,SEM=<\f.\s.\t.(Faculty(f) & Faculty(s) & Faculty(t))>] -> 'tathā'
REASON[CASE=abl,ALT=other_account,SEM=<\f.\s.\t.(GovernsAttainmentOf(f,s) & GovernsAttainmentOf(s,t) & Governs(t,nirvana))>] -> 'uttarottara-saṃprāpti-nirvāṇa-ādi-ādhipatyataḥ'
```

```nltk-dep
'uttarottara-saṃprāpti-nirvāṇa-ādi-ādhipatyataḥ' -> 'ājñāsyāmi-ākhyam' | 'ājñā-ākhyam' | 'ājñātāvi-indriyam' | 'tathā'
```

**Feature chart checkpoints.** The five-token parse composes three
named Faculties with a distributed Faculty predicate and an ordered
governing relation. `ALT=other_account` belongs to the final compound's
*ādi*; it does not add a fourth Faculty or a new verse claim.

| Span | Constituent | Result |
|---|---|---|
| [0, 1) | `FIRST` | the Faculty named “I shall know” |
| [1, 2) | `SECOND` | the Faculty named “knowledge” |
| [2, 3) | `THIRD` | the Faculty of one who has known |
| [0, 5) | `S` | three Faculty predications and the ordered attainment–nirvāṇa sequence |

## 5. Translation

### Literal Translation

> Likewise, the one called “I shall know,” the one called knowledge, and the
> faculty of one who has known, because of governing efficacy over
> successive attainment, nirvāṇa, and the rest.

### Bhāṣya-informed study translation

> Likewise, each of the three is a Faculty: “I shall know” and “knowledge”
> govern attainment of their respective successors, and “one who has
> known” governs nirvāṇa; another account is also given.

## 6. Philosophical Translation

> The first two govern attainment of their successor Faculties; the
> third governs nirvāṇa. The further account explains the same three
> through abandonment and liberated abiding, without adding a fourth.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| anājñātam-ājñāsyāmi | I shall know what is not known | first of the three |
| ājñā | knowledge | the faculty-name; not the Idea |
| ājñātāvin | one who has known | completed in this sequence |
| uttarottara-saṃprāpti | successive attainment | the first two govern attainment of their respective successor Faculties |
| nirvāṇa / parinirvāṇa | nirvāṇa / parinirvāṇa | the verse says nirvāṇa; the Bhāṣya specifies parinirvāṇa |
| ādi | and so forth | the Bhāṣya takes it to signal another mode of explanation, not an open list of Faculties |
| avimukta-citta | mind not liberated | no parinirvāṇa |
| darśana-heya | abandoned by seeing | class of affliction |
| bhāvanā-heya | abandoned by cultivation | class of affliction |
| prahāṇa | abandonment | not the checking of 2.03 |
| dṛṣṭa-dharma-sukha-vihāra | pleasant abiding in this life | not parinirvāṇa |

## 8. Logical Determination

**Kārikā, derived.** The first two named Faculties govern attainment
of the next in the sequence; the third governs *nirvāṇa*. *Tathā*
distributes Facultyhood to all three. The parse does not turn the
names into tenses of one act, or treat *ādi* as a fourth destination.

```nltk-sem
each : \f.\s.\t.(Faculty(f) & Faculty(s) & Faculty(t))
reason : \f.\s.\t.(GovernsAttainmentOf(f,s) & GovernsAttainmentOf(s,t) & Governs(t,nirvana))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(Faculty(shall_know_faculty) & Faculty(knowledge_faculty) & Faculty(has_known_faculty) & GovernsAttainmentOf(shall_know_faculty,knowledge_faculty) & GovernsAttainmentOf(knowledge_faculty,has_known_faculty) & Governs(has_known_faculty,nirvana))

# THEORY first_account_prose
# EXPECT first_account_prose T
all x.((x = has_known_faculty) -> Governs(x,parinirvana))
all p.(Parinirvanes(p) -> LiberatedMind(p))

# THEORY other_account_prose
# EXPECT other_account_prose T
(Governs(shall_know_faculty,abandonment_by_seeing) & Governs(knowledge_faculty,abandonment_by_cultivation) & Governs(has_known_faculty,present_pleasant_abiding))
all x.(PleasantAbiding(x) -> ExperiencesLiberationJoyAndHappiness(x))

# THEORY rejected_liberation_suffices
# EXPECT rejected_liberation_suffices F
all p.(LiberatedMind(p) -> Parinirvanes(p))

# THEORY rejected_fourth_attainment
# EXPECT rejected_fourth_attainment F
exists x.((x = fourth_faculty) & GovernsAttainmentOf(has_known_faculty,x))

# THEORY rejected_abiding_is_parinirvana
# EXPECT rejected_abiding_is_parinirvana F
all p.(PleasantAbiding(p) -> Parinirvanes(p))
```

The first prose theory uses the Bhāṣya's *parinirvāṇa* where the verse
has *nirvāṇa*. Its negative sentence gives a necessary condition:
parinirvāṇa requires liberated mind. The rejected converse keeps this
from becoming a sufficient condition. The other prose theory is the
second explanation signalled by *ādi*: abandonment of afflictions
specified by seeing and by cultivation, then pleasant abiding in this
life. The model keeps that present abiding distinct from parinirvāṇa
and from the checking of afflictions in 2.03.

```nltk-valuation
shall_know_faculty => first_f
knowledge_faculty => second_f
has_known_faculty => third_f
fourth_faculty => fourth_f
nirvana => nirvana_goal
parinirvana => parinirvana_goal
abandonment_by_seeing => seeing_abandonment
abandonment_by_cultivation => cultivation_abandonment
present_pleasant_abiding => present_abiding
Faculty => {first_f,second_f,third_f}
GovernsAttainmentOf => {(first_f,second_f),(second_f,third_f)}
Governs => {(third_f,nirvana_goal),(third_f,parinirvana_goal),(first_f,seeing_abandonment),(second_f,cultivation_abandonment),(third_f,present_abiding)}
LiberatedMind => {living_realized,departed_realized}
Parinirvanes => {departed_realized}
PleasantAbiding => {living_realized}
ExperiencesLiberationJoyAndHappiness => {living_realized}
```

The finite witness tests the two explanations separately. It does not
identify verse *nirvāṇa* and prose *parinirvāṇa*, derive a historical
path-stage chronology, or prove the final attainment from liberated
mind alone. The Bhāṣya's seeing-abandonment reading rests on a
substantive witness repair, so that textual uncertainty remains marked.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): The three complete the series. The first governs
attainment of the next, the second governs attainment of the last, and the
third governs parinirvāṇa. They are not tenses of one act.

2.03 took five of the eight. This verse takes the three that remain, and the twenty-two are named. Their constitution is not yet analyzed.

The first account is attainment of the next, and then parinirvāṇa. The reason is narrow: no parinirvāṇa while mind is not liberated. It does not say liberated mind is already parinirvāṇa.

The second account is the work. Seeing and cultivation abandon specified classes. The text does not list the classes. Pleasant abiding is present experience of the joy and happiness of liberation. It is not ordinary pleasure, and it is not identified with parinirvāṇa.

Prahāṇa is abandonment. It is not the checking of 2.03, and it is not a generic improvement.

Interpretation: the three complete the controllers of purification on the Kośa Path. The principles remain deposited. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_04
    a vak:Karika ;
    rdfs:label "VAK 2.04" ;
    vak:hasTopic vak:ThreeThatCompleteTheEight ;
    vak:belongsTo vak:Indriyanirdesa .

vak:IShallKnow vak:governsAttainmentOf vak:KnowledgeFaculty ;
    vak:governs vak:AbandonmentBySeeing .
vak:KnowledgeFaculty vak:governsAttainmentOf vak:OneWhoHasKnown ;
    vak:governs vak:AbandonmentByCultivation .
vak:OneWhoHasKnown vak:governs vak:Parinirvana, vak:PleasantAbiding .

vak:Parinirvana vak:requires vak:LiberatedMind .

organon:PurificationControllers
    organon:completedBy vak:VAK_2_04 ;
    organon:notTheVerseEnglish true .
```
