# VAK_2.37 — Temporal, Ethical, and Domain Classifications of Prāpti

## 1. Sanskrit — Devanāgarī

```text
त्रैयध्विकानां त्रिविधा शुभादीनां शुभादिका ।
स्वधातुका तदाप्तानां अनाप्तानां चतुर्विधा ॥ VAkK_2.37 ॥
```

## 2. Sanskrit — IAST

```text
traiyadhvikānāṃ trividhā śubhādīnāṃ śubhādikā /
svadhātukā tadāptānām anāptānāṃ caturvidhā // VAkK_2.37 //
```

Source form:

```text
traiyadhvikānāṃ trividhā śubhādīnāṃ śubhādikā /
svadhātukā tadāptānāṃ anāptānāṃ caturvidhā // VAkK_2.37 //
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| traiyadhvikānām | tri-adhvika-ānām | genitive plural | of the three-time items |
| trividhā | tri-vidhā | feminine nominative singular | threefold |
| śubha-ādīnām | śubhādīnām | genitive plural | of wholesome and so forth |
| śubha-ādikā | śubhādikā | feminine nominative singular | beginning with wholesome / of wholesome-type etc. |
| sva-dhātukā | svadhātukā | feminine nominative singular | belonging to its own domain |
| tad-āptānām | tadāptānām | genitive plural | of those acquired / attained there |
| anāptānām | anāptānām | genitive plural | of those not acquired |
| caturvidhā | catur-vidhā | feminine nominative singular | fourfold |

## 4. Literal Translation

```text
For the three-time items, prāpti is threefold.
For wholesome and the others, it is of wholesome-type and so forth.
For those acquired in their own domain, it belongs to that domain;
for the unacquired, it is fourfold.
```

## 5. Philosophical Translation

```text
Prāpti is not a single undifferentiated relation.
It is classified by time, ethical status, and domain.
A dharma's relation to a series must be tracked according to temporal position,
wholesome or other status, domain-belonging, and non-acquisition profile.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| traiyadhvika | three-time | Past, present, future; exact scope later to verify |
| trividhā | threefold | Temporal classification |
| śubha | wholesome | Ethical class; may overlap with kuśala vocabulary |
| śubhādika | wholesome and so forth | Ethical/status classification series |
| svadhātuka | belonging to its own domain | Domain-specific relation |
| āpta | acquired / attained | Connected by prāpti |
| anāpta | not acquired / not attained | Not connected by prāpti |
| caturvidhā | fourfold | Fourfold classification of non-acquired relation |

## 7. Logical Determination

VAK_2.37 classifies prāpti as a multi-axis feature relation.

```text
PrāptiClassification:
    timeStatus
    ethicalStatus
    domainStatus
    acquisitionStatus
```

Logical protocols:

```text
Disjunction:
    threefold by time
    ethical/status divisions
    own-domain vs non-acquired divisions

Hypothetical:
    if dharma has temporal class X,
    then prāpti has corresponding time-profile.
```

This is the beginning of a relation-matrix for structural operators.

## 8. Relation to Indriya and Citta-Caitta

Earlier indriya and caitta profiles were classified by status and count.
Here prāpti is classified by the same style of feature logic.

```text
IndriyaFeatureSet
    = faculty-status classifications

CaittaFeatureSet
    = appearance-status classifications

PraptiFeatureSet
    = relation-status classifications
```

## 9. Organon Interpretation

Organon reading:

```text
FeatureAttachment:
    feature
    series
    timeStatus
    ethicalStatus
    domainStatus
    acquiredStatus
```

This is Dataset state tracking:

```text
A feature is not merely present.
It is present in time,
within a domain,
with a status,
and relative to a series.
```

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .

vak:PraptiFeatureSet a rdfs:Class .
vak:hasTimeStatus a rdf:Property .
vak:hasEthicalStatus a rdf:Property .
vak:hasDomainStatus a rdf:Property .
vak:hasAcquisitionStatus a rdf:Property .
```

## 11. Commit History

```text
VAK_2.37 opened.
Method: kārikā-first speculative seed.
Theme: classifications of prāpti by time, ethical status, and domain.
Organon mapping: feature attachment matrix for the Semantic Dataset.
Zero-padded file naming maintained: VAK_2.37.
```
