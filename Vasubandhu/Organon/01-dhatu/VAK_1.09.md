# VAK_1.09 — The Form-Base

## 1. Sanskrit (Devanāgarī)

> रूपं पञ्चेन्द्रियाण्यर्थाः पञ्चाविज्ञप्तिरेव च ।
>
> तद्विज्ञानाश्रया रूपप्रसादाश्चक्षुरादयः ॥ १.०९ ॥॥

## 2. Sanskrit (IAST)

> rūpaṃ pañcendriyāṇy arthāḥ pañcāvijñaptir eva ca /
>
> tadvijñānāśrayā rūpaprasādāś cakṣurādayaḥ // 1.09 //

## 3. Lexical Analysis

```text
rūpam                  → the form-base
pañcendriyāṇi          → pañca + indriyāṇi
pañcāvijñaptiḥ          → pañca + avijñaptiḥ
tadvijñānāśrayāḥ       → tad-vijñāna-āśrayāḥ
rūpaprasādāḥ           → rūpa-prasādāḥ
cakṣurādayaḥ           → cakṣus-ādayaḥ
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| rūpam | nominative neuter | form; the form-base |
| pañca indriyāṇi | nominative neuter plural | five organs |
| arthāḥ | nominative masculine plural | meanings |
| pañca | numeral | counts the meanings |
| avijñaptiḥ | nominative feminine singular | and *avijñapti* |
| eva ca | particles | and just that |
| tad-vijñāna-āśrayāḥ | nominative plural | supports of the corresponding principle |
| rūpa-prasādāḥ | nominative plural | clarities of form |
| cakṣus-ādayaḥ | nominative plural | beginning with the eye |

*Pañca* counts the meanings. *Avijñapti* is singular. Eleven. The principle
is not a twelfth member of form. The organs support it.

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

The first line enumerates the form-base. The second defines the five organs.
They are clarities of form, and supports of the principle that corresponds.

## 5. Translation

### Literal Translation

Form is the five organs, the five meanings, and *avijñapti*. The clarities
of form, beginning with the eye, are supports of the corresponding
principle.

### Bhāṣya-informed study translation

The form-base is the five organs — eye, ear, nose, tongue, body — the five
meanings of those organs, each its own, and *avijñapti*. The meanings are
visible form, sound, odor, taste, and the tangible. The five are clarities
of form. In order they support the principle of visible form, of sound, of
odor, of taste, and of the tangible. *Avijñapti* is named, not defined.
The five meanings remain to be indicated.

## 6. Philosophical Translation

Again, two lines. The first is the collection. The second is the support.

This is where the base starts, and it is not the system. The opening
division already set Pure and Impure, Conditioned and Unconditioned. The
base is the first subsystem caught in that division. Form collects eleven:
five organs, five meanings, *avijñapti*. Essences and principles are not
enumerated here. Without them the collection is not the whole.

Meaning stays lowercase. The commentary glosses it as condition. Organ and
meaning are the two sides, not two inventories. The organ does not see a
finished object. It is a clarity of form, and a support of the principle
that corresponds. The eye supports the eye-principle. So the Prakaraṇa.

*Avijñapti* is the eleventh, singular, and not yet defined. Dependence on
the four great elements, in the scripture cited, is not the appropriation
of 1.08.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| rūpa | form | the form-base; eleven |
| skandha | base | the first subsystem; not the whole |
| indriya | organ | here, once an organized being is in view |
| artha | meaning | lowercase; the other side |
| viṣaya | condition | the commentary's gloss of meaning; not a second list |
| avijñapti | *avijñapti* | named, not defined |
| rūpa-prasāda | clarity of form | what the five organs are |
| vijñāna | principle | the supported; not a twelfth member of form |
| āśraya | support | the organ, of the corresponding principle |
| āyatana | essence | cited for the eye; not enumerated |
| upādāya | depending on | the four great elements; not 1.08 |

## 8. Logical Determination

```text
form-base
    = five organs
    + five meanings
    + avijñapti
    = eleven
    principle not a member

organ
    = clarity of form
    = support of the corresponding principle
    eye → eye-principle
    and so on

meaning
    glossed as condition
    not a second inventory

base starts here
essence and principle not enumerated
1.10 not opened
```

## 9. Interpretive Note

The hinge is the count, then *āśraya*. Interpretation of the base as first
subsystem is in the Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_09 a vak:Karika ;
    vak:hasTopic vak:FormBase ;
    vak:belongsTo vak:Dhatunirdesa .

vak:FormBase vak:hasMember vak:FiveOrgans, vak:FiveMeanings, vak:Avijnapti ;
    vak:count 11 ;
    vak:includesPrinciple false ;
    vak:isWholeSystem false .

vak:Eye vak:is vak:ClarityOfForm ;
    vak:supports vak:EyePrinciple .

vak:Meaning vak:glossedAs vak:Condition .
vak:Avijnapti vak:defined false .
```
