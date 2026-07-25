# VAK 6.17

## Sanskrit

### Devanāgarī

तत ऊष्मगतोत्पत्तिस्तच्चतुःसत्यगोचरम् ।
षोडशाकारमूष्मभ्यो मूर्धानस्तेऽपि तादृशाः ॥ ६.१७ ॥

### IAST

`tata ūṣmagatotpattis tac catuḥsatya-gocaram |`
`ṣoḍaśākāram ūṣmabhyo mūrdhānas te ’pi tādṛśāḥ || 6.17 ||`

## Padaccheda

`tataḥ | uṣmagata-utpattiḥ | tat | catuḥ-satya-gocaram | ṣoḍaśa-ākāram | uṣmabhyaḥ | mūrdhānaḥ | te | api | tādṛśāḥ`

## Grammar

- **tataḥ** — ablative singular used adverbially: “from that,” referring to the cultivated Dharma-Foundation of VAK 6.16.
- **uṣmagata-utpattiḥ** — nominative singular feminine compound: “the arising of Heat.”
- **tat** — nominative singular neuter pronoun referring to *uṣmagata*.
- **catuḥsatya-gocaram** — nominative singular neuter agreeing with *tat*: “having the Four Truths as its cognitive range.”
- **ṣoḍaśākāram** — nominative singular neuter agreeing with *tat*: “having sixteen aspects.”
- **uṣmabhyaḥ** — ablative plural: “from the Heats,” collectively “from Heat.”
- **mūrdhānaḥ** — nominative plural masculine: “the Summits.”
- **te api** — “they too.”
- **tādṛśāḥ** — nominative plural masculine: “of the same kind.”

## Literal Translation

From that arises Heat. It has the Four Truths as its cognitive range and possesses sixteen aspects. From Heat arise the Summits; they too are of the same kind.

## Philosophical Translation

From the cultivated Dharma-Foundation arises the stage called Heat. Its object-field is the Four Truths, examined through sixteen aspects. From Heat arise the Summits, which retain the same object-field and the same sixteenfold structure.

## Doctrinal Determination

The opening **tataḥ** links Heat directly to the repeatedly cultivated Dharma-Foundation of the preceding verse. The Bhāṣya calls Heat a wholesome root and the preliminary sign of the fire of the Noble Path because the latter burns the fuel of the afflictions.

Heat is therefore preparatory rather than yet the Noble Path itself.

Its object is the Four Truths:

1. suffering,
2. origin,
3. cessation,
4. Path.

Each is examined under four aspects, producing sixteen aspects in total:

- suffering: impermanent, suffering, empty, not-self;
- origin: cause, arising, production, condition;
- cessation: cessation, peace, excellence, release;
- Path: Path, right method, practice, leading outward.

The Summits arise from Heat. Their object and aspect-structure are the same. Their distinction lies in superior strength and maturity.

## Logical Determination

```text
DharmaFoundation
    → Heat

Heat {
    objectRange: FourTruths
    aspectCount: Sixteen
}

Heat
    → Summits

Summits {
    objectRange: FourTruths
    aspectCount: Sixteen
    strength: GreaterThanHeat
}
```

## OWL++ Seed

```text
Class: PreparatoryPenetration
Class: Heat
Class: Summit
Class: FourTruths
Class: SixteenAspects

ObjectProperty: arisesFrom
ObjectProperty: hasObjectRange
ObjectProperty: hasAspectStructure
ObjectProperty: strongerThan

Heat SubClassOf PreparatoryPenetration
Summit SubClassOf PreparatoryPenetration

Heat SubClassOf arisesFrom some DharmaFoundation
Heat SubClassOf hasObjectRange only FourTruths
Heat SubClassOf hasAspectStructure only SixteenAspects

Summit SubClassOf arisesFrom some Heat
Summit SubClassOf hasObjectRange only FourTruths
Summit SubClassOf hasAspectStructure only SixteenAspects
Summit strongerThan Heat
```

## Determinate Summary

From the cultivated Dharma-Foundation arises Heat. Heat takes the Four Truths as object through sixteen aspects. From Heat arise the Summits, preserving the same object and aspect-structure at a stronger stage of cultivation.
