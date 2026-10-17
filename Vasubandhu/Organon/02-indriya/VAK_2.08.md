# VAK_2.08 — Gladness, Distress, One Neutral

## 1. Sanskrit (Devanāgarī)

> अन्यत्र सा सौमनस्यमशाता चैतसी पुनः ।
>
> दौर्मनस्यमुपेक्षा तु मध्या उभयी अविकल्पनात् ॥ २.८ ॥

## 2. Sanskrit (IAST)

> anyatra sā saumanasyam aśātā caitasī punaḥ /
>
> daurmanasyam upekṣā tu madhyā ubhayī avikalpanāt // 2.8 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| anyatra | indeclinable | elsewhere; outside the third dhyāna |
| sā | nominative | that agreeable mental feeling |
| saumanasyam | nominative | gladness |
| aśātā caitasī | nominative | disagreeable, mental |
| punaḥ | indeclinable | in turn |
| daurmanasyam | nominative | distress |
| upekṣā | nominative | neutral feeling |
| tu | particle | but |
| madhyā | nominative | the middle |
| ubhayī | nominative | of both kinds |
| avikalpanāt | ablative | because of non-differentiation |

Ubhayī is not two neutral faculties. One faculty includes bodily and mental.

## 4. Grammar

```text
% start S
S[FACULTY=gladness] -> Feeling[MODE=mental, TONE=agreeable, LEVEL!=third]
S[FACULTY=distress] -> Feeling[MODE=mental, TONE=disagreeable]
S[FACULTY=neutral] -> Feeling[TONE=neutral, MODE=?m]
```

Neutral unifies with both modes because `TONE=neutral` does not split.

## 5. Translation

### Literal Translation

Elsewhere, that is gladness. Disagreeable mental feeling, in turn, is distress. Neutral feeling, however, is the middle, of both kinds, because of non-differentiation.

### Bhāṣya-informed study translation

> Elsewhere agreeable mental feeling is gladness. Disagreeable mental feeling is distress. Neutral feeling is the middle, of both kinds, and remains one faculty because the neutral operation does not split. Pleasure and pain divide by mode; neutral feeling does not.

## 6. Philosophical Translation

> Pleasure and pain split by mode. Neutral feeling does not. The net does not multiply a faculty where the operation is undivided.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| saumanasya | gladness | agreeable mental feeling outside the third dhyāna |
| prīti | rapture | identified here with gladness; absent in the third dhyāna |
| daurmanasya | distress | disagreeable mental feeling |
| upekṣā | neutral feeling | the middle; not every equanimity |
| madhyā | middle | neither agreeable nor disagreeable |
| ubhayī | of both kinds | bodily and mental; one faculty |
| vikalpana | differentiation | how mental pleasure and pain mostly arise; not Discrimination |
| avikalpana | non-differentiation | why neutral feeling is one |
| viṣaya-vaśa | force of the viṣaya | bodily pleasure and pain, even in an arhat |
| svarasena | in its own course | how neutral feeling arises |
| upekṣaṇa | remaining neutral | the respect in which the modes do not differ |

## 8. Logical Determination

```text
disagreeable + bodily
    → pain
agreeable + bodily
    → pleasure
agreeable + mental + third dhyāna
    → pleasure
agreeable + mental + elsewhere
    → gladness
disagreeable + mental
    → distress
neutral + bodily or mental
    → one neutral faculty

mental pleasure or pain
    → mostly through differentiation
bodily pleasure or pain
    → force of the viṣaya
    → possible for an arhat

different arising or different effect
    → may split the faculty
no difference in remaining neutral
    → one faculty
```

Different mode does not force two faculties. Same tone does not force one.

## 9. Interpretive Note

2.07 left the name. This verse gives it. Elsewhere is specified: desire realm, first dhyāna, second dhyāna. Absence of the five cognition-groups explained why the third-dhyāna feeling is mental. Dispassion toward rapture explains why it is not gladness. Rapture is gladness is the local statement. It is not a rule for every text.

For the most part stays. Differentiation is not every mental pleasure or pain, and it is not affliction. The arhat may still have bodily pleasure and pain. The sentence does not say the arhat has no thought.

Neutral feeling arises in its own course. That is not the unconditioned, and it is not an advanced attainment by this sentence alone. Ubhayī keeps the modes. One faculty is the count, not the erasure of bodily and mental.

Organon reading: the net reflects agreeable mental feeling into gladness or into pleasure, by level. It reflects the two neutral modes as one jewel. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_08
    a vak:Karika ;
    rdfs:label "VAK 2.08" ;
    vak:hasTopic vak:Gladness, vak:Distress, vak:NeutralFeeling ;
    vak:belongsTo vak:Indriyanirdesa .

vak:Gladness vak:isAgreeableMentalFeeling true ;
    vak:outside vak:ThirdDhyana ;
    vak:identifiedWith vak:Rapture .
vak:Distress vak:isDisagreeableMentalFeeling true .
vak:NeutralFeeling vak:includes vak:Bodily, vak:Mental ;
    vak:oneFacultyBecause vak:NonDifferentiation .

organon:JeweledNet
    organon:projectsByLevel true ;
    organon:notTheVerseEnglish true .
```
