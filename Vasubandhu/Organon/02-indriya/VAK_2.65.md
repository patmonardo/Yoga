# VAK_2.65 — Elements and Derived Form

## 1. Sanskrit (Devanāgarī)

```sanskrit
द्विधा भूतानि तद्धेतुः भौतिकस्य तु पञ्चधा /
त्रिधा भौतिकमन्योन्यं भूतानामेकधैव तत् // २.६५ //
```

## 2. Sanskrit (IAST)

```text
dvidhā bhūtāni taddhetuḥ bhautikasya tu pañcadhā /
tridhā bhautikam anyonyaṃ bhūtānām ekadhaiva tat // 2.65 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| dvidhā | numeral adverb | In two ways. |
| bhūtāni | n. nom. pl. | The great elements. |
| taddhetuḥ | m. nom. sg. compound | Their cause; the elements as cause of elements. |
| bhautikasya | n. gen. sg. | Of derived material form. |
| tu | particle | But; turns to another causal relation. |
| pañcadhā | numeral adverb | In five ways. |
| tridhā | numeral adverb | In three ways. |
| bhautikam | n. nom. sg. | Derived material form. |
| anyonyaṃ | reciprocal adverb | Mutually, one another. |
| bhūtānām | n. gen. pl. | Of the great elements. |
| ekadhā | numeral adverb | In one way. |
| eva | particle | Only. |
| tat | n. nom. sg. | That derived material form. |

The [running witness](../../Sources/kosabhasya.txt) and older VAK
study read *dvidhā bhūtāni taddhetuḥ* and *tridhā bhautikam
anyonyaṃ*. The former Organon verse replaced both phrases and lost
the reciprocal qualification. The normalized tokens open
*ekadhaiva* to *ekadhā eva*.

```text
# tokens: dvidhā bhūtāni taddhetuḥ bhautikasya tu pañcadhā tridhā bhautikam anyonyaṃ bhūtānām ekadhā eva tat
```

## 4. Grammar

The verse presents four class-level causal profiles: elements for
elements in two ways, elements for derived form in five, derived form
for derived form mutually in three, and derived form for elements in
one way only. The Bhāṣya identifies the ways and qualifies their
actual application. The `SEM` records profiles rather than asserting
that every pair of material instances stands in every relation.

```nltk-fcfg
% start S
# tokens: dvidhā bhūtāni taddhetuḥ bhautikasya tu pañcadhā tridhā bhautikam anyonyaṃ bhūtānām ekadhā eva tat
S[SEM=<(?ee & ?ef & ?ff & ?fe)>] -> EE[SEM=?ee] EF[SEM=?ef] FF[SEM=?ff] FE[SEM=?fe]
EE[SEM=<CauseProfile(element_kind,element_kind,two_ways)>] -> TWO[COUNT=2] ELEMENTS[CASE=nom,NUM=pl] THEIR_CAUSE[CASE=nom,NUM=sg]
TWO[COUNT=2] -> 'dvidhā'
ELEMENTS[CASE=nom,NUM=pl] -> 'bhūtāni'
THEIR_CAUSE[CASE=nom,NUM=sg] -> 'taddhetuḥ'
EF[SEM=<CauseProfile(element_kind,derived_form_kind,five_ways)>] -> OF_DERIVED[CASE=gen,NUM=sg] BUT FIVE[COUNT=5]
OF_DERIVED[CASE=gen,NUM=sg] -> 'bhautikasya'
BUT -> 'tu'
FIVE[COUNT=5] -> 'pañcadhā'
FF[SEM=<MutualCauseProfile(derived_form_kind,three_ways)>] -> THREE[COUNT=3] DERIVED[CASE=nom,NUM=sg] MUTUAL
THREE[COUNT=3] -> 'tridhā'
DERIVED[CASE=nom,NUM=sg] -> 'bhautikam'
MUTUAL -> 'anyonyaṃ'
FE[SEM=<CauseProfile(derived_form_kind,element_kind,one_way)>] -> OF_ELEMENTS[CASE=gen,NUM=pl] ONE[COUNT=1] ONLY THAT[CASE=nom,NUM=sg]
OF_ELEMENTS[CASE=gen,NUM=pl] -> 'bhūtānām'
ONE[COUNT=1] -> 'ekadhā'
ONLY -> 'eva'
THAT[CASE=nom,NUM=sg] -> 'tat'
```

```nltk-dep
'bhūtāni' -> 'dvidhā' | 'taddhetuḥ'
'bhautikasya' -> 'tu' | 'pañcadhā'
'bhautikam' -> 'tridhā' | 'anyonyaṃ'
'tat' -> 'bhūtānām' | 'ekadhā' | 'eva'
```

**Feature chart checkpoints.** Element-to-element spans [0, 3),
element-to-derived [3, 6), derived-to-derived [6, 9), and
derived-to-element [9, 13); the root spans [0, 13). The four
numeral features and the genitives constrain the pairings. Mutuality
is explicit only in the third profile.

## 5. Translation

### Literal Translation

> The elements are causes of elements in two ways, but of derived form
> in five. Derived form is cause of derived form mutually in three ways;
> of the elements it is cause in just one way.

### Bhāṣya-informed study translation

> Elements cause other elements in two ways and derived form in five.
> Derived forms cause one another in three ways; derived form causes
> elements in one way only.

## 6. Philosophical Translation

> The verse specifies a four-part causal matrix across elements and
> derived material form. The Bhāṣya identifies the two ways as
> homogeneous and co-arisen causes, the five as functions of the
> conditioning cause, the three mutual ways as co-arisen,
> homogeneous, and maturation causes, and the one return to the
> elements as maturation.

## 7. Technical Vocabulary

| Term | Rendering |
|---|---|
| bhūta | Great element. |
| bhautika | Derived material form. |
| taddhetuḥ | Their cause; keeps the first profile element-to-element. |
| anyonyaṃ | Mutually; qualifies the derived-form-to-derived-form profile. |
| pañcadhā | Fivefold: generation, dependent support, foundation, sustaining, increase. |
| ekadhā eva | In one way only: maturation in the Bhāṣya. |

## 8. Logical Determination

**Kārikā, derived.** The root `SEM` records four class-level
profiles. The identities of their modes and the caution that the
conditioning cause is not always counted come from the Bhāṣya.

```nltk-sem
element_element : CauseProfile(element_kind,element_kind,two_ways)
element_derived : CauseProfile(element_kind,derived_form_kind,five_ways)
derived_derived : MutualCauseProfile(derived_form_kind,three_ways)
derived_element : CauseProfile(derived_form_kind,element_kind,one_way)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(CauseProfile(element_kind,element_kind,two_ways) & CauseProfile(element_kind,derived_form_kind,five_ways) & MutualCauseProfile(derived_form_kind,three_ways) & CauseProfile(derived_form_kind,element_kind,one_way))

