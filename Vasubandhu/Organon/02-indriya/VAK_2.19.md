# VAK_2.19 — Realization and What It Entails

## 1. Sanskrit (Devanāgarī)

```sanskrit
अष्टाभिरेकादशभिस्त्वाज्ञाज्ञातेन्द्रियान्वितः ।
आज्ञास्यामीन्द्रियोपेतस्त्रयोदशभिरन्वितः ॥ २.१९ ॥
```

## 2. Sanskrit (IAST)

```text
aṣṭābhir ekādaśabhis tv ājñājñātendriyānvitaḥ /
ājñāsyāmīndriyopetas trayodaśabhir anvitaḥ // 2.19 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| aṣṭābhiḥ | instrumental plural numeral | with eight; completes 2.18's final subject |
| ekādaśabhiḥ | instrumental plural numeral | with eleven [Faculties] |
| tu | contrastive particle | however |
| ājñā-ājñāta-indriya-anvitaḥ | nominative singular masculine compound | possessor of the knowledge-Faculty or the Faculty of one who has known; separate cases in the prose |
| ājñāsyāmi-indriya-upetaḥ | nominative singular masculine compound | one possessing the Faculty “I shall know” |
| trayodaśabhiḥ | instrumental plural numeral | with thirteen [Faculties] |
| anvitaḥ | nominative singular masculine past passive participle | endowed; necessarily possessing under the ongoing question |

The gloss at 51.17 is difficult. The two cases are distinguished by
the explicit ājñendriyeṇa and ājñātāvīndriyeṇa in the following prose.
This does not settle every occurrence of the damaged ājñātendriya.

**Grammar tokens.** External sandhi is opened; the possessor compounds
remain intact. Eight completes the previous subject.

```text
# tokens: aṣṭābhiḥ ekādaśabhiḥ tu ājñā-ājñāta-indriya-anvitaḥ ājñāsyāmi-indriya-upetaḥ trayodaśabhiḥ anvitaḥ
```

## 4. Grammar

Eleven distributes over two separate possessors. Thirteen predicates
endowment of the prospective Faculty's possessor. The Bhāṣya supplies
the lists, not a claim of simultaneous operation or a restriction
of the whole thirteen to the uninterrupted Path.

```nltk-fcfg
% start S
# tokens: aṣṭābhiḥ ekādaśabhiḥ tu ājñā-ājñāta-indriya-anvitaḥ ājñāsyāmi-indriya-upetaḥ trayodaśabhiḥ anvitaḥ
S[SEM=<(?carry & ?eleven & ?thirteen)>] -> CARRY[CONTINUED=previous_subject,SEM=?carry] ELEVENCLAUSE[SEM=?eleven] THIRTEENCLAUSE[SEM=?thirteen]
ELEVENCLAUSE[SEM=<(NecessaryCount(knowledge_f,?count) & NecessaryCount(has_known_f,?count))>] -> ELEVEN[CASE=ins,CNT=11,SEM=?count] BUT TWOCASES[CASE=nom,NUM=sg,GEN=m,READING=alternative]
THIRTEENCLAUSE[SEM=<NecessaryCount(?given,?count)>] -> PROSPECTIVE[CASE=nom,NUM=sg,GEN=m,SEM=?given] THIRTEEN[CASE=ins,CNT=13,SEM=?count] ENDOWED[CASE=nom,NUM=sg,GEN=m]
CARRY[CONTINUED=previous_subject,SEM=<PreviousSubjectCount(eight)>] -> 'aṣṭābhiḥ'
ELEVEN[CASE=ins,CNT=11,SEM=<eleven>] -> 'ekādaśabhiḥ'
BUT -> 'tu'
TWOCASES[CASE=nom,NUM=sg,GEN=m,READING=alternative] -> 'ājñā-ājñāta-indriya-anvitaḥ'
PROSPECTIVE[CASE=nom,NUM=sg,GEN=m,SEM=<shall_know_f>] -> 'ājñāsyāmi-indriya-upetaḥ'
THIRTEEN[CASE=ins,CNT=13,SEM=<thirteen>] -> 'trayodaśabhiḥ'
ENDOWED[CASE=nom,NUM=sg,GEN=m] -> 'anvitaḥ'
```

```nltk-dep
'ājñā-ājñāta-indriya-anvitaḥ' -> 'ekādaśabhiḥ' | 'tu'
'anvitaḥ' -> 'ājñāsyāmi-indriya-upetaḥ' | 'trayodaśabhiḥ' | 'aṣṭābhiḥ'
```

The dependency block checks vocabulary coverage, not parsing. The opening
eight has its subject in 2.18, not in the thirteen-clause.

| Span | Constituent | Result |
|---|---|---|
| [0, 1) | `CARRY` | eight completes the previous subject |
| [1, 4) | `ELEVENCLAUSE` | separate eleven-counts |
| [4, 7) | `THIRTEENCLAUSE` | thirteen for “I shall know” |
| [0, 7) | `S` | carried count and realization possession |

## 5. Translation

### Literal Translation

> With eight. But one accompanied by the knowledge-faculty or the faculty of
> one who has known, with eleven. One furnished with the faculty “I shall
> know” is accompanied by thirteen.

### Bhāṣya-informed study translation

> With eight. One possessing the knowledge-Faculty or the Faculty of
> one who has known, however, necessarily possesses eleven Faculties
> in either case. One possessing the “I shall know” Faculty necessarily
> possesses thirteen.

## 6. Philosophical Translation

> The necessary possession sets differ without ranking realization by
> their size. Eleven and thirteen describe guaranteed companions,
> not the constituents of a single Path-moment.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| ājñendriya | knowledge-faculty | eleven |
| ājñātāvīndriya | one who has known | eleven; another set |
| ājñāsyāmīndriya | I shall know | thirteen |
| śraddhādi | the five | all five, not faith alone |
| tair eva daśabhiḥ | those same ten | carries the common members |
| samanvāgata | possessing | not one path-moment |

## 8. Logical Determination

**Kārikā, derived.** Eight is the carried count. Eleven distributes over
two cases, and thirteen over the third. The damaged introductory gloss
is not formalized as a separate identity.

```nltk-sem
necessary_count : \f.\n.NecessaryCount(f,n)
continued_eight : PreviousSubjectCount(eight)
prospective_count : NecessaryCount(shall_know_f,thirteen)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(PreviousSubjectCount(eight) & NecessaryCount(knowledge_f,eleven) & NecessaryCount(has_known_f,eleven) & NecessaryCount(shall_know_f,thirteen))

