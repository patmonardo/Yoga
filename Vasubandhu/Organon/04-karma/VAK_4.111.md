# VAK 4.111 — Completion of Giving, Patience, and Discipline

## 1. Sanskrit (Devanāgarī)

```sanskrit
सर्वत्र सर्वं ददतः कारुण्याद्दानपूरणम् ।
अङ्गच्छेदेऽप्यकोपात्तु रागिणः क्षान्तिशीलयोः ॥ ४.१११ ॥
```

## 2. Sanskrit (IAST)

```iast
sarvatra sarvaṃ dadataḥ kāruṇyād dānapūraṇam /
aṅgacchede 'py akopāt tu rāgiṇaḥ kṣāntiśīlayoḥ // 4.111 //
```

The verse gives two completion-conditions: compassion-governed giving,
and non-arising anger under extreme bodily injury. The Bhāṣya says the
second condition completes both patience and discipline, even while
passion remains.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `sarvatra` | indeclinable adverb | everywhere, in every relevant case |
| `sarvam` | accusative neuter singular | everything given |
| `dadataḥ` | genitive masculine singular present participle of `√dā` | of one who gives |
| `kāruṇyāt` | ablative neuter singular | from compassion |
| `dāna-pūraṇam` | nominative neuter singular compound | completion of giving |
| `aṅga-cchede` | locative masculine singular compound | when bodily parts are being cut |
| `api` | concessive particle | even |
| `akopāt` | ablative singular | because no anger arises |
| `tu` | contrastive particle | but, and |
| `rāgiṇaḥ` | genitive masculine singular | of one still possessing passion |
| `kṣānti-śīlayoḥ` | genitive feminine dual | of patience and discipline |

The Bhāṣya expands `sarvam` as giving everything to everyone, from eye to
marrow, and clarifies that the giver seeks no exceptional advancement.

## 4. Grammar

The first half names the condition for completion of giving:

```text
sarvatra sarvaṃ dadataḥ kāruṇyāt
    dāna-pūraṇam [bhavati]
```

> Giving is complete for one who gives everything everywhere from compassion.

The second half sets a concessive test:

```text
aṅga-cchede api
    akopāt
    rāgiṇaḥ
    kṣānti-śīlayoḥ [pūraṇam bhavati]
```

> For one still possessing passion, patience and discipline are complete
> through the absence of anger even when bodily parts are being cut.

The Bhāṣya confirms the dual: both the perfection of patience and the
perfection of discipline are complete under this condition. It does not
separately elaborate their respective functions here.

## 5. Translation

### Literal

> Giving is complete for one who gives everything everywhere from
> compassion. Patience and discipline are complete for one still
> possessing passion who does not become angry even when bodily parts
> are being cut.

### Bhāṣya-informed

> Giving is complete for one who gives everything everywhere from
> compassion. Patience and discipline are complete for one still
> possessing passion who does not become angry even when bodily parts
> are being cut. The Bhāṣya specifies giving everything to everyone,
> extending from the eye to the marrow, without seeking exceptional
> personal advancement. It explains that, although passion has not
> yet been abandoned, not even the slightest anger arises during the
> bodily injury.

The bodily examples are the Bhāṣya's account of the perfection-test, not
a behavioral recommendation. The source's qualification that passion
remains is retained.

## 6. Philosophical Translation

> Giving is complete for one who gives everything everywhere from compassion. Patience and discipline are complete for one still possessing passion who does not become angry even when bodily parts are being cut.

## 7. Technical Vocabulary

- **`Dāna-pūraṇa`** — completion of giving. The Bhāṣya expands the
  recipients to everyone and the gift to everything.
- **`Kāruṇya`** — compassion, the stated ground of giving.
- **`Abhyudaya-viśeṣa`** — exceptional advancement or prosperity sought
  for oneself; the Bhāṣya says this is not the giver's aim.
- **`Aṅga-ccheda`** — cutting of bodily parts, the extreme situation in
  which non-anger is tested.
- **`Akopa`** — absence of anger; the Bhāṣya intensifies this as not
  becoming angry in the slightest.
- **`Rāgin` / `avītarāga`** — still possessing passion; the Bhāṣya
  explicitly says the person is not yet free from passion.
- **`Kṣānti`** — patience; paired with discipline as complete through
  non-arising anger in this passage.
- **`Śīla`** — discipline; the Bhāṣya says its perfection is complete
  together with patience under the same condition.

## 8. Logical Determination

```text
Giving:
    gives everything to everyone
    + compassion as ground
    + no pursuit of exceptional personal advancement
    → completion of giving

Patience and discipline:
    passion not yet abandoned
    + bodily injury
    + no anger, even in the slightest
    → completion of both perfections
```

This is the Bhāṣya's stated test. The passage does not give a separate
criterion for discipline or further describe conduct in response to injury.

## 9. Interpretive Note

The verse specifies compassion as the ground of giving and non-anger as
the decisive condition shared by patience and discipline. It does not
name *cetanā* here; the motive is expressed through compassion and the
absence of a desire for special advancement. These terms should not be
silently collapsed into a technical identity.

The bodily giving and injury examples belong to the source's account and
are preserved without turning them into practical advice. The study covers
`[267|03]–[267|09]`; 4.112 begins at `[267|10]` with the perfection of
vigor.

### Former Philosophical Translation

> Giving reaches completion when its whole field and extent are governed
> by compassion rather than the giver's pursuit of special advancement.
> Patience and discipline reach completion under a different test: even
> though passion has not been entirely abandoned, the specified injury
> does not produce anger. The Bhāṣya thus distinguishes completion of
> these practical courses from the claim that every passion has already
> ceased.

## 10. OWL++ Seed

```text
Class: GivingPerfection
Class: PatiencePerfection
Class: DisciplinePerfection
Class: Compassion
Class: ExceptionalPersonalAdvancement
Class: RemainingPassion
Class: BodilyInjury
Class: NonArisingAnger

Rule: CompleteGiving
  action = GivesEverythingToEveryone
  ground = Compassion
  excludesAim = ExceptionalPersonalAdvancement

Rule: CompletePatienceAndDiscipline
  condition = BodilyInjury
  anger = NonArisingAnger
  allows = RemainingPassion
  result = PatiencePerfection + DisciplinePerfection
```
