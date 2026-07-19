# VAK 6.19

## Sanskrit

### Devanāgarī

कामाप्तदुःखविषया त्वधिमात्रा क्षणं च सा ।  
तथाग्रधर्माः सर्वे तु पञ्चस्कन्धा विनाप्तिभिः ॥ ६.१९ ॥

### IAST

**kāmāpta-duḥkha-viṣayā tv adhimātrā kṣaṇaṃ ca sā |**  
**tathāgradharmāḥ sarve tu pañcaskandhāḥ vināptibhiḥ || 6.19 ||**

## Padaccheda

- kāma-āpta-duḥkha-viṣayā
- tu
- adhimātrā
- kṣaṇam
- ca
- sā
- tathā
- agra-dharmāḥ
- sarve
- tu
- pañca-skandhāḥ
- vinā
- āptibhiḥ

## Grammar

- **kāmāpta-duḥkha-viṣayā** — nominative singular feminine, agreeing with an understood **adhimātrā kṣāntiḥ**: “having suffering belonging to the desire-domain as its object.”
- **tu** — “but,” marking the distinction of highest Acceptance from the lower two grades.
- **adhimātrā** — nominative singular feminine: “highest,” “strongest,” or “most intense.”
- **kṣaṇam** — accusative singular used adverbially: “for one moment.”
- **ca sā** — “and it,” referring to highest Acceptance.
- **tathā** — “likewise,” introducing the Highest Mundane Dharmas.
- **agra-dharmāḥ** — nominative plural masculine: “the Highest Mundane Dharmas.”
- **sarve tu pañca-skandhāḥ** — “all, however, consist of the five aggregates.”
- **vinā āptibhiḥ** — “without acquisitions”; the Bhāṣya identifies the excluded factor as **prāpti**.

## Literal Translation

But the highest Acceptance has the suffering belonging to the desire-domain as its object, and it lasts for one moment. The Highest Mundane Dharmas are likewise. All these consist of the five aggregates, excluding acquisitions.

## Philosophical Translation

The highest grade of Acceptance is restricted to the suffering of the desire-domain and occurs for a single moment. The Highest Mundane Dharmas have the same object and the same momentary duration. Although the preparatory stages are intrinsically Prajñā, their complete associated complex comprises the five aggregates, but excludes acquisition.

## Doctrinal Determination

### Highest Acceptance

The highest grade of **kṣānti** differs from its lower and middle forms. The object-range has been progressively contracted until only suffering in the desire-domain remains. This stage occurs for a single moment.

- lower and middle Acceptance retain the broader Truth-structure;
- highest Acceptance is restricted to desire-domain suffering;
- highest Acceptance lasts one moment.

### Highest Mundane Dharmas

The **laukikāgradharmas**, the Highest Mundane Dharmas, are “likewise”:

- their object is desire-domain suffering;
- their duration is one moment;
- they immediately precede the Path of Seeing.

They are the highest dharmas that still belong to the mundane domain.

### Intrinsic Nature and Complete Constitution

Heat, Summits, Acceptances, and Highest Mundane Dharmas are intrinsically **Prajñā**, because they belong to the structure of smṛtyupasthāna. When their full associated complex is counted, however, they comprise all five aggregates:

- rūpa
- vedanā
- saṃjñā
- saṃskāra
- vijñāna

The acquisitions associated with these states are excluded from the states themselves.

## Sequence

```text
Heat
    ↓
Summits
    ↓
Acceptance
    lower
    middle
    highest
    ↓
Highest Mundane Dharmas
    ↓
Path of Seeing
```

## Logical Determination

```text
HighestAcceptance {
    object: DesireDomainSuffering
    duration: OneMoment
}

HighestMundaneDharmas {
    object: DesireDomainSuffering
    duration: OneMoment
    immediatelyPrecedes: PathOfSeeing
}

PreparatoryPenetrationStage {
    intrinsicNature: Prajna
    completeConstitution: FiveAggregates
    excludes: Acquisition
}
```

## OWL++ Seed

```text
Class: HighestAcceptance
Class: HighestMundaneDharmas
Class: DesireDomainSuffering
Class: OneMoment
Class: FiveAggregates
Class: Acquisition
Class: PathOfSeeing

ObjectProperty: hasObject
ObjectProperty: hasDuration
ObjectProperty: immediatelyPrecedes
ObjectProperty: hasCompleteConstitution
ObjectProperty: excludes

HighestAcceptance hasObject DesireDomainSuffering
HighestAcceptance hasDuration OneMoment

HighestMundaneDharmas hasObject DesireDomainSuffering
HighestMundaneDharmas hasDuration OneMoment
HighestMundaneDharmas immediatelyPrecedes PathOfSeeing

PreparatoryPenetrationStage hasCompleteConstitution FiveAggregates
PreparatoryPenetrationStage excludes Acquisition
```

## Determinate Summary

Highest Acceptance takes desire-domain suffering as its object and lasts one moment. The Highest Mundane Dharmas have the same object and duration and immediately precede the Path of Seeing. All four preparatory stages are intrinsically Prajñā, comprise the five aggregates with their associates, and exclude acquisition.