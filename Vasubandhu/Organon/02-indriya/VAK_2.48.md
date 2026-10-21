# VAK_2.48 — Result-Sort

## 1. Sanskrit (Devanāgarī)

```sanskrit
सभागता सा तु पुनर्विपाकोऽप्याप्तयो द्विधा ।
लक्षणानि च निःष्यन्दाः समापत्त्यसमन्वयाः ॥ २.४८ ॥
```

## 2. Sanskrit (IAST)

```text
sabhāgatā sā tu punar vipāko 'py āptayo dvidhā /
lakṣaṇāni ca niḥṣyandāḥ samāpatty-asamanvayāḥ // 2.48 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sabhāgatā | nom. sg. f. | same-class |
| sā tu punaḥ | nom. sg. f. + particles | that same-class, however, additionally; resumes the preceding classifications |
| vipākaḥ api | nom. sg. m. + particle | also maturation |
| āptayaḥ dvidhā | nom. pl. f. + adverb | acquisitions, twofold by result-sort; not a dual of acquisitions |
| lakṣaṇāni ca | nom. pl. n. + particle | and the marks; twofold is carried forward |
| niḥṣyandāḥ | nom. pl. m. | homogeneous outflows |
| samāpatti-asamanvayāḥ | nom. pl. m.; coordinative compound | the two attainments and non-acquisition; the masculine final member governs agreement |

The opening completes the “likewise” at the end of 2.47. The
Bhāṣya carries sentient classification, homogeneous outflow, and
unobscured-indeterminate status forward, not the Desire/Form limit.
The normalized tokens separate external sandhi; the final compound
remains one token and has three referents.

```text
# tokens: sabhāgatā sā tu punaḥ vipākaḥ api āptayaḥ dvidhā lakṣaṇāni ca niḥṣyandāḥ samāpattyasamanvayāḥ
```

## 4. Grammar

There is no expressed finite verb. The first clause resumes the
preceding predicates and adds maturation; the second supplies
“twofold” to both acquisitions and marks. The last predicate's
“only” is explicit in the prose; the verse SEM records the positive
outflow classification, and a separate prose theory records the exclusion.

```nltk-fcfg
% start S
# tokens: sabhāgatā sā tu punaḥ vipākaḥ api āptayaḥ dvidhā lakṣaṇāni ca niḥṣyandāḥ samāpattyasamanvayāḥ
S[SEM=<(?same & ?twofold & ?outflow)>] -> SAMECLASS[SEM=?same] TWOFOLD[SEM=?twofold] OUTFLOWGROUP[SEM=?outflow]
SAMECLASS[SEM=<(SentientClassed(same_class) & HomogeneousOutflow(same_class) & Unobscured(same_class) & Indeterminate(same_class) & ResultOption(same_class,outflow) & ResultOption(same_class,maturation))>] -> CLASS[CASE=nom,NUM=sg] PRONOUN[CASE=nom,NUM=sg,REF=same_class] CONTRAST RESUMPTION RESULT[CASE=nom,NUM=sg] ALSO[FORCE=additional]
TWOFOLD[SEM=<(ResultOption(acquisition,outflow) & ResultOption(acquisition,maturation) & ResultOption(marks,outflow) & ResultOption(marks,maturation))>] -> ACQUISITIONS[CASE=nom,NUM=pl] TWOWAYS[SORTS=2] MARKS[CASE=nom,NUM=pl] AND[SCOPE=twofold]
OUTFLOWGROUP[SEM=<all x.(OutflowOnlyKind(x) -> ResultOption(x,outflow))>] -> OUTFLOWS[CASE=nom,NUM=pl] COMPOUND[CASE=nom,NUM=pl,ATTAINMENTS=2,NONACQUISITION=1]
CLASS[CASE=nom,NUM=sg] -> 'sabhāgatā'
PRONOUN[CASE=nom,NUM=sg,REF=same_class] -> 'sā'
CONTRAST -> 'tu'
RESUMPTION -> 'punaḥ'
RESULT[CASE=nom,NUM=sg] -> 'vipākaḥ'
ALSO[FORCE=additional] -> 'api'
ACQUISITIONS[CASE=nom,NUM=pl] -> 'āptayaḥ'
TWOWAYS[SORTS=2] -> 'dvidhā'
MARKS[CASE=nom,NUM=pl] -> 'lakṣaṇāni'
AND[SCOPE=twofold] -> 'ca'
OUTFLOWS[CASE=nom,NUM=pl] -> 'niḥṣyandāḥ'
COMPOUND[CASE=nom,NUM=pl,ATTAINMENTS=2,NONACQUISITION=1] -> 'samāpattyasamanvayāḥ'
```

```nltk-dep
'sabhāgatā' -> 'sā' | 'tu' | 'punaḥ' | 'vipākaḥ'
'vipākaḥ' -> 'api'
'āptayaḥ' -> 'dvidhā' | 'lakṣaṇāni'
'lakṣaṇāni' -> 'ca'
'samāpattyasamanvayāḥ' -> 'niḥṣyandāḥ'
```

The three constituent lengths are 6, 4, and 2. Two result-sorts
do not count two acquisitions. The prose's three-Realm range is
modeled separately from the inherited ethical and sentient predicates.

## 5. Translation

### Literal Translation

> Same-class is likewise; that, however, is also maturation.
> Acquisitions are twofold, and so are the marks.
> The attainments and non-acquisition are homogeneous outflows.

### Bhāṣya-informed study translation

> Same-class is likewise classed with sentient beings, is a homogeneous
> outflow, and is unobscured-indeterminate; it is also maturation.
> Acquisitions and marks each admit two result-sorts: homogeneous outflow
> and maturation. The two attainments and non-acquisition are homogeneous
> outflows only.

## 6. Philosophical Translation

> Shared catalogue membership does not impose a shared result-sort.
> Same-class adds maturation without losing homogeneous outflow;
> acquisitions and marks admit both sorts, while the two attainments
> and non-acquisition admit homogeneous outflow alone. The dissociated
> formations close; the inquiry into causes and conditions follows.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| sabhāgatā | same-class | inherited classifications, plus maturation; all three Realms in the prose |
| dvidhā | twofold | result-sorts of acquisitions and marks, not a count of individual dharmas |
| niḥṣyanda / naiḥṣyandika | homogeneous outflow | the result-sort, not ethical indeterminacy |
| vipāka / vipākaja | maturation / maturation-born | being a result, not merely having maturation as an effect |
| acittasamāpattī | two attainments without consciousness | non-reflective attainment and cessation attainment |
| asamanvāgama | non-acquisition | homogeneous outflow only; distinct from acquisition |
| sattvāsattvākhyatā | sentient and non-sentient classification | the marks accompany all conditioned dharmas, not beings alone |

## 8. Logical Determination

```nltk-sem
same_class : (SentientClassed(same_class) & HomogeneousOutflow(same_class) & Unobscured(same_class) & Indeterminate(same_class) & ResultOption(same_class,outflow) & ResultOption(same_class,maturation))
twofold : (ResultOption(acquisition,outflow) & ResultOption(acquisition,maturation) & ResultOption(marks,outflow) & ResultOption(marks,maturation))
outflow_group : all x.(OutflowOnlyKind(x) -> ResultOption(x,outflow))
prose_only : all x.(OutflowOnlyKind(x) -> -ResultOption(x,maturation))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((SentientClassed(same_class) & HomogeneousOutflow(same_class) & Unobscured(same_class) & Indeterminate(same_class) & ResultOption(same_class,outflow) & ResultOption(same_class,maturation)) & (ResultOption(acquisition,outflow) & ResultOption(acquisition,maturation) & ResultOption(marks,outflow) & ResultOption(marks,maturation)) & all x.(OutflowOnlyKind(x) -> ResultOption(x,outflow)))

