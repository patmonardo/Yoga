# VAK_2.61 — Four Conditions

## 1. Sanskrit (Devanāgarī)

```sanskrit
चित्तचैत्ताः / तथान्येऽपि संप्रयुक्तकवर्जिताः /
चत्वारः प्रत्यया उक्ताः / हेत्वाख्यः पञ्च हेतवः // २.६१ //
```

## 2. Sanskrit (IAST)

```text
cittacaittāḥ / tathā 'nye 'pi saṃprayuktakavarjitāḥ /
catvāraḥ pratyayā uktāḥ / hetvākhyaḥ pañca hetavaḥ // 2.61 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| cittacaittāḥ | m. nom. pl. | Mind and mental factors: the first scope of the preceding four profiles. |
| tathā | indeclinable | Likewise. |
| anye | m. nom. pl. | Other dharmas, here material and mind-dissociated. |
| api | particle | Also. |
| saṃprayuktakavarjitāḥ | m. nom. pl. | Excluding the associated cause; qualifies the others. |
| catvāraḥ | m. nom. pl. numeral | Four. |
| pratyayāḥ | m. nom. pl. | Conditions. |
| uktāḥ | m. nom. pl. participle | Taught. |
| hetvākhyaḥ | m. nom. sg. | Named “cause”; qualifies the cause-condition. |
| pañca | numeral | Five. |
| hetavaḥ | m. nom. pl. | Causes. |

The running [Sanskrit witness](../../Sources/kosabhasya.txt) prints
this kārikā in four separated fragments at 97.27, 97.29, 98.04, and
98.07. The previous Organon first line was unsupported by that witness.
The normalized tokens open *nye 'pi* and the final visarga before
*uktāḥ* without changing the attested wording.

```text
# tokens: cittacaittāḥ tathā anye api saṃprayuktakavarjitāḥ catvāraḥ pratyayāḥ uktāḥ hetvākhyaḥ pañca hetavaḥ
```

## 4. Grammar

The opening names mind and mental factors, then applies the preceding
causal profiles likewise to other dharmas while excluding the
associated cause for those others. The next two fragments introduce
four conditions and specify that the cause-condition comprises five
causes. Their individual identities come from the Bhāṣya.

```nltk-fcfg
% start S
# tokens: cittacaittāḥ tathā anye api saṃprayuktakavarjitāḥ catvāraḥ pratyayāḥ uktāḥ hetvākhyaḥ pañca hetavaḥ
S[SEM=<(?scope & ?four & ?cause)>] -> SCOPE[SEM=?scope] FOUR[SEM=?four] CAUSE[SEM=?cause]
SCOPE[SEM=<(?mind & ?others)>] -> MIND[CASE=nom,NUM=pl,SEM=?mind] OTHERS[CASE=nom,NUM=pl,SEM=?others]
MIND[CASE=nom,NUM=pl,SEM=<ProfilesApplyTo(citta_caitta)>] -> 'cittacaittāḥ'
OTHERS[CASE=nom,NUM=pl,SEM=<(ProfilesApplyTo(other_dharmas) & OmitsAssociated(other_dharmas))>] -> LIKEWISE OTHER[CASE=nom,NUM=pl] ALSO WITHOUT_ASSOC[CASE=nom,NUM=pl]
LIKEWISE -> 'tathā'
OTHER[CASE=nom,NUM=pl] -> 'anye'
ALSO -> 'api'
WITHOUT_ASSOC[CASE=nom,NUM=pl] -> 'saṃprayuktakavarjitāḥ'
FOUR[SEM=<FourConditionsTaught(conditions)>] -> FOUR_NUM[CASE=nom,CNT=4] COND[CASE=nom,NUM=pl] TAUGHT[CASE=nom,NUM=pl]
FOUR_NUM[CASE=nom,CNT=4] -> 'catvāraḥ'
COND[CASE=nom,NUM=pl] -> 'pratyayāḥ'
TAUGHT[CASE=nom,NUM=pl] -> 'uktāḥ'
CAUSE[SEM=<CauseConditionHasFive(cause_condition)>] -> CAUSE_NAMED[CASE=nom,NUM=sg] FIVE[CNT=5] CAUSES[CASE=nom,NUM=pl]
CAUSE_NAMED[CASE=nom,NUM=sg] -> 'hetvākhyaḥ'
FIVE[CNT=5] -> 'pañca'
CAUSES[CASE=nom,NUM=pl] -> 'hetavaḥ'
```

```nltk-dep
'cittacaittāḥ' -> 'tathā' | 'anye' | 'api' | 'saṃprayuktakavarjitāḥ'
'pratyayāḥ' -> 'catvāraḥ' | 'uktāḥ'
'hetavaḥ' -> 'hetvākhyaḥ' | 'pañca'
```

**Feature chart checkpoints.** The profile-scope phrase spans [0,
5), the four-condition phrase [5, 8), the cause-condition phrase [8,
11), and the root [0, 11). The plural agreement and numeral
features constrain those claims. The exclusion modifies the other
dharmas, not mind and mental factors.

## 5. Translation

### Literal Translation

> Mind and mental factors; the others likewise, but without the
> associated cause. Four conditions are taught; five causes are called
> the cause-condition.

### Bhāṣya-informed study translation

> The four causal profiles apply to mind and mental factors, and
> likewise to other dharmas except for the associated cause. Four
> conditions are taught; five causes constitute the cause-condition.

## 6. Philosophical Translation

> The causal profiles of 2.60 first govern mind and mental factors.
> Material and mind-dissociated dharmas follow those profiles with the
> associated cause removed. The exposition then moves from the six
> causes to four conditions; five causes other than the conditioning
> cause make up the cause-condition.

## 7. Technical Vocabulary

| Term | Rendering |
|---|---|
| cittacaittāḥ | Mind and mental factors; first domain of the four profiles. |
| saṃprayuktakavarjitāḥ | Without the associated cause; qualifies the other dharmas. |
| pratyaya | Condition; four kinds are reported in the sūtra. |
| hetu-pratyaya | Cause-condition; five of the six causes. |
| kāraṇa-hetu | Conditioning cause; omitted from that five-cause set. |
| samanantara / ālambana / adhipati | Immediately antecedent / object / predominant; the other three conditions named in prose. |

## 8. Logical Determination

**Kārikā, derived.** The root `SEM` states the two domains of the
causal profiles, the associated-cause exception for the other domain,
the four-condition count, and the five-cause count of the
cause-condition. The identities of the conditions and the omitted
conditioning cause are Bhāṣya determinations.

```nltk-sem
scope : ProfilesApplyTo(citta_caitta) & ProfilesApplyTo(other_dharmas) & OmitsAssociated(other_dharmas)
four : FourConditionsTaught(conditions)
cause : CauseConditionHasFive(cause_condition)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(ProfilesApplyTo(citta_caitta) & ProfilesApplyTo(other_dharmas) & OmitsAssociated(other_dharmas) & FourConditionsTaught(conditions) & CauseConditionHasFive(cause_condition))

