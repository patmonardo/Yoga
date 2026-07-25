# VAK_2.38 — Path-Status and Neutral Prāpti Classifications

## 1. Sanskrit — Devanāgarī

```text
त्रिधा न शैक्षाशैक्षाणां अहेयानां द्विधा मता ।
अव्याकृताप्तिः सहजा अभिज्ञानैर्माणिकादृते ॥ VAkK_2.38 ॥
```

## 2. Sanskrit — IAST

```text
tridhā na śaikṣāśaikṣāṇām aheyānāṃ dvidhā matā /
avyākṛtāptiḥ sahajā abhijñānairmāṇikād ṛte // VAkK_2.38 //
```

Source form:

```text
tridhā naśaikṣāśaikṣāṇāṃ aheyānāṃ dvidhā matā /
avyākṛtāptiḥ sahajā abhijñānairmāṇikādṛte // VAkK_2.38 //
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| tridhā | tridhā | adverb | threefold |
| na | na | particle | not |
| śaikṣa-aśaikṣāṇām | śaikṣāśaikṣāṇām | genitive plural | of trainees and non-trainees |
| aheyānām | aheyānām | genitive plural | of what is not to be abandoned |
| dvidhā | dvidhā | adverb | twofold |
| matā | matā | feminine nominative singular | held / considered |
| avyākṛta-āptiḥ | avyākṛtāptiḥ | feminine nominative singular | acquisition of indeterminate status |
| sahajā | sahajā | feminine nominative singular | co-arisen / innate |
| abhijñā-nirmāṇika-ād ṛte | abhijñānairmāṇikād ṛte | ablative phrase | except for what is produced by supernormal knowledge; segmentation to verify |

## 4. Literal Translation

```text
For the śaikṣa and aśaikṣa, and for the aheya, it is not threefold; it is held to be twofold.
The acquisition of the indeterminate is co-arisen, except for what is produced through abhijñā.
```

## 5. Philosophical Translation

```text
Prāpti is further classified by path-status and abandonability.
For trainee, non-trainee, and non-abandonable states, the relevant profile is twofold rather than threefold.
Indeterminate acquisition is generally co-arisen, with an exception for special knowledge-produced cases.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| śaikṣa | trainee / learner | Path-status |
| aśaikṣa | non-trainee / adept | Completion-status |
| aheya | not to be abandoned | Abandonment-status |
| dvidhā | twofold | Count-classification |
| avyākṛta | indeterminate / neutral | Neither wholesome nor unwholesome |
| āpti | acquisition | Same field as prāpti |
| sahajā | co-arisen / innate | Arising together with the relevant state |
| abhijñā | supernormal knowledge | Special knowledge-power; exact technical scope later |
| nirmāṇika | produced / constructed | Possibly knowledge-produced manifestation; verify later |

## 7. Logical Determination

VAK_2.38 continues the prāpti relation-matrix.

```text
pathStatus:
    śaikṣa
    aśaikṣa

aheyaStatus:
    not to be abandoned

neutralStatus:
    avyākṛta
```

Logical protocols:

```text
Disjunction:
    śaikṣa / aśaikṣa / aheya / avyākṛta

Hypothetical:
    if status = śaikṣa or aśaikṣa or aheya,
    then the prāpti-profile is twofold.

    if acquisition = avyākṛta,
    then it is co-arisen, except for the special knowledge-produced case.
```

## 8. Relation to Indriya and Citta-Caitta

The same feature logic now operates on structural relations.

```text
Indriya
    classified by realm, purity, and configuration

Caitta
    classified by mental and ethical profile

Prāpti
    classified by path-status, abandonability, and neutrality
```

This confirms that the chapter is building a general Feature Logic of conditioned experience.

## 9. Organon Interpretation

Organon reading:

```text
PraptiProfile:
    pathStatus = śaikṣa | aśaikṣa
    abandonmentStatus = aheya
    ethicalStatus = avyākṛta
    arisingMode = sahajā | specialKnowledgeProduced
```

This is relation metadata for the Semantic Dataset.

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .

vak:ShaiksaPraptiProfile a vak:PraptiFeatureSet .
vak:AshaiksaPraptiProfile a vak:PraptiFeatureSet .
vak:AheyaPraptiProfile a vak:PraptiFeatureSet .
vak:AvyakrtaPraptiProfile a vak:PraptiFeatureSet ;
    vak:hasArisingMode vak:Sahaja .
```

## 11. Commit History

```text
VAK_2.38 opened.
Method: kārikā-first speculative seed.
Theme: prāpti classifications by path-status, abandonability, and neutral acquisition.
Technical details marked for later Bhāṣya review.
Organon mapping: relation metadata for the Semantic Dataset.
Zero-padded file naming maintained: VAK_2.38.
```
