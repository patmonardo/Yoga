# VAK_2.63 — Activity at Ceasing and Arising

## 1. Sanskrit (Devanāgarī)

```sanskrit
निरुध्यमाने कारित्रं द्वौ हेतू कुरुतः त्रयः /
जायमाने ततोऽन्यौ तु प्रत्ययौ तद्विपर्ययात् // २.६३ //
```

## 2. Sanskrit (IAST)

```text
nirudhyamāne kāritraṃ dvau hetū kurutaḥ trayaḥ /
jāyamāne tato 'nyau tu pratyayau tadviparyayāt // 2.63 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| nirudhyamāne | loc. sg. present participle | At the ceasing state of a dharma. |
| kāritraṃ | n. acc. sg. | Activity or function. |
| dvau | m. nom. dual | Two. |
| hetū | m. nom. dual | Causes. |
| kurutaḥ | 3rd dual present middle | Perform. |
| trayaḥ | m. nom. pl. | Three causes, with “perform activity” supplied. |
| jāyamāne | loc. sg. present participle | At the arising state of a dharma. |
| tataḥ | ablative adverb | From that account. |
| anyau | m. nom. dual | The other two. |
| tu | particle | But. |
| pratyayau | m. nom. dual | Conditions. |
| tadviparyayāt | abl. sg. | According to its reversal. |

The local [running witness](../../Sources/kosabhasya.txt) prints
this verse in four fragments at 100.21, 100.24, 100.25, and 101.01.
The older VAK study preserves the continuous line. The former
Organon text omitted the opening timing and activity words.

```text
# tokens: nirudhyamāne kāritram dvau hetū kurutaḥ trayaḥ jāyamāne tataḥ anyau tu pratyayau tadviparyayāt
```

## 4. Grammar

The first clause says that two causes perform activity at the ceasing
state. Ellipsis carries “perform activity” to the three causes at the
arising state. The other two conditions act in the reverse temporal
arrangement. The Bhāṣya names the causes and conditions in each group.

```nltk-fcfg
% start S
# tokens: nirudhyamāne kāritram dvau hetū kurutaḥ trayaḥ jāyamāne tataḥ anyau tu pratyayau tadviparyayāt
S[SEM=<(?ceasing & ?arising & ?reverse)>] -> CEASING[SEM=?ceasing] ARISING[SEM=?arising] REVERSE[SEM=?reverse]
CEASING[SEM=<TwoCausesActAt(ceasing_state)>] -> CESS[CASE=loc,NUM=sg] ACTIVITY[CASE=acc,NUM=sg] TWO[CASE=nom,NUM=du] CAUSES[CASE=nom,NUM=du] DO[NUM=du]
CESS[CASE=loc,NUM=sg] -> 'nirudhyamāne'
ACTIVITY[CASE=acc,NUM=sg] -> 'kāritram'
TWO[CASE=nom,NUM=du] -> 'dvau'
CAUSES[CASE=nom,NUM=du] -> 'hetū'
DO[NUM=du] -> 'kurutaḥ'
ARISING[SEM=<ThreeCausesActAt(arising_state)>] -> THREE[CASE=nom,NUM=pl] ARISE[CASE=loc,NUM=sg]
THREE[CASE=nom,NUM=pl] -> 'trayaḥ'
ARISE[CASE=loc,NUM=sg] -> 'jāyamāne'
REVERSE[SEM=<OtherTwoConditionsReverse(conditions_pair)>] -> FROM OTHER[CASE=nom,NUM=du] BUT COND[CASE=nom,NUM=du] REV[CASE=abl]
FROM -> 'tataḥ'
OTHER[CASE=nom,NUM=du] -> 'anyau'
BUT -> 'tu'
COND[CASE=nom,NUM=du] -> 'pratyayau'
REV[CASE=abl] -> 'tadviparyayāt'
```

```nltk-dep
'kurutaḥ' -> 'nirudhyamāne' | 'kāritram' | 'dvau' | 'hetū'
'jāyamāne' -> 'trayaḥ'
'pratyayau' -> 'tataḥ' | 'anyau' | 'tu' | 'tadviparyayāt'
```

**Feature chart checkpoints.** The ceasing clause spans [0, 5), the
arising clause [5, 7), the reverse clause [7, 12), and the root [0,
12). Dual and plural features constrain the two cause groups and the
other two conditions. Their identities belong to the Bhāṣya.

## 5. Translation

### Literal Translation

> At a dharma's ceasing, two causes perform their activity; three [do
> so] at its arising. The other two conditions act by the reverse of
> this arrangement.

### Bhāṣya-informed study translation

> Two causes act on a dharma that is ceasing, and three on one that is
> arising. The other two conditions act in the reverse temporal order.

## 6. Philosophical Translation

> The verse distinguishes the activity of two causes at the present
> state directed toward cessation from that of three causes at the
> future state directed toward arising. The Bhāṣya assigns the
> immediately antecedent and object-conditions to the opposite sides
> of this timing pattern.

## 7. Technical Vocabulary

| Term | Rendering |
|---|---|
| nirudhyamāna | Ceasing; explained as the present directed toward cessation. |
| jāyamāna | Arising; explained as the future directed toward arising. |
| kāritra | Activity or causal function. |
| tadviparyayāt | By reversal of the preceding temporal arrangement. |
| avakāśa | Opening; the immediately antecedent condition gives it for arising. |
| anāvaraṇa | Non-obstruction; the predominant condition's activity in every state. |

## 8. Logical Determination

**Kārikā, derived.** The root `SEM` records the activity of two causes
at ceasing, three at arising, and the reverse timing of the other two
conditions. The Bhāṣya supplies the membership of each group, the
opening given by the immediately antecedent condition, apprehension
through the object-condition, and non-obstruction by predominance.

```nltk-sem
ceasing : TwoCausesActAt(ceasing_state)
arising : ThreeCausesActAt(arising_state)
reverse : OtherTwoConditionsReverse(conditions_pair)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
TwoCausesActAt(ceasing_state) & ThreeCausesActAt(arising_state) & OtherTwoConditionsReverse(conditions_pair)

