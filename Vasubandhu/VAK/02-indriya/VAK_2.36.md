# VAK_2.36 — Prāpti, Aprāpti, and Relation to the Own Series

## 1. Sanskrit — Devanāgarī

```text
नामकायादयश्चेति प्राप्तिर्लाभः समन्वयः ।
प्राप्त्यप्राप्ती स्वसंतान पतितानां निरोधयोः ॥ VAkK_2.36 ॥
```

## 2. Sanskrit — IAST

```text
nāmakāyādayaś ceti prāptir lābhaḥ samanvayaḥ /
prāptyaprāptī svasaṃtāna-patitānāṃ nirodhayoḥ // VAkK_2.36 //
```

Source form:

```text
nāmakāyādayaśceti prāptirlābhaḥ samanvayaḥ /
prāptyaprāptī svasaṃtāna patitānāṃ nirodhayoḥ // VAkK_2.36 //
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| nāma-kāya-ādayaḥ | nāmakāyādayaḥ | masculine nominative plural | name-bodies and so forth |
| ca | ca | indeclinable | and |
| iti | iti | particle | thus |
| prāptiḥ | prāptiḥ | feminine nominative singular | acquisition / attainment |
| lābhaḥ | lābhaḥ | masculine nominative singular | obtaining / gain |
| samanvayaḥ | samanvayaḥ | masculine nominative singular | connection / endowment / co-ordination |
| prāpti-aprāptī | prāptyaprāptī | feminine nominative dual | acquisition and non-acquisition |
| sva-saṃtāna-patitānām | svasaṃtāna-patitānām | genitive plural compound | of what has fallen into one's own series |
| nirodhayoḥ | nirodhayoḥ | locative/genitive dual | of the two cessations / in relation to cessations |

## 4. Literal Translation

```text
Name-bodies and so forth are also included.
Prāpti is obtaining, connection, or endowment.
Prāpti and aprāpti concern what has entered one's own series and the two cessations.
```

## 5. Philosophical Translation

```text
The structural-operator catalog also includes name-groups and related formations.
Prāpti is defined as a relation of acquisition, obtaining, or endowment.
Prāpti and aprāpti mark whether a determination is connected with one's own stream or with cessation-status.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| nāmakāya | name-body / name-group | Linguistic or naming aggregate; later review needed |
| prāpti | acquisition / attainment / endowment | Structural relation of having or being connected with a dharma |
| lābha | obtaining | Synonym or gloss of prāpti |
| samanvaya | connection / endowment | Being connected with, coordinated with, or endowed with |
| aprāpti | non-acquisition | Structural non-having or non-connection |
| svasaṃtāna | own series / own continuum | The conditioned stream to which a dharma belongs |
| patita | fallen into / entered | Belonging within a series |
| nirodha | cessation | Technical cessation-status; details to verify with Bhāṣya |

## 7. Logical Determination

VAK_2.36 defines prāpti as a structural relation.

```text
prāpti
    = lābha
    = samanvaya
    = acquisition / endowment / connection
```

The logical protocol is Relation-Status:

```text
a dharma may be related to a series by prāpti
or not related by aprāpti.
```

This is a structural operator, not an ordinary mental factor.

## 8. Relation to Indriya and Citta-Caitta

Indriyas and caittas tell us what operates or appears.
Prāpti tells us whether a dharma is connected to a given series.

```text
Indriya
    = faculty-operation

Caitta
    = feature-operation

Prāpti / Aprāpti
    = relation-status of belonging / not-belonging
```

This is crucial for the Dataset: features require ownership or attachment-to-series rules.

## 9. Organon Interpretation

Organon reading:

```text
PraptiRelation:
    subjectSeries
    dharma
    relationStatus = acquired | not-acquired
```

Engineering analogy:

```text
prāpti
    = feature attached to stream

aprāpti
    = feature not attached to stream
```

This supports state tracking across a continuum.

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:PraptiRelation a rdfs:Class ;
    rdfs:label "prāpti relation" ;
    rdfs:comment "A relation of acquisition, endowment, or connection between a dharma and a series." .

vak:ApraptiRelation a rdfs:Class ;
    rdfs:label "aprāpti relation" ;
    rdfs:comment "A relation of non-acquisition or non-connection." .

vak:hasSeries a rdf:Property .
vak:hasDharma a rdf:Property .
vak:hasRelationStatus a rdf:Property .
```

## 11. Commit History

```text
VAK_2.36 opened.
Method: kārikā-first speculative seed.
Theme: prāpti and aprāpti as structural relation-status operators.
Technical vocabulary marked for later Bhāṣya review.
Organon mapping: feature attachment / non-attachment to a conditioned series.
Zero-padded file naming maintained: VAK_2.36.
```
