# VAK_2.30 — The Indeterminate Counts

## 1. Sanskrit (Devanāgarī)

> निवृतेऽष्टादशान्यत्र द्वादशाव्याकृते मताः ।
>
> मिद्धं सर्वाविरोधित्वाद्यत्र स्यादधिकं हि तत् ॥ २.३० ॥

## 2. Sanskrit (IAST)

> nivṛte 'ṣṭādaśānyatra dvādaśāvyākṛte matāḥ /
>
> middhaṃ sarvāvirodhitvād yatra syād adhikaṃ hi tat // 2.30 //

Anyatra is the indeterminate other than the obscured. Not elsewhere in general.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| nivṛte | locative | in the obscured |
| aṣṭādaśa | numeral | eighteen |
| anyatra | indeclinable | in the other |
| dvādaśa | numeral | twelve |
| avyākṛte | locative | in the indeterminate |
| matāḥ | nominative | are accepted |
| middham | nominative | torpor |
| sarva-avirodhitvāt | ablative | because incompatible with none |
| yatra syāt | | wherever it may occur |
| adhikam | | additional |

Indeterminate is karmic. Not the unfixed of 2.27. Torpor is not sluggishness.

## 4. Grammar

```text
obscured-indeterminate
    10 universal + 6 afflicted + vitarka, vicāra
    = 18
    view does not add

unobscured-indeterminate
    10 + vitarka, vicāra
    = 12

torpor
    compatible with wholesome, unwholesome, indeterminate
    additional wherever it occurs
```

## 5. Translation

### Literal Translation

In the obscured, eighteen. In the other indeterminate, twelve are accepted. Because torpor is incompatible with none, wherever it may occur, that is additional.

### Bhāṣya-informed study translation

In the desire realm, consciousness associated with the view of a self in the personal aggregate, or with a view grasping an extreme, is obscured-indeterminate. Eighteen: the ten, the six, vitarka, and vicāra. As before, the view is not an addition. The indeterminate other than the obscured is the unobscured-indeterminate. Twelve are accepted: the ten, vitarka, and vicāra. Teachers of the outer regions also accept indeterminate regret. On their account, thirteen.

Torpor is not incompatible with the factors already stated, since it can be wholesome, unwholesome, or indeterminate. Wherever it occurs, additional. Where twenty-two, twenty-three. Where twenty-three, twenty-four. And so forth.

## 6. Philosophical Translation

Indeterminate is not unstructured. Obscured keeps the afflicted six and drops the unwholesome two. Unobscured drops the six and does not take the wholesome ten. Afflicted and unwholesome stay apart. Wholesome and unobscured stay apart.

The two views are forms of Discrimination, as before. Present, not a nineteenth. The outer-region thirteen is regret, and it stays attributed. Torpor's thirteen on the twelve is a different thirteen.

Compatible is not present. The count rises where torpor occurs. Eighteen becoming nineteen, and twelve becoming thirteen, are applications of the rule. The prose states twenty-two and twenty-three.

Organon reading:

Possibility is not the event. Objective Logic on the mind is the pass, not the translation. Not the final pass.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| nivṛta-avyākṛta | obscured-indeterminate | afflicted, not unwholesome |
| anivṛta-avyākṛta | unobscured-indeterminate | the other |
| satkāya-dṛṣṭi | view of a self in the aggregate | named; not defined here |
| antagrāha-dṛṣṭi | extreme view | named; not defined here |
| bahirdeśaka | outer-region teachers | the attributed thirteen |
| middha | torpor | not styāna |
| avirodha | non-opposition | admissibility, not occurrence |

## 8. Logical Determination

```text
obscured
    = 10 + 6 + 2
    = 18
view
    = specialize Discrimination
    = 18

unobscured
    = 10 + 2
    = 12

outer-region regret
    = 13
    attributed

torpor occurs
    → count + 1
torpor compatible
    ↛ torpor present

22 → 23, 23 → 24
    stated
18 → 19, 12 → 13
    applications, not the prose's examples
thirteen by torpor
    ≠ thirteen by regret
```

## 9. Interpretive Note

The desire-realm five are now counted. Wholesome was 2.28. Unwholesome was 2.29. These two close the set. Higher levels are the next transition.

The views are named, not defined. No later account is imported. The alternative on regret is not decided. No school beyond outer-region teachers. The region is not identified.

And so forth leaves the rule open. It does not put every alternative in one consciousness.

Organon reading: ethical class, identity, and actual addition stay apart. A number without its derivation is not the proposition. Not the verse English.

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
