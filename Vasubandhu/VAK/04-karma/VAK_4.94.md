# VAK_4.94

## 1. Sanskrit — Devanāgarī

अप्रहेयस्य ते त्वेकं द्वे चत्वारि यथाक्रमम् ।
अयोगविहितं क्लिष्टं विधिभ्रष्टं च केचन ॥ ४.९४ ॥

## 2. Sanskrit — IAST

**apraheyasya te tv ekaṃ dve catvāri yathākramam |**  
**ayoga-vihitaṃ kliṣṭaṃ vidhi-bhraṣṭaṃ ca kecana || 4.94 ||**

## 3. Padaccheda

apraheyasya / te / tu / ekam / dve / catvāri / yathākramam / ayoga-vihitam / kliṣṭam / vidhi-bhraṣṭam / ca / kecana

## 4. Grammar

- **apraheyasya**: “of non-abandonable karma.”
- **te**: “those same,” referring to the three target classes fixed in 4.93.
- **ekam, dve, catvāri**: one, two, four results.
- **yathākramam**: respectively, in the established order.
- **ayoga-vihitam**: provisionally, improperly constituted or undertaken without proper application.
- **kliṣṭam**: afflicted.
- **vidhi-bhraṣṭam**: deviating from prescribed procedure.
- **kecana**: some teachers; a reported view.

## 5. Literal Translation

For non-abandonable karma, those result classes are respectively one, two, and four. Some regard what is improperly performed as afflicted and as deviating from the prescribed procedure.

## 6. Philosophical Translation

Non-abandonable karma has its own directed range of relations to seeing-abandonable, cultivation-abandonable, and non-abandonable result-dharmas: one, two, and four respectively. The verse then records a view according to which defective activity is marked by affliction and deviation from proper procedure.

## 7. Technical Vocabulary

- **apraheya**: non-abandonable.
- **darśana-heya**: abandonable through seeing.
- **bhāvanā-heya**: abandonable through cultivation.
- **ayoga**: improper application or failure of appropriate conjunction; exact sense awaits Bhāṣya.
- **kliṣṭa**: afflicted.
- **vidhi-bhraṣṭa**: fallen away from prescribed procedure.
- **kecana**: some teachers.

## 8. Doctrinal Determination

For non-abandonable karma:

| Result-dharma class | Result-relations |
|---|---:|
| Seeing-abandonable | 1 |
| Cultivation-abandonable | 2 |
| Non-abandonable | 4 |

Together with 4.93, the completed matrix is:

| Source karma ↓ / Result dharma → | Seeing-abandonable | Cultivation-abandonable | Non-abandonable |
|---|---:|---:|---:|
| Seeing-abandonable | 3 | 4 | 1 |
| Cultivation-abandonable | 2 | 4 | 3 |
| Non-abandonable | 1 | 2 | 4 |

The second half is explicitly a reported view and should remain provisional until the Bhāṣya identifies its exact scope.

## 9. Logical Determination

Let `C(Hk,Hr)` be the number of admissible technical result-types for source abandonment-status `Hk` and result abandonment-status `Hr`.

- `C(NonAbandonable, SeeingAbandonable) = 1`
- `C(NonAbandonable, CultivationAbandonable) = 2`
- `C(NonAbandonable, NonAbandonable) = 4`

The relation is directed: in general, `C(x,y) ≠ C(y,x)`.

## 10. Light Organon Interpretation

The Kernel should represent the completed table as a directed compatibility relation:

```text
AbandonmentResultRule {
    sourceStatus
    targetStatus
    permittedResultTypes[]
    resultTypeCount
}
```

Affliction-status and procedural conformity should remain distinct fields pending Bhāṣya clarification.

## 11. OWL++ Seed

```ttl
vak:NonAbandonableToSeeing
    vak:hasSourceStatus vak:NonAbandonable ;
    vak:hasTargetStatus vak:SeeingAbandonable ;
    vak:hasResultCardinality 1 .

vak:NonAbandonableToCultivation
    vak:hasSourceStatus vak:NonAbandonable ;
    vak:hasTargetStatus vak:CultivationAbandonable ;
    vak:hasResultCardinality 2 .

vak:NonAbandonableToNonAbandonable
    vak:hasSourceStatus vak:NonAbandonable ;
    vak:hasTargetStatus vak:NonAbandonable ;
    vak:hasResultCardinality 4 .
```

## 12. Commit Note

VAK_4.94 — Complete the abandonment-status result matrix

- assign 1/2/4 result-relations to non-abandonable karma
- preserve the established target order
- complete the directed 3×3 abandonment-status matrix
- record the reported view concerning `ayoga-vihita`
- keep afflicted status and procedural deviation distinct pending Bhāṣya analysis
