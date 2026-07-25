# VAK_3.91 — Kalpa Machinery: Intermediate Kalpas of Decline and Increase

## 1. Sanskrit — Devanāgarī

```sanskrit
अन्तःकल्पोऽमिताद्यावद्दशवर्षायुषस्ततः ।
उत्कर्षा अपकर्षाश्च कल्पा अष्टादशापरे ॥ VAkK_3.91 ॥
```

## 2. Sanskrit — IAST

```iast
antaḥkalpo 'mitād yāvad daśavarṣāyuṣas tataḥ /
utkarṣā apakarṣāś ca kalpā aṣṭādaśāpare // VAkK_3.91 //
```

## 3. Source Caution

The source reading is:

```iast
antaḥ kalpo 'mitāt yavaddaśavarṣāyuṣaḥ tataḥ /
utkarṣā apakarṣāśca kalpā aṣṭā daśāpare // VAkK_3.91 //
```

Sandhi and compounds have been lightly normalized:

```iast
antaḥ-kalpaḥ amitāt yāvat daśa-varṣa-āyuṣaḥ tataḥ /
utkarṣāḥ apakarṣāḥ ca kalpāḥ aṣṭādaśa apare //
```

The verse defines an `antaḥ-kalpa`, an intermediate kalpa, by the decline of human lifespan from immeasurable to ten years. It then states that the remaining eighteen intermediate kalpas consist of increases and decreases. This verse should be read with VAkK_3.92, which supplies the special first increase and the total twenty-kalpa standing period of the opened world.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| antaḥkalpaḥ | antaḥ-kalpaḥ | intermediate kalpa |
| amitāt | amitāt | from immeasurable |
| yāvat | yāvat | up to, until |
| daśavarṣāyuṣaḥ | daśa-varṣa-āyuṣaḥ | having ten-year lifespan |
| tataḥ | tataḥ | thereafter, from that point |
| utkarṣāḥ | utkarṣāḥ | increases, upward movements |
| apakarṣāḥ | apakarṣāḥ | decreases, downward movements |
| ca | ca | and |
| kalpāḥ | kalpāḥ | kalpas |
| aṣṭādaśa | aṣṭādaśa | eighteen |
| apare | apare | the others, the remaining ones |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| antaḥ-kalpaḥ | nominative singular masculine | subject: the intermediate kalpa |
| amitāt | ablative singular | starting point: from immeasurable lifespan |
| yāvat daśa-varṣa-āyuṣaḥ | limit phrase | until beings have lifespan of ten years |
| tataḥ | adverb | thereafter |
| utkarṣāḥ apakarṣāḥ ca | nominative plural masculine | increases and decreases |
| kalpāḥ aṣṭādaśa apare | nominative plural phrase | the other eighteen kalpas |

## 6. Literal Translation

An intermediate kalpa is from immeasurable [lifespan] up to those whose lifespan is ten years. Thereafter, the other eighteen kalpas are increases and decreases.

## 7. Philosophical Translation

The text now gives the internal turning of the kalpa-wheel. One intermediate kalpa is the decline of human lifespan from immeasurable down to ten years. After that, the remaining eighteen intermediate kalpas are alternating movements of increase and decrease.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| antaḥ-kalpa | intermediate kalpa | internal cycle within the larger kalpa machinery |
| amita | immeasurable | initial upper lifespan condition |
| daśa-varṣa-āyuṣ | ten-year lifespan | terminal low point of decline |
| utkarṣa | increase / ascent | upward phase of lifespan expansion |
| apakarṣa | decrease / decline | downward phase of lifespan contraction |
| aṣṭādaśa | eighteen | the remaining intermediate kalpas after the first decline |
| apara | other / remaining | subsequent members of the sequence |

## 9. Doctrinal Determination

VAkK_3.90 defined the large process-pair:

```text
saṃvarta-kalpa
    → contraction / dissolution

vivarta-kalpa
    → expansion / formation
```

VAkK_3.91 now gives the internal time-wheel of the opened world:

```text
first intermediate kalpa
    → lifespan declines
    → from immeasurable
    → to ten years

remaining eighteen intermediate kalpas
    → utkarṣa / increase
    → apakarṣa / decrease
```

This is precisely the turning-wheel language: the world-age is articulated by rhythmic increase and decrease of lifespan.

## 10. Logical Determination

This verse defines kalpa internally by reversible motion.

```text
antaḥ-kalpa
    → decline from immeasurable to ten
    → then cycles of increase and decrease
```

The kalpa is not merely an interval. It is a structured oscillation.

## 11. Interpretive Note

The technical pair is important:

```text
utkarṣa
    = upward drawing / increase / ascent

apakarṣa
    = downward drawing / decrease / decline
```

These are not moral metaphors only. They are formal terms for the rise and fall of lifespan within the world-age.

This is the language of a wheel turning:

```text
increase
    → peak
        → decline
            → nadir
                → increase again
```

The wheel is measured by lifespan. Human life-duration becomes the indicator of the cosmic phase.

## 12. Organon Interpretation

Light contact point:

```text
The kalpa-wheel turns through measured increase and decrease.
```

For this pass, we stay close to the Kośa. The lingo is exact: `antaḥ-kalpa`, `utkarṣa`, and `apakarṣa`. The wheel is not vague recurrence; it is a technical sequence of lifespan-contraction and lifespan-expansion.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_91
    a vak:Karika ;
    rdfs:label "VAK 3.91" ;
    vak:sourceReference "VAkK_3.91" ;
    vak:continues vak:VAK_3_90 ;
    vak:hasTopic vak:AntahKalpa ;
    vak:hasTopic vak:KalpaIncreaseDecrease ;
    vak:belongsTo vak:KalpaMachineryBlock .

vak:AntahKalpa
    a logic:CosmicProcessInterval ;
    rdfs:label "antaḥ-kalpa" ;
    vak:hasCanonicalTranslation "intermediate kalpa" ;
    vak:hasInitialLimit vak:ImmeasurableLifespan ;
    vak:hasTerminalLimit vak:TenYearLifespan .

vak:KalpaIncreaseDecrease
    a logic:CyclePattern ;
    rdfs:label "utkarṣa and apakarṣa" ;
    vak:hasUpwardPhase vak:Utkarsa ;
    vak:hasDownwardPhase vak:Apakarsa .

vak:Utkarsa
    a logic:CyclePhase ;
    rdfs:label "utkarṣa" ;
    vak:hasCanonicalTranslation "increase / ascent" .

vak:Apakarsa
    a logic:CyclePhase ;
    rdfs:label "apakarṣa" ;
    vak:hasCanonicalTranslation "decrease / decline" .
```

## 14. Commit Note

Committed VAK_3.91 / VAkK_3.91.

Established:
- an intermediate kalpa runs from immeasurable lifespan down to ten-year lifespan.
- the remaining eighteen intermediate kalpas are phases of increase and decrease.
- the precise lingo is `antaḥ-kalpa`, `utkarṣa`, and `apakarṣa`.
- the kalpa-wheel turns through measured increase and decrease of lifespan.