# THEORY prose_causes
# EXPECT prose_causes T
ActsAt(coarisen,ceasing_state) & ActsAt(associated,ceasing_state) & ActsAt(homogeneous,arising_state) & ActsAt(pervasive,arising_state) & ActsAt(maturation,arising_state)

# THEORY prose_conditions
# EXPECT prose_conditions T
GivesOpeningTowardArising(immediately_antecedent) & ActsAt(immediately_antecedent,arising_state) & PresentApprehension(object) & ActsAt(object,ceasing_state)

# THEORY prose_predominance
# EXPECT prose_predominance T
ConditionKind(predominant) & NonObstructionInEveryState(predominant)

# THEORY rejected_coarisen_at_arising
# EXPECT rejected_coarisen_at_arising F
ActsAt(coarisen,ceasing_state) & ActsAt(coarisen,arising_state)

# THEORY rejected_object_at_arising
# EXPECT rejected_object_at_arising F
PresentApprehension(object) & ActsAt(object,arising_state)
```

```nltk-valuation
ceasing_state => ceasing_phase
arising_state => arising_phase
conditions_pair => other_two_conditions
coarisen => coarisen_cause
associated => associated_cause
homogeneous => homogeneous_cause
pervasive => pervasive_cause
maturation => maturation_cause
immediately_antecedent => samanantara_condition
object => object_condition
predominant => predominant_condition
TwoCausesActAt => {ceasing_phase}
ThreeCausesActAt => {arising_phase}
OtherTwoConditionsReverse => {other_two_conditions}
ActsAt => {(coarisen_cause,ceasing_phase),(associated_cause,ceasing_phase),(homogeneous_cause,arising_phase),(pervasive_cause,arising_phase),(maturation_cause,arising_phase),(samanantara_condition,arising_phase),(object_condition,ceasing_phase)}
GivesOpeningTowardArising => {samanantara_condition}
PresentApprehension => {object_condition}
ConditionKind => {predominant_condition}
NonObstructionInEveryState => {predominant_condition}
```

The finite valuation witnesses the verse's three claims and the
Bhāṣya's distinct assignments. Removing any of the three verse
predications makes the verse false. The prose countertests reject
putting the co-arisen cause or object-condition on the opposite side.

## 9. Interpretive Note

**Translation note.** The Bhāṣya explains the ceasing state as the
present directed toward cessation and the arising state as the future
directed toward production. Co-arisen and associated causes act at
the former; homogeneous, pervasive, and maturation causes act at the
latter. The immediately antecedent condition gives an opening toward
arising, while an object is apprehended by present mind and factors
at ceasing. Predominance operates by non-obstruction in every state.

The verse states the temporal contrast; the Bhāṣya assigns the named
causes and conditions to it. The next verse counts conditions for
specific classes of dharma.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_63 a vak:Karika ; vak:hasTopic vak:CausalActivityTiming .
vak:TwoCauses vak:actAt vak:Ceasing .
vak:ThreeCauses vak:actAt vak:Arising .
vak:OtherTwoConditions vak:reverseTiming true .
```
