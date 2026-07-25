# VAK_3.90 — Kalpa Classification: Contraction and Expansion

## 1. Sanskrit — Devanāgarī

```sanskrit
संवर्तकल्पो नरकासंभवाद्भाजनक्षयः ।
विवर्तकल्पः प्राग्वायोर्यावन्नरकसंभवः ॥ VAkK_3.90 ॥
```

## 2. Sanskrit — IAST

```iast
saṃvartakalpo narakāsaṃbhavād bhājanakṣayaḥ /
vivartakalpaḥ prāgvāyor yāvan narakasaṃbhavaḥ // VAkK_3.90 //
```

## 3. Source Caution

The source reading is:

```iast
saṃvarttakalpo narakasaṃbhavāt bhājanakṣayaḥ /
vivartakalpaḥ prāgvāyoryāvannaraka saṃbhavaḥ // VAkK_3.90 //
```

The first pāda is read here as `naraka-asaṃbhavāt`, “from the non-arising of hell-beings,” rather than `naraka-saṃbhavāt`, because the doctrinal sense of the saṃvarta-kalpa is the period of contraction beginning when beings cease to arise in the hells and ending with destruction of the receptacle-world. The source form is compressed and should be checked against the bhāṣya and printed editions.

Sandhi has been lightly separated:

```iast
saṃvarta-kalpaḥ naraka-asaṃbhavāt bhājana-kṣayaḥ /
vivarta-kalpaḥ prāk-vāyoḥ yāvat naraka-saṃbhavaḥ //
```

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| saṃvartakalpaḥ | saṃvarta-kalpaḥ | kalpa of contraction / dissolution |
| narakāsaṃbhavāt | naraka-asaṃbhavāt | from the non-arising of hell-beings |
| bhājanakṣayaḥ | bhājana-kṣayaḥ | destruction of the receptacle-world |
| vivartakalpaḥ | vivarta-kalpaḥ | kalpa of expansion / formation |
| prāgvāyoḥ | prāk-vāyoḥ | from the first wind / prior wind |
| yāvat | yāvat | up to, until |
| narakasaṃbhavaḥ | naraka-saṃbhavaḥ | arising of hell-beings |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| saṃvarta-kalpaḥ | nominative singular masculine | subject: contraction kalpa |
| naraka-asaṃbhavāt | ablative singular compound | starting point: from non-arising of naraka beings |
| bhājana-kṣayaḥ | nominative singular masculine | endpoint / defining limit: destruction of the receptacle-world |
| vivarta-kalpaḥ | nominative singular masculine | subject: expansion kalpa |
| prāk-vāyoḥ | ablative/genitive singular compound | starting point: from the first wind |
| yāvat naraka-saṃbhavaḥ | limit phrase | until the arising of hell-beings |

## 6. Literal Translation

The contraction kalpa is from the non-arising of hell-beings to the destruction of the receptacle-world. The expansion kalpa is from the first wind up to the arising of hell-beings.

## 7. Philosophical Translation

A kalpa is now classified according to world-process. The saṃvarta-kalpa is the period of cosmic contraction: beings cease to arise in the hells, and the process culminates in the destruction of the receptacle-world. The vivarta-kalpa is the period of cosmic expansion: beginning with the primordial wind, it continues until beings again arise in the hells.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| saṃvarta | contraction / dissolution | phase of cosmic withdrawal and destruction |
| kalpa | kalpa / aeon | cosmic time-cycle |
| naraka | hell / naraka | lower realm used as marker of population/emptying |
| asaṃbhava | non-arising | cessation of birth in a realm |
| bhājana | receptacle-world | container-world, environmental world-system |
| kṣaya | destruction / exhaustion | terminal dissolution |
| vivarta | expansion / formation | phase of cosmic re-formation |
| prāk-vāyu | first wind | initial formative wind of world-expansion |
| saṃbhava | arising | beginning of birth/population in a realm |

## 9. Doctrinal Determination

VAkK_3.89 ended: `kalpo bahuvidhaḥ smṛtaḥ`, “kalpa is remembered as manyfold.” VAkK_3.90 begins the classification.

```text
saṃvarta-kalpa
    → begins with non-arising in the hells
    → ends with destruction of the receptacle-world

vivarta-kalpa
    → begins with the first wind
    → ends with the arising of hell-beings
```

The kalpa is therefore not merely long duration. It is a structured world-process.

## 10. Logical Determination

This verse gives kalpa as process-bound duration.

```text
kalpa
    → world-process interval
        → defined by beginning-limit
        → defined by ending-limit
```

A kalpa is intelligible because it has determinate thresholds: when beings cease to arise, when the receptacle-world is destroyed, when formative wind begins, and when beings again arise.

## 11. Interpretive Note

The contrast is exact:

```text
saṃvarta
    → depopulation
    → destruction of bhājana-loka

vivarta
    → first formative wind
    → repopulation down to naraka
```

The use of naraka as a boundary is significant. The world is fully expanded when even the lowest hell-realm is populated; it is entering contraction when beings no longer arise there.

## 12. Organon Interpretation

Light contact point:

```text
Kalpa is measured world-process, not empty duration.
```

For this pass, we stay close to the Kośa. The kalpa machinery defines cosmic time by the states of world-formation and world-dissolution. Time is indexed to the condition of the world-field.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_90
    a vak:Karika ;
    rdfs:label "VAK 3.90" ;
    vak:sourceReference "VAkK_3.90" ;
    vak:continues vak:VAK_3_89 ;
    vak:hasTopic vak:KalpaClassification ;
    vak:belongsTo vak:KalpaMachineryBlock .

vak:SamvartaKalpa
    a logic:CosmicProcessInterval ;
    rdfs:label "saṃvarta-kalpa" ;
    vak:hasCanonicalTranslation "contraction / dissolution kalpa" ;
    vak:beginsWith vak:NarakaNonArising ;
    vak:endsWith vak:BhajanaWorldDestruction .

vak:VivartaKalpa
    a logic:CosmicProcessInterval ;
    rdfs:label "vivarta-kalpa" ;
    vak:hasCanonicalTranslation "expansion / formation kalpa" ;
    vak:beginsWith vak:FirstWind ;
    vak:endsWith vak:NarakaArising .

vak:BhajanaWorldDestruction
    a logic:CosmicEvent ;
    rdfs:label "bhājana-kṣaya" ;
    vak:hasCanonicalTranslation "destruction of the receptacle-world" .

vak:FirstWind
    a logic:CosmicFormationEvent ;
    rdfs:label "prāk-vāyu" ;
    vak:hasCanonicalTranslation "first wind" .
```

## 14. Commit Note

Committed VAK_3.90 / VAkK_3.90.

Established:
- the manyfold kalpa classification begins.
- saṃvarta-kalpa is defined from non-arising in hells to destruction of the receptacle-world.
- vivarta-kalpa is defined from the first wind to the arising of hell-beings.
- kalpa is measured world-process, not empty duration.
