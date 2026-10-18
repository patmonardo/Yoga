# VAK_2.15 — What Ceases at Death

## 1. Sanskrit (Devanāgarī)

```sanskrit
निरोधयत्युपरमान्नारूप्ये जीवितं मनः ।
उपेक्षां चैव रूपेऽष्टौ कामे दश नवाष्टौ वा ॥ २.१५ ॥
```

## 2. Sanskrit (IAST)

```text
nirodhayaty uparamān nārūpye jīvitaṃ manaḥ /
upekṣāṃ caiva rūpe 'ṣṭau kāme daśa navāṣṭau vā // 2.15 //
```

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
% start S
S[CEASE=death, REALM=formless] -> Life Mind Neutral
S[CEASE=death, REALM=form] -> Eight
S[CEASE=death, REALM=desire, SEX=?s] -> Ten|Nine|Eight
S[CEASE=gradual] -> Body Life Mind Neutral
S[CEASE=death, MIND=wholesome] -> ... + Five
```

Cessation features do not invert the acquisition features.

## 5. Translation

### Literal Translation

> Brings to cessation, at death in the formless realm, life, mind, and
> neutral feeling. In the form realm, eight. In the desire realm, ten, nine,
> or eight.

### Bhāṣya-informed study translation

> At death in the formless realm, life, mind, and neutral feeling are
> brought to cessation. In the Form realm, eight; in the desire realm, ten,
> nine, or eight.

## 6. Philosophical Translation

> Death does not reverse birth. The faculties that cease are those that cannot cease separately. A wholesome mind carries the five with it.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| tyāga | loss | the heading after acquisition |
| nirodhayati | brings to cessation | at death; not abandonment |
| sakṛn-maraṇa | death all at once | the kārikā counts |
| krama-mṛtyu | gradual death | four; the next clause |
| śubha / kuśala citta | wholesome mind | adds the five |
| samagra-indriya | faculties complete | Form Realm arising and dying |
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

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): One dying in the formless realm brings to cessation
life, mind, and neutral feeling. In the form realm, eight: those three and
the five beginning with the eye. In the desire realm, ten, nine, or eight,
according to sexual characteristic: ten with both sex faculties, nine with
one, eight with neither.

2.14 asked what is first acquired as maturation. Mind and neutral feeling were present and not in that count. Here they cease. The inventories are not the same list run backward.

All at once is the scope of the verse numbers. Gradual death is a different dependency. The four are not one substance, and a change in one at another time is not thereby a change in the others.

The five cease in a wholesome death and remain wholesome. Cessation of the occurrence is not path-abandonment, and not a denial of future continuation by the word nirodha alone.

Interpretation: the consequence is the terminal membership. The doctrine is inherited. Not the verse English.

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
