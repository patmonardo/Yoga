# VAK_2.35 — Dissociated Formations

## 1. Sanskrit (Devanāgarī)

```sanskrit
विप्रयुक्तास्तु संस्काराः प्राप्त्यप्राप्ती सभागता ।
आसंज्ञिकं समापत्ती जीवितं लक्षणानि च ॥ २.३५ ॥
```

## 2. Sanskrit (IAST)

```text
viprayuktās tu saṃskārāḥ prāptyaprāptī sabhāgatā /
āsaṃjñikaṃ samāpattī jīvitaṃ lakṣaṇāni ca // 2.35 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| viprayuktāḥ | nom. pl. m.; past passive participle | dissociated |
| tu | particle | the new class |
| saṃskārāḥ | nom. pl. m. | formations |
| prāpti-aprāptī | nom. dual f. | acquisition and non-acquisition |
| sabhāgatā | nom. sg. f. | commonality |
| āsaṃjñikam | nom. sg. n. | listed; English not locked |
| samāpattī | nom. dual f. | two attainments |
| jīvitam | nom. sg. n. | life |
| lakṣaṇāni | nom. pl. n. | the marks |

Dissociated is the class-name. Not unconditioned. Not causally disconnected.
## 4. Grammar

```text
% start S
S[CLASS=dissociated] -> Acquisition NonAcquisition Commonality Asamjnika TwoAttainments Life Marks NameGroups
S[CLASS=dissociated] -> Formation[ASSOCIATED=false, FORM=false]
```

Not associated, not form, still conditioned.  
The duals are pairs; the plurals are not single entities.  
The members are named, not yet defined.

## 5. Translation

### Literal Translation

> The dissociated formations are acquisition and non-acquisition,
> commonality, āsaṃjñika, the two attainments, life, and the marks.
### Bhāṣya-informed study translation

> The dissociated formations are acquisition and non-acquisition,
> commonality, āsaṃjñika, the two attainments, life, and the marks.
## 6. Philosophical Translation

> Dissociated is not unconditioned and not form. The list names; it does not establish each as a distinct real.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| citta-viprayukta-saṃskāra | dissociated formation | not associated; not form; still conditioned |
| prāpti | acquisition | listed; defined next |
| aprāpti | non-acquisition | the pair |
| sabhāgatā | commonality | listed |
| āsaṃjñika | āsaṃjñika | English not locked |
| samāpatti | attainment | two; not identified here |
| jīvita | life | listed |
| lakṣaṇa | mark | plural |
| nāma-kāya | groups of names | the continuation |

## 8. Logical Determination

```python
from nltk.sem.logic import LogicParser
lp = LogicParser()

diss = lp.parse(r'all x.(Dissociated(x) -> (Formation(x) & -Associated(x) & -Form(x)))')
list = lp.parse(r'Dissociated(x) -> (Acquisition(x) | NonAcquisition(x) | Commonality(x) | Asamjnika(x) | Attainment(x) | Life(x) | Marks(x) | NameGroup(x))')
```

Named, not defined.  
Not associated, not form, still conditioned.  
The list is not a set of established reals.

## 9. Interpretive Note

**Translation note.** The commentary adds the groups of names and the rest, and explains dissociated formations as neither associated with consciousness nor possessing the nature of Form. It does not define the listed attainments, life, or marks here.

The class opens after the close of consciousness and the mental factors. No objection. No school. The members follow separately.

Āsaṃjñika is not one of the two attainments. Their definitions are not imported. Life is not defined. The marks are not enumerated.

The double negation stays in the source. The English follows the class-name.

Interpretation: occurrence and credit are not the same question. This verse names the book. It does not yet grade. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_35
    a vak:Karika ;
    rdfs:label "VAK 2.35" ;
    vak:hasTopic vak:DissociatedFormations ;
    vak:belongsTo vak:Indriyanirdesa .

vak:DissociatedFormations vak:notForm true .
vak:DissociatedFormations vak:notAssociated true .
vak:Prapti vak:definedHere false .

organon:RecordsNotClassmates
    organon:notTheVerseEnglish true .
```
