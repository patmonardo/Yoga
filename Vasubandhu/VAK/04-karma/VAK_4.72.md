# VAK_4d — VAkK_4.72

## 1. Sanskrit — Devanāgarī

समं प्राक् च मृतस्यास्ति न मौलोऽन्याश्रयोदयात् ।
सेनादिष्वेककार्यत्वात् सर्वे कर्तृवदन्विताः ॥ VAkK_4.72 ॥

## 2. Sanskrit — IAST

samaṃ prāk ca mṛtasyāsti na maulo ’nyāśrayodayāt /
senādiṣv ekakāryatvāt sarve kartṛvad anvitāḥ // VAkK_4.72 //

Source text:

```text
samaṃ prāk ca mṛtasyāsti na maulaḥ anyāśrayodayāt /
senādiṣvekakāryatvāt sarve karttṛvadanvitāḥ //
```

Textual normalization:

```text
maulaḥ + anya- → maulo ’nya-
karttṛ → kartṛ
```

The verse addresses two questions:

```text
1. When is the principal karmic course of killing completed?
2. Who acquires it in collective action?
```

## 3. Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| samaṃ | samam | simultaneously |
| prāk | prāk | beforehand; earlier |
| mṛtasyāsti | mṛtasya asti | it exists for one who has died / when death has occurred |
| maulo ’nya- | maulaḥ anya- | the principal course; another... |
| āśrayodayāt | āśraya-udayāt | because of the arising of another support |
| senādiṣu | senā-ādiṣu | in armies and similar collectives |
| ekakāryatvāt | eka-kāryatvāt | because of one common undertaking |
| sarve | sarve | all |
| kartṛvat | kartṛ-vat | like the immediate doer |
| anvitāḥ | anvitāḥ | connected; implicated |

Provisional expansion:

```text
If the victim dies before the agent
or simultaneously with the agent,
the principal course exists.

If the agent dies first
and another support arises
before the victim dies,
the principal course does not arise in that new support.

In armies and similar collectives,
because there is one common undertaking,
all are implicated like the immediate doer.
```

## 4. Grammar

- `samam`: adverbial accusative, “simultaneously.”
- `prāk`: indeclinable, “before; earlier.”
- `mṛtasya`: genitive singular of the past passive participle from `mṛ`, “of one who has died.”
- `asti`: “exists; occurs.”
- `maulaḥ`: masculine nominative singular, “principal; constitutive.”
- `anyāśrayodayāt`: ablative compound, “because of the arising of another support.”
- `senādiṣu`: locative plural, “in armies and similar groups.”
- `ekakāryatvāt`: ablative abstract compound, “because of unity of undertaking.”
- `kartṛvat`: “like the doer.”
- `anvitāḥ`: masculine nominative plural, “connected; implicated.”

The compressed first half concerns the relation between the victim’s death and the continuity of the initiating agent’s support. The second half is syntactically clear: collective participants united in one operation are connected with the act as the immediate performer is.

## 5. Literal Translation

The principal course exists when the death occurs beforehand or simultaneously; it does not exist after another support has arisen. In armies and similar collectives, because they have one common undertaking, all are connected with the act like the doer.

## 6. Philosophical Translation

The completion of killing requires continuity between the agent who initiated the lethal process and the support in which the victim’s death occurs. If the victim dies before the agent or at the same time, the principal course can be completed. If the agent has already died and another support has arisen before the victim dies, that later death does not establish the principal course in the new support. In collective violence, however, physical execution by one member does not isolate responsibility in that individual: where all participate in one unified undertaking, all are karmically implicated as agents.

## 7. Technical Vocabulary

### maula

```text
maula
    principal
    constitutive
    root-phase of the karmic course
```

The `maula-karmapatha` is the principal completion, distinguished from preparation and aftermath.

### āśraya

```text
āśraya
    support
    psycho-physical support of the aggregate-series
```

It should not be reduced simply to “body.”

### anyāśraya

```text
anya-āśraya
    another support
```

This signals a change of life-support relevant to attribution.

### eka-kāryatva

```text
eka-kāryatva
    unity of undertaking
    participation in one common operation
```

