# VAK_2.34 — One Meaning, Fivefold Association

## 1. Sanskrit (Devanāgarī)

```sanskrit
चित्तं मनोऽथ विज्ञानमेकार्थं चित्तचैतसाः ।
साश्रयालम्बनाकाराः संप्रयुक्ताश्च पञ्चधा ॥ २.३४ ॥
```

## 2. Sanskrit (IAST)

```text
cittaṃ mano 'tha vijñānam ekārthaṃ cittacaitasāḥ /
sāśrayālambanākārāḥ saṃprayuktāś ca pañcadhā // 2.34 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| cittam | nom. sg. n. | consciousness |
| manaḥ | nom. sg. n. | mind |
| vijñānam | nom. sg. n. | Cognition |
| eka-artham | nom. sg. n.; compound | one meaning |
| citta-caitasāḥ | nom. pl. m.; compound | consciousness and the mental factors |
| sa-āśraya | compound adjective, nom. pl. m. | having a support |
| ālambana | nom. sg. n. | cognitive support |
| ākāra | nom. sg. n. | manner |
| saṃprayuktāḥ | nom. pl. m.; past passive participle | associated |
| pañcadhā | adverb | fivefold |

Artha is meaning. Vijñāna is Cognition. Not Principle.
## 4. Grammar

```text
% start S
S[REFERENT=one] -> Citta[FUNCTION=gather] Manas[FUNCTION=consider] Vijnana[FUNCTION=cognize]
S[ASSOCIATED=fivefold] -> Citta Caitta[SUPPORT=eq, OBJECT=eq, MANNER=eq, TIME=eq, INSTANCE=eq]
```

One referent, three functions.  
Association is five equalities, not identity of factors.

## 5. Translation

### Literal Translation

> Consciousness, mind, and Cognition have one meaning. Consciousness and the
> mental factors are associated in five ways.
### Bhāṣya-informed study translation

> Consciousness, mind, and Cognition have one meaning. Consciousness and the
> mental factors are associated through support, object, aspect, time, and
> instance.
## 6. Philosophical Translation

> One occurrence, three functions. Association is five equalities. Produced occurrence is not Citta the Universal. Dravya-equality is one instance, not substance.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| citta | consciousness | gathers; or variegated |
| manas | mind | support-function of the same occurrence |
| vijñāna | Cognition | supported Cognition; not Principle |
| ekārtha | one meaning | contextual; not every text |
| āśraya | support | the faculty depended on |
| ālambana | cognitive support | what is apprehended |
| ākāra | manner | how that support is taken |
| saṃprayoga | association | the five equalities |
| dravya-samatā | equality of instance | one of each; not substance |

What is gathered is not specified. No seed-theory is inserted.

## 8. Logical Determination

```python
from nltk.sem.logic import LogicParser
lp = LogicParser()

one = lp.parse(r'Citta(x) & Manas(x) & Vijnana(x) -> OneMeaning(x)')
five = lp.parse(r'all c f.(Associated(c,f) -> (EqSupport(c,f) & EqObject(c,f) & EqManner(c,f) & EqTime(c,f) & EqInstance(c,f)))')
```

One referent, three functions.  
Five equalities, not identity.  
One of each is not all factors one entity.

## 9. Interpretive Note

**Translation note.** The commentary gives the five relations as equality of support, cognitive object, aspect, time, and instance, illustrated by one consciousness and one of each factor. It treats manner as distinct from support and object. Its fivefold account does not resolve the previously noted questions about shared support or simultaneous occurrence.

The section closes. Distributions and particular distinctions give way to the names. Others are not a named school. The questions introduce explanations, not a developed objection.

Support is not the cognitive support. Manner is not a separate image, and not a theory of representation. Having manner is the local function.

Fivefold association does not settle the shared support of attention and equanimity, deferred at 2.25. It does not refute the alternative on vitarka and vicāra at 2.33. Level-attribution is still not moment-co-presence. Repeating the relation does not supply the missing explanation.

Interpretation: common reference, common conditions, and identity of factor stay apart. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_34
    a vak:Karika ;
    rdfs:label "VAK 2.34" ;
    vak:hasTopic vak:FivefoldAssociation ;
    vak:belongsTo vak:Indriyanirdesa .

vak:CittaManasVijnana vak:oneReferentHere true .
vak:FiveEqualities vak:includes vak:Support, vak:Alambana, vak:Akara, vak:Time, vak:Instance .

organon:ProducedOccurrenceNotTheUniversal
    organon:notTheVerseEnglish true .
```
