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

Form is the five faculties, the five *arthas*, and *avijñapti* also. The eye and the others are clarities of form, supports of the corresponding Principles.

*Artha* stands. The Bhāṣya glosses it as *viṣaya*. They are not two cells. *Artha* is the wiggle of *viṣaya*.

### Bhāṣya-informed

The aggregate of form is the five faculties, the five respective *viṣayas* of those faculties, and *avijñapti*. That is the whole of the *rūpa-skandha*. The faculties beginning with the eye are clarities of form. They support the Principle correlated with each. *Avijñapti* is named, not defined. The five *arthas* remain to be explained.

## 6. Philosophical Translation

Schema, as Ontology. Not a second vocabulary pasted on the verse.

```text
skandha        Base
āyatana        Meaning
dhātu          Definition
```

This verse is the Base of form. Eleven members. Meaning is what happens when members combine. Definition is not this verse. Definition is *dhātu*.

```text
sound              the member, on the Base
what is heard      the combination
what it means      Meaning
                   āyatana
                   not yet Definition
```

*Artha* is that wiggle: damn hot, very hot, hot, room temp. One Condition. Degrees. The gloss *viṣaya* points at the wiggle. It does not hand over an Object. Object is another point in the pipeline, Hegel’s Object, reached by the chakras. Not spent here.

## 7. Vocabulary

| Sanskrit | In this verse |
|---|---|
| rūpa-skandha | the Base of form. Eleven |
| indriya | faculty. A rule applied to nature |
| artha | the wiggle of *viṣaya*. Left untranslated in the literal |
| viṣaya | the Bhāṣya gloss. Condition |
| avijñapti | named. Not defined until 1.11 |
| vijñāna | Principle. Not a member of this Base |
| āyatana | Meaning. Not this verse’s count |
| dhātu | Definition. Not this verse |

## 8. Logical Determination

```text
RūpaSkandha = Indriya×5 + Artha×5 + Avijñapti
Vijñāna ∉ RūpaSkandha
Artha = wiggle(Viṣaya)
Object ∉ this verse
```

## 9. Interpretive Note

Kośa voice. The schema is how the received count is read: a Base, whose members combine into Meaning. Definition waits. The Bhāṣya is not synced.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_09 a vak:Karika ;
    vak:hasTopic vak:RupaBase ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Skandha vak:schemaRole "Base" .
vak:Ayatana vak:schemaRole "Meaning" .
vak:Dhatu vak:schemaRole "Definition" .
```
