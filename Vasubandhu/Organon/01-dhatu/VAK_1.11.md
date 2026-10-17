# VAK_1.11 — The Continuity Called Avijñapti

## 1. Sanskrit (Devanāgarī)

```sanskrit
विक्षिप्ताचित्तकस्यापि योऽनुबन्धः शुभाशुभः ।
महाभूतान्युपादाय स ह्यविज्ञप्तिरुच्यते ॥ १.११ ॥
```

## 2. Sanskrit (IAST)

```text
vikṣiptācittakasyāpi yo 'nubandhaḥ śubhāśubhaḥ /
mahābhūtāny upādāya sa hy avijñaptir ucyate // 1.11 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| vikṣipta-acittakasya | genitive singular | of one otherwise directed, or without consciousness |
| api | particle | even; the scope is wider |
| yaḥ ... saḥ | relative and correlative | which continuity is so called |
| anubandhaḥ | nominative masculine | the continuity |
| śubha-aśubhaḥ | nominative masculine | wholesome or unwholesome |
| mahābhūtāni | accusative plural | the Great Elements |
| upādāya | absolutive | depending on |
| hi | particle | indeed; the naming |
| avijñaptiḥ | nominative feminine | the name |
| ucyate | passive | is called |

The compound is compressed. The commentary separates *vikṣiptacittakasya*
and *acittakasya*. *Api* also brings in one whose consciousness is present
and not otherwise directed.

## 4. Grammar

```text
yaḥ anubandhaḥ
    śubha-aśubhaḥ
    vikṣipta-acittakasya api
    mahābhūtāni upādāya
        → saḥ avijñaptiḥ ucyate
```

A relative definition. *Śubhāśubhaḥ* agrees with *anubandhaḥ*. The name
*avijñaptiḥ* is feminine. The gender difference belongs to the naming.

## 5. Translation

### Literal Translation

> The wholesome or unwholesome continuity which, depending on the great
> Great Elements, belongs even to one whose consciousness is otherwise
> directed or absent: that indeed is called *avijñapti*.

### Bhāṣya-informed study translation

> The wholesome or unwholesome continuity that persists even when
> consciousness is directed elsewhere or absent depends on the Great
> Elements and is called *avijñapti*.

## 6. Philosophical Translation

Again, a definition. Named at 1.09. Counted around at 1.10. Defined here.
The word stays Sanskrit.

The continuity is the subject. Wholesome or unwholesome is its character.
*Api* keeps the minded case. The conspicuous cases are not the whole class:
otherwise directed, without consciousness, and also present and undistracted.
The commentary reads the first as a different consciousness, and the second
as the attainment of non-perception or the attainment of cessation. Continuity
is a stream.

Ethical continuity alone would also fit acquisition. *Mahābhūtāny upādāya*
is the differentiator. The Vaibhāṣikas take *upādāya* as cause, because the
Great Elements produce and the rest. That reading is marked. It is not the verse's
only word.

The name is the contrast. Form and action, and yet it does not inform another
as *vijñapti* does. The summary adds two origins, *vijñapti* or absorption.
The verse does not. Outward action is not the whole.

Which Great Elements are meant is the next question. Not this verse.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| avijñapti | *avijñapti* | the name stays |
| anubandha | continuity | glossed as stream |
| pravāha | stream | the commentary's word |
| śubha / aśubha | wholesome / unwholesome | *kuśala* / *akuśala* |
| citta | consciousness | otherwise directed, absent, or present |
| vikṣipta | otherwise directed | a different consciousness |
| acittaka | without consciousness | two attainments |
| api | even | includes the undistracted |
| mahābhūta | Great Element | the differentiator; defined next |
| upādāya | depending on | causal reading is Vaibhāṣika |
| prāpti-vāha | stream of acquisition | the similar, distinguished |
| vijñapti | *vijñapti* | informs another; the contrast |
| samādhi | absorption | one origin, in the summary |

## 8. Logical Determination

```text
named at 1.09
counted around at 1.10
defined here

wholesome or unwholesome stream
    could also be acquisition

stream depending on the Great Elements
    → avijñapti

api
    otherwise directed
    without consciousness
    also present and undistracted

Form and action
    and does not inform another

summary, not the verse
    from vijñapti or from absorption

1.12 not opened
```

## 9. Interpretive Note

**Translation note.** The Bhāṣya explains that *api* also includes a person whose consciousness is present and not otherwise directed; it specifies non-perception and cessation attainments as examples of absence of consciousness. It further glosses *avijñapti* as Form and action that does not inform another as *vijñapti* does.

The hinge is *upādāya*, then *api*. Interpretation of the name is in the
Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_11 a vak:Karika ;
    vak:hasTopic vak:Avijnapti ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Avijnapti vak:is vak:WholesomeOrUnwholesomeStream ;
    vak:dependsOn vak:GreatElements ;
    vak:distinctFrom vak:AcquisitionStream ;
    vak:informsAnother false ;
    vak:continuesWhenConsciousnessOtherwiseDirected true ;
    vak:continuesWithoutConsciousness true ;
    vak:continuesUndistracted true .

vak:UpadayaCausalReading vak:attributedTo vak:Vaibhasika .
```