# THEORY prose_only_outflow
# EXPECT prose_only_outflow T
all x.(OutflowOnlyKind(x) -> -ResultOption(x,maturation))

# THEORY prose_classification
# EXPECT prose_classification T
RealmOption(same_class,desire) & RealmOption(same_class,form) & RealmOption(same_class,formless)
all x.(RealmOption(same_class,x) -> (x = desire | x = form | x = formless))
all x.(VerseKind(x) -> SentientClassed(x))
NonSentientClassed(marks) & SentientClassed(marks)

# THEORY prose_closure
# EXPECT prose_closure T
AlreadyExplained(non_reflective_result) & AlreadyExplained(life)
Closes(unit,dissociated_formations) & -Closes(unit,chapter)
QuestionOf(next_unit,causes_conditions) & -Answers(unit,causes_conditions)

# THEORY rejected_two_realms_transferred
# EXPECT rejected_two_realms_transferred F
all x.(RealmOption(same_class,x) -> (x = desire | x = form))

# THEORY rejected_all_dissociated_formations_are_maturation
# EXPECT rejected_all_dissociated_formations_are_maturation F
all x.(VerseKind(x) -> ResultOption(x,maturation))

# THEORY rejected_marks_only_sentient
# EXPECT rejected_marks_only_sentient F
SentientClassed(marks) & -NonSentientClassed(marks)

