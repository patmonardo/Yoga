# VAK_2.32 — Ethical Paired Caitta Determinations

## 1. Sanskrit — Devanāgarī

```text
अह्रीरगुरुता अवद्ये भयादर्शित्वमत्रपा ।
प्रेम श्रद्धा गुरुत्वं ह्रीः ते पुनः कामरूपयोः ॥ VAkK_2.32 ॥
```

## 2. Sanskrit — IAST

```text
ahrīr agurutā avadye bhayādarśitvam atrapā /
prema śraddhā gurutvaṃ hrīḥ te punaḥ kāmarūpayoḥ // VAkK_2.32 //
```

Source form:

```text
ahrīragurutā avadye bhayādarśitva matrapā /
prema śraddhā gurutvaṃ hrīḥ te punaḥ kāmarūpayoḥ // VAkK_2.33 //
```

## 3. Textual Caution

The local source marks this verse as `VAkK_2.33`, and then marks the following verse also as `VAkK_2.33`.

For working repo continuity, this file normalizes the first duplicated `2.33` as `VAK_2.32`.

```text
Source numbering:
    first duplicated VAkK_2.33

Working numbering:
    VAK_2.32
```

The sandhi and segmentation around `bhayādarśitva matrapā` should be checked later against the Bhāṣya and printed editions.

## 4. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| ahrīḥ | a-hrīḥ | feminine nominative singular | absence of hrī / shamelessness |
| agurutā | a-gurutā | feminine nominative singular | lack of seriousness / lack of respect |
| avadye | avadye | locative singular | regarding the blameworthy |
| bhaya-adarśitvam | bhaya-adarśitvam | neuter nominative singular compound | not seeing danger / absence of fear-recognition |
| atrapā | a-trapā | feminine nominative singular | lack of restraint / absence of moral concern |
| prema | prema | neuter nominative singular | affection / fondness |
| śraddhā | śraddhā | feminine nominative singular | confidence |
| gurutvam | gurutvam | neuter nominative singular | seriousness / respect / weightiness |
| hrīḥ | hrīḥ | feminine nominative singular | inward moral shame / self-respect |
| te | te | pronoun, nominative plural | these |
| punaḥ | punaḥ | indeclinable | again / furthermore |
| kāma-rūpayoḥ | kāma-rūpayoḥ | locative dual | in the desire and form realms |

## 5. Literal Translation

```text
Ahrī is lack of seriousness regarding the blameworthy.
Atrapā is not seeing danger there.

Prema, śraddhā, seriousness, and hrī occur again in the desire and form realms.
```

## 6. Philosophical Translation

```text
The catalog now discriminates paired ethical determinations.

Shamelessness and lack of moral concern are defined through a failure to take the blameworthy seriously and a failure to see danger in it.
Their positive counterparts — affection, confidence, seriousness, and hrī — are again located within the desire and form realms.
```

## 7. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| ahrī | shamelessness / absence of hrī | Negative ethical feature |
| agurutā | lack of seriousness / lack of respect | Absence of weightiness toward what matters |
| avadya | blameworthy | Object-domain of ethical evaluation |
| bhayādarśitva | not seeing danger | Failure to recognize danger in the blameworthy |
| atrapā | absence of moral concern | Negative counterpart to apatrapā / trapā; segmentation to verify |
| prema | affection / fondness | Positive relational feature |
| śraddhā | confidence | Also wholesome caitta and pure faculty |
| gurutva | seriousness / respect / weight | Positive counterpart to agurutā |
| hrī | moral self-respect | Positive ethical restraint |
| kāma-rūpa | desire and form realms | Realm-location for the listed factors |

## 8. Logical Determination

VAK_2.32 refines the caitta catalog by giving paired determinations.

```text
negative ethical features:
    ahrī
    atrapā

positive or stabilizing features:
    prema
    śraddhā
    gurutva
    hrī
```

The dominant protocol is Discriminative Opposition:

```text
agurutā
    opposed to
    gurutva

ahrī
    opposed to
    hrī

failure to see danger
    opposed to
    ethical recognition of the blameworthy
```

This is a feature-level logic of Appearance:

```text
Citta-Caitta
    = appearance-law
    = how the field is configured either toward clarity or distortion
```

## 9. Relation to Indriya

The indriya-system gives governing efficacy as faculty-givenness.

This verse shows how caittas configure that givenness ethically:

```text
Indriya
    = faculty-givenness

Caitta
    = ethical and affective configuration of the citta-field
```

The same faculty-givenness can be configured through:

```text
lack of seriousness
lack of danger-recognition
or
confidence, seriousness, and hrī
```

Thus caitta is not merely a mental add-on. It is the law by which appearance becomes ethically qualified.

## 10. Organon Interpretation

Organon reading:

```text
EthicalCaittaPairing:
    negativeFeature = ahrī | atrapā
    positiveFeature = śraddhā | gurutva | hrī
    realmScope = kāma | rūpa
```

Learning implication:

```text
The Agent must detect not only feature-presence,
but paired oppositions within the field of appearance.
```

This is discriminative knowledge of ethical feature-polarity.

## 11. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:EthicalCaittaDetermination a rdfs:Class ;
    rdfs:label "Ethical Caitta Determination" ;
    rdfs:comment "A paired ethical feature of the citta-field." .

vak:Ahrī a vak:EthicalCaittaDetermination .
vak:Atrapā a vak:EthicalCaittaDetermination .
vak:Prema a vak:EthicalCaittaDetermination .
vak:Śraddhā a vak:EthicalCaittaDetermination .
vak:Gurutva a vak:EthicalCaittaDetermination .
vak:Hrī a vak:EthicalCaittaDetermination .

vak:hasOpposedFeature a rdf:Property ;
    rdfs:label "has opposed feature" .

vak:Ahrī vak:hasOpposedFeature vak:Hrī .
vak:Agurutā vak:hasOpposedFeature vak:Gurutva .
```

## 12. Commit History

```text
VAK_2.32 opened.
Method: kārikā-first speculative seed.
Theme: ethical paired caitta determinations.
Source numbering caution recorded: first duplicated VAkK_2.33 normalized as VAK_2.32.
Logical protocols recorded: discriminative opposition and ethical feature-pairing.
Relation to indriya tracked: caitta as ethical configuration of faculty-givenness in appearance.
Zero-padded file naming maintained: VAK_2.32.
```
