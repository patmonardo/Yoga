# VAK_2.42 — The Non-Reflective Attainment

## 1. Sanskrit (Devanāgarī)

```sanskrit
तथासंज्ञिसमापत्तिर्ध्यानेऽन्त्ये निःसृतीच्छया ।
शुभा उपपद्यवेद्यैव नार्यस्यैकाध्विकाप्यते ॥ २.४२ ॥
```

## 2. Sanskrit (IAST)

```text
tathāsaṃjñisamāpattir dhyāne 'ntye niḥsṛtīcchayā /
śubhā upapadyavedyaiva nāryasyaikādhvikāpyate // 2.42 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| tathā | adverb | likewise, that much |
| asaṃjñi-samāpattiḥ | nom. sg. f.; compound | non-reflective attainment |
| dhyāne antye | loc. sg. n. + loc. sg. n. | in the final dhyāna |
| niḥsṛti-icchayā | instr. sg. f.; compound | by the wish for release |
| śubhā | nom. sg. f. | wholesome |
| upapadya-vedyā eva | nom. sg. f. + particle | to be experienced only in the next rebirth |
| na āryasya | gen. sg. m.; negation | not a noble person's |
| eka-adhvikā | nom. sg. f.; adjective | of one temporal period, explained as present only |
| āpyate | 3 sg. present passive of √āp | is acquired |

Two name-construals: attainment of the non-reflective beings, or attainment that is non-reflective. The sequence stated is attainment, then maturation. Not rebirth first.

```text
# tokens: tathā asaṃjñisamāpattiḥ dhyāne antye niḥsṛtīcchayā śubhā upapadyavedyā eva na āryasya ekādhvikā āpyate
```

## 4. Grammar

“Likewise” carries forward only cessation of consciousness and mental factors from 2.41, not that result's indeterminate ethical status. The prose resolves the final dhyāna as the fourth and the one temporal period as present acquisition. The wish for release describes the entrant's assessment, not an assertion that this attainment is liberation. The exclusive next-rebirth timing concerns maturation, not the time at which the attainment is entered.

```nltk-fcfg
% start S
# tokens: tathā asaṃjñisamāpattiḥ dhyāne antye niḥsṛtīcchayā śubhā upapadyavedyā eva na āryasya ekādhvikā āpyate
S[SEM=<(?cessation & ?level & ?motive & ?ethical & ?timing & ?person & ?acquisition)>] -> CESSATION[SEM=?cessation] LEVEL[SEM=?level] MOTIVE[SEM=?motive] ETHICAL[SEM=?ethical] TIMING[SEM=?timing] PERSON[SEM=?person] ACQUISITION[SEM=?acquisition]
CESSATION[SEM=<CessationOf(attainment,consciousness_and_factors)>] -> LIKEWISE ATTAINMENT
LIKEWISE -> 'tathā'
ATTAINMENT -> 'asaṃjñisamāpattiḥ'
LEVEL[SEM=<AtLevel(attainment,fourth_dhyana)>] -> DHYANA FINAL
DHYANA -> 'dhyāne'
FINAL -> 'antye'
MOTIVE[SEM=<EnteredWithWish(attainment,release)>] -> WISH
WISH -> 'niḥsṛtīcchayā'
ETHICAL[SEM=<Wholesome(attainment)>] -> WHOLESOME
WHOLESOME -> 'śubhā'
TIMING[SEM=<all x.(MaturationTiming(attainment,x) <-> (x = next_rebirth))>] -> NEXT ONLY
NEXT -> 'upapadyavedyā'
ONLY -> 'eva'
PERSON[SEM=<-Eligible(noble,attainment)>] -> NOT NOBLE
NOT -> 'na'
NOBLE -> 'āryasya'
ACQUISITION[SEM=<all x.(AcquisitionTime(attainment,x) <-> (x = present))>] -> ONETIME ACQUIRED
ONETIME -> 'ekādhvikā'
ACQUIRED -> 'āpyate'
```

```nltk-dep
'asaṃjñisamāpattiḥ' -> 'tathā' | 'dhyāne' | 'niḥsṛtīcchayā' | 'śubhā' | 'upapadyavedyā' | 'āryasya' | 'āpyate'
'dhyāne' -> 'antye'
'upapadyavedyā' -> 'eva'
'āryasya' -> 'na'
'āpyate' -> 'ekādhvikā'
```

The seven constituent lengths are 2, 2, 1, 1, 2, 2, and 2.

## 5. Translation

### Literal Translation

> Likewise, the non-reflective attainment is in the final dhyāna and is entered with the wish for release. It is wholesome, [its maturation] experienced only in the next rebirth, not a noble person's, and acquired in one temporal period.

### Bhāṣya-informed study translation

> Likewise, non-reflective attainment is cessation of consciousness and the mental factors. It belongs to the fourth dhyāna and is entered with the wish for release. It is wholesome, with maturation experienced only in the next rebirth; it is not for a noble person and is acquired only as a present instance.

## 6. Philosophical Translation

> “Likewise” shares the cessation, not the result's ethical status. The attainment is wholesome; its next-rebirth maturation is indeterminate. Present-only acquisition does not exclude later possession of what has become past.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| asaṃjñi-samāpatti | non-reflective attainment | the cause |
| āsaṃjñika | non-reflective result | the maturation; 2.41 |
| niḥsṛti-icchā | wish for release | their construal |
| upapadya-vedya | next rebirth | the timing |
| eka-adhvika | one time | present acquisition |
| acittaka | without consciousness | the state; not the class-name |
| vinipāta-sthāna | place of downfall | the noble assessment |

## 8. Logical Determination

```nltk-sem
present_acquisition : all x.(AcquisitionTime(attainment,x) <-> (x = present))
next_rebirth_maturation : all x.(MaturationTiming(attainment,x) <-> (x = next_rebirth))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(CessationOf(attainment,consciousness_and_factors) & AtLevel(attainment,fourth_dhyana) & EnteredWithWish(attainment,release) & Wholesome(attainment) & all x.(MaturationTiming(attainment,x) <-> (x = next_rebirth)) & -Eligible(noble,attainment) & all x.(AcquisitionTime(attainment,x) <-> (x = present)))

