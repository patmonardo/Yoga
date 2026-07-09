# VAK_3.87 — Measure: Linear Scale from Aṅguli to Yojana

## 1. Sanskrit — Devanāgarī

```sanskrit
चतुर्विंशतिरङ्गुल्यो हस्तो हस्तचतुष्टयम् ।
धनुः पञ्चशतान्येषां क्रोशोऽरण्यं च तन्मतम् ॥ VAkK_3.87 ॥
```

## 2. Sanskrit — IAST

```iast
caturviṃśatir aṅgulyo hasto hasta-catuṣṭayam /
dhanuḥ pañcaśatāny eṣāṃ krośo 'raṇyaṃ ca tanmatam // VAkK_3.87 //
```

## 3. Source Caution

The source reading is:

```iast
caturviśatiraṅgulyo hasto hastacatuṣṭayam /
dhanuḥ pañcaśatānyeṣāṃ krośo raṇyaṃ ca tanmatam // VAkK_3.87 //
```

Sandhi has been lightly separated:

```iast
catur-viṃśatiḥ aṅgulyaḥ hastaḥ hasta-catuṣṭayam /
dhanuḥ pañca-śatāni eṣām krośaḥ araṇyam ca tat matam //
```

The source prints `raṇyaṃ`; this is provisionally read as `araṇyam`, a wilderness-distance measure associated here with the krośa. The verse continues the measure-series from VAkK_3.86: after the finger/finger-joint scale, it gives standard linear measures up to krośa/araṇya. This should be checked against the bhāṣya.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| caturviṃśatiḥ | catur-viṃśatiḥ | twenty-four |
| aṅgulyaḥ | aṅgulyaḥ | fingers / finger-breadths |
| hastaḥ | hastaḥ | cubit / forearm measure |
| hasta-catuṣṭayam | hasta-catuṣṭayam | four hastas |
| dhanuḥ | dhanuḥ | bow-length |
| pañcaśatāni | pañca-śatāni | five hundred |
| eṣām | eṣām | of these |
| krośaḥ | krośaḥ | krośa distance measure |
| araṇyam | araṇyam | wilderness-distance; provisional |
| ca | ca | and |
| tat matam | tat matam | that is regarded / considered so |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| catur-viṃśatiḥ aṅgulyaḥ | nominative plural phrase | twenty-four aṅgulis |
| hastaḥ | nominative singular masculine | predicated measure: one hasta |
| hasta-catuṣṭayam | nominative/accusative singular neuter | four hastas |
| dhanuḥ | nominative singular neuter | bow-length measure |
| pañca-śatāni eṣām | nominative/accusative plural + genitive plural | five hundred of these |
| krośaḥ | nominative singular masculine | krośa measure |
| araṇyam ca | nominative/accusative singular neuter + particle | and araṇya, provisional second name/measure |
| tat matam | neuter participial phrase | that is regarded as such |

## 6. Literal Translation

Twenty-four aṅgulis are a hasta. Four hastas are a dhanu. Five hundred of these are a krośa, and that is also regarded as an araṇya.

## 7. Philosophical Translation

The material measure-series now reaches ordinary linear space. Finger-breadths make a cubit; four cubits make a bow-length; five hundred bow-lengths make a krośa, also treated as an araṇya measure. The atomic scale has now unfolded into humanly usable spatial units.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| aṅguli | finger-breadth | bodily linear measure |
| hasta | cubit / forearm | 24 aṅgulis |
| catuṣṭaya | group of four | fourfold grouping |
| dhanuḥ | bow-length | 4 hastas |
| śata | hundred | counting multiplier |
| pañca-śata | five hundred | multiplier from dhanu to krośa |
| krośa | krośa | larger distance measure |
| araṇya | wilderness-distance | provisional name/associated measure |
| mata | regarded / accepted | conventional measure determination |

## 9. Doctrinal Determination

VAkK_3.86 carried material measure from atom through dust, nit, barley, and finger-joint. VAkK_3.87 continues this into linear bodily and distance measures.

```text
aṅguli
    × 24
        = hasta

hasta
    × 4
        = dhanuḥ

dhanuḥ
    × 500
        = krośa / araṇya
```

The world-field is measured upward from the body into traversable distance.

## 10. Logical Determination

This verse gives a conventional measure-ladder.

```text
bodily measure
    → constructed unit
        → larger distance-unit
            → traversable world-space
```

The scale moves from the body as measure to the world as measurable extension.

## 11. Interpretive Note

This confirms the movement begun in VAkK_3.85–3.86. The Kośa does not simply declare the world vast. It builds the world as a linked series of measures:

```text
paramāṇu
    → particle
        → grain
            → finger
                → cubit
                    → bow-length
                        → krośa
```

This is exactly the machinery a Buddha is said to master: the whole world as determinate measure, from invisible atom to cosmic range.

## 12. Organon Interpretation

Light contact point:

```text
World-space becomes intelligible through a lawful measure-ladder.
```

For this pass, we stay with the Kośa. The linear world is not assumed as a neutral container. It is constructed as a proportional order of units grounded in bodily and material measure.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_87
    a vak:Karika ;
    rdfs:label "VAK 3.87" ;
    vak:sourceReference "VAkK_3.87" ;
    vak:continues vak:VAK_3_86 ;
    vak:hasTopic vak:LinearMeasureSequence ;
    vak:belongsTo vak:MicroMeasureBlock .

vak:LinearMeasureSequence
    a logic:MeasureSeries ;
    rdfs:label "linear measure sequence from aṅguli to krośa" ;
    vak:hasStep vak:AnguliToHasta ;
    vak:hasStep vak:HastaToDhanu ;
    vak:hasStep vak:DhanuToKrosa .

vak:AnguliToHasta
    a logic:MeasureConversion ;
    rdfs:label "24 aṅgulis = 1 hasta" ;
    vak:sourceUnit vak:Anguli ;
    vak:targetUnit vak:Hasta ;
    vak:hasMultiplier 24 .

vak:HastaToDhanu
    a logic:MeasureConversion ;
    rdfs:label "4 hastas = 1 dhanuḥ" ;
    vak:sourceUnit vak:Hasta ;
    vak:targetUnit vak:Dhanu ;
    vak:hasMultiplier 4 .

vak:DhanuToKrosa
    a logic:MeasureConversion ;
    rdfs:label "500 dhanuḥ = 1 krośa" ;
    vak:sourceUnit vak:Dhanu ;
    vak:targetUnit vak:Krosa ;
    vak:hasMultiplier 500 .
```

## 14. Commit Note

Committed VAK_3.87 / VAkK_3.87.

Established:
- 24 aṅgulis make one hasta.
- 4 hastas make one dhanuḥ.
- 500 dhanuḥ make one krośa, also associated with araṇya.
- the atomic/material measure-series expands into humanly usable linear world-space.
