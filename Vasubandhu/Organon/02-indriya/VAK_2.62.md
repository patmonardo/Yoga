# VAK_2.62 — Antecedent, Object, Predominant

## 1. Sanskrit (Devanāgarī)

> चित्तचैत्ता अचरमा उत्पन्नाः समनन्तरः /
> सर्वे धर्मा अालम्बनाः कारणाख्योऽधिपः स्मृतः // २.६२ //

## 2. Sanskrit (IAST)

> cittacaittā acaramā utpannāḥ samanantaraḥ /
>
> sarve dharmā ālambanāḥ kāraṇākhyo 'dhipaḥ smṛtaḥ // 2.62 //

## 3. Lexical Analysis

| Pada | Morphology | Force |
|---|---|---|
| cittacaittāḥ | m. pl. | Mind and mental factors. |
| acaramāḥ | adj. | Not final. |
| utpannāḥ | adj. | Arisen. |
| samanantaraḥ | m. sg. | Immediately antecedent. |
| sarve | adj. | All. |
| dharmāḥ | m. pl. | Dharmas. |
| ālambanāḥ | m. pl. | Object-conditions. |
| kāraṇākhyaḥ | adj. | Named conditioning. |
| adhipaḥ | m. sg. | Predominant. |
| smṛtaḥ | adj. | Held. |

## 4. Grammar

```text
% start S
S[CONDITION=antecedent] -> Arisen[TYPE=citta-caitta, FINAL=false]
S[CONDITION=object] -> AllDharmas[APPROPRIATE=true]
S[CONDITION=predominant] -> ConditioningCause
```

Antecedent is arisen citta-caitta, not final, whole complex of next.  
Not own-kind.  
Object is all dharmas as appropriate.  
Predominant is the conditioning cause.  
Future-knowledge is not settled.

## 5. Translation

### Literal Translation

Arisen mind and mental factors, not final, are the immediately antecedent. All dharmas are the object-condition. What is named the conditioning cause is held to be the predominant.

### Bhāṣya-informed study translation

> The immediately antecedent condition is arisen mind and mental factors other than the final, excluding an arhat's final mind and factors: the whole complex is the condition of the next whole complex. The object-condition is all dharmas, as appropriate: visible form for eye-cognition, all dharmas for mental cognition. What is named the conditioning cause is held to be the predominant condition.

## 6. Philosophical Translation

> Antecedent is arisen citta-caitta, not final, whole complex of next. Not own-kind. Object is all dharmas as appropriate. Predominant is the conditioning cause. Future-knowledge is not settled.

## 7. Technical Vocabulary

| Term | Rendering |
|---|---|
| samanantara | Immediately antecedent. Arisen citta-caitta, not final. |
| ālambana | Object. All dharmas as appropriate. |
| adhipati | Predominant. The conditioning cause. |

## 8. Logical Determination

Antecedent is the whole complex of the next. Not own-kind. Object is all dharmas as appropriate. Predominant is the conditioning cause.

## 9. Interpretive Note

Antecedent is arisen citta-caitta, not final, whole complex of next. Not own-kind. Object is all dharmas as appropriate. Predominant is the conditioning cause. Future-knowledge is not settled.

## 10. OWL++ Seed

```turtle
:AntecedentCondition :isArisenCittaCaitta true ; :isFinal false ; :isWholeComplexOfNext true ; :isOwnKind false .
:ObjectCondition :isAllDharmasAsAppropriate true .
:PredominantCondition :isConditioningCause true .
```
