# VAK_2.62 — Antecedent, Object, Predominant

## 1. Sanskrit (Devanāgarī)

```sanskrit
चित्तचैत्ता अचरमा उत्पन्नाः समनन्तरः /
सर्वे धर्मा अालम्बनाः कारणाख्योऽधिपः स्मृतः // २.६२ //
```

## 2. Sanskrit (IAST)

```text
cittacaittā acaramā utpannāḥ samanantaraḥ /
sarve dharmā ālambanāḥ kāraṇākhyo 'dhipaḥ smṛtaḥ // 2.62 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| cittacaittāḥ | m. pl. | consciousness and mental factors. |
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

> Arisen consciousness and mental factors, other than the final, are
> immediately antecedent. All dharmas are object-conditions; what is named
> the conditioning cause is held to be predominant.
### Bhāṣya-informed study translation

> Arisen consciousness and mental factors, except the final ones, are the
> immediately antecedent condition. All dharmas are object-conditions.
> What is called the conditioning cause is held to be the predominant
> condition.
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

**Translation note.** The Bhāṣya excludes an arhat's final consciousness and
factors and treats the whole preceding complex as condition for the next
whole complex. Object range is “as appropriate”: visible Form for
eye-cognition and all dharmas for mental cognition. A question about knowing
a future after a future is raised but not settled.

Antecedent is arisen citta-caitta, not final, whole complex of next. Not own-kind. Object is all dharmas as appropriate. Predominant is the conditioning cause. Future-knowledge is not settled.

## 10. OWL++ Seed

```turtle
:AntecedentCondition :isArisenConsciousnessCaitta true ; :isFinal false ; :isWholeComplexOfNext true ; :isOwnKind false .
:ObjectCondition :isAllDharmasAsAppropriate true .
:PredominantCondition :isConditioningCause true .
```
