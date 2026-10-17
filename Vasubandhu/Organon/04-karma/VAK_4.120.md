# VAK 4.120 — Performed and Accumulated Action

## 1. Sanskrit (Devanāgarī)

```sanskrit
संचेतनसमाप्तिभ्यां निष्कौकृत्यविपक्षतः ।
परिवाराद्विपाकाच्च कर्मोपचितमुच्यते ॥ ४.१२० ॥
```

## 2. Sanskrit (IAST)

```iast
saṃcetanasamāptibhyāṃ niṣkaukṛtyavipakṣataḥ /
parivārād vipākāc ca karmopacitam ucyate // 4.120 //
```

The Bhāṣya counts five conditions: deliberate intention, completion,
absence of remorse and counteraction, accompaniment, and maturation.
Absence of remorse and counteraction forms one combined condition.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `saṃcetana-samāptibhyām` | instrumental dual compound | through deliberate intention and completion |
| `niṣkaukṛtya-vipakṣataḥ` | ablatival compound | through absence of remorse and an opposing factor |
| `parivārāt` | ablative singular | through accompaniment |
| `vipākāt` | ablative singular | through determination toward maturation |
| `ca` | indeclinable conjunction | and |
| `karma` | nominative singular neuter | action |
| `upacitam` | nominative singular neuter past passive participle | accumulated |
| `ucyate` | third-person singular present passive of `√vac` | is called |

The Bhāṣya's fivefold analysis separates the instrumental dual into
`saṃcetanā` and `samāpti`, and treats lack of remorse together with lack
of an opposing factor as one condition.

## 4. Grammar

The five conditions are:

```text
1. saṃcetanā
2. samāpti
3. niṣkaukṛtya + niṣpratipakṣa
4. parivāra
5. vipākadāna-niyama
```

The main predication contrasts a status of action:

```text
karma upacitam ucyate
    action is called accumulated
```

The Bhāṣya frames the distinction by opening with `kṛtaṃ copacitaṃ ca
karmocyate` and concludes that action can be done without being
accumulated. Thus occurrence alone does not entail `upacita`.

## 5. Translation

### Literal Translation
> An action is called accumulated through deliberate intention, completion,
> absence of remorse and counteraction, accompaniment, and determination
> toward maturation.

### Bhāṣya-informed study translation

> An action is called accumulated through deliberate intention, completion, absence
> of remorse and counteraction, accompaniment, and determination toward maturation.

## 6. Philosophical Translation

> An action is called accumulated through deliberate intention, completion, absence of remorse and counteraction, accompaniment, and determination toward maturation.

## 7. Technical Vocabulary

- **`Kṛta`** — done or performed. Its occurrence does not by itself make
  the action accumulated.
- **`Upacita`** — accumulated; the stronger status distinguished from
  merely having been done.
- **`Saṃcetanā`** — deliberate or considered action. The Bhāṣya contrasts
  it with action done without prior awareness or suddenly.
- **`Samāpti`** — completion. The required number of misconducts or
  action-courses varies in the Bhāṣya's examples.
- **`Niṣkaukṛtya` / `nirvipratisāra`** — absence of remorse.
- **`Pratipakṣa`** — opposing or counteracting factor; its absence is
  paired with absence of remorse as one condition.
- **`Parivāra`** — accompaniment. The Bhāṣya states that unwholesome
  action is accompanied by unwholesome factors and directs that wholesome
  action be treated correspondingly.
- **`Vipākadāna-niyama`** — determination that the action gives
  maturation.
- **`Vipāka`** — maturation, not a generic effect or an automatic reward.

## 8. Logical Determination

```text
Kṛta(action) does not entail Upacita(action)
```

The Bhāṣya specifies five conditions for accumulated status:

```text
deliberate action
completion of the relevant course
absence of remorse and opposing factor
congruent accompaniment
determination toward maturation
```

Completion is threshold-sensitive:

```text
required course incomplete → done, not accumulated
required course complete   → accumulated
```

The examples allow that a single misconduct or action-course may suffice
for one person, while more may be required in another case. This is not a
fixed numerical rule for all actions.

## 9. Interpretive Note

**Translation note.** The Bhāṣya's completion examples and its application to wholesome action
are preserved in the paired study. The informed translation also included: The Bhāṣya says deliberate action is done after consideration, not without prior awareness or suddenly. Completion is relative to the number of misconducts or action-courses required in a particular case: until that course is complete, action has been done but is not accumulated; when complete, it is accumulated. The other conditions are that the action is without remorse and without an opposing factor, that unwholesome action has unwholesome accompaniment (and wholesome action is to be analyzed correspondingly), and that its giving of maturation is determinate.

VAK 4.119 asks how the mildness or intensity of six factors determines
action-weight. VAK 4.120 asks when an action that has occurred is also
accumulated. These are different questions: an action can be done without
crossing the completion or causal-determination threshold stated here.

The contrast also sharpens the role of volition. In 4.119, `cetanā` is
the factor by which the action-course is completed; here `saṃcetanā`
describes doing an action deliberately, after consideration. Neither use
makes volition identical with the whole action. The verse names deliberate
action as one condition among five, with completion, opposition,
accompaniment, and maturation separately articulated.

The source span is `[271|19]–[272|03]`. The witness reads `saṃcenataḥ`
in the first explanatory question, normalized as `saṃcetanataḥ`, and has
the compressed `vipākadāna niyataṃ`, parsed here as `vipākadāne niyatam`.
The next topic opens at `[272|04]`.

**Former Philosophical Translation.**
> A performed action and an accumulated action are not identical
> determinations. Deliberate intention matters, but is not enough by
> itself: the required course must be complete, the action must remain
> without remorse or opposition, its accompaniment must be congruent, and
> maturation must be fixed. The analysis makes causal persistence
> intelligible without treating karma as a stored substance or reducing
> the event to its initial volition.

## 10. OWL++ Seed

```text
Class: PerformedAction
Class: AccumulatedAction
Class: DeliberateIntention
Class: Completion
Class: AbsenceOfRemorseAndCounteraction
Class: CongruentAccompaniment
Class: DeterminateMaturation

Rule: AccumulationConditions
  AccumulatedAction -> DeliberateIntention
  AccumulatedAction -> Completion
  AccumulatedAction -> AbsenceOfRemorseAndCounteraction
  AccumulatedAction -> CongruentAccompaniment
  AccumulatedAction -> DeterminateMaturation

Relation: PerformedAction -> doesNotByItselfEntail -> AccumulatedAction
```
