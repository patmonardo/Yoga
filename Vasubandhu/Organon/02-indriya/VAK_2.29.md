# VAK_2.29 — How Many in the Unwholesome

## 1. Sanskrit (Devanāgarī)

> आवेणिके त्वकुशले दृष्टियुक्ते च विंशतिः ।
>
> क्लेशैश्चतुर्भिः क्रोधाद्यैः कौकृत्येनैकविंशतिः ॥ २.२९ ॥

## 2. Sanskrit (IAST)

> āveṇike tv akuśale dṛṣṭiyukte ca viṃśatiḥ /
>
> kleśaiś caturbhiḥ krodhādyaiḥ kaukṛtyenaikaviṃśatiḥ // 2.29 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| āveṇike | locative | in the isolated |
| akuśale | locative | in unwholesome consciousness |
| dṛṣṭi-yukte | locative | associated with a view |
| viṃśatiḥ | numeral | twenty |
| kleśaiḥ caturbhiḥ | instrumental | with one of four afflictions |
| krodha-ādyaiḥ | instrumental | with one secondary beginning with anger |
| kaukṛtyena | instrumental | with regret |
| ekaviṃśatiḥ | numeral | twenty-one |

The instrumentals distribute. Not one joint list.

## 4. Grammar

```text
% start S
S[ETHICAL=unwholesome, ISOLATED=true] -> Twenty
S[ETHICAL=unwholesome, VIEW=true] -> Twenty
S[ETHICAL=unwholesome, ADDED=?a] -> TwentyOne
Twenty -> Universal[10] Afflicted[6] Unwholesome[2] Vitarka Vicara
```

View specializes Discrimination; it does not add a member.  
One added associate (four afflictions, secondary, or regret) increments the count.

## 5. Translation

### Literal Translation

But in isolated unwholesome consciousness, and in that associated with a view, twenty. With the four afflictions, with those beginning with anger, or with regret, twenty-one.

### Bhāṣya-informed study translation

> In isolated unwholesome consciousness, and in that associated with a view, twenty. The view is a special form of prajñā, already counted among the universal factors. With one of the four afflictions, a secondary beginning with anger, or regret, twenty-one. Addition increments; specialization does not.

## 6. Philosophical Translation

> Isolated is ignorance alone. View specializes Discrimination. One added associate changes the count. Different name is not different factor.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| āveṇika | isolated | ignorance without another distinct affliction |
| dṛṣṭi-yukta | associated with a view | three named; unwholesome |
| prajñā-viśeṣa | a special form of Discrimination | why the count does not rise |
| rāga, pratigha, māna, vicikitsā | attachment, hostility, conceit, doubt | the four; one at a time |
| krodhādi | secondary beginning with anger | one adds one |
| kaukṛtya | regret | the unwholesome case here |

Not every view is unwholesome. The obscured-indeterminate views are the next unit.

## 8. Logical Determination

```python
from nltk.sem.logic import LogicParser
lp = LogicParser()

base = lp.parse(r'all c.(Unwholesome(c) & (Isolated(c) | View(c)) -> Count(c,20))')
added = lp.parse(r'all c.(AddedAssociate(c) -> Count(c,21))')
view = lp.parse(r'View(x) -> SpecializationOf(x,Prajna)')
```

Specialization leaves the count unchanged.  
Addition increments it.  
View is not a second factor.

## 9. Interpretive Note

Ignorance alone does not remove heedlessness, laziness, lack of faith, sluggishness, and agitation. Those are the afflicted ground. The restriction is another affliction such as attachment.

The three views are wrong view, attachment to views, and attachment to rules and observances. Unwholesome is essential. Prajñā here is not liberating knowledge. A count of its occurrence is not adequacy.

Or distributes the four. Not twenty-four. The singular secondary controls the anger-group. Plurals in the verse are alternatives.

Regret here is the unwholesome case of 2.28. Not all regret is unwholesome. Torpor is a later addition. These totals do not rule it out.

Organon reading: labels are not the count. Identity first. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_29
    a vak:Karika ;
    rdfs:label "VAK 2.29" ;
    vak:hasTopic vak:UnwholesomeCount ;
    vak:belongsTo vak:Indriyanirdesa .

vak:IsolatedUnwholesome vak:hasCount 20 .
vak:ViewAssociated vak:hasCount 20 .
vak:AddedAssociate vak:hasCount 21 .

organon:ViewNotAnAddedFactor
    organon:notTheVerseEnglish true .
```
