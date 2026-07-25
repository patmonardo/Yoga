# VAK 4.92

## 1. Sanskrit — Devanāgarī

धर्माः शैक्षादिका एकं फलं त्रीण्यपि च द्वयम् ।  
ताभ्यामन्यस्य शैक्षाद्या द्वे द्वे पञ्च फलानि च ॥ ४.९२ ॥

## 2. Sanskrit — IAST

**dharmāḥ śaikṣādikā ekaṃ phalaṃ trīṇy api ca dvayam |**  
**tābhyām anyasya śaikṣādyā dve dve pañca phalāni ca || 4.92 ||**

The verse completes the path-status classification begun in VAK 4.91. The statuses are trainee (*śaikṣa*), beyond training (*aśaikṣa*), and neither.

## 3. Padaccheda

`dharmāḥ | śaikṣa-ādikāḥ | ekam | phalam | trīṇi | api | ca | dvayam | tābhyām | anyasya | śaikṣa-ādyāḥ | dve | dve | pañca | phalāni | ca`

Continuing from VAK 4.91:

- for beyond-training karma, trainee, beyond-training, and neither result-dharmas stand in respectively one, three, and two result-relations;
- for karma other than trainee and beyond-training, those three result classes stand in respectively two, two, and five result-relations.

## 4. Grammar

- **śaikṣādikāḥ** — the classes beginning with trainee, in the order trainee, beyond-training, neither.
- **ekam phalam** — one result.
- **trīṇi** — three results.
- **dvayam** — a pair, two results.
- **tābhyām anyasya** — of that which is other than those two, namely neither trainee nor beyond-training.
- **dve dve** — two and two respectively.
- **pañca phalāni** — five results.

## 5. Literal Translation

For the karma of one beyond training, the dharmas beginning with the trainee class constitute respectively one result, three results, and two. For karma other than those two, the classes beginning with the trainee constitute respectively two, two, and five results.

## 6. Philosophical Translation

The causal relation between activity and result is determined by the respective path-status of both terms. Activity belonging to one beyond training does not relate uniformly to trainee, beyond-training, and neither dharmas; each target class admits a different number of result-relations. Activity belonging to neither status likewise has its own ordered distribution. Path-status therefore becomes causally effective only within the ordered relation of source and result.

## 7. Technical Vocabulary

- **śaikṣa** — trainee; one for whom noble training remains.
- **aśaikṣa** — beyond training; one for whom the required training is complete.
- **tābhyām anya** — other than those two; neither trainee nor beyond-training.
- **phala** — one of the five technical result-relations: maturation, outflow, disconnection, activity-produced, or dominant result.

## 8. Doctrinal Determination

For beyond-training karma:

| Result-dharma status | Result-relations |
|---|---:|
| Trainee | 1 |
| Beyond training | 3 |
| Neither | 2 |

For karma belonging to neither status:

| Result-dharma status | Result-relations |
|---|---:|
| Trainee | 2 |
| Beyond training | 2 |
| Neither | 5 |

The five in the final cell means that the entire fivefold result range is admissible for that ordered source-target relation; it does not mean every individual karma necessarily produces five separate results.

## 9. Logical Determination

Let `C(Sk, Sr)` be the number of admissible technical result-types for source status `Sk` and result status `Sr`.

```text
C(BeyondTraining, Trainee) = 1
C(BeyondTraining, BeyondTraining) = 3
C(BeyondTraining, Neither) = 2

C(Neither, Trainee) = 2
C(Neither, BeyondTraining) = 2
C(Neither, Neither) = 5
```

The matrix is directed: `C(x,y)` does not imply `C(y,x)`. Equal cardinality also does not imply identical result-type membership.

## 10. Light Organon Interpretation

At the Kernel level, this is a directed relational table:

```text
PathStatusResultRule {
    sourceStatus
    targetStatus
    permittedResultTypes[]
    resultTypeCount
}
```

The count should be derived from the permitted set. Classification of source and target does not itself determine the relation; the ordered pair must be evaluated.

## 11. OWL++ Seed

```ttl
vak:VAK_4_92 a vak:Karika ;
    vak:continues vak:VAK_4_91 ;
    vak:hasTopic vak:PathStatusResultMatrix .

vak:BeyondTrainingToTrainee vak:hasResultCardinality 1 .
vak:BeyondTrainingToBeyondTraining vak:hasResultCardinality 3 .
vak:BeyondTrainingToNeither vak:hasResultCardinality 2 .
vak:NeitherToTrainee vak:hasResultCardinality 2 .
vak:NeitherToBeyondTraining vak:hasResultCardinality 2 .
vak:NeitherToNeither vak:hasResultCardinality 5 .
```

## 12. Commit Note

- complete the path-status result matrix begun in VAK 4.91;
- assign 1/3/2 result-relations for beyond-training karma across trainee/beyond-training/neither targets;
- assign 2/2/5 for neither-status karma;
- preserve source and result as distinct ordered roles;
- distinguish result-set cardinality from exact membership;
- model the table as a directed Kernel relation.
