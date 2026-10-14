# VAK_4.94 — Non-abandonable Results and Action Constitution

## 1. Sanskrit (Devanāgarī)

```sanskrit
अप्रहेयस्य ते त्वेकं द्वे चत्वारि यथाक्रमम् ।
अयोगविहितं क्लिष्टं विधिभ्रष्टं च केचन ॥ ४.९४ ॥
```

## 2. Sanskrit (IAST)

```iast
apraheyasya te tv ekaṃ dve catvāri yathākramam /
ayogavihitaṃ kliṣṭaṃ vidhibhraṣṭaṃ ca kecana // 4.94 //
```

## 3. Lexical Analysis

```text
apraheyasya | te | tu | ekam | dve | catvāri | yathākramam |
ayogavihitam | kliṣṭam | vidhibhraṣṭam | ca | kecana
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| `apraheyasya` | genitive singular | of action not to be abandoned |
| `te` | nominative masculine plural demonstrative | those same ordered result classes established in 4.93 |
| `tu` | contrastive particle | but; now, in contrast |
| `ekam` | nominative neuter singular | one result |
| `dve` | nominative neuter dual | two results |
| `catvāri` | nominative neuter plural | four results |
| `yathākramam` | indeclinable | respectively, in the established order |
| `ayogavihitam` | nominative neuter singular compound | improperly constituted |
| `kliṣṭam` | nominative neuter singular | afflicted |
| `vidhibhraṣṭam` | nominative neuter singular compound | deviating from prescribed procedure |
| `ca` | coordinating particle | and; also |
| `kecana` | nominative masculine plural pronoun | some teachers; a reported view |

The verse has two movements: it completes the abandonment-status result
matrix, then turns to reported classifications of action as improperly
constituted.

## 4. Grammar

**Action not to be abandoned**

```text
apraheyasya [karmaṇaḥ]
    te [darśana-heyādayo dharmāḥ]
    ekam dve catvāri [phalāni]
    yathākramam
```

> For action not to be abandoned, those same result classes have respectively
> one, two, and four results.

The order remains: dharmas to be abandoned through seeing, dharmas to be
abandoned through cultivation, and dharmas not to be abandoned.

**Reported action-classification**

```text
ayogavihitam [karma]
    kliṣṭam
    vidhibhraṣṭam ca
    kecana [manyante]
