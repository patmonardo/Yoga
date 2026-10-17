# VAK_2.63 — Activity Toward Ceasing and Arising

## 1. Sanskrit (Devanāgarī)

```sanskrit
द्वौ हेतू पञ्च च /
ततः अन्याव् तु प्रत्ययौ तद्विपर्ययात् // २.६३ //
```

## 2. Sanskrit (IAST)

```text
dvau hetū pañca ca /
tataḥ anyau tu pratyayau tadviparyayāt // 2.63 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
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

> Of the five causes, two act toward ceasing and three toward arising; the
> other two conditions act in the reverse way.
### Bhāṣya-informed study translation

> Of the five causes, two act toward the ceasing present and three toward
> the arising future. The other two conditions act in the reverse way.
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

**Translation note.** The Bhāṣya identifies the two as co-arisen and
associated and the three as homogeneous, pervasive, and maturation. The
immediately antecedent condition acts toward arising by giving an opening;
the object-condition acts toward ceasing because present consciousness and
factors apprehend. The predominant condition operates in every state through
non-obstruction. A target state is not thereby the cause itself.

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
