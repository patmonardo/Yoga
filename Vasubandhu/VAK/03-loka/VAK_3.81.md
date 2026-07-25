# VAK_3.81 — Time-Measure: Arūpya Lifespans and the Mahākalpa

## 1. Sanskrit — Devanāgarī

```sanskrit
आरूप्ये विंशतिः कल्पसहस्राण्यधिकाधिकम् ।
महाकल्पः परीत्ताभात् प्रभृत्यधर्मधस्ततः ॥ VAkK_3.81 ॥
```

## 2. Sanskrit — IAST

```iast
ārūpye viṃśatiḥ kalpasahasrāṇy adhikādhikam /
mahākalpaḥ parīttābhāt prabhṛty adharmadhas tataḥ // VAkK_3.81 //
```

## 3. Source Caution

The source reading is:

```iast
ārūpye viṃśatiḥ kalpasahasrāṇya dhikādhikam /
mahākalpaḥ parīttābhāt prabhṛtyadharmadhastataḥ // VAkK_3.81 //
```

Sandhi has been lightly separated:

```iast
ārūpye viṃśatiḥ kalpa-sahasrāṇi adhika-adhikam /
mahā-kalpaḥ parīttābhāt prabhṛti adharaṃ adhaḥ tataḥ //
```

The second pāda is difficult in the transmitted text. `prabhṛty adharmadhas tataḥ` is provisionally understood as: “from Parīttābha onward, and below from there,” the measure is a mahākalpa. The exact interpretation of `adharmadhas` / `adharam adhaḥ` should be checked against the bhāṣya and printed editions.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| ārūpye | ārūpye | in the formless realm |
| viṃśatiḥ | viṃśatiḥ | twenty |
| kalpasahasrāṇi | kalpa-sahasrāṇi | thousands of kalpas |
| adhikādhikam | adhika-adhikam | increasingly, successively more |
| mahākalpaḥ | mahā-kalpaḥ | great kalpa |
| parīttābhāt | parīttābhāt | from Parīttābha |
| prabhṛti | prabhṛti | beginning from, onward from |
| adhas / adharaṃ | adhas / adharaṃ | below, lower; provisional |
| tataḥ | tataḥ | from there, thereafter |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| ārūpye | locative singular neuter | realm-location: in the formless realm |
| viṃśatiḥ | nominative singular feminine | number: twenty |
| kalpa-sahasrāṇi | nominative/accusative plural neuter | thousands of kalpas |
| adhika-adhikam | adverbial compound | successively increasing |
| mahā-kalpaḥ | nominative singular masculine | the great kalpa; measure-unit |
| parīttābhāt | ablative singular | from Parīttābha |
| prabhṛti | indeclinable | beginning from |
| adhas tataḥ | adverbial phrase | below from there; provisional |

## 6. Literal Translation

In the formless realm, there are twenty thousand kalpas, increasingly more. From Parīttābha onward, and below from there, the measure is a mahākalpa.

## 7. Philosophical Translation

The lifespan scale now reaches the formless realm: arūpya beings are measured in tens of thousands of kalpas, increasing successively by twenty thousand. Beginning from Parīttābha and below, the relevant large measure is the mahākalpa.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| ārūpya | formless realm | realm beyond rūpa-form; still a saṃsāric birth-field |
| kalpa | kalpa / aeon | cosmic time-unit |
| kalpa-sahasra | thousand kalpas | multiplied kalpa-duration |
| viṃśati | twenty | base increment for arūpya lifespan sequence |
| adhika-adhikam | increasingly more | successive increase from level to level |
| mahā-kalpa | great kalpa | large cosmic time-cycle; measure for lower relevant realms |
| Parīttābha | Parīttābha | rūpa-deva class marking a boundary point |
| prabhṛti | beginning from | sequence marker |
| adhas | below | lower range from the stated boundary; provisional |

## 9. Doctrinal Determination

VAkK_3.80 distinguished kāma-deva time from rūpa-deva time: kāma-devas retain day-and-night; rūpa-devas do not, and their lifespans are measured by kalpas. VAkK_3.81 extends the kalpa measure into the arūpya realm and introduces the mahākalpa boundary.

```text
kāma realm
    → day-and-night remains

rūpa realm
    → no day-and-night
    → kalpa-scale lifespan

arūpya realm
    → lifespan in thousands of kalpas
    → successively increasing by twenty-thousand kalpas

Parīttābha and below
    → mahākalpa measure
```

The text now establishes kalpa-time as the measure of high-world duration.

## 10. Logical Determination

This verse raises temporal measure from cyclic day to cosmic aeon.

```text
day-and-night time
    → divine day-and-night conversion
        → kalpa duration
            → thousands of kalpas
                → mahākalpa scale
```

The higher the realm, the less ordinary temporality applies. Yet the result is still measurable duration, not release from duration.

## 11. Interpretive Note

This is the point where kalpa becomes unavoidable for the Loka-nirdeśa. The Kośa is not using kalpa merely as a poetic “very long time.” It is a technical measure of world-duration and lifespan-duration.

```text
kalpa
    = cosmic duration-unit
    = measure of high-realm lifespan
    ≠ timelessness
```

That last distinction matters. Even arūpya lifespans, enormous as they are, remain within time. They are not liberation from time.

## 12. Organon Interpretation

Light contact point:

```text
Kalpa-time is still measured time.
```

For this pass, we keep close to the Kośa. The text is teaching that higher realms alter temporal form and extend temporal scale, but they do not abolish temporal determination. Even the formless realm is still counted.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_81
    a vak:Karika ;
    rdfs:label "VAK 3.81" ;
    vak:sourceReference "VAkK_3.81" ;
    vak:continues vak:VAK_3_80 ;
    vak:hasTopic vak:ArupyaLifespanMeasure ;
    vak:hasTopic vak:MahakalpaMeasure ;
    vak:belongsTo vak:TimeMeasureBlock .

vak:ArupyaLifespanMeasure
    a logic:TemporalMeasure ;
    rdfs:label "arūpya lifespan measure" ;
    vak:hasMeasureUnit vak:KalpaThousands ;
    vak:hasIncreasePattern vak:TwentyThousandKalpaIncrease .

vak:KalpaThousands
    a logic:CosmicTimeMeasure ;
    rdfs:label "kalpa-sahasrāṇi" ;
    vak:hasCanonicalTranslation "thousands of kalpas" .

vak:MahakalpaMeasure
    a logic:CosmicTimeMeasure ;
    rdfs:label "mahākalpa" ;
    vak:hasCanonicalTranslation "great kalpa" .

vak:TwentyThousandKalpaIncrease
    a logic:MeasurePattern ;
    rdfs:label "viṃśatiḥ kalpa-sahasrāṇi adhikādhikam" ;
    vak:hasCanonicalTranslation "successively increasing by twenty thousand kalpas" .
```

## 14. Commit Note

Committed VAK_3.81 / VAkK_3.81.

Established:
- arūpya lifespans are measured in thousands of kalpas.
- the arūpya sequence increases successively by twenty thousand kalpas.
- the mahākalpa is introduced as a major cosmic time-measure beginning from Parīttābha and below.
- kalpa-time is still measured time, not liberation from temporal determination.
