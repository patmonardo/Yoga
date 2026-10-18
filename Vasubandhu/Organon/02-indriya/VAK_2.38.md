# VAK_2.38 — Status Does Not Inherit

## 1. Sanskrit (Devanāgarī)

```sanskrit
त्रिधा नशैक्षाशैक्षाणामहेयानां द्विधा मता ।
अव्याकृताप्तिः सहजाभिज्ञानैर्माणिकादृते ॥ २.३८ ॥
```

## 2. Sanskrit (IAST)

```text
tridhā naśaikṣāśaikṣāṇām aheyānāṃ dvidhā matā /
avyākṛtāptiḥ sahajābhijñānairmāṇikād ṛte // 2.38 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| na-śaikṣa-aśaikṣāṇām | gen. pl. m.; compound | of what is neither trainee nor beyond training |
| tridhā | adverb | threefold |
| aheyānām | gen. pl. m.; past passive participle | of what is not to be abandoned |
| dvidhā | adverb | twofold |
| avyākṛta-āptiḥ | nom. sg. f.; compound | acquisition of the indeterminate |
| sahajābhijñānairmāṇikād ṛte | nom. sg. f. + instr. pl. n. + abl. sg. n. + indeclinable (sandhied phrase) | co-arisen; except the superknowledges and magical-creation mind |

The Bhāṣya specifies two indeterminate superknowledges and the magical-creation mind as exceptions. The verse retains the sandhied form; sahajā is simultaneous, not innate.
## 4. Grammar

```text
% start S
S[PATH=neither] -> Acquisition[PATH=trainee|beyond|neither]
S[ABANDON=none] -> Acquisition[ABANDON=cultivation|none]
S[ETHICAL=indeterminate, COARISE=true] -> Acquisition[EXCEPT=superknowledge|magical]
```

Neither-trainee-nor-beyond allows three.  
Not-to-be-abandoned allows two.  
Indeterminate acquisition is co-arisen, with the stated exceptions.

## 5. Translation

### Literal Translation

> Acquisition of what is neither trainee nor beyond training is threefold.
> Acquisition of what is not to be abandoned is twofold. Acquisition of the
> indeterminate is co-arisen, except the superknowledges and the magical-
> creation mind.
### Bhāṣya-informed study translation

> Acquisition of what is neither in training nor beyond training is
> threefold. Of what is not to be abandoned, it is twofold. Indeterminate
> acquisition is co-arisen, except for the superknowledges and the magical-
> creation mind.
## 6. Philosophical Translation

> Status of the credit need not inherit the status of the dharma. Indeterminate acquisition is co-arisen, with exceptions. Co-arising is not innateness.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| naivaśaikṣanāśaikṣa | neither | the third path-class |
| aheya | not to be abandoned | the dharma; the credit may differ |
| sahajā | co-arisen | not innate |
| agrajā | prior | the exception |
| abhijñā | superknowledge | two indeterminate |
| nairmāṇika | magical-creation mind | the other exception |

Crafts are a further attributed extension. Not every skill is a superknowledge.

## 8. Logical Determination

```text
path-class of the dharma
    ≠ path-class of the acquisition
abandonment-class likewise
weak unobscured-indeterminate
    → co-arisen only
special cultivation
    → prior, co-arisen, subsequent
indeterminate
    ≠ weak
```

## 9. Interpretive Note

**Translation note.** The commentary specifies that the indeterminate superknowledges and magical-creation mind may have acquisition that precedes, accompanies, or follows them through special preparatory practice. It continues with obscured form and Desire Realm form in 2.39. The relation of acquisition to the path that obtained it is commentary, not part of the verse's threefold predicate.

An exception engine on the matrix of 2.37. Cessation through Discrimination is neither trainee nor beyond, in itself. Its credit follows the path that obtained it. The continuation into obscured form and Desire Realm form is 2.39.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_38 a vak:Karika ; vak:hasTopic vak:AcquisitionDoesNotInherit .
```
