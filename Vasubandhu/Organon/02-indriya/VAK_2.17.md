# VAK_2.17 — The Necessary Three

## 1. Sanskrit (Devanāgarī)

```sanskrit
एकादशभिरर्हत्त्वमुक्तं त्वेकस्य संभवात् ।
उपेक्षाजीवितमनोयुक्तोऽवश्यं त्रयान्वितः ॥ २.१७ ॥
```

## 2. Sanskrit (IAST)

```text
ekādaśabhir arhattvam uktaṃ tv ekasya saṃbhavāt /
upekṣājīvitamanoyukto 'vaśyaṃ trayānvitaḥ // 2.17 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| ekādaśabhiḥ | instrumental plural numeral | through eleven [Faculties] |
| arhattvam | nominative singular neuter noun | arhatship |
| uktam | nominative singular neuter past passive participle | is said; agrees with arhatship |
| tu | contrastive particle | however |
| ekasya | genitive singular numeral, substantival | of one [person], not one moment |
| saṃbhavāt | ablative singular masculine noun | because of the possibility |
| upekṣā-jīvita-mano-yuktaḥ | nominative singular masculine compound | one endowed with any one of neutral feeling, life, or Mind, as resolved by the Bhāṣya |
| avaśyam | indeclinable | necessarily |
| traya-anvitaḥ | nominative singular masculine compound | endowed with those three; not exactly three Faculties in total |

Any one is the commentary's anyatamena. The kārikā compresses it.

**Grammar tokens.** External sandhi is opened; compounds remain intact. The first clause completes the preceding attainment inquiry. The second begins necessary possession, with the Bhāṣya resolving the compound as any one of the three.

```text
# tokens: ekādaśabhiḥ arhattvam uktam tu ekasya saṃbhavāt upekṣā-jīvita-mano-yuktaḥ avaśyam traya-anvitaḥ
```

## 4. Grammar

The instrumental eleven belongs to the report of attainment. The genitive one person depends on possibility, and the ablative gives the explanation. It does not say all eleven are possessed at once. In the second clause, the masculine subject and predicate describe the person. Necessarily scopes the possession implication for any person; it does not turn possession into simultaneous occurrence of all three. The *avaśyam* lexical SEM supplies that universal scope.

```nltk-fcfg
% start S
# tokens: ekādaśabhiḥ arhattvam uktam tu ekasya saṃbhavāt upekṣā-jīvita-mano-yuktaḥ avaśyam traya-anvitaḥ
S[SEM=<(?report & ?possession)>] -> REPORT[SEM=?report] POSSESSION[SEM=?possession]
REPORT[SEM=<ReportedAttainmentCount(arhatship,eleven) & PossibleAcrossAttainments(one_person)>] -> ELEVEN FRUIT SAID BUT ONE POSSIBILITY
ELEVEN -> 'ekādaśabhiḥ'
FRUIT -> 'arhattvam'
SAID -> 'uktam'
BUT -> 'tu'
ONE -> 'ekasya'
POSSIBILITY -> 'saṃbhavāt'
POSSESSION[SEM=<all x.((Possesses(x,neutral_f) | Possesses(x,life_f) | Possesses(x,mind_f)) -> (Possesses(x,neutral_f) & Possesses(x,life_f) & Possesses(x,mind_f)))>] -> ANYONE NECESSARILY ALLTHREE
ANYONE -> 'upekṣā-jīvita-mano-yuktaḥ'
NECESSARILY -> 'avaśyam'
ALLTHREE -> 'traya-anvitaḥ'
```

```nltk-dep
'uktam' -> 'ekādaśabhiḥ' | 'arhattvam' | 'tu' | 'saṃbhavāt'
'saṃbhavāt' -> 'ekasya'
'traya-anvitaḥ' -> 'upekṣā-jīvita-mano-yuktaḥ' | 'avaśyam'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 6) | `REPORT` | eleven reported across one person's attainments |
| [6, 9) | `POSSESSION` | any one of the three entails all three |
| [0, 9) | `S` | attainment report followed by possession implication |

## 5. Translation

### Literal Translation

> Arhatship is said through eleven, however, because of the possibility for one person. One endowed with neutral feeling, life, or mind is necessarily accompanied by the three.

### Bhāṣya-informed study translation

> Arhatship is said to be attained through eleven Faculties, however, because that is possible across one person's repeated attainments. One who possesses any one of neutral feeling, life, or Mind necessarily possesses all three.

## 6. Philosophical Translation

> Possession of any one of neutral feeling, life, or Mind entails the other two. This is neither exactly three Faculties nor three factors continuously occurring together.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| samanvāgata | possessing | not attained, not occurring |
| avaśyam | necessarily | none without the others |
| aniyama | no fixed rule | the remainder |
| apratilabdha | not acquired | distinct from a Faculty acquired and subsequently lost |
| vihīna | lost | no longer possessed; distinct from a possessed Faculty that is currently inactive |
| samucchinna-kuśala-mūla | severed wholesome roots | lacks the five |

## 8. Logical Determination

**Kārikā, derived.** The SEM joins the carried eleven-person report to the reciprocal possession implication. The *avaśyam* SEM scopes the implication over persons. Necessity is represented as a universal rule in this finite model, not as modal logic. Neither simultaneous attainment nor continuous occurrence is asserted.

