# VAK_2.61 — Four Conditions

## 1. Sanskrit (Devanāgarī)

> चित्तचैत्ताः समानाः शेषाः सम्प्रयुक्ताद् ऋते /
> चत्वारः प्रत्यया उक्ताः हेत्वाख्यः पञ्च हेतवः // २.६१ //

## 2. Sanskrit (IAST)

> cittacaittāḥ samānāḥ śeṣāḥ saṃprayuktād ṛte /
>
> catvāraḥ pratyayā uktāḥ hetvākhyaḥ pañca hetavaḥ // 2.61 //

## 3. Lexical Analysis

| Pada | Morphology | Force |
|---|---|---|
| cittacaittāḥ | m. pl. | Mind and mental factors. |
| samānāḥ | adj. | Likewise. |
| śeṣāḥ | adj. | The others. |
| saṃprayuktāt | abl. sg. | From the associated. |
| ṛte | pcl. | Excluding. |
| catvāraḥ | num. | Four. |
| pratyayāḥ | m. pl. | Conditions. |
| uktāḥ | adj. | Taught. |
| hetvākhyaḥ | adj. | Named cause. |
| pañca | num. | Five. |
| hetavaḥ | m. pl. | Causes. |

## 4. Grammar

```text
% start S
S[CONDITION=four] -> Cause | Antecedent | Object | Predominant
S[CONDITION=cause] -> FiveCauses[NOT=conditioning]
```

Four conditions named.  
Cause-condition is five causes, not the conditioning cause.  
Associated exclusion is a different question.  
Other three named, not defined.

## 5. Translation

### Literal Translation

Mind and the mental factors, likewise. The others also, excluding the associated cause. Four conditions are taught. The one named cause is the five causes.

### Bhāṣya-informed study translation

> Four conditions named. Cause-condition is five causes, not the conditioning cause. Associated exclusion is a different question. Other three named, not defined.

## 6. Philosophical Translation

> Four conditions named. Cause-condition is five causes, not the conditioning cause. Associated exclusion is a different question. Other three named, not defined.

## 7. Technical Vocabulary

| Term | Rendering |
|---|---|
| pratyaya | Condition. |
| hetu-pratyaya | Cause-condition. Five causes, not the conditioning cause. |
| samanantara | Immediately antecedent. |
| ālambana | Object. |
| adhipati | Predominant. |

## 8. Logical Determination

Four conditions named. Cause-condition is five causes, not the conditioning cause.

## 9. Interpretive Note

Four conditions named. Cause-condition is five causes, not the conditioning cause. Associated exclusion is a different question. Other three named, not defined.

## 10. OWL++ Seed

```turtle
:FourConditions :named true .
:CauseCondition :isFiveCauses true ; :excludes :ConditioningCause .
:AntecedentCondition :named true ; :defined false .
:ObjectCondition :named true ; :defined false .
:PredominantCondition :named true ; :defined false .
```
