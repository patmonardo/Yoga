# VAK_8.31

## Sanskrit

ध्यानयोर्मुदिता अन्यानि षट्सु केचित्तु पञ्चसु ।
न तैः प्रहाणं नृष्वेव जन्यन्ते त्र्यन्वितो ध्रुवम् ॥

## IAST

dhyānayor muditā anyāni ṣaṭsu kecit tu pañcasu /
na taiḥ prahāṇaṃ nṛṣv eva janyante tryanvito dhruvam //

## Source and Segmentation Caution

The verse closes the classification of the four apramāṇas. Its compressed syntax distributes the four across meditative levels, denies them the function of directly abandoning the afflictions, restricts their initial production to human existence, and adds a final accompaniment rule whose exact scope should be checked against the bhāṣya.

## Padaccheda

dhyānayoḥ | muditā | anyāni | ṣaṭsu | kecit | tu | pañcasu | na | taiḥ | prahāṇam | nṛṣu | eva | janyante | tri-anvitaḥ | dhruvam

## Grammar

- **dhyānayoḥ** — locative dual: in the two Dhyānas
- **muditā** — sympathetic joy
- **anyāni** — the others, namely the remaining three immeasurables
- **ṣaṭsu** — in six levels or grounds
- **kecit tu pañcasu** — but some hold that they occur in five
- **na taiḥ prahāṇam** — abandonment is not effected by them
- **nṛṣu eva janyante** — they are first generated only among humans
- **tri-anvitaḥ dhruvam** — certainly accompanied by three; the precise referent is compressed and requires bhāṣya control

## Literal Translation

Sympathetic joy occurs in the two Dhyānas; the others occur in six levels, though some say in five. Abandonment is not effected by them. They are generated only among humans. One is certainly accompanied by three.

## Philosophical Translation

The four immeasurables are distributed across determinate meditative levels. Sympathetic joy has the narrower range of the first two Dhyānas, while friendliness, compassion, and equanimity extend across a broader set of grounds. Yet none of the four directly severs the afflictions. They are cultivated transformations of relation, first generated in human existence, not substitutes for the path of abandonment.

## Technical Vocabulary

- **muditā** — sympathetic joy
- **dhyāna** — determinate meditative level
- **bhūmi** — level or ground, implied by the locative numerals
- **prahāṇa** — abandonment or severance of affliction
- **janyante** — are generated or first produced
- **nṛṣu** — among human beings
- **anvita** — accompanied or conjoined

## Doctrinal Determination

VAK_8.31 completes the apramāṇa complex by fixing four limits:

1. **Level-distribution** — the immeasurables are not all supported by exactly the same meditative range.
2. **Non-abandoning function** — they counteract hostile, cruel, envious, and appropriative tendencies, but they do not by themselves effect prahāṇa.
3. **Human generation** — their initial production belongs specifically to human existence.
4. **Accompaniment** — the final phrase supplies a conjunction rule whose exact doctrinal assignment remains provisional until the bhāṣya pass.

The decisive point is that universal benevolence and liberation from affliction are related but not identical achievements.

## Logical Determination

The apramāṇas universalize the practical relation to beings, but universality of relation is not yet the negative power of severance.

```text
counter-practice
    ≠
abandonment
```

They transform how the field is inhabited, while prahāṇa removes the afflictive ground itself. The verse therefore prevents the Brahma-vihāras from being inflated into a complete theory of liberation.

## Organon Interpretation

The human field is not treated here as an inferior accident. It is the determinate sphere in which universal relation can first be consciously generated.

```text
human finitude
    → cultivation of unrestricted relation
    → meditative stabilization
```

But the universal relation remains distinct from the path-act that severs bondage. This is an important boundary between Buddha-Mind as universal responsiveness and Arhat-function as abandonment.

The two must cooperate without being conflated:

```text
apramāṇa
    universalizes relation

prahāṇa
    removes the afflictive condition
```

## OWL++ Seed

```turtle
@prefix vak: <https://organon.example/vak/> .
@prefix dharma: <https://organon.example/dharma/> .

vak:VAK_8_31 a vak:Karika ;
    vak:chapter "Samapattinirdesa" ;
    vak:verseNumber "8.31" ;
    vak:determines dharma:ApramanaLevelDistribution,
                   dharma:NonAbandoningFunction,
                   dharma:HumanGeneration ;
    vak:statesDistinctFrom dharma:Prahaṇa .

dharma:Mudita vak:supportedBy dharma:TwoDhyanas .

dharma:OtherThreeApramanas vak:supportedBy dharma:SixLevels ;
    vak:hasAlternativeClassification dharma:FiveLevels .
```

## Commit History

First-pass kārikā analysis committed after identifying VAK_8.31 as the closing verse of the four immeasurables and preserving the compressed final accompaniment rule as provisional pending the bhāṣya pass.
