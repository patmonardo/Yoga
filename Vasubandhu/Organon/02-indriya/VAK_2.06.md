# VAK_2.06 — Engagement and Withdrawal

## 1. Sanskrit (Devanāgarī)

```sanskrit
प्रवृत्तेराश्रयोत्पत्तिस्थितिप्रत्युपभोगतः ।
चतुर्दश तथान्यानि निवृत्तेरिन्द्रियाणि वा ॥ २.६ ॥
```

## 2. Sanskrit (IAST)

```text
pravṛtter āśrayotpattisthitipratyupabhogataḥ /
caturdaśa tathānyāni nivṛtter indriyāṇi vā // 2.6 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| pravṛtteḥ | genitive singular | of engagement |
| āśraya-utpatti-sthiti-pratyupabhogataḥ | ablative singular compound, adverbial | with respect to Basis, arising, persistence, and experience |
| caturdaśa | nominative neuter plural | fourteen [Faculties] |
| tathā | indeclinable | likewise |
| anyāni | nominative neuter plural | the others, distinct from the fourteen |
| nivṛtteḥ | genitive singular | of withdrawal |
| indriyāṇi | nominative neuter plural | Faculties |
| vā | particle | or; marks the alternative opinion |

*Pravṛtti* qualifies all four functions. *Tathā* carries the same fourfold
pattern to *nivṛtti*. The Bhāṣya supplies the eight-member remainder and
identifies the members of each function.

**Grammar tokens.** External sandhi is opened; the four-member ablative
compound remains one token with its internal order represented in SEM.
The eight members are supplied by the Bhāṣya, not inserted into the
verse's token stream.

```text
# tokens: pravṛtteḥ āśraya-utpatti-sthiti-pratyupabhogataḥ caturdaśa tathā anyāni nivṛtteḥ indriyāṇi vā
```

## 4. Grammar

The genitives assign the two courses. The ablative compound supplies
four ordered functional places for engagement, and *tathā* applies
that same pattern to withdrawal. *Anyāni* distinguishes the second
group; *vā* marks the whole arrangement as another opinion. The verse
speaks fourteen and “the others,” while the Bhāṣya determines the
latter as eight. The grammar records the two groups without silently
putting the numeral eight into the Sanskrit.

```nltk-fcfg
% start S
# tokens: pravṛtteḥ āśraya-utpatti-sthiti-pratyupabhogataḥ caturdaśa tathā anyāni nivṛtteḥ indriyāṇi vā
S[SEM=<(?roles(?eng) & ?count(?eng) & ?same(?roles)(?withdraw) & ?other(?withdraw)(?eng) & ?fac(?eng)(?withdraw) & ?alt)>] -> ENG[CASE=gen,SEM=?eng] ROLES[CASE=abl,SEM=?roles] FOURTEEN[CASE=nom,NUM=pl,GEN=n,CNT=14,SEM=?count] SAME[SEM=?same] OTHER[CASE=nom,NUM=pl,GEN=n,SEM=?other] WITHDRAW[CASE=gen,SEM=?withdraw] FACULTIES[CASE=nom,NUM=pl,GEN=n,SEM=?fac] OR[ALT=opinion,SEM=?alt]
ENG[CASE=gen,SEM=<engagement>] -> 'pravṛtteḥ'
ROLES[CASE=abl,SEM=<\c.(BasisSlot(c) & ArisingSlot(c) & PersistenceSlot(c) & ExperienceSlot(c))>] -> 'āśraya-utpatti-sthiti-pratyupabhogataḥ'
FOURTEEN[CASE=nom,NUM=pl,GEN=n,CNT=14,SEM=<\c.GroupCount(c,fourteen)>] -> 'caturdaśa'
SAME[SEM=<\R.\c.R(c)>] -> 'tathā'
OTHER[CASE=nom,NUM=pl,GEN=n,SEM=<\c.\e.OtherGroup(c,e)>] -> 'anyāni'
WITHDRAW[CASE=gen,SEM=<withdrawal>] -> 'nivṛtteḥ'
FACULTIES[CASE=nom,NUM=pl,GEN=n,SEM=<\e.\w.(FacultyGroup(e) & FacultyGroup(w))>] -> 'indriyāṇi'
OR[ALT=opinion,SEM=<AlternativeOpinion>] -> 'vā'
```

```nltk-dep
'indriyāṇi' -> 'pravṛtteḥ' | 'āśraya-utpatti-sthiti-pratyupabhogataḥ' | 'caturdaśa' | 'tathā' | 'anyāni' | 'nivṛtteḥ' | 'vā'
```

**Feature chart checkpoints.** The eight-token parse retains the
genitive course distinction, the ablative role compound, the
fourteen-count feature, and the alternative-opinion marker.

| Span | Constituent | Result |
|---|---|---|
| [0, 1) | `ENG` | engagement course |
| [1, 2) | `ROLES` | four ordered functional places |
| [2, 3) | `FOURTEEN` | fourteen-member first group |
| [3, 4) | `SAME` | transfer of the four places |
| [4, 6) | `OTHER WITHDRAW` | distinct withdrawal group |
| [0, 8) | `S` | two course assignments under an alternative opinion |

## 5. Translation

### Literal Translation

> Or, as to Basis, arising, persistence, and experience of engagement,
> fourteen; likewise the others are faculties of withdrawal.

### Bhāṣya-informed study translation

> Or, for engagement, fourteen [Faculties] with respect to Basis, arising,
> persistence, and experience; likewise, the others are Faculties of
> withdrawal.

## 6. Philosophical Translation

> Engagement and withdrawal are two courses of the same rules. The alternative does not replace the first account.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| pravṛtti | engagement | the fourteen; not “the world” |
| nivṛtti | withdrawal | the eight; not bare inactivity |
| āśraya | Basis | six for engagement; five beginning with faith for withdrawal; not *ālambana* |
| utpatti / prabhava | arising | female and male; or I shall know |
| sthiti | persistence | life; or the knowledge-faculty |
| pratyupabhoga / upabhoga | experience | the feelings; or one who has known |
| vā / matavikalpa | or | difference of opinion |
| śikṣā-viśeṣa | particular training | why speech is refused |

## 8. Logical Determination

**Kārikā, derived.** The SEM applies the four places first to
engagement and then, through *tathā*, to withdrawal. It asserts the
fourteen-member first group, the distinct other group, and the
alternative-opinion marker. The Bhāṣya supplies the second group's
eight members and the concrete distribution below; those are prose
premises, not a hidden numeral in the verse parse. `BasisSlot` and
`BasisFor` express *āśraya*, not *ālambana*.

```nltk-sem
four_places : \c.(BasisSlot(c) & ArisingSlot(c) & PersistenceSlot(c) & ExperienceSlot(c))
same_four : \R.\c.R(c)
fourteen_group : \c.GroupCount(c,fourteen)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(BasisSlot(engagement) & ArisingSlot(engagement) & PersistenceSlot(engagement) & ExperienceSlot(engagement) & GroupCount(engagement,fourteen) & BasisSlot(withdrawal) & ArisingSlot(withdrawal) & PersistenceSlot(withdrawal) & ExperienceSlot(withdrawal) & OtherGroup(withdrawal,engagement) & FacultyGroup(engagement) & FacultyGroup(withdrawal) & AlternativeOpinion)

