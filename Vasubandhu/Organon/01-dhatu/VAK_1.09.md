# VAK_1.09

## 1. Sanskrit (Devanāgarī)

> रूपं पञ्चेन्द्रियाण्यर्थाः पञ्चाविज्ञप्तिरेव च ।
>
> तद्विज्ञानाश्रया रूपप्रसादाश्चक्षुरादयः ॥ १.०९ ॥॥

## 2. Sanskrit (IAST)

> rūpaṃ pañcendriyāṇy arthāḥ pañcāvijñaptir eva ca /
>
> tadvijñānāśrayā rūpaprasādāś cakṣurādayaḥ // 1.09 //

## 3. Padaccheda

rūpam | pañca | indriyāṇi | arthāḥ | pañca | avijñaptiḥ | eva | ca |
tad-vijñāna-āśrayāḥ | rūpa-prasādāḥ | cakṣus-ādayaḥ

`Pañca` counts the *arthas*. `Avijñapti` is singular. Eleven. *Vijñāna* is not a twelfth member of *rūpa*.

## 4. Grammar

```text
rūpa-skandha
    = five indriyas
    + five arthas
    + avijñapti
```

The second line: the eye and the rest are *rūpa-prasāda*, supports of the corresponding *vijñāna*.

## 5. Translation

### Literal

Form is the five faculties, the five Meanings, and *avijñapti* also. The eye and the others are clarities of form, supports of the corresponding Principles.

*Artha* is Meaning. The Bhāṣya glosses it as *viṣaya*. They are not two cells. Meaning is the wiggle of *viṣaya*.

### Bhāṣya-informed

The aggregate of form is the five faculties, the five respective *viṣayas* of those faculties, and *avijñapti*. That is the whole of the *rūpa-skandha*. The faculties beginning with the eye are clarities of form. They support the Principle correlated with each. *Avijñapti* is named, not defined. The five Meanings remain to be explained.

## 6. Philosophical Translation

Schema, as Ontology. The method of constructing it.

```text
skandha        Base
āyatana        Meaning
dhātu          Definition
```

This verse is the Base of form. Eleven members. Meaning is what the members combine into. Definition is *dhātu*. Not this verse.

```text
sound              the member, on the Base
what is heard      the combination
what it means      Meaning
```

Sāṃkhya discriminates *tanmātra* and the subtle Elements. Vedānta tosses that discrimination. Form Theory and Substance Theory do not.

```text
tanmātra           Form
                   the five Meanings
subtle Element     not the same cell
                   Substance Theory keeps the cut
```

The gloss *viṣaya* points at the wiggle. It does not hand over an Object. Object is another point in the pipeline.

## 7. Vocabulary

| Sanskrit | In this verse |
|---|---|
| rūpa-skandha | the Base of form. Eleven |
| indriya | faculty. A rule applied to nature |
| artha | Meaning. The wiggle of *viṣaya* |
| viṣaya | the Bhāṣya gloss. Condition |
| tanmātra | Form-side of the five Meanings. Not Vedānta-collapsed into the subtle Element |
| avijñapti | named. Not defined until 1.11 |
| vijñāna | Principle. Not a member of this Base |
| āyatana | Meaning. Not this verse’s count |
| dhātu | Definition. Not this verse |

## 8. Logical Determination

```text
RūpaSkandha = Indriya×5 + Meaning×5 + Avijñapti
Vijñāna ∉ RūpaSkandha
Meaning = wiggle(Viṣaya)
Tanmātra ≠ SubtleElement
Object ∉ this verse
```

## 9. Interpretive Note

Kośa voice. Meaning is the English of *artha* because that is how the Ontology is built. The Bhāṣya is not synced.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_09 a vak:Karika ;
    vak:hasTopic vak:RupaBase ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Artha vak:english "Meaning" .
vak:Tanmatra vak:distinctFrom vak:SubtleElement .
```
