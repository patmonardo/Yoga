# VAK_3.49

## 1. Sanskrit (Devanāgarī)

> अश्वकर्णो विनितको निमिन्धरगिरिस्ततः ।
>
> द्वीपा बहिश्चक्रवाडः सप्त हैमाः स आयसः ॥ ३.४९ ॥

## 2. Sanskrit (IAST)

> aśvakarṇo vinitako nimindharagiris tataḥ /
>
> dvīpā bahiś cakravāḍaḥ sapta haimāḥ sa āyasaḥ // 3.49 //

The local witness reads `vinitaka` and `nimindhara`; these forms are preserved
pending comparison with a critical edition and variant cosmological lists.

## 3. Lexical Analysis

```text
aśvakarṇaḥ                  → aśvakarṇo
vinitakaḥ                   → vinitako
nimindhara-giriḥ            → nimindharagiriḥ
tataḥ                       → tataḥ
dvīpāḥ                      → dvīpā
bahiḥ                       → bahiś
cakravāḍaḥ                  → cakravāḍaḥ
sapta                       → sapta
haimāḥ                      → haimāḥ
saḥ                         → sa
āyasaḥ                      → āyasaḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| aśvakarṇaḥ | nominative masculine singular | Aśvakarṇa, continuing the mountain list |
| vinitakaḥ | nominative masculine singular | Vinitaka, a surrounding mountain |
| nimindhara-giriḥ | nominative masculine singular compound | Mount Nimindhara, outermost of the seven surrounding ranges |
| tataḥ | indeclinable | from there, beyond that, next |
| dvīpāḥ | nominative masculine plural | continents or island-regions |
| bahiḥ | indeclinable | outside, beyond |
| cakravāḍaḥ | nominative masculine singular | outer encircling mountain-wall |
| sapta | cardinal number | seven, referring to the mountains surrounding Sumeru |
| haimāḥ | nominative masculine plural | golden, made of gold |
| saḥ | nominative masculine singular pronoun | that one, Cakravāḍa |
| āyasaḥ | nominative masculine singular | iron, made of iron |

## 4. Grammar

The first line finishes the list begun in 3.48:

```text
[tatra santi]
    aśvakarṇaḥ
    vinitakaḥ
    nimindhara-giriḥ
```

The spatial sequence then proceeds outward:

```text
tataḥ dvīpāḥ
tebhyaḥ bahiḥ cakravāḍaḥ
```

The Bhāṣya supplies the second ablative relation: the four continents are
outside Nimindhara, and Cakravāḍa is outside the continents.

The closing predicates distribute by number:

```text
[yugandharādayaḥ] sapta [parvatāḥ] haimāḥ
saḥ [cakravāḍaḥ] āyasaḥ
```

Thus “seven” excludes central Sumeru and refers to its seven surrounding
mountains; the singular pronoun refers to the outer Cakravāḍa.

## 5. Translation

### Close syntactic construe

> [There are] Aśvakarṇa, Vinitaka, and Mount Nimindhara. Beyond them are the
> continents; outside is Cakravāḍa. The seven are golden; that one is iron.

### Bhāṣya-informed study translation

> Aśvakarṇa, Vinitaka, and Nimindhara complete the seven golden mountain-ranges
> surrounding Sumeru, with Nimindhara outermost. Beyond it lie the four
> continents, and beyond them stands the iron Cakravāḍa, enclosing the entire
> four-continent world.

The outermost position of Nimindhara, number of continents, enclosing function
of Cakravāḍa, and material assignments are supplied by the Bhāṣya.

## 6. Philosophical Translation

> The oriented field reaches determinate closure: a center, surrounding
> ranges, four continents, and an outer boundary. Each place is defined by its
> relation to the others, and the iron Cakravāḍa closes the topology of the
> four-continent world.

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| Aśvakarṇa | Aśvakarṇa | fifth surrounding mountain in the received list |
| Vinitaka | Vinitaka | sixth surrounding mountain; local witness form retained |
| Nimindhara-giri | Mount Nimindhara | seventh and outermost surrounding mountain |
| dvīpa | continent / island-region | four regions outside Nimindhara |
| bahiḥ | outside / beyond | orders successive regions by exteriority |
| Cakravāḍa | Cakravāḍa | iron mountain-wall enclosing the four-continent world |
| prākāra | rampart / enclosing wall | Bhāṣya description of the mountain-rings' function |
| haima | golden | material determination of the seven surrounding mountains |
| āyasa | iron | material determination of Cakravāḍa |

## 8. Logical Determination

### Completion of the bounded topology

```text
Sumeru at center
    → seven golden surrounding ranges
        → four continents
            → iron Cakravāḍa
```

The World System now possesses nested interiority and a terminal exterior
boundary. Cakravāḍa does not merely follow the other mountains in a list; it
encloses the four-continent world. The Bhāṣya's question about how these
structures arise begins with the next Kārikā and is treated in VAK 3.50.

## 9. Interpretive Note

VAK 3.49 completes the topology of the four-continent world:

```text
center
    → concentric enclosure
        → four continents
            → terminal boundary
```

The verse orders mountain, continent, and boundary by their position relative
to Sumeru. The Bhāṣya's following inquiry into the genesis of these structures
belongs with VAK 3.50, not this verse's translation or study.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:VAK_3_49
    a vak:Karika ;
    vak:completes loka:GreatMountainSystem ;
    vak:describes loka:FourContinentField,
        loka:CakravadaBoundary .

loka:FourContinentWorld
    loka:hasCenter loka:Sumeru ;
    loka:hasSurroundingSystem loka:SevenGoldenMountains ;
    loka:hasRegionalField loka:FourContinents ;
    loka:hasOuterBoundary loka:Cakravada .

loka:Cakravada
    a loka:IronMountainBoundary ;
    loka:encloses loka:FourContinentWorld .
```
