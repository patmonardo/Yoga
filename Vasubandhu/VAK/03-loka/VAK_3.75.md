# VAK_3.75 — World-System Scale: Human Measures Across the Four Continents

## 1. Sanskrit — Devanāgarī

```sanskrit
जाम्बूद्वीपाः प्रमाणेन चतुःसार्धत्रिहस्तकाः ।
द्विगुणोत्तरवृद्धया तु पूर्वगोदोत्तराव्हयाः ॥ VAkK_3.75 ॥
```

## 2. Sanskrit — IAST

```iast
jāmbūdvīpāḥ pramāṇena catuḥsārdhatrihastakāḥ /
dviguṇottaravṛddhayā tu purvagodottarāvhayāḥ // VAkK_3.75 //
```

## 3. Source Caution

The source reading is:

```iast
jāmbūdvīpāḥ pramāṇena catuḥsārdhatrihastakāḥ /
dviguṇottaravṛddhayā tu purvagodottarāvhayāḥ // VAkK_3.75 //
```

The compound `catuḥsārdhatrihastakāḥ` is transmitted in a compressed form. It is provisionally read as a body-measure in hastas for the humans of Jambūdvīpa, with the other named continents increasing successively by doubling. This should be checked carefully against the bhāṣya and printed editions.

Likely intended structure:

```iast
jāmbūdvīpāḥ pramāṇena ... hastakāḥ /
dvi-guṇa-uttara-vṛddhayā tu pūrva-goda-uttara-āvhayāḥ //
```

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| jāmbūdvīpāḥ | jāmbū-dvīpāḥ | inhabitants of Jambūdvīpa; Jambūdvīpa people |
| pramāṇena | pramāṇena | by measure, in measurement |
| catuḥsārdhatrihastakāḥ | catuḥ-sārdha-tri-hastakāḥ | a hasta-measure; exact parsing provisional |
| dviguṇottaravṛddhayā | dvi-guṇa-uttara-vṛddhayā | by successive doubling increase |
| tu | tu | but / indeed |
| purvagodottarāvhayāḥ | pūrva-goda-uttara-āvhayāḥ | those named Pūrva, Goda, and Uttara; i.e. the other continents |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| jāmbūdvīpāḥ | nominative plural masculine | subject: Jambūdvīpa inhabitants |
| pramāṇena | instrumental singular neuter | with respect to measure |
| catuḥsārdhatrihastakāḥ | nominative plural masculine compound | measured in hastas; exact value provisional |
| dvi-guṇa-uttara-vṛddhayā | instrumental singular feminine | by successive double increase |
| pūrva-goda-uttara-āvhayāḥ | nominative plural masculine | those named Pūrva, Goda, and Uttara |

## 6. Literal Translation

The Jambūdvīpa people, by measure, are of a hasta-measure expressed as `catuḥsārdhatri`. Those called Pūrva, Goda, and Uttara increase successively by doubling.

## 7. Philosophical Translation

The text now measures beings, not merely worlds. Human bodies differ by continent: the people of Jambūdvīpa have a specified bodily measure, while the inhabitants of the other continents — Pūrva, Goda, and Uttara — increase successively by doubling.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| Jambūdvīpa | Jambūdvīpa | southern continent; human reference-world |
| pramāṇa | measure | determinate magnitude |
| hasta | cubit / hand-measure | bodily unit of measure |
| dvi-guṇa | double | twofold increase |
| uttara-vṛddhi | successive increase | ordered increase to the next member |
| Pūrva | eastern continent | likely Pūrvavideha; abbreviated here |
| Goda | western continent | likely Godānīya / Aparagodānīya; abbreviated here |
| Uttara | northern continent | likely Uttarakuru; abbreviated here |

## 9. Doctrinal Determination

VAkK_3.73–3.74 gave the thousandfold expansion of world-systems. VAkK_3.75 returns from cosmic scale to body-measure within the four-continent world.

```text
world-system scale
    → four-continent world
    → human inhabitants
    → bodily measure by continent
    → successive doubling
```

This is still spatial and quantitative, but the focus narrows from world-domain to embodied inhabitants.

## 10. Logical Determination

This verse introduces proportional embodiment.

```text
continent
    → body-measure
    → ordered increase
```

The world-field is not only arranged by mountains, cities, suns, moons, and world-systems. It also determines the scale of bodies that arise within it.

## 11. Interpretive Note

This is a useful transition verse. The Kośa is still in a spatial-measure register, but now spatial measure is applied to embodied beings. The body is measured as belonging to a determinate continent.

```text
loka
    → continent
    → inhabitant
    → bodily magnitude
```

The shift toward time is approaching, but the present verse remains primarily about magnitude and location.

## 12. Organon Interpretation

Light contact point:

```text
A world-field determines the measure of its inhabitants.
```

For this pass, we simply observe the Kośa’s presentation: the cosmological field is not abstract space. It is inhabited, and its inhabitants are themselves quantitatively determined by their world-position.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_75
    a vak:Karika ;
    rdfs:label "VAK 3.75" ;
    vak:sourceReference "VAkK_3.75" ;
    vak:continues vak:VAK_3_74 ;
    vak:hasTopic vak:HumanBodyMeasure ;
    vak:belongsTo vak:WorldMeasureBlock .

vak:HumanBodyMeasure
    a logic:EmbodiedMeasure ;
    rdfs:label "human body-measures across the four continents" ;
    vak:hasBaseContinent vak:Jambudvipa ;
    vak:hasIncreasePattern vak:SuccessiveDoubling .

vak:SuccessiveDoubling
    a logic:MeasurePattern ;
    rdfs:label "dvi-guṇa-uttara-vṛddhi" ;
    vak:hasCanonicalTranslation "successive doubling increase" .
```

## 14. Commit Note

Committed VAK_3.75 / VAkK_3.75.

Established:
- the text turns from world-system scale back to embodied measures within the four-continent world.
- Jambūdvīpa provides the base bodily measure.
- Pūrva, Goda, and Uttara are ordered by successive doubling.
- this remains a spatial/quantitative measure verse, preparing the later shift into time/lifespan.
