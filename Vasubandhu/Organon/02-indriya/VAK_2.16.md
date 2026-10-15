# VAK_2.16 — Fruits Through Faculties

## 1. Sanskrit (Devanāgarī)

> क्रममृत्यौ तु चत्वारि शुभे सर्वत्र पञ्च च ।
>
> नवाप्तिरन्त्यफलयोः सप्ताष्टनवभिर्द्वयोः ॥ २.१६ ॥

## 2. Sanskrit (IAST)

> kramamṛtyau tu catvāri śubhe sarvatra pañca ca /
>
> navāptir antyaphalayoḥ saptāṣṭanavabhir dvayoḥ // 2.16 //

The first half closed the death count in 2.15. This study is the fruit question.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| krama-mṛtyau | locative | in gradual death |
| catvāri | numeral | four |
| śubhe | locative | with a wholesome mind |
| sarvatra pañca ca | indeclinable | five in addition, everywhere |
| nava-āptiḥ | nominative | attainment through nine |
| antya-phalayoḥ | genitive dual | of the two extreme fruits |
| sapta-aṣṭa-navabhiḥ | instrumental | through seven, eight, or nine |
| dvayoḥ | genitive dual | of the two middle fruits |

Antya is the extremes of the four, stream-entry and arhatship, not the last two in time. The instrument is faculties. The fruit is not the set.

## 4. Grammar

```text
gradual death
    → four cease together
wholesome mind
    → five in addition

two extremes
    → through nine
    stream-entry and arhatship

two middle
    → through seven, eight, or nine
    once-returning and non-returning
```

Nine for stream-entry is not the nine for arhatship.

## 5. Translation

### Literal Translation

In gradual death, however, four. With a wholesome mind, everywhere five in addition. Attainment of the two extreme fruits is through nine. Of the two, through seven, eight, or nine.

### Bhāṣya-informed study translation

The extremes are stream-entry and arhatship. The middle are once-returning and non-returning.

Stream-entry through nine: the five beginning with faith, excluding one who has known, together with mind and neutral feeling. “I shall know” is on the uninterrupted path. The knowledge-faculty is on the path of liberation. Attainment is through both. They bring about, and support, the acquisition of disconnection.

Arhatship through nine: the five, excluding “I shall know,” together with mind and any one of pleasure, gladness, and neutral feeling.

Once-returning and non-returning, each through seven, eight, or nine. Sequential, mundane: seven, the five, neutral feeling, and mind. Supramundane: eight, the knowledge-faculty as eighth. Already free from desire: nine, as stream-entry. Non-returning differs: any one of the three feelings, by the support. A sharp sequential practitioner who enters dhyāna on the ninth path of liberation attains non-returning through eight on a mundane path: neutral feeling on the uninterrupted path, gladness on liberation. Supramundane, nine.

The Abhidharma says arhatship through eleven. It is attained through nine alone. Eleven is said because that is possible for one person, falling away and attaining again with pleasure, with gladness, and with neutral feeling. The three feelings are not at one time. A non-returner who has fallen away does not attain again with pleasure. One already free from desire does not fall away. That dispassion was attained through both paths.

## 6. Philosophical Translation

The fruit is one result. The faculties through which it is attained are not the fruit. Stream-entry and arhatship are each nine, and not the same nine. The middle fruits are seven, eight, or nine by route: sequential mundane, sequential supramundane, or from prior dispassion. Eight can be two different sets. Eleven is one person across attainments, not one moment.

Organon rendering:

Consequence and the members that mediate it. Same consequence, different membership. The number does not name the set. Not the verse English.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| śrāmaṇya-phala | fruit of the path | four |
| antya-phala | extreme fruit | stream-entry, arhatship |
| madhya | middle | once-returning, non-returning |
| ānantarya-mārga | uninterrupted path | bears “I shall know” |
| vimukti-mārga | path of liberation | bears the knowledge-faculty |
| visaṃyoga-prāpti | acquisition of disconnection | brought, then supported |
| ānupūrvika | sequential | seven or eight |
| vītarāga | already free from desire | nine |
| ekasya | of one person | the eleven |

## 8. Logical Determination

```text
stream-entry
    = five, mind, neutral feeling,
      I shall know, knowledge-faculty
    = 9
    the two realization-faculties on two paths

arhatship
    = five, mind, one of three feelings,
      knowledge-faculty, one who has known
    = 9

once-returning, non-returning
    sequential mundane          7
    sequential supramundane     8
    prior dispassion            9

sharp, ninth liberation, mundane
    neutral feeling + gladness across the two paths
    = 8
supramundane
    = 9

eleven
    = one person, repeated attainment, three feelings
    ≠ one moment

same fruit
    ↛ same set
same count
    ↛ same composition
```

## 9. Interpretive Note

The death clauses stand in 2.15. Four do not cease separately. Five are added on a wholesome mind.

Extreme is first and last, not the last two. The stream-entry nine includes two path-names. They are not nine factors in one moment. Arhatship says any one feeling, not three together. That prepares the eleven.

Eight may be the knowledge-faculty added, or gladness added across the path-moments. The number does not identify the route.

Eleven aggregates a history. The reply denies the three feelings at one time. A fallen non-returner does not regain the fruit with pleasure. Prior dispassion, attained through both paths, does not fall away. No general theory of relapse is added.

Organon reading: the result is invariant. The mediating membership is not. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_16
    a vak:Karika ;
    rdfs:label "VAK 2.16" ;
    vak:hasTopic vak:FruitAttainment ;
    vak:belongsTo vak:Indriyanirdesa .

vak:StreamEntry vak:throughCount 9 .
vak:Arhatship vak:throughCount 9 ;
    vak:acrossPerson 11 .
vak:MiddleFruit vak:throughCount 7, 8, 9 .

organon:SameFruitNotSameSet
    organon:notTheVerseEnglish true .
```
