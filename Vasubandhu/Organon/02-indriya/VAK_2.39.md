# VAK_2.39 — Form, then Non-Acquisition

## 1. Sanskrit (Devanāgarī)

```sanskrit
निवृतस्य च रूपस्य कामे रूपस्य नाग्रजा ।
अक्लिष्टाव्याकृताप्राप्तिः सातीताजातयोस्त्रिधा ॥ २.३९ ॥
```

## 2. Sanskrit (IAST)

```text
nivṛtasya ca rūpasya kāme rūpasya nāgrajā /
akliṣṭāvyākṛtāprāptiḥ sātītājātayos tridhā // 2.39 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| nivṛtasya rūpasya | gen. sg. n.; adjective and noun | of obscured Form |
| ca | conjunction | also; carries forward the co-arisen-only predicate |
| kāme rūpasya | loc. sg. + gen. sg. n. | of Form in the Desire Realm |
| na agrajā | negation + nom. sg. f. | not prior-arisen |
| akliṣṭā | nom. sg. f.; adjective | unafflicted; resolved as unobscured in the prose |
| avyākṛtā | nom. sg. f.; adjective | indeterminate |
| aprāptiḥ | nom. sg. f. | non-acquisition |
| sā | nom. sg. f.; pronoun | that non-acquisition, not acquisition |
| atīta-ajātayoḥ | gen. dual m. | of past and not-yet-arisen |
| tridhā | adverb | threefold |

Not-yet-arisen is future. Unobscured and indeterminate are two axes.

```text
# tokens: nivṛtasya ca rūpasya kāme rūpasya na agrajā akliṣṭā avyākṛtā aprāptiḥ sā atītājātayoḥ tridhā
```

## 4. Grammar

The first clause inherits “acquisition is co-arisen only” from 2.38; the prose specifies obscured-indeterminate manifest Form. The second excludes prior acquisition of Desire-Realm manifest and nonmanifest Form while admitting co-arisen and subsequent acquisition. Those ranges overlap: the second does not cancel the first's narrower restriction. The final pronoun switches the temporal subject to non-acquisition, with past and future as the paired dharma-times.

```nltk-fcfg
% start S
# tokens: nivṛtasya ca rūpasya kāme rūpasya na agrajā akliṣṭā avyākṛtā aprāptiḥ sā atītājātayoḥ tridhā
S[SEM=<(?obscured & ?desire & ?ethical & ?temporal)>] -> OBSCURED[SEM=?obscured] DESIRE[SEM=?desire] ETHICAL[SEM=?ethical] TEMPORAL[SEM=?temporal]
OBSCURED[SEM=<AcquisitionOption(obscured_manifest,coarisen) & -AcquisitionOption(obscured_manifest,prior) & -AcquisitionOption(obscured_manifest,subsequent)>] -> OBSCUREDGEN ALSO FORM
OBSCUREDGEN -> 'nivṛtasya'
ALSO -> 'ca'
FORM -> 'rūpasya'
DESIRE[SEM=<-AcquisitionOption(desire_form,prior) & AcquisitionOption(desire_form,coarisen) & AcquisitionOption(desire_form,subsequent)>] -> DESIREREALM FORM NOT PRIOR
DESIREREALM -> 'kāme'
NOT -> 'na'
PRIOR -> 'agrajā'
ETHICAL[SEM=<all x.(NonAcquisition(x) -> (Unobscured(x) & Indeterminate(x)))>] -> UNAFFLICTED INDETERMINATE NONACQUISITION
UNAFFLICTED -> 'akliṣṭā'
INDETERMINATE -> 'avyākṛtā'
NONACQUISITION -> 'aprāptiḥ'
TEMPORAL[SEM=<all x y.((PastFuture(x) & Time(y)) -> NonAcquisitionOption(x,y))>] -> THAT PASTFUTURE THREE
THAT -> 'sā'
PASTFUTURE -> 'atītājātayoḥ'
THREE -> 'tridhā'
```

```nltk-dep
'rūpasya' -> 'nivṛtasya' | 'ca' | 'kāme'
'agrajā' -> 'rūpasya' | 'na'
'aprāptiḥ' -> 'akliṣṭā' | 'avyākṛtā'
'tridhā' -> 'sā' | 'atītājātayoḥ'
```

The four constituents span [0, 3), [3, 7), [7, 10), [10, 13). The model's Desire-Realm Form label represents its general range, not a claim that each Form subtype admits subsequent acquisition.

## 5. Translation

### Literal Translation

> Of obscured Form also, [acquisition is co-arisen only]. Of Form in the Desire Realm, [acquisition] is not prior-arisen. Non-acquisition is unafflicted and indeterminate; for past and not-yet-arisen dharmas it is threefold.

### Bhāṣya-informed study translation

> Acquisition of obscured-indeterminate manifest Form is co-arisen only. Acquisition of Desire-Realm Form is never prior to it. Non-acquisition is always unobscured-indeterminate; for past and future dharmas, non-acquisition may be past, present, or future.

## 6. Philosophical Translation

> Non-acquisition does not inherit the ethical class of what is not possessed. Its temporal classification is also distinct from the restrictions just imposed on acquisition of Form.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| nivṛta | obscured | prose specifies obscured-indeterminate manifest Form |
| agrajā | prior | excluded for Desire-Realm Form |
| aprāpti | non-acquisition | the second half |
| akliṣṭa | unobscured | not the ethical axis |
| ajāta | not yet arisen | future |

## 8. Logical Determination

```nltk-sem
classification : all x.(NonAcquisition(x) -> (Unobscured(x) & Indeterminate(x)))
temporal : all x y.((PastFuture(x) & Time(y)) -> NonAcquisitionOption(x,y))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((AcquisitionOption(obscured_manifest,coarisen) & -AcquisitionOption(obscured_manifest,prior) & -AcquisitionOption(obscured_manifest,subsequent)) & (-AcquisitionOption(desire_form,prior) & AcquisitionOption(desire_form,coarisen) & AcquisitionOption(desire_form,subsequent)) & all x.(NonAcquisition(x) -> (Unobscured(x) & Indeterminate(x))) & all x y.((PastFuture(x) & Time(y)) -> NonAcquisitionOption(x,y)))