```nltk-sem
any_of_three : Possesses(p,neutral_f) | Possesses(p,life_f) | Possesses(p,mind_f)
all_three : Possesses(p,neutral_f) & Possesses(p,life_f) & Possesses(p,mind_f)
person_history : PossibleAcrossAttainments(one_person)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(ReportedAttainmentCount(arhatship,eleven) & PossibleAcrossAttainments(one_person) & all x.((Possesses(x,neutral_f) | Possesses(x,life_f) | Possesses(x,mind_f)) -> (Possesses(x,neutral_f) & Possesses(x,life_f) & Possesses(x,mind_f))))

# THEORY prose_exclusions
# EXPECT prose_exclusions T
all x.(FormlessBorn(x) -> all y.(SensoryFive(y) -> -Possesses(x,y)))
all x.(HigherRealmBorn(x) -> all y.((SexFaculty(y) | y = pain_f) -> -Possesses(x,y)))
all x.(OrdinaryFourthOrFormless(x) -> -Possesses(x,pleasure_f))
all x.(OrdinaryThirdFourthOrFormless(x) -> -Possesses(x,gladness_f))
all x.(DesireDispassionate(x) -> -Possesses(x,distress_f))
all x.(SeveredRoots(x) -> all y.(FaithFive(y) -> -Possesses(x,y)))

# THEORY rejected_exactly_three
# EXPECT rejected_exactly_three F
all x.all y.(Possesses(x,y) -> (y = neutral_f | y = life_f | y = mind_f))

# THEORY rejected_possession_means_current_occurrence
# EXPECT rejected_possession_means_current_occurrence F
all x.all y.(Possesses(x,y) -> OccurringNow(x,y))

# THEORY rejected_triad_entails_eye
# EXPECT rejected_triad_entails_eye F
all x.(Possesses(x,mind_f) -> Possesses(x,eye_f))
```

```nltk-valuation
arhatship => arhatship_fruit
eleven => count_eleven
one_person => attainment_person
neutral_f => neutral
life_f => life
mind_f => mind
pain_f => pain
pleasure_f => pleasure
gladness_f => gladness
distress_f => distress
eye_f => eye
ReportedAttainmentCount => {(arhatship_fruit,count_eleven)}
PossibleAcrossAttainments => {attainment_person}
Possesses => {(formless_person,neutral),(formless_person,life),(formless_person,mind),(formless_person,faith),(third_person,neutral),(third_person,life),(third_person,mind),(third_person,pleasure),(third_person,eye),(fourth_person,neutral),(fourth_person,life),(fourth_person,mind),(rootless_person,neutral),(rootless_person,life),(rootless_person,mind),(rootless_person,eye),(desire_person,neutral),(desire_person,life),(desire_person,mind),(desire_person,distress)}
OccurringNow => {(formless_person,mind),(third_person,mind),(fourth_person,mind),(rootless_person,mind),(desire_person,mind)}
SensoryFive => {eye,ear,nose,tongue,body}
SexFaculty => {female,male}
FaithFive => {faith,vigor,mindfulness,concentration,comprehension}
FormlessBorn => {formless_person}
HigherRealmBorn => {formless_person,third_person,fourth_person}
OrdinaryFourthOrFormless => {formless_person,fourth_person}
OrdinaryThirdFourthOrFormless => {formless_person,third_person,fourth_person}
DesireDispassionate => {formless_person,third_person,fourth_person}
SeveredRoots => {rootless_person}
```

The representative cases test that the triad can accompany extra Faculties and that eye-possession is not entailed. OccurringNow is an illustrative countermodel to identifying possession with occurrence, not an exhaustive psychology of these persons. The exclusion formulas preserve ordinary-person and dispassion qualifications. Damaged realization-Faculty compounds remain provisional in the paired Bhāṣya; they are not hardened into formal axioms. No fixed rule for the remainder means no additional possession follows from this triad alone, not that other rules are absent.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the verse translation): One who possesses any one of neutral feeling, life, or mind necessarily possesses the three. None of them is possessed without the others. With the remaining faculties there is no fixed rule. Possession is excluded by birth, by non-acquisition or loss, by dispassion, by severed roots, and by path-status. Where not excluded, possession stands.

The eleven is numbered in this verse and studied with 2.16's continuous attainment discussion. The second half changes the predicate.

The triad is reciprocal. Necessarily, and none without the others. The count is accompaniment, not exactly three and no more.

Pleasure and gladness name an ordinary person. The exclusion is not every person at those levels. Fourth dhyāna for pleasure. Third and fourth for gladness. Formless in both. Distress is dispassion, not realm alone. The five are severed roots, not a mood.

The realization-faculty exclusions are provisional where the compounds are damaged. Lacking the knowledge-faculty is not lacking all knowledge. Established in fruits is not a bar on every later path-relation.

Interpretation: one possession entails two others. The look-ahead on non-reflective is not this cut. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_17
    a vak:Karika ;
    rdfs:label "VAK 2.17" ;
    vak:hasTopic vak:NecessaryTriad ;
    vak:belongsTo vak:Indriyanirdesa .

vak:NeutralFeeling vak:entailsPossession vak:Life, vak:Mind .
vak:Remainder vak:fixedRule false .

vak:Life vak:entailsPossession vak:NeutralFeeling, vak:Mind .
vak:Mind vak:entailsPossession vak:NeutralFeeling, vak:Life .

organon:VAK_2_17_Interpretation
    organon:distinguishes vak:Possession, vak:CurrentOccurrence,
        vak:RepeatedAttainment .
```
