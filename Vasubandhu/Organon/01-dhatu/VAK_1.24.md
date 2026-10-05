# VAK_1.24 — Form and Dharma

## 1. Sanskrit (Devanāgarī)

> विशेषणार्थं प्राधान्याद्बहुधर्माग्रसंग्रहात् ।
>
> एकमायतनं रूपमेकं धर्माख्यमुच्यते ॥ १.२४ ॥

## 2. Sanskrit (IAST)

> viśeṣaṇārthaṃ prādhānyād bahudharmāgrasaṃgrahāt /
>
> ekam āyatanaṃ rūpam ekaṃ dharmākhyam ucyate // 1.24 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| viśeṣaṇārtham | viśeṣaṇa + artham; accusative neuter singular, adverbial | for the sake of distinction; both names |
| prādhānyāt | ablative singular | because of primacy; the name form |
| bahudharmāgrasaṃgrahāt | bahu-dharma-agra-saṃgrahāt; ablative singular | because many dharmas, and the highest, are gathered; the name dharma |
| ekam āyatanam | nominative neuter singular | one essence |
| rūpam | nominative neuter singular | called form |
| ekam dharmākhyam | dharma-ākhyam; nominative neuter singular | one called dharma |
| ucyate | third person singular passive | is called; one verb, both names |

The sandhi `prādhānyād` voices `t` before `b`. The compound is two gatherings, not one: many dharmas, and the highest dharma. The verse does not call the many highest.

## 4. Grammar

```text
viśeṣaṇa-artham
    both names

prādhānyāt
    the essence called form

bahu-dharma-agra-saṃgrahāt
    the essence called dharma

ekam āyatanam rūpam ucyate
ekam dharma-ākhyam ucyate
```

One verb carries both. *Ekam* is repeated. Two essences, not one essence under two titles.

## 5. Translation

### Literal Translation

For the sake of distinction, because of primacy, and because many dharmas and the highest are gathered, one essence is called form, and one is called dharma.

### Bhāṣya-informed study translation

Why, among the ten essences included in the form-base, is one called the form-essence? And why, though all are dharma by own-nature, is one called the dharma-essence? For distinction. So that each of the ten is known as an essence, arranged as condition and what has the condition, not as one collective. Eye and the rest already have their names. What is form, and is not called eye or by those other names, is known as the form-essence. No further name is given.

Or the form-essence is named from primacy. It resists: contact with the hand and the rest makes it form. It can be shown: this, here, there. In the world too, that is what is recognized as form, not the others.

For distinction, one dharma-essence is named, not all. Many dharmas, beginning with feeling, are gathered there, so the general name dharma is used. The highest dharma, nirvāṇa, is gathered there, and not in the others.

Others say the one is called the form-essence because it is gross by its twentyfold variety, and because it is the range of three eyes: the fleshly, the divine, and the noble eye of wisdom.

## 6. Philosophical Translation

For distinction, one essence is called form, and one is called dharma.

The form-base holds ten essences. Nine already have names: eye, ear, nose, tongue, body, sound, odor, taste, tangible. The one that remains is called form. Primacy is the other reason. It resists contact. It can be shown. The world already calls it form.

The other essence is called dharma because of what it gathers. Feeling, reflection, and formations are gathered there. Nirvāṇa is gathered there, and not in the others. The many are not the highest. The highest is not the many.

Form and dharma are the two names. The ten are not one essence called form. All dharmas are not one essence called dharma.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| āyatana | essence | one called form; one called dharma |
| rūpa | form | the name, and the form-base that holds the ten |
| dharma | dharma | the name of the gathering; not a second word for essence |
| viśeṣaṇārtham | for distinction | both names |
| prādhānya | primacy | the name form |
| bahu-dharma-saṃgraha | gathering of many dharmas | beginning with feeling |
| agra | the highest | nirvāṇa; not a name for the many |
| rūpa-skandha | form-base | includes the ten; is not the one essence called form |
| viṣaya-viṣayin | condition and what has the condition | how the ten are arranged |
| sapratigha | resistant | primacy |
| sanidarśana | able to be shown | primacy |
| vedanā | feeling | first of the many gathered |
| saṃjñā | reflection | gathered under the dharma name; not manas |
| saṃskāra | formation | gathered under the dharma name |
| nirvāṇa | nirvāṇa | the highest dharma |

## 8. Logical Determination

```text
rūpa : dharma
    two essences
    one verb
    distinction belongs to both

form-base
    ten essences
    nine already named
    one called form
        primacy
        resists
        can be shown
        the world already says form
    the base is not that one essence

dharma-essence
    not every dharma
    gathers the many, beginning with feeling
        feeling, reflection, formations
    gathers the highest
        nirvāṇa
        not in the others
    the many are not the highest

others
    twentyfold
    three eyes
    not the verse

1.25 not opened
```

## 9. Interpretive Note

The hinge is the repeated *ekam*. Form and dharma are a dyad of names, not two words for the essence arrangement. The three that stand between the form-base and the principle-base are what the dharma-essence gathers. They remain bases. There is no sixth base called dharma.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_24 a vak:Karika ;
    vak:hasTopic vak:RupaDharma ;
    vak:belongsTo vak:Dhatunirdesa .

vak:FormEssence vak:namedBy vak:Distinction, vak:Primacy ;
    vak:memberOf vak:FormBase ;
    vak:notIdenticalTo vak:FormBase .

vak:DharmaEssence vak:namedBy vak:Distinction, vak:Gathering ;
    vak:gathers vak:Feeling, vak:Reflection, vak:Formations, vak:Nirvana .

vak:Rupa vak:dyad vak:Dharma .
```
