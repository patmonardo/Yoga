# VAK_2.61 — Four Conditions

## 1. Sanskrit (Devanāgarī)

```sanskrit
चित्तचैत्ताः समानाः शेषाः सम्प्रयुक्ताद् ऋते /
चत्वारः प्रत्यया उक्ताः हेत्वाख्यः पञ्च हेतवः // २.६१ //
```

## 2. Sanskrit (IAST)

```text
cittacaittāḥ samānāḥ śeṣāḥ saṃprayuktād ṛte /
catvāraḥ pratyayā uktāḥ hetvākhyaḥ pañca hetavaḥ // 2.61 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| cittacaittāḥ | m. pl. | consciousness and mental factors. |
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

> Consciousness and mental factors, and the others likewise except the
> associated [cause]. Four conditions are taught; the cause-named
> condition is five causes.
### Bhāṣya-informed study translation

> Consciousness and mental factors, and the other [dharmas] likewise,
> except for the associated cause. Four conditions are taught; the
> cause-condition is the five causes.
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

**Translation note.** The Bhāṣya names the four conditions as cause,
immediately antecedent, object, and predominant. The “cause-condition”
consists of the five causes other than the conditioning cause; these
similarly named notions are distinct. The associated-cause exclusion
continues the preceding discussion and does not redefine the four
conditions.

Four conditions named. Cause-condition is five causes, not the conditioning cause. Associated exclusion is a different question. Other three named, not defined.

## 10. OWL++ Seed

```turtle
:FourConditions :named true .
:CauseCondition :isFiveCauses true ; :excludes :ConditioningCause .
:AntecedentCondition :named true ; :defined false .
:ObjectCondition :named true ; :defined false .
:PredominantCondition :named true ; :defined false .
```
