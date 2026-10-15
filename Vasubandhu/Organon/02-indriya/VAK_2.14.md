# VAK_2.14 — First Acquired as Maturation

## 1. Sanskrit (Devanāgarī)

> कामेष्वादौ विपाको द्वे लभ्यते नोपपादुकैः ।
>
> तैः षड्वा सप्त वा अष्टौ वा षड् रूपेषु एकमुत्तरे ॥ २.१४ ॥

## 2. Sanskrit (IAST)

> kāmeṣv ādau vipāko dve labhyate nopapādukaiḥ /
>
> teḥ ṣaḍ vā sapta vā aṣṭau vā ṣaḍ rūpeṣu ekam uttare // 2.14 //

The kārikā witness has teḥ. The Bhāṣya supports taiḥ, by them. The witness is kept. The analysis uses taiḥ.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| kāmeṣu | locative | in the desire realm |
| ādau | locative | initially |
| vipākaḥ | nominative | as maturation |
| dve | dual | two |
| labhyate | passive | is acquired; singular with a dual |
| na upapādukaiḥ | instrumental | not by the spontaneously born |
| taiḥ | instrumental | by them |
| ṣaṭ, sapta, aṣṭau | numerals | six, seven, or eight |
| rūpeṣu | locative | in the form realm |
| ekam uttare | nominative | one in the higher |

The count is faculties first acquired as maturation. It is not every faculty present.

## 4. Grammar

```text
desire, not spontaneous
    body and life
    2

spontaneous
    no sexual characteristic     6
    one                          7
    both                         8
    eye, ear, nose, tongue, body, life, plus the marks

form
    the same six

formless, the higher
    life alone
```

Mind and neutral feeling are present at relinking. They are afflicted, so they are not in the count.

## 5. Translation

### Literal Translation

In the desire realm, initially, two are acquired as maturation, not by the spontaneously born. By them, six or seven or eight. Six in the form realm. One in the higher.

### Bhāṣya-informed study translation

Acquisition is now to be explained. How many faculties are first acquired as maturation, and in which realm? In the desire realm, initially, two: body and life. Not by the spontaneously born. So by the egg-born, the womb-born, and the moisture-born. Why not mind and neutral feeling? At relinking both are necessarily afflicted.

By the spontaneously born, six, if without sexual characteristic, as at the beginning of the age: eye, ear, nose, tongue, body, and life. Seven, if one characteristic, as among gods and others. Eight, if both. Both occur, in the unfortunate destinies.

Six in the form realm: the same six. The desire realm is called desires because desire predominates. The form realm is called forms because form predominates. One in the higher. The formless realm is higher than the form realm, beyond it in attainment and superior in rebirth. There only life is first acquired as maturation. Acquisition has been explained.

## 6. Philosophical Translation

The first matured set depends on realm, birth, and sexual characteristic. Non-spontaneous desire-realm birth begins with body and life. Spontaneous birth begins with the five and life, plus none, one, or both marks. Form begins with the six. Formless begins with life alone, as maturation. Mind and neutral feeling can be present and still not be the result.

Organon rendering:

Membership and consequence, inherited from the Vidyā. The consequence asked here is which members are first acquired as maturation. Presence is not that membership. The indriyas are being read in that light. Not the verse English.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| lābha | acquisition | the new question |
| ādau / prathamataḥ | initially | first of the new continuum |
| vipāka | maturation | the predicate of the count |
| pratisaṃdhi | relinking | where mind and neutral feeling are afflicted |
| upapāduka | spontaneously born | six, seven, or eight |
| aṇḍaja, jarāyuja, saṃsvedaja | egg-born, womb-born, moisture-born | the two |
| vyañjana | sexual characteristic | none, one, both; not a word |
| kliṣṭa | afflicted | why mind and neutral feeling are out of the count |

The birth-modes are the account. They are not rewritten as biology.

## 8. Logical Determination

```text
initial maturation-set
    = realm, birth, sexual characteristic

desire, not spontaneous
    → body, life
    = 2

desire, spontaneous, none
    → five and life
    = 6
one
    = 7
both
    = 8

form
    = 6
formless
    = life
    = 1

present at relinking
    ↛ acquired as maturation
mind and neutral feeling
    → present, afflicted, not the count
```

The six are not the six of mind. Life is in them. Mind is not.

## 9. Interpretive Note

2.13 closed the distinctions of kind. This opens acquisition. What can be connected with a realm does not settle what is first acquired there as maturation. The formless eight of 2.12 are another question. One here is the maturation-count, not the absence of mind.

Higher is attainment and rebirth, not a direction, and not liberation. The triad stays unconnected.

Organon reading: consequence is the predicate. Membership is which faculties fall under it. The doctrine is inherited. The analysis is this chapter. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_14
    a vak:Karika ;
    rdfs:label "VAK 2.14" ;
    vak:hasTopic vak:InitialAcquisition ;
    vak:belongsTo vak:Indriyanirdesa .

vak:NonSpontaneousDesire vak:initiallyAcquires vak:Body, vak:Life .
vak:FormlessRealm vak:initiallyAcquires vak:Life .
vak:MindAtRelinking vak:present true ;
    vak:acquiredAsMaturation false .

organon:MembershipConsequence
    organon:inherited true ;
    organon:notTheVerseEnglish true .
```