### kartṛ

```text
kartṛ
    doer
    immediate performer
```

### anvita

```text
anvita
    connected
    joined
    implicated
```

## 8. Doctrinal Determination

The principal killing course is completed at the victim’s death, not merely at intention, preparation, or assault.

```text
attack
    ↓
delay
    ↓
victim’s death
        = principal completion
```

If the victim dies before or simultaneously with the agent, the relevant support remains continuous through completion.

If the agent dies first:

```text
former support ceases
    ↓
another support arises
    ↓
victim dies later
```

the new support does not acquire the former life’s principal killing course. Preparatory karmic force may remain, but the `maula` is denied.

The second half establishes distributed agency:

```text
many agents
    +
one common undertaking
    ↓
shared karmic implication
```

The criterion is participation in one practical operation, not merely whose hand delivered the final blow.

## 9. Logical Determination

The verse presents two opposed attribution rules.

### Diachronic contraction

```text
support transition before completion
    →
principal attribution does not transfer
```

Causal continuity is not identical with identity of the support that owns the completion.

### Synchronic expansion

```text
many supports
    +
unity of undertaking
    →
shared attribution
```

Thus:

```text
diachronically:
    support-difference limits attribution

synchronically:
    practical unity extends attribution
```

The verse therefore defines agency functionally through supported process and common operation rather than through a permanent substance.

## 10. Light Organon Interpretation

A moral processor requires both temporal identity tracking and collective agency tracking.

```text
MoralProcess
    hasInitiatingSupport
    hasCompletionEvent
    hasSupportTransition
    hasParticipants
    hasSharedUndertaking
```

For temporal attribution:

```text
PrincipalCompletion
    requires
    completion before or simultaneous with
    the initiating support’s transition
```

For collective attribution:

```text
participatesInSameUndertaking
    →
implicatedLikeImmediateDoer
```

Mere membership in a group is insufficient; `eka-kāryatva`, participation in one common undertaking, is the operative criterion.

## 11. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_72
    a vak:Karika ;
    rdfs:label "VAkK 4.72" ;
    vak:continues vak:VAK_4_71 ;
    vak:hasTopic vak:TemporalCompletion,
                 vak:CollectiveAgency .

vak:PrincipalKillingCourse
    rdfs:subClassOf vak:PrincipalKarmicCourse ;
    vak:requiresOutcome vak:DeathOfVictim ;
    vak:requiresSupportContinuity vak:ContinuityUntilDeathEvent .

vak:SupportTransition
    a logic:StateTransition ;
    rdfs:label "arising of another support" .

vak:CollectiveOperation
    a logic:JointAction ;
    vak:hasUnityCriterion vak:OneCommonUndertaking .

vak:OneCommonUndertaking
    rdfs:label "eka-kāryatva" .

vak:CollectiveParticipant
    vak:participatesIn vak:CollectiveOperation ;
    vak:mayBeImplicatedAs vak:ImmediateDoer .
```

Rule-oriented seed:

```text
Rule:
    InitiatedLethalProcess(?agent, ?victim)
    and DeathOf(?victim, ?death)
    and BeforeOrSimultaneous(
        ?death,
        SupportTransitionOf(?agent)
    )
    ->
    PrincipalKillingCourse(?agent)

Rule:
    SupportTransitionOf(?agent, ?transition)
    and Before(?transition, DeathOf(?victim))
    ->
    not PrincipalKillingCourse(?agent)

Rule:
    ParticipatesIn(?agent, ?operation)
    and OneCommonUndertaking(?operation)
    and KillingOutcome(?operation)
    ->
    ImplicatedLikeImmediateDoer(?agent)
```

## 12. Commit Note

Committed VAK_4d / VAkK_4.72.

Established:
- the victim’s death as the completion-event of killing
- support-continuity as a condition of principal attribution
- denial of principal completion after another support has arisen
- collective attribution through unity of undertaking
- distinction between immediate physical execution and distributed practical agency

First-pass determination:

```text
responsibility depends upon
    temporal continuity of agency
    and
    unity of collective undertaking
```
