# VAK_2.08 — Gladness, Distress, One Neutral

## 1. Sanskrit (Devanāgarī)

> अन्यत्र सा सौमनस्यमशाता चैतसी पुनः ।
>
> दौर्मनस्यमुपेक्षा तु मध्या उभयी अविकल्पनात् ॥ २.८ ॥

## 2. Sanskrit (IAST)

> anyatra sā saumanasyam aśātā caitasī punaḥ /
>
> daurmanasyam upekṣā tu madhyā ubhayī avikalpanāt // 2.8 //

The research witness separates madhyā ubhayī avikalpanāt. The running source contracts madhyobhayyavikalpanāt. The separated forms are used here.

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
anyatra sā
    → saumanasyam
    desire realm, first dhyāna, second dhyāna

aśātā caitasī punaḥ
    → daurmanasyam

upekṣā tu madhyā
    neither agreeable nor disagreeable

ubhayī
    bodily and mental

avikalpanāt
    one faculty, because the neutral operation does not differ
```

The third dhyāna is free of prīti. The Bhāṣya identifies prīti with saumanasya. That is why agreeable mental feeling there is the pleasure-faculty.

## 5. Translation

### Literal Translation

Elsewhere, that is gladness. Disagreeable mental feeling, in turn, is distress. Neutral feeling, however, is the middle, of both kinds, because of non-differentiation.

### Bhāṣya-informed study translation

Outside the third dhyāna, in the desire realm and the first and second dhyānas, that agreeable mental feeling is the gladness-faculty. In the third dhyāna, because of dispassion toward rapture, it is the pleasure-faculty and not the gladness-faculty. Rapture is gladness.

Disagreeable mental feeling is distress. Neutral feeling is the middle: neither agreeable nor disagreeable, neither painful nor pleasurable. It is of both kinds, bodily and mental. It is made one faculty because of non-differentiation.

Mental pleasure and pain arise for the most part through differentiation. Bodily pleasure and pain do not. They arise through the force of the viṣaya, even in arhats. So those two are distinguished as faculties. Neutral feeling, bodily or mental, arises in its own course even without that differentiation, and is made one faculty. Bodily pleasure supports in one way, mental pleasure in another. Bodily pain injures in one way, mental pain in another. In neutral feeling that difference does not exist. With respect to remaining neutral, there is no division.

## 6. Philosophical Translation

Agreeable mental feeling is gladness, except in the third dhyāna, where rapture is absent and the name is pleasure. Disagreeable mental feeling is distress. Neutral feeling is the middle, bodily and mental, one faculty, because the neutral operation does not split.

Pleasure and pain split by mode because arising and effect differ. Neutral feeling does not. For the most part is kept. Differentiation is not the cause of every mental pleasure or pain.

Organon rendering:

Two projections of one agreeable mental feeling. Elsewhere the jewel is gladness. In the third dhyāna it reflects the pleasure-place. Neutral feeling is one jewel in two modes. The net does not multiply a faculty where the operation is undivided. Not the verse English.

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