# THEORY rejected_result_is_attainment
# EXPECT rejected_result_is_attainment F
(non_reflective_result = non_reflective_attainment) & AlreadyExplained(non_reflective_result)
```

```nltk-valuation
same_class => same_class_kind
acquisition => acquisition_kind
marks => marks_kind
non_reflective_attainment => non_reflective_attainment_kind
cessation_attainment => cessation_attainment_kind
non_acquisition => non_acquisition_kind
non_reflective_result => non_reflective_result_kind
life => life_kind
outflow => homogeneous_outflow_sort
maturation => maturation_sort
desire => desire_realm
form => form_realm
formless => formless_realm
unit => unit_2_48
next_unit => unit_2_49
dissociated_formations => dissociated_formations_section
chapter => indriya_chapter
causes_conditions => causes_conditions_question
VerseKind => {same_class_kind,acquisition_kind,marks_kind,non_reflective_attainment_kind,cessation_attainment_kind,non_acquisition_kind}
OutflowOnlyKind => {non_reflective_attainment_kind,cessation_attainment_kind,non_acquisition_kind}
ResultOption => {(same_class_kind,homogeneous_outflow_sort),(same_class_kind,maturation_sort),(acquisition_kind,homogeneous_outflow_sort),(acquisition_kind,maturation_sort),(marks_kind,homogeneous_outflow_sort),(marks_kind,maturation_sort),(non_reflective_attainment_kind,homogeneous_outflow_sort),(cessation_attainment_kind,homogeneous_outflow_sort),(non_acquisition_kind,homogeneous_outflow_sort)}
SentientClassed => {same_class_kind,acquisition_kind,marks_kind,non_reflective_attainment_kind,cessation_attainment_kind,non_acquisition_kind}
NonSentientClassed => {marks_kind}
HomogeneousOutflow => {same_class_kind}
Unobscured => {same_class_kind}
Indeterminate => {same_class_kind}
RealmOption => {(same_class_kind,desire_realm),(same_class_kind,form_realm),(same_class_kind,formless_realm)}
AlreadyExplained => {non_reflective_result_kind,life_kind}
Closes => {(unit_2_48,dissociated_formations_section)}
QuestionOf => {(unit_2_49,causes_conditions_question)}
Answers => {}
```

The six verse-kind labels are headings, not six distinct real dharmas:
the marks remain a plural category. The nine result-option tuples
give the passage's three two-sort headings and three outflow-group
headings, not nine produced dharmas. Options classify kinds; they do
not assert that every instance is simultaneously both sorts.

The inherited predicates concern same-class here. The single entry
under `HomogeneousOutflow` does not deny the outflow classifications
of the other headings, which are recorded under `ResultOption`.
The marks admit both sentient and non-sentient cases; this does not
make each individual mark both. No unrestricted Realm/result-sort
cross-product, ethical classification of all six kinds, or causal
sufficiency is inferred. The finite model checks this accounting,
not the reality of dissociated formations.

## 9. Interpretive Note

**Translation note.** The “likewise” inherited from 2.47 is selective.
Same-class spans Desire, Form, and Formless Realms, and admits maturation
as well as homogeneous outflow. Acquisition and marks are twofold in
this result classification. The two attainments and non-acquisition
are homogeneous outflows only. The non-reflective result and life are
referred back to earlier explanations, not identified with those
attainments.

In the Organon reading, Cognition joins and governs Perception and
Conception and guides the Dharma Base, remaining distinct from
consciousness and Mind. Closing this central classification preserves
its differentiated relations rather than flattening the headings
into a common causal nature. The next question returns to the causes
and conditions required for arising; it does not announce a chapter
ending or resolve the preceding distinct-entity debates.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_48 a vak:Karika ;
    vak:hasTopic vak:ResultSort ;
    vak:closes vak:DissociatedFormationsDiscussion ;
    vak:hasNextInquiry vak:CausesAndConditions .
vak:SameClass vak:hasResultOption vak:HomogeneousOutflow, vak:Maturation ;
    vak:hasRealmOption vak:DesireRealm, vak:FormRealm, vak:FormlessRealm .
vak:Acquisition vak:hasResultOption vak:HomogeneousOutflow, vak:Maturation .
vak:Marks vak:hasResultOption vak:HomogeneousOutflow, vak:Maturation ;
    vak:hasClassificationOption vak:Sentient, vak:NonSentient .
vak:NonReflectiveAttainment vak:hasResultOption vak:HomogeneousOutflow .
vak:CessationAttainment vak:hasResultOption vak:HomogeneousOutflow .
vak:NonAcquisition vak:hasResultOption vak:HomogeneousOutflow .
```
