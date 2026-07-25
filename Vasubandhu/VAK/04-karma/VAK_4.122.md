# VAK_4.122

## Sanskrit — Devanāgarī

दौःशील्यमशुभं रूपं शीलं तद्विरतिर्द्विधा ।
प्रतिक्षिप्ताच्च बुद्धेन विशुद्धं तु चतुर्गुणम् ॥ ४.१२२ ॥

## Sanskrit — IAST

dauḥśīlyam aśubhaṃ rūpaṃ śīlaṃ tadviratir dvidhā |
pratikṣiptāc ca buddhena viśuddhaṃ tu caturguṇam || 4.122 ||

## Padaccheda

dauḥśīlyam | aśubham | rūpam | śīlam | tat-viratiḥ | dvidhā | pratikṣiptāt | ca | buddhena | viśuddham | tu | catur-guṇam

## Translation

Misconduct consists in unwholesome bodily and verbal form. Discipline is abstention from such conduct and is twofold: restraint from what is intrinsically unwholesome and restraint from what the Buddha has prohibited. Purified discipline possesses four qualities.

## Analysis

The verse turns from the merit-basis of giving to the second merit-basis, moral discipline. `Dauḥśīlya` is not merely an inward defect but unwholesome determination embodied through bodily and verbal form. `Śīla` is defined as `virati`, determinate abstention: not mere non-occurrence, but the active prevention of a possible misconduct from becoming actual.

The twofold restraint distinguishes intrinsically unwholesome actions from conduct prohibited by the Buddha within an adopted discipline. The first tracks the harmful structure of the act itself; the second functions as a determinate training protocol designed to prevent affliction, stabilize the community, and support concentration.

The particle `tu` marks the difference between simple compliance and purified discipline. External rule-following can block harmful output, while `viśuddha-śīla` transforms the causes and dispositions that would generate that output. VAK_4.123 supplies its four qualities.

## Doctrinal determination

1. Misconduct is unwholesome bodily and verbal form.
2. Moral discipline is determinate abstention from misconduct.
3. Restraint is karmically real, not mere absence of action.
4. Discipline is twofold: restraint from intrinsic wrongdoing and from Buddha-prohibited conduct within training.
5. Purified discipline is distinguished from external conformity.
6. Purified discipline possesses four qualities, explained in VAK_4.123.

## Logical determination

```text
UnwholesomeVolition(agent)
∧ ExecutesThroughBodyOrSpeech(agent, act)
→ MisconductForm(act)

RecognizesProhibitedPossibility(agent, act)
∧ RefrainsFrom(agent, act)
→ MoralDiscipline(agent)

Prohibited(act) ←
    IntrinsicallyUnwholesome(act)
    ∨ ProhibitedByBuddhaWithinTraining(act)
```

## Organon interpretation

The verse distinguishes corrupted output, inhibitory law, and purified generative architecture:

```text
dauḥśīlya
    corrupted output

śīla
    inhibitory law

viśuddha śīla
    purified action-generating instrument
```

Basic discipline controls execution. Purified discipline reconfigures the generator of harmful execution. The twofold prohibition also distinguishes domain-level ethical invariants from explicit rules of an adopted operating discipline.

## Structural schema

```text
MoralDiscipline
├── opposed state: misconduct
│   └── unwholesome bodily-verbal form
├── basic definition: abstention
├── two domains
│   ├── intrinsically unwholesome conduct
│   └── conduct prohibited by the Buddha
└── purified form
    └── four qualities in VAK_4.123
```

## OWL++ seed

```ttl
vak:VAK_4_122 a vak:Karika ;
    rdfs:label "VAK 4.122" ;
    vak:continues vak:VAK_4_121 ;
    vak:hasTopic vak:MoralDiscipline,
                 vak:TwofoldRestraint,
                 vak:PurifiedDiscipline .

vak:Misconduct
    vak:actualizedAs vak:UnwholesomeBodilyVerbalForm .

vak:MoralDiscipline
    vak:definedAs vak:AbstentionFromMisconduct .

vak:TwofoldRestraint
    vak:hasMember vak:RestraintFromIntrinsicWrongdoing,
                  vak:RestraintFromBuddhaProhibitedConduct .

vak:PurifiedDiscipline
    vak:hasQualityCount "4" ;
    vak:explainedBy vak:VAK_4_123 .
```

## Commit note

VAK_4.122 — define moral discipline as twofold restraint and introduce its purification.