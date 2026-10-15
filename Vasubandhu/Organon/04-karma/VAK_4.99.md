# VAK_4.99 — The Divider's Culpable Speech and Its Maturation

## 1. Sanskrit (Devanāgarī)

```sanskrit
तदवद्यं मृषावादस्तेन भेत्ता समन्वितः ।
अवीचौ पच्यते कल्पमधिकैरधिका रुजः ॥ ४.९९ ॥
```

## 2. Sanskrit (IAST)

```iast
tad-avadyaṃ mṛṣāvādas tena bhettā samanvitaḥ /
avīcau pacyate kalpam adhikair adhikā rujaḥ // 4.99 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `tat-avadyaṃ` | nominative neuter singular | the culpable action associated with that division |
| `mṛṣā-vādaḥ` | nominative masculine singular | false speech |
| `tena` | instrumental masculine singular | with that false speech |
| `bhettā` | nominative masculine singular agent noun | the divider |
| `samanvitaḥ` | nominative masculine singular participle | endowed with it |
| `avīcau` | locative singular | in Avīci |
| `pacyate` | third-person singular passive | undergoes maturation |
| `kalpam` | accusative singular of duration | for a kalpa; specified by the Bhāṣya as an intermediate kalpa |
| `adhikaiḥ` | instrumental plural | with additional actions of *ānantarya* understood |
| `adhikāḥ` | nominative feminine plural | greater or increased |
| `rujaḥ` | nominative feminine plural | pains |

The verse answers the 4.98 question of what the divider is endowed with:
the culpable false speech. It then states the maturation locus and duration,
before noting that additional actions of *ānantarya* increase the pains.

## 4. Grammar

**The divider's culpable action**

```text
tat-avadyaṃ
    mṛṣā-vādaḥ [asti]

bhettā
    tena [mṛṣā-vādena]
    samanvitaḥ
```

> The culpable action associated with that is false speech, and the divider
> is endowed with it.

The Bhāṣya specifies that this false speech co-arises with the Saṅgha
division as verbal manifestation and non-disclosing continuity. It is the
divider's action, not the Saṅgha's resulting state of non-concord.

**Maturation and increased pains**

```text
[bhettā]
    avīcau
    kalpam
    pacyate

adhikaiḥ [ānantarya-karmabhiḥ]
    adhikāḥ rujaḥ [bhavanti]
```

> The divider undergoes maturation in Avīci for a kalpa; with additional
> actions of *ānantarya*, the pains are greater.

The Bhāṣya glosses the duration as one intermediate kalpa and explains the
increase through a more susceptible support and more numerous, more intense
causes of pain.

## 5. Translation

### Literal

> The culpable action associated with that is false speech, and the divider
> is endowed with it. He undergoes maturation in Avīci for a kalpa; with
> additional actions of *ānantarya*, the pains are greater.

### Bhāṣya-informed

> The culpable action that produces the Saṅgha's division is false speech,
> and it is this verbal action—not the community's condition of non-concord—
> that belongs to the divider. More precisely, it comprises verbal
> manifestation and non-disclosing continuity co-arising with the division.
> This action matures in the great Avīci hell for one intermediate kalpa.
> When additional actions of *ānantarya* are present, the support becomes
> denser and more sensitive, and the causes of pain become more numerous and
> more intense.

The manifestation/non-disclosing-continuity analysis, intermediate-kalpa
duration, and explanation of increased pain are Bhāṣya determinations.

## 6. Philosophical Translation

> The culpable action associated with that is false speech, and the divider is endowed with it. He undergoes maturation in Avīci for a kalpa; with additional actions of *ānantarya*, the pains are greater.

## 7. Technical Vocabulary

- **Culpable action** (*avadya*) — the blameworthy action associated with
  Saṅgha division.
- **False speech** (*mṛṣāvāda*) — the divider's verbal action in this case.
- **Divider** (*bhettā*) — the agent who possesses the culpable speech.
- **Verbal manifestation** (*vāg-vijñapti*) and **non-disclosing continuity**
  (*vāg-avijñapti*) — the two verbal factors the Bhāṣya says arise together
  with the Saṅgha division. Keep this pair distinct from the resulting
  non-concord.
- **Avīci** — the maturation locus specified for this action; the Bhāṣya
  says other actions of *ānantarya* do not necessarily mature there.
- **Intermediate kalpa** (*antarakalpa*) — the Bhāṣya's specification of
  the verse's `kalpam`.
- **Pain** (*ruj*) — increased in proportion to additional actions of
  *ānantarya* in the Bhāṣya's account.
- **Action of *ānantarya*** — the additional grave action whose presence
  increases the painful maturation in this passage.

## 8. Logical Determination

Let `D` be the divider, `K` the culpable false-speech action, `S` the
Saṅgha, `N` its resulting non-concord, and `M` the divider's later
maturation.

```text
Bears(D, K)
Causes(K, N)
Bears(S, N)
Bears(D's later continuum, M)
```

Thus:

```text
K ≠ N
N ≠ M
```

For multiple actions of *ānantarya*, the Bhāṣya describes increased painful
intensity within the Avīci maturation, not a separate sequence of
immediately successive births:

```text
more ānantarya actions
    → denser, more sensitive support
    → more numerous and intense causes
    → twofold through fivefold feeling
```

## 9. Interpretive Note

VAK 4.98 assigns the resulting non-concord to the Saṅgha. VAK 4.99
completes the attribution by assigning culpable false speech to the
divider, then describes the maturation of that action. The Bhāṣya's
account of multiple actions intensifying the painful support resolves the
question of how several *ānantarya* actions relate without treating each
as a separate intervening birth.

### Former Philosophical Translation

> The divider's culpable speech belongs to the agent; the non-concord it
> produces belongs to the Saṅgha; the later maturation belongs to the
> divider's continuum. One causal course links these distinct determinations
> without collapsing action, collective result, and experienced maturation
> into one bearer or one moment.

## 10. OWL++ Seed

```text
Class: Action
Class: FalseSpeechAction
  SubClassOf: Action
Class: VerbalManifestation
Class: NonDisclosingContinuity
Class: SaṅghaDivision
Class: NonConcord
Class: AviciMaturation
Class: AnantaryaAction

ObjectProperty: performedBy
  Domain: Action
ObjectProperty: causes
  Domain: Action
ObjectProperty: borneBy
  Domain: SaṅghaDivision
ObjectProperty: maturesAs
  Domain: Action

Rule: DividerCulpableAction
  action = FalseSpeechAction
  performedBy = Divider
  factors = {VerbalManifestation, NonDisclosingContinuity}
Rule: SaṅghaDivisionMaturation
  action = FalseSpeechAction
  maturesAs = AviciMaturation
  duration = IntermediateKalpa
Rule: AdditionalAnantaryaActions
  increase = PainfulMaturationIntensity

Constraint: DividerActionIsNotSaṅghaNonConcord
Constraint: AdditionalActionsDoNotEntailSeparateImmediateBirthSequence
```
