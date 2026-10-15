# VAK_2.15 — What Ceases at Death

## 1. Sanskrit (Devanāgarī)

> निरोधयत्युपरमान्नारूप्ये जीवितं मनः ।
>
> उपेक्षां चैव रूपेऽष्टौ कामे दश नवाष्टौ वा ॥ २.१५ ॥

## 2. Sanskrit (IAST)

> nirodhayaty uparamān nārūpye jīvitaṃ manaḥ /
>
> upekṣāṃ caiva rūpe 'ṣṭau kāme daśa navāṣṭau vā // 2.15 //

Uparamān nārūpye is compressed. The Bhāṣya reads it as death in the formless realm. That governs the translation. The wording is not silently repaired.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| nirodhayati | causative | brings to cessation |
| uparamān nārūpye | transmitted | death in the formless realm, by the commentary |
| jīvitam, manaḥ, upekṣām | accusative | life, mind, neutral feeling |
| rūpe aṣṭau | locative | eight in the form realm |
| kāme | locative | in the desire realm |
| daśa nava aṣṭau vā | numerals | ten, nine, or eight |

Nirodha here is cessation of possessed faculties at death. It is not abandonment, and it is not the deferred identity.

## 4. Grammar

```text
formless, at death
    life, mind, neutral feeling
    3

form
    those three and the five beginning with the eye
    8

desire, all at once
    both marks     10
    one            9
    neither        8
```

The kārikā counts are simultaneous death. Gradual death is the next clause: four, body, life, mind, and neutral feeling. They do not cease separately. A wholesome mind adds the five everywhere. That addition completes the death count. It is marked, not imported as a new topic.

## 5. Translation

### Literal Translation

Brings to cessation, at death in the formless realm, life, mind, and neutral feeling. In the form realm, eight. In the desire realm, ten, nine, or eight.

### Bhāṣya-informed study translation

Loss is now to be explained. Dying in which realm, how many faculties does one bring to cessation? In the formless realm: life, mind, and neutral feeling. In the form realm, eight: those three and the five beginning with the eye. All there are spontaneously born. They arise and die with faculties complete.

In the desire realm, ten, nine, or eight. Both sexual characteristics, ten: the eight and female and male. One, nine. Neither, eight. This is the rule for death all at once.

In gradual death, four: body, life, mind, and neutral feeling. These do not cease separately. That rule is for an afflicted or indeterminate mind. With a wholesome mind, everywhere five in addition: those beginning with faith. In the formless realm, eight. In the form realm, thirteen. The rest are to be counted the same way.

## 6. Philosophical Translation

The end is not the reverse of the beginning. 2.14 counted what is first acquired as maturation. This counts what ceases at death. In the formless realm life alone was the initial result. At death, life, mind, and neutral feeling cease. Form adds the five. Desire adds neither, one, or both marks. Gradual death ends on four that do not cease apart. A wholesome mind adds the five. Their ceasing is not their abandonment.

Organon rendering:

Consequence at the boundary. Membership is which possessed faculties cease, by realm, marks, mode of dying, and the quality of the last mind. Not the inverse of the constructor. Not the verse English.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| tyāga | loss | the heading after acquisition |
| nirodhayati | brings to cessation | at death; not abandonment |
| sakṛn-maraṇa | death all at once | the kārikā counts |
| krama-mṛtyu | gradual death | four; the next clause |
| śubha / kuśala citta | wholesome mind | adds the five |
| samagra-indriya | faculties complete | form-realm arising and dying |
| vyañjana | sexual characteristic | eight, nine, or ten |

## 8. Logical Determination

```text
formless, all at once
    = life, mind, neutral feeling
    = 3
form
    = those three + five
    = 8
desire, all at once
    = 8, 9, or 10

gradual
    = body, life, mind, neutral feeling
    = 4
    do not cease separately

wholesome mind
    = the stated count + five
formless
    = 8
form
    = 13

initial maturation-set
    ≠ terminal set
cessation at death
    ≠ to be abandoned
```

## 9. Interpretive Note

2.14 asked what is first acquired as maturation. Mind and neutral feeling were present and not in that count. Here they cease. The inventories are not the same list run backward.

All at once is the scope of the verse numbers. Gradual death is a different dependency. The four are not one substance, and a change in one at another time is not thereby a change in the others.

The five cease in a wholesome death and remain wholesome. Cessation of the occurrence is not path-abandonment, and not a denial of future continuation by the word nirodha alone.

Organon reading: the consequence is the terminal membership. The doctrine is inherited. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_15
    a vak:Karika ;
    rdfs:label "VAK 2.15" ;
    vak:hasTopic vak:CessationAtDeath ;
    vak:belongsTo vak:Indriyanirdesa .

vak:FormlessDeath vak:ceases vak:Life, vak:Mind, vak:NeutralFeeling .
vak:FormDeath vak:hasCount 8 .
vak:DesireDeath vak:hasCount 8, 9, 10 .

organon:NotTheInverse
    organon:notAbandonment true ;
    organon:notTheVerseEnglish true .
```
