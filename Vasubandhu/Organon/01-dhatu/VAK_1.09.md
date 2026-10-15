# VAK_1.09 — The Form-Base

## 1. Sanskrit (Devanāgarī)

> रूपं पञ्चेन्द्रियाण्यर्थाः पञ्चाविज्ञप्तिरेव च ।
>
> तद्विज्ञानाश्रया रूपप्रसादाश्चक्षुरादयः ॥ १.०९ ॥

## 2. Sanskrit (IAST)

> rūpaṃ pañcendriyāṇy arthāḥ pañcāvijñaptir eva ca /
>
> tadvijñānāśrayā rūpaprasādāś cakṣurādayaḥ // 1.09 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| rūpam | nominative neuter singular | form; the form-base |
| pañcendriyāṇi | pañca + indriyāṇi; nominative neuter plural | five faculties |
| arthāḥ | nominative masculine plural | meanings |
| pañca | numeral | counts the meanings, not the faculties again |
| avijñaptiḥ | nominative feminine singular | one member; named, not defined |
| eva ca | particles | and just that |
| tadvijñānāśrayāḥ | tad-vijñāna-āśrayāḥ; nominative plural | supports of the corresponding cognition |
| rūpaprasādāḥ | rūpa-prasādāḥ; nominative plural | clarities of form |
| cakṣurādayaḥ | cakṣus-ādayaḥ; nominative plural | beginning with the eye |

## 4. Grammar

```text
rūpam
    = pañca indriyāṇi
    + arthāḥ pañca
    + avijñaptiḥ eva ca

cakṣur-ādayaḥ
    = rūpa-prasādāḥ
    = tad-vijñāna-āśrayāḥ
```

The first line enumerates. The second defines the five faculties. They are clarities of form, and supports of the cognition that corresponds. The cognition is not a member of the count.

## 5. Translation

### Literal

Form is the five faculties, the five meanings, and *avijñapti*. The clarities of form, beginning with the eye, are supports of the corresponding cognition.

### Bhāṣya-informed

The form-base is the five faculties — eye, ear, nose, tongue, body — the five meanings of those faculties, each its own, and *avijñapti*. The meanings are visible form, sound, odor, taste, and the tangible. The five are clarities of form. In order they support the cognition of visible form, of sound, of odor, of taste, and of the tangible. *Avijñapti* is named, not defined. The five meanings remain to be indicated.

## 6. Philosophical Translation

Eleven, and no twelfth. Form collects five faculties, five meanings, and *avijñapti*.

The faculty is a clarity of form. It is the support of the cognition that corresponds. The eye supports the cognition of the eye. The cognition is supported. It is not counted.

Meaning stays lowercase. The commentary glosses it as condition. Faculty and meaning are the two sides, not two inventories. *Avijñapti* is the eleventh, singular, and not yet defined.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| rūpa | form | the form-base; eleven |
| skandha | base | the first collection; not the whole |
| indriya | faculty | the Dhātu-verse word; organ is not this page |
| artha | meaning | lowercase |
| viṣaya | condition | the commentary’s gloss of meaning; not a second list |
| avijñapti | *avijñapti* | named, not defined |
| rūpa-prasāda | clarity of form | what the five faculties are |
| vijñāna | cognition | not principle |
| āśraya | support | of the corresponding cognition; not a twelfth member |
| āyatana | essence | cited for the eye; not enumerated |
| upādāya | depending on | the four great elements; not the appropriation of 1.08 |
| dhātu | principle | not a member of this count |

## 8. Logical Determination

```text
form-base
    = five faculties
    + five meanings
    + avijñapti
    = eleven

faculty
    = clarity of form
    = support of the corresponding cognition
    eye → cognition of the eye
    and so on

cognition
    supported
    not counted

meaning
    glossed as condition
    not a second inventory
```

## 9. Interpretive Note

The hinge is the count, then the support. The five faculties are indicated. The five meanings are named and left for the next verse. The scripture calls the eye an internal essence, a clarity of form depending on the four great elements. That citation is not this enumeration. The Prakaraṇa agrees: the eye is a clarity of form that supports the cognition of the eye.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_09 a vak:Karika ;
    vak:hasTopic vak:FormBase ;
    vak:belongsTo vak:Dhatunirdesa .

vak:FormBase vak:hasMember vak:FiveFaculties, vak:FiveMeanings, vak:Avijnapti ;
    vak:count 11 ;
    vak:includesCognition false .

vak:Eye vak:is vak:ClarityOfForm ;
    vak:supports vak:EyeCognition .

vak:Avijnapti vak:defined false .
vak:Meaning vak:glossedAs vak:Condition .
```
