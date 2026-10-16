# VAK_6.16 — The Combined Cognitive Condition and Four Aspects of Seeing

## 1. Sanskrit (Devanāgarī)

```sanskrit
स धर्मस्मृत्युपस्थाने समस्तालम्बने स्थितः ।
आनित्यदुःखतः शून्यानात्मतस्तान् विपश्यति ॥ ६.१६ ॥
```

## 2. Sanskrit (IAST)

```text
sa dharmasmṛtyupasthāne samastālambane sthitaḥ |
ānityaduḥkhataḥ śūnyānātmatas tān vipaśyati || 6.16 ||
```

The preceding establishments preserve body, feeling, consciousness, and
dharmas as distinct fields. This verse joins them in the combined cognitive
Condition of the dharma establishment and specifies four aspects of seeing.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `saḥ` | nominative singular masculine pronoun | the practitioner formed by the preceding cultivation |
| `dharmasmṛtyupasthāne` | locative singular neuter compound | in the establishment of recollection concerning dharmas |
| `samastālambane` | locative singular neuter compound | with a combined cognitive Condition |
| `sthitaḥ` | nominative singular masculine participle of `√sthā` | established in that practice |
| `ānitya-` | first member of a compressed series | as impermanent; explained by prose `anityataḥ` |
| `duḥkhataḥ` | adverbial ablative | as suffering |
| `śūnyataḥ` | adverbial ablative | as empty |
| `anātmataḥ` | adverbial ablative | as not-self |
| `tān` | accusative plural masculine pronoun | those fields beginning with body |
| `vipaśyati` | third-person singular present of `vi-√paś` | sees distinctly |

```text
saḥ | dharma-smṛti-upasthāne | samasta-ālambane | sthitaḥ |
ānitya-duḥkhataḥ | śūnya-anātmataḥ | tān | vipaśyati
```

The separate kārikā has `ānitya-`; the running verse has `ānaty-`, while the
prose gives `anityataḥ`. The latter fixes the local sense without silently
altering either Sanskrit witness.

## 4. Grammar

The main construction is `saḥ ... sthitaḥ ... tān vipaśyati`: the practitioner,
established in the dharma establishment, sees those previously distinguished
fields. The locatives `dharmasmṛtyupasthāne` and `samastālambane` agree; the
second specifies its combined cognitive Condition. The Bhāṣya calls this a
`saṃbhinna-ālambana`.

`Tān` refers to body, feeling, consciousness (`citta`), and dharmas together.
The prose resolves the four seeing-aspects as parallel expressions:

```text
anityataḥ   as impermanent
duḥkhataḥ   as suffering
śūnyataḥ    as empty
anātmataḥ   as not-self
```

The scope rule from 6.14 still governs: impermanence applies to the
conditioned, suffering to what is with influx, and emptiness and not-self to
all dharmas. Combination of the fields does not erase those differences.

**Future Feature Grammar sketch (not executable):**

```text
PRACTITIONER[STATE=established, PRACTICE=dharma-establishment]
  ← saḥ + dharmasmṛtyupasthāne + sthitaḥ
CONDITION[COMPOSITION=combined,
          FIELDS=body+feeling+consciousness+dharmas]
  ← samastālambane + tān
SEEING[ASPECTS=impermanent+suffering+empty+not-self,
       SCOPE=conditioned|with-influx|all-dharmas]
  ← vipaśyati + [four adverbial aspects, Bhāṣya resolution]
```

The source supplies the locative construction and the four aspects. The
feature slots preserve combined scope and the distinct applicability rules
for later reflective modeling.

## 5. Translation

### Literal Translation

> Established in the dharma establishment with a combined cognitive Condition,
> the practitioner sees those [fields] as impermanent, suffering, empty, and
> not-self.

### Bhāṣya-informed study translation

> Having cultivated the establishments for body, feeling, consciousness, and
> dharmas, the practitioner stands in the dharma establishment with a combined
> cognitive Condition. They gather those fields together and see them in four
> aspects: as impermanent, suffering, empty, and not-self.

### Translation note

The combined Condition and the referent of `tān` are specified by the Bhāṣya.
The applicability of the four aspects follows the preceding unit's scope rule.

## 6. Philosophical Translation

> The practitioner has examined four fields and can now hold them together as
> one articulated cognitive Condition. Distinct seeing works across that
> whole through impermanence, suffering, emptiness, and not-self, while each
> aspect keeps the range proper to it. The synthesis belongs to the operation
> of Prajñā rather than to a loss of the fields' differences.

The movement in this unit is:

```text
separately examined fields
    → combined cognitive Condition
    → four scoped aspects of distinct seeing
```

## 7. Technical Vocabulary

**`Dharma-smṛtyupasthāna` — establishment of recollection concerning dharmas**

The fourth establishment can take dharmas alone or, as here, a combined
Condition comprising body, feeling, consciousness, and dharmas. Prajñā remains
its intrinsic nature under the distinction established in 6.15.