# THEORY prose_distribution
# EXPECT prose_distribution T
(GroupCount(withdrawal,eight) & FacultyGroup(withdrawal))
all x.(EngagementFaculty(x) -> (BasisFor(x,engagement) | ArisingFor(x,engagement) | PersistsFor(x,engagement) | ExperiencesFor(x,engagement)))
all x.((BasisFor(x,engagement) | ArisingFor(x,engagement) | PersistsFor(x,engagement) | ExperiencesFor(x,engagement)) -> EngagementFaculty(x))
all x.(WithdrawalFaculty(x) -> (BasisFor(x,withdrawal) | ArisingFor(x,withdrawal) | PersistsFor(x,withdrawal) | ExperiencesFor(x,withdrawal)))
all x.((BasisFor(x,withdrawal) | ArisingFor(x,withdrawal) | PersistsFor(x,withdrawal) | ExperiencesFor(x,withdrawal)) -> WithdrawalFaculty(x))
all x.(EngagementFaculty(x) -> -WithdrawalFaculty(x))
all x.(FacultyHere(x) -> (EngagementFaculty(x) | WithdrawalFaculty(x)))
all x.((EngagementFaculty(x) | WithdrawalFaculty(x)) -> FacultyHere(x))
(NeedsTraining(speech) & ActWithoutMember(taking,hand) & PleasureDueTo(genital_pleasure,female_f))

# THEORY rejected_all_causes_are_faculties
# EXPECT rejected_all_causes_are_faculties F
all x.((exists y.Causes(x,y)) -> FacultyHere(x))

# THEORY rejected_withdrawal_is_absence
# EXPECT rejected_withdrawal_is_absence F
all x.(WithdrawalFaculty(x) -> -FacultyHere(x))

