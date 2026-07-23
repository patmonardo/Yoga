# VAK_7.30 — The Range of the Buddha's Powers

## Sanskrit

### Devanāgarī

```text
प्राङ्निवासच्युतोत्पादबलं ध्यानेषु शेषितम् ।
सर्वभूमिषु केनास्य बलमव्याहतं यतः ॥ ७.३० ॥
```

### IAST

```text
prāṅnivāsa-cyutotpāda-balaṃ dhyāneṣu śeṣitam /
sarvabhūmiṣu kenāsya balam avyāhataṃ yataḥ // VAK_7.30 //
```

## Source Caution

The transmitted line is compressed, and manuscript or e-text forms vary around *prāṅnivāsa* / *pūrvanivāsa*. The doctrinal sense is clear from the bhāṣya: the power concerning former abodes and the power concerning death-and-rebirth are based in the dhyānas; the remaining powers operate in all levels.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| prāk-nivāsa | compound | former abodes, previous lives |
| cyuta-utpāda | compound | death and rebirth |
| balam | nominative/accusative singular neuter | power |
| dhyāneṣu | locative plural | in the dhyānas |
| śeṣitam | past passive participle | confined, left restricted |
| sarva-bhūmiṣu | locative plural | in all levels or planes |
| kena | instrumental/interrogative | why; by what reason |
| asya | genitive singular | of him; of the Buddha |
| balam | nominative singular | power |
| avyāhatam | nominative singular neuter | unobstructed |
| yataḥ | causal indeclinable | because |

## Literal Translation

The power concerning former abodes and the power concerning death and rebirth are confined to the dhyānas; the remaining powers are present in all levels. Why? Because his power is unobstructed.

## Philosophical Translation

Two powers require the concentrated observational support of the meditative absorptions: recollection of former lives and vision of beings dying and being reborn. The other powers are not limited to one meditative level, because the Buddha's cognitive power meets no obstruction in its proper operation.

## Technical Vocabulary

### bhūmi

```text
bhūmi
    level
    plane
    meditative or cognitive ground
```

Here *bhūmi* marks the level in which a power is available or operative.

### avyāhata

```text
avyāhata
    unobstructed
    not impeded
    not checked by an incompatible condition
```

The claim is functional rather than merely honorific: the Buddha's power is not blocked when its proper object is present.

## Doctrinal Determination

### Two powers dependent on dhyāna

```text
former-abode power
    recollection of previous lives

cyutotpāda power
    knowledge of death and rebirth
```

These depend upon the concentrated clarity of the dhyānas.

### The remaining powers

The other powers are available throughout the levels appropriate to the Buddha's activity. They are not confined to a single meditative base.

The verse therefore distinguishes:

```text
powers requiring a specific support
    and
powers whose operation is broadly available
```

## Logical Determination

VAK 7.29 classified the powers by the knowledges composing them. VAK 7.30 now classifies them by their **range of operation**.

```text
composition
    which knowledges constitute a power

scope
    in which levels that power can operate
```

This confirms that a complete Path analysis needs more than a list of faculties. It must also state the conditions and range of their exercise.

## Organon Light

The Dialectical Copula is indeed master of analytical scopes in the limited sense needed here:

```text
it determines
    which relation is active
    which support it requires
    and how widely its power extends
```

A power is not fully defined until both its content and its scope are known.

No stronger identification is imposed in this first kārikā pass.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix sam: <http://127.0.0.1:3000/samapatti#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_30
    a vak:Karika ;
    rdfs:label "VAK 7.30" ;
    vak:determines jna:PowerOperationalScope,
                   jna:UnobstructedBuddhaPower .

jna:FormerAbodesPower
    jna:operatesIn sam:DhyanaLevels .

jna:DeathRebirthPower
    jna:operatesIn sam:DhyanaLevels .

jna:RemainingBuddhaPowers
    jna:operatesIn jna:AllRelevantLevels ;
    jna:hasProperty jna:UnobstructedOperation .
```

## Commit History

```text
2026-07-23 — Initial kārikā-pass analysis for VAK_7b.
```
