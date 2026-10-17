# VAK_2.38 — Status Does Not Inherit

## 1. Sanskrit (Devanāgarī)

> त्रिधा नशैक्षाशैक्षाणामहेयानां द्विधा मता ।
>
> अव्याकृताप्तिः सहजाभिज्ञानैर्माणिकादृते ॥ २.३८ ॥

## 2. Sanskrit (IAST)

> tridhā naśaikṣāśaikṣāṇām aheyānāṃ dvidhā matā /
>
> avyākṛtāptiḥ sahajābhijñānairmāṇikād ṛte // 2.38 //

## 3. Lexical Analysis

| Pada | Force |
|---|---|
| na-śaikṣa-aśaikṣāṇām | of what is neither trainee nor beyond training |
| tridhā | threefold |
| aheyānām | of what is not to be abandoned |
| dvidhā | twofold |
| avyākṛta-āptiḥ | acquisition of the indeterminate |
| sahajā | co-arisen |
| ṛte | except |

Sahajā is simultaneous. Not innate.

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

Threefold, of what is neither trainee nor beyond training. Of what is not to be abandoned, held to be twofold. Acquisition of the indeterminate is co-arisen, except the superknowledges and the magical creation.

### Bhāṣya-informed study translation

> Acquisition of what is neither trainee nor beyond training may itself be any of the three. Of what is not to be abandoned, acquisition is abandoned by cultivation or itself not to be abandoned. Indeterminate acquisition is co-arisen, except the two indeterminate superknowledges and the magical-creation mind, whose acquisition may precede, accompany, and follow.

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

An exception engine on the matrix of 2.37. Cessation through Discrimination is neither trainee nor beyond, in itself. Its credit follows the path that obtained it. The continuation into obscured form and desire-realm form is 2.39.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_38 a vak:Karika ; vak:hasTopic vak:AcquisitionDoesNotInherit .
```