# THEORY rejected_same_group
# EXPECT rejected_same_group F
all x.(EngagementFaculty(x) -> WithdrawalFaculty(x))
```

```nltk-valuation
engagement => engagement_course
withdrawal => withdrawal_course
fourteen => fourteen_members
eight => eight_members
speech => speech_power
taking => taking_act
hand => hand_power
genital_pleasure => genital_pleasure_event
female_f => female_faculty
BasisSlot => {engagement_course,withdrawal_course}
ArisingSlot => {engagement_course,withdrawal_course}
PersistenceSlot => {engagement_course,withdrawal_course}
ExperienceSlot => {engagement_course,withdrawal_course}
GroupCount => {(engagement_course,fourteen_members),(withdrawal_course,eight_members)}
OtherGroup => {(withdrawal_course,engagement_course)}
FacultyGroup => {engagement_course,withdrawal_course}
AlternativeOpinion => {()}
BasisFor => {(eye,engagement_course),(ear,engagement_course),(nose,engagement_course),(tongue,engagement_course),(body,engagement_course),(mind,engagement_course),(faith,withdrawal_course),(vigor,withdrawal_course),(mindfulness,withdrawal_course),(concentration,withdrawal_course),(comprehension,withdrawal_course)}
ArisingFor => {(female_faculty,engagement_course),(male_faculty,engagement_course),(shall_know,withdrawal_course)}
PersistsFor => {(life,engagement_course),(knowledge,withdrawal_course)}
ExperiencesFor => {(pleasure,engagement_course),(pain,engagement_course),(gladness,engagement_course),(distress,engagement_course),(equanimity,engagement_course),(has_known,withdrawal_course)}
EngagementFaculty => {eye,ear,nose,tongue,body,mind,female_faculty,male_faculty,life,pleasure,pain,gladness,distress,equanimity}
WithdrawalFaculty => {faith,vigor,mindfulness,concentration,comprehension,shall_know,knowledge,has_known}
FacultyHere => {eye,ear,nose,tongue,body,mind,female_faculty,male_faculty,life,pleasure,pain,gladness,distress,equanimity,faith,vigor,mindfulness,concentration,comprehension,shall_know,knowledge,has_known}
NeedsTraining => {speech_power}
ActWithoutMember => {(taking_act,hand_power)}
PleasureDueTo => {(genital_pleasure_event,female_faculty)}
Causes => {(speech_power,speaking_act),(hand_power,taking_act),(foot_power,moving_act),(anus_power,excretion_act),(genital_power,genital_pleasure_event)}
```

The finite witness has 6 + 2 + 1 + 5 engagement Faculties and
5 + 1 + 1 + 1 withdrawal Faculties. The model tests the reported
distribution and its exclusions; it does not prove the Bhāṣya's
empirical examples or turn every causal contributor into a Faculty.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): Or the same twenty-two under another order. Fourteen
govern engagement through Basis, arising, persistence, and experience.
Eight govern withdrawal in those same four places. Withdrawal is not bare
absence; it has its own Basis, arising, persistence, and experience.

Tathā is the point. Withdrawal has the same four places as engagement. The members differ. Feeling-experience is not the experience of one who has known. They occupy the corresponding place.

The order is explained by the functions, not only received. Arising from female and male is not a full account of generation. Life is continued standing. The five form the Basis of withdrawal. The three split into arising, persistence, and experience, as 2.04 had already distinguished them.

Speech depends on training. That does not mean no cultivated faculty counts: the eight are in this same unit. Hand and foot are not different from the act, and the act occurs without them. Excretion is heavy matter and wind. Pleasure of the genital organ is already assigned to female and male. The last step is the threat: every cause would be a faculty of its own act.

Interpretation: the array is what we subject ourselves to. The principles remain the membership discriminator. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_06
    a vak:Karika ;
    rdfs:label "VAK 2.06" ;
    vak:hasTopic vak:EngagementAndWithdrawal ;
    vak:belongsTo vak:Indriyanirdesa ;
    vak:reportsPosition vak:AlternativeOpinion .

vak:Engagement vak:hasCount 14 ;
    vak:hasBasis vak:SixFaculties ;
    vak:hasArising vak:FemaleMaleFaculties ;
    vak:hasPersistence vak:LifeFaculty ;
    vak:hasExperience vak:FeelingFive .
vak:Withdrawal vak:hasCount 8 ;
    vak:hasBasis vak:FiveBeginningWithFaith ;
    vak:hasArising vak:IShallKnow ;
    vak:hasPersistence vak:KnowledgeFaculty ;
    vak:hasExperience vak:OneWhoHasKnown .

organon:IndriyaArray
    organon:subjectedTo true ;
    organon:notTheVerseEnglish true .
```
