# VAK_1.34 — Taking an Object, and Appropriated

## 1. Sanskrit (Devanāgarī)

> सप्त सालम्बनाश्चित्तधातवोऽर्धं च धर्मतः ।
>
> नवानुपात्तास्ते चाष्टौ शब्दश्चान्ये नव द्विधा ॥ १.३४ ॥

## 2. Sanskrit (IAST)

> sapta sālambanāś cittadhātavo 'rdhaṃ ca dharmataḥ /
>
> navānupāttās te cāṣṭau śabdaś cānye nava dvidhā // 1.34 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sapta | numeral | the seven citta-principles |
| sa-ālambana | adjective | taking an object |
| citta-dhātavaḥ | compound | the six cognition-principles and the mind-principle |
| ardham dharmataḥ | accusative plus ablative | a half, with respect to the dharma-principle |
| nava an-upātta | numeral plus adjective | nine unappropriated |
| te ca aṣṭau | pronoun plus numeral | those eight |
| śabdaḥ | nominative | sound |
| anye nava dvidhā | the other nine, in two ways | appropriated and unappropriated |

The half is the associated portion. The eight of the second count are the seven plus the whole dharma-principle. The scope changes.

## 4. Grammar

```text
sapta citta-dhātavaḥ sa-ālambanāḥ
    ardham ca dharmataḥ

nava an-upāttāḥ
    te ca aṣṭau śabdaḥ ca

anye nava dvidhā
```

Two cuts. The first is object. The second is appropriation.

## 5. Translation

### Literal Translation

Seven citta-principles take an object, and a half with respect to the dharma-principle. Nine are unappropriated: those eight, and sound. The other nine are twofold.

### Bhāṣya-informed study translation

How many take an object, how many do not? The seven citta-principles take an object: the eye, ear, nose, tongue, and body cognition-principles, the mind-cognition principle, and the mind-principle. They take an object because they grasp a condition. And a half of the dharma-principle: the portion whose nature is the mental factors. So the ten whose nature is form, and the unassociated portion of the dharma-principle, do not take an object.

How many are appropriated, how many unappropriated? Nine are unappropriated. Which nine? The seven just stated as taking an object, together with a half of the eighth, are recalled. Those eight, and sound: the seven citta-principles, the dharma-principle, and the sound-principle. The other nine are twofold, appropriated and unappropriated.

Of these, eye, ear, nose, tongue, and body, when present, are appropriated. Past and future, they are unappropriated. The visible, smell, taste, and tangible principles, when present and not separate from the organ, are appropriated. The others are unappropriated: hair, body-hair, nails, and teeth apart from the root; feces, urine, saliva, mucus, blood, and the like; earth, water, and the like.

What does appropriated mean? What citta and the mental factors have taken up as a basis, because they follow one another in benefit and injury. What the world calls animate.

## 6. Philosophical Translation

Taking an object is the seven, and the associated half of the dharma-principle. The ten whose nature is form do not take an object. Neither does the unassociated half.

Appropriation is a different cut. The nine that never are appropriated are the seven, the whole dharma-principle, and sound. The other nine are appropriated only when present and, for the four meanings, only when not separate from the organ. Appropriated is the basis citta has taken up. Benefit and injury run both ways. That is what is called animate.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| sālambana | taking an object | grasps a condition |
| citta-dhātu | citta-principle | the six cognitions and the mind-principle |
| ardham dharmataḥ | a half of the dharma-principle | the associated mental factors |
| anālambana | not taking an object | the ten of form, and the unassociated half |
| anupātta | unappropriated | nine, always |
| upātta | appropriated | present organ, or present meaning not separate from it |
| śabda | sound | among the nine always unappropriated |
| sacetana | animate | the world's name for appropriated |

## 8. Logical Determination

```text
take an object
    seven citta-principles
    associated half of the dharma-principle

do not take an object
    ten whose nature is form
    unassociated half of the dharma-principle

always unappropriated
    the seven
    the whole dharma-principle
    sound

twofold
    five organs: appropriated when present
    four meanings: appropriated when present and not separate from the organ
    otherwise unappropriated

appropriated
    taken up by citta and the mental factors as a basis
    benefit and injury follow both ways

1.35 not opened
```

## 9. Interpretive Note

The hinge is the change of scope. The first count uses a half. The second count uses the whole dharma-principle. Sound joins the nine. The definition of appropriated is the close.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_34 a vak:Karika ;
    vak:hasTopic vak:ObjectAndAppropriation ;
    vak:belongsTo vak:Dhatunirdesa .

vak:SevenCittaPrinciples vak:takesObject true .
vak:AssociatedDharmaHalf vak:takesObject true .
vak:NineAlwaysUnappropriated vak:includes
    vak:SevenCittaPrinciples, vak:DharmaPrinciple, vak:SoundPrinciple .
```
