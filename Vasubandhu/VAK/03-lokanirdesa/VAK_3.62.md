# VAK_3.62 — Bhājanaloka: Solar Motion and Lunar Appearance

## 1. Sanskrit — Devanāgarī

```sanskrit
लवशो रात्र्यहर्वृद्धी दक्षिणोत्तरगे रवौ ।
स्वच्छाययार्कसामीप्याद्विकलेंदुसमीक्षणम् ॥ VAkK_3.62 ॥
```

## 2. Sanskrit — IAST

```iast
lavaśo rātryaharvṛddhī dakṣiṇottarage ravau /
svacchāyayārkasāmīpyād vikalendusamīkṣaṇam // VAkK_3.62 //
```

## 3. Source Caution

The source reading is:

```iast
lavaśo rātryaharvṛddhī dakṣiṇottarage ravau /
svacchāyayārkasāmīpyādvikalendusamīkṣaṇam // VAkK_3.62 //
```

Sandhi has been lightly separated:

```iast
lavaśaḥ rātri-ahaḥ-vṛddhī dakṣiṇa-uttara-ge ravau /
sva-chāyayā arka-sāmīpyāt vikala-indu-samīkṣaṇam //
```

The compound `vikalendu-samīkṣaṇam` is provisionally read as “the seeing of the moon as incomplete/deficient,” i.e. lunar phases or partial lunar appearance. The exact explanation should be checked in the bhāṣya.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| lavaśaḥ | lavaśaḥ | by lavas; by small increments |
| rātryaharvṛddhī | rātri-ahaḥ-vṛddhī | increases of night and day |
| dakṣiṇottarage | dakṣiṇa-uttara-ge | going south and north |
| ravau | ravau | when the sun; in the sun |
| svacchāyayā | sva-chāyayā | by its own shadow |
| arkasāmīpyāt | arka-sāmīpyāt | because of proximity to the sun |
| vikalendusamīkṣaṇam | vikala-indu-samīkṣaṇam | seeing of the moon as incomplete; lunar phase appearance |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| lavaśaḥ | adverbial expression | by small increments, lava by lava |
| rātri-ahaḥ-vṛddhī | nominative/accusative dual feminine | increase of night and day as paired magnitudes |
| dakṣiṇa-uttara-ge | locative singular masculine | when going southward or northward |
| ravau | locative singular masculine | in/with respect to the sun |
| sva-chāyayā | instrumental singular feminine | by its own shadow |
| arka-sāmīpyāt | ablative singular neuter | because of nearness to the sun |
| vikala-indu-samīkṣaṇam | nominative/accusative singular neuter | seeing the moon as incomplete |

## 6. Literal Translation

The increases of night and day occur by small increments when the sun goes south and north. The seeing of the moon as incomplete is because of its own shadow and because of proximity to the sun.

## 7. Philosophical Translation

Night and day increase gradually, in minute increments, according to the sun’s southward and northward movement. The moon appears incomplete because of its own shadow and because of its relation of nearness to the sun.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| lava | lava; small time-unit | minute increment of temporal variation |
| rātri | night | opposed temporal magnitude |
| ahaḥ | day | opposed temporal magnitude |
| vṛddhi | increase | growth of duration |
| dakṣiṇa-gati | southward motion | solar movement producing temporal variation |
| uttara-gati | northward motion | solar movement producing temporal variation |
| ravi / arka | sun | celestial source of day-night and lunar appearance relations |
| sva-chāyā | own shadow | causal condition for lunar appearance |
| sāmīpya | proximity | relational nearness |
| indu | moon | celestial body whose appearance varies |
| vikala | incomplete / deficient | partial appearance; lunar phase condition |
| samīkṣaṇa | seeing / observation | appearance to perception |

## 9. Doctrinal Determination

VAkK_3.60 established simultaneous local day-moments. VAkK_3.61 established seasonal increase and decrease of night and day. VAkK_3.62 now gives the causal-celestial explanation of that variation and also explains the moon’s changing appearance.

```text
sun's north/south motion
    → incremental increase of day/night

moon's shadow and solar proximity
    → partial lunar appearance
```

Because the sun and moon are part of the ascent into the divine world-order, this verse should be retained within the VAK_3d gods/deva-world thread rather than isolated as mere calendrical astronomy.

## 10. Logical Determination

This verse introduces mediated appearance.

```text
celestial motion
    → temporal measure

celestial relation
    → visible appearance
```

The moon is not simply what it immediately seems. Its appearance is determined by relation: its own shadow and its proximity to the sun.

## 11. Interpretive Note

The first half of the verse completes the night/day measure sequence. The second half introduces appearance as relationally conditioned.

```text
vikala-indu-samīkṣaṇa
    = seeing the moon as incomplete
    = appearance produced by conditions
```

This is a clean bridge into the deva-field. Sun and moon are both cosmological measures and devic markers. They belong to the same vertical world-order that will next be populated by terraces, gods, cities, gardens, and higher birth-modes.

## 12. Organon Interpretation

Light contact point:

```text
Appearance is not bare immediacy.
Appearance is relation-mediated manifestation.
```

The moon’s partial appearance is a small but important example of conditioned manifestation within the world-container. The rational-empirical field is not only made of things and measures, but of appearances generated through relations.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_62
    a vak:Karika ;
    rdfs:label "VAK 3.62" ;
    vak:sourceReference "VAkK_3.62" ;
    vak:continues vak:VAK_3_61 ;
    vak:hasTopic vak:SolarMotion ;
    vak:hasTopic vak:LunarAppearance ;
    vak:bridgesTo vak:DevaWorldBlock ;
    vak:belongsTo vak:BhajanalokaBlock .

vak:SolarMotion
    a logic:CosmologicalMotion ;
    rdfs:label "southward and northward motion of the sun" ;
    vak:conditions vak:DayNightIncrease .

vak:LunarAppearance
    a logic:ConditionedAppearance ;
    rdfs:label "seeing the moon as incomplete" ;
    vak:conditionedBy vak:OwnShadow ;
    vak:conditionedBy vak:SolarProximity .

vak:SolarProximity
    a logic:RelationalCondition ;
    rdfs:label "arka-sāmīpya" ;
    vak:hasCanonicalTranslation "proximity to the sun" .
```

## 14. Commit Note

Committed VAK_3.62 / VAkK_3.62.

Established:
- day and night increase incrementally according to the sun’s north/south motion.
- the moon’s partial appearance is conditioned by shadow and solar proximity.
- sun and moon are retained in VAK_3d as part of the devic ascent-field.
- VAK_3.62 bridges the calendrical celestial sequence into the deva-world section beginning at VAK_3.63.
