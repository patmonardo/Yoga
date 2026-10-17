# VAK_2.65 — Elements and Derived Form

## 1. Sanskrit (Devanāgarī)

```sanskrit
भूतानि भूतहेतूनि पञ्चधा रूपहेतवः /
रूपं रूपस्य त्रिधा भूतानामेकधैव तत् // २.६५ //
```

## 2. Sanskrit (IAST)

```text
bhūtāni bhūtahetūni pañcadhā rūpahetavaḥ /
rūpaṃ rūpasya tridhā bhūtānām ekadhaiva tat // 2.65 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| bhūtāni | neuter nominative plural | Elements. |
| bhūtahetūni | neuter nominative plural compound adjective | causes of Elements. |
| pañcadhā | adverbial numeral | in five ways. |
| rūpahetavaḥ | masculine nominative plural compound | causes of derived Form. |
| rūpam | neuter nominative singular | derived Form. |
| rūpasya | neuter genitive singular | of derived Form. |
| tridhā | adverbial numeral | in three ways. |
| bhūtānām | neuter genitive plural | of the Elements. |
| ekadhā | adverbial numeral | in one way. |
| eva | emphatic particle | only. |
| tat | neuter nominative singular pronoun | that. |

## 4. Grammar

```text
% start S
S[CAUSE=Elements-of-Elements] -> Two[HOMOGENEOUS=true, COARISEN=true]
S[CAUSE=Elements-of-derived] -> Five[FUNCTIONS=conditioning]
S[CAUSE=derived-of-derived] -> Three
S[CAUSE=derived-of-Elements] -> One[MATURATION=true]
```

Elements cause Elements in two ways, and derived Form in five functions of the conditioning cause.  
Derived Form causes derived Form in three ways; it causes Elements in one way, by maturation.  
The conditioning cause is not always counted.

## 5. Translation

### Literal Translation

> The Elements are cause-condition for the Elements in two ways, and for
> derived Form in five. Form is cause-condition for Form in three ways; of
> the Elements, that is in one way only.
### Bhāṣya-informed study translation

> Elements are cause-condition for Elements in two ways and for derived
> Form in five. Form is cause-condition for Form in three ways; of the
> Elements, in one way only.
## 6. Philosophical Translation

> Elements cause Elements in two ways, and derived Form in five functions
> of the conditioning cause. Derived Form causes derived Form in three
> ways, and Elements in one, through maturation. The conditioning cause
> is not always counted.

## 7. Technical Vocabulary

| Term | Rendering |
|---|---|
| bhūta | Element. |
| rūpa | Form; here, derived Form. |
| kāraṇa-hetu | Conditioning cause. Five functions. |
| janana | Generation. |
| niśraya | Dependent support. |
| pratiṣṭhā | Foundation. |
| upastambha | Sustaining. |
| vṛddhi | Increase. |

## 8. Logical Determination

Elements cause Elements in two ways and derived Form in five functions. Derived Form causes derived Form in three ways and Elements in one. The conditioning cause is not always counted.

## 9. Interpretive Note

**Translation note.** The Bhāṣya identifies the two Element-to-Element
relations as homogeneous and co-arisen. Five Element-to-Form functions are
generation, dependent support, foundation, sustaining, and increase; these
are the conditioning cause divided fivefold. Form causes Form through
co-arising, homogeneity, and maturation. Form causes Elements as bodily and
verbal action whose maturation is the Elements. Conditioning cause is not
always counted.

Elements cause Elements in two ways, derived Form in five functions of the conditioning cause. Derived Form causes derived Form in three ways, and Elements in one through maturation. The conditioning cause is not always counted.

## 10. OWL++ Seed

```turtle
:Elements :causeElements :TwoWays .
:Elements :causeDerivedForm :FiveFunctions .
:DerivedForm :causeDerivedForm :ThreeWays .
:DerivedForm :causeElements :OneWay .
:ConditioningCause :notAlwaysCounted true .
```
