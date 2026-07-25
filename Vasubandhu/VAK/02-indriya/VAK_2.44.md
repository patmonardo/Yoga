# VAK_2.44 — Nirodha Acquisition Constraints

## 1. Sanskrit — Devanāgarī

```text
बोधिलभ्या मुनेः न प्राक् चतुस्त्रिंशत्क्षणाप्तितः ।
कामरूपाश्रये भूते निरोधाख्यादितो नृषु ॥ VAkK_2.44 ॥
```

## 2. Sanskrit — IAST

```text
bodhilabhyā muneḥ na prāk catustriṃśatkṣaṇāptitaḥ /
kāmarūpāśraye bhūte nirodhākhyādito nṛṣu // VAkK_2.44 //
```

Source form:

```text
bodhilabhyā muneḥ na prāk catustriṃśatkṣaṇāptitaḥ /
kāmarūpāśraye bhūte nirodhākhyādito nṛṣu // VAkK_2.44 //
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| bodhi-labhyā | bodhilabhyā | feminine nominative singular | obtainable at awakening / through bodhi |
| muneḥ | muneḥ | genitive singular | of the sage / muni |
| na prāk | na prāk | phrase | not before |
| catuḥ-triṃśat-kṣaṇa-āptitaḥ | catustriṃśatkṣaṇāptitaḥ | ablative compound | from the acquisition of thirty-four moments; technical review needed |
| kāma-rūpa-āśraye | kāmarūpāśraye | locative singular compound | in a support of desire and form |
| bhūte | bhūte | locative singular | in a being / existent basis |
| nirodha-ākhyā | nirodhākhyā | feminine nominative singular | called nirodha |
| āditaḥ | āditaḥ | indeclinable | from the beginning / initially |
| nṛṣu | nṛṣu | locative plural | among humans |

## 4. Literal Translation

```text
For the sage it is obtainable at awakening, not before the acquisition of thirty-four moments.
The state called nirodha initially occurs among humans, in a support of desire and form.
```

## 5. Philosophical Translation

```text
Nirodha-samāpatti has strict acquisition constraints.
For the sage, it is connected with awakening and not obtained prior to a specific sequence of acquisitions.
Its initial occurrence is tied to human embodiment and to a support involving the desire and form realms.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| bodhi | awakening | Awakening-status |
| labhya | obtainable | Acquisition possibility |
| muni | sage | Specific path figure |
| catustriṃśat-kṣaṇa | thirty-four moments | Dense technical sequence; must be reviewed with Bhāṣya |
| āpti | acquisition | Prāpti relation |
| kāma-rūpa-āśraya | desire/form support | Embodied support-condition |
| bhūta | being / existent basis | Support-status; verify |
| nirodhākhyā | called nirodha | Cessation-attainment from VAK_2.43 |
| nṛ | human | Human locus |

## 7. Logical Determination

VAK_2.44 completes the nirodha-samāpatti profile with acquisition constraints.

```text
NirodhaAcquisitionRule:
    eligibility = muni / ārya-series
    condition = bodhi-related acquisition
    notBefore = specified moment-sequence
    initialLocus = human support
    support = kāma-rūpa basis
```

Logical protocol:

```text
an attainment is not merely possible in abstraction.
It has sequence, support, and eligibility conditions.
```

This is explicit structural state-transition logic.

## 8. Relation to Indriya and Citta-Caitta

Indriya and citta-caitta establish the event architecture.
Nirodha acquisition rules establish special path-state transitions.

```text
ordinary experience:
    faculty + field + feature

special attainment:
    support + eligibility + sequence + acquisition
```

So the chapter now contains both ordinary operation and exceptional path-state logic.

## 9. Organon Interpretation

Organon reading:

```text
NirodhaTransitionRule:
    requiresSupport = human / kāma-rūpa
    requiresSequence = thirty-four-moment acquisition
    requiresPathStatus = sage / awakening-context
```

Engineering implication:

```text
The Dataset requires guarded transitions.
Some states are only reachable when specified preconditions are met.
```

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .

vak:NirodhaTransitionRule a rdfs:Class ;
    vak:requiresSupport vak:KamaRupaSupport ;
    vak:requiresLocus vak:HumanLocus ;
    vak:requiresPathContext vak:BodhiContext ;
    vak:hasTargetState vak:NirodhaSamapattiProfile .
```

## 11. Commit History

```text
VAK_2.44 opened.
Method: kārikā-first speculative seed.
Theme: acquisition constraints for nirodha-samāpatti.
Technical sequence details marked for later Bhāṣya review.
Organon mapping: guarded state-transition rule in the Semantic Dataset.
Zero-padded file naming maintained: VAK_2.44.
```
