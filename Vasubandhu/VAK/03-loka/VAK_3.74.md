# VAK_3.74 — World-System Scale: Medium and Great Thousandfold World-Systems

## 1. Sanskrit — Devanāgarī

```sanskrit
तत्सहस्रं द्विसाहस्रो लोकधातुस्तु मध्यमः ।
तत्सहस्रं त्रिसाहस्रः समसंवर्तसंभवः ॥ VAkK_3.74 ॥
```

## 2. Sanskrit — IAST

```iast
tatsahasraṃ dvisāhasro lokadhātus tu madhyamaḥ /
tatsahasraṃ trisāhasraḥ samasaṃvarta-saṃbhavaḥ // VAkK_3.74 //
```

## 3. Source Caution

The source reading is:

```iast
tatsahasraṃ dvisāhasro lokadhātustu madhyamaḥ /
tatsahasraṃ trisāhasraḥ samasaṃvartasaṃbhavaḥ // VAkK_3.74 //
```

Sandhi has been lightly separated:

```iast
tat-sahasram dvi-sāhasraḥ loka-dhātuḥ tu madhyamaḥ /
tat-sahasram tri-sāhasraḥ sama-saṃvarta-saṃbhavaḥ //
```

`dvi-sāhasra` and `tri-sāhasra` are treated here as second- and third-order thousandfold aggregations. `sama-saṃvarta-saṃbhava` is provisionally read as sharing a common dissolution and arising. The exact cosmological formula should be checked against the bhāṣya.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| tatsahasram | tat-sahasram | a thousand of that; a thousand of the prior thousandfold system |
| dvisāhasraḥ | dvi-sāhasraḥ | two-thousandfold / second-order thousandfold |
| lokadhātuḥ | loka-dhātuḥ | world-domain, world-system |
| tu | tu | but / indeed |
| madhyamaḥ | madhyamaḥ | middle / medium |
| tatsahasram | tat-sahasram | a thousand of that again |
| trisāhasraḥ | tri-sāhasraḥ | three-thousandfold / third-order thousandfold |
| samasaṃvartasaṃbhavaḥ | sama-saṃvarta-saṃbhavaḥ | having common dissolution and arising |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| tat-sahasram | nominative/accusative singular neuter | a thousand of that previous aggregate |
| dvi-sāhasraḥ | nominative singular masculine | second-order thousandfold aggregate |
| loka-dhātuḥ | nominative singular masculine | world-domain / world-system |
| madhyamaḥ | nominative singular masculine | middle, medium; qualifies `loka-dhātuḥ` |
| tat-sahasram | nominative/accusative singular neuter | a thousand of that middle aggregate |
| tri-sāhasraḥ | nominative singular masculine | third-order thousandfold aggregate |
| sama-saṃvarta-saṃbhavaḥ | nominative singular masculine compound | characterized by common dissolution and arising |

## 6. Literal Translation

A thousand of that is the middle world-domain, the second thousandfold. A thousand of that is the third thousandfold, having common dissolution and arising.

## 7. Philosophical Translation

The small thousandfold world-system becomes the unit for a larger aggregate: a thousand of those forms the middle, second-order thousandfold world-domain. A thousand of that middle aggregate forms the third-order thousandfold system, whose worlds undergo dissolution and arising together.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| tat-sahasra | a thousand of that | iterative expansion from prior aggregate |
| dvi-sāhasra | second thousandfold | middle-order world-system |
| loka-dhātu | world-domain | world-system as a domain, not merely a place |
| madhyama | middle / medium | intermediate scale between small and great |
| tri-sāhasra | third thousandfold | great thousandfold world-system |
| saṃvarta | dissolution / contraction | world-system destruction phase |
| saṃbhava | arising / coming-to-be | world-system formation phase |
| sama | common / shared | shared process across the aggregate |

## 9. Doctrinal Determination

VAkK_3.73 established the small thousandfold world-system. VAkK_3.74 iterates that unit into larger aggregates.

```text
small thousandfold system
    × 1000
        = middle / second-order thousandfold world-domain

middle thousandfold system
    × 1000
        = third-order thousandfold world-system
        = common dissolution and arising
```

The text now presents cosmos as scaled iteration with shared cycles of formation and destruction.

## 10. Logical Determination

This verse introduces recursive aggregation.

```text
unit
    → thousandfold aggregate
        → thousandfold of the thousandfold
            → thousandfold of the thousandfold of the thousandfold
```

The world-domain is therefore a repeatable and recursively scaled structure.

## 11. Interpretive Note

The phrase `loka-dhātu` is important. This is a world-domain, not merely a container. The domain has internal inhabitants, celestial markers, deva-fields, Brahma-worlds, and now shared cycles of arising and dissolution.

```text
loka-dhātu
    = domain of world-appearance
    = scaled territory of arising and dissolution
```

For this pass, we should simply observe the Kośa’s presentation: the local deva-world is being placed inside a much larger recurring cosmological aggregate.

## 12. Organon Interpretation

Light contact point:

```text
The world-field becomes recursive and cyclic.
```

Without over-reading the verse, the structural point is clear: a world can be a unit, a unit can be aggregated, and an aggregate can share common arising and dissolution. The territory of appearance is not only visible and inhabited; it is scalable and cyclical.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_74
    a vak:Karika ;
    rdfs:label "VAK 3.74" ;
    vak:sourceReference "VAkK_3.74" ;
    vak:continues vak:VAK_3_73 ;
    vak:hasTopic vak:MiddleThousandfoldWorldSystem ;
    vak:hasTopic vak:GreatThousandfoldWorldSystem ;
    vak:belongsTo vak:WorldSystemScaleBlock .

vak:MiddleThousandfoldWorldSystem
    a logic:CosmologicalAggregate ;
    rdfs:label "middle / second-order thousandfold world-domain" ;
    vak:aggregates vak:SmallThousandfoldWorldSystem ;
    vak:hasUnitCount 1000 .

vak:GreatThousandfoldWorldSystem
    a logic:CosmologicalAggregate ;
    rdfs:label "third-order thousandfold world-system" ;
    vak:aggregates vak:MiddleThousandfoldWorldSystem ;
    vak:hasUnitCount 1000 ;
    vak:hasCommonProcess vak:CommonDissolutionAndArising .

vak:CommonDissolutionAndArising
    a logic:CyclicWorldProcess ;
    rdfs:label "sama-saṃvarta-saṃbhava" ;
    vak:hasCanonicalTranslation "common dissolution and arising" .
```

## 14. Commit Note

Committed VAK_3.74 / VAkK_3.74.

Established:
- a thousand small thousandfold systems form the middle / second-order thousandfold world-domain.
- a thousand middle systems form the third-order thousandfold world-system.
- the great aggregate shares common dissolution and arising.
- the world-field is presented as recursive, scalable, and cyclic.
