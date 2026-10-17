# VAK_2.18 — What Possession Entails

## 1. Sanskrit (Devanāgarī)

> चतुर्भिः सुखकायाभ्यां पञ्चभिश्चक्षुरादिमान् ।
>
> सौमनस्यी च दुःखी तु सप्तभिः स्त्रीन्द्रियादिमान् ॥ २.१८ ॥

## 2. Sanskrit (IAST)

> caturbhiḥ sukhakāyābhyāṃ pañcabhiś cakṣurādimān /
>
> saumanasyī ca duḥkhī tu saptabhiḥ strīndriyādimān // 2.18 //

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
% start S
S[POSSESS=4] -> Pleasure | Body
S[POSSESS=5] -> Eye | Gladness
S[POSSESS=7] -> Pain
S[POSSESS=8] -> Female | FaithFive
```

The count is a feature determined by the possessed faculty.

## 5. Translation

### Literal Translation

With four, in the cases of pleasure and body. One possessing the eye and so forth, with five, and one possessing gladness. One possessing pain, however, with seven. One possessing the female faculty and so forth.

### Bhāṣya-informed study translation

> Possession is not uniform. Pleasure and body each require four. The eye and the rest, and gladness, require five. Pain requires seven. The female faculty and those gathered with it require eight. The five beginning with faith require a different eight. The necessary companions are fixed by the faculty possessed; there is no single rule for the remainder.

## 6. Philosophical Translation

> The necessary companions are fixed by the faculty possessed. There is no single rule for the remainder.

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
