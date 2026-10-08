# VAK_2.41 — Commonality and the Non-Reflecting Condition

## 1. Sanskrit (Devanāgarī)

> सभागता सत्त्वसाम्यमासंज्ञिकमसंज्ञिषु ।
>
> निरोधश्चित्तचैत्तानां विपाकः ते बृहत्फलाः ॥ २.४१ ॥

## 2. Sanskrit (IAST)

> sabhāgatā sattvasāmyam āsaṃjñikam asaṃjñiṣu /
>
> nirodhaś cittacaittānāṃ vipākaḥ te bṛhatphalāḥ // 2.41 //

## 3. Lexical Analysis

```text
sabhāgatā      → sabhāgatā
sattvasāmyam   → sattva-sāmyam
āsaṃjñikam     → āsaṃjñikam
asaṃjñiṣu      → a-saṃjñiṣu
nirodhaś       → nirodhaḥ
cittacaittānām → citta-caittānām
vipākaḥ        → vipākaḥ
te bṛhatphalāḥ → te bṛhat-phalāḥ
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| sabhāgatā | nominative feminine singular | class-commonality |
| sattva-sāmyam | nominative neuter singular | sameness among sentient beings |
| āsaṃjñikam | nominative neuter singular | Non-Reflecting condition |
| asaṃjñiṣu | locative masculine plural | among Non-Reflecting beings |
| nirodhaḥ | nominative masculine singular | cessation |
| citta-caittānām | genitive plural | of consciousness and associated mental factors |
| vipākaḥ | nominative masculine singular | maturation-result |
| te | nominative plural pronoun | those beings |
| bṛhat-phalāḥ | nominative masculine plural | Bṛhatphala beings |

## 4. Scientific English Rendering

> Class-commonality is sameness among sentient beings. The Non-Reflecting
> condition among Non-Reflecting beings is cessation of consciousness and
> associated mental factors; it is a maturation-result. Those beings are
> Bṛhatphala.

The Bhāṣya explains the Non-Reflecting condition as the maturation of the
Non-Reflecting attainment. During its interval, consciousness and associated
mental factors are prevented from arising; they arise at rebirth into that
state and again at departure from it.

## 5. Interpretation

The verse joins two unlike formations. *Sabhāgatā* is debated as the ground
of common classification among distinct sentient continua. The Vaibhāṣika
account treats it as a distinct real Dharma, both undivided among beings as
such and differentiated by Principle-range, ground, destiny, birth mode,
species, sex, discipline, and path-status. The critical response asks what
work the additional entity performs, why its logic should exclude non-
sentient kinds, and how its own differentiated instances are grouped.

*Āsaṃjñika* is different. It is a specified maturation-result in certain
Bṛhatphala beings: the future arising of consciousness and associated mental
factors is prevented for a long interval, like a dam holding back river
water. It is not the general absence of Reflection, nor a proof that all
mental determination has been eliminated.

The Kośa-wide synthesis remains: Vijñāna is Discriminative Cognition joining
and governing Perception and Conception. Their unity is Inconceivable as
homogeneous operation, with its Idea disclosed in the Cognition Base.
Vijñāna governs Mind and guides Dharma Base. Form Base and Dharma Base
classify the same *avijñapti* differently, with Vijñāna bearing a *prati*
relation to it. This local cessation is a conditioned result in the Impure
Wheel; it does not remove the governing relation or identify the Hub with
an empirical state of blankness.

## 6. Logical Determination

The competing commonality accounts:

```text
Vaibhasika:
    CommonClassification(S1, S2, class)
        requires RealCommonality(class)

Critical account:
    CommonClassification(S1, S2, class)
        is grounded in matching conditioned determinations;
        no additional commonality-entity is established
```

The Non-Reflecting condition:

```text
NonReflectingAttainment(S)
    → MaturationResult(S, NonReflectingCondition)
    → PreventsArising(S, ConsciousnessAndAssociatedFactors)
       for a long interval
```

The Bhāṣya retains boundary events:

```text
RebirthIntoCondition and DepartureFromCondition
    permit consciousness and associated mental factors
```

## 7. Interpretive Note

The Bhāṣya records four alternatives concerning whether commonality is
relinquished or acquired at death and rebirth. It uses entry into the
certainty of the noble Path and transition of destiny as distinct cases.
These examples belong to the debate over commonality and must not be merged
with the Non-Reflecting maturation account.

After a very long interval, Non-Reflecting beings depart with the arising of
Reflection and are reborn in the Desire Principle. The former attainment's
formative force is exhausted and no new force has been accumulated. The
source's simile compares this to arrows whose force is spent.

## 8. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_41
    a vak:Karika ;
    rdfs:label "VAK 2.41" ;
    vak:hasTopic vak:ClassCommonality,
        vak:NonReflectingCondition ;
    vak:belongsTo vak:Indriyanirdesa .

vak:VaibhasikaCommonality
    vak:asserts vak:CommonalityAsRealDharma .

vak:NonReflectingCondition
    vak:isMaturationResultOf vak:NonReflectingAttainment ;
    vak:preventsArisingOf vak:ConsciousnessAndAssociatedFactors ;
    vak:occursAmong vak:BrhatphalaBeings .
```
