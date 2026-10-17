# VAK_2.14 — First Acquired as Maturation

## 1. Sanskrit (Devanāgarī)

```sanskrit
कामेष्वादौ विपाको द्वे लभ्यते नोपपादुकैः ।
तैः षड्वा सप्त वा अष्टौ वा षड् रूपेषु एकमुत्तरे ॥ २.१४ ॥
```

## 2. Sanskrit (IAST)

```text
kāmeṣv ādau vipāko dve labhyate nopapādukaiḥ /
teḥ ṣaḍ vā sapta vā aṣṭau vā ṣaḍ rūpeṣu ekam uttare // 2.14 //
```

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
% start S
S[ACQUIRE=first, REALM=desire, BIRTH=non-spontaneous] -> Body Life
S[ACQUIRE=first, REALM=desire, BIRTH=spontaneous, SEX=?s] -> Six|Seven|Eight
S[ACQUIRE=first, REALM=form] -> Six
S[ACQUIRE=first, REALM=formless] -> Life
```

`ACQUIRE=first` fails for mind and neutral feeling at relinking.

## 5. Translation

### Literal Translation

> In the desire realm, initially, two are acquired as maturation, not by the
> spontaneously born. By them, six or seven or eight. Six in the form realm.
> One in the higher.

### Bhāṣya-informed study translation

> In the desire realm, two are first acquired as maturation, but not by the
> spontaneously born. By them, six, seven, or eight; in the Form realm, six;
> in the higher realm, one.

## 6. Philosophical Translation

> First acquisition is the maturation that opens the continuum. Afflicted mind and neutral feeling at relinking are not that opening.

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

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): In the desire realm, at the beginning, two faculties
are acquired as maturation, the body-faculty and the life-faculty, but not
by the spontaneously born. By the spontaneously born, six, seven, or eight
are acquired: six without sexual characteristic, seven with one, eight
with both. In the form realm, six. In the higher, the formless, one: life
alone. Mind and neutral feeling are not among these, because at relinking
both are necessarily afflicted.

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
