# VAK_4.93

## 1. Sanskrit — Devanāgarī

त्रीणि चत्वारि चैकं च दृग्घेयस्य तदादयः ।
ते द्वे चत्वार्यथ त्रीणि भावनाहेयकर्मणः ॥ ४.९३ ॥

## 2. Sanskrit — IAST

**trīṇi catvāri caikaṃ ca dṛg-gheyasya tad-ādayaḥ |**  
**te dve catvāry atha trīṇi bhāvanā-heya-karmaṇaḥ || 4.93 ||**

## 3. Padaccheda

`trīṇi / catvāri / ca / ekam / ca / dṛk-heyasya / tad-ādayaḥ / te / dve / catvāri / atha / trīṇi / bhāvanā-heya-karmaṇaḥ`

## 4. Grammar

- `dṛg-gheyasya`: genitive singular, “of karma abandonable through seeing.”
- `tad-ādayaḥ`: “the classes beginning with that,” fixing the ordered target series: seeing-abandonable, cultivation-abandonable, non-abandonable.
- `te`: “those same,” carrying the target series into the second half.
- `bhāvanā-heya-karmaṇaḥ`: “of karma abandonable through cultivation.”

## 5. Literal Translation

For karma abandonable through seeing, the result-dharmas beginning with that class admit respectively three, four, and one result-relations. For karma abandonable through cultivation, those same classes admit respectively two, four, and three.

## 6. Philosophical Translation

The causal range of activity is determined by the mode under which source and result stand in relation to abandonment. Karma removable through seeing and karma removable through cultivation possess distinct distributions across seeing-abandonable, cultivation-abandonable, and non-abandonable result-dharmas.

## 7. Technical Vocabulary

- `darśana-heya` / `dṛg-heya`: abandonable through seeing.
- `bhāvanā-heya`: abandonable through cultivation.
- `apraheya`: non-abandonable; implied as the third target class and completed in VAK_4.94.
- `heya`: to be abandoned.

## 8. Doctrinal Determination

For seeing-abandonable karma:

| Result-dharma class | Result-relations |
|---|---:|
| Seeing-abandonable | 3 |
| Cultivation-abandonable | 4 |
| Non-abandonable | 1 |

For cultivation-abandonable karma:

| Result-dharma class | Result-relations |
|---|---:|
| Seeing-abandonable | 2 |
| Cultivation-abandonable | 4 |
| Non-abandonable | 3 |

Exact membership of each counted set remains for the Bhāṣya pass.

## 9. Logical Determination

Define `C(sourceStatus, targetStatus)` as the number of admissible technical result-types.

- `C(SeeingAbandonable, SeeingAbandonable) = 3`
- `C(SeeingAbandonable, CultivationAbandonable) = 4`
- `C(SeeingAbandonable, NonAbandonable) = 1`
- `C(CultivationAbandonable, SeeingAbandonable) = 2`
- `C(CultivationAbandonable, CultivationAbandonable) = 4`
- `C(CultivationAbandonable, NonAbandonable) = 3`

The matrix is directed; reversing source and target is not licensed.

## 10. Light Organon Interpretation

At the Kernel level:

```text
AbandonmentResultRule {
    sourceAbandonmentStatus
    targetAbandonmentStatus
    permittedResultTypes[]
    resultTypeCount
}
```

Intrinsic classification is necessary, but ordered relational position determines operative compatibility.

## 11. OWL++ Seed

```ttl
vak:SeeingToSeeing vak:hasResultCardinality 3 .
vak:SeeingToCultivation vak:hasResultCardinality 4 .
vak:SeeingToNonAbandonable vak:hasResultCardinality 1 .
vak:CultivationToSeeing vak:hasResultCardinality 2 .
vak:CultivationToCultivation vak:hasResultCardinality 4 .
vak:CultivationToNonAbandonable vak:hasResultCardinality 3 .
```

## 12. Commit Note

- begin the abandonment-status result matrix
- assign 3/4/1 to seeing-abandonable karma
- assign 2/4/3 to cultivation-abandonable karma
- preserve the fixed target order
- treat source and target as directed roles
- continue the matrix into VAK_4.94