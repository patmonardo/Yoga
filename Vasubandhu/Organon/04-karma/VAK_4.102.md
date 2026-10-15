# VAK_4.102 — Six Exclusions from Dharma Chakra Division

## 1. Sanskrit (Devanāgarī)

```sanskrit
आदावन्तेऽर्बुदात्पूर्वं युगाच्चोपरते मुनौ ।
सीमायां चाप्यबद्धायां चक्रभेदो न जायते ॥ ४.१०२ ॥
```

## 2. Sanskrit (IAST)

```iast
ādāv ante 'rbudāt pūrvaṃ yugāc coparate munau /
sīmāyāṃ cāpy abaddhāyāṃ cakrabhedo na jāyate // 4.102 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `ādau` | locative singular used adverbially | at the beginning of the Dharma Chakra's operation |
| `ante` | locative singular used adverbially | at its end |
| `arbudāt` | ablative neuter singular | before the `arbuda`, glossed by the Bhāṣya as defects of discipline and view |
| `pūrvam` | indeclinable adverb | before; governs `arbudāt` and is carried forward to `yugāt` |
| `yugāt` | ablative neuter singular | before the pair, identified by the Bhāṣya as the foremost pair of disciples |
| `ca` | indeclinable particle | and |
| `uparate` | locative singular past participle | when the Sage has passed away |
| `munau` | locative masculine singular | with `uparate`, forming a locative absolute |
| `sīmāyām` | locative feminine singular | while the communal boundary is in that condition |
| `api` | indeclinable particle | also; emphasizes the boundary condition |
| `abaddhāyām` | locative feminine singular past participle | while unbound or not formally established |
| `cakra-bhedaḥ` | nominative masculine singular compound | division of the Dharma Chakra |
| `na` | negative particle | negates the arising |
| `jāyate` | third-person singular present middle | arises, occurs |

## 4. Grammar

The verse applies one negative predicate to a sequence of six conditions:

```text
ādau
ante
arbudāt pūrvam
yugāt pūrvam
uparate munau
sīmāyām abaddhāyām

in each:
    cakra-bhedaḥ na jāyate
```

The Bhāṣya interprets the first two as phases of the Dharma Chakra's
operation, resolves the two ablative phrases through discipline/view and
the foremost pair of disciples, and explains the final locative absolute
as the absence of a formally established common boundary.

The Bhāṣya adds a final qualification not stated in the verse: even a
formally bound boundary does not by itself entail division; the occurrence
depends on action.

## 5. Translation

### Literal

> At the beginning, at the end, before the excrescence, before the pair,
> when the Sage has passed away, and while the boundary is unbound, division
> of the wheel does not arise.

### Bhāṣya-informed

> Division of the Dharma Chakra does not arise at the beginning or end,
> before defects of discipline and view have arisen, before the foremost
> pair of disciples has appeared, after the Sage has passed away, or while
> the communal boundary remains unbound.

The commentary explains that the beginning and end are times when the
Saṅgha is `ekarasa`, one in tenor; that the two `arbuda` are defects of
discipline and view; and that the pair is the foremost pair of disciples.
It further says that division does not arise after the Sage has passed
away because no rival remains, or before a common boundary is established.
Its concluding qualification is that actual division depends on action.

## 6. Philosophical Translation

> At the beginning, at the end, before the excrescence, before the pair, when the Sage has passed away, and while the boundary is unbound, division of the wheel does not arise.

## 7. Technical Vocabulary

- **`Cakrabheda`** — division of the Dharma Chakra, the specific collective
  rupture discussed in the preceding verses.
- **`Ekarasa`** — “one in tenor” or “of one flavor”; the Bhāṣya's
  description of the Saṅgha at the beginning and end.
- **`Arbuda`** — literally an excrescence; the Bhāṣya identifies
  `śīlārbuda` and `dṛṣṭyarbuda`, defects of discipline and view.
- **`Yuga` / `śrāvakāgrayuga`** — the pair of foremost disciples. The
  Bhāṣya connects their presence with the possibility of reconciliation,
  while the precise force of `bhinnanyāyaparivāsāt` remains uncertain.
- **`Uparate munau`** — after the Sage has passed away; the Bhāṣya says
  the relevant rival is then absent.
- **`Sīmā`** — the common communal boundary within which two parties can
  stand as one divided Saṅgha.
- **`Karmādhīnatvāt`** — “because it depends on action.” This is the
  Bhāṣya's final qualification: the listed background conditions do not
  by themselves produce division.

## 8. Logical Determination

```text
Exclusions from cakrabheda:
    beginning of the Dharma Chakra's operation
    end of the dispensation
    before discipline and view defects arise
    before the foremost pair of disciples appears
    after the Sage has passed away
    before a common sīmā is established

Even when those exclusions do not apply:
    established conditions do not entail actual division
    actual occurrence remains dependent on action
```

The six conditions delimit when this form of division cannot arise. The
Bhāṣya's final sentence blocks the converse inference from an established
boundary to an actual `cakrabheda`.

## 9. Interpretive Note

The passage distinguishes conditions that make this division unavailable
from the action on which its actual occurrence depends. It is therefore a
useful causal-pipeline example: historical phase, internal condition,
agents, and common boundary constrain the possible event, but do not
mechanically produce it.

The Bhāṣya names action-dependence with `karmādhīnatvāt`; it does not name
*cetanā* or specify the volitional structure of that action. The rendering
therefore preserves “action-dependent” without filling in an unstated
volition theory.

The source unit is `[262|10]–[262|19]`. It stops before the new question
about why killing parents and related actions count as actions of
immediate result at `[262|20]`. The difficult phrase concerning the
foremost pair is retained as uncertain.

### Former Philosophical Translation

> The Dharma Chakra's division is excluded where its historical or
> institutional conditions are absent: before internal defects have
> appeared, before the agents associated with reconciliation are present,
> after the Teacher has passed away, and before one common boundary can
> hold the two parties. Even when those conditions are available, division
> is not automatic; its occurrence remains action-dependent.

## 10. OWL++ Seed

```text
Class: DharmaChakraDivision
Class: DisciplineDefect
Class: ViewDefect
Class: ForemostDisciplePair
Class: LivingTeacher
Class: BoundSīmā
Class: DivisiveAction

Rule: ExcludedCakrabheda
  when = AnyOf(
    BeginningOfDharmaChakra,
    EndOfDispensation,
    BeforeDisciplineOrViewDefect,
    BeforeForemostDisciplePair,
    AfterSageHasPassedAway,
    BeforeSīmāIsBound
  )
  result = CakrabhedaDoesNotArise

Rule: ActionDependentOccurrence
  backgroundConditions = ConditionsForPossibleCakrabheda
  actualOccurrence = DependsOn(DivisiveAction)

Constraint: BoundSīmāAloneDoesNotEntailCakrabheda
```
