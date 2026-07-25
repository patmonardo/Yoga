# VAK_3.60 — Bhājanaloka: Sun–Moon Positions and Simultaneous Day-Moments

## 1. Sanskrit — Devanāgarī

```sanskrit
अर्धेन मेरोश्चन्द्रार्कौ पञ्चाशत्सैकयोजनौ ।
अर्धरात्रोऽस्तंगमनं मध्याह्न उदयः सकृत् ॥ VAkK_3.60 ॥
```

## 2. Sanskrit — IAST

```iast
ardhena meroś candrārkau pañcāśat-saika-yojanau /
ardharātro 'staṃgamanaṃ madhyāhna udayaḥ sakṛt // VAkK_3.60 //
```

## 3. Source Caution

The source reading is:

```iast
ardhena meroścandrārkau pañcāśatsaikayojanau /
ardharātro 'staṃgamanaṃ madhyānha udayaḥ sakṛta // VAkK_3.60 //
```

Sandhi has been lightly separated:

```iast
ardhena meroḥ candra-arkau pañcāśat-sa-eka-yojanau /
ardha-rātraḥ astaṃ-gamanam madhyāhnaḥ udayaḥ sakṛt //
```

The source prints `madhyānha`, but the expected form is `madhyāhna`. The source also prints `sakṛta`; first-pass normalization reads `sakṛt`, while marking the form for Pass 2 verification against Pradhan and the bhāṣya.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| ardhena | ardhena | by half; at the half-level |
| meroḥ | meroḥ | of Meru |
| candrārkau | candra-arkau | moon and sun |
| pañcāśatsaikayojanau | pañcāśat-sa-eka-yojanau | fifty plus one yojanas; fifty-one yojanas |
| ardharātraḥ | ardha-rātraḥ | midnight |
| astaṃgamanam | astaṃ-gamanam | setting; going to setting |
| madhyāhnaḥ | madhya-ahnaḥ / madhyāhnaḥ | midday |
| udayaḥ | udayaḥ | rising |
| sakṛt | sakṛt | at once; simultaneously |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| ardhena | instrumental singular neuter | measure or position: “by/at half” |
| meroḥ | genitive singular masculine | “of Meru” |
| candra-arkau | nominative dual masculine | subject: moon and sun |
| pañcāśat-sa-eka-yojanau | nominative dual masculine compound | predicate measure of the two celestial bodies |
| ardha-rātraḥ | nominative singular masculine | one simultaneous day-moment: midnight |
| astaṃ-gamanam | nominative/accusative singular neuter | another simultaneous day-moment: setting |
| madhyāhnaḥ | nominative singular masculine | another simultaneous day-moment: midday |
| udayaḥ | nominative singular masculine | another simultaneous day-moment: rising |
| sakṛt | indeclinable | simultaneously, at one time |

## 6. Literal Translation

At half of Meru are the moon and sun, each fifty-one yojanas. Midnight, setting, midday, and rising occur at once.

## 7. Philosophical Translation

The sun and moon are placed in relation to Meru, at its half-level, and are measured as fifty-one yojanas. Their motion determines opposed local times simultaneously: where it is midnight for one region, it is sunset, midday, or sunrise for another.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| Meru | Meru | central cosmological axis |
| candra | moon | celestial body paired with the sun |
| arka | sun | celestial body paired with the moon |
| pañcāśat-sa-eka | fifty plus one | numerical measure, fifty-one |
| yojana | yojana | cosmological distance-unit |
| ardha-rātra | midnight | local temporal determination |
| astaṃ-gamana | setting | local solar event |
| madhyāhna | midday | local temporal determination |
| udaya | rising | local solar event |
| sakṛt | simultaneously | marks co-presence of opposed day-moments |

## 9. Doctrinal Determination

VAkK_3.59 gave the interval between the sun and moon. VAkK_3.60 now fixes their relation to Meru and introduces simultaneous temporal differentiation.

```text
Meru-axis
    → sun / moon position
    → local temporal opposition
```

The important doctrinal point is not astronomy in the modern sense, but world-order as a determinate field of orientation. Sunrise, midday, sunset, and midnight are not absolute moments but local determinations distributed around the world-system.

## 10. Logical Determination

This verse converts spatial cosmology into temporal differentiation.

```text
spatial axis
    → celestial motion
    → differentiated local time
```

The world-container is therefore not merely extended space. It is a structured field in which positions generate opposed appearances of time.

## 11. Interpretive Note

The verse introduces a perspectival logic inside bhājanaloka. The same celestial configuration yields different temporal determinations depending on location.

```text
one cosmic order
    many local appearances
```

This is a useful first-pass marker for the later Organon distinction between a single rational field and its locally situated projections.

## 12. Organon Interpretation

Light contact point:

```text
The same world-axis yields differentiated temporal appearances.
```

This is not yet path-doctrine, but it prepares a rational-empirical field in which orientation matters. The world is ordered, but finite beings occupy only partial standpoints within that order.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_60
    a vak:Karika ;
    rdfs:label "VAK 3.60" ;
    vak:sourceReference "VAkK_3.60" ;
    vak:continues vak:VAK_3_59 ;
    vak:hasTopic vak:SunMoonPosition ;
    vak:hasTopic vak:SimultaneousDayMoments ;
    vak:belongsTo vak:BhajanalokaBlock .

vak:SunMoonPosition
    a logic:CosmologicalDetermination ;
    rdfs:label "sun and moon position relative to Meru" ;
    vak:hasMeasure "fifty-one yojanas" .

vak:SimultaneousDayMoments
    a logic:TemporalDifferentiation ;
    rdfs:label "midnight, setting, midday, and rising occur simultaneously" .
```

## 14. Commit Note

Committed VAK_3.60 / VAkK_3.60.

Established:
- the working file prefix is `VAK`, while the source marker remains `VAkK`.
- the sun and moon are placed relative to Meru.
- local day-moments are simultaneous across the world-system.
- bhājanaloka now becomes a field of spatial-temporal orientation.
