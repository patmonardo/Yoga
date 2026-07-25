# VAK_3b — VAkK_3.44

## Sanskrit — Devanāgarī

अधोनृसुरगाजानां मर्मच्छेदस्त्वबादिभिः ।
सम्यङ् मिथ्यात्वनियताः आर्यानन्तर्यकारिणः ॥ VAkK_3.44 ॥

## Sanskrit — IAST

adhonṛsuragājānāṃ marmacchedas tv abādibhiḥ /
samyaṅ mithyātvaniyatā āryānantaryakāriṇaḥ // VAkK_3.44 //

## Source Caution

The source reads:

```text
adhonṛsuragājānāṃ marmacchedastvabādibhiḥ /
samyaṅ mithyātvaniyatā āryānantaryakāriṇaḥ // VAkK_3.44 //
```

This closes the death/transition discussion before VAkK_3.45 begins the outer container-world (`bhājanaloka`). The compounds are dense and should be checked carefully against the Bhāṣya.

## Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| adhonṛsuragājānām | adho-nṛ-sura-gā-jānām | of those going downward, humans, gods, and birth-groups; provisional |
| marmacchedaḥ | marma-chedaḥ | cutting of vital points |
| tu | tu | but / however |
| abādibhiḥ | ab-ādibhiḥ | by water and so forth; provisional |
| samyak | samyak | right / correct |
| mithyātva | mithyātva | wrongness / false orientation |
| niyatāḥ | niyatāḥ | determined / fixed |
| āryāḥ | āryāḥ | noble ones |
| ānantaryakāriṇaḥ | ānantarya-kāriṇaḥ | doers of immediate-result actions |

## Grammar

```text
adho-nṛ-sura-gā-jānām
    = of downward-going, human, and divine birth-groups; provisional

marma-chedaḥ tu ab-ādibhiḥ
    = but the cutting of vital points is by water and so forth

samyak-mithyātva-niyatāḥ
    = those fixed in rightness or wrongness

āryāḥ ānantarya-kāriṇaḥ
    = noble ones and doers of ānantarya actions
```

## Literal Translation

For those going downward, humans, gods, and birth-groups, there is cutting of vital points by water and so forth. Those fixed in rightness or wrongness are noble ones and doers of immediate-result actions.

## Philosophical Translation

The closing verse of this block completes the analysis of transition by referring to the severance of vital points and to beings whose orientation is fixed: those fixed in rightness, those fixed in wrongness, noble ones, and performers of immediate-result actions. The exact technical distribution remains Bhāṣya-dependent.

## Technical Vocabulary

| Sanskrit | Working translation | Note |
|---|---|---|
| adho-ga | downward-going | Direction toward lower destiny; provisional within compound |
| nṛ | human | Human destiny or class |
| sura | god / deva | Divine destiny or class |
| marma | vital point | Critical life-point |
| cheda | cutting / severance | Severing process |
| ab-ādi | water and so forth | Instrumental series; requires Bhāṣya control |
| samyak | right / correct | Right orientation |
| mithyātva | wrongness | Wrong orientation |
| niyata | fixed / determined | Determinate orientation |
| ārya | noble one | Path-attained person |
| ānantarya-kārin | doer of immediate-result action | Performer of grave action with immediate karmic result |

## Doctrinal Determination

VAkK_3.42–3.43 analyzed transition:

```text
manovijñāna
upekṣā
avyākṛta register
krama-cyuti
```

VAkK_3.44 closes this micro-section by adding two determinations.

First, transition involves `marma-cheda`, severance at vital points:

```text
marma-cheda
    = cutting / severance of vital points
```

Second, beings can be fixed in orientation:

```text
samyaktva-niyata
mithyātva-niyata
ārya
ānantarya-kārin
```

This is the final internal marker before the text turns outward to `bhājanaloka` in 3.45.

## Logical Determination

The block closes by showing that conditioned transition has both bodily and moral-orientational determination.

```text
transition
    has bodily severance
    has orientation-fixity
```

This prepares the next large movement:

```text
inner world of conditioned experience
    → outer container-world
```

## Interpretive Note

This verse concludes the first human-experience block of Lokanirdeśa. The path-relevant point is that the wheel is not only biological, psychological, or cosmological. It is also orientational.

```text
samyak / mithyā
    right orientation / wrong orientation
```

This anticipates the later path-discrimination between what is Path and what is not Path.

## Organon Interpretation

Light contact point:

```text
The wheel has transition-features and orientation-features.
```

The first block has now shown the world of conditioned experience as a field of features:

```text
contact
feeling
mental approach
kleśa
karma
vastu
nutriment
transition
orientation
```

This is the Rational-Empirical Field that will later be discriminated as Path and not-Path.

## OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_44
    a vak:Karika ;
    rdfs:label "VAkK 3.44" ;
    vak:continues vak:VAK_3_43 ;
    vak:hasTopic vak:MarmaCheda ;
    vak:hasTopic vak:OrientationFixity ;
    vak:closesBlock vak:HumanExperienceWorld .

vak:MarmaCheda
    a logic:TransitionFeature ;
    rdfs:label "marma-cheda" ;
    vak:hasCanonicalTranslation "severance of vital points" .

vak:OrientationFixity
    a logic:PathOrientation ;
    rdfs:label "samyaktva / mithyātva niyatatā" .
```

## Commit Note

Committed VAK_3b / VAkK_3.44.

Established:
- the death/transition block is closed.
- transition includes severance of vital points and determinate orientation.
- 3.44 concludes the first inner human-experience block before 3.45 begins the larger container-world.
