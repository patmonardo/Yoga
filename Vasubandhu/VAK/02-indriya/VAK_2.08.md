# VAK_2.08 — Mental Pleasure, Mental Pain, and Neutral Feeling

## 1. Sanskrit — Devanāgarī

```text
अन्यत्र सा सौमनस्यं अशाता चैतसी पुनः ।
दौर्मनस्यमुपेक्षा तु मध्या उभयी अविकल्पनात् ॥ VAkK_2.8 ॥
```

## 2. Sanskrit — IAST

```text
anyatra sā saumanasyaṃ aśātā caitasī punaḥ /
daurmanasyam upekṣā tu madhyā ubhayī avikalpanāt // VAkK_2.8 //
```

Source form:

```text
anyatra sā saumanasyaṃ aśātā caitasī punaḥ /
daurmanasyamupekṣā tu madhyā ubhayī avikalpanāt // VAkK_2.8 //
```

## 3. Padaccheda

| Text | Padaccheda | Basic Sense |
|---|---|---|
| anyatra | anyatra | elsewhere / in other cases |
| sā | sā | that |
| saumanasyam | saumanasyam | gladness / mental pleasure |
| aśātā | aśātā | disagreeable / unpleasant |
| caitasī | caitasī | mental |
| punaḥ | punaḥ | again / in turn |
| daurmanasyam | daurmanasyam | distress / mental displeasure |
| upekṣā | upekṣā | neutral / equanimous feeling |
| tu | tu | but |
| madhyā | madhyā | middle / neutral |
| ubhayī | ubhayī | both / of both kinds |
| avikalpanāt | avikalpanāt | because of non-differentiation / absence of distinction |

## 4. Grammar

```text
anyatra sā saumanasyam
    “elsewhere, that is saumanasya”
    referring back to agreeable mental feeling outside the third dhyāna case

aśātā caitasī punaḥ daurmanasyam
    “again, disagreeable mental [feeling] is daurmanasya”

upekṣā tu madhyā
    “but upekṣā is the middle [feeling]”

ubhayī avikalpanāt
    “of both kinds because of non-differentiation”
```

## 5. Literal Translation

```text
Elsewhere, that [agreeable mental feeling] is gladness.
Again, disagreeable mental feeling is distress.
But neutral feeling is middle and of both kinds,
because there is no differentiation.
```

## 6. Philosophical Translation

```text
Outside the special case of the third dhyāna, pleasant mental feeling is the faculty
of gladness. Unpleasant mental feeling is the faculty of distress. Neutral feeling,
however, is the middle faculty and applies to both bodily and mental feeling because
there is no decisive differentiation of pleasant and unpleasant tone.
```

## 7. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| anyatra | elsewhere | Outside the third-dhyāna exception of VAK_2.07 |
| saumanasya | gladness / mental pleasure | Pleasant mental feeling outside the special sukha case |
| daurmanasya | distress / mental displeasure | Unpleasant mental feeling |
| upekṣā | neutral / equanimous feeling | Middle feeling-tone |
| madhyā | middle | Neither pleasant nor unpleasant |
| ubhayī | of both kinds | Bodily and mental |
| avikalpana | non-differentiation | Absence of decisive pleasant/unpleasant determination |
| caitasī vedanā | mental feeling | Feeling associated with mind |

## 8. Classification Note

VAK_2.07–2.08 together define all five feeling faculties.

```text
duḥkha
    = unpleasant bodily feeling

sukha
    = pleasant bodily feeling
      plus pleasant mental feeling in the third dhyāna

saumanasya
    = pleasant mental feeling elsewhere

daurmanasya
    = unpleasant mental feeling

upekṣā
    = neutral feeling, bodily and mental
```

This completes the analysis of the five *vedanā-indriyas*.

## 9. Vikalpa / Avikalpana Note

The verse uses **avikalpana**, not simple lack of thought in a casual sense.

```text
avikalpanāt
    =
because of non-differentiation
```

Here it means that neutral feeling is not sharply differentiated into pleasant or unpleasant. For that reason, *upekṣā* can apply to both bodily and mental feeling.

This must not be confused with the project rule concerning **vikalpa** as imaginative differentiation in other contexts. Here the prefix **a-** marks the absence of the decisive differentiation that would classify the feeling as pleasant or unpleasant.

