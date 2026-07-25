# VAK_3.95 — Kalpa Machinery: Cakravartin Arising and the Four Wheel-Types

## 1. Sanskrit — Devanāgarī

```sanskrit
चक्रवर्तिसमुत्पत्तिर्नाधोऽशीतिसहस्रकात् ।
सुवर्णरूप्यताम्रायश्चक्रिणस्तेऽधरक्रमात् ॥ VAkK_3.95 ॥
```

## 2. Sanskrit — IAST

```iast
cakravarti-samutpattir nādho 'śītisahasrakāt /
suvarṇa-rūpya-tāmrāyaś-cakriṇaḥ te 'dhara-kramāt // VAkK_3.95 //
```

## 3. Source Caution

The source reading is:

```iast
cakravartisamutpattirnādho 'śītisahasrakāt /
suvarṇarūpyatāmrāyaścakriṇaḥ te 'dharakramāt // VAkK_3.95 //
```

Sandhi has been lightly separated:

```iast
cakravarti-samutpattiḥ na adhaḥ aśīti-sahasrakāt /
suvarṇa-rūpya-tāmra-ayaḥ-cakriṇaḥ te adhara-kramāt //
```

The verse gives the threshold for the arising of a cakravartin and classifies cakravartins by the material of the wheel: gold, silver, copper, and iron. `adhara-kramāt` indicates descending order.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| cakravartisamutpattiḥ | cakravarti-samutpattiḥ | arising of a wheel-turning king |
| nādho | na adhaḥ | not below |
| aśītisahasrakāt | aśīti-sahasrakāt | from eighty thousand; lifespan threshold |
| suvarṇa | suvarṇa | gold |
| rūpya | rūpya | silver |
| tāmra | tāmra | copper |
| ayaḥ | ayaḥ | iron |
| cakriṇaḥ | cakriṇaḥ | wheel-possessors, cakravartins |
| te | te | they |
| adhara-kramāt | adhara-kramāt | in descending order |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| cakravarti-samutpattiḥ | nominative singular feminine | subject: arising of a cakravartin |
| na adhaḥ | negative adverbial phrase | not below |
| aśīti-sahasrakāt | ablative singular | below / from the eighty-thousand mark |
| suvarṇa-rūpya-tāmra-ayaḥ-cakriṇaḥ | nominative plural masculine compound | wheel-kings possessing gold, silver, copper, or iron wheels |
| te | nominative plural masculine | they |
| adhara-kramāt | ablative/adverbial compound | in descending sequence |

## 6. Literal Translation

The arising of a wheel-turning king is not below [the lifespan of] eighty thousand. They are wheel-possessors of gold, silver, copper, and iron, in descending order.

## 7. Philosophical Translation

The cakravartin appears only when the human lifespan has not fallen below eighty thousand years. Wheel-turning sovereignty is itself graded: there are golden, silver, copper, and iron wheel-kings, arranged in descending order.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| cakravartin | wheel-turning king | universal monarch appearing under specific temporal conditions |
| samutpatti | arising / origination | emergence within the kalpa-wheel |
| aśīti-sahasra | eighty thousand | lifespan threshold for cakravartin arising |
| suvarṇa | gold | highest wheel-type |
| rūpya | silver | second wheel-type |
| tāmra | copper | third wheel-type |
| ayaḥ | iron | lowest wheel-type |
| cakrin | wheel-possessor | one who has the royal wheel-jewel |
| adhara-krama | descending order | ordered decline of cakravartin types |

## 9. Doctrinal Determination

VAkK_3.94 located Buddha-arising in the declining phase. VAkK_3.95 now locates cakravartin-arising at a higher lifespan threshold.

```text
cakravartin-arising
    → not below 80,000-year lifespan
```

The cakravartins are graded by wheel-material:

```text
gold wheel
    → silver wheel
        → copper wheel
            → iron wheel
```

This is a royal counterpart to the Buddha-arising doctrine: both Buddha and cakravartin are world-historical appearances, but they arise under different temporal conditions.

## 10. Logical Determination

This verse gives sovereign appearance as phase-conditioned and rank-graded.

```text
world-wheel phase
    → lifespan threshold
        → cakravartin-arising
            → graded wheel-type
```

The wheel here is not only cosmic; it is also royal and political.

## 11. Interpretive Note

The word `cakravartin` itself is crucial:

```text
cakra
    → wheel

vartin
    → one who turns / proceeds / operates

cakravartin
    → wheel-turning sovereign
```

This belongs directly to the wheel-language we are tracking. The Dharma-wheel and the royal wheel are not identical, but both are world-transforming forms of wheel-turning.

```text
Buddha
    → turns Dharma-wheel

Cakravartin
    → turns royal/worldly wheel
```

## 12. Organon Interpretation

Light contact point:

```text
World-history has different wheel-turners at different temporal thresholds.
```

For this pass, we stay close to the Kośa. The kalpa-wheel conditions not only the arising of Buddhas, but also the arising of universal monarchy. The same temporal schema gives both Dharma-historical and royal-political appearances.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_95
    a vak:Karika ;
    rdfs:label "VAK 3.95" ;
    vak:sourceReference "VAkK_3.95" ;
    vak:continues vak:VAK_3_94 ;
    vak:hasTopic vak:CakravartinArising ;
    vak:belongsTo vak:KalpaMachineryBlock .

vak:CakravartinArising
    a logic:WorldHistoricalAppearance ;
    rdfs:label "cakravarti-samutpatti" ;
    vak:hasLifespanThreshold vak:EightyThousandYearLifespan ;
    vak:hasWheelType vak:GoldenWheel ;
    vak:hasWheelType vak:SilverWheel ;
    vak:hasWheelType vak:CopperWheel ;
    vak:hasWheelType vak:IronWheel .

vak:GoldenWheel a logic:CakravartinWheel ; rdfs:label "suvarṇa-cakra" .
vak:SilverWheel a logic:CakravartinWheel ; rdfs:label "rūpya-cakra" .
vak:CopperWheel a logic:CakravartinWheel ; rdfs:label "tāmra-cakra" .
vak:IronWheel a logic:CakravartinWheel ; rdfs:label "ayaḥ-cakra" .
```

## 14. Commit Note

Committed VAK_3.95 / VAkK_3.95.

Established:
- cakravartins do not arise below the eighty-thousand-year lifespan threshold.
- cakravartins are fourfold: gold, silver, copper, and iron wheel-kings.
- their wheel-types are arranged in descending order.
- the kalpa-wheel conditions royal world-history as well as Buddha-arising.