```

> Some include afflicted action and action deviating from prescribed
> procedure under the classification “improperly constituted.”

The Bhāṣya distinguishes the explanations offered by different teachers;
they should not be collapsed into one unqualified definition.

## 5. Translation

### Scientific English Rendering

> For action not to be abandoned, those same result classes have respectively
> one, two, and four results. Some classify afflicted action, and also action
> deviating from prescribed procedure, as improperly constituted.

### Bhāṣya-informed study translation

> Action not to be abandoned has, in order, one, two, and four results when
> related to dharmas to be abandoned through seeing, to be abandoned through
> cultivation, and not to be abandoned: the dominant result; the
> activity-produced and dominant results; and the corresponding,
> disconnection, activity-produced, and dominant results. The Bhāṣya explains
> that the repeated “respectively” preserves the order through its abbreviated
> middle statement. The inquiry then distinguishes action properly
> constituted, improperly constituted, and neither. One view classifies
> afflicted action as improperly constituted because it arises from
> non-methodical attention; another also includes action that departs from
> the appropriate procedure. Other teachers identify wholesome action as
> properly constituted and not deviating from procedure, with action outside
> these classes neither properly nor improperly constituted.

## 6. Philosophical Translation

> The final action-status row preserves causal efficacy while excluding
> maturation: action not to be abandoned can still stand in corresponding,
> disconnection, activity-produced, and dominant relations to dharmas not to
> be abandoned. The discussion then shifts from which results an action can
> have to how action is constituted. The Bhāṣya preserves distinct accounts
> of improper constitution—arising from non-methodical attention and
> deviation from appropriate procedure—rather than silently reducing them
> to a single criterion.

## 7. Technical Vocabulary

- **Not to be abandoned** (*apraheya*) — the third class in the abandonment
  matrix; it does not mean causally inactive.
- **Respectively** (*yathākramam*) — preserves the established order of the
  three result-dharma classes.
- **Abbreviated recitation** (*peyāla*) — the Bhāṣya's account of compressed
  repeated material whose omitted members are understood from the stated
  order.
- **Improperly constituted** (*ayogavihita*) — the action classification
  discussed through reported accounts of afflicted origin and procedural
  deviation.
- **Properly constituted** (*yogavihita*) and **neither properly nor
  improperly constituted** — the other classes in the Bhāṣya's threefold
  classification.
- **Afflicted** (*kliṣṭa*) — a predicate distinguished from the separate
  question of procedural conformity.
- **Deviating from prescribed procedure** (*vidhibhraṣṭa*) — departure from
  the manner of conduct specified in the Bhāṣya's examples.

## 8. Logical Determination

Let `M`, `C`, `D`, `P`, and `A` name maturation, corresponding,
disconnection, activity-produced, and dominant results respectively.

**Final abandonment-status row**

| Action status ↓ / Result status → | Seeing-abandonable | Cultivation-abandonable | Not to be abandoned |
|---|---|---|---|
| not to be abandoned | `A` | `P, A` | `C, D, P, A` |

**Completed 4.93–4.94 matrix**

| Action status ↓ / Result status → | Seeing-abandonable | Cultivation-abandonable | Not to be abandoned |
|---|---|---|---|
| seeing-abandonable | `C, P, A` | `M, C, P, A` | `A` |
| cultivation-abandonable | `P, A` | `M, C, P, A` | `D, P, A` |
| not to be abandoned | `A` | `P, A` | `C, D, P, A` |

The counts are `3, 4, 1`; `2, 4, 3`; and `1, 2, 4`. The second half of the
verse opens a different classification and does not add another row to this
matrix.

## 9. Interpretive Note

The completed matrix does not make “not to be abandoned” synonymous with
absence of causal operation: its self-status cell retains four result
relations. The subsequent discussion changes the question from result
membership to the constitution of action. The Bhāṣya reports differing
accounts and preserves their attributions; afflicted origin and procedural
deviation remain distinguishable criteria rather than an imposed,
universalized rule.

## 10. OWL++ Seed

```text
Class: Action
Class: ResultDharma
Class: ResultRelationType
Class: SeeingAbandonable
Class: CultivationAbandonable
Class: NonAbandonable

Rule: NonAbandonableToSeeingAbandonable
  permittedResultTypes = {DominantResult}
Rule: NonAbandonableToCultivationAbandonable
  permittedResultTypes = {ActivityProducedResult, DominantResult}
Rule: NonAbandonableToNonAbandonable
  permittedResultTypes = {CorrespondingResult, DisconnectionResult,
                          ActivityProducedResult, DominantResult}

Class: ActionConstitutionStatus
Class: ProperlyConstitutedAction
  SubClassOf: Action
Class: ImproperlyConstitutedAction
  SubClassOf: Action
Class: NeitherConstitutionClassAction
  SubClassOf: Action
Class: AfflictedAction
  SubClassOf: Action
Class: ProcedurallyDeviantAction
  SubClassOf: Action

Rule: ReportedNonMethodicalAttentionAccount
  afflictedAction arisesFrom nonMethodicalAttention
  → mayBeClassifiedAs ImproperlyConstitutedAction
Rule: ReportedProceduralDeviationAccount
  action deviatesFrom appropriateProcedure
  → mayBeClassifiedAs ImproperlyConstitutedAction
Rule: ReportedWholesomeActionAccount
  wholesomeAction and doesNotDeviateFrom appropriateProcedure
  → mayBeClassifiedAs ProperlyConstitutedAction

Constraint: PreserveReportedViewAttribution
Constraint: DoNotCollapseAfflictedOriginAndProceduralDeviation
```
