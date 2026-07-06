# VAK_3.76 — World-Measure: Body-Measures of Kāma-Devas and Rūpa-Devas

## 1. Sanskrit — Devanāgarī

```sanskrit
पादवृद्ध्या तनुर्यावत्सार्धक्रोशो दिवौकसाम् ।
कामिनां रूपिणां त्वादौ योजनार्धं ततः परम् ॥ VAkK_3.76 ॥
```

## 2. Sanskrit — IAST

```iast
pādavṛddhyā tanur yāvat sārdhakrośo divaukasām /
kāmināṃ rūpiṇāṃ tv ādau yojanārdhaṃ tataḥ param // VAkK_3.76 //
```

## 3. Source Caution

The source reading is:

```iast
pādabṛddhayā tanuryāva tsārdhakrośo divaukasām /
kāmināṃ rūpiṇāṃ tvādau yojanārdhaṃ tataḥ param // VAkK_3.76 //
```

The source appears to print `pādabṛddhayā`; this is normalized here as `pāda-vṛddhyā`, “by quarter-increase” or “by increase of a quarter.” Sandhi has also been separated:

```iast
pāda-vṛddhyā tanuḥ yāvat sārdha-krośaḥ divaukasām /
kāminām rūpiṇām tu ādau yojana-ardham tataḥ param //
```

The exact distribution of these body-measures across the six kāma-deva classes and the rūpa-deva classes should be checked against the bhāṣya. This first pass records the structural movement from human continent-measures to deva body-measures.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| pādavṛddhyā | pāda-vṛddhyā | by quarter-increase; by increase of a quarter |
| tanuḥ | tanuḥ | body |
| yāvat | yāvat | up to, as far as |
| sārdhakrośaḥ | sa-ardha-krośaḥ | one and a half krośas |
| divaukasām | divaukasām | of heavenly dwellers |
| kāminām | kāminām | of those belonging to kāma; desire-realm beings |
| rūpiṇām | rūpiṇām | of form-possessing beings; rūpa-devas |
| tu | tu | but / however |
| ādau | ādau | at first, initially |
| yojanārdham | yojana-ardham | half a yojana |
| tataḥ param | tataḥ param | after that, beyond that |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| pāda-vṛddhyā | instrumental singular feminine | means or pattern of increase: by quarter-increase |
| tanuḥ | nominative singular feminine | subject: body |
| yāvat sārdha-krośaḥ | limit phrase | up to one and a half krośas |
| divaukasām kāminām | genitive plural | of desire-realm heavenly dwellers |
| rūpiṇām | genitive plural | of form-realm beings |
| ādau | locative/adverb | initially, at the beginning |
| yojana-ardham | nominative/accusative singular neuter | half a yojana |
| tataḥ param | adverbial phrase | beyond that, after that |

## 6. Literal Translation

For the desire-realm heavenly dwellers, the body increases by quarters up to one and a half krośas. But for the form-possessing beings, at first it is half a yojana, and beyond that [it increases further].

## 7. Philosophical Translation

The measurement of inhabitants now rises from the human continents to the deva realms. The bodies of kāma-devas are graded by quarter-increase up to one and a half krośas; the rūpa-devas begin with a still larger measure, half a yojana, and continue beyond it.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| pāda | quarter / foot | here a fractional measure of increase |
| vṛddhi | increase | ordered growth of bodily measure |
| tanu | body | measured embodied form |
| krośa | krośa | distance-unit; here bodily measure |
| sārdha-krośa | one and a half krośas | upper measure for kāma-deva bodies |
| divaukas | heavenly dweller | deva inhabitant |
| kāmin | desire-realm being | kāma-associated deva |
| rūpin | form-possessing being | rūpa-realm being |
| yojana | yojana | larger distance-unit |
| yojanārdha | half a yojana | initial measure of rūpa-deva bodies |

## 9. Doctrinal Determination

VAkK_3.75 measured human bodies across the four continents. VAkK_3.76 extends body-measure into the deva realms.

```text
human body-measure
    → continent-based scale

kāma-deva body-measure
    → quarter-increase
    → up to one and a half krośas

rūpa-deva body-measure
    → begins at half a yojana
    → continues beyond
```

The text is still presenting spatial magnitude, but now magnitude is explicitly tied to higher modes of embodiment.

## 10. Logical Determination

This verse distinguishes embodied measure by realm.

```text
realm
    → mode of embodiment
        → body-measure
            → increase-pattern
```

The higher world-field does not abolish body. It remeasures body according to its own order.

## 11. Interpretive Note

This remains part of the spatial-measure block. The Kośa is not yet focused on lifespan or temporal duration. It is still specifying how beings occupy space: first as humans of different continents, now as devas of different realms.

```text
loka-position
    → body-scale
    → graded magnitude
```

The movement from `kāminām` to `rūpiṇām` is important. Desire-realm devas and form-realm devas are both measured, but the form realm begins at a different scale.

## 12. Organon Interpretation

Light contact point:

```text
A higher realm remeasures embodiment rather than abolishing embodiment.
```

For this pass, we stay with the Kośa’s presentation. The field determines not only where beings are, but how large their bodies are within that field.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_76
    a vak:Karika ;
    rdfs:label "VAK 3.76" ;
    vak:sourceReference "VAkK_3.76" ;
    vak:continues vak:VAK_3_75 ;
    vak:hasTopic vak:DevaBodyMeasure ;
    vak:belongsTo vak:WorldMeasureBlock .

vak:DevaBodyMeasure
    a logic:EmbodiedMeasure ;
    rdfs:label "body-measures of kāma-devas and rūpa-devas" ;
    vak:hasSubMeasure vak:KamaDevaBodyMeasure ;
    vak:hasSubMeasure vak:RupaDevaBodyMeasure .

vak:KamaDevaBodyMeasure
    a logic:EmbodiedMeasure ;
    rdfs:label "kāma-deva body-measure" ;
    vak:hasIncreasePattern vak:QuarterIncrease ;
    vak:hasUpperMeasure "one and a half krośas" .

vak:RupaDevaBodyMeasure
    a logic:EmbodiedMeasure ;
    rdfs:label "rūpa-deva body-measure" ;
    vak:hasInitialMeasure "half a yojana" .

vak:QuarterIncrease
    a logic:MeasurePattern ;
    rdfs:label "pāda-vṛddhi" ;
    vak:hasCanonicalTranslation "quarter-increase" .
```

## 14. Commit Note

Committed VAK_3.76 / VAkK_3.76.

Established:
- the measure block moves from human bodies to deva bodies.
- kāma-deva bodies increase by quarters up to one and a half krośas.
- rūpa-deva bodies begin at half a yojana and continue beyond.
- the focus remains spatial magnitude and embodied measure, preparing the coming transition into time.
