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

The three names are neuter singular Faculty designations. *Tathā*
distributes Facultyhood to each; the causal ablative assigns the first
two to successive attainments and the third to *nirvāṇa*. The Bhāṣya
confirms that distribution. `ALT=other_account` records the force of
*ādi*, which introduces another explanation of the same three rather
than a fourth Faculty or destination.

```nltk-fcfg
% start S
# tokens: ājñāsyāmi-ākhyam ājñā-ākhyam ājñātāvi-indriyam tathā uttarottara-saṃprāpti-nirvāṇa-ādi-ādhipatyataḥ
S[SEM=<(?each & ?reason)>] -> FIRST[CASE=nom,NUM=sg,GEN=n,ROLE=first] SECOND[CASE=nom,NUM=sg,GEN=n,ROLE=second] THIRD[CASE=nom,NUM=sg,GEN=n,ROLE=third] TATHA[DISTR=each,SEM=?each] REASON[CASE=abl,ALT=other_account,ORDER=first_second_third,SEM=?reason]
FIRST[CASE=nom,NUM=sg,GEN=n,ROLE=first] -> 'ājñāsyāmi-ākhyam'
SECOND[CASE=nom,NUM=sg,GEN=n,ROLE=second] -> 'ājñā-ākhyam'
THIRD[CASE=nom,NUM=sg,GEN=n,ROLE=third] -> 'ājñātāvi-indriyam'
TATHA[DISTR=each,SEM=<(Faculty(shall_know_faculty) & Faculty(knowledge_faculty) & Faculty(has_known_faculty))>] -> 'tathā'
REASON[CASE=abl,ALT=other_account,ORDER=first_second_third,SEM=<(GovernsAttainmentOf(shall_know_faculty,knowledge_faculty) & GovernsAttainmentOf(knowledge_faculty,has_known_faculty) & Governs(has_known_faculty,nirvana))>] -> 'uttarottara-saṃprāpti-nirvāṇa-ādi-ādhipatyataḥ'
```

```nltk-dep
'uttarottara-saṃprāpti-nirvāṇa-ādi-ādhipatyataḥ' -> 'ājñāsyāmi-ākhyam' | 'ājñā-ākhyam' | 'ājñātāvi-indriyam' | 'tathā'
```

**Feature chart checkpoints.** The five tokens yield one root. The
three `ROLE` features keep the named positions distinct; `DISTR=each`
marks the scope of *tathā*. The causal compound carries the ordered
first explanation, while `ALT=other_account` points to the separate
Bhāṣya theory below. No unspoken Faculty or attainment token is added.

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

**Kārikā, derived.** The parse predicates Faculty of each named item,
assigns the first two to attainment of their respective successors,
and assigns the third to *nirvāṇa*. This ordered distribution is
Bhāṣya-informed. It neither adds a fourth Faculty nor identifies the
verse's *nirvāṇa* with the prose's *parinirvāṇa*.

```nltk-sem
each : Faculty(shall_know_faculty) & Faculty(knowledge_faculty) & Faculty(has_known_faculty)
reason : GovernsAttainmentOf(shall_know_faculty,knowledge_faculty) & GovernsAttainmentOf(knowledge_faculty,has_known_faculty) & Governs(has_known_faculty,nirvana)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(Faculty(shall_know_faculty) & Faculty(knowledge_faculty) & Faculty(has_known_faculty)) & (GovernsAttainmentOf(shall_know_faculty,knowledge_faculty) & GovernsAttainmentOf(knowledge_faculty,has_known_faculty) & Governs(has_known_faculty,nirvana))

# THEORY first_account_prose
# EXPECT first_account_prose T
all x.((x = has_known_faculty) -> Governs(x,parinirvana))
all p.(Parinirvanes(p) -> LiberatedMind(p))

# THEORY other_account_prose
# EXPECT other_account_prose T
Governs(shall_know_faculty,abandonment_by_seeing) & Governs(knowledge_faculty,abandonment_by_cultivation) & Governs(has_known_faculty,present_pleasant_abiding)
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

The first prose account specifies *parinirvāṇa* and says liberated mind
is necessary for it; the rejected converse prevents sufficiency from
being read into that claim. The second account, signalled by *ādi*,
assigns abandonment by seeing, abandonment by cultivation, and
pleasant abiding in this life to the same three Faculties. The two
abandonment classes are not enumerated here. Present pleasant abiding
is distinct from *parinirvāṇa* and from the checking in 2.03.

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

The finite model witnesses the accepted and rejected readings. It does
not identify verse *nirvāṇa* with prose *parinirvāṇa*, establish a full
path-stage chronology, or prove that liberated mind suffices for final
attainment. The seeing-abandonment reading depends on the marked
Bhāṣya witness repair and remains provisional.

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
