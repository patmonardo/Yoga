# VAK_1.09 — The Form Base

## 1. Sanskrit (Devanāgarī)

```sanskrit
रूपं पञ्चेन्द्रियाण्यर्थाः पञ्चाविज्ञप्तिरेव च ।
तद्विज्ञानाश्रया रूपप्रसादाश्चक्षुरादयः ॥ १.०९ ॥
```

## 2. Sanskrit (IAST)

```text
rūpaṃ pañcendriyāṇy arthāḥ pañcāvijñaptir eva ca /
tadvijñānāśrayā rūpaprasādāś cakṣurādayaḥ // 1.09 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| rūpam | nominative neuter singular | Form; the Form Base |
| pañcendriyāṇi | pañca + indriyāṇi; nominative neuter plural | five Faculties |
| arthāḥ | nominative masculine plural | meanings |
| pañca | numeral | counts the meanings, not the faculties again |
| avijñaptiḥ | nominative feminine singular | one member; named, not defined |
| eva ca | particles | and just that |
| tadvijñānāśrayāḥ | tad-vijñāna-āśrayāḥ; nominative plural | supports of the corresponding Cognition |
| rūpaprasādāḥ | rūpa-prasādāḥ; nominative plural | clarities of Form |
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

The first line enumerates. The second defines the five Faculties. They are clarities of Form, and supports of the Cognition that corresponds. Cognition is not a member of the count.

## 5. Translation

### Literal Translation

> Form is the five Faculties, the five meanings, and *avijñapti*. The
> clarities of Form, beginning with the eye, are supports of the
> corresponding Cognition.

### Bhāṣya-informed study translation

> The Form Base comprises five Faculties—eye, ear, nose, tongue, and
> body—their five corresponding meanings—visible Form, sound, odor, taste,
> and the tangible—and *avijñapti*. The five Faculties are clarities of
> Form, each serving as the support of the Cognition corresponding to its
> meaning.

## 6. Philosophical Translation

Eleven, and no twelfth. Form collects five Faculties, five meanings, and *avijñapti*.

The Faculty is a clarity of Form. It supports the corresponding Cognition; the eye supports Eye-Cognition. Cognition is supported, not counted.

Meaning stays lowercase. The commentary glosses it as condition. Faculty and meaning are the two sides, not two inventories. *Avijñapti* is the eleventh, singular, and not yet defined.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| rūpa | Form | the Form Base; eleven |
| skandha | Base | the first collection; not the whole |
| indriya | Faculty | one of the five; not a synonym for an anatomical organ |
| artha | meaning | the five |
| viṣaya | condition | the commentary’s gloss of meaning; not a second list |
| avijñapti | *avijñapti* | named, not defined |
| rūpa-prasāda | clarity of Form | what the five Faculties are |
| vijñāna | Cognition | not Principle |
| āśraya | support | of the corresponding Cognition; not a twelfth member |
| āyatana | Essence | cited for the eye; not enumerated |
| upādāya | depending on | the four Great Elements; not the appropriation of 1.08 |
| dhātu | Principle | not a member of this count |

## 8. Logical Determination

```text
Form Base
    = five Faculties
    + five meanings
    + avijñapti
    = eleven

Faculty
    = clarity of Form
    = support of the corresponding Cognition
    Eye → Eye-Cognition
    and so on

Cognition
    supported
    not counted

Meaning
    glossed as condition
    not a second inventory
```

## 9. Interpretive Note

The hinge is the count, then the support. The five Faculties are indicated. The five meanings are named and left for the next verse. The scripture calls the eye an internal Essence, a clarity of Form depending on the four Great Elements. That citation is not this enumeration. The Prakaraṇa agrees: the eye is a clarity of Form that supports Eye-Cognition.

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
