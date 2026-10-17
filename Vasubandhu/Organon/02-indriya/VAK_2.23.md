# VAK_2.23 — Consciousness and the Factors

## 1. Sanskrit (Devanāgarī)

```sanskrit
चित्तं चैत्ताः सहावश्यं सर्वसंस्कृतलक्षणैः ।
प्राप्त्या वा पञ्चधा चैत्ता महाभूम्यादिभेदतः ॥ २.२३ ॥
```

## 2. Sanskrit (IAST)

```text
cittaṃ caittāḥ sahāvaśyaṃ sarvasaṃskṛtalakṣaṇaiḥ /
prāptyā vā pañcadhā caittā mahābhūmyādibhedataḥ // 2.23 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| cittam | nominative | consciousness |
| caittāḥ | nominative | mental factors |
| saha avaśyam | indeclinable | necessarily together |
| saṃskṛta-lakṣaṇaiḥ | instrumental | with the marks of the conditioned |
| prāptyā | instrumental | with acquisition |
| vā | particle | a distinction of cases |
| pañcadhā | adverb | fivefold |
| mahā-bhūmi-ādi-bhedataḥ | ablative | by the division beginning with the great ground |

Citta is consciousness. It is not a substance behind the event. Caitta is the factor. Manas is not this word.

## 4. Grammar

```text
% start S
S[COARISE=true] -> Citta Caitta
S[COARISE=true, MARKS=true] -> Conditioned
S[COARISE=true, ACQUIRE=true] -> SentientDesignation
S[TYPE=caitta, CLASS=?c] -> GreatGround | WholesomeGround | AfflictionGround | UnwholesomeGround | LimitedAffliction
```

`COARISE=true` forces mutual presence.  
`ACQUIRE=true` unifies only with sentient designation.  
The five classes are features of caitta, not further co-arising minima.

## 5. Translation

### Literal Translation

> Consciousness and the mental factors, necessarily together. Everything
> with the marks of the conditioned. Or with acquisition. Mental factors are
> fivefold, by the division beginning with the great ground.

### Bhāṣya-informed study translation

> Consciousness and mental factors necessarily arise together. All
> conditioned things arise together with the marks of the conditioned; or,
> only those designated as sentient arise with acquisition. Mental factors
> are fivefold by divisions beginning with the great ground.

## 6. Philosophical Translation

> Co-arising is mutual necessity, not identity. Acquisition is restricted to sentient designation. The five classes name ranges of operation, not further co-arising units.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| citta | consciousness | not manas |
| caitta | mental factor | not a faculty |
| saṃskṛta-lakṣaṇa | mark of the conditioned | not enumerated |
| prāpti | acquisition | sentient designation only |
| sattvākhya | designated as belonging to a sentient being | the restriction |
| bhūmi | ground | gativiṣaya, range of operation |
| mahābhūmika | great-ground | every consciousness |
| parītta-kleśa-mahābhūmika | limited-affliction great-ground | the fifth name, kept |

Great is range. Not a meditative stage, and not a place.

## 8. Logical Determination

```python
from nltk.sem.logic import LogicParser
lp = LogicParser()

coarise = lp.parse(r'all x y.(Citta(x) & Caitta(y) -> CoArise(x,y))')
marks = lp.parse(r'all x.(Conditioned(x) -> Marks(x))')
acquire = lp.parse(r'all x.(SentientDesignation(x) -> Acquisition(x))')
ground = lp.parse(r'all x.(GreatGround(x) -> EveryConsciousness(x))')
```

Co-arising is mutual.  
Acquisition is restricted.  
Great-ground is the class that occurs in every consciousness.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): Consciousness and the mental factors necessarily
co-arise; neither exists without the other. Everything conditioned arises
with the marks. Acquisition accompanies only what is designated as
belonging to a sentient being. Mental factors are fivefold by the division
beginning with the great ground. The great-ground factors occur in every
consciousness.

Three relations, not one together. Reciprocal for consciousness and factors. Universal for the marks. Restricted for acquisition.

Ground is range of operation. Not a place, not automatically a meditative level, not a path-stage. The five names are not yet five exclusive sets. Members and ranges wait.

Universality of the first class does not make it wholesome. The wholesome class stays available for the next verses.

Interpretation: the controller looked toward is post this pair. The verse is the pair, and the restricted acquisition. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_23
    a vak:Karika ;
    rdfs:label "VAK 2.23" ;
    vak:hasTopic vak:CittaCaittaCoarising ;
    vak:belongsTo vak:Indriyanirdesa .

vak:Citta vak:requires vak:Caitta .
vak:Prapti vak:appliesOnlyTo vak:SentientDesignation .

organon:PraptiNotTheTranslation
    organon:notTheVerseEnglish true .
```
