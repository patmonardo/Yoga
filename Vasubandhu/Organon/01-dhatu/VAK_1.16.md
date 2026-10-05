# VAK_1.16 — Principle, Mind-Essence, and the Seven

## 1. Sanskrit (Devanāgarī)

> विज्ञानं प्रतिविज्ञप्तिः मन आयतनं च तत् ।
>
> धातवः सप्त च मताः षड्विज्ञानान्यथो मनः ॥ १.१६ ॥॥

## 2. Sanskrit (IAST)

> vijñānaṃ prativijñaptiḥ mana āyatanaṃ ca tat /
>
> dhātavaḥ sapta ca matāḥ ṣaḍvijñānāny atho manaḥ // 1.16 //

## 3. Lexical Analysis

```text
vijñānam            → principle
prativijñaptiḥ      → respective apprehension
mana āyatanam      → the mind-essence
tat                → that same principle
dhātavaḥ sapta      → seven principles
ṣaḍ vijñānāni     → the six principles
atho manaḥ         → and mind
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| vijñānam | nominative neuter | the principle defined |
| prativijñaptiḥ | nominative feminine | the predicate |
| manaḥ | nominative | mind, in the essence; and the seventh |
| āyatanam | nominative | essence |
| tat | nominative | that same base |
| dhātavaḥ | nominative plural | principles |
| sapta matāḥ | numeral and participle | seven are accepted |
| ṣaṭ vijñānāni | numeral and plural | the six |
| atho | connective | and also |

*Prati* is respective. The commentary opens it: apprehension with respect
to each condition, glossed *upalabdhi*. Gender differs. The referent does
not.

## 4. Grammar

```text
vijñānam = prativijñaptiḥ

tat = manaḥ āyatanam

dhātavaḥ sapta = ṣaṭ vijñānāni + manaḥ
```

*Tat* resumes the principle-base. One content under the essence-arrangement.
Not a mind beside the principle. The seven are the six, and mind. The
mind-group principle is one of the six. The mind-principle is the seventh.
Their relation is the next verse.

## 5. Translation

### Literal Translation

Principle is respective apprehension. That is also the mind-essence. Seven
principles are accepted: the six principles, and mind.

### Bhāṣya-informed study translation

Principle is apprehension with respect to each condition. The principle-base
is six groups, from the eye-principle through the mind-group principle. That
same base is the mind-essence. As principles, seven are accepted: those six,
and the mind-principle.

The commentary then closes the count. Five bases, twelve essences, eighteen
principles. The form-base, apart from *avijñapti*, is the ten essences and the
ten principles. Feeling, reflection, and formations, together with *avijñapti*
and the unconditioned, are the dharma-essence and the dharma-principle.

## 6. Philosophical Translation

Again, two lines. The first defines the principle and places it as an essence.
The second counts seven.

Principle is respective apprehension. The commentary opens the respect: each
condition, glossed as *upalabdhi*. That same principle is the mind-essence.
Not a second thing.

Seven are accepted. Six run from the eye-principle through the mind-group
principle. The seventh is the mind-principle. The sixth and the seventh are
not one name counted twice.

The commentary closes the count on this verse. Five bases. Twelve essences.
Eighteen principles. The form-base, apart from *avijñapti*, is the ten. The
three beginning with feeling, with *avijñapti* and the unconditioned, are the
dharma-essence and the dharma-principle. The principle-base is the
mind-essence, and the seven.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| vijñāna | principle | not consciousness |
| prativijñapti | respective apprehension | *upalabdhi*, each condition |
| vijñāna-skandha | principle-base | defined here |
| mana-āyatana | mind-essence | the same base |
| manovijñāna-dhātu | mind-group principle | one of the six |
| manodhātu | mind-principle | the seventh |
| cakṣurvijñāna | eye-principle | first of the six |
| rūpa-skandha | form-base | organs, meanings, and *avijñapti* |
| avijñapti | *avijñapti* | form; not among the ten |
| saṃjñā | reflection | not this verse's predicate |
| viṣaya | condition | the commentary's each |
| upalabdhi | apprehension | gloss, not the verse-word |

## 8. Logical Determination

```text
form-base
    apart from avijñapti → ten essences, ten principles
    avijñapti remains form

1.15
    feeling, reflection, formations
    with avijñapti and the unconditioned
    → dharma-essence and dharma-principle

1.16
    principle = respective apprehension
    that = mind-essence
    seven = six + mind-principle
    sixth of the six ≠ the seventh

close
    five bases
    twelve essences     10 + 1 + 1
    eighteen principles 10 + 1 + 7

1.17 not opened
```

## 9. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_16 a vak:Karika ;
    vak:hasTopic vak:PrincipleMindEssenceSeven ;
    vak:belongsTo vak:Dhatunirdesa .

vak:PrincipleBase vak:definedAs vak:RespectiveApprehension ;
    vak:also vak:MindEssence .
vak:MindGroupPrinciple vak:memberOf vak:SixPrinciples .
vak:MindPrinciple vak:distinctFrom vak:MindGroupPrinciple .
vak:Avijnapti vak:remainsIn vak:FormBase ;
    vak:notAmong vak:Ten .
```
