# VAK_2.31 — Dhyāna-Stage Caitta Profiles

## 1. Sanskrit — Devanāgarī

```text
कौकृत्यमिद्धाकुशलान्याद्ये ध्याने न सन्त्यतः ।
ध्यानान्तरे वितर्कश्च विचारश्चाप्यतः परम् ॥ VAkK_2.31 ॥
```

## 2. Sanskrit — IAST

```text
kaukṛtyamiddhākuśalāny ādye dhyāne na santy ataḥ /
dhyānāntare vitarkaś ca vicāraś cāpy ataḥ param // VAkK_2.31 //
```

Source form:

```text
kaukṛtyamiddhākuśalānyādye dhyāne na santyataḥ /
dhyānāntare vitarkaśca vicāraścāpyataḥ param // VAkK_2.31 //
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| kaukṛtya | kaukṛtya | neuter noun in compound | regret / remorse |
| middha | middha | neuter noun in compound | sleepiness / torpor |
| akuśalāni | akuśalāni | neuter nominative plural | unwholesome factors |
| ādye | ādye | locative singular | in the first |
| dhyāne | dhyāne | locative singular | in dhyāna |
| na santi | na santi | finite verb, plural | are not present |
| ataḥ | ataḥ | indeclinable | from this / thence |
| dhyāna-antare | dhyānāntare | locative singular compound | in another dhyāna / subsequent dhyāna |
| vitarkaḥ | vitarkaḥ | masculine nominative singular | vitarka |
| ca | ca | indeclinable | and |
| vicāraḥ | vicāraḥ | masculine nominative singular | vicāra |
| api | api | particle | also |
| ataḥ param | ataḥ param | phrase | beyond this / thereafter |

## 4. Literal Translation

```text
Kaukṛtya, middha, and unwholesome factors are not present in the first dhyāna.
In another dhyāna, vitarka also is not present; beyond this, vicāra too is not present.
```

## 5. Philosophical Translation

```text
As the dhyāna-level changes, the caitta profile changes.
In the first dhyāna, regret, torpor, and unwholesome factors are absent.
In a further dhyāna, vitarka is no longer present.
Beyond that, vicāra too is no longer present.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| kaukṛtya | regret / remorse | Additional factor in VAK_2.28–2.29 |
| middha | sleepiness / torpor | Compatible factor in VAK_2.30, but absent at this dhyāna level |
| akuśala | unwholesome | Unskillful factor-status |
| ādya dhyāna | first dhyāna | First meditative absorption level |
| dhyānāntara | another/subsequent dhyāna | Further dhyāna-stage |
| vitarka | vitarka | Left untranslated; coarse applicative function |
| vicāra | vicāra | Left untranslated; subtler investigative function |
| ataḥ param | beyond this | Progressive stage marker |

## 7. Logical Determination

VAK_2.31 gives dhyāna-stage feature-presence rules for caitta profiles.

```text
first dhyāna:
    kaukṛtya, middha, and akuśala factors are not present

further dhyāna:
    vitarka is not present

beyond that:
    vicāra is not present
```

The dominant protocol is Hypothetical stage-logic:

```text
if stage = first dhyāna,
then these factors are absent.

if stage = further dhyāna,
then vitarka is absent.

if stage = beyond that,
then vicāra is absent.
```

Thus the citta-caitta catalog is sensitive to contemplative level.

## 8. Relation to Indriya

Indriya profiles were earlier defined by configuration, count, and qualifying conditions.

Here caitta profiles are defined by contemplative stage.

```text
Indriya configuration
    = faculty-array under conditions

Caitta configuration
    = appearance-array under dhyāna-stage
```

This continues the same pattern at the level of appearance.

## 9. Organon Interpretation

Organon reading:

```text
DhyanaCaittaProfile:
    stage = first | further | beyond
    absentFactors = kaukṛtya | middha | akuśala | vitarka | vicāra
```

Learning implication:

```text
Higher learning is not only feature acquisition.
It is also the lawful clarification of which factors are present at each stabilization-level.
```

The Agent requires stage-sensitive feature rules.

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .

vak:FirstDhyanaCaittaProfile a vak:CittaCaittaProfile ;
    vak:hasDhyanaStage vak:FirstDhyana ;
    vak:hasAbsentFactor vak:Kaukṛtya, vak:Middha, vak:AkusalaFactor .

vak:FurtherDhyanaCaittaProfile a vak:CittaCaittaProfile ;
    vak:hasAbsentFactor vak:Vitarka .

vak:BeyondFurtherDhyanaCaittaProfile a vak:CittaCaittaProfile ;
    vak:hasAbsentFactor vak:Vicāra .
```

## 11. Commit History

```text
VAK_2.31 opened.
Method: kārikā-first speculative seed.
Theme: dhyāna-stage caitta profiles.
Logical protocols recorded: hypothetical stage-rule and feature-presence logic.
Relation to indriya tracked: caitta profiles repeat configuration logic at the appearance/stabilization level.
Zero-padded file naming maintained: VAK_2.31.
```
