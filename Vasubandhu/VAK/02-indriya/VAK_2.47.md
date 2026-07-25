# VAK_2.47 — Nāmakāya and Linguistic Structural Formations

## 1. Sanskrit — Devanāgarī

```text
नामकायादयः संज्ञावाक्याक्षरसमुक्तयः ।
कामरूपाप्तसत्त्वाख्या निःष्यन्दाव्याकृतास्तथा ॥ VAkK_2.47 ॥
```

## 2. Sanskrit — IAST

```text
nāmakāyādayaḥ saṃjñāvākyākṣarasamuktayaḥ /
kāmarūpāptasattvākhyā niḥṣyandāvyākṛtās tathā // VAkK_2.47 //
```

Source form:

```text
nāmakāyādayaḥ saṃjñāvākyākṣarasamuktayaḥ /
kāmarūpāptasattvākhyā niḥṣyandāvyākṛtāḥ tathā // VAkK_2.47 //
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| nāma-kāya-ādayaḥ | nāmakāyādayaḥ | masculine nominative plural | name-groups and so forth |
| saṃjñā-vākya-akṣara-samuktayaḥ | saṃjñāvākyākṣarasamuktayaḥ | masculine nominative plural compound | collections/utterances of designation, sentence, and syllable/letter |
| kāma-rūpa-āpta | kāmarūpāpta | compound | acquired in desire and form realms |
| sattva-ākhyāḥ | sattvākhyāḥ | masculine nominative plural | called/associated with beings |
| niḥṣyanda | niḥṣyanda | masculine nominative plural | outflow / homogeneous result |
| avyākṛtāḥ | avyākṛtāḥ | masculine nominative plural | indeterminate / neutral |
| tathā | tathā | indeclinable | likewise |

## 4. Literal Translation

```text
Name-groups and the rest are collections of designation, sentence, and syllable/letter.
They are acquired in the desire and form realms, called connected with beings,
and likewise are niḥṣyanda and indeterminate.
```

## 5. Philosophical Translation

```text
The dissociated formation catalog includes linguistic structural formations:
name-groups, sentence-groups, and syllable or letter-groups.
These are treated as conditioned structural formations with realm-status,
being-related status, result-status, and indeterminate ethical status.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| nāmakāya | name-group / name-body | Linguistic structural formation |
| saṃjñā | designation | Naming or recognizing marker |
| vākya | sentence / statement | Linguistic unit |
| akṣara | syllable / letter | Minimal linguistic unit; review context |
| samukti | collection / utterance | Grouping or expression; technical review needed |
| kāma-rūpa-āpta | acquired in desire and form realms | Realm-status |
| sattvākhyā | called connected with beings | Being-related classification |
| niḥṣyanda | outflow / homogeneous result | Result-type; developed soon |
| avyākṛta | indeterminate / neutral | Ethical/status class |

## 7. Logical Determination

VAK_2.47 extends the structural-operator layer to linguistic formations.

```text
NāmakāyaFeatureSet:
    designation
    sentence
    syllable / letter
    realm-status
    being-status
    result-status
    ethical-status
```

Logical protocol:

```text
language-units are treated as conditioned structural formations,
not merely external sounds.
```

This is important for the feature-logic of experience: naming and articulation are themselves classified features.

## 8. Relation to the Feature Logic

The chapter now includes:

```text
Indriya
    faculty-givenness

Citta-Caitta
    appearance configuration

Viprayukta-saṃskāra
    structural operators

Nāmakāya
    linguistic structural operators
```

Thus the Dataset must include naming and expression structures as conditioned operators.

## 9. Organon Interpretation

Organon reading:

```text
LinguisticStructuralFormation:
    nameGroup
    sentenceGroup
    syllableGroup
    realmStatus
    resultStatus
    ethicalStatus
```

Engineering implication:

```text
Corpus structure is not accidental.
Names, sentences, and tokens are themselves conditioned formations.
```

This directly touches the Corpus side of the Organon.

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .

vak:Namakaya a vak:ViprayuktaSamskara .
vak:Vakyakaya a vak:ViprayuktaSamskara .
vak:Aksarakaya a vak:ViprayuktaSamskara .

vak:LinguisticStructuralFormation a rdfs:Class ;
    rdfs:subClassOf vak:ViprayuktaSamskara .
```

## 11. Commit History

```text
VAK_2.47 opened.
Method: kārikā-first speculative seed.
Theme: nāmakāya and linguistic structural formations.
Technical terms marked for later Bhāṣya review.
Organon mapping: names, sentences, and syllables as corpus-level conditioned structures.
Zero-padded file naming maintained: VAK_2.47.
```
