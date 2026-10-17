# VAK_1.45 — Named by the Support

## 1. Sanskrit (Devanāgarī)

```sanskrit
तद्विकारविकारित्वादाश्रयाश्चक्षुरादयः ।
अतोऽसाधारणत्वाद्धि विज्ञानं तैर्निरुच्यते ॥ १.४५ ॥
```

## 2. Sanskrit (IAST)

```text
tadvikāravikāritvād āśrayāś cakṣurādayaḥ /
ato 'sādhāraṇatvād dhi vijñānaṃ tair nirucyate // 1.45 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| tad-vikāra-vikāritvāt | ablative | because altered by their alteration |
| āśrayāḥ cakṣur-ādayaḥ | nominative | the eye and the rest are supports |
| ataḥ | adverb | therefore |
| asādhāraṇatvāt | ablative | because not in common |
| hi | particle | for |
| vijñānam taiḥ | nominative, instrumental | cognition by them |
| nirucyate | passive | is designated |

The first reason makes them supports. The second gives the name.

## 4. Grammar

```text
support
    cognition changes when the eye changes
    not when the visible changes

name
    eye-cognition, not form-cognition
    the eye is not a support of another cognition
    a visible is an object of more than one
```

## 5. Translation

### Literal Translation

> Because of being altered by their alteration, the eye and the rest are
> supports. Therefore, because they are not in common, cognition is
> designated by them.

### Bhāṣya-informed study translation

> The Eye and the other Faculties are supports because the Cognition
> Principles they support change when they change. Therefore, because those
> Faculties are not shared, Cognition is designated by them.

## 6. Philosophical Translation

Both are required. Only one is the support. The cut is the alteration. Benefit and impairment of the eye, acuity and dullness, are followed by the cognition. A change in the visible is not followed in that way. The dependence on the eye is the stronger one. That is why it is the support.

The name follows the support, not the object. Eye-cognition, not form-cognition. The eye is not in common. It cannot support another cognition. A visible can be the object of mind-cognition and of another eye-cognition. The drum names the sound. The barley names the sprout. The support names the cognition.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| vikāra | alteration | benefit, impairment, acuity, dullness |
| āśraya | support | the eye and the rest |
| asādhāraṇa | not in common | the eye supports only its own cognition |
| nirucyate | is designated | the name follows the support |
| bherī-śabda | drum-sound | the support names the product |
| yava-aṅkura | barley-sprout | the same |

## 8. Logical Determination

```text
both required
    eye and visible

support
    the one whose alteration the cognition follows

name
    from the support
    because the support is not in common

object
    in common
    mind-cognition and another eye-cognition

1.46 not opened
```

## 9. Interpretive Note

**Translation note.** The Bhāṣya says the cognitions alter with changes in their Faculties, while an alteration of visible Forms and the other conditions does not similarly change them. The Bhāṣya says Cognition depends on both a Faculty support and a visible Condition; that Condition may be shared by more than one Cognition, while the Faculty support is specific.

The hinge is the name. The object is shared. The support is not. Cognition is designated by the support that is not in common.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_45 a vak:Karika ;
    vak:hasTopic vak:NamedByTheSupport ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Eye vak:supports vak:EyeCognition .
vak:Visible vak:objectOf vak:EyeCognition, vak:MindCognition .
vak:Cognition vak:namedBy vak:Support .
```
