# VAK_4.95 — Projecting and Completing a Birth

## 1. Sanskrit (Devanāgarī)

```sanskrit
एकं जन्माक्षिपत्येकमनेकं परिपूरकम् ।
नाक्षेपिके समापत्ती अचित्ते प्राप्तयो न च ॥ ४.९५ ॥
```

## 2. Sanskrit (IAST)

```iast
ekaṃ janmākṣipaty ekam anekaṃ paripūrakam /
nākṣepike samāpattī acitte prāptayo na ca // 4.95 //
```

## 3. Lexical Analysis

```text
ekam | janma | ākṣipati | ekam | anekam | paripūrakam |
na | ākṣepike | samāpattī | acitte | prāptayaḥ | na | ca
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| `ekam` | nominative neuter singular, with `karma` understood | one action as projector |
| `janma` | accusative neuter singular | one birth; specified by the Bhāṣya as `nikāyasabhāga` |
| `ākṣipati` | third-person singular present | projects or determines |
| `ekam` | accusative neuter singular | one, agreeing with `janma` |
| `anekam` | nominative neuter singular | multiple; the completing action is many |
| `paripūrakam` | nominative neuter singular | completing, filling out |
| `na` | negative particle | not |
| `ākṣepike` | nominative feminine dual | projectors |
| `samāpattī` | nominative feminine dual | the two attainments |
| `acitte` | nominative feminine dual adjective | non-mental; qualifying the two attainments |
| `prāptayaḥ` | nominative feminine plural | acquisitions or possession-relations |
| `na ca` | negative coordination | nor are they |

In the first half, the verse contrasts one projecting action with multiple
completing actions. In the second, the two non-mental attainments and
acquisitions are separately excluded as projectors. The Bhāṣya defines the
projected “birth” as membership in a `nikāyasabhāga`, a common class of
beings.

## 4. Grammar

**Projection and completion**

```text
ekam [karma]
    ekam janma
    ākṣipati

paripūrakam [karma]
    anekam
```

> One action projects one birth; the completing action is multiple.

The Bhāṣya clarifies the direction of this numerical claim: one action does
not project many births, while many actions may project one birth together,
so the `nikāyasabhāga` is not projected piecemeal.

**What is not a projector**

```text
acitte samāpattī
    na ākṣepike

prāptayaḥ
    na [ākṣepikāḥ] ca
```

> The two non-mental attainments are not projectors, nor are acquisitions.

The prose confirms that `acitte` qualifies the two attainments. Acquisitions
are excluded separately, not described as “non-mental acquisitions.”

## 5. Translation

### Scientific English Rendering

> One action projects one birth; the completing action is multiple. The two
> non-mental attainments are not projectors, nor are acquisitions.

### Bhāṣya-informed study translation

> One action projects one `nikāyasabhāga`, one common class of beings, and
> does not project many such births. Many actions may project one class
> together, rather than projecting it in fragments. Many completing actions
> fill out that birth's particular features. The two non-mental attainments
> do not project a birth-class, nor do acquisitions.

The Aniruddha example, the two explanations of his remembered births, the
painter analogy, and the stated grounds for excluding attainments and
acquisitions belong to the Bhāṣya.

## 6. Philosophical Translation

> Projection establishes the unity of a birth-class; completion differentiates
> its particular features. The unity is not a one-cause/one-life arithmetic:
> one projecting action does not extend to many births, but multiple actions
> may jointly project one undivided class-membership. The causal relation is
> therefore asymmetrical, not a simple bijection. Neither the two
> non-mental attainments nor acquisition as a possession-relation performs
> this projecting function.

This reading stays with the Bhāṣya's claim about `nikāyasabhāga`; it does not
reduce the full constitution of a life to a single cause or infer that
projecting and completing exhaust every causal contribution.

## 7. Technical Vocabulary

- **Projecting action** (*ākṣepaka-karma*) — action that projects a birth-class.
- **Completing action** (*paripūraka-karma*) — the multiple actions that fill
  out the particular features of that birth.
- **Birth** (*janma*) — here, the Bhāṣya's designation for acquisition of a
  `nikāyasabhāga`, not a claim that every feature of a life has one projector.
- **Common class of beings** (*nikāyasabhāga*) — the class-membership whose
  acquisition is called being born in that class.
- **Non-mental attainments** (*acitta-samāpattī*) — the two attainments named
  in the prose; they are not projectors.
- **Acquisition** (*prāpti*) — a possession-relation, distinct from the
  operation that projects class-membership.
- **Volition** (*cetanā*) — present in the alternative account as a stream of
  giving-intentions; it is not inserted as a synonym for every action.

## 8. Logical Determination

Let `J` be one `nikāyasabhāga`, `Kp` a projecting action, and `Kcᵢ` the
multiple completing actions.

```text
Kp → J
Kp ↛ many distinct J
{Kp₁, Kp₂, ...} → one J may be jointly projected
{Kc₁, Kc₂, ...} → particular features of J are completed
```

Thus the Bhāṣya asserts a limit on one-to-many projection but permits
many-to-one projection. It does not state a strict one-to-one bijection
between individual actions and births.

```text
Projects(non-mental attainment, J) = false
Projects(prāpti, J) = false
```

The Bhāṣya says the attainments lack maturation and are not coexistent with
action. It separately excludes acquisitions, with the compressed rationale
`karmaṇo 'nekaphalatvāt`; that explanation is retained without expanding it
beyond what the passage states.

## 9. Interpretive Note

The painter example distinguishes unity of projected class from multiplicity
of completed features: an outline establishes a figure, then many strokes
differentiate it. The Aniruddha exchange similarly distinguishes a singular
reported occasion from a causal history that may include further action or a
stream of volitions. The Bhāṣya's own qualifications prevent the formula
“one action, one birth” from becoming an absolute one-to-one law.

## 10. OWL++ Seed

```text
Class: Action
Class: BirthClass
Class: ProjectingAction
  SubClassOf: Action
Class: CompletingAction
  SubClassOf: Action
Class: NonMentalAttainment
Class: Acquisition

ObjectProperty: projectsBirthClass
  Domain: Action
  Range: BirthClass

ObjectProperty: completesBirthFeatures
  Domain: Action
  Range: BirthClass

Rule: OneActionDoesNotProjectManyBirthClasses
Rule: MultipleActionsMayJointlyProjectOneBirthClass
Rule: MultipleCompletingActionsMayCompleteBirthFeatures

Constraint: NonMentalAttainmentsAreNotProjectors
Constraint: AcquisitionIsNotProjection
Constraint: ProjectionAndCompletionAreDistinctCausalRoles
```
