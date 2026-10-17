# VAK_8.08 — Third and Fourth Dhyāna Factors: Eighteen by Name

## 1. Sanskrit (Devanāgarī)

```sanskrit
तृतीये पञ्च तूपेक्षा स्मृतिः प्रज्ञा सुखं स्थितिः ।
चत्वार्यन्तेऽसुखादुःखोपेक्षास्मृतिसमाधयः ॥ ८.०८ ॥
```

## 2. Sanskrit (IAST)

```text
tṛtīye pañca tūpekṣā smṛtiḥ prajñā sukhaṃ sthitiḥ |
catvāry ante 'sukhāduḥkhopekṣāsmṛtisamādhayaḥ || 8.08 ||
```

The Sanskrit follows the local kārikā witness. The
Devanāgarī renders the same reading. The prose resolves
`sthiti` as samādhi and supplies the purification
qualifications of the fourth dhyāna's equanimity and
mindfulness.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `tṛtīye` | locative singular neuter ordinal | in the third [dhyāna] |
| `pañca` | numeral | five [factors] |
| `tu` | transition or contrast particle (`tu + upekṣā` → `tūpekṣā`) | however; now |
| `upekṣā` | nominative singular feminine | equanimity |
| `smṛtiḥ` | nominative singular feminine | mindfulness or recollection |
| `prajñā` | nominative singular feminine | discriminative knowing, glossed as clear comprehension |
| `sukham` | nominative singular neuter | ease or pleasure |
| `sthitiḥ` | nominative singular feminine | stability, here samādhi |
| `catvāri` | nominative plural neuter numeral (`catvāry ante`) | four [factors] |
| `ante` | locative singular (`ante 'sukha-`) | in the last, the fourth dhyāna |
| `asukha-aduḥkha` | compound member | neither pleasure nor pain; the prose reverses the order to `aduḥkhāsukhā vedanā` without changing the determination |
| `upekṣā-smṛti-samādhayaḥ` | ending of the coordinated compound | equanimity, mindfulness, and concentration |

## 4. Grammar

The third-dhyāna list counts five; `prajñā` is glossed as clear comprehension, and `sthiti` as samādhi. The fourth list has four: purification qualifies its equanimity and mindfulness; neutral feeling is a separate factor.

```nltk-fcfg
% start S
# tokens: tṛtīye pañca tūpekṣā smṛtiḥ prajñā sukhaṃ sthitiḥ catvāri ante asukhāduḥkhopekṣāsmṛtisamādhayaḥ
S -> CL[K=third] CL[K=fourth]
CL[K=third] -> LOC[CASE=loc,NUM=sg,GEN=n] NUM[COUNT=five] N[CASE=nom,NUM=sg,GEN=f] N[CASE=nom,NUM=sg,GEN=f] N[CASE=nom,NUM=sg,GEN=f] N[CASE=nom,NUM=sg,GEN=n] N[CASE=nom,NUM=sg,GEN=f,ALIAS=samadhi]
CL[K=fourth] -> NUM[COUNT=four] LOC[CASE=loc,NUM=sg,GEN=n] N[CASE=nom,NUM=pl,GEN=m,COUNT=four,QUAL=partly_purified]
LOC[CASE=loc,NUM=sg,GEN=n] -> 'tṛtīye'
NUM[COUNT=five] -> 'pañca'
N[CASE=nom,NUM=sg,GEN=f] -> 'tūpekṣā'
N[CASE=nom,NUM=sg,GEN=f] -> 'smṛtiḥ'
N[CASE=nom,NUM=sg,GEN=f] -> 'prajñā'
N[CASE=nom,NUM=sg,GEN=n] -> 'sukhaṃ'
N[CASE=nom,NUM=sg,GEN=f,ALIAS=samadhi] -> 'sthitiḥ'
NUM[COUNT=four] -> 'catvāri'
LOC[CASE=loc,NUM=sg,GEN=n] -> 'ante'
N[CASE=nom,NUM=pl,GEN=m,COUNT=four,QUAL=partly_purified] -> 'asukhāduḥkhopekṣāsmṛtisamādhayaḥ'
```

```nltk-dep
'sthitiḥ' -> 'tṛtīye' | 'pañca' | 'tūpekṣā' | 'smṛtiḥ' | 'prajñā' | 'sukhaṃ'
'asukhāduḥkhopekṣāsmṛtisamādhayaḥ' -> 'catvāri' | 'ante'
```

