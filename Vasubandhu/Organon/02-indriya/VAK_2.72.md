# VAK_2.72 — Fourfold Indeterminate

## 1. Sanskrit (Devanāgarī)

> विपाकजैर्यापथिकशिल्पस्थानिकनैर्मितम् /
> चतुर्धाऽव्याकृतं कामे रूपे शिल्पविवर्जितम् // २.७२ //

## 2. Sanskrit (IAST)

> vipākajairyāpathikaśailpasthānikanairmitam /
>
> caturdhāvyākṛtaṃ kāme rūpe śilpavivarjitam // 2.72 //

## 3. Lexical Analysis

| Pada | Morphology | Force |
|---|---|---|
| vipākajaiḥ | inst. pl. | By maturation-born. |
| īryāpathika | adj. | Deportment. |
| śailpasthānika | adj. | Craft. |
| nairmitam | adj. | Creation. |
| caturdhā | adv. | Fourfold. |
| avyākṛtam | adj. | Indeterminate. |
| kāme | loc. sg. | In the desire realm. |
| rūpe | loc. sg. | In the form realm. |
| śilpa | n. sg. | Craft. |
| vivarjitam | adj. | Excluded. |

## 4. Grammar

```text
% start S
S[INDETERMINATE=four] -> Desire[MATURATION=true, DEPORTMENT=true, CRAFT=true, CREATION=true]
S[INDETERMINATE=three] -> Form[CRAFT=false]
```

Having divided carries over.  
Avyākṛta is unobscured-indeterminate. Not the obscured.  
Creation is supernormal, not ordinary construction.

## 5. Translation

### Literal Translation

Indeterminate in the desire realm, fourfold: maturation-born, deportment, craft, and creation. In the form realm, excluding craft.

### Bhāṣya-informed study translation

> Having divided carries over. Avyākṛta is unobscured-indeterminate. Not the obscured. Creation is supernormal, not ordinary construction.

## 6. Philosophical Translation

> Having divided carries over. Avyākṛta is unobscured-indeterminate. Not the obscured. Creation is supernormal, not ordinary construction.

## 7. Technical Vocabulary

| Term | Rendering |
|---|---|
| avyākṛta | Indeterminate. Unobscured-indeterminate. |
| vipākaja | Maturation-born. |
| īryāpathika | Deportment. |
| śailpasthānika | Craft. |
| nairmita | Creation. Supernormal. |

## 8. Logical Determination

Having divided carries over. Avyākṛta is unobscured-indeterminate. Creation is supernormal.

## 9. Interpretive Note

Having divided carries over. Avyākṛta is unobscured-indeterminate. Not the obscured. Creation is supernormal, not ordinary construction.

## 10. OWL++ Seed

```turtle
:DesireIndeterminate :kinds 4 .
:FormIndeterminate :kinds 3 ; :hasCraft false .
:Avyakrta :isUnobscuredIndeterminate true .
:Creation :isSupernormal true .
```
