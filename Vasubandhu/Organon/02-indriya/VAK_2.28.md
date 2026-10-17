# VAK_2.28 — How Many in the Wholesome

## 1. Sanskrit (Devanāgarī)

```sanskrit
सवितर्कविचारत्वात् कुशले कामचेतसि ।
द्वाविंशतिश्चैतसिकाः कौकृत्यमधिकं क्वचित् ॥ २.२८ ॥
```

## 2. Sanskrit (IAST)

```text
savitarkavicāratvāt kuśale kāmacetasi /
dvāviṃśatiś caitasikāḥ kaukṛtyam adhikaṃ kvacit // 2.28 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sa-vitarka-vicāratvāt | abl. sg. n.; compound | because accompanied by vitarka and vicāra |
| kuśale kāma-cetasi | loc. sg. n. + loc. sg. n. | in wholesome desire-realm consciousness |
| dvāviṃśatiḥ | nom. sg. f.; numeral | twenty-two |
| caitasikāḥ | nom. pl. m. | mental factors |
| kaukṛtyam | nom. sg. n. | regret |
| adhikam kvacit | adjective + adverb | additional, in some cases |

Kvacit keeps regret out of the wholesome ground. Consciousness itself is not one of the twenty-two.
## 4. Grammar

```text
% start S
S[REALM=desire, ETHICAL=wholesome] -> TwentyTwo[UNIVERSAL=10, WHOLESOME=10, VITARKA=true, VICARA=true]
S[REALM=desire, ETHICAL=wholesome, REGRET=true] -> TwentyThree
```

Desire-realm consciousness forces `VITARKA` and `VICARA`.  
Regret is optional; it does not redefine the base.

## 5. Translation

### Literal Translation

> In wholesome desire-realm consciousness, because it is accompanied by
> vitarka and vicāra, there are twenty-two mental factors; regret may be
> additional in some cases.
### Bhāṣya-informed study translation

> In wholesome desire-realm consciousness, twenty-two mental factors occur
> with vitarka and vicāra; regret may be additional where present.
## 6. Philosophical Translation

> The count is necessity, not inventory. Regret is optional. The name kaukṛtya is transferred from the basis; it is not the basis itself.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| kāma-cetas | desire-realm consciousness | with vitarka and vicāra |
| vitarka, vicāra | vitarka, vicāra | counted; not defined here |
| kaukṛtya | regret | the factor, not the deed |
| vipratisāra | regret in consciousness | the definition |
| kukṛta | badly done | the basis |
| hetūpacāra | cause's name on the effect | the alternative |
| ubhayādhiṣṭhāna | twofold basis | done and not done |
| āveṇika | isolated | not explained until 2.29 |

## 8. Logical Determination

```python
from nltk.sem.logic import LogicParser
lp = LogicParser()

base = lp.parse(r'all c.(Desire(c) & Wholesome(c) -> Count(c,22))')
regret = lp.parse(r'all c.(Regret(c) -> Count(c,23))')
name = lp.parse(r'Kaukrtya(x) <-> RegretWithSupport(x,BadlyDone)')
```

Twenty-two is necessity.  
Twenty-three is the optional addition.  
The name is transferred; it is not the basis.

## 9. Interpretive Note

**Translation note.** The commentary enumerates the twenty-two as the ten universal, ten wholesome, vitarka, and vicāra. It explains kaukṛtya through the badly done, while also considering transfer from object to name and from cause to effect. Wholesome regret may follow failure to do the wholesome or doing the unwholesome; kvacit marks its unfixed occurrence.

Five cases are announced. This verse is the wholesome one. Isolated is not consciousness without factors. Obscured and unobscured stay apart. Twenty-two faculties were another count. These are mental factors.

Kvacit is the unfixed of 2.27 made local. Regret can be wholesome and still not be in every wholesome consciousness. Further additions may be stated later. This is the local rule.

Two accounts of the name stay alternatives. Object-support, and cause on effect. The direction of the second is from cause to effect. Omission is included without pretending the omitted deed occurred.

Interpretation: inherited sets, realm factors, and a licensed addition. The deed is not a factor. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_28
    a vak:Karika ;
    rdfs:label "VAK 2.28" ;
    vak:hasTopic vak:WholesomeDesireCount ;
    vak:belongsTo vak:Indriyanirdesa .

vak:WholesomeDesireCount vak:hasBaseCount 22 .
vak:Regret vak:sometimesAdditional true .

organon:DeedNotFactor
    organon:notTheVerseEnglish true .
```
