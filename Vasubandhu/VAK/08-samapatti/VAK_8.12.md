# VAK_8.12 — Feelings in the Dhyāna Rebirths

## Sanskrit

### Devanāgarī

```text
सौमनस्यसुखोपेक्षा उपेक्षासुमनस्कते ।
सुखोपेक्षे उपेक्षा प्रविदो ध्यानोपपत्तिषु ॥ ८.१२ ॥
```

### IAST

```text
saumanasyasukhopekṣā upekṣāsumanaskate /
sukhopekṣe upekṣā pravido dhyānopapattiṣu // VAK_8.12 //
```

## Source Caution

The transmitted text is highly compressed and the form `pravido` is opaque in isolation. The doctrinal distribution is nevertheless clear from the sequence and the bhāṣya tradition: the four dhyāna rebirths are being distinguished by the feelings present in each.

This first kārikā pass therefore preserves the source reading while treating the line as an ordered fourfold distribution.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| saumanasya | nominative singular neuter | mental gladness; satisfaction |
| sukha | nominative singular neuter | pleasure; ease |
| upekṣā | nominative singular feminine | equanimity; neutral feeling |
| upekṣā-sumanaskate | compressed dual expression | equanimity and mental gladness |
| sukha-upekṣe | nominative dual neuter | pleasure and equanimity |
| upekṣā | nominative singular feminine | equanimity alone |
| dhyāna-upapattiṣu | locative plural | in the rebirths corresponding to the dhyānas |

## Grammar

The verse is an elliptical ordered list. The understood frame is:

```text
in the rebirth corresponding to the first dhyāna
    saumanasya, sukha, and upekṣā

in the rebirth corresponding to the second dhyāna
    upekṣā and saumanasya

in the rebirth corresponding to the third dhyāna
    sukha and upekṣā

in the rebirth corresponding to the fourth dhyāna
    upekṣā
```

The kārikā therefore does not merely repeat the feelings present in meditative attainment. It distinguishes the affective constitution of the corresponding rebirth-realms.

## Literal Translation

In the rebirths corresponding to the dhyānas there are, respectively: mental gladness, pleasure, and equanimity; equanimity and mental gladness; pleasure and equanimity; and equanimity.

## Philosophical Translation

The four dhyāna worlds are differentiated by their fields of feeling. The first still permits mental gladness, pleasure, and equanimity; the second, mental gladness and equanimity; the third, pleasure and equanimity; and the fourth, equanimity alone. The ascent through the form realm is therefore also a staged purification of affect.

## Technical Vocabulary

### saumanasya

```text
saumanasya
    mental gladness
    affective satisfaction
    joy on the mental side
```

It should not be collapsed into bodily ease. The distinction between `saumanasya` and `sukha` allows the Kośa to classify mental and bodily feeling separately.

### sukha

```text
sukha
    pleasure
    ease
    agreeable feeling
```

Within this distribution, `sukha` remains present in the first and third dhyāna rebirths but not in the second or fourth.

### upekṣā

```text
upekṣā
    equanimity
    neutral feeling
    evenness
```

Unlike the other feelings, equanimity extends through all four dhyāna rebirths.

This continuity is significant:

```text
first dhyāna rebirth
    upekṣā present

second dhyāna rebirth
    upekṣā present

third dhyāna rebirth
    upekṣā present

fourth dhyāna rebirth
    upekṣā alone
```

## Doctrinal Determination

VAK 8.12 distinguishes the affective structure of the four form-realm rebirths.

| Dhyāna rebirth | Feelings present |
|---|---|
| First | saumanasya, sukha, upekṣā |
| Second | saumanasya, upekṣā |
| Third | sukha, upekṣā |
| Fourth | upekṣā alone |

The sequence is not a simple monotonic subtraction of all feeling. Instead, different kinds of feeling are selectively removed.

```text
mental gladness
    present in first and second
    absent in third and fourth

pleasure
    present in first and third
    absent in second and fourth

equanimity
    present throughout
    exclusive in the fourth
```

The fourth dhyāna rebirth is thus affectively immovable because the oscillation among gladness, pleasure, and their opposites has been reduced to equanimity alone.

## Logical Determination

The verse gives a qualitative matrix rather than a single linear scale.

```text
levels
    first
    second
    third
    fourth

qualities
    saumanasya
    sukha
    upekṣā
```

The levels are distinguished by different combinations of these qualities.

```text
first
    {saumanasya, sukha, upekṣā}

second
    {saumanasya, upekṣā}

third
    {sukha, upekṣā}

fourth
    {upekṣā}
```

This is a precise example of staged qualitative logic:

```text
purification
    does not mean emptying all content

purification
    means removing determinations
    until the proper qualitative whole remains
```

## Organon Light

The immediate doctrinal point should remain primary: the dhyāna rebirths are distinguished by their affective constitution.

Still, the structure is important for the larger project. Each stage is not merely numerically higher. It is a determinate reconfiguration of feeling.

```text
science of stages
    requires
science of qualitative composition
```

The fourth dhyāna is therefore not empty neutrality. It is the completed dominance of `upekṣā` within the form realm.

The broader movement toward ārūpya remains ahead. The present verse completes the feeling-logic of the rūpa-dhātu rebirths before the chapter resumes its analysis of the attainments and their transitions.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix dhy: <http://127.0.0.1:3000/dhyana#> .
@prefix ved: <http://127.0.0.1:3000/vedana#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_8_12
    a vak:Karika ;
    rdfs:label "VAK 8.12" ;
    vak:determines dhy:AffectiveDistributionAcrossDhyanaRebirths .

dhy:FirstDhyanaRebirth
    ved:hasFeeling ved:Saumanasya,
                   ved:Sukha,
                   ved:Upeksha .

dhy:SecondDhyanaRebirth
    ved:hasFeeling ved:Saumanasya,
                   ved:Upeksha .

dhy:ThirdDhyanaRebirth
    ved:hasFeeling ved:Sukha,
                   ved:Upeksha .

dhy:FourthDhyanaRebirth
    ved:hasFeeling ved:Upeksha .
```

## Commit History

```text
2026-07-25 — Initial kārikā-pass analysis.
```