## 10. Logical Determination

VAK_2.08 completes the affective classification by combining two axes:

```text
locus:
    bodily / mental

hedonic tone:
    pleasant / unpleasant / neutral
```

The full logical field becomes:

```text
unpleasant + bodily
    -> duḥkha

pleasant + bodily
    -> sukha

pleasant + mental + third dhyāna
    -> sukha

pleasant + mental + elsewhere
    -> saumanasya

unpleasant + mental
    -> daurmanasya

neutral + bodily or mental
    -> upekṣā
```

## 11. Transcendental Placement

The feeling faculties are governing powers of affective valuation.

```text
pleasant
unpleasant
neutral
```

These are not merely psychological decorations. They determine how experience becomes affectively available, appropriated, entangling, or neutralized.

The inclusion of *upekṣā* is especially important. Neutral feeling is still a faculty because non-differentiated affective tone also governs experience.

```text
upekṣā
    =
middle valuation-driver
```

## 12. Organon Interpretation

Organon reading:

```text
saumanasya-indriya
    =
pleasant mental valuation-driver

daurmanasya-indriya
    =
unpleasant mental valuation-driver

upekṣā-indriya
    =
neutral / middle valuation-driver
```

Together with VAK_2.07:

```text
bodily affect
mental affect
neutral affect
```

The affective field is now fully determined.

## 13. Compact Formula

```text
VAK_2.08 completes the five feeling faculties:
mental pleasure is saumanasya, mental pain is daurmanasya,
and neutral feeling is upekṣā, applying to both bodily and mental feeling because it is undifferentiated.
```

## 14. OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_08 a vak:Karika ;
    rdfs:label "VAK 2.08" ;
    vak:sourceVerse "VAkK_2.8" ;
    vak:chapter vak:Indriyanirdesa ;
    vak:hasTopic vak:SaumanasyaIndriya, vak:DaurmanasyaIndriya, vak:UpeksaIndriya ;
    vak:hasKeyTerm vak:Saumanasya, vak:Daurmanasya, vak:Upeksa, vak:Avikalpana ;
    vak:hasLiteralTranslation
        "Elsewhere, that agreeable mental feeling is gladness. Again, disagreeable mental feeling is distress. But neutral feeling is middle and of both kinds, because there is no differentiation." ;
    vak:hasPhilosophicalTranslation
        "Outside the special case of the third dhyāna, pleasant mental feeling is the faculty of gladness. Unpleasant mental feeling is the faculty of distress. Neutral feeling, however, is the middle faculty and applies to both bodily and mental feeling because there is no decisive differentiation of pleasant and unpleasant tone." .

vak:SaumanasyaIndriya a vak:Indriya ;
    rdfs:label "saumanasya-indriya" ;
    vak:canonicalTranslation "gladness faculty / mental pleasure faculty" ;
    vak:logicalFunction "Pleasant mental feeling outside the third-dhyāna sukha case." .

vak:DaurmanasyaIndriya a vak:Indriya ;
    rdfs:label "daurmanasya-indriya" ;
    vak:canonicalTranslation "distress faculty / mental displeasure faculty" ;
    vak:logicalFunction "Unpleasant mental feeling." .

vak:UpeksaIndriya a vak:Indriya ;
    rdfs:label "upekṣā-indriya" ;
    vak:canonicalTranslation "neutral feeling faculty / equanimity faculty" ;
    vak:logicalFunction "Middle feeling-tone applying to both bodily and mental feeling." .

vak:Avikalpana a logic:Determination ;
    rdfs:label "avikalpana" ;
    vak:canonicalTranslation "non-differentiation" .
```

## 15. Commit History

```text
VAK_2.08 opened.
Chapter: Indriyanirdeśa.
Method: kārikā-first.
Mental pleasure outside third dhyāna identified as saumanasya.
Unpleasant mental feeling identified as daurmanasya.
Neutral feeling identified as upekṣā, middle and applicable to both bodily and mental loci.
Technical guardrail added: avikalpana = non-differentiation in affective classification.
Organon note added: feeling faculties as valuation-drivers.
Zero-padded file naming maintained: VAK_2.08.
```
