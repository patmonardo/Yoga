# VAK_4.120

## Sanskrit — Devanāgarī

संचेतनसमाप्तिभ्यां निष्कौकृत्यविपक्षतः ।
परिवाराद्विपाकाच्च कर्मोपचितमुच्यते ॥ ४.१२० ॥

## Sanskrit — IAST

saṃcetanasamāptibhyāṃ niṣkaukṛtyavipakṣataḥ |
parivārād vipākāc ca karmopacitam ucyate || 4.120 ||

> Textual caution: the local electronic source prints `niṣkraukṛtya`; this analysis provisionally normalizes it to `niṣkaukṛtya`, from `kaukṛtya` (“remorse”). The exact construction of `niṣkaukṛtyavipakṣataḥ` remains for Bhāṣya confirmation.

## Padaccheda

saṃcetanā | samāpti | -bhyām | niṣ-kaukṛtya | vipakṣataḥ | parivārāt | vipākāt | ca | karma | upacitam | ucyate

## Literal translation

> Through deliberate intention and completion, through freedom from remorse, through relation to an opposing factor, through accompaniment, and through maturation, karma is called accumulated.

## Philosophical translation

> An action does not become fully accumulated merely because something externally happened. It becomes incorporated into the causal continuum when the agent consciously intends it, carries it through to completion, does not inwardly undo the deed through remorse, stands in a determinate relation to counterforces, is reinforced by associated conduct and dispositions, and thereby establishes a capacity for maturation. Accumulated karma is activity that has become causally consolidated.

## Technical vocabulary

- **upacita** — accumulated, consolidated, built into the continuum.
- **saṃcetanā** — full or deliberate volition.
- **samāpti** — completion or objective accomplishment.
- **niṣkaukṛtya** — freedom from remorse.
- **vipakṣa** — opposing factor, counteragent, or antidotal determination.
- **parivāra** — surrounding accompaniments and reinforcing factors.
- **vipāka** — maturation or matured result.

## Performed and accumulated karma

The verse distinguishes occurrence from causal consolidation:

- a deed may occur without becoming deeply accumulated;
- deliberate adoption, completion, post-action endorsement, reinforcement, and maturation make it a stable causal determination of the continuum.

`Upacita` does not imply a material karmic substance. It means that the activity has been sufficiently determined for its efficacy to persist after the present event has ceased.

## Deliberate intention and completion

`Saṃcetanā` is conscious adoption of the deed as one’s undertaking. `Samāpti` is its objective realization. Together they unite subjective purpose and completed actuality:

```text
saṃcetanā — the end is inwardly willed
samāpti   — the end is outwardly accomplished
```

An accidental event and a deliberately completed deed may resemble one another physically while differing fundamentally as karma.

## Remorse and post-action transformation

Remorse does not erase the historical event, but it changes the agent’s present relation to it. Repudiation, confession, restraint, repair, and cultivation of a contrary state can interrupt the self-reinforcing continuation of an unwholesome deed.

Freedom from remorse is not intrinsically wholesome. It strengthens whichever orientation the deed already has: non-regret reinforces wholesome and unwholesome deeds alike.

## Counteraction

`Vipakṣa` should be understood structurally rather than arithmetically. A counterfactor does not simply subtract units from karma; it reorganizes the continuum around a contrary practical orientation. The exact syntax of `vipakṣataḥ` remains provisional pending the Bhāṣya.

## Accompaniment

A principal act is surrounded by associated mental factors, preparatory and subsequent actions, repetition, encouragement, rejoicing, and habitual dispositions. These form its `parivāra` and can greatly enlarge the karmic complex.

## Maturation

Accumulated karma is causally organized toward `vipāka`. The present act ceases, but a structured capacity for determinate maturation remains. This permits temporally distant results without positing a permanent self or a material store of karma.

## Relation to VAK_4.119

VAK_4.119 asks how strongly karma is constituted through field, basis, preparation, volition, intention, and subsequent reinforcement. VAK_4.120 asks how an activity becomes causally consolidated.

```text
VAK_4.119 — intensity of the complete deed
VAK_4.120 — accumulation of the completed deed
```

Together they trace an end-to-end structure:

```text
orientation → volition → preparation → objective execution → completion
→ endorsement or repudiation → reinforcement or counteraction → maturation
```

## Doctrinal determination

1. Not every performed deed is equally accumulated.
2. Deliberate intention and completion contribute to accumulation.
3. The post-action relation of the agent modifies consolidation.
4. Remorse and counteractive factors oppose continued reproduction.
5. Accompanying factors reinforce and enlarge the principal act.
6. Accumulated karma possesses a determinate relation to maturation.
7. Karmic continuity is structured causal persistence, not a permanent agent.

## Logical determination

```text
AccumulationStatus(k) = f(
  deliberateness,
  completion,
  postActionRelation,
  counteractiveRelation,
  accompaniment,
  maturation
)
```

## Organon interpretation

An executed action changes the world; an accumulated action also changes the world-producing instrument. The deed is compiled into the continuing practical architecture of the agent:

```text
performed operation → updated agent-state → future volition → further activity
```

Karma is therefore recursive. It is not only what the instrument produces, but how the instrument modifies itself through what it produces.

## Structural schema

```text
AccumulatedKarma
├── subjective adoption — saṃcetanā
├── objective accomplishment — samāpti
├── post-action relation — niṣkaukṛtya / remorse
├── opposition — vipakṣa
├── reinforcement — parivāra
└── causal expression — vipāka
```

## OWL++ seed

```ttl
vak:VAK_4_120 a vak:Karika ;
    rdfs:label "VAK 4.120" ;
    vak:continues vak:VAK_4_119 ;
    vak:hasTopic vak:AccumulatedKarma .

vak:AccumulatedKarma
    vak:determinedBy vak:DeliberateIntention,
                     vak:Completion,
                     vak:PostActionRelation,
                     vak:CounteractiveRelation,
                     vak:AccompanyingFactors,
                     vak:Maturation .

vak:CounteractiveFactor
    rdfs:label "Vipakṣa" ;
    vak:opposes vak:KarmicTendency .

vak:KarmicAccompaniment
    rdfs:label "Parivāra" ;
    vak:reinforces vak:PrincipalKarmicAct .
```

## Commit note

- distinguish performed karma from causally accumulated karma;
- define deliberate intention and objective completion as initial conditions;
- analyze remorse and non-remorse as post-action transformations;
- preserve `niṣkaukṛtyavipakṣataḥ` for Bhāṣya confirmation;
- treat counteraction structurally rather than arithmetically;
- define `parivāra` as reinforcing accompaniment;
- connect accumulated karma with maturation;
- interpret accumulation as incorporation of a deed into the future activity-producing instrument.