# THEORY prose_sets
# EXPECT prose_sets T
all x.(Requires(knowledge_f,x) <-> (CommonTen(x) | x = knowledge_f))
all x.(Requires(has_known_f,x) <-> (CommonTen(x) | x = has_known_f))
all x.(Requires(shall_know_f,x) <-> (CommonTen(x) | x = body_f | x = pain_f | x = shall_know_f))
all x.all y.all z.((Possesses(x,y) & Requires(y,z)) -> Possesses(x,z))

# THEORY rejected_same_eleven_set
# EXPECT rejected_same_eleven_set F
all x.(Requires(knowledge_f,x) <-> Requires(has_known_f,x))

# THEORY rejected_thirteen_is_current_operation
# EXPECT rejected_thirteen_is_current_operation F
all x.all y.((Possesses(x,shall_know_f) & Requires(shall_know_f,y)) -> OccurringNow(x,y))

# THEORY rejected_omitted_means_not_possessed
# EXPECT rejected_omitted_means_not_possessed F
all x.(Possesses(x,knowledge_f) -> -Possesses(x,body_f))
```

```nltk-valuation
eight => count_eight
eleven => count_eleven
thirteen => count_thirteen
knowledge_f => knowledge
has_known_f => one_who_has_known
shall_know_f => shall_know
body_f => body
pain_f => pain
PreviousSubjectCount => {count_eight}
NecessaryCount => {(knowledge,count_eleven),(one_who_has_known,count_eleven),(shall_know,count_thirteen)}
CommonTen => {pleasure,gladness,neutral,life,mind,faith,vigor,mindfulness,concentration,comprehension}
Requires => {(knowledge,pleasure),(knowledge,gladness),(knowledge,neutral),(knowledge,life),(knowledge,mind),(knowledge,faith),(knowledge,vigor),(knowledge,mindfulness),(knowledge,concentration),(knowledge,comprehension),(knowledge,knowledge),(one_who_has_known,pleasure),(one_who_has_known,gladness),(one_who_has_known,neutral),(one_who_has_known,life),(one_who_has_known,mind),(one_who_has_known,faith),(one_who_has_known,vigor),(one_who_has_known,mindfulness),(one_who_has_known,concentration),(one_who_has_known,comprehension),(one_who_has_known,one_who_has_known),(shall_know,pleasure),(shall_know,gladness),(shall_know,neutral),(shall_know,life),(shall_know,mind),(shall_know,faith),(shall_know,vigor),(shall_know,mindfulness),(shall_know,concentration),(shall_know,comprehension),(shall_know,body),(shall_know,pain),(shall_know,shall_know)}
Possesses => {(knowledge_person,pleasure),(knowledge_person,gladness),(knowledge_person,neutral),(knowledge_person,life),(knowledge_person,mind),(knowledge_person,faith),(knowledge_person,vigor),(knowledge_person,mindfulness),(knowledge_person,concentration),(knowledge_person,comprehension),(knowledge_person,knowledge),(knowledge_person,body),(prospective_person,pleasure),(prospective_person,gladness),(prospective_person,neutral),(prospective_person,life),(prospective_person,mind),(prospective_person,faith),(prospective_person,vigor),(prospective_person,mindfulness),(prospective_person,concentration),(prospective_person,comprehension),(prospective_person,body),(prospective_person,pain),(prospective_person,shall_know)}
OccurringNow => {(prospective_person,shall_know)}
```

The elevens share ten and differ in the given realization Faculty.
Thirteen contains the common ten, body, pain, and its own realization
Faculty. These are possession implications, not exclusive totals.
The knowledge-person's extra Body-Faculty illustrates that omission
from a necessary list does not entail absence; it is not a biography
established by this passage. `OccurringNow` is likewise an illustrative
countermodel, not a full Path psychology.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): The knowledge-faculty and the faculty of one who has
known each require eleven. “I shall know” requires thirteen. The
difference is not further realization. Its possession list includes
body and pain; the passage does not explain their necessity by
assigning the whole list to one Path-moment.

The eight stands in 2.18. Pratyekam still holds: female, male, distress, and each of the five are separate eights.

The damaged gloss is kept. The contrast is carried by ājñendriyeṇa and ājñātāvīndriyeṇa. The resolution is marked, not a silent repair.

Pain in the thirteen is not a constituent of the seeing-path moment. The predicate is possession. Why body and pain are necessary here and absent from the common ten is not explained. No cause is inserted.

Interpretation: the named faculty, its path-role, and the exact list. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_19
    a vak:Karika ;
    rdfs:label "VAK 2.19" ;
    vak:hasTopic vak:RealizationClosure ;
    vak:belongsTo vak:Indriyanirdesa .

vak:KnowledgeFaculty vak:closesOn 11 .
vak:OneWhoHasKnown vak:closesOn 11 .
vak:IShallKnow vak:closesOn 13 .

organon:VAK_2_19_Interpretation
    organon:distinguishes vak:NecessaryPossession,
        vak:CurrentOperation, vak:RealizationDegree .
```
