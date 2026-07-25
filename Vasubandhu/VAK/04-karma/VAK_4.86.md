# VAK_4.86

## 1. Sanskrit — Devanāgarī

लोभजं कायवाक्कर्म मिथ्याजीवः पृथक्कृतः ।  
दुःशोधत्वात् परिष्कारलोभोत्थं चेन्न सूत्रतः ॥ ४.८६ ॥

Local source:

```text
lobhajaṃ kāyavākkarma mithyājīvaḥ pṛthak kṛtaḥ /
duḥśodhatvāt pariṣkāralobhotthaṃ cet na sūtrataḥ // VAkK_4.86 //
```

## 2. Sanskrit — IAST

**lobhajaṃ kāya-vāk-karma mithyājīvaḥ pṛthak kṛtaḥ |**  
**duḥśodhatvāt pariṣkāra-lobhotthaṃ cen na sūtrataḥ || 4.86 ||**

The verse turns to the definition and separate classification of wrong livelihood.

## 3. Padaccheda

```text
lobha-jam
kāya-vāk-karma
mithyā-ājīvaḥ
pṛthak
kṛtaḥ
duḥ-śodhatvāt
pariṣkāra-lobha-uttham
cet
na
sūtrataḥ
```

Expanded sense:

> Bodily or verbal karma arising from greed is wrong livelihood. It is classified separately because it is difficult to purify. If one says that wrong livelihood is only what arises from greed for requisites, no—this is not so according to the sūtra.

## 4. Grammar

- **lobhajam**: neuter nominative singular agreeing with *karma*; “born from greed.”
- **kāya-vāk-karma**: bodily or verbal karma.
- **mithyā-ājīvaḥ**: wrong livelihood; an improper means of sustaining life.
- **pṛthak kṛtaḥ**: treated separately, classified distinctly.
- **duḥśodhatvāt**: because it is difficult to purify.
- **pariṣkāra-lobhottham**: arisen from greed for requisites or material supports.
- **cet**: if it is said.
- **na**: not so.
- **sūtrataḥ**: according to the sūtra; on scriptural authority.

## 5. Literal Translation

> Bodily or verbal karma born of greed is wrong livelihood. It is treated separately because it is difficult to purify. If it is said that it is only what arises from greed for requisites, no—according to the sūtra.

## 6. Philosophical Translation

> Wrong livelihood is not a unique bodily or verbal medium. It is bodily or verbal activity reorganized under greed as the governing principle of sustenance. It receives separate treatment because this mode of activity is especially difficult to purify. Yet the category must not be restricted without warrant to greed for one specific class of material requisites; its extension is fixed by the sūtra.

The determining relation is:

```text
same expressive medium:
    body or speech

different governing ground:
    greed operating through livelihood
```

## 7. Technical Vocabulary

### ājīva

```text
ājīva
    livelihood
    means by which life is sustained
```

### mithyājīva

```text
mithyājīva
    wrong livelihood
```

It is bodily or verbal karma whose relation to livelihood is governed by greed.

### lobhaja

```text
lobhaja
    born from greed
```

### pariṣkāra

```text
pariṣkāra
    requisite
    equipment
    material support
```

### duḥśodhatva

```text
duḥśodhatva
    difficulty of purification
```

For the kārikā pass, the safe determination is simply that wrong livelihood is separately classified because it is difficult to purify.

## 8. Doctrinal Determination

Wrong livelihood belongs to bodily and verbal karma. It is not an additional expressive medium or an eleventh karmic course.

Its form is:

```text
bodily karma
or verbal karma

qualified by:
    arising from greed
    and functioning as livelihood
```

Its separate classification does not imply a separate substance. It marks a practically significant subtype with a distinctive correction profile.

The proposed restriction is:

```text
wrong livelihood
    =
activity arising specifically from greed for requisites
```

The verse rejects this as too narrow on scriptural grounds.

## 9. Logical Determination

Let:

```text
A = activity
M = expressive medium
R = governing root
F = practical function
```

Then:

```text
M ∈ {Body, Speech}
R = Greed
F = Livelihood
```

Formally:

```text
BodilyOrVerbal(A)
and ArisesFrom(A, Greed)
and FunctionsAs(A, Livelihood)
    →
WrongLivelihood(A)
```

A subtype may require separate treatment without becoming a new substrate:

```text
SubclassOf(WrongLivelihood, BodilyOrVerbalKarma)
and DifficultToPurify(WrongLivelihood)
    →
SeparateDoctrinalTreatment(WrongLivelihood)
```

The verse rejects the equivalence:

```text
WrongLivelihood(A)
    ↔
ArisesFromGreedForRequisites(A)
```

The latter may be one instance, but it does not exhaust the class.

## 10. Light Organon Interpretation

At the Kernel level, classification cannot rely solely on surface operation. The same bodily or verbal act may belong to a different doctrinal class according to its governing ground and practical function.

```text
ActivityClassification {
    medium
    root
    function
    doctrinalClass
}
```

For wrong livelihood:

```text
medium:
    body or speech

root:
    greed

function:
    livelihood

class:
    wrong livelihood
```

A subtype may be separately indexed because it has a distinctive correction profile rather than a distinct substrate.

## 11. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_86
    a vak:Karika ;
    rdfs:label "VAkK 4.86" ;
    vak:continues vak:VAK_4_85 ;
    vak:hasTopic vak:WrongLivelihood .

vak:WrongLivelihood
    rdfs:label "mithyājīva" ;
    rdfs:subClassOf vak:BodilyOrVerbalKarma ;
    vak:arisesFrom vak:Greed ;
    vak:hasPracticalFunction vak:Livelihood ;
    vak:hasCorrectionProfile vak:DifficultToPurify ;
    vak:receivesSeparateClassification true .

vak:GreedForRequisites
    rdfs:subClassOf vak:Greed ;
    rdfs:label "pariṣkāra-lobha" .
```

Rule seed:

```text
BodilyOrVerbalKarma(?activity)
and ArisesFrom(?activity, Greed)
and FunctionsAs(?activity, Livelihood)
    →
WrongLivelihood(?activity)
```

Constraint:

```text
WrongLivelihood(?activity)
    does not imply
ArisesOnlyFromGreedForRequisites(?activity)
```

## 12. Commit Note

```text
VAK_4.86 — Define and separately classify wrong livelihood

- define wrong livelihood as bodily or verbal karma born of greed
- preserve it as a subtype of bodily and verbal activity
- explain its separate treatment through difficulty of purification
- distinguish separate classification from a separate expressive medium
- reject the proposed restriction to greed for requisites
- defer the exact scriptural extension to the Bhāṣya pass
- keep the Organon interpretation at the Kernel classification level
```

### First-pass determination

```text
wrong livelihood
    =
bodily or verbal karma
born of greed
and functioning as livelihood
```

```text
it is separately classified
because it is difficult to purify
```

```text
it is not restricted
without qualification
to greed for material requisites
```