`Ante` means the fourth dhyāna, not bhavāgra. Neutral feeling and equanimity are distinct factors; the verse counts names (`nāmataḥ`), not distinct substances.


**Close construe.** In the third dhyāna are five factors:
equanimity, mindfulness, clear comprehension, ease, and
stability. In the fourth are four: neither-pain-nor-
pleasure feeling, purified equanimity, purified mindfulness,
and samādhi.

## 5. Translation

### Literal Translation

> In the third are five: equanimity, mindfulness,
> discriminative knowing, ease, and stability. In the
> last are four: neither pleasure nor pain, equanimity,
> mindfulness, and concentration.

### Bhāṣya-informed study translation

> In the third dhyāna are five factors: equanimity, mindfulness,
> clear comprehension, ease, and stability, that is, samādhi. In
> the last are four: feeling that is neither pleasure nor pain,
> purified equanimity, purified mindfulness, and samādhi.

## 6. Philosophical Translation

> The later dhyānas are positively specified through
> their factors and their qualifications. The fourth
> does not merely lack the third's pleasant feeling:
> neutral feeling is counted, and equanimity and mindfulness
> are explicitly qualified by purification.

The completed eighteenfold inventory counts named factors
across four attainments. It does not yet establish
eighteen distinct kinds of dharma, nor eighteen factors
simultaneously present in one attainment.

## 7. Technical Vocabulary

**`Upekṣā`.** Equanimity. Its separate position beside
neutral feeling in the fourth list prevents reducing
it here to a feeling that is neither painful nor pleasant.
The later analysis will determine the factor more fully.

**`Smṛti`.** Mindfulness or recollection. It is a named
factor in the third and, with purification specified,
in the fourth. The present verse does not reduce it
to autobiographical memory or to recalling past lives.

**`Saṃprajñāna`.** Clear comprehension, the prose's
expansion of the verse's prajñā. This is the local
factor designation; it does not by itself assert final
liberation or omniscience.

**`Sthiti`.** Stability. The prose explicitly identifies
it with samādhi here. The synonym does not establish
an unchanging mind or a permanent mental substance.

**`Aduḥkhāsukhā vedanā`.** Feeling that is neither
painful nor pleasant. The source names a feeling,
not the absence of every feeling. Its presence is
compatible with the five-Base accompanied dhyāna
constitution discussed earlier.

**`Upekṣāpariśuddhi / smṛtipariśuddhi`.** Purification
of equanimity and of mindfulness. These are the fourth
dhyāna factors as expanded by the Bhāṣya. “Purified”
must not automatically mean “uncontaminated” and erase
the separate mode classification of VAK 8.05–8.06.

**`Nāmataḥ`.** By name or designation. The transmitted
`nāmata evam` qualifies the eighteenfold total and
prepares a different counting question in VAK 8.09.
Repeated roles across levels are included in the total.

## 8. Logical Determination

The verse completes the third- and fourth-dhyāna lists and identifies stability with samādhi [verse; prose]. Its eighteen is a count by name across the four dhyānas, not a claim of eighteen distinct dharmas.

**Signature.** `FactorOf(level,factor)`; `Count(level,n)`; `Purified(level,factor)`; `SameRole(x,y)`; `NamedTotal(n)`.

**Finite data.** The third list has five names and the fourth four; the latter's equanimity and mindfulness carry purification, and neutral feeling remains a separate factor.

```nltk-valuation
first => first
second => second
third => third
fourth => fourth
vitarka => vitarka
vicara => vicara
priti => priti
pliancy => pliancy
clarity => clarity
upeksa => upeksa
smrti => smrti
comprehension => comprehension
sukha => sukha
sthiti => sthiti
neutralfeeling => neutralfeeling
upeksapurified => upeksapurified
smrtipurified => smrtipurified
samadhi => samadhi
five => five
four => four
eighteen => eighteen
FactorOf => {(first,vitarka),(first,vicara),(first,priti),(first,pliancy),(first,samadhi),(second,priti),(second,sukha),(second,samadhi),(second,clarity),(third,upeksa),(third,smrti),(third,comprehension),(third,sukha),(third,sthiti),(fourth,neutralfeeling),(fourth,upeksapurified),(fourth,smrtipurified),(fourth,samadhi)}
Count => {(third,five),(fourth,four)}
Purified => {(fourth,upeksa),(fourth,smrti)}
SameRole => {(sthiti,samadhi)}
NamedTotal => {eighteen}
```

**Rules (verse and prose).**

