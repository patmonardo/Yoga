# VAK_1.34 — Taking an Object, and Appropriated

## 1. Sanskrit (Devanāgarī)

```sanskrit
सप्त सालम्बनाश्चित्तधातवोऽर्धं च धर्मतः ।
नवानुपात्तास्ते चाष्टौ शब्दश्चान्ये नव द्विधा ॥ १.३४ ॥
```

## 2. Sanskrit (IAST)

```text
sapta sālambanāś cittadhātavo 'rdhaṃ ca dharmataḥ /
navānupāttās te cāṣṭau śabdaś cānye nava dvidhā // 1.34 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sapta | numeral | the seven consciousness Principles |
| sa-ālambana | adjective | taking an object |
| citta-dhātavaḥ | compound | the six Cognition Principles and the mind-Principle |
| ardham dharmataḥ | accusative plus ablative | a half, with respect to the dharma-Principle |
| nava an-upātta | numeral plus adjective | nine unappropriated |
| te ca aṣṭau | pronoun plus numeral | those eight |
| śabdaḥ | nominative | sound |
| anye nava dvidhā | the other nine, in two ways | appropriated and unappropriated |

The half is the associated portion. The eight of the second count are the seven plus the whole dharma-Principle. The scope changes.

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

> Seven consciousness Principles take an object, and a half with respect to the
> dharma-Principle. Nine are unappropriated: those eight, and sound. The
> other nine are twofold.

### Bhāṣya-informed study translation

> Seven consciousness Principles and the mental-factor portion of the Dharma
> Principle take an object. Nine are unappropriated: those eight and sound.
> The other nine are twofold.

## 6. Philosophical Translation

Taking an object is the seven, and the associated half of the dharma-Principle. The ten whose nature is form do not take an object. Neither does the unassociated half.

Appropriation is a different cut. The nine that never are appropriated are the seven, the whole dharma-Principle, and sound. The other nine are appropriated only when present and, for the four meanings, only when not separate from the organ. Appropriated is the basis citta has taken up. Benefit and injury run both ways. That is what is called animate.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| sālambana | taking an object | grasps a condition |
| citta-dhātu | consciousness Principle | the six cognitions and the mind-Principle |
| ardham dharmataḥ | a half of the dharma-Principle | the associated mental factors |
| anālambana | not taking an object | the ten of form, and the unassociated half |
| anupātta | unappropriated | nine, always |
| upātta | appropriated | present organ, or present meaning not separate from it |
| śabda | sound | among the nine always unappropriated |
| sacetana | animate | the world's name for appropriated |

## 8. Logical Determination

```text
take an object
    seven consciousness Principles
    associated half of the dharma-Principle

do not take an object
    ten whose nature is form
    unassociated half of the dharma-Principle

always unappropriated
    the seven
    the whole dharma-Principle
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

**Translation note.** The seven consciousness Principles are the five sensory Cognitions, the Mind-Cognition Principle, and the Mind Principle; the relevant half of the Dharma Principle is its mental-factor portion. The nine unappropriated are those seven, the Dharma Principle, and sound. “Appropriated” means taken up by consciousness and mental factors as a basis through mutual benefit or injury—the animate, as the world calls it.

The hinge is the change of scope. The first count uses a half. The second count uses the whole dharma-Principle. Sound joins the nine. The definition of appropriated is the close.

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
