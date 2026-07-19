# VAK 6.23

## Sanskrit

### Devanāgarī

मूर्धलाभी न मूलच्छित् क्षान्तिलाभ्यनपायगः ।
शिष्यगोत्रान्निवर्त्य द्वे बुद्धः स्यात् त्रीण्यपीतरः ॥ ६.२३ ॥

### IAST

**mūrdhalābhī na mūlacchit kṣāntilābhy anapāyagaḥ |**
**śiṣyagotrān nivartya dve buddhaḥ syāt trīṇy apītaraḥ || 6.23 ||**

## Padaccheda

```text
mūrdha-lābhī
na
mūla-cchit

kṣānti-lābhī
anapāya-gaḥ

śiṣya-gotrāt
nivartya
dve
buddhaḥ
syāt

trīṇi
api
itaraḥ
```

The transmitted sandhi **śiṣyagotrān nivartya** is understood as **śiṣyagotrāt nivartya**: “turning away from the lineage of a disciple.”

## Grammar

- **mūrdha-lābhī** — nominative singular masculine, possessive formation: “one who has attained the Summits.”
- **na mūla-cchit** — “does not cut the roots”; **mūla-cchit** is a nominative singular agent noun, “a cutter of roots.”
- **kṣānti-lābhī** — nominative singular masculine: “one who has attained Acceptance.”
- **anapāya-gaḥ** — nominative singular masculine: “one who does not go to a bad destiny.”
- **śiṣya-gotrāt** — ablative singular: “from the lineage of a disciple,” namely the Śrāvaka lineage.
- **nivartya** — absolutive of *ni-√vṛt*: “having turned away,” “having withdrawn.”
- **dve** — accusative dual neuter: “two,” referring to the first two preparations, Heat and Summits.
- **buddhaḥ syāt** — optative construction: “he may become a Buddha.”
- **trīṇi api** — accusative plural neuter: “even three,” referring to Heat, Summits, and Acceptance.
- **itaraḥ** — nominative singular masculine: “the other,” understood as the other type of Buddha, the Pratyekabuddha.

## Literal Translation

One who has attained the Summits does not cut off the roots. One who has attained Acceptance does not go to a bad destiny. Having turned away from the disciple-lineage after two, one may become a Buddha; after even three, the other.

## Philosophical Translation

Attainment of the Summits prevents the destruction of the wholesome roots, while attainment of Acceptance prevents rebirth in the painful destinies. A practitioner initially belonging to the Śrāvaka lineage may, after attaining the first two preparations, redirect the path toward complete Buddhahood; after attaining the first three, the path may still be redirected toward Pratyekabuddhahood.

# Successive Irreversibilities

## Summits

```text
mūrdhalābhī na mūlacchit
```

One who has obtained the Summits will no longer completely sever the wholesome roots.

```text
Heat
    wholesome roots may still be severed

Summits
    wholesome roots will not be severed
```

Here **mūla** means the wholesome roots previously classified as non-greed, non-hatred, and non-delusion.

## Acceptance

```text
kṣāntilābhy anapāyagaḥ
```

One who has attained Acceptance will no longer proceed to an **apāya**, a painful destiny:

```text
hell beings
animals
hungry spirits
```

Acceptance therefore establishes a stronger security than the Summits:

```text
Summits
    security of the wholesome roots

Acceptance
    security against painful rebirth
```

The preparations are not merely stronger versions of the same cognition. Each stage produces a determinate change in the practitioner’s possible future course.

# Gotra and Redirection

The second half concerns **gotra**, lineage or spiritual disposition.

```text
śiṣya-gotra
    lineage of the disciple
    Śrāvaka lineage
```

The verse indicates that this lineage is not absolutely fixed during the earlier preparations.

## After the first two

The **two** are:

```text
Heat
Summits
```

A practitioner who has cultivated these within the Śrāvaka lineage may turn away from that lineage and orient the path toward complete Buddhahood.

## After the first three

The **three** are:

```text
Heat
Summits
Acceptance
```

After Acceptance, redirection toward the “other Buddha”—the Pratyekabuddha—remains possible.

The verse therefore distinguishes two thresholds:

```text
after Heat and Summits:
    redirection toward complete Buddhahood remains possible

after Heat, Summits, and Acceptance:
    redirection toward Pratyekabuddhahood remains possible
```

The traditional interpretation understands **buddhaḥ** here as the fully awakened Buddha and **itaraḥ** as the Pratyekabuddha.

# Stage and Result

The verse presents a cumulative ordering:

```text
Heat
    initial preparatory transformation

Summits
    wholesome roots can no longer be severed

Acceptance
    painful destinies can no longer be reached

Highest Mundane Dharmas
    immediately precede the Path of Seeing
```

Thus increasing penetration is marked not only by stronger knowledge but by the progressive exclusion of incompatible possibilities.

# Doctrinal Determination

VAK 6.23 specifies:

```text
Summits:
    prevent severance of wholesome roots

Acceptance:
    prevents passage into painful destinies

Śrāvaka lineage after two preparations:
    may be redirected toward Buddhahood

Śrāvaka lineage after three preparations:
    may still be redirected toward Pratyekabuddhahood
```

This introduces **gotra** into the account of the preparations. The stages determine not only cognitive maturity but also which forms of future awakening remain possible.

# Logical Determination

```text
SummitAttainment {
    excludes:
        SeveranceOfWholesomeRoots
}

AcceptanceAttainment {
    excludes:
        RebirthInPainfulDestiny
}

DiscipleLineageAfterTwoPreparations {
    mayRedirectToward:
        CompleteBuddhahood
}

DiscipleLineageAfterThreePreparations {
    mayRedirectToward:
        Pratyekabuddhahood
}
```

# OWL++ Seed

```text
Class: WholesomeRootSeverance
Class: PainfulDestiny

Class: DiscipleLineage
Class: CompleteBuddhahood
Class: Pratyekabuddhahood

ObjectProperty: excludesFuturePossibility
ObjectProperty: mayRedirectToward
ObjectProperty: attainedStage

SummitAttainment
    excludesFuturePossibility WholesomeRootSeverance

AcceptanceAttainment
    excludesFuturePossibility PainfulDestiny

DiscipleLineageAfterTwoPreparations
    mayRedirectToward CompleteBuddhahood

DiscipleLineageAfterThreePreparations
    mayRedirectToward Pratyekabuddhahood
```

# Determinate Summary

```text
Attainment of the Summits:
    secures the wholesome roots

Attainment of Acceptance:
    secures the practitioner
    against painful rebirth

The earlier preparations:
    do not yet absolutely fix lineage

After the first two:
    Buddhahood remains possible

After the first three:
    Pratyekabuddhahood remains possible
```

The essential point is:

> **Each higher preparation excludes a deeper form of regression while progressively determining the possible direction of awakening.**