```nltk-fol
# THEORY shared
# [verse] tṛtīye pañca; [prose] prajñā = saṃprajñāna, sthiti = samādhi
Count(third,five)
FactorOf(third,upeksa)
FactorOf(third,smrti)
FactorOf(third,comprehension)
FactorOf(third,sukha)
SameRole(sthiti,samadhi)
# [verse] catvāry ante; [prose] fourth equanimity and mindfulness are purified
Count(fourth,four)
FactorOf(fourth,neutralfeeling)
Purified(fourth,upeksa)
Purified(fourth,smrti)
FactorOf(fourth,samadhi)
# [prose] 5 + 4 + 5 + 4, counted nāmataḥ
NamedTotal(eighteen)
```

**Results (NLTK).** The finite-model checker confirms the listed membership, count, purification, and total assertions. The total is a tally of named roles; it is not a derived count of unique dharmas (the next verse treats that question).

**Scope cautions.** The fourth's neutral feeling is not the same factor as equanimity; “purified” does not mean uncontaminated. Failure to list clear comprehension in the fourth is not a claim that all knowing is absent. `Ante` refers to the fourth dhyāna, not bhavāgra.

## 9. Interpretive Note

**Qualifiers are part of the determination.** The verse's
brief upekṣā and smṛti in the fourth compound receive
explicit purification qualifications in prose. A study
that simply repeats the unqualified words would omit
part of the Bhāṣya's account. Conversely, adding a
full theory of what causes that purification would
go beyond this short source unit.

**No inference from non-listing to total absence.**
The research comparison speaks of prajñā dropping
out as a separately counted limb. That qualification
is essential: the present inventory does not establish
that fourth-dhyāna cognition lacks every form of prajñā.
The next substantial analysis will clarify how the
named factors are counted as distinct dharmas.

**Witness cautions.** The running source prints
`smādhiś ca` in the third list; the local extract
regularizes this as `samādhiś ca`. The next sentence's
explicit synonym statement and the verse securely
identify the factor. The change in order from
`asukhāduḥkha` to `aduḥkhāsukha` is retained as a
verse/prose difference, not treated as a doctrinal
contradiction. Originals remain unchanged.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates the factor's role and its
qualification within an attainment. Yoga Technē, its
kriyā–karma companion, concerns its developed operation.
The fourth list illustrates why a recurring name
alone is insufficient: the prose specifies purification
of two recurring factors.

For Organon representation, counting named roles is
not the same as counting underlying kinds. A level-
indexed factor inventory can repeat a determination
and qualify it differently without resolving its
substantial identity. The study should preserve that
question rather than collapse names immediately into
unique entities or multiply entities merely from
repeated names.

This is a structural project use of the source's
counting distinction. It does not turn the dhyānas
into a software type system or substitute a quantitative
complexity measure for their contemplative determination.

**Review status.** Provisional, Bhāṣya-controlled study.
The two factor inventories, prajñā/saṃprajñāna expansion,
sthiti/samādhi synonym, purification qualifiers, neutral
feeling, and eighteenfold name-count have been checked
against the local extract and running source. The
count by distinct dharmas remains for VAK 8.09.

## 10. OWL++ Seed

```text
Class: DhyanaAttainment
Class: NamedFactorRole
Class: FactorQualification

ObjectProperty: countsNamedFactor
ObjectProperty: hasQualification
ObjectProperty: hasLocalSynonym

ThirdDhyana:
    factors: Equanimity, Mindfulness, ClearComprehension, Sukha, Samadhi
    factorCount: 5

FourthDhyana:
    factors: NeutralFeeling, PurifiedEquanimity, PurifiedMindfulness, Samadhi
    factorCount: 4

Sthiti:
    localSynonym: Samadhi

PrajnaInThirdList:
    proseExpansion: Samprajnana

AllFourDhyanaInventories:
    counts: 5, 4, 5, 4
    total: 18
    countingBasis: ByName

ProjectConstraint: Equanimity is separately counted from neutral feeling.
ProjectConstraint: Neutral feeling is not absence of feeling.
ProjectConstraint: Purification is not automatically uncontaminated mode.
ProjectConstraint: Non-listing as a factor does not prove total absence.
ProjectConstraint: Eighteen named roles are not yet eighteen distinct dharmas.
ProjectConstraint: Substantial recount continues in VAK 8.09.
```

This is a declarative project seed, not executable OWL.
VAK 8.09 next recounts the factors by distinct dharma
and identifies several of their natures.
