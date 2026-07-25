# VAK 6.18

## Sanskrit

### Devanāgarī

उभयाकरणं धर्मेणान्यैरपि तु वर्धनम् ।
तेभ्यः क्षान्तिर्द्विधा तद्वत् क्षान्त्या धर्मेण वर्धनम् ॥ ६.१८ ॥

### IAST

**ubhayākaraṇaṃ dharmeṇānyair api tu vardhanam |**  
**tebhyaḥ kṣāntir dvidhā tadvat kṣāntyā dharmeṇa vardhanam || 6.18 ||**

## Padaccheda

- ubhaya-ākaraṇam
- dharmeṇa
- anyaiḥ api tu
- vardhanam
- tebhyaḥ
- kṣāntiḥ
- dvidhā
- tadvat
- kṣāntyāḥ
- dharmeṇa
- vardhanam

## Grammar

- **ubhaya-ākaraṇam** — nominative/accusative singular neuter: “the initial formation of both,” referring to Heat and the Summits.
- **dharmeṇa** — instrumental singular: “through the Dharma-Foundation.”
- **anyaiḥ api tu** — instrumental plural: “but also through the others,” namely the other three Foundations.
- **vardhanam** — nominative singular neuter: “development,” “increase,” “strengthening.”
- **tebhyaḥ** — ablative plural: “from those,” referring to the developed preceding stages.
- **kṣāntiḥ** — nominative singular feminine: “Acceptance,” “Receptivity,” or “Patience.”
- **dvidhā** — adverb: “in two forms” or “in two grades.”
- **tadvat** — indeclinable: “like that,” “in the same manner.”
- **kṣāntyāḥ** — genitive singular feminine: “of Acceptance.”
- **dharmeṇa vardhanam** — “its development is through the Dharma-Foundation.”

## Literal Translation

The initial formation of both is through the Dharma-Foundation, but their development is also through the others. From them arises Acceptance; in two forms it is like them. The development of Acceptance is through the Dharma-Foundation.

## Philosophical Translation

Heat and the Summits are first established through the Dharma-Foundation of Recollection, though their subsequent strengthening may proceed through all four Foundations. From their maturity arises Acceptance. Its lower and middle grades continue the previous pattern, while Acceptance as such is developed through the Dharma-Foundation alone.

## Doctrinal Determination

The verse distinguishes two operations:

- **ākaraṇa** — initial formation
- **vardhana** — subsequent strengthening

Heat and the Summits are first formed by arranging the sixteen aspects of the Four Truths through the Dharma-Foundation. Once formed, they may be strengthened through all four Foundations of Recollection.

From the developed Summits arises **kṣānti**. Here kṣānti is not ordinary patience but receptivity or acceptance toward the Truths. It has three grades: lower, middle, and highest. The first two continue the same object-structure as the preceding stages; the highest grade is treated in VAK 6.19.

The final restriction is important: Acceptance is developed through the Dharma-Foundation alone. The Path is becoming progressively more concentrated upon the Truth-structured Dharma-field.

## Logical Determination

```text
Heat {
    initiallyFormedBy: DharmaFoundation
    developedBy: FourFoundations
}

Summits {
    initiallyFormedBy: DharmaFoundation
    developedBy: FourFoundations
}

Acceptance {
    arisesFrom: Summits
    grades: [Lower, Middle, Highest]
    developedBy: DharmaFoundation
}
```

## OWL++ Seed

```text
Class: InitialFormation
Class: Development
Class: Heat
Class: Summit
Class: Acceptance
Class: LowerAcceptance
Class: MiddleAcceptance
Class: HighestAcceptance
Class: DharmaFoundation
Class: FourFoundations

ObjectProperty: initiallyFormedBy
ObjectProperty: developedBy
ObjectProperty: arisesFrom
ObjectProperty: hasGrade

Heat initiallyFormedBy DharmaFoundation
Heat developedBy FourFoundations
Summit initiallyFormedBy DharmaFoundation
Summit developedBy FourFoundations
Acceptance arisesFrom Summit
Acceptance developedBy DharmaFoundation
```

## Determinate Summary

- Heat and the Summits are initially formed through the Dharma-Foundation.
- They may later be strengthened through all four Foundations.
- From them arises Acceptance.
- Lower and middle Acceptance continue the preceding pattern.
- Acceptance is developed through the Dharma-Foundation alone.

## Commit Note

`Add VAK 6.18 formation, development, and the arising of Acceptance`
