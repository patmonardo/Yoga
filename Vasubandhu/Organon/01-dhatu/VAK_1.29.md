# VAK_1.29 — Visible, Resistant, Indeterminate

## 1. Sanskrit (Devanāgarī)

> सनिदर्शन एकोऽत्र रूपं सप्रतिघा दश ।
>
> रूपिणोऽव्याकृता अष्टौ त एवारूपशब्दकाः ॥ १.२९ ॥

## 2. Sanskrit (IAST)

> sanidarśana eko 'tra rūpaṃ sapratighā daśa /
>
> rūpiṇo 'vyākṛtā aṣṭau ta evārūpaśabdakāḥ // 1.29 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sanidarśanaḥ | sa-nidarśanaḥ; nominative masculine singular | visible; can be pointed out |
| ekaḥ | nominative masculine singular | one |
| atra | indeclinable | here, among the eighteen |
| rūpam | nominative neuter singular | the visible-form principle |
| sapratighāḥ | sa-pratighāḥ; nominative masculine plural | resistant |
| daśa | numeral | ten |
| rūpiṇaḥ | nominative masculine plural | form-bearing; the ten in the form-base |
| avyākṛtāḥ | nominative masculine plural | indeterminate |
| aṣṭau | numeral | eight |
| te eva | nominative plural, with emphasis | those same ten |
| arūpaśabdakāḥ | a-rūpa-śabdakāḥ | excluding visible form and sound |

The final compound does not say the eight are without form. It excludes two of the ten: the visible-form principle and the sound-principle.

## 4. Grammar

```text
sanidarśanaḥ ekaḥ atra
    rūpam
        the one visible

sapratighāḥ daśa
    rūpiṇaḥ
        the ten in the form-base

avyākṛtāḥ aṣṭau
    te eva a-rūpa-śabdakāḥ
        those ten, excluding form and sound
```

Three questions, three counts. The masculine adjective agrees with the understood principle. Neuter *rūpam* names the one.

## 5. Translation

### Literal Translation

One here is visible: form. Ten are resistant. Eight form-bearing ones are indeterminate: those same, excluding form and sound.

### Bhāṣya-informed study translation

Among the eighteen Principles, one is visible: the Visible Form Principle.
The ten Principles included in the Form Base are resistant by obstruction.
Eight of those ten are indeterminate, neither wholesome nor unwholesome:
those same ten excluding Visible Form and Sound.

## 6. Philosophical Translation

Visibility, resistance, and ethical status are three determinations. They do not collapse.

The one visible is the visible-form principle, not the form-base. The ten resistant are the form-base as principles: five organs and five meanings. The eight indeterminate are those ten minus visible form and sound.

The cognition-principles are not in this count. The mind-principle is not in this count.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| dhātu | principle | the eighteen |
| sanidarśana | visible | can be pointed out |
| anidarśana | not visible | the other seventeen |
| rūpa-dhātu | visible-form principle | the one visible |
| sapratigha | resistant | the ten, by obstruction |
| pratigha | resistance | three kinds; the count uses one |
| āvaraṇa-pratighāta | obstruction | blocking a place |
| viṣaya-pratighāta | condition-resistance | the organ in its condition |
| ālambana-pratighāta | support-resistance | consciousness and the concomitants |
| rūpin | form-bearing | the ten in the form-base |
| avyākṛta | indeterminate | neither wholesome nor unwholesome |
| śabda-dhātu | sound-principle | excluded from the eight |
| vijñāna | cognition | not this count |
| citta | consciousness | the seven, in the comparison only |

## 8. Logical Determination

```text
eighteen principles

visible
    one
    visible-form principle
    the rest not visible

resistant
    ten
    the form-base as principles
    obstruction, not the other two

indeterminate
    eight
    those ten
    excluding visible form and sound
    five organs, smell, taste, tangible

not this verse
    the Cognition Principle, the seven
    the dharma-principle
    1.30 not opened
```

## 9. Interpretive Note

The hinge is the three counts. Interpretation of the three resistances is in the Bhāṣya. The eight are not a denial of form.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_29 a vak:Karika ;
    vak:hasTopic vak:VisibleResistantIndeterminate ;
    vak:belongsTo vak:Dhatunirdesa .

vak:VisibleFormPrinciple vak:visible true ;
    vak:among vak:TenFormPrinciples .
vak:TenFormPrinciples vak:resistantBy vak:Obstruction ;
    vak:includedIn vak:FormBase .
vak:EightIndeterminate vak:derivedFrom vak:TenFormPrinciples ;
    vak:excludes vak:VisibleFormPrinciple, vak:SoundPrinciple .
```
