# VAK_2.09 — Pure Faculties, Material Faculties, and Outflow Classification

## 1. Sanskrit — Devanāgarī

```text
दृग्भावनाशैक्षपथे नव त्रीणि अमलं त्रयम् ।
रूपीणि जीवितं दुःखे सास्रवाणि द्विधा नव ॥ VAkK_2.9 ॥
```

## 2. Sanskrit — IAST

```text
dṛgbhāvanāśaikṣapathe nava trīṇi amalaṃ trayam /
rūpīṇi jīvitaṃ duḥkhe sāsravāṇi dvidhā nava // VAkK_2.9 //
```

Source form:

```text
dṛgbhāvanāśaikṣapathe nava trīṇi amalaṃ trayam /
rūpīṇi jīvitaṃ duḥkhe sāsravāṇi dvidhā nava // VAkK_2.9 //
```

## 3. Padaccheda

| Text | Padaccheda | Basic Sense |
|---|---|---|
| dṛgbhāvanāśaikṣapathe | dṛg-bhāvanā-aśaikṣa-pathe | on the paths of seeing, cultivation, and no-more-training |
| nava | nava | nine |
| trīṇi | trīṇi | three |
| amalam | amalam | stainless / pure |
| trayam | trayam | triad / set of three |
| rūpīṇi | rūpīṇi | material / having form |
| jīvitam | jīvitam | life |
| duḥkhe | duḥkhe | in / regarding pain |
| sāsravāṇi | sa-āsravāṇi | with outflows / contaminated |
| dvidhā | dvidhā | twofold / in two ways |
| nava | nava | nine |

## 4. Grammar

```text
dṛg-bhāvanā-aśaikṣa-pathe
    locative singular compound
    “on the path of seeing, cultivation, and no-more-training”

nava trīṇi ... trayam
    numerals used in compressed classificatory syntax
    “nine, three, the triad”

amalam
    nominative / accusative singular neuter
    “stainless,” “pure”

rūpīṇi
    nominative / accusative plural neuter
    “material,” “possessing form”

sāsravāṇi
    nominative / accusative plural neuter
    “with outflows,” “contaminated”

dvidhā nava
    “nine are twofold”
```

## 5. Textual Caution

This verse begins a dense technical classification of the twenty-two faculties. The kārikā is compressed, and the final placement of each class should be checked against the Bhāṣya when that layer is integrated.

This file therefore treats the verse as a **kārikā-first classification draft**.

## 6. Literal Translation

```text
On the paths of seeing, cultivation, and no-more-training:
nine, three, and the triad are pure.
The material faculties, life, and pain are with outflows;
nine are twofold.
```

## 7. Philosophical Translation

```text
The faculties are now sorted by path-status and purity. Some faculties function as
pure on the paths of seeing, cultivation, and no-more-training. The material faculties,
the life faculty, and the pain faculty are classified as with outflows, while nine faculties
are twofold, capable of being classified according to both contaminated and uncontaminated modes.
```

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| dṛk-patha | path of seeing | The path where truth is directly seen |
| bhāvanā-patha | path of cultivation | The path of repeated development |
| aśaikṣa-patha | path of no-more-training | The completed path beyond training |
| amala | stainless / pure | Without stain; uncontaminated in path context |
| rūpin | material / having form | The form-based faculties |
| jīvita | life faculty | Here classified as sāsrava |
| duḥkha | pain faculty | Here classified as sāsrava |
| sāsrava | with outflows / contaminated | Still connected with outflow / taint |
| dvidhā | twofold | Capable of classification in two modes |

## 9. Classification Note

The verse appears to classify the faculties along at least three axes:

```text
path-status:
    path of seeing
    path of cultivation
    path of no-more-training

purity-status:
    amala
    stainless / pure

outflow-status:
    sāsrava
    with outflows / contaminated
    dvidhā
    twofold
```

The first hemistich concerns pure faculties in relation to the three path-levels:

```text
dṛg-patha
bhāvanā-patha
aśaikṣa-patha
```

The second hemistich begins the classification of faculties as:

```text
sāsrava
    with outflows

dvidhā
    twofold
```

## 10. Logical Determination

After VAK_2.01–2.08 define the faculties and the feeling distinctions, VAK_2.09 begins a new operation: classification by purity and path.

```text
indriya
    no longer only = governing efficacy
    now also = classifiable according to path-status and contamination-status
```

The doctrinal movement is:

```text
functional definition
    -> affective differentiation
    -> purity / impurity classification
```

This is important because a faculty is not merely present or absent. It can function at different levels of purification.

## 11. Transcendental Placement

The Logic of Experience now becomes a Logic of Path-Qualification.

```text
same faculty-structure
    can be read through path-status
    and through outflow-status
```

The category **amala** marks the faculty insofar as it belongs to the purified path. The category **sāsrava** marks the faculty insofar as it remains within contaminated experience.

The verse therefore introduces a higher classification of the same indriya-system:

```text
with outflows
pure
or twofold
```

## 12. Organon Interpretation

Organon reading:

```text
sāsrava-indriya
    =
faculty-driver operating under contaminated conditions

amala-indriya
    =
faculty-driver operating under purified path-conditions

dvidhā-indriya
    =
faculty-driver capable of both contaminated and purified modes
```

So the chapter now moves from **what the faculties do** to **under what path-condition they operate**.

## 13. Compact Formula

```text
VAK_2.09 begins the classification of faculties by path and purity:
some are pure in relation to the paths, some are with outflows,
and nine are twofold.
```

## 14. OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_09 a vak:Karika ;
    rdfs:label "VAK 2.09" ;
    vak:sourceVerse "VAkK_2.9" ;
    vak:chapter vak:Indriyanirdesa ;
    vak:hasTopic vak:PathStatusOfIndriyas, vak:OutflowStatusOfIndriyas ;
    vak:hasKeyTerm vak:DrgPatha, vak:BhavanaPatha, vak:AsaiksaPatha, vak:Amala, vak:Sasrava, vak:Dvidha ;
    vak:hasLiteralTranslation
        "On the paths of seeing, cultivation, and no-more-training: nine, three, and the triad are pure. The material faculties, life, and pain are with outflows; nine are twofold." ;
    vak:hasPhilosophicalTranslation
        "The faculties are now sorted by path-status and purity. Some faculties function as pure on the paths of seeing, cultivation, and no-more-training. The material faculties, the life faculty, and the pain faculty are classified as with outflows, while nine faculties are twofold, capable of being classified according to both contaminated and uncontaminated modes." .

vak:Amala a logic:Determination ;
    rdfs:label "amala" ;
    vak:canonicalTranslation "stainless / pure" .

vak:Sasrava a logic:Determination ;
    rdfs:label "sāsrava" ;
    vak:canonicalTranslation "with outflows / contaminated" .

vak:Dvidha a logic:Determination ;
    rdfs:label "dvidhā" ;
    vak:canonicalTranslation "twofold" .

vak:PathStatusOfIndriyas a logic:Determination ;
    rdfs:label "path-status of faculties" ;
    organon:logicalFunction "Classifies faculties according to seeing, cultivation, and no-more-training." .
```

## 15. Commit History

```text
VAK_2.09 opened.
Chapter: Indriyanirdeśa.
Method: kārikā-first.
Technical caution added: dense classification to be checked against Bhāṣya layer.
New axis introduced: path-status and purity-status.
Terms introduced: amala, sāsrava, dvidhā.
Organon note added: faculties classified by contaminated, purified, and twofold operating modes.
Zero-padded file naming maintained: VAK_2.09.
```
