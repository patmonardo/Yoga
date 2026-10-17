# VAK_2.65 — Elements and Derived Form

## 1. Sanskrit (Devanāgarī)

> भूतानि भूतहेतूनि पञ्चधा रूपहेतवः /
> रूपं रूपस्य त्रिधा भूतानामेकधैव तत् // २.६५ //

## 2. Sanskrit (IAST)

> bhūtāni bhūtahetūni pañcadhā rūpahetavaḥ /
>
> rūpaṃ rūpasya tridhā bhūtānām ekadhaiva tat // 2.65 //

## 3. Lexical Analysis

| Pada | Morphology | Force |
|---|---|---|
| bhūtāni | n. pl. | Elements. |
| bhūtahetūni | adj. | Cause of elements. |
| pañcadhā | adv. | In five ways. |
| rūpahetavaḥ | m. pl. | Causes of derived form. |
| rūpam | n. sg. | Derived form. |
| rūpasya | gen. sg. | Of derived form. |
| tridhā | adv. | In three ways. |
| bhūtānām | gen. pl. | Of the elements. |
| ekadhā | adv. | In one way. |
| eva | pcl. | Only. |
| tat | n. sg. | That. |

## 4. Grammar

```text
% start S
S[CAUSE=elements-of-elements] -> Two[HOMOGENEOUS=true, COARISEN=true]
S[CAUSE=elements-of-derived] -> Five[FUNCTIONS=conditioning]
S[CAUSE=derived-of-derived] -> Three
S[CAUSE=derived-of-elements] -> One[MATURATION=true]
```

Elements cause elements in two ways, derived form in five functions of the conditioning cause.  
Derived form of derived form in three, of elements in one, maturation.  
Conditioning cause is not always counted.

## 5. Translation

### Literal Translation

The elements are cause of those in two ways, and of derived form in five. Derived form, of one another, in three. Of the elements, that, in one way only.

### Bhāṣya-informed study translation

> Elements cause elements in two ways, derived form in five functions of the conditioning cause. Derived form of derived form in three, of elements in one, maturation. Conditioning cause is not always counted.

## 6. Philosophical Translation

> Elements cause elements in two ways, derived form in five functions of the conditioning cause. Derived form of derived form in three, of elements in one, maturation. Conditioning cause is not always counted.

## 7. Technical Vocabulary

| Term | Rendering |
|---|---|
| bhūta | Element. |
| rūpa | Derived form. |
| kāraṇa-hetu | Conditioning cause. Five functions. |
| janana | Generation. |
| niśraya | Dependent support. |
| pratiṣṭhā | Foundation. |
| upastambha | Sustaining. |
| vṛddhi | Increase. |

## 8. Logical Determination

Elements cause elements in two ways. Derived form in five functions. Conditioning cause is not always counted.

## 9. Interpretive Note

Elements cause elements in two ways, derived form in five functions of the conditioning cause. Derived form of derived form in three, of elements in one, maturation. Conditioning cause is not always counted.

## 10. OWL++ Seed

```turtle
:Elements :causeElements :TwoWays .
:Elements :causeDerivedForm :FiveFunctions .
:DerivedForm :causeDerivedForm :ThreeWays .
:DerivedForm :causeElements :OneWay .
:ConditioningCause :notAlwaysCounted true .
```
