# VAK_1.48 — Two Cognitions, the Permanent, the Faculty

## 1. Sanskrit (Devanāgarī)

```sanskrit
पञ्च बाह्या द्विविज्ञेया नित्या धर्मा असंस्कृताः ।
धर्मार्धमिन्द्रियं ये च द्वादशाध्यात्मिकाः स्मृताः ॥ १.४८ ॥
```

## 2. Sanskrit (IAST)

```text
pañca bāhyā dvivijñeyā nityā dharmā asaṃskṛtāḥ /
dharmārdham indriyaṃ ye ca dvādaśādhyātmikāḥ smṛtāḥ // 1.48 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| pañca bāhyāḥ | nominative | five external |
| dvi-vijñeyāḥ | nominative | knowable by two cognitions |
| nityāḥ dharmāḥ asaṃskṛtāḥ | nominative | unconditioned dharmas are permanent |
| dharma-ardham | nominative | a portion of the dharma-Principle |
| indriyam | nominative | is faculty |
| ye ca dvādaśa adhyātmikāḥ | relative | and the twelve called internal |

The printed divijñeyāḥ is read as dvi-vijñeyāḥ. A portion is not a count of half.

## 4. Grammar

```text
known
    five external, by two
    the remaining thirteen, by mind-cognition alone

permanent
    no Principle entire
    the unconditioned portion of the dharma-Principle

faculty
    a portion of the dharma-Principle
    the twelve internal
    not the five external
    not the remaining portion
```

## 5. Translation

### Literal Translation

> The five external are knowable by two. Unconditioned dharmas are
> permanent. A portion of the dharma is faculty, and the twelve called
> internal.

### Bhāṣya-informed study translation

> The five external Principles are knowable by two. Unconditioned Dharmas are
> permanent. A portion of the Dharma Principle, and the twelve internal
> Principles, are Faculties.

## 6. Philosophical Translation

The five external are known twice. Once by their own cognition, once by mind-cognition. The remaining thirteen are not the object of the five. Mind-cognition alone knows them.

No Principle is permanent as a whole. The permanent is a portion of the dharma-Principle, the unconditioned dharmas. The rest are impermanent.

Faculty is the handoff. A portion of the dharma-Principle, and the twelve internal. The five beginning with the eye keep their names. The seven mind-Principles are the one mind-faculty. Female and male are a portion of the body. The five external, and the remaining portion of the dharma-Principle, are not faculty. Twenty-two are stated. The Ābhidharmikas set mind after life, because mind takes an object.

The chapter closes on that cut.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| bāhya | external | the five objects |
| dvi-vijñeya | knowable by two | own cognition and mind-cognition |
| nitya | permanent | a portion only |
| asaṃskṛta | unconditioned | the permanent portion |
| dharma-ardha | a portion of the dharma | not a count of half |
| adhyātmika | internal | the twelve |
| indriya | faculty | the twenty-two of the sūtra |
| sālambana | takes an object | why mind is recited after life |

## 8. Logical Determination

```text
known by two
    visible, sound, smell, taste, tangible

known by one
    the remaining thirteen

permanent
    unconditioned dharmas
    a portion of the dharma-Principle

faculty
    a portion of the dharma-Principle
    the twelve internal

not faculty
    the five external
    the remaining portion

chapter complete
    2.01 not opened
```

## 9. Interpretive Note

**Translation note.** The five are Visible Form, Sound, Smell, Taste, and Tangible, each knowable by its corresponding sensory Cognition and by Mind-Cognition. Only the unconditioned portion of the Dharma Principle is permanent. The faculties within its portion and the twelve internal Principles are further enumerated in the Bhāṣya.

The hinge is the close. Two cognitions for the five external. Permanence only as a portion. Faculty as a portion and the twelve internal. The Exposition of the Principles ends on that.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_48 a vak:Karika ;
    vak:hasTopic vak:TwoCognitionsThePermanentTheFaculty ;
    vak:belongsTo vak:Dhatunirdesa ;
    vak:closesChapter true .

vak:FiveExternal vak:knownBy vak:OwnCognition, vak:MindCognition .
vak:UnconditionedDharmas vak:permanent true .
vak:TwelveInternal vak:faculty true .
```
