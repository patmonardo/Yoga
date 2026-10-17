# VAK_2.34 — One Meaning, Fivefold Association

## 1. Sanskrit (Devanāgarī)

> चित्तं मनोऽथ विज्ञानमेकार्थं चित्तचैतसाः ।
>
> साश्रयालम्बनाकाराः संप्रयुक्ताश्च पञ्चधा ॥ २.३४ ॥

## 2. Sanskrit (IAST)

> cittaṃ mano 'tha vijñānam ekārthaṃ cittacaitasāḥ /
>
> sāśrayālambanākārāḥ saṃprayuktāś ca pañcadhā // 2.34 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| cittam | nominative | consciousness |
| manaḥ | nominative | mind |
| vijñānam | nominative | cognition |
| eka-artham | nominative | one meaning |
| citta-caitasāḥ | nominative | consciousness and the mental factors |
| sa-āśraya | | having a support |
| ālambana | | cognitive support |
| ākāra | | manner |
| saṃprayuktāḥ | | associated |
| pañcadhā | | fivefold |

Artha is meaning. Vijñāna is cognition. Not principle.

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

Consciousness, mind, and cognition have one meaning. Consciousness and the mental factors have support, cognitive support, and manner, and are associated fivefold.

### Bhāṣya-informed study translation

> Citta, manas, and vijñāna have one meaning here, three functions. Consciousness and the mental factors are associated fivefold: equality of support, cognitive support, manner, time, and instance. One consciousness, one of each factor. The referent is one; the roles are not.

## 6. Philosophical Translation

> One occurrence, three functions. Association is five equalities. Produced occurrence is not Citta the Universal. Dravya-equality is one instance, not substance.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| citta | consciousness | gathers; or variegated |
| manas | mind | support-function of the same occurrence |
| vijñāna | cognition | supported cognition; not principle |
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

The section closes. Distributions and particular distinctions give way to the names. Others are not a named school. The questions introduce explanations, not a developed objection.

Support is not the cognitive support. Manner is not a separate image, and not a theory of representation. Having manner is the local function.

Fivefold association does not settle the shared support of attention and equanimity, deferred at 2.25. It does not refute the alternative on vitarka and vicāra at 2.33. Level-attribution is still not moment-co-presence. Repeating the relation does not supply the missing explanation.

Organon reading: common reference, common conditions, and identity of factor stay apart. Not the verse English.

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
