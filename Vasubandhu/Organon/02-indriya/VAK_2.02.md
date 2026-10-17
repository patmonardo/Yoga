# VAK_2.02 — Own Meaning, and the Body-Portion

## 1. Sanskrit (Devanāgarī)

```sanskrit
स्वार्थोपलब्ध्याधिपत्यात् सर्वस्य च षडिन्द्रियम् ।
स्त्रीत्वपुंस्त्वाधिपत्यात्तु कायात् स्त्रीपुरुषेन्द्रिये ॥ २.२ ॥
```

## 2. Sanskrit (IAST)

```text
svārthopalabdhyādhipatyāt sarvasya ca ṣaḍindriyam /
strītvapuṃstvādhipatyāt tu kāyāt strīpuruṣendriye // 2.2 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sva-artha-upalabdhi-ādhipatyāt | ablative of cause | because of governing efficacy in apprehending one's own meaning |
| sarvasya | genitive | of everything |
| ca | conjunction | and; mind's range |
| ṣaḍ-indriyam | nominative | the six are faculty |
| strītva-puṃstva-ādhipatyāt | ablative of cause | because of governing female-being and male-being |
| tu | particle | but |
| kāyāt | ablative | from the body |
| strī-puruṣa-indriye | nominative dual | the female and male faculties |

## 4. Grammar

```text
% start S
S[TYPE=faculty] -> NP[MODE=?m] VP[GOVERN=apprehension]
NP[MODE=own-meaning] -> 'the five'
NP[MODE=all] -> 'mind'
NP[MODE=sex] -> 'female' | 'male'
VP[GOVERN=apprehension] -> 'govern apprehension'
S[TYPE=faculty] -> NP[MODE=sex] VP[FROM=body]
```

`MODE` distinguishes own-meaning, all, and the sex-faculties. `FROM=body` unifies female/male with the body-faculty.

## 5. Translation

### Literal Translation

> Because of governing efficacy in the apprehension of their own meaning,
> and of all, the six are faculty. But because of governing efficacy over
> female-being and male-being, the female and male faculties are from the
> body.

### Bhāṣya-informed study translation

> The five are Faculties by governing apprehension of their own meanings;
> mind is so by apprehending all. The female and male Faculties are from the
> body through governing female-being and male-being.

## 6. Philosophical Translation

> Faculty here is governing apprehension. Female and male are the body-faculty under a further name.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| sva-artha | own meaning | not object; not a domain |
| upalabdhi | apprehension | not a rank below cognition |
| ādhipatya | governing efficacy | superior power, adhikaṃ prabhutvam |
| sarvasya | of all | mind's range; not all at once |
| ṣaḍindriya | the six faculties | five and mind |
| kāyāt | from the body-faculty | a portion; not another entity |
| strītva | female-being | form, voice, movement, intention |
| puṃstva | male-being | form, voice, movement, intention |
| saṃkleśa / vyavadāna | defilement / purification | the Kośa Path; not this verse's predicate |

## 8. Logical Determination

```text
remote
    cognition, then recognition, then avoidance
    ↛ the predicate of the eye and ear

seeing
    = visual cognition
    ≠ a second operation beside it

faculty
    ↔ governs apprehension
    ∧ superior power
    ∧ common cause across the field
    ∧ apprehension conforms to the faculty

meaning
    → condition of the apprehension
    ↛ faculty

five
    → own meaning
mind
    → all meanings

female, male
    ⊂ body-faculty
    ≠ another substance
```

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): The six are faculty by governing apprehension—five of
their own meaning, mind of all. The female and male faculties are not
further substances; they are the body-faculty named apart because they
govern female-being and male-being.

2.01 distributed four matters, two, defilement, and purification. This verse is the revision of the first distribution. The unnamed others keep cognition as the place of governing efficacy, and refuse a second operation called seeing. The reply is svārthopalabdhi.

Superior power is the cut against the meaning. The eye is common across visible form, and apprehension follows the eye's condition. Visible form is a condition. It does not govern. The same up to mind and dharmas. Mind's all and mind's dharmas are both kept. They are not synonyms.

Female and male receive a name inside the body-faculty. The portion is local. The governed configuration is wider: form, voice, movement, intention. That is the transmitted account. It is not a modern theory of sex.

Interpretation: Applied Indriya Theory, with the extension inside the body-faculty. Defilement and purification are the Kośa Path. The faculties that govern them are its controllers. Not the verse English. Not this verse's predicate.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_02
    a vak:Karika ;
    rdfs:label "VAK 2.02" ;
    vak:hasTopic vak:OwnMeaningAndBodyPortion ;
    vak:belongsTo vak:Indriyanirdesa .

vak:SensoryFive vak:governs vak:ApprehensionOfOwnMeaning .
vak:MindFaculty vak:governs vak:ApprehensionOfAll .
vak:Meaning vak:notA vak:Indriya .
vak:FemaleFaculty vak:partOf vak:BodyFaculty .
vak:MaleFaculty vak:partOf vak:BodyFaculty .

organon:KosaPath
    organon:namedBy vak:Defilement, vak:Purification ;
    organon:controlledBy vak:FeelingFive, vak:EightBeginningWithFaith ;
    organon:notThePredicateOf vak:VAK_2_02 .
```