# THEORY provisional_present_gloss
# EXPECT provisional_present_gloss T
ProvisionalPresentOption(present,present) & -ProvisionalPresentOption(present,past) & -ProvisionalPresentOption(present,future)

# THEORY rejected_same_temporal_range_for_both_form_cases
# EXPECT rejected_same_temporal_range_for_both_form_cases F
all x.(AcquisitionOption(desire_form,x) -> AcquisitionOption(obscured_manifest,x))

# THEORY rejected_future_nonacquisition_only_future
# EXPECT rejected_future_nonacquisition_only_future F
all x.(NonAcquisitionOption(future,x) -> (x = future))

# THEORY rejected_nonacquisition_can_be_unwholesome
# EXPECT rejected_nonacquisition_can_be_unwholesome F
exists x.(NonAcquisition(x) & Unwholesome(x))
```

```nltk-valuation
obscured_manifest => obscured_manifest_range
desire_form => desire_form_general_range
coarisen => coarisen_time
prior => prior_time
subsequent => subsequent_time
past => past_time
present => present_time
future => future_time
AcquisitionOption => {(obscured_manifest_range,coarisen_time),(desire_form_general_range,coarisen_time),(desire_form_general_range,subsequent_time)}
NonAcquisition => {nonacquisition_example_one,nonacquisition_example_two}
Unobscured => {nonacquisition_example_one,nonacquisition_example_two}
Indeterminate => {nonacquisition_example_one,nonacquisition_example_two}
Unwholesome => {}
PastFuture => {past_time,future_time}
Time => {past_time,present_time,future_time}
NonAcquisitionOption => {(past_time,past_time),(past_time,present_time),(past_time,future_time),(future_time,past_time),(future_time,present_time),(future_time,future_time)}
ProvisionalPresentOption => {(present_time,present_time)}
```

The six past/future combinations belong to the verse theory. The present-only proposal has a separately named provisional predicate and theory; it is not smuggled into the verse's semantic root. Finite examples test internal classification, not the ontological dispute about acquisition and non-acquisition.

## 9. Interpretive Note

**Translation note.** The Bhāṣya grounds the weakness of obscured-indeterminate manifest Form in its failure to produce nonmanifest Form even when intense. Its present-dharma non-acquisition gloss is damaged. The proposed present-only reading is retained only in the Bhāṣya discussion and separately marked model, not the kārikā translation.

Realm classifications of non-acquisition, and ordinary-person status, are 2.40. The Buddha counterexample belongs there: absence of another lineage is not non-nobility.

In the Organon reading, Cognition joins and governs Perception and Conception and guides the Dharma Base, without becoming consciousness or Mind. The acquisition/non-acquisition dyad retains distinct positive and negative classifications. A negative determination is not an untyped blank, nor does its classification by itself prove that it is a separate substance.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_39 a vak:Karika ; vak:hasTopic vak:NonAcquisitionTyped .
vak:NonAcquisition vak:classification vak:UnobscuredIndeterminate .
vak:PresentOnlyNonAcquisitionGloss vak:reviewStatus vak:Provisional .
```
