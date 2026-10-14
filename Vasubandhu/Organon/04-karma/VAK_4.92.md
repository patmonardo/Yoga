# VAK_4.92 — Completion of the Training-status Result Matrix

## 1. Sanskrit (Devanāgarī)

```sanskrit
धर्माः शैक्षादिका एकं फलं त्रीण्यपि च द्वयम् ।
ताभ्यामन्यस्य शैक्षाद्या द्वे द्वे पञ्च फलानि च ॥ ४.९२ ॥
```

## 2. Sanskrit (IAST)

```iast
dharmāḥ śaikṣādikā ekaṃ phalaṃ trīṇy api ca dvayam /
tābhyām anyasya śaikṣādyā dve dve pañca phalāni ca // 4.92 //
```

## 3. Lexical Analysis

```text
dharmāḥ | śaikṣa-ādikāḥ | ekam | phalam | trīṇi | api | ca | dvayam |
tābhyām | anyasya | śaikṣa-ādyāḥ | dve | dve | pañca | phalāni | ca
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| `dharmāḥ` | nominative masculine plural | result-dharmas in the ordered classification |
| `śaikṣa-ādikāḥ` | nominative masculine plural compound | classes beginning with trainee |
| `ekam phalam` | nominative neuter singular | one result |
| `trīṇi` | nominative neuter plural | three results |
| `api ca` | additive coordination | and also |
| `dvayam` | nominative neuter singular collective | a pair; two results |
| `tābhyām` | ablative dual pronoun | other than those two, trainee and beyond-training |
| `anyasya` | genitive singular | belonging to the other action-class, neither status |
| `śaikṣa-ādyāḥ` | nominative masculine plural compound | result-dharmas in the order trainee, beyond training, neither |
| `dve dve` | distributive neuter duals | two results for each of the first two classes |
| `pañca phalāni` | nominative neuter plural | five results for the third class |

The opening result-class sequence continues the beyond-training action clause
begun in 4.91. The Bhāṣya identifies the three classes and the exact result
memberships. The second half specifies action belonging to neither trainee
nor one beyond training.

## 4. Grammar

**Beyond-training action**

```text
aśaikṣasya karmaṇaḥ
    dharmāḥ śaikṣādikāḥ
    ekam phalam, trīṇi, dvayam
```

> For action belonging to one beyond training, result-dharmas beginning with
> the trainee class are respectively one, three, and two results.

The ordered result classes are trainee, beyond training, and neither. The
Bhāṣya specifies which result-relations constitute each count.

**Action other than those two statuses**

```text
śaikṣāśaikṣābhyām anyasya [karmaṇaḥ]
    śaikṣādyāḥ [dharmāḥ]
    dve dve pañca phalāni
