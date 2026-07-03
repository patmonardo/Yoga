# VAK_2.48 — Result-Status of Structural Operators

## 1. Sanskrit — Devanāgarī

```text
सभागता सा तु पुनर्विपाकोऽपि आप्तयो द्विधा ।
लक्षणानि च निःष्यन्दाः समापत्त्यः समन्वयाः ॥ VAkK_2.48 ॥
```

## 2. Sanskrit — IAST

```text
sabhāgatā sā tu punar vipāko 'pi āptayo dvidhā /
lakṣaṇāni ca niḥṣyandāḥ samāpattyaḥ samanvayāḥ // VAkK_2.48 //
```

Source form:

```text
sabhāgatā sā tu punarvipāko 'pi āptayo dvidhā /
lakṣaṇāni ca niḥṣyandāḥ samāpattya samanvayāḥ // VAkK_2.48 //
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| sabhāgatā | sabhāgatā | feminine nominative singular | class-commonality |
| sā | sā | pronoun | that |
| tu | tu | particle | but / however |
| punaḥ | punaḥ | indeclinable | again / furthermore |
| vipākaḥ api | vipāko 'pi | phrase | also maturation-result |
| āptayaḥ | āptayaḥ | feminine nominative plural | acquisitions / attainments |
| dvidhā | dvidhā | adverb | twofold |
| lakṣaṇāni | lakṣaṇāni | neuter nominative plural | marks |
| ca | ca | indeclinable | and |
| niḥṣyandāḥ | niḥṣyandāḥ | masculine nominative plural | outflows / homogeneous results |
| samāpattyaḥ | samāpattyaḥ | feminine nominative plural | attainments / absorptions |
| samanvayāḥ | samanvayāḥ | masculine nominative plural | connections / endowments |

## 4. Literal Translation

```text
That sabhāgatā, furthermore, is also vipāka.
The acquisitions are twofold. The marks are niḥṣyanda, and the samāpattis are endowments/connections.
```

## 5. Philosophical Translation

```text
The structural operators are now assigned result-status.
Class-commonality may function as maturation-result.
Acquisitions have a twofold profile.
The conditioned marks are treated as niḥṣyanda-results,
and samāpattis are interpreted through the logic of endowment or connection.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| sabhāgatā | class-commonality | From VAK_2.41 |
| vipāka | maturation-result | Result of prior conditioning |
| āpti | acquisition / attainment | Prāpti relation |
| dvidhā | twofold | Classification marker |
| lakṣaṇa | mark / determination | Conditioned marks from VAK_2.45 |
| niḥṣyanda | outflow / homogeneous result | Result-type; developed in phala block |
| samāpatti | attainment / absorption | Special structural state |
| samanvaya | endowment / connection | Relation of connected possession |

## 7. Logical Determination

VAK_2.48 closes the conditioned-mark/structural-operator block by assigning result-status.

```text
sabhāgatā
    = also vipāka

āpti
    = twofold

lakṣaṇa
    = niḥṣyanda

samāpatti
    = samanvaya / connected endowment
```

Logical protocol:

```text
structural operators are not merely listed;
they are classified by result-type and relation-type.
```

This anticipates the next major block: the cause-result system.

## 8. Relation to the Feature Logic

This verse acts as a bridge:

```text
ViprayuktaFeatureSet
    -> LakṣaṇaFeatureSet
    -> PhalaFeatureSet
```

So the chapter is now moving from structural and lifecycle features into result logic.

## 9. Organon Interpretation

Organon reading:

```text
StructuralOperatorResultProfile:
    operator
    resultStatus
    relationStatus
```

Engineering implication:

```text
Every structural operator requires metadata about what kind of result it is,
and how it is connected to a series.
```

This is the bridge into the Hetu-Phala engine.

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .

vak:Sabhagata vak:hasResultType vak:Vipaka .
vak:Laksana vak:hasResultType vak:Nisyanda .
vak:Samapatti vak:hasRelationType vak:Samanvaya .
vak:Apti vak:hasClassification vak:Twofold .
```

## 11. Commit History

```text
VAK_2.48 opened.
Method: kārikā-first speculative seed.
Theme: result-status and relation-status of structural operators.
Technical details marked for later Bhāṣya review.
Organon mapping: bridge from structural operators to the cause-result system.
Zero-padded file naming maintained: VAK_2.48.
```
