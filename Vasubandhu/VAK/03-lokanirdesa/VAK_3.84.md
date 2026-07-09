# VAK_3.84 — Time-Measure: Cold Naraka Lifespans

## 1. Sanskrit — Devanāgarī

```sanskrit
वाहाद्वर्षशतेनैकतिलोद्धारक्षयायुषः ।
अर्बुदा द्विंशतिगुणप्रतिवृद्ध्यायुषः परे ॥ VAkK_3.84 ॥
```

## 2. Sanskrit — IAST

```iast
vāhād varṣaśatenaika-tiloddhāra-kṣayāyuṣaḥ /
arbudā dviṃśatiguṇa-prativṛddhy-āyuṣaḥ pare // VAkK_3.84 //
```

## 3. Source Caution

The source reading is:

```iast
vāhādvarṣaśatenaikatiloddhārakṣayāyuṣaḥ /
arvudā dviṃśatiguṇaprativṛddhayāyuṣaḥ pare // VAkK_3.84 //
```

Sandhi has been lightly separated:

```iast
vāhāt varṣa-śatena eka-tila-uddhāra-kṣaya-āyuṣaḥ /
arbudāḥ dviṃśati-guṇa-prativṛddhi-āyuṣaḥ pare //
```

The source prints `arvudā`; the normalized Sanskrit form is `arbudāḥ`, referring to the Arbuda cold naraka and the following cold narakas. The first pāda is read as an analogy: the lifespan of Arbuda is the time it would take to exhaust a vāha-measure of sesame seeds by removing one seed every hundred years. The following cold narakas increase by twentyfold increments. This should be checked against the bhāṣya.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| vāhāt | vāhāt | from a vāha measure; a large measure/container |
| varṣaśatena | varṣa-śatena | by one hundred years; every hundred years |
| eka | eka | one |
| tiloddhāra | tila-uddhāra | removal of a sesame seed |
| kṣayāyuṣaḥ | kṣaya-āyuṣaḥ | lifespan lasting until exhaustion |
| arbudāḥ | arbudāḥ | Arbuda and related cold naraka beings; normalized |
| dviṃśatiguṇa | dviṃśati-guṇa | twentyfold |
| prativṛddhi | prativṛddhi | successive increase |
| āyuṣaḥ | āyuṣaḥ | lifespans |
| pare | pare | the others, the subsequent ones |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| vāhāt | ablative singular | from a vāha measure |
| varṣa-śatena | instrumental singular | by a hundred-year interval |
| eka-tila-uddhāra | compound | removing one sesame seed |
| kṣaya-āyuṣaḥ | nominative plural masculine | those whose lifespan lasts until exhaustion |
| arbudāḥ | nominative plural masculine | the Arbuda cold naraka beings / narakas; normalized |
| dviṃśati-guṇa-prativṛddhi-āyuṣaḥ | nominative plural masculine compound | having lifespans increasing successively twentyfold |
| pare | nominative plural masculine | the later ones, subsequent cold narakas |

## 6. Literal Translation

The Arbudas have a lifespan lasting until the exhaustion of a vāha by removing one sesame seed every hundred years. The subsequent ones have lifespans successively increased twentyfold.

## 7. Philosophical Translation

The cold narakas are measured by an almost inconceivable duration: Arbuda lasts as long as it would take to empty a great vāha of sesame seeds if only one seed were removed every hundred years. Each following cold naraka increases that lifespan twentyfold.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| vāha | vāha-measure | large capacity measure used in the duration analogy |
| varṣa-śata | hundred years | interval for each sesame-seed removal |
| tila | sesame seed | minimal countable unit in the analogy |
| uddhāra | removal / taking out | operation repeated at each interval |
| kṣaya | exhaustion | endpoint of the duration analogy |
| āyuḥ | lifespan | temporal duration of a birth-state |
| Arbuda | Arbuda | first cold naraka in this duration sequence |
| dviṃśati-guṇa | twentyfold | multiplier for later cold naraka lifespans |
| prativṛddhi | successive increase | ordered increase from one cold naraka to the next |

## 9. Doctrinal Determination

VAkK_3.82–3.83 gave hot naraka, animal, and preta time-measures. VAkK_3.84 now gives the cold naraka lifespan rule.

```text
Arbuda cold naraka
    → vāha of sesame seeds
    → one seed removed every 100 years
    → lifespan lasts until exhaustion

subsequent cold narakas
    → lifespan increases successively twentyfold
```

The Kośa uses a concrete counting analogy to express an otherwise ungraspable temporal magnitude.

## 10. Logical Determination

This verse introduces duration by exhaustion of a counted series.

```text
large finite collection
    → minimal repeated subtraction
    → vast duration until exhaustion
```

The duration is immense, but it is still finite and measurable. It is not infinite time; it is counted time stretched through an extreme operation.

## 11. Interpretive Note

This verse is powerful because it gives a pedagogical model of kalpa-like vastness without abandoning measure. The cold naraka duration is not left vague. It is made thinkable by a finite but nearly unimaginable counting procedure.

```text
one sesame seed
    every 100 years
        until the vāha is exhausted
```

This is still saṃsāric time. It is terrifyingly vast, but the key philosophical point remains: even this duration has measure, sequence, and exhaustion.

## 12. Organon Interpretation

Light contact point:

```text
Extreme duration is represented by a rule of counted depletion.
```

For this pass, we simply observe the Kośa’s method. It does not merely name a vast lifespan; it defines a procedure for imagining duration through repeated subtraction from a finite store.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_84
    a vak:Karika ;
    rdfs:label "VAK 3.84" ;
    vak:sourceReference "VAkK_3.84" ;
    vak:continues vak:VAK_3_83 ;
    vak:hasTopic vak:ColdNarakaLifespanMeasure ;
    vak:belongsTo vak:TimeMeasureBlock .

vak:ColdNarakaLifespanMeasure
    a logic:TemporalMeasure ;
    rdfs:label "lifespan measure of the cold narakas" ;
    vak:hasBaseCase vak:ArbudaLifespanMeasure ;
    vak:hasIncreasePattern vak:TwentyfoldSuccessiveIncrease .

vak:ArbudaLifespanMeasure
    a logic:TemporalMeasure ;
    rdfs:label "Arbuda lifespan measure" ;
    vak:modeledBy vak:SesameSeedDepletionAnalogy .

vak:SesameSeedDepletionAnalogy
    a logic:DurationAnalogy ;
    rdfs:label "one sesame seed removed every hundred years until a vāha is exhausted" ;
    vak:hasInterval "100 years" ;
    vak:hasRemovedUnit vak:SesameSeed ;
    vak:hasContainerMeasure vak:Vaha .

vak:TwentyfoldSuccessiveIncrease
    a logic:MeasurePattern ;
    rdfs:label "dviṃśati-guṇa-prativṛddhi" ;
    vak:hasCanonicalTranslation "successive twentyfold increase" .
```

## 14. Commit Note

Committed VAK_3.84 / VAkK_3.84.

Established:
- Arbuda cold naraka lifespan is modeled by exhausting a vāha of sesame seeds, removing one seed every hundred years.
- subsequent cold naraka lifespans increase successively twentyfold.
- extreme duration is represented by a finite depletion procedure.
- the verse continues the time-measure block and keeps vast duration within measurable saṃsāric time.
