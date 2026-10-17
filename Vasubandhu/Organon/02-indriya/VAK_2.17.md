# VAK_2.17 — The Necessary Three

## 1. Sanskrit (Devanāgarī)

> एकादशभिरर्हत्त्वमुक्तं त्वेकस्य संभवात् ।
>
> उपेक्षाजीवितमनोयुक्तोऽवश्यं त्रयान्वितः ॥ २.१७ ॥

## 2. Sanskrit (IAST)

> ekādaśabhir arhattvam uktaṃ tv ekasya saṃbhavāt /
>
> upekṣājīvitamanoyukto 'vaśyaṃ trayānvitaḥ // 2.17 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| ekādaśabhiḥ | instrumental | through eleven |
| arhattvam uktam | nominative | arhatship is said |
| tu ekasya saṃbhavāt | ablative | because possible for one person |
| upekṣā-jīvita-manas-yuktaḥ | nominative | endowed with neutral feeling, life, or mind |
| avaśyam | indeclinable | necessarily |
| traya-anvitaḥ | nominative | accompanied by the three |

Any one is the commentary's anyatamena. The kārikā compresses it.

## 4. Grammar

```text
% start S
S[POSSESS=three] -> Neutral | Life | Mind
S[POSSESS=?p] -> Other[EXCLUDED=false]
```

The triad forces co-possession. Other faculties carry exclusion features.

## 5. Translation

### Literal Translation

Arhatship is said through eleven, however, because of the possibility for one person. One endowed with neutral feeling, life, or mind is necessarily accompanied by the three.

### Bhāṣya-informed study translation

> One who possesses any one of neutral feeling, life, or mind necessarily possesses the three. None of them is possessed without the others. With the remaining faculties there is no fixed rule. Possession is excluded by birth, by non-acquisition or loss, by dispassion, by severed roots, and by path-status. Where not excluded, possession stands.

## 6. Philosophical Translation

> The triad of neutral feeling, life, and mind is inseparable. Every other faculty is conditional.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| samanvāgata | possessing | not attained, not occurring |
| avaśyam | necessarily | none without the others |
| aniyama | no fixed rule | the remainder |
| apratilabdha | not acquired | |
| vihīna | lost | |
| samucchinna-kuśala-mūla | severed wholesome roots | lacks the five |

## 8. Logical Determination

```text
possess any one of {neutral feeling, life, mind}
    → possess all three

remainder
    → may or may not

formless
    → no eye, ear, nose, tongue, body
form or formless
    → no female, no male, no pain
ordinary person, fourth dhyāna or formless
    → no pleasure
ordinary person, third or fourth, or formless
    → no gladness
free from desire for the desire realm
    → no distress
severed roots
    → no five

possession
    ≠ occurring now
not acquired
    ≠ lost
    ≠ possessed but not operating
```

## 9. Interpretive Note

The eleven stands in 2.16. This verse changes the predicate.

The triad is reciprocal. Necessarily, and none without the others. The count is accompaniment, not exactly three and no more.

Pleasure and gladness name an ordinary person. The exclusion is not every person at those levels. Fourth dhyāna for pleasure. Third and fourth for gladness. Formless in both. Distress is dispassion, not realm alone. The five are severed roots, not a mood.

The realization-faculty exclusions are provisional where the compounds are damaged. Lacking the knowledge-faculty is not lacking all knowledge. Established in fruits is not a bar on every later path-relation.

Organon reading: one possession entails two others. The look-ahead on non-reflective is not this cut. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_17
    a vak:Karika ;
    rdfs:label "VAK 2.17" ;
    vak:hasTopic vak:NecessaryTriad ;
    vak:belongsTo vak:Indriyanirdesa .

vak:NeutralFeeling vak:entailsPossession vak:Life, vak:Mind .
vak:Remainder vak:fixedRule false .

organon:NotNonReflective
    organon:notThisVerse true ;
    organon:notTheVerseEnglish true .
```
