# VAK_3.83 — Time-Measure: Avīci, Animals, and Pretas

## 1. Sanskrit — Devanāgarī

```sanskrit
अर्धं प्रतापनेऽवीचावन्तःकल्पं परं पुनः ।
कल्पं तिरश्चां प्रेतानां मासान्हा शतपञ्चकम् ॥ VAkK_3.83 ॥
```

## 2. Sanskrit — IAST

```iast
ardhaṃ pratāpane 'vīcāv antaḥkalpaṃ paraṃ punaḥ /
kalpaṃ tiraścāṃ pretānāṃ māsānhā śatapañcakam // VAkK_3.83 //
```

## 3. Source Caution

The source reading is:

```iast
ardhaṃ pratāpane avīcāvantaḥkalpaṃ paraṃ punaḥ /
kalpaṃ tiraścāṃ pretānāṃ māsānhā śatapañcakam // VAkK_3.83 //
```

Sandhi has been lightly separated:

```iast
ardham pratāpane avīcau antaḥ-kalpam param punaḥ /
kalpam tiraścām pretānām māsāḥ ahāḥ śata-pañcakam //
```

The sequence is provisionally read as: Pratāpana has half [of the prior measure], Avīci has an intermediate kalpa, and beyond that animals have a kalpa. For pretas, one day is a month, and lifespan is five hundred [years by that measure]. The second pāda `māsānhā` is compressed and is read here as `māsāḥ ahāḥ`, “months are days,” i.e. a month functions as a day. This should be checked against the bhāṣya and printed editions.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| ardham | ardham | half |
| pratāpane | pratāpane | in Pratāpana hell |
| avīcau | avīcau | in Avīci hell |
| antaḥkalpam | antaḥ-kalpam | an intermediate kalpa |
| param | param | beyond, further |
| punaḥ | punaḥ | again / further |
| kalpam | kalpam | a kalpa |
| tiraścām | tiraścām | of animals; of beings going horizontally |
| pretānām | pretānām | of pretas |
| māsāḥ | māsāḥ | months |
| ahāḥ | ahāḥ | days |
| śatapañcakam | śata-pañcakam | five hundred |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| ardham | nominative/accusative singular neuter | half measure |
| pratāpane | locative singular | in Pratāpana |
| avīcau | locative singular | in Avīci |
| antaḥ-kalpam | accusative singular masculine/neuter | intermediate kalpa; lifespan measure |
| param punaḥ | adverbial phrase | further, again beyond that |
| kalpam | accusative singular masculine | a kalpa |
| tiraścām | genitive plural | of animals |
| pretānām | genitive plural | of pretas |
| māsāḥ ahāḥ | nominative plural | months are days; a month as day-unit |
| śata-pañcakam | nominative/accusative singular neuter | five hundred |

## 6. Literal Translation

In Pratāpana it is half. In Avīci, the further [lifespan] is an intermediate kalpa. Again, for animals it is a kalpa. For pretas, months are days; [their lifespan is] five hundred.

## 7. Philosophical Translation

The time-measure continues downward and outward. Pratāpana is marked by a half-measure; Avīci is measured by an intermediate kalpa. Animals may live for a kalpa, while pretas have their own time-regime: a month counts as a day, and their lifespan is five hundred by that measure.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| Pratāpana | Pratāpana hell | later hot naraka; lifespan half-measure |
| Avīci | Avīci hell | uninterrupted hell; lifespan measured by an intermediate kalpa |
| antaḥ-kalpa | intermediate kalpa | time-unit between larger cosmic measures |
| kalpa | kalpa / aeon | cosmic duration-unit |
| tiryañc | animal | animal realm; literally side-going / horizontal being |
| preta | preta | hungry ghost / departed being realm |
| māsa | month | preta day-unit in this verse |
| ahaḥ | day | daily temporal unit |
| śata-pañcaka | five hundred | lifespan count by the relevant unit |

## 9. Doctrinal Determination

VAkK_3.82 measured the six narakas beginning with Saṃjīva by using kāma-deva lifespans as day-and-night units. VAkK_3.83 continues the lower-realm time-measures and expands beyond the hot narakas.

```text
Pratāpana
    → half-measure

Avīci
    → intermediate kalpa

animals
    → kalpa

pretas
    → one month = one day
    → lifespan: 500 by that measure
```

This completes an important lower-realm temporal spread: hell, animal, and preta realms each have distinct time-regimes.

## 10. Logical Determination

This verse continues realm-specific temporal determination.

```text
realm
    → time-unit
        → lifespan-measure
```

The lower realms are not simply places of suffering or obscuration. They are also temporal structures, each with its own duration-rule.

## 11. Interpretive Note

The contrast with the previous verses is useful. High realms move from day-and-night to kalpa-scale duration; lower realms also enter kalpa-scale or altered day-measure, but with a different existential valence.

```text
higher duration
    → refined or formless birth-field

lower duration
    → painful / obscured birth-field

both
    → measured time
```

Again, the Path-Discriminator must not confuse vast duration with freedom. Long life in Avīci or among animals is still saṃsāric duration.

## 12. Organon Interpretation

Light contact point:

```text
Duration belongs to the realm as much as location does.
```

For this pass, we stay with the Kośa’s presentation. The world-field assigns beings not only a place and body, but a clock, a unit of day, and a scale of life.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_83
    a vak:Karika ;
    rdfs:label "VAK 3.83" ;
    vak:sourceReference "VAkK_3.83" ;
    vak:continues vak:VAK_3_82 ;
    vak:hasTopic vak:LowerRealmLifespanMeasure ;
    vak:belongsTo vak:TimeMeasureBlock .

vak:LowerRealmLifespanMeasure
    a logic:TemporalMeasure ;
    rdfs:label "lifespans of Avīci, animals, and pretas" ;
    vak:hasSubMeasure vak:AviciLifespanMeasure ;
    vak:hasSubMeasure vak:AnimalLifespanMeasure ;
    vak:hasSubMeasure vak:PretaLifespanMeasure .

vak:AviciLifespanMeasure
    a logic:TemporalMeasure ;
    rdfs:label "Avīci lifespan measure" ;
    vak:hasMeasureUnit vak:AntahKalpa .

vak:PretaLifespanMeasure
    a logic:TemporalMeasure ;
    rdfs:label "preta lifespan measure" ;
    vak:hasDayUnit "one month" ;
    vak:hasLifespanCount 500 .

vak:AntahKalpa
    a logic:CosmicTimeUnit ;
    rdfs:label "antaḥ-kalpa" ;
    vak:hasCanonicalTranslation "intermediate kalpa" .
```

## 14. Commit Note

Committed VAK_3.83 / VAkK_3.83.

Established:
- Pratāpana receives a half-measure.
- Avīci is measured by an intermediate kalpa.
- animals may have a kalpa lifespan.
- preta time uses a month as a day-unit, with lifespan counted as five hundred by that measure.
- lower realms also have distinct time-regimes.
