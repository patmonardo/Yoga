# VAK_4.93 — Results by Mode of Abandonment

## 1. Sanskrit (Devanāgarī)

```sanskrit
त्रीणि चत्वारि चैकं च दृग्घेयस्य तदादयः ।
ते द्वे चत्वार्यथ त्रीणि भावनाहेयकर्मणः ॥ ४.९३ ॥
```

## 2. Sanskrit (IAST)

```iast
trīṇi catvāri caikaṃ ca dṛg-gheyasya tad-ādayaḥ /
te dve catvāry atha trīṇi bhāvanā-heya-karmaṇaḥ // 4.93 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `trīṇi` | nominative neuter plural | three results |
| `catvāri` | nominative neuter plural | four results |
| `ca` | coordinating particle | and |
| `ekam` | nominative neuter singular | one result |
| `dṛg-gheyasya` | genitive singular compound | of action to be abandoned through seeing |
| `tad-ādayaḥ` | nominative masculine plural compound | result-dharmas beginning with that class |
| `te` | nominative masculine plural demonstrative | those same ordered result-classes |
| `dve` | nominative neuter dual | two results |
| `atha` | connective particle | then; next in the sequence |
| `bhāvanā-heya-karmaṇaḥ` | genitive singular compound | of action to be abandoned through cultivation |

The result classes follow one ordered sequence: to be abandoned through
seeing, to be abandoned through cultivation, and not to be abandoned. The
verse gives result counts for the first two action classes; the Bhāṣya
specifies each result-set.

## 4. Grammar

**Action to be abandoned through seeing**

```text
dṛg-gheyasya [karmaṇaḥ]
    tad-ādayaḥ [dharmāḥ]
    trīṇi catvāri ekam [phalāni]
```

> For action to be abandoned through seeing, the result-dharmas beginning
> with that class are respectively three, four, and one results.

**Action to be abandoned through cultivation**

```text
bhāvanā-heya-karmaṇaḥ
    te [tad-ādayā dharmāḥ]
    dve catvāri atha trīṇi [phalāni]
```

> For action to be abandoned through cultivation, those same result-classes
> are respectively two, four, and three results.

`Tad-ādayaḥ` and `te` preserve the same target sequence across both clauses.

## 5. Translation

### Literal

> For action to be abandoned through seeing, result-dharmas beginning with
> that class are respectively three, four, and one results. For action to be
> abandoned through cultivation, those same result-classes are respectively
> two, four, and three results.

### Bhāṣya-informed

> Action to be abandoned through seeing has result-dharmas to be abandoned
> through seeing as three results, excluding maturation and disconnection;
> result-dharmas to be abandoned through cultivation as four results,
> excluding disconnection; and dharmas not to be abandoned as one result:
> the dominant result. Action to be abandoned through cultivation has
> result-dharmas to be abandoned through seeing as two results:
> activity-produced and dominant; result-dharmas to be abandoned through
> cultivation as four results, excluding disconnection; and dharmas not to
> be abandoned as three results, excluding maturation and the corresponding
> result.

## 6. Philosophical Translation

> For action to be abandoned through seeing, result-dharmas beginning with that class are respectively three, four, and one results. For action to be abandoned through cultivation, those same result-classes are respectively two, four, and three results.

## 7. Technical Vocabulary

- **Action** — the rendering of *karma/karman*.
- **To be abandoned through seeing** (*darśana-heya*, *dṛg-heya*) — the
  first abandonment-status class.
- **To be abandoned through cultivation** (*bhāvanā-heya*) — the second
  abandonment-status class.
- **Not to be abandoned** (*apraheya*) — the third class in the ordered
  target sequence.
- **Maturation result** (*vipāka-phala*), **corresponding result**
  (*niṣyanda-phala*), **disconnection-result** (*visaṃyoga-phala*),
  **activity-produced result** (*puruṣakāra-phala*), and **dominant result**
  (*adhipati-phala*) — the five result-relations named in the Bhāṣya.

## 8. Logical Determination

Let `M`, `C`, `D`, `P`, and `A` name maturation, corresponding,
disconnection, activity-produced, and dominant results respectively.

| Action status ↓ / Result status → | Seeing-abandonable | Cultivation-abandonable | Not to be abandoned |
|---|---|---|---|
| seeing-abandonable | `C, P, A` | `M, C, P, A` | `A` |
| cultivation-abandonable | `P, A` | `M, C, P, A` | `D, P, A` |

Numerically, the two rows are `3, 4, 1` and `2, 4, 3`. The first and last
result classes are explicit in the order; the Bhāṣya supplies the memberships
of each cell.

## 9. Interpretive Note

This verse begins the result matrix indexed by abandonment status. It
classifies the causal relations of action and resulting dharmas; it does not
identify the action itself with the Path operation that abandons a dharma.
The Bhāṣya's exclusions and named results show why the numerical sequence is
not enough on its own: each count stands for a specific set of relations.

### Former Philosophical Translation

> The mode by which an action is to be abandoned does not alone determine
> its result-profile. The result-dharma's own abandonment status also
> matters: the ordered source-target pair selects the available result
> relations. The same count can therefore conceal different causal
> memberships, and reversing the two statuses need not preserve the
> relation.

## 10. OWL++ Seed

```text
Class: Action
Class: ResultDharma
Class: AbandonmentStatus
Class: SeeingAbandonable
  SubClassOf: AbandonmentStatus
Class: CultivationAbandonable
  SubClassOf: AbandonmentStatus
Class: NonAbandonable
  SubClassOf: AbandonmentStatus
Class: ResultRelationType
Class: MaturationResult
  SubClassOf: ResultRelationType
Class: CorrespondingResult
  SubClassOf: ResultRelationType
Class: DisconnectionResult
  SubClassOf: ResultRelationType
Class: ActivityProducedResult
  SubClassOf: ResultRelationType
Class: DominantResult
  SubClassOf: ResultRelationType

Rule: SeeingAbandonableToSeeingAbandonable
  permittedResultTypes = {CorrespondingResult,
                          ActivityProducedResult, DominantResult}
Rule: SeeingAbandonableToCultivationAbandonable
  permittedResultTypes = {MaturationResult, CorrespondingResult,
                          ActivityProducedResult, DominantResult}
Rule: SeeingAbandonableToNonAbandonable
  permittedResultTypes = {DominantResult}
Rule: CultivationAbandonableToSeeingAbandonable
  permittedResultTypes = {ActivityProducedResult, DominantResult}
Rule: CultivationAbandonableToCultivationAbandonable
  permittedResultTypes = {MaturationResult, CorrespondingResult,
                          ActivityProducedResult, DominantResult}
Rule: CultivationAbandonableToNonAbandonable
  permittedResultTypes = {DisconnectionResult,
                          ActivityProducedResult, DominantResult}

Constraint: ActionAndResultAbandonmentStatusesAreOrdered
Constraint: ResultCountsAreDerivedFromResultMembership
```