# THEORY prose_cause_result_and_possession
# EXPECT prose_cause_result_and_possession T
MaturationOf(result,attainment) & Indeterminate(result) & -(attainment = result)
PossessesInstance(first_moment,present) & PossessesInstance(second_moment,past) & PossessesInstance(second_moment,present)
-CultivatesFuture(attainment) & -AcquiredWithLevel(attainment,fourth_dhyana)

# THEORY reported_regaining
# EXPECT reported_regaining T
ReportedNecessaryRegaining(fallen_practitioner,attainment) & ReportedRebirth(fallen_practitioner,nonreflective_beings)

# THEORY rejected_likewise_transfers_result_ethics
# EXPECT rejected_likewise_transfers_result_ethics F
Indeterminate(attainment) & Wholesome(attainment)

# THEORY rejected_present_acquisition_precludes_past_possession
# EXPECT rejected_present_acquisition_precludes_past_possession F
all x.(AcquisitionTime(attainment,present) -> -PossessesInstance(x,past))

# THEORY rejected_fourth_dhyana_automatically_acquires_attainment
# EXPECT rejected_fourth_dhyana_automatically_acquires_attainment F
AcquiredWithLevel(attainment,fourth_dhyana) & AtLevel(attainment,fourth_dhyana)
```

```nltk-valuation
attainment => nonreflective_attainment
result => nonreflective_maturation
consciousness_and_factors => consciousness_factor_group
fourth_dhyana => fourth_dhyana_level
release => release_wish
next_rebirth => next_rebirth_period
present => present_time
past => past_time
noble => noble_person_class
first_moment => first_moment_example
second_moment => second_moment_example
fallen_practitioner => fallen_practitioner_example
nonreflective_beings => nonreflective_being_group
CessationOf => {(nonreflective_attainment,consciousness_factor_group)}
AtLevel => {(nonreflective_attainment,fourth_dhyana_level)}
EnteredWithWish => {(nonreflective_attainment,release_wish)}
Wholesome => {nonreflective_attainment}
MaturationTiming => {(nonreflective_attainment,next_rebirth_period)}
Eligible => {}
AcquisitionTime => {(nonreflective_attainment,present_time)}
MaturationOf => {(nonreflective_maturation,nonreflective_attainment)}
Indeterminate => {nonreflective_maturation}
PossessesInstance => {(first_moment_example,present_time),(second_moment_example,past_time),(second_moment_example,present_time)}
CultivatesFuture => {}
AcquiredWithLevel => {}
ReportedNecessaryRegaining => {(fallen_practitioner_example,nonreflective_attainment)}
ReportedRebirth => {(fallen_practitioner_example,nonreflective_being_group)}
```

The second-moment example is a continuing attainment before relinquishment, not every possible second moment. Past possession does not mean acquiring a past instance on entry. The regaining predicates label the report marked by *kila*, not a finite proof of necessary future rebirth. Empty eligibility records only the negative noble-person case tested here, not universal ineligibility.

## 9. Interpretive Note

**Translation note.** The commentary identifies the final dhyāna as the fourth and explains the wish for release. Its maturation is indeterminate and experienced only in the next rebirth; even after falling away, the attainment is said to be produced again. Noble persons do not enter it. Acquisition is present-instance only, compared with the restraint of individual liberation; no future instance is cultivated because the attainment is without consciousness.

Kila marks the necessary rebirth after falling away. Report, not a recommendation. The restraint of individual liberation is the analogy for present-only acquisition. Not an identity of the two.

In the Organon reading, Cognition joins and governs Perception and Conception and guides the Dharma Base, remaining distinct from consciousness and Mind. An entrant's wish for release does not establish liberation. The classification must preserve the distinction between a practice, its maturation, present acquisition, continuing past possession, and cultivation of future instances.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_42 a vak:Karika ; vak:hasTopic vak:NonReflectiveAttainment .
vak:LikewiseIn2_42 vak:carries vak:ConsciousnessAndFactorCessation .
vak:NonReflectiveAttainment vak:ethicalClass vak:Wholesome ;
    vak:acquiredInstanceTime vak:Present ;
    vak:maturationTiming vak:NextRebirth .
```
