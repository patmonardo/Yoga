# VAK_2.42 — Asaṃjñi-Samāpatti Profile

## 1. Sanskrit — Devanāgarī

```text
तथासंज्ञिसमापत्तिः ध्यानेऽन्त्ये निःसृतीच्छया ।
शुभा उपपद्यवेद्यैव नार्यस्य एकाध्विकाप्यते ॥ VAkK_2.42 ॥
```

## 2. Sanskrit — IAST

```text
tathāsaṃjñisamāpattiḥ dhyāne 'ntye niḥsṛtīcchayā /
śubhā upapadyavedyaiva nāryasya ekādhvikāpyate // VAkK_2.42 //
```

Source form:

```text
tathāsaṃjñisamāpattiḥ dhyāne 'ntye niḥsṛtīcchayā /
śubhā upapadyavedyaiva nāryasya ekādhvikāpyate // VAkK_2.42 //
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| tathā | tathā | indeclinable | likewise |
| asaṃjñi-samāpattiḥ | asaṃjñisamāpattiḥ | feminine nominative singular | attainment of non-ideation |
| dhyāne antye | dhyāne 'ntye | locative phrase | in the final dhyāna |
| niḥsṛti-icchayā | niḥsṛtīcchayā | instrumental singular | through desire for release / emergence |
| śubhā | śubhā | feminine nominative singular | wholesome |
| upapadya-vedyā eva | upapadyavedyā eva | feminine nominative singular phrase | experienced at rebirth only; verify |
| na āryasya | nāryasya | genitive singular with negation | not of the noble one |
| eka-adhvikā | ekādhvikā | feminine nominative singular | belonging to one time |
| āpyate | āpyate | passive, 3rd singular | is acquired / obtained |

## 4. Literal Translation

```text
Likewise, the asaṃjñi-samāpatti occurs in the final dhyāna through the wish for release.
It is wholesome, experienced at rebirth only, not belonging to the noble one, and is acquired as one-time.
```

## 5. Philosophical Translation

```text
The attainment of non-ideation is profiled as a structural meditative state.
It belongs to the final dhyāna, is motivated by a wish for release, is wholesome,
and has restricted status with respect to noble persons, temporal acquisition, and rebirth-result.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| asaṃjñi-samāpatti | attainment of non-ideation | Meditative state involving absence/suspension of ideational activity |
| antya-dhyāna | final dhyāna | Highest relevant dhyāna level in this context |
| niḥsṛti-icchā | desire for release | Motivating orientation |
| śubha | wholesome | Ethical/status qualifier |
| upapadya-vedya | to be experienced at rebirth | Technical result-timing; verify later |
| ārya | noble one | Path-status |
| ekādhvika | one-time / one-temporal | Temporal profile |
| āpyate | is acquired | Prāpti relation |

## 7. Logical Determination

VAK_2.42 gives a profile for asaṃjñi-samāpatti.

```text
AsamjniSamapattiProfile:
    dhyānaStage = final
    motivation = wish for release
    ethicalStatus = śubha
    resultTiming = upapadya-vedya
    pathScope = not ārya
    timeProfile = ekādhvika
```

This continues the same feature logic:

```text
state
    = class + stage + motive + status + result + acquisition profile
```

## 8. Relation to Indriya and Citta-Caitta

The citta-caitta system described ordinary appearance operation.
Asaṃjñi-samāpatti describes a structural state in which that operation is not simply active in the usual way.

```text
Citta-Caitta
    = appearance operation

Samāpatti
    = structural stabilization / suspension profile
```

## 9. Organon Interpretation

Organon reading:

```text
StructuralStateProfile:
    stateType = asaṃjñi-samāpatti
    stabilizationLevel = final dhyāna
    ethicalStatus = wholesome
    acquisitionScope = restricted
```

Engineering implication:

```text
The Dataset must model special states,
not just ordinary event-streams.
```

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .

vak:AsamjniSamapattiProfile a vak:ViprayuktaSamskara ;
    vak:hasDhyanaStage vak:FinalDhyana ;
    vak:hasMotivation vak:NihsrtiIccha ;
    vak:hasEthicalStatus vak:Subha ;
    vak:hasResultTiming vak:UpapadyaVedya .
```

## 11. Commit History

```text
VAK_2.42 opened.
Method: kārikā-first speculative seed.
Theme: asaṃjñi-samāpatti as special structural state profile.
Technical vocabulary marked for later Bhāṣya review.
Organon mapping: special state-profile in the Semantic Dataset.
Zero-padded file naming maintained: VAK_2.42.
```