```

> For action belonging to neither trainee nor one beyond training, the same
> ordered result classes have respectively two, two, and five results.

`Tābhyām anyasya` refers to action other than action of the two named
training-status classes; the Bhāṣya identifies this as neither-status action.

## 5. Translation

### Scientific English Rendering

> For action belonging to one beyond training, dharmas beginning with the
> trainee class are respectively one, three, and two results. For action
> belonging to neither trainee nor one beyond training, the same ordered
> classes are respectively two, two, and five results.

### Bhāṣya-informed study translation

> For beyond-training action, trainee dharmas stand as one result: the
> dominant result. Dharmas belonging to one beyond training stand as three
> results, with maturation and disconnection excluded; the corresponding,
> activity-produced, and dominant results remain. Dharmas belonging to
> neither trainee nor one beyond training stand as two results:
> activity-produced and dominant. For action belonging to neither trainee
> nor one beyond training, trainee dharmas stand as two results:
> activity-produced and dominant. Dharmas belonging to one beyond training
> stand in the same way. Dharmas belonging to neither status stand as all
> five results: maturation, corresponding, disconnection, activity-produced,
> and dominant.

## 6. Philosophical Translation

> The result-profile of action belonging to one beyond training is
> asymmetrical across the three result-status classes: one result, three,
> and two. Action belonging to neither status has a different profile: two,
> two, and five. These counts summarize distinct memberships in the
> five-result classification; equal counts do not imply identical causal
> relations, and the largest count does not itself rank a Path status.

## 7. Technical Vocabulary

- **Action** — the rendering of *karma/karman*; no additional volition is
  inserted where this verse does not name *cetanā*.
- **Result** — the rendering of *phala* in this classification.
- **Trainee** (*śaikṣa*) — the first training-status class.
- **Beyond training** (*aśaikṣa*) — the second training-status class; not
  “untrained.”
- **Neither status** (*naivaśaikṣa-nāśaikṣa*) — neither trainee nor beyond
  training.
- **Maturation result** (*vipāka-phala*), **corresponding result**
  (*niṣyanda-phala*), **disconnection-result** (*visaṃyoga-phala*),
  **activity-produced result** (*puruṣakāra-phala*), and **dominant result**
  (*adhipati-phala*) — the five result-relations specified by the Bhāṣya.

## 8. Logical Determination

Let `M`, `C`, `D`, `P`, and `A` name maturation, corresponding,
disconnection, activity-produced, and dominant results respectively.

**Rows specified in this verse**

| Action status ↓ / Result status → | Trainee | Beyond training | Neither |
|---|---|---|---|
| beyond training | `A` | `C, P, A` | `P, A` |
| neither | `P, A` | `P, A` | `M, C, D, P, A` |

**Completed 4.91–4.92 matrix**

| Action status ↓ / Result status → | Trainee | Beyond training | Neither |
|---|---|---|---|
| trainee | `C, P, A` | `C, P, A` | `D, P, A` |
| beyond training | `A` | `C, P, A` | `P, A` |
| neither | `P, A` | `P, A` | `M, C, D, P, A` |

The numerical projection is `3, 3, 3` for trainee action, `1, 3, 2` for
beyond-training action, and `2, 2, 5` for neither-status action. Result
membership is directed: reversing action and result status does not preserve
the set.

## 9. Interpretive Note

The completed matrix makes action-status and result-status jointly
determinative. The Bhāṣya gives an exact set of result-relations for each
ordered pair; a count is only a compressed statement of that set. In the
Kośa's wider cognitive movement, Discriminative Cognition joins and governs
Perception and Conception; this matrix articulates practical causal
differentiation through action and result-status. Its five-result
neither-to-neither cell expresses the breadth of that classified relation,
not a ranking of spiritual worth.

## 10. OWL++ Seed

```text
Class: Action
Class: ResultDharma
Class: ResultRelationType
Class: TraineeAction
  SubClassOf: Action
Class: BeyondTrainingAction
  SubClassOf: Action
Class: NeitherTrainingStatusAction
  SubClassOf: Action
Class: TraineeDharma
  SubClassOf: ResultDharma
Class: BeyondTrainingDharma
  SubClassOf: ResultDharma
Class: NeitherTrainingStatusDharma
  SubClassOf: ResultDharma

Class: CorrespondingResult
  SubClassOf: ResultRelationType
Class: DisconnectionResult
  SubClassOf: ResultRelationType
Class: ActivityProducedResult
  SubClassOf: ResultRelationType
Class: DominantResult
  SubClassOf: ResultRelationType
Class: MaturationResult
  SubClassOf: ResultRelationType

ObjectProperty: hasActionTrainingStatus
  Domain: Action
ObjectProperty: hasResultTrainingStatus
  Domain: ResultDharma

Rule: BeyondTrainingToTrainee
  permittedResultTypes = {DominantResult}
Rule: BeyondTrainingToBeyondTraining
  permittedResultTypes = {CorrespondingResult,
                          ActivityProducedResult, DominantResult}
Rule: BeyondTrainingToNeither
  permittedResultTypes = {ActivityProducedResult, DominantResult}
Rule: NeitherToTrainee
  permittedResultTypes = {ActivityProducedResult, DominantResult}
Rule: NeitherToBeyondTraining
  permittedResultTypes = {ActivityProducedResult, DominantResult}
Rule: NeitherToNeither
  permittedResultTypes = {MaturationResult, CorrespondingResult,
                          DisconnectionResult, ActivityProducedResult,
                          DominantResult}

Constraint: ResultCountsAreDerivedFromResultTypeMembership
Constraint: ReversingTrainingStatusDoesNotPreserveResultMembership
```
