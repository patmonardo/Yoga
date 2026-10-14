# VAK_4.98 — Saṅgha Division and Its Bearer

## 1. Sanskrit (Devanāgarī)

```sanskrit
सङ्घभेदस्त्वसामग्रीस्वभावो विप्रयुक्तकः ।
अक्लिष्टाव्याकृतो धर्मः सङ्घस्तेन समन्वितः ॥ ४.९८ ॥
```

## 2. Sanskrit (IAST)

```iast
saṃghabhedas tv asāmagrīsvabhāvo viprayuktakaḥ /
akliṣṭāvyākṛto dharmaḥ saṃghas tena samanvitaḥ // 4.98 //
```

## 3. Lexical Analysis

```text
saṃgha-bhedaḥ | tu | asāmagrī-svabhāvaḥ | viprayuktakaḥ |
akliṣṭa-avyākṛtaḥ | dharmaḥ | saṃghaḥ | tena | samanvitaḥ
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| `saṃgha-bhedaḥ` | nominative masculine singular compound | Saṅgha division; the resulting condition of non-concord |
| `tu` | contrastive particle | but; marks a distinction from the causal action |
| `asāmagrī-svabhāvaḥ` | nominative masculine singular compound | having non-concord as its nature |
| `viprayuktakaḥ` | nominative masculine singular | dissociated; classified as a factor dissociated from consciousness |
| `akliṣṭa-avyākṛtaḥ` | nominative masculine singular compound | non-afflicted and indeterminate |
| `dharmaḥ` | nominative masculine singular | a conditioned Dharma |
| `saṃghaḥ` | nominative masculine singular | the Saṅgha that bears the division |
| `tena` | instrumental masculine singular pronoun | with it, referring to the division |
| `samanvitaḥ` | nominative masculine singular past passive participle | endowed with it |

The verse changes focus from the action that produces division to the
division as a resulting condition. The Bhāṣya explains why the same term
can be used for both cause and result, then identifies the Saṅgha as bearer
of the resulting non-concord.

## 4. Grammar

**Nature of Saṅgha division**

```text
saṃgha-bhedaḥ tu
    asāmagrī-svabhāvaḥ
    viprayuktakaḥ
    akliṣṭa-avyākṛtaḥ dharmaḥ
```

> But Saṅgha division has non-concord as its nature; it is a dissociated,
> non-afflicted, indeterminate Dharma.

The Bhāṣya specifies `asāmagrī` as a conditioned formation dissociated from
consciousness and classified as non-afflicted and indeterminate.

**Bearer of the division**

```text
saṃghaḥ
    tena
    samanvitaḥ
```

> The Saṅgha is endowed with it.

The instrumental `tena` refers to the division. The subject of this clause
is the Saṅgha, not the agent who caused the division.

## 5. Translation

### Scientific English Rendering

> But Saṅgha division has non-concord as its nature; it is a dissociated,
> non-afflicted, indeterminate Dharma. The Saṅgha is endowed with it.

### Bhāṣya-informed study translation

> The division itself must be distinguished from the action that produces
> it. Strictly considered, Saṅgha division is the condition of non-concord,
> a conditioned formation dissociated from consciousness and classified as
> non-afflicted and indeterminate. This resulting condition belongs to the
> Saṅgha that has been divided, not to the agent who divided it.

The causal use of “Saṅgha division,” the classification of non-concord, and
the explicit distinction between divider and bearer are supplied by the
Bhāṣya.

## 6. Philosophical Translation

> The cause of a division and the divided condition are distinct
> determinations. The action belongs to the divider; the resulting
> non-concord is borne by the Saṅgha. Naming the cause by its result does
> not make them one and the same Dharma.

## 7. Technical Vocabulary

- **Saṅgha division** (*saṃghabheda*) — in the strict definition here, the
  resulting condition of non-concord; in the prior action-list, the same
  expression can name its cause.
- **Non-concord** (*asāmagrī*) — the intrinsic nature assigned to the
  divided condition.
- **Dissociated** (*viprayukta*) — the Bhāṣya identifies the condition as
  a conditioned formation dissociated from consciousness.
- **Non-afflicted** (*akliṣṭa*) and **indeterminate** (*avyākṛta*) — the
  technical classifications of the resulting condition; they do not
  transfer the ethical classification of the causal action to its result.
- **Result-name applied to cause** (*hetau phalopacāra*) — the Bhāṣya's
  explanation for calling the causal action “Saṅgha division.”
- **Endowed with** (*samanvita*) — the predicate assigning the resulting
  condition to the Saṅgha as its bearer.

## 8. Logical Determination

Let `D` be the divider, `K` the causal action, `S` the Saṅgha, and `B` the
resulting condition of non-concord.

```text
Performs(D, K)
Causes(K, B)
Bears(S, B)
```

The Bhāṣya rejects these identifications:

```text
K = B
Bears(D, B)
```

The use of the result-name for the cause is a transfer of designation:

```text
Causes(K, B)
    → the name “Saṅgha division” may be applied to K
```

The transfer preserves the causal relation only if the action and resulting
condition remain distinct.

## 9. Interpretive Note

The verse gives a precise attribution rule: the divider performs the
causal action, while the Saṅgha is endowed with the resulting non-concord.
The result's classification as non-afflicted and indeterminate is not a
reclassification of the action that produced it. The Bhāṣya thereby
separates causal agency, conditioned result, and bearer.

## 10. OWL++ Seed

```text
Class: Action
Class: Saṅgha
Class: SaṅghaDivision
Class: NonConcord
Class: ConditionedFormationDissociatedFromConsciousness
Class: NonAfflictedDharma
Class: IndeterminateDharma

ObjectProperty: performedBy
  Domain: Action
ObjectProperty: causes
  Domain: Action
ObjectProperty: borneBy
  Domain: SaṅghaDivision

Individual: SchismaticAction
  Type: Action
Individual: ResultingNonConcord
  Type: SaṅghaDivision
  Type: NonConcord
  Type: ConditionedFormationDissociatedFromConsciousness
  Type: NonAfflictedDharma
  Type: IndeterminateDharma

Rule: SaṅghaDivisionNameTransfer
  if causes(SchismaticAction, ResultingNonConcord)
  then resultNameMayApplyToCause(SaṅghaDivisionName,
                                 SchismaticAction)

Constraint: CausalActionIsNotResultingNonConcord
Constraint: SaṅghaBearsTheDivisionNotTheDivider
```
