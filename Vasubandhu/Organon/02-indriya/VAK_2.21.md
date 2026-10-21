# VAK_2.21 — The Greatest Number

## 1. Sanskrit (Devanāgarī)

```sanskrit
बहुभिर्युक्त एकान्नविंशत्यामलवर्जितैः ।
द्विलिङ्ग आर्यो रागी एकलिङ्गद्वयामलवर्जितैः ॥ २.२१ ॥
```

## 2. Sanskrit (IAST)

```text
bahubhir yukta ekānnaviṃśatyāmalavarjitaiḥ /
dviliṅga āryo rāgī ekaliṅgadvayāmalavarjitaiḥ // 2.21 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| bahubhiḥ | instrumental plural adjective | with the greatest number [of Faculties], as the prose question specifies |
| yuktaḥ | nominative singular masculine past passive participle | endowed; possession, not simultaneous manifestation |
| ekānna-viṃśatyā | instrumental singular numeral | with nineteen, one short of twenty |
| amala-varjitaiḥ | instrumental plural adjective | with [Faculties] excluding the stainless three |
| dvi-liṅgaḥ | nominative singular masculine possessive compound | possessing both sex Faculties; first subject, qualified as complete in the prose |
| āryaḥ | nominative singular masculine noun | noble person; second subject, glossed as trainee |
| rāgī | nominative singular masculine adjective from rāgin | still with attachment, not free from attachment |
| eka-liṅga-dvaya-amala-varjitaiḥ | instrumental plural compound adjective | with [Faculties] excluding one sex Faculty and two stainless Faculties |

The running witness has a short vowel in the final compound; the
study's long-vowel reading is editorial. The prose resolves two
uncontaminated Faculties. External sandhi is opened for parsing.

```text
# tokens: bahubhiḥ yuktaḥ ekānnaviṃśatyā amala-varjitaiḥ dviliṅgaḥ āryaḥ rāgī eka-liṅga-dvaya-amala-varjitaiḥ
```

## 4. Grammar

The first subject follows its instrumental predicates. The prose's
“who else?” separates the noble trainee from the person possessing
both sex Faculties. The second clause inherits the numeral through
shared `CNT` and `COUNTSEM` features; it does not carry both-sex
status or exclusion of all three stainless Faculties. Completeness and trainee status are
Bhāṣya qualifications, not additional words in the verse.

```nltk-fcfg
% start S
# tokens: bahubhiḥ yuktaḥ ekānnaviṃśatyā amala-varjitaiḥ dviliṅgaḥ āryaḥ rāgī eka-liṅga-dvaya-amala-varjitaiḥ
S[SEM=<(?first & ?second)>] -> FIRST[CNT=?n,COUNTSEM=?count,SEM=?first] SECOND[CNT=?n,COUNTSEM=?count,SEM=?second]
FIRST[CNT=19,COUNTSEM=?count,SEM=<(MaximumCount(?person,?count) & ?exclude(?person) & BothSexes(?person))>] -> MOST[CASE=ins] ENDOWED[CASE=nom,GEN=m] NINETEEN[CASE=ins,CNT=19,SEM=?count] FIRSTEXCLUSION[CASE=ins,STAINLESS=3,SEM=?exclude] BOTH[CASE=nom,GEN=m,SEM=?person]
SECOND[CNT=19,COUNTSEM=?count,SEM=<(MaximumCount(learner,?count) & Noble(learner) & ?attached(learner) & ?exclude(learner))>] -> NOBLE[CASE=nom,GEN=m,SUBJECT=second] ATTACHED[CASE=nom,GEN=m,SEM=?attached] SECONDEXCLUSION[CASE=ins,SEX=1,STAINLESS=2,SEM=?exclude]
MOST[CASE=ins] -> 'bahubhiḥ'
ENDOWED[CASE=nom,GEN=m] -> 'yuktaḥ'
NINETEEN[CASE=ins,CNT=19,SEM=<nineteen>] -> 'ekānnaviṃśatyā'
FIRSTEXCLUSION[CASE=ins,STAINLESS=3,SEM=<\c.ExcludesThreeStainless(c)>] -> 'amala-varjitaiḥ'
BOTH[CASE=nom,GEN=m,SEM=<both_sexes>] -> 'dviliṅgaḥ'
NOBLE[CASE=nom,GEN=m,SUBJECT=second] -> 'āryaḥ'
ATTACHED[CASE=nom,GEN=m,SEM=<\c.StillAttached(c)>] -> 'rāgī'
SECONDEXCLUSION[CASE=ins,SEX=1,STAINLESS=2,SEM=<\c.ExcludesOneSexTwoStainless(c)>] -> 'eka-liṅga-dvaya-amala-varjitaiḥ'
```

```nltk-dep
'yuktaḥ' -> 'bahubhiḥ' | 'ekānnaviṃśatyā' | 'amala-varjitaiḥ' | 'dviliṅgaḥ' | 'āryaḥ'
'āryaḥ' -> 'rāgī' | 'eka-liṅga-dvaya-amala-varjitaiḥ'
```

The link from endowment to the second subject marks ellipsis; it does
not make the two subjects one person. The dependency audit checks
token coverage, not a full syntactic derivation.

| Span | Constituent | Result |
|---|---|---|
| [0, 5) | `FIRST` | nineteen, both sex Faculties, all three stainless excluded |
| [5, 8) | `SECOND` | nineteen carried, noble still attached, one sex and two stainless excluded |
| [0, 8) | `S` | two subjects and two exclusion patterns |

## 5. Translation

### Literal Translation

> Endowed with the greatest number, nineteen, excluding the stainless: one
> possessing both sex faculties. A noble person still possessing attachment,
> excluding one sex faculty and two stainless faculties.

### Bhāṣya-informed study translation

> A person possessing both sex Faculties, with Faculties complete,
> possesses the greatest number, nineteen, excluding the three stainless
> Faculties. A noble trainee still with attachment likewise possesses
> nineteen, excluding one sex Faculty and two stainless Faculties:
> the Faculty of one who has known and either of the other two.

## 6. Philosophical Translation

> The maximum count does not measure completion of realization.
> One nineteen includes both sex Faculties and no realization-Faculty;
> the trainee's nineteen includes one sex Faculty and one
> realization-Faculty. Equal totals preserve different qualifications.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| bahubhiḥ | the greatest number | nineteen |
| amala | stainless | the three; not every wholesome |
| dvi-liṅga | both sex faculties | dvivyañjana; the first case |
| samagra-indriya | complete in faculties | relative to the nineteen |
| ārya rāgin | noble, still with attachment | avītarāga śaikṣa |
| dvayoś cānyatarat | and either of the other two | with one who has known; two exclusions |

## 8. Logical Determination

**Kārikā, derived.** The SEM distinguishes the two subjects and their
exclusion patterns while deriving both counts from the one numeral.
The following finite inventories expand the Bhāṣya: the complete first case, and two alternative trainee cases.
The trainee alternatives are not a joint possession of both remaining
realization-Faculties.

```nltk-sem
first_exclusion : \c.ExcludesThreeStainless(c)
attachment : \c.StillAttached(c)
second_exclusion : \c.ExcludesOneSexTwoStainless(c)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(MaximumCount(both_sexes,nineteen) & ExcludesThreeStainless(both_sexes) & BothSexes(both_sexes) & MaximumCount(learner,nineteen) & Noble(learner) & StillAttached(learner) & ExcludesOneSexTwoStainless(learner))

