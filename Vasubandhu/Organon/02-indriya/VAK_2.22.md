# VAK_2.22 — What Arises Together

## 1. Sanskrit (Devanāgarī)

> कामेऽष्टद्रव्यकोऽशब्दः परमाणुरनिन्द्रियः ।
>
> कायेन्द्रियी नवद्रव्यः दशद्रव्योऽपरेन्द्रियः ॥ २.२२ ॥

## 2. Sanskrit (IAST)

> kāme 'ṣṭadravyako 'śabdaḥ paramāṇur anindriyaḥ /
>
> kāyendriyī navadravyaḥ daśadravyo 'parendriyaḥ // 2.22 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| kāme | locative | in the desire realm |
| aṣṭa-dravyakaḥ | nominative | of eight constituents |
| a-śabdaḥ | nominative | without sound |
| paramāṇuḥ | nominative | minimal aggregate |
| an-indriyaḥ | nominative | without a faculty |
| kāya-indriya-in | nominative | possessing the body-faculty |
| nava-dravyaḥ | nominative | of nine |
| daśa-dravyaḥ | nominative | of ten |
| apara-indriyaḥ | nominative | possessing another faculty |

Dravya counts constituents in a co-arising aggregate. Not substance.

## 4. Grammar

```text
% start S
S[REALM=desire, SOUND=false, FACULTY=none] -> Aggregate[COUNT=8]
S[REALM=desire, SOUND=false, FACULTY=body] -> Aggregate[COUNT=9]
S[REALM=desire, SOUND=false, FACULTY=other] -> Aggregate[COUNT=10]
S[REALM=desire, SOUND=true] -> Aggregate[COUNT=?c+1]
Aggregate[COUNT=8] -> Elements[4] Derived[visible,odor,taste,tangible]
```

`FACULTY=other` unifies only with one of eye, ear, nose, tongue.  
Sound adds one. The minimal aggregate is the base that cannot be smaller.

## 5. Translation

### Literal Translation

In the desire realm, a soundless minimal aggregate without a faculty consists of eight constituents. One possessing the body-faculty consists of nine. One possessing another faculty consists of ten.

### Bhāṣya-informed study translation

> Distinct character does not imply separate arising. In the desire realm the soundless minimal aggregate without a faculty is eight: the four great elements and visible form, odor, taste, and the tangible. With the body-faculty it is nine. With another faculty it is ten. Sound adds one. The minimal aggregate is the smallest that still co-arises.

## 6. Philosophical Translation

> Co-arising is not identity of character. The minimal aggregate is the smallest set that cannot arise apart. Faculty and sound are additions, not further minima.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| niyata-sahotpāda | necessary co-arising | the new question |
| paramāṇu | minimal aggregate | most subtle cluster |
| dravya | constituent | not substance |
| mahābhūta | great element | earth, water, fire, air |
| upādāya-rūpa | derived form | the four in the eight |
| aparendriya | another faculty | eye, ear, nose, or tongue |
| upātta-mahābhūta-hetuka | caused by appropriated great elements | the sound that can conjoin |

## 8. Logical Determination

```python
from nltk.sem.logic import LogicParser
lp = LogicParser()

base = lp.parse(r'all x.(Minimal(x) & Desire(x) & -Sound(x) & -Faculty(x) -> Count(x,8))')
body = lp.parse(r'all x.(Minimal(x) & Faculty(x,body) -> Count(x,9))')
other = lp.parse(r'all x.(Minimal(x) & Faculty(x,other) -> Count(x,10))')
sound = lp.parse(r'all x.(Sound(x) -> Count(x,n+1))')
```

Distinct character does not force separate arising.  
The base is the smallest co-arising set.  
Faculty and sound are increments, not new minima.

## 9. Interpretive Note

The faculty-property differentiation closed at 2.21. This asks a different relation.

Hard, fluid, hot, and moving are predominance, not the absence of the others. Activities are offered: holding together, sustaining, ripening, spreading. Others say heat in water is known from greater cold. The reply: greater intensity need not be mixture, as with sound or feeling. Others say presence as seed, not in own form, citing the elements in a log. Seed is not actual form under another name.

Visible color in wind is said to be accepted, not inferred. An inference is then offered from odor in moving air. The tension is kept.

Eight is not every individual determination, and not four essences. Support is counted as constituent. Supported is counted by essence. Repeated elemental quartets are counted by kind. Words may be chosen. The meaning is what is examined. The damaged compounds stay marked in the bhāṣya.

Organon reading: the unit of the count has to travel with the number. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_22
    a vak:Karika ;
    rdfs:label "VAK 2.22" ;
    vak:hasTopic vak:MaterialCoarising ;
    vak:belongsTo vak:Indriyanirdesa .

vak:SoundlessBase vak:hasCount 8 .
vak:BodyCluster vak:hasCount 9 .
vak:OtherSenseCluster vak:hasCount 10 .

organon:CoarisingNotPossession
    organon:notTheVerseEnglish true .
```
