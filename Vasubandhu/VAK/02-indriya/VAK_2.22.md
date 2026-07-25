# VAK_2.22 — Material Conjunction of Indriya

## 1. Sanskrit — Devanāgarī

```text
कामेऽष्टद्रव्यकोऽशब्दः परमाणुरनिन्द्रियः ।
कायेन्द्रियी नवद्रव्यः दशद्रव्योऽपरेन्द्रियः ॥ VAkK_2.22 ॥
```

## 2. Sanskrit — IAST

```text
kāme 'ṣṭadravyako 'śabdaḥ paramāṇur anindriyaḥ /
kāyendriyī navadravyaḥ daśadravyo 'parendriyaḥ // VAkK_2.22 //
```

Source form:

```text
kāme 'ṣṭadravyako 'śabdaḥ paramāṇuranindriyaḥ /
kāyendriyī navadravyaḥ daśadravyo 'parendriyaḥ // VAkK_2.22 //
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| kāme | kāme | locative singular | in the desire realm |
| aṣṭadravyakaḥ | aṣṭa-dravyakaḥ | masculine nominative singular compound | eight-substance / eight-dravya composite |
| aśabdaḥ | a-śabdaḥ | masculine nominative singular | without sound |
| paramāṇuḥ | paramāṇuḥ | masculine nominative singular | minimal atom / minimal material unit |
| anindriyaḥ | an-indriyaḥ | masculine nominative singular | without faculty |
| kāyendriyī | kāya-indriyī | masculine nominative singular | having the body-faculty |
| navadravyaḥ | nava-dravyaḥ | masculine nominative singular | nine-substance / nine-dravya composite |
| daśadravyaḥ | daśa-dravyaḥ | masculine nominative singular | ten-substance / ten-dravya composite |
| aparendriyaḥ | apara-indriyaḥ | masculine nominative singular | having another faculty |

## 4. Literal Translation

```text
In the desire realm, a minimal material unit without sound and without faculty is eight-dravya.
Having the body-faculty, it is nine-dravya; having another faculty, it is ten-dravya.
```

## 5. Philosophical Translation

```text
Within the desire realm, sensible givenness is not simple.

A minimal material unit without sound and without faculty is already an eightfold composite.
When body-faculty is present, the composite becomes ninefold.
When another faculty is present, the composite becomes tenfold.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| kāma | desire realm | Realm of sensuous embodiment and desire-conditioned givenness |
| dravya | substance / real constituent | Here: constituent item in a minimal material complex; not metaphysical Substance in the Hegelian sense |
| aṣṭadravyaka | eight-dravya composite | Minimal non-faculty material complex in the desire realm, without sound |
| śabda | sound | Explicitly excluded in the first case |
| paramāṇu | minimal atom / minimal material unit | Abhidharma material minimum; not modern physical atom |
| anindriya | without faculty | Material unit not bearing an indriya |
| kāyendriyī | having the body-faculty | Material unit with tactile/body faculty |
| navadravya | nine-dravya | Eightfold base plus body-faculty |
| aparendriya | having another faculty | Material unit bearing another faculty; to be checked with Bhāṣya for exact compositional implication |
| daśadravya | ten-dravya | Tenfold faculty-bearing composite |

## 7. Logical Determination

VAK_2.22 shifts from faculty-count and possession-profile to the material composition of faculty-bearing givenness.

```text
anindriya-paramāṇu
    = eightfold material conjunction

kāyendriyī-paramāṇu
    = ninefold material conjunction

aparendriya-paramāṇu
    = tenfold material conjunction
```

The dominant logical protocol is Conjunction:

```text
paramāṇu
    ≠ simple isolated unit

paramāṇu
    = minimal composite
    = dravya-conjunction
```

But the verse also contains Disjunction and Hypothetical structure:

```text
Disjunction:
    without faculty
    with body-faculty
    with another faculty

Hypothetical:
    if anindriya, then eight-dravya
    if kāyendriyī, then nine-dravya
    if aparendriya, then ten-dravya
```

Thus the material basis of indriya is already a logical configuration space.

## 8. Organon Interpretation

Organon reading:

```text
Indriya
    = governing efficacy
    = Kernel-side sensible givenness

Paramāṇu
    = minimal frame of sensible givenness
    = dravya-composite
```

VAK_2.22 shows that the Kernel Dataset is not built from simple atomic immediacies. Even the minimal unit is a composed feature-frame.

```text
Kernel Dataset
    Frame:
        realm = kāma
        unit = paramāṇu
        soundStatus = absent
        facultyStatus = none | body | other
        dravyaCount = 8 | 9 | 10
```

So the indriya-system implements a material feature model:

```text
sensible givenness
    = composed
    = counted
    = conditionally profiled
```

## 9. Indriya FeatureSet

```text
IndriyaMaterialFeatureSet:
    realmStatus
    soundStatus
    facultyPresence
    facultyType
    dravyaCount
    compositeProfile
```

The verse gives a compact rule-set:

```text
if realmStatus = kāma
and soundStatus = absent
and facultyPresence = none
then dravyaCount = 8

if facultyType = kāya-indriya
then dravyaCount = 9

if facultyType = apara-indriya
then dravyaCount = 10
```

This is why VAK_2.22 is a good bridge from indriya classification to Dataset architecture:

```text
Indriya
    is not merely listed.

Indriya
    is materially implemented as a feature-bearing configuration.
```

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:Paramanu a rdfs:Class ;
    rdfs:label "paramāṇu" ;
    rdfs:comment "Minimal material unit or frame of sensible givenness." .

vak:IndriyaMaterialProfile a rdfs:Class ;
    rdfs:label "Indriya Material Profile" ;
    rdfs:comment "A material feature-profile defined by realm, sound-status, faculty-status, and dravya-count." .

vak:hasRealmStatus a rdf:Property ;
    rdfs:label "has realm status" .

vak:hasSoundStatus a rdf:Property ;
    rdfs:label "has sound status" .

vak:hasFacultyStatus a rdf:Property ;
    rdfs:label "has faculty status" .

vak:hasDravyaCount a rdf:Property ;
    rdfs:label "has dravya count" .

vak:AnindriyaParamanuProfile a vak:IndriyaMaterialProfile ;
    vak:hasRealmStatus vak:KamaRealm ;
    vak:hasSoundStatus vak:SoundAbsent ;
    vak:hasFacultyStatus vak:NoFaculty ;
    vak:hasDravyaCount 8 .

vak:KayendriyiParamanuProfile a vak:IndriyaMaterialProfile ;
    vak:hasRealmStatus vak:KamaRealm ;
    vak:hasFacultyStatus vak:BodyFaculty ;
    vak:hasDravyaCount 9 .

vak:AparendriyaParamanuProfile a vak:IndriyaMaterialProfile ;
    vak:hasRealmStatus vak:KamaRealm ;
    vak:hasFacultyStatus vak:OtherFaculty ;
    vak:hasDravyaCount 10 .
```

## 11. Commit History

```text
VAK_2.22 opened.
Method: kārikā-first speculative seed.
Theme: material conjunction of indriya-bearing givenness.
Logical protocols recorded: conjunction, disjunction, and hypothetical feature rules.
Organon mapping: paramāṇu as minimal Kernel Dataset frame.
Dense dravya mechanics marked for later Bhāṣya verification.
Zero-padded file naming maintained: VAK_2.22.
```
