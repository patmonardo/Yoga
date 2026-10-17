# VAK_2.63 — Activity Toward Ceasing and Arising

## 1. Sanskrit (Devanāgarī)

> द्वौ हेतू पञ्च च ततः अन्याव् तु प्रत्ययौ तद्विपर्ययात् // २.६३ //

## 2. Sanskrit (IAST)

> dvau hetū pañca ca tataḥ anyau tu pratyayau tadviparyayāt // 2.63 //

## 3. Lexical Analysis

| Pada | Morphology | Force |
|---|---|---|
| dvau | num. | Two. |
| hetū | m. dual | Causes. |
| pañca | num. | Five. |
| tataḥ | abl. | From that. |
| anyau | adj. | Other. |
| tu | pcl. | But. |
| pratyayau | m. dual | Conditions. |
| tadviparyayāt | abl. sg. | By the reverse of that. |

## 4. Grammar

```text
% start S
S[ACT=toward-ceasing] -> CoArisen | Associated
S[ACT=toward-arising] -> Homogeneous | Pervasive | Maturation
S[ACT=opening] -> Antecedent
S[ACT=apprehension] -> Object
S[ACT=non-obstruction] -> Predominance
```

Two causes act toward the present directed to cessation.  
Three toward the future directed to arising.  
Antecedent gives an opening toward arising.  
Object is present apprehension.  
Predominance is non-obstruction in every state.  
Target is not the cause.

## 5. Translation

### Literal Translation

Two causes perform activity toward the ceasing. Three, toward the arising. The other two conditions, by the reverse of that.

### Bhāṣya-informed study translation

> Two causes act toward the present directed to cessation. Three toward the future directed to arising. Antecedent gives an opening toward arising. Object is present apprehension. Predominance is non-obstruction in every state. Target is not the cause.

## 6. Philosophical Translation

> Two causes act toward the present directed to cessation. Three toward the future directed to arising. Antecedent gives an opening toward arising. Object is present apprehension. Predominance is non-obstruction in every state. Target is not the cause.

## 7. Technical Vocabulary

| Term | Rendering |
|---|---|
| nirudhyamāna | Ceasing. Present, directed toward cessation. |
| utpadyamāna | Arising. Future, directed toward arising. |
| avakāśa | Opening. Given by the antecedent. |

## 8. Logical Determination

Two act toward cessation. Three toward arising. Antecedent gives an opening. Object is present apprehension. Predominance is non-obstruction.

## 9. Interpretive Note

Two causes act toward the present directed to cessation. Three toward the future directed to arising. Antecedent gives an opening toward arising. Object is present apprehension. Predominance is non-obstruction in every state.

## 10. OWL++ Seed

```turtle
:CoArisenCause :actsToward :Ceasing .
:AssociatedCause :actsToward :Ceasing .
:HomogeneousCause :actsToward :Arising .
:PervasiveCause :actsToward :Arising .
:MaturationCause :actsToward :Arising .
:AntecedentCondition :givesOpening true .
:ObjectCondition :isPresentApprehension true .
:PredominanceCondition :isNonObstruction true .
```
