# VAK_3.64 — Deva-World Approach: Terrace-Devas and Mahārājikas

## 1. Sanskrit — Devanāgarī

```sanskrit
करोटपाणयस्तासु मालाधाराः सदामदाः ।
महाराजिकदेवाश्च पर्वतेष्वपि सप्तसु ॥ VAkK_3.64 ॥
```

## 2. Sanskrit — IAST

```iast
karoṭapāṇayas tāsu mālādhārāḥ sadāmadāḥ /
mahārājikadevāś ca parvateṣv api saptasu // VAkK_3.64 //
```

## 3. Source Caution

The source reading is:

```iast
karoṭapāṇayastāsu mālādhārāssadāmadāḥ /
mahārājikadevāśca parvateṣvapi saptasu // VAkK_3.64 //
```

Sandhi has been lightly separated:

```iast
karoṭa-pāṇayaḥ tāsu mālā-dhārāḥ sadā-madāḥ /
mahārājika-devāḥ ca parvateṣu api saptasu //
```

The names `Karoṭapāṇi`, `Mālādhāra`, and `Sadāmada` designate deva classes associated with the terraces. Their exact distribution across the four terraces should be checked against the bhāṣya.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| karoṭapāṇayaḥ | karoṭa-pāṇayaḥ | Karoṭapāṇis; “bowl/skull-handed” by form, but left as class-name |
| tāsu | tāsu | on/in those; referring to the terraces |
| mālādhārāḥ | mālā-dhārāḥ | Mālādhāras; garland-bearers |
| sadāmadāḥ | sadā-madāḥ | Sadāmadas; always-intoxicated / ever-delighted ones; class-name |
| mahārājikadevāḥ | mahārājika-devāḥ | Mahārājika devas |
| ca | ca | and |
| parvateṣu | parvateṣu | on the mountains |
| api | api | also / even |
| saptasu | saptasu | on seven |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| karoṭa-pāṇayaḥ | nominative plural masculine | first class of terrace-devas |
| tāsu | locative plural feminine | “on those,” referring back to the four `pariṣaṇḍāḥ` |
| mālā-dhārāḥ | nominative plural masculine | second class of terrace-devas |
| sadā-madāḥ | nominative plural masculine | third class of terrace-devas |
| mahārājika-devāḥ | nominative plural masculine | another deva class; the Mahārājikas |
| parvateṣu saptasu | locative plural masculine | on the seven mountains |
| api | indeclinable | also, extending the distribution |

## 6. Literal Translation

On those terraces are the Karoṭapāṇis, the Mālādhāras, and the Sadāmadas. The Mahārājika devas also dwell on the seven mountains.

## 7. Philosophical Translation

The four terraces of Meru are not empty structures: they are inhabited by classes of devas, named as Karoṭapāṇis, Mālādhāras, and Sadāmadas. The Mahārājika devas are also distributed across the seven mountains.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| Karoṭapāṇi | Karoṭapāṇi | deva class associated with Meru terraces |
| Mālādhāra | Mālādhāra | deva class, “garland-bearer” by literal sense |
| Sadāmada | Sadāmada | deva class, “ever-intoxicated / ever-delighted” by literal sense |
| Mahārājika-deva | Mahārājika deva | gods belonging to the realm of the Great Kings |
| pariṣaṇḍa | terrace / ledge | habitat-zone named in VAK_3.63 |
| parvata | mountain | surrounding mountain-zone |
| sapta | seven | count of mountains associated with the Mahārājikas |

## 9. Doctrinal Determination

VAkK_3.63 established the architectural approach-field through Meru’s four terraces. VAkK_3.64 now populates that field.

```text
terraces
    → Karoṭapāṇis
    → Mālādhāras
    → Sadāmadas

seven mountains
    → Mahārājika devas
```

The transition is important: divine beings appear only after the measured topology has been established.

## 10. Logical Determination

This verse converts place into habitation.

```text
measured structure
    → inhabited region
    → named deva classes
```

The divine world is therefore a structured distribution of beings across cosmological supports, not an undifferentiated supernatural realm.

## 11. Interpretive Note

The first explicit deva verse is intentionally modest. It does not yet reach the high gods of the summit or the aerial kāma-devas. It begins with beings positioned on the terraces and mountains around Meru.

```text
deva-world begins at the slopes
    not beyond the world-container
```

This supports the VAK_3d reading: the devic field is a vertical ascent within the same rational-empirical world-system.

## 12. Organon Interpretation

Light contact point:

```text
A world-level becomes concrete when its inhabitants are determined.
```

The topology of VAK_3.63 becomes a populated domain in VAK_3.64. This is a clean movement from structure to occupant, from place-form to living content.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_64
    a vak:Karika ;
    rdfs:label "VAK 3.64" ;
    vak:sourceReference "VAkK_3.64" ;
    vak:continues vak:VAK_3_63 ;
    vak:hasTopic vak:TerraceDevas ;
    vak:hasTopic vak:MaharajikaDevas ;
    vak:belongsTo vak:DevaWorldApproachBlock .

vak:TerraceDevas
    a logic:DevaClassDistribution ;
    rdfs:label "devas dwelling on Meru terraces" ;
    vak:includesDevaClass vak:Karotapani ;
    vak:includesDevaClass vak:Maladhara ;
    vak:includesDevaClass vak:Sadamada .

vak:MaharajikaDevas
    a logic:DevaClass ;
    rdfs:label "Mahārājika devas" ;
    vak:dwellsOn vak:SevenMountains .

vak:SevenMountains
    a logic:CosmologicalSupport ;
    rdfs:label "seven mountains" .
```

## 14. Commit Note

Committed VAK_3.64 / VAkK_3.64.

Established:
- the four Meru terraces are populated by named deva classes.
- Karoṭapāṇis, Mālādhāras, and Sadāmadas are treated as class-names for first-pass purposes.
- Mahārājika devas are distributed on the seven mountains.
- the deva-world begins as inhabited topology: structure becomes habitat.
