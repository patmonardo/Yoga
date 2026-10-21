# VAK_2.38 — Acquisition Status and Temporal Exceptions

## 1. Sanskrit (Devanāgarī)

```sanskrit
त्रिधा नशैक्षाशैक्षाणामहेयानां द्विधा मता ।
अव्याकृताप्तिः सहजाभिज्ञानैर्माणिकादृते ॥ २.३८ ॥
```

## 2. Sanskrit (IAST)

```text
tridhā naśaikṣāśaikṣāṇām aheyānāṃ dvidhā matā /
avyākṛtāptiḥ sahajābhijñānairmāṇikād ṛte // 2.38 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| na-śaikṣa-aśaikṣāṇām | gen. pl. m.; compound | of what is neither trainee nor beyond training |
| tridhā | adverb | threefold |
| aheyānām | gen. pl. m.; past passive participle | of what is not to be abandoned |
| dvidhā | adverb | twofold |
| matā | nom. sg. f.; past passive participle of √man | held to be; agrees with supplied acquisition |
| avyākṛta-āptiḥ | nom. sg. f.; compound | acquisition of the indeterminate |
| sahajā | nom. sg. f.; adjective | co-arisen, simultaneous with the acquired dharma |
| abhijñā-nairmāṇikāt | abl. sg.; compound, final t voiced before ṛte | superknowledges and magical-creation consciousness, the exception-group |
| ṛte | indeclinable governing the exception | except |

The Bhāṣya specifies two indeterminate superknowledges and magical-creation consciousness as exceptions. The verse retains the sandhied form; sahajā is simultaneous, not innate.

```text
# tokens: tridhā naśaikṣāśaikṣāṇām aheyānām dvidhā matā avyākṛtāptiḥ sahajā abhijñānairmāṇikāt ṛte
```

## 4. Grammar

Acquisition is supplied in the first two clauses. Threefold and twofold summarize ranges whose members the prose distinguishes; they do not give every subtype every option. The prose narrows the final rule to unobscured-indeterminate dharmas and then exempts the two indeterminate superknowledges and magical-creation consciousness. The final compound is an ablative exception-group, not a separate instrumental plural *abhijñā*.

```nltk-fcfg
% start S
# tokens: tridhā naśaikṣāśaikṣāṇām aheyānām dvidhā matā avyākṛtāptiḥ sahajā abhijñānairmāṇikāt ṛte
S[SEM=<(?status & ?abandonment & ?temporal)>] -> STATUS[SEM=?status] ABANDONMENT[SEM=?abandonment] TEMPORAL[SEM=?temporal]
STATUS[SEM=<all x.(StatusClass(x) -> StatusAggregate(x))>] -> THREE NEITHER
THREE -> 'tridhā'
NEITHER -> 'naśaikṣāśaikṣāṇām'
ABANDONMENT[SEM=<all x.(AbandonmentClass(x) -> AbandonmentAggregate(x))>] -> NOTABANDONABLE TWO HELD
NOTABANDONABLE -> 'aheyānām'
TWO -> 'dvidhā'
HELD -> 'matā'
TEMPORAL[SEM=<all x.((UnobscuredIndeterminate(x) & -MainException(x)) -> (TemporalOption(x,coarisen) & -TemporalOption(x,prior) & -TemporalOption(x,subsequent)))>] -> INDETERMINATE COARISEN EXCEPTIONS EXCEPT
INDETERMINATE -> 'avyākṛtāptiḥ'
COARISEN -> 'sahajā'
EXCEPTIONS -> 'abhijñānairmāṇikāt'
EXCEPT -> 'ṛte'
```

```nltk-dep
'tridhā' -> 'naśaikṣāśaikṣāṇām'
'matā' -> 'aheyānām' | 'dvidhā'
'sahajā' -> 'avyākṛtāptiḥ' | 'ṛte'
'ṛte' -> 'abhijñānairmāṇikāt'
```

The constituent spans are [0, 2), [2, 5), and [5, 9). The parse's temporal predicate is prose-resolved, not the unqualified claim that every indeterminate dharma has only co-arisen acquisition.

## 5. Translation

### Literal Translation

> Acquisition of what is neither trainee nor beyond training is threefold. Acquisition of what is not to be abandoned is twofold. Acquisition of the indeterminate is co-arisen, except the superknowledges and magical-creation consciousness.

### Bhāṣya-informed study translation

> Acquisition of dharmas neither in training nor beyond training is threefold in status. Acquisition of dharmas not to be abandoned is held to be twofold. Acquisition of unobscured-indeterminate dharmas is co-arisen only, except for the two indeterminate superknowledges and magical-creation consciousness.

## 6. Philosophical Translation

> The acquired dharma's status need not be its acquisition's status. Nor does a dharma's not being abandonable make its acquisition necessarily non-abandonable. The general temporal matrix now receives a restricted simultaneous-only rule and specified exceptions.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| naivaśaikṣanāśaikṣa | neither | the third path-class |
| aheya | not to be abandoned | the dharma's acquisition may nevertheless be abandonable through cultivation |
| bhāvanāheya | abandonable through cultivation | classification, not an assertion of completed abandonment |
| sahajā | co-arisen | not innate |
| agrajā | prior | the exception |
| abhijñā | superknowledge | two indeterminate |
| nairmāṇika | magical-creation consciousness | the other main exception |

Crafts are a further attributed extension. Not every skill is a superknowledge.

## 8. Logical Determination

The following finite cases distinguish paths by which cessation through Discrimination was acquired. They are not different cessation entities asserted by this model. The aggregate classifications are unions, not unrestricted per-case options.

```nltk-sem
status : all x.(StatusClass(x) -> StatusAggregate(x))
abandonment : all x.(AbandonmentClass(x) -> AbandonmentAggregate(x))
temporal : all x.((UnobscuredIndeterminate(x) & -MainException(x)) -> (TemporalOption(x,coarisen) & -TemporalOption(x,prior) & -TemporalOption(x,subsequent)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.(StatusClass(x) -> StatusAggregate(x)) & all x.(AbandonmentClass(x) -> AbandonmentAggregate(x)) & all x.((UnobscuredIndeterminate(x) & -MainException(x)) -> (TemporalOption(x,coarisen) & -TemporalOption(x,prior) & -TemporalOption(x,subsequent))))

# THEORY prose_ranges_and_exceptions
# EXPECT prose_ranges_and_exceptions T
all y.(StatusAggregate(y) <-> exists x.(NeitherStatusCase(x) & AcquisitionStatus(x,y)))
all y.(AbandonmentAggregate(y) <-> exists x.(NonAbandonableCase(x) & AcquisitionAbandonment(x,y)))
all x.(MainException(x) -> (TemporalOption(x,prior) & TemporalOption(x,coarisen) & TemporalOption(x,subsequent)))

# THEORY rejected_every_neither_case_has_three_statuses
# EXPECT rejected_every_neither_case_has_three_statuses F
all x y.((NeitherStatusCase(x) & StatusClass(y)) -> AcquisitionStatus(x,y))

# THEORY rejected_nonabandonable_always_inherited
# EXPECT rejected_nonabandonable_always_inherited F
all x.(NonAbandonableCase(x) -> AcquisitionAbandonment(x,not_abandonable))

# THEORY rejected_all_unobscured_indeterminate_only_coarisen
# EXPECT rejected_all_unobscured_indeterminate_only_coarisen F
all x.(UnobscuredIndeterminate(x) -> (-TemporalOption(x,prior) & -TemporalOption(x,subsequent)))
```

```nltk-valuation
coarisen => coarisen_time
prior => prior_time
subsequent => subsequent_time
not_abandonable => not_abandonable_class
StatusClass => {trainee,beyond_training,neither_status}
StatusAggregate => {trainee,beyond_training,neither_status}
NeitherStatusCase => {contaminated_case,nondiscriminative_cessation,discriminative_ordinary,discriminative_trainee,discriminative_beyond}
AcquisitionStatus => {(contaminated_case,neither_status),(nondiscriminative_cessation,neither_status),(discriminative_ordinary,neither_status),(discriminative_trainee,trainee),(discriminative_beyond,beyond_training)}
AbandonmentClass => {cultivation_abandonable,not_abandonable_class}
AbandonmentAggregate => {cultivation_abandonable,not_abandonable_class}
NonAbandonableCase => {nondiscriminative_cessation,discriminative_ordinary,discriminative_trainee,discriminative_beyond,path_truth}
AcquisitionAbandonment => {(nondiscriminative_cessation,cultivation_abandonable),(discriminative_ordinary,cultivation_abandonable),(discriminative_trainee,not_abandonable_class),(discriminative_beyond,not_abandonable_class),(path_truth,not_abandonable_class)}
UnobscuredIndeterminate => {ordinary_unobscured,superknowledge_one,superknowledge_two,creation_consciousness}
MainException => {superknowledge_one,superknowledge_two,creation_consciousness}
TemporalOption => {(ordinary_unobscured,coarisen_time),(superknowledge_one,prior_time),(superknowledge_one,coarisen_time),(superknowledge_one,subsequent_time),(superknowledge_two,prior_time),(superknowledge_two,coarisen_time),(superknowledge_two,subsequent_time),(creation_consciousness,prior_time),(creation_consciousness,coarisen_time),(creation_consciousness,subsequent_time)}
```

The unnamed superknowledge slots preserve the source's two without importing later identifications. Craft-based and greatly habituated deportment-based cases are an attributed further extension in the prose; they are not silently added to the main verse exceptions or denied by this partial illustrative model.

## 9. Interpretive Note

**Translation note.** The commentary resolves both aggregate counts through specific cases, then explicitly calls the simultaneous-only rule an exception to 2.37. It explains the main exceptions by strength and distinctive preparatory practice. The attributed craft/deportment extension follows before the obscured Form discussion of 2.39.

In the Organon reading, Cognition joins and governs Perception and Conception and guides the Dharma Base while remaining distinct from consciousness and Mind. Here determination belongs to a relation: cessation's own status does not simply dictate that of acquisition. The classification must retain the acquiring path and temporal relation without confusing an abandonable acquisition with an already abandoned dharma.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_38 a vak:Karika ;
    vak:hasTopic vak:AcquisitionStatus, vak:TemporalExceptions .
vak:AcquisitionStatus vak:requiresAcquiringPathDistinction true .
vak:CoarisenAcquisition vak:notEquivalentTo vak:Innateness .
```
