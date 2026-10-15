# VAK_2.18 — What Possession Entails

## 1. Sanskrit (Devanāgarī)

> चतुर्भिः सुखकायाभ्यां पञ्चभिश्चक्षुरादिमान् ।
>
> सौमनस्यी च दुःखी तु सप्तभिः स्त्रीन्द्रियादिमान् ॥ २.१८ ॥

## 2. Sanskrit (IAST)

> caturbhiḥ sukhakāyābhyāṃ pañcabhiś cakṣurādimān /
>
> saumanasyī ca duḥkhī tu saptabhiḥ strīndriyādimān // 2.18 //

The last subject takes its count from the next opening, aṣṭābhiḥ. That completion is marked. The eleven and thirteen are not this verse.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| caturbhiḥ | instrumental | with four |
| sukha-kāyābhyām | instrumental dual | pleasure, and body, separately |
| pañcabhiḥ | instrumental | with five |
| cakṣur-ādi-mān | nominative | one possessing the eye and so forth |
| saumanasyī | nominative | one possessing gladness |
| duḥkhī tu | nominative | one possessing pain, however |
| saptabhiḥ | instrumental | with seven |
| strī-indriya-ādi-mān | nominative | one possessing the female faculty and so forth |

The dual distributes four over two cases. It does not make pleasure and body one set of four.

## 4. Grammar

```text
pleasure
    → triad + pleasure
    = 4
body
    → triad + body
    = 4

eye, ear, nose, tongue, each
    → triad + body + that faculty
    = 5

gladness
    → triad + pleasure + gladness
    = 5

pain
    → body, life, mind, four feelings
    = 7
    distress not included

female and so forth
    → eight, from the next opening
```

The predicate is necessarily possesses, carried from 2.17.

## 5. Translation

### Literal Translation

With four, in the cases of pleasure and body. One possessing the eye and so forth, with five, and one possessing gladness. One possessing pain, however, with seven. One possessing the female faculty and so forth.

### Bhāṣya-informed study translation

One possessing pleasure necessarily possesses four: the three beginning with neutral feeling, and pleasure. One possessing body, four: those three and body. One possessing the eye, five: neutral feeling, life, mind, body, and the eye. The same for ear, nose, and tongue.

One possessing gladness, five: neutral feeling, life, mind, pleasure, and gladness. With which pleasure is one born in the second dhyāna, who has not attained the third, endowed? With an afflicted pleasure belonging to the third dhyāna.

One possessing pain, seven: body, life, mind, and four feeling-faculties. Pain, pleasure, gladness, and neutral feeling. Not distress.

One possessing the female faculty, eight: those seven and the female faculty. And so forth gathers male, distress, and those beginning with faith. Each of male and distress is eight on that seven. One possessing a faculty beginning with faith possesses the five together with neutral feeling, life, and mind. A different eight.

## 6. Philosophical Translation

If this is possessed, what else must be. Pleasure and body each close on four, and not the same four. Eye and gladness each close on five, and not the same five. Pain closes on seven. Female, male, and distress close on that seven plus themselves. Faith and the rest close on the five plus the triad. Equal counts are not interchangeable sets.

The second-dhyāna case keeps birth, attainment, and possession apart. Afflicted third-level pleasure can be possessed without the third dhyāna attained, and without pleasure manifest.

Organon rendering:

Membership under possession. The consequence of one member is a determinate set. Not activation, and not the non-reflective look-ahead. Not the verse English.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| samanvāgata | possessing | not occurring now |
| cakṣur-ādi | eye and so forth | ear, nose, tongue; separate cases |
| strī-indriya-ādi | female and so forth | male, distress, the five; another range |
| dvitīya-dhyāna-ja | born in the second dhyāna | the test |
| tṛtīya-dhyāna-alābhin | not attained the third | possession without attainment |
| kliṣṭa | afflicted | the third-level pleasure in the answer |

## 8. Logical Determination

```text
triad
    = neutral feeling, life, mind

pleasure
    = triad + pleasure
body
    = triad + body

eye, ear, nose, tongue
    = triad + body + that one
    = 5

gladness
    = triad + pleasure + gladness
    = 5

pain
    = body, life, mind,
      pain, pleasure, gladness, neutral feeling
    = 7

female, male, distress
    = those seven + itself
    = 8

five beginning with faith
    = the five + triad
    = 8

possessed
    ↛ active now
same count
    ↛ same set
```

## 9. Interpretive Note

The closures are minimums. They do not say no other faculty can be possessed.

Eye requires body, and body requires the triad. Gladness requires pleasure, and pleasure requires the triad. Two ways to five.

The second-dhyāna answer is short. It does not explain the mechanism. Latent would add a theory the sentence does not give. The claim is the afflicted third-level pleasure, possessed, the dhyāna not attained.

Distress is the next eight, not part of the seven. The faith eight does not ride on the pain seven. Tu marks that.

Organon reading: the set, the initiating faculty, and the relation. A number alone loses the determination. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_18
    a vak:Karika ;
    rdfs:label "VAK 2.18" ;
    vak:hasTopic vak:PossessionClosure ;
    vak:belongsTo vak:Indriyanirdesa .

vak:PleasureFaculty vak:closesOn 4 .
vak:EyeFaculty vak:closesOn 5 .
vak:GladnessFaculty vak:closesOn 5 .
vak:PainFaculty vak:closesOn 7 .

organon:EqualCountNotEqualSet
    organon:notTheVerseEnglish true .
```