**`Samasta-ālambana` — combined cognitive Condition**

The kārikā names the whole taken up in this contemplation. Its components
remain differentiated; the total Condition is their articulated combination.

**`Saṃbhinna-ālambana` / `asaṃbhinna-ālambana` — mixed / unmixed Condition**

The Bhāṣya calls the Condition in 6.16 `saṃbhinna`. The end of 6.15 contrasts
it with an unmixed Condition that takes one field alone. The distinction
concerns composition of the cognitive Condition, not clarity or confusion.

**`Sthita` — established**

The practitioner has a stable standpoint in the dharma establishment. The
participle qualifies the agent of `vipaśyati`; it does not itself name a new
Path stage.

**`Tān` — those fields**

The plural retains body, feeling, consciousness, and dharmas within the
combined Condition. The Bhāṣya explicitly resolves the reference as all the
fields beginning with body.

**`Vipaśyati` — sees distinctly**

The verb names the discriminative act developed from the examination
prescribed in 6.14. Its four adverbial expressions specify aspects under
which the combined field is seen.

**`Anityataḥ / duḥkhataḥ / śūnyataḥ / anātmataḥ` — as impermanent / suffering / empty / not-self**

These are the prose's parallel forms. The separate kārikā starts with
`ānitya-`, while the running verse transmits `ānaty-`. The preceding Bhāṣya
assigns impermanence to conditioned dharmas, suffering to those with influx,
and emptiness and not-self to all dharmas. The combined Condition does not
broaden the first two beyond those ranges.

## 8. Logical Determination

The source's structure can be represented as:

```text
Members(CombinedCondition) = {Body, Feeling, Consciousness, Dharmas}
EstablishedIn(practitioner, DharmaEstablishment)
TakesCondition(DharmaEstablishment, CombinedCondition)
SeesThrough(practitioner, CombinedCondition,
            {Impermanence, Suffering, Emptiness, NotSelf})
```

The inherited applicability constraints remain:

```text
Conditioned(x) → Applicable(Impermanence, x)
WithInflux(x)  → Applicable(Suffering, x)
Dharma(x)     → Applicable(Emptiness, x)
Dharma(x)     → Applicable(NotSelf, x)
```

A later LogicFrame can evaluate these predications for each member without
turning a combined Condition into an undifferentiated class.

## 9. Interpretive Note

**The whole retains its fields.** The practitioner sees the four examined
fields together; `tān` and the Bhāṣya's `kāyādīn sarvān` preserve their
plurality.

**Four aspects are acts of seeing.** `Vipaśyati` governs the aspect terms.
Their role is to determine how the field is comprehended in practice, with
the applicability rules established in 6.14.

**Organon interpretation.** The combined Condition offers a reflective
surface on which a field's identity, membership, and applicable aspects can
be held together. A future Model can carry those features into LogicFrame
without suppressing the differences required for correct predication. This
is project formalization of the source's contemplative relation.

## 10. OWL++ Seed

```text
Class: EstablishmentOfRecollection
Class: DharmaEstablishment
    SubClassOf: EstablishmentOfRecollection
Class: CognitiveCondition
Class: CombinedCondition
    SubClassOf: CognitiveCondition
Class: ExaminationField
Class: BodyField
    SubClassOf: ExaminationField
Class: FeelingField
    SubClassOf: ExaminationField
Class: ConsciousnessField
    SubClassOf: ExaminationField
Class: DharmaField
    SubClassOf: ExaminationField
Class: SeeingAspect
Class: ImpermanenceAspect
    SubClassOf: SeeingAspect
Class: SufferingAspect
    SubClassOf: SeeingAspect
Class: EmptinessAspect
    SubClassOf: SeeingAspect
Class: NotSelfAspect
    SubClassOf: SeeingAspect

ObjectProperty: hasCognitiveCondition
    Domain: EstablishmentOfRecollection
    Range: CognitiveCondition

ObjectProperty: combinesField
    Domain: CombinedCondition
    Range: ExaminationField

ObjectProperty: seesThroughAspect
    Domain: DharmaEstablishment
    Range: SeeingAspect

Assertion: DharmaEstablishment hasCognitiveCondition CombinedCondition
Assertion: CombinedCondition combinesField BodyField
Assertion: CombinedCondition combinesField FeelingField
Assertion: CombinedCondition combinesField ConsciousnessField
Assertion: CombinedCondition combinesField DharmaField

Constraint: ImpermanenceAspect appliesTo ConditionedDharma
Constraint: SufferingAspect appliesTo WithInfluxDharma
Constraint: EmptinessAspect appliesTo AllDharmas
Constraint: NotSelfAspect appliesTo AllDharmas

View: CombinedFourAspectSeeing
    Preserves: FieldIdentity, CombinedMembership, CognitiveCondition,
               SeeingAspect, ApplicabilityScope, SourceProvenance
```

The seed is a project schema for the combined Condition and the aspects of
seeing. It carries forward the scope distinctions from 6.14.
