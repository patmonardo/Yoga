# VAK_2.30 — The Indeterminate Counts

## 1. Sanskrit (Devanāgarī)

```sanskrit
निवृतेऽष्टादशान्यत्र द्वादशाव्याकृते मताः ।
मिद्धं सर्वाविरोधित्वाद्यत्र स्यादधिकं हि तत् ॥ २.३० ॥
```

## 2. Sanskrit (IAST)

```text
nivṛte 'ṣṭādaśānyatra dvādaśāvyākṛte matāḥ /
middhaṃ sarvāvirodhitvād yatra syād adhikaṃ hi tat // 2.30 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| nivṛte | loc. sg. n. | in the obscured |
| aṣṭādaśa | numeral, indeclinable use | eighteen |
| anyatra | adverb | in the other |
| dvādaśa | numeral, indeclinable use | twelve |
| avyākṛte | loc. sg. n. | in the indeterminate |
| matāḥ | nom. pl. m.; past passive participle | are accepted |
| middham | nom. sg. n. | torpor |
| sarva-avirodhitvāt | abl. sg. n.; compound | because incompatible with none |
| yatra syāt | relative adverb + 3 sg. optative | wherever it may occur |
| adhikam | neuter adjective used adverbially | additional |

Indeterminate is karmic. Not the unfixed of 2.27. Torpor is not sluggishness.
## 4. Grammar

```text
% start S
S[ETHICAL=obscured-indeterminate] -> Eighteen
S[ETHICAL=unobscured-indeterminate] -> Twelve
S[TORPOR=true] -> Count[BASE=?b, PLUS=1]
Eighteen -> Universal[10] Afflicted[6] Vitarka Vicara
Twelve -> Universal[10] Vitarka Vicara
```

View does not add.  
Torpor is compatible with all three ethical classes and increments wherever it occurs.

## 5. Translation

### Literal Translation

> In obscured-indeterminate consciousness, there are eighteen; in the other
> indeterminate consciousness, twelve. Torpor, being incompatible with none,
> may be additional wherever it occurs.
### Bhāṣya-informed study translation

> In obscured-indeterminate consciousness, eighteen factors are accepted; in
> the other indeterminate, twelve. Torpor is compatible with all and is
> additional wherever it occurs.
## 6. Philosophical Translation

> Obscured and unobscured are two indeterminate classes. View specializes. Torpor increments; it does not redefine the base.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| nivṛta-avyākṛta | obscured-indeterminate | afflicted, not unwholesome |
| anivṛta-avyākṛta | unobscured-indeterminate | the other |
| satkāya-dṛṣṭi | view of a self in the Bases | named; not defined here |
| antagrāha-dṛṣṭi | extreme view | named; not defined here |
| bahirdeśaka | outer-region teachers | the attributed thirteen |
| middha | torpor | not styāna |
| avirodha | non-opposition | admissibility, not occurrence |

## 8. Logical Determination

```python
from nltk.sem.logic import LogicParser
lp = LogicParser()

obscured = lp.parse(r'all c.(ObscuredIndeterminate(c) -> Count(c,18))')
unobscured = lp.parse(r'all c.(UnobscuredIndeterminate(c) -> Count(c,12))')
torpor = lp.parse(r'all c.(Torpor(c) -> Count(c,base+1))')
```

View does not add.  
Torpor is compatible with all three; compatibility is not presence.  
The increment is local.

## 9. Interpretive Note

**Translation note.** The commentary derives eighteen from the ten universal, six affliction-great-ground factors, vitarka, and vicāra; the view adds none. The unobscured-indeterminate count is the ten universal with vitarka and vicāra. Because torpor may be wholesome, unwholesome, or indeterminate, it may add one to either count.

The desire-realm five are now counted. Wholesome was 2.28. Unwholesome was 2.29. These two close the set. Higher levels are the next transition.

The views are named, not defined. No later account is imported. The alternative on regret is not decided. No school beyond outer-region teachers. The region is not identified.

And so forth leaves the rule open. It does not put every alternative in one consciousness.

Interpretation: ethical class, identity, and actual addition stay apart. A number without its derivation is not the proposition. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_30
    a vak:Karika ;
    rdfs:label "VAK 2.30" ;
    vak:hasTopic vak:IndeterminateCount ;
    vak:belongsTo vak:Indriyanirdesa .

vak:ObscuredIndeterminate vak:hasCount 18 .
vak:UnobscuredIndeterminate vak:hasCount 12 .
vak:Torpor vak:countedOnlyWhenOccurrent true .

organon:CompatibleNotPresent
    organon:notTheVerseEnglish true .
```
