# VAK_7.34 — The Equality of the Buddhas

## Sanskrit

### Devanāgarī

```text
संभारधर्मकायाभ्यां जगतश्चार्थचर्यया ।
समता सर्वबुद्धानां नायुर्जातिप्रमाणतः ॥ ७.३४ ॥
```

### IAST

```text
saṃbhāra-dharma-kāyābhyāṃ jagataś cārtha-caryayā /
samatā sarva-buddhānāṃ nāyur-jāti-pramāṇataḥ // VAK_7.34 //
```

## Source Caution

The verse follows VAK_7.33 on great compassion and determines the respects in which all Buddhas are equal and the respects in which they differ.

The first-pass reading should preserve the contrast:

```text
essential equality
    accumulation
    Dharma-body
    activity for the welfare of the world

manifest difference
    lifespan
    birth
    bodily measure
```

The term `dharma-kāya` is retained without importing a later fully developed three-body theory.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| saṃbhāra | nominal stem within compound | accumulation, collected equipment |
| dharma-kāyābhyām | instrumental dual | by accumulation and Dharma-body |
| jagataḥ | genitive singular | of the world |
| ca | conjunction | and |
| artha-caryayā | instrumental singular feminine | by activity for benefit or welfare |
| samatā | nominative singular feminine | equality |
| sarva-buddhānām | genitive plural | of all Buddhas |
| na | negation | not |
| āyuḥ | nominal stem | lifespan |
| jāti | nominal stem | birth |
| pramāṇataḥ | ablative adverbial formation | with respect to measure or magnitude |

## Grammar

The governing judgment is:

```text
samatā sarva-buddhānām
    equality of all Buddhas
```

The instrumental expressions state the grounds of equality:

```text
saṃbhāra-dharma-kāyābhyām
    by accumulation and Dharma-body

jagataḥ artha-caryayā
    by activity for the welfare of the world
```

The concluding negation restricts the assertion:

```text
na āyur-jāti-pramāṇataḥ
    not with respect to lifespan,
    birth,
    or bodily measure
```

## Literal Translation

All Buddhas are equal with respect to accumulation, Dharma-body, and activity for the welfare of the world, but not with respect to lifespan, birth, or bodily measure.

## Philosophical Translation

All Buddhas possess equality in the perfected accumulation that grounds awakening, in the Dharma-constitution realized through awakening, and in their activity for the welfare of the world. This equality does not require empirical uniformity: lifespan, circumstances of birth, and bodily magnitude may differ.

## Technical Vocabulary

### saṃbhāra

```text
saṃbhāra
    accumulation
    collected equipment
    cultivated conditions supporting Buddhahood
```

The term indicates the completed preparatory constitution required for Buddha-knowledge and Buddha-activity.

### dharma-kāya

```text
dharma-kāya
    Dharma-body
    the Buddha as constituted by perfected dharmas
```

The visible Buddha may differ in lifespan and bodily measure, while the realized Dharma-constitution of Buddhahood remains equal.

### artha-caryā

```text
artha
    benefit
    welfare

caryā
    activity
    operative conduct
```

Thus `jagataḥ artha-caryā` is activity for the welfare of the world. It is the objective manifestation of the great compassion determined in VAK_7.33.

### samatā

```text
samatā
    equality
    identity in a determinate respect
```

Equality does not abolish difference. It states sameness under a specified universal.

### pramāṇa

Here `pramāṇa` means measure or bodily magnitude, not principle of knowing. The local grammatical field governs the translation.

## Doctrinal Determination

The verse establishes three grounds of Buddha-equality:

```text
all Buddhas
    complete the requisite accumulation

all Buddhas
    realize the same perfected Dharma-constitution

all Buddhas
    act for the welfare of beings
```

It also establishes three empirical differences:

```text
lifespan
birth
bodily measure
```

These are differences of manifestation, not deficiencies in Buddhahood.

## Logical Determination

The verse gives a qualified identity judgment:

```text
A and B are equal
    with respect to U

A and B differ
    with respect to P
```

Thus:

```text
Buddhahood
    is one in essential determination

Buddhas
    are many in manifestation
```

This is determinate equality rather than numerical identity or vague resemblance.

## Organon Light

The verse distinguishes formation, constitution, and operation:

```text
saṃbhāra
    accumulated formation

dharma-kāya
    realized constitution

artha-caryā
    effective manifestation
```

These three incarnate the higher determination:

```text
Buddha-samatā
    equality of Buddhahood
```

The triple is not transcendental. The unity is not one member of the triple but the higher Idea expressed through all three.

A further working insight emerged in discussion:

```text
same rational form
    does not mean
same empirical development
```

For humans and Buddhas alike, empirical form may differ while rational form remains the same. The deeper question concerns the ground of differential manifestation: karma, guṇa, and conditioned buddhi. This belongs to the larger Jñānanirdeśa inquiry and should be developed without displacing the first-pass kārikā analysis.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix path: <http://127.0.0.1:3000/path#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_34
    a vak:Karika ;
    rdfs:label "VAK 7.34" ;
    vak:determines path:BuddhaEquality ;
    vak:distinguishes path:EssentialBuddhaEquality,
                      path:ManifestBuddhaDifference .

path:BuddhaEquality
    a logic:DeterminateEquality ;
    path:hasGround path:Accumulation,
                   path:DharmaBody,
                   path:WorldBenefitingActivity .

path:EssentialBuddhaEquality
    path:hasRespect path:Accumulation,
                    path:DharmaBody,
                    path:WorldBenefitingActivity .

path:ManifestBuddhaDifference
    path:hasRespect path:Lifespan,
                    path:Birth,
                    path:BodilyMeasure .

path:WorldBenefitingActivity
    path:hasObjectField path:World ;
    path:expresses path:GreatCompassion .
```

## Commit History

```text
2026-07-24 — Initial kārikā-pass analysis for VAK_7c.
```