# THEORY prose_four_kinds
# EXPECT prose_four_kinds T
ConditionKind(cause_condition) & ConditionKind(immediately_antecedent) & ConditionKind(object) & ConditionKind(predominant)

# THEORY prose_five_causes
# EXPECT prose_five_causes T
InCauseCondition(coarisen) & InCauseCondition(associated) & InCauseCondition(homogeneous) & InCauseCondition(pervasive) & InCauseCondition(maturation) & -InCauseCondition(conditioning)

# THEORY prose_other_counts
# EXPECT prose_other_counts T
OtherCauseCount(afflicted,four_count) & OtherCauseCount(maturation_born,four_count) & OtherCauseCount(remaining,three_count) & OtherCauseCount(first_noble,two_count)

# THEORY rejected_mind_omits_associated
# EXPECT rejected_mind_omits_associated F
ProfilesApplyTo(citta_caitta) & OmitsAssociated(citta_caitta)

# THEORY rejected_conditioning_in_cause_condition
# EXPECT rejected_conditioning_in_cause_condition F
CauseConditionHasFive(cause_condition) & InCauseCondition(conditioning)
```

```nltk-valuation
citta_caitta => mind_factors
other_dharmas => other_domain
conditions => condition_inventory
cause_condition => cause_condition_kind
immediately_antecedent => antecedent_kind
object => object_kind
predominant => predominant_kind
coarisen => coarisen_cause
associated => associated_cause
homogeneous => homogeneous_cause
pervasive => pervasive_cause
maturation => maturation_cause
conditioning => conditioning_cause
afflicted => afflicted_class
maturation_born => maturation_class
remaining => remaining_class
first_noble => first_noble_class
four_count => four
three_count => three
two_count => two
ProfilesApplyTo => {mind_factors,other_domain}
OmitsAssociated => {other_domain}
FourConditionsTaught => {condition_inventory}
CauseConditionHasFive => {cause_condition_kind}
ConditionKind => {cause_condition_kind,antecedent_kind,object_kind,predominant_kind}
InCauseCondition => {coarisen_cause,associated_cause,homogeneous_cause,pervasive_cause,maturation_cause}
OtherCauseCount => {(afflicted_class,four),(maturation_class,four),(remaining_class,three),(first_noble_class,two)}
```

The finite model witnesses the two verse counts and the
Bhāṣya-specified five-cause membership. It rejects transferring the
associated-cause exclusion to mind and mental factors or admitting
the conditioning cause to the cause-condition.

## 9. Interpretive Note

**Translation note.** The kārikā's opening fragments finish the
preceding six-cause discussion. The Bhāṣya specifies that material
and mind-dissociated dharmas follow the four profiles after the
associated cause is removed, giving counts of four, four, three, and
two. It then cites the four conditions: cause, immediately antecedent,
object, and predominant. Of the six causes, the five apart from the
conditioning cause constitute the cause-condition.

The change of topic occurs within the kārikā. The other three
conditions are named here; their definitions belong to subsequent
passages.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_61 a vak:Karika ; vak:hasTopic vak:FourConditions .
vak:OtherDharmas vak:omitsCause vak:AssociatedCause .
vak:CauseCondition vak:hasCauseCount 5 ; vak:excludes vak:ConditioningCause .
```
