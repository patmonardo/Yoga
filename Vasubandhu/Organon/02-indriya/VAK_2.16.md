# VAK_2.16 — Fruits Through Faculties

## 1. Sanskrit (Devanāgarī)

```sanskrit
क्रममृत्यौ तु चत्वारि शुभे सर्वत्र पञ्च च ।
नवाप्तिरन्त्यफलयोः सप्ताष्टनवभिर्द्वयोः ॥ २.१६ ॥
```

## 2. Sanskrit (IAST)

```text
kramamṛtyau tu catvāri śubhe sarvatra pañca ca /
navāptir antyaphalayoḥ saptāṣṭanavabhir dvayoḥ // 2.16 //
```

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
% start S
S[FRUIT=extreme, COUNT=9] -> StreamEntry | Arhatship
S[FRUIT=middle, COUNT=?c] -> OnceReturning | NonReturning
S[COUNT=11, PERSON=one] -> Arhatship[FEELING=?f]
```

Eleven unifies only under `PERSON=one` across successive feelings.

## 5. Translation

### Literal Translation

> In gradual death, however, four. With a wholesome mind, everywhere five in
> addition. Attainment of the two extreme fruits is through nine. Of the
> two, through seven, eight, or nine.

### Bhāṣya-informed study translation

> In gradual death, however, four; with a wholesome [consciousness], five
> everywhere as well. Attainment of the two extreme fruits is through nine;
> of the two middle fruits, through seven, eight, or nine.

## 6. Philosophical Translation

> Attainment is through the faculties that bring about and support disconnection. Eleven is successive possibility, not co-presence.

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

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): The extreme fruits are attained through nine.
Stream-entry takes the five beginning with faith, excluding one who has
known, with mind and neutral feeling. Arhatship takes the five, excluding
“I shall know,” with mind and any one feeling. The middle fruits take
seven, eight, or nine according to route. Eleven is not a simultaneous
count. It is one person attaining again across different feelings.

The death clauses stand in 2.15. Four do not cease separately. Five are added on a wholesome mind.

Extreme is first and last, not the last two. The stream-entry nine includes two path-names. They are not nine factors in one moment. Arhatship says any one feeling, not three together. That prepares the eleven.

Eight may be the knowledge-faculty added, or gladness added across the path-moments. The number does not identify the route.

Eleven gathers a history. The reply denies the three feelings at one time. A fallen non-returner does not regain the fruit with pleasure. Prior dispassion, attained through both paths, does not fall away. No general theory of relapse is added.

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
