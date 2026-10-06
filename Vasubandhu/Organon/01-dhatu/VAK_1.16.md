# VAK_1.16 — Cognition, Mind Essence, and the Seven Principles

## 1. Sanskrit (Devanāgarī)

> विज्ञानं प्रतिविज्ञप्तिः मन आयतनं च तत् ।
>
> धातवः सप्त च मताः षड्विज्ञानान्यथो मनः ॥ १.१६ ॥

## 2. Sanskrit (IAST)

> vijñānaṃ prativijñaptiḥ mana āyatanaṃ ca tat /
>
> dhātavaḥ sapta ca matāḥ ṣaḍvijñānāny atho manaḥ // 1.16 //

## 3. Lexical Analysis

```text
vijñānaṃ prativijñaptiḥ       → vijñānam + prativijñaptiḥ
mana āyatanaṃ ca tat          → manaḥ + āyatanam + ca + tat
dhātavo matāḥ                  → dhātavaḥ + matāḥ
ṣaḍvijñānāny atho manaḥ       → ṣaṭ + vijñānāni + atho + manaḥ
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| vijñānam | nominative neuter singular | cognition |
| prativijñaptiḥ | nominative feminine singular | respective apprehension |
| manaḥ | nominative neuter singular | Mind |
| āyatanam | nominative neuter singular | Essence |
| tat | nominative neuter singular | that; refers to Cognition Base |
| dhātavaḥ | nominative masculine plural | Principles |
| sapta | numeral | seven |
| matāḥ | nominative masculine plural participle | accepted; taught |
| ṣaṭ | numeral | six |
| vijñānāni | nominative neuter plural | Cognitions |
| atho | connective | and also |

## 4. Grammar

```text
vijñānam = prativijñaptiḥ

tat = manaḥ āyatanam

dhātavaḥ sapta = ṣaṭ vijñānāni + manaḥ
```

The verse defines Cognition as respective apprehension. The Bhāṣya identifies
that same Cognition Base as Mind Essence and explains the seven Principles as
the six Cognition Principles together with Mind Principle.

## 5. Translation

### Literal Translation

Cognition is respective apprehension. That is also Mind Essence. Seven
Principles are accepted: the six Cognitions, and Mind.

### Bhāṣya-informed study translation

Cognition is apprehension with respect to each Condition. That same
Cognition Base is Mind Essence. Seven Principles are accepted: the six
Cognition Principles, from Eye-Cognition through Mind-Cognition, and Mind
Principle.

## 6. Systematic Placement

| Base | Essence | Principle |
|---|---|---|
| Cognition Base | Mind Essence | six Cognition Principles and Mind Principle |

The Bhāṣya closes the count at five Bases, twelve Essences, and eighteen
Principles.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| vijñāna | Cognition | respective apprehension |
| prativijñapti | respective apprehension | the Bhāṣya glosses this as *upalabdhi* |
| vijñānaskandha | Cognition Base | the Base considered as Mind Essence |
| mana-āyatana | Mind Essence | the Essence determination |
| manovijñāna-dhātu | Mind-Cognition Principle | one of the six |
| manodhātu | Mind Principle | the seventh; distinct from Mind-Cognition Principle |

## 8. Logical Determination

```text
Cognition Base
    → Mind Essence
    → six Cognition Principles + Mind Principle

five Bases
twelve Essences
eighteen Principles
```

## 9. Interpretive Note

The verse establishes the seven-Principle count. The relation between Mind
Principle and the six Cognition Principles is taken up in 1.17.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_16 a vak:Karika ;
    vak:hasTopic vak:PrincipleMindEssenceSeven ;
    vak:belongsTo vak:Dhatunirdesa .

vak:CognitionBase vak:also vak:MindEssence ;
    vak:projectedAs vak:SixCognitionPrinciples, vak:MindPrinciple .

vak:MindCognitionPrinciple vak:memberOf vak:SixCognitionPrinciples ;
    vak:distinctFrom vak:MindPrinciple ;
    vak:relationOpenedIn vak:VAK_1_17 .

vak:CountClose vak:bases 5 ;
    vak:essences 12 ;
    vak:principles 18 .
```