# THEORY prose_inventories
# EXPECT prose_inventories T
CompleteFaculties(both_sexes) & Trainee(learner)
all x.(WorldlyMember(x) <-> (Faculty(x) & -Stainless(x)))
all x.(ProspectiveMember(x) <-> (Faculty(x) & -(x = female_f) & -(x = known_f) & -(x = knowledge_f)))
all x.(KnowledgeMember(x) <-> (Faculty(x) & -(x = male_f) & -(x = known_f) & -(x = prospective_f)))
all x.(Stainless(x) <-> (x = prospective_f | x = knowledge_f | x = known_f))

# THEORY rejected_equal_count_equal_members
# EXPECT rejected_equal_count_equal_members F
all x.(WorldlyMember(x) <-> ProspectiveMember(x))

# THEORY rejected_complete_means_all_twenty_two
# EXPECT rejected_complete_means_all_twenty_two F
all x.(Faculty(x) -> WorldlyMember(x))

# THEORY rejected_trainee_has_completed_faculty
# EXPECT rejected_trainee_has_completed_faculty F
ProspectiveMember(known_f) | KnowledgeMember(known_f)

# THEORY rejected_trainee_combines_other_two
# EXPECT rejected_trainee_combines_other_two F
ProspectiveMember(prospective_f) & ProspectiveMember(knowledge_f)
```

```nltk-valuation
both_sexes => complete_both_sexes
learner => attached_trainee
nineteen => count_nineteen
female_f => female
male_f => male
prospective_f => shall_know
knowledge_f => knowledge
known_f => one_who_has_known
MaximumCount => {(complete_both_sexes,count_nineteen),(attached_trainee,count_nineteen)}
ExcludesThreeStainless => {complete_both_sexes}
BothSexes => {complete_both_sexes}
Noble => {attached_trainee}
StillAttached => {attached_trainee}
ExcludesOneSexTwoStainless => {attached_trainee}
CompleteFaculties => {complete_both_sexes}
Trainee => {attached_trainee}
Faculty => {eye,ear,nose,tongue,body,female,male,life,mind,pain,pleasure,gladness,distress,neutral,faith,vigor,mindfulness,concentration,comprehension,shall_know,knowledge,one_who_has_known}
Stainless => {shall_know,knowledge,one_who_has_known}
WorldlyMember => {eye,ear,nose,tongue,body,female,male,life,mind,pain,pleasure,gladness,distress,neutral,faith,vigor,mindfulness,concentration,comprehension}
ProspectiveMember => {eye,ear,nose,tongue,body,male,life,mind,pain,pleasure,gladness,distress,neutral,faith,vigor,mindfulness,concentration,comprehension,shall_know}
KnowledgeMember => {eye,ear,nose,tongue,body,female,life,mind,pain,pleasure,gladness,distress,neutral,faith,vigor,mindfulness,concentration,comprehension,knowledge}
```

Each inventory has nineteen actual members out of twenty-two.
The trainee examples choose opposite sex Faculties to display the
one-sex exclusion; neither realization alternative is tied to that
choice. Either sex can be retained in either alternative. The first
nineteen and each trainee nineteen share eighteen members.
`MaximumCount` is a label checked against these inventories, not
a proof that no unmodeled configuration exceeds nineteen.

The source's maximum question is not a universal assertion that every
trainee, including one lacking other Faculties, possesses nineteen.
Nor does possession assert simultaneous occurrence or greater strength.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): The greatest number is nineteen. One possessing both
sex faculties is endowed with nineteen, excluding the stainless triad. A
trainee still possessing attachment is also endowed with nineteen,
excluding one sex faculty and two of the stainless. The maximum is not the
full twenty-two. It is the complete ordinary or still-attached noble
continuum.

The first case reaches nineteen by retaining all Faculties other than
the realization triad, not by that absence alone. Both sex characteristics
do not by themselves supply the nineteen. Complete is the qualification.

The trainee exclusions are compatibility with a stage, not a deficit measured against the worldly case. Continuing attachment is kept. Noble is not the end of training. Possession is not nineteen faculties in one moment, and not a measure of strength.

Dviliṅga does not join ārya. Who else introduces the second subject. Stainless is uncontaminated, all three in the first case, two named in the second. The conjunction is one who has known and either of the other two, not either completed knowledge or one other.

The Bhāṣya closes the Faculty differentiation introduced through the
Principles; it does not close the chapter. In the Organon reading,
Cognition governs Perception and Conception without collapsing into
Mind or consciousness. A count of possessed Faculties is not itself
an account of that governing operation.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_21
    a vak:Karika ;
    rdfs:label "VAK 2.21" ;
    vak:hasTopic vak:MaximumPossession ;
    vak:belongsTo vak:Indriyanirdesa .

vak:WorldlyMaximum vak:hasCount 19 ;
    vak:excludes vak:ThreeStainless .
vak:TraineeMaximum vak:hasCount 19 ;
    vak:hasStainlessCount 1 .

organon:VAK_2_21_Interpretation
    organon:distinguishes vak:MaximumPossession, vak:FacultyMembership,
        vak:RealizationStatus .
```