# THEORY prose_two_and_five
# EXPECT prose_two_and_five T
Includes(two_ways,homogeneous) & Includes(two_ways,coarisen) & Includes(five_ways,generation) & Includes(five_ways,support) & Includes(five_ways,foundation) & Includes(five_ways,sustaining) & Includes(five_ways,increase)

# THEORY prose_three_and_one
# EXPECT prose_three_and_one T
Includes(three_ways,coarisen) & Includes(three_ways,homogeneous) & Includes(three_ways,maturation) & Includes(one_way,maturation)

# THEORY prose_not_always
# EXPECT prose_not_always T
Includes(five_ways,generation) & -AlwaysCounted(conditioning_cause)

# THEORY rejected_return_has_coarisen
# EXPECT rejected_return_has_coarisen F
Includes(one_way,maturation) & Includes(one_way,coarisen)

# THEORY rejected_five_lacks_generation
# EXPECT rejected_five_lacks_generation F
Includes(five_ways,support) & -Includes(five_ways,generation)
```

```nltk-valuation
element_kind => elem
derived_form_kind => form
two_ways => two
five_ways => five
three_ways => three
one_way => one
homogeneous => homo
coarisen => co
generation => gen
support => sup
foundation => found
sustaining => sust
increase => incr
maturation => mat
conditioning_cause => cond
CauseProfile => {(elem,elem,two),(elem,form,five),(form,elem,one)}
MutualCauseProfile => {(form,three)}
Includes => {(two,homo),(two,co),(five,gen),(five,sup),(five,found),(five,sust),(five,incr),(three,co),(three,homo),(three,mat),(one,mat)}
AlwaysCounted => {}
```

The finite valuation witnesses all four verse profiles. Removing any
one profile makes the verse formula false. The Bhāṣya's fivefold
conditioning-cause functions and the single maturation relation back
to elements remain separate from the verse's bare counts.

## 9. Interpretive Note

**Translation note.** The two element-to-element causes are
homogeneous and co-arisen. The five element-to-derived-form functions
are generation, dependent support, foundation, sustaining, and
increase, described as a fivefold division of the conditioning cause.
Derived form may cause derived form through co-arising, homogeneity,
and maturation; the prose narrows the co-arisen case to bodily and
verbal action that accompanies mind. Derived form causes elements
through maturation when elements are the maturation of bodily or
verbal action. The conditioning cause is not counted in every context.

The verse gives four profiles, while the Bhāṣya determines their
modes and scope. The next verse turns to the classes of mind.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_65 a vak:Karika ; vak:hasTopic vak:ElementsAndDerivedForm .
vak:Elements vak:causeElements vak:TwoWays ; vak:causeDerivedForm vak:FiveFunctions .
vak:DerivedForm vak:mutuallyCausesDerivedForm vak:ThreeWays ; vak:causeElements vak:OneWay .
```
