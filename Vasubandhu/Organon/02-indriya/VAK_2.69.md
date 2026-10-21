# VAK_2.69 — Form and Formless Unobscured Succession

## 1. Sanskrit (Devanāgarī)

```sanskrit
अष्टाभ्यो निवृतं तस्मात् षट् त्रिभ्योऽनिवृतं पुनः /
तस्मात् षट् एवमारूप्ये तस्य नीतिः शुभात्पुनः // २.६९ //
```

## 2. Sanskrit (IAST)

```text
aṣṭābhyo nivṛtaṃ tasmāt ṣaṭ tribhyo 'nivṛtaṃ punaḥ /
tasmāt ṣaṭ evam ārūpye tasya nītiḥ śubhāt punaḥ // 2.69 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| aṣṭābhyaḥ | abl. pl. numeral | From eight predecessors. |
| nivṛtam | n. nom. sg. | Obscured-indeterminate Form-realm mind. |
| tasmāt | abl. sg. | From that obscured, then that unobscured mind. |
| ṣaṭ | numeral | Six successors, in each pair. |
| tribhyaḥ | abl. pl. numeral | From three predecessors. |
| anivṛtam | n. nom. sg. | Unobscured-indeterminate mind. |
| punaḥ | adverb | Again; then opens the next wholesome case. |
| evam | adverb | Likewise. |
| ārūpye | loc. sg. | In the formless realm. |
| tasya | gen. sg. pronoun | Of that unobscured kind. |
| nītiḥ | f. nom. sg. | Rule or pattern. |
| śubhāt | abl. sg. | From wholesome; begins the next calculation. |

The [running witness](../../Sources/kosabhasya.txt) reads
*aṣṭābhyo nivṛtaṃ … tribhyo 'nivṛtaṃ punaḥ* and ends with
*evamārūpye tasya nītiḥ śubhātpunaḥ*. The former Organon wording
reordered the first phrase and left the last two words outside its
parse. The normalized tokens open external sandhi.

```text
# tokens: aṣṭābhyaḥ nivṛtam tasmāt ṣaṭ tribhyaḥ anivṛtam punaḥ tasmāt ṣaṭ evam ārūpye tasya nītiḥ śubhāt punaḥ
```

## 4. Grammar

Form obscured mind arises after eight kinds and has six successors.
Form unobscured arises after three and has six successors. The latter
three/six rule also holds for formless unobscured mind. *Śubhāt
punaḥ* opens the subsequent formless wholesome case without supplying
its count here.

```nltk-fcfg
% start S
# tokens: aṣṭābhyaḥ nivṛtam tasmāt ṣaṭ tribhyaḥ anivṛtam punaḥ tasmāt ṣaṭ evam ārūpye tasya nītiḥ śubhāt punaḥ
S[SEM=<(?obsc8 & ?obsc6 & ?unobsc3 & ?unobsc6 & ?formless & ?open)>] -> OBSC8[SEM=?obsc8] OBSC6[SEM=?obsc6] UNOBSC3[SEM=?unobsc3] UNOBSC6[SEM=?unobsc6] FORMLESS[SEM=?formless] OPEN[SEM=?open]
OBSC8[SEM=<PredecessorCount(form_obscured,eight)>] -> FROM_EIGHT[CASE=abl,NUM=pl,COUNT=8] OBSC[CASE=nom,NUM=sg]
FROM_EIGHT[CASE=abl,NUM=pl,COUNT=8] -> 'aṣṭābhyaḥ'
OBSC[CASE=nom,NUM=sg] -> 'nivṛtam'
OBSC6[SEM=<SuccessorCount(form_obscured,six)>] -> FROM_OBSC[CASE=abl,NUM=sg] SIX1[COUNT=6]
FROM_OBSC[CASE=abl,NUM=sg] -> 'tasmāt'
SIX1[COUNT=6] -> 'ṣaṭ'
UNOBSC3[SEM=<PredecessorCount(form_unobscured,three)>] -> FROM_THREE[CASE=abl,NUM=pl,COUNT=3] UNOBSC[CASE=nom,NUM=sg] AGAIN
FROM_THREE[CASE=abl,NUM=pl,COUNT=3] -> 'tribhyaḥ'
UNOBSC[CASE=nom,NUM=sg] -> 'anivṛtam'
AGAIN -> 'punaḥ'
UNOBSC6[SEM=<SuccessorCount(form_unobscured,six)>] -> FROM_UNOBSC[CASE=abl,NUM=sg] SIX2[COUNT=6]
FROM_UNOBSC[CASE=abl,NUM=sg] -> 'tasmāt'
SIX2[COUNT=6] -> 'ṣaṭ'
FORMLESS[SEM=<(PredecessorCount(formless_unobscured,three) & SuccessorCount(formless_unobscured,six))>] -> LIKEWISE IN_FORMLESS[CASE=loc,NUM=sg] ITS[CASE=gen,NUM=sg] RULE[CASE=nom,NUM=sg]
LIKEWISE -> 'evam'
IN_FORMLESS[CASE=loc,NUM=sg] -> 'ārūpye'
ITS[CASE=gen,NUM=sg] -> 'tasya'
RULE[CASE=nom,NUM=sg] -> 'nītiḥ'
OPEN[SEM=<WholesomeCaseOpened(formless_realm)>] -> FROM_GOOD[CASE=abl,NUM=sg] AGAIN2
FROM_GOOD[CASE=abl,NUM=sg] -> 'śubhāt'
AGAIN2 -> 'punaḥ'
```

```nltk-dep
'nivṛtam' -> 'aṣṭābhyaḥ'
'ṣaṭ' -> 'tasmāt'
'anivṛtam' -> 'tribhyaḥ' | 'punaḥ'
'nītiḥ' -> 'evam' | 'ārūpye' | 'tasya'
'śubhāt' -> 'punaḥ'
```

**Feature chart checkpoints.** Form obscured's eight and six span
[0, 2) and [2, 4); Form unobscured's three and six span [4, 7)
and [7, 9); the formless rule spans [9, 13); the open wholesome
fragment spans [13, 15). The root spans [0, 15). The final fragment
has no count in this verse.

## 5. Translation

### Literal Translation

> The obscured [mind] arises from eight; from it, six [arise]. The
> unobscured, again, arises from three; from it, six. Thus in the
> formless realm is its rule. From the wholesome, however—

### Bhāṣya-informed study translation

> Form obscured mind follows eight kinds and is followed by six. Form
> unobscured follows three and is followed by six; formless
> unobscured follows the same three/six rule. From formless wholesome,
> however—

## 6. Philosophical Translation

> The verse gives two directed counts for Form obscured and Form
> unobscured, carries the unobscured pattern into the formless realm,
> and opens the next calculation from formless wholesome. The Bhāṣya
> identifies the excluded kinds and the six successors in each case.

## 7. Technical Vocabulary

| Term | Rendering |
|---|---|
| nivṛta | Obscured-indeterminate Form mind; eight predecessors, six successors. |
| anivṛta | Unobscured-indeterminate Form mind; three predecessors, six successors. |
| tasya nītiḥ | Its rule; the unobscured three/six pattern carried to formless mind. |
| śubhāt punaḥ | From wholesome, however; opens the next verse's count. |

## 8. Logical Determination

**Kārikā, derived.** The root `SEM` states four directed Form counts,
the repeated three/six for formless unobscured, and the opening of
the formless wholesome case. It does not infer that Form obscured's
eight/six rule also applies in the formless realm.

```nltk-sem
form_obscured_eight : PredecessorCount(form_obscured,eight)
form_obscured_six : SuccessorCount(form_obscured,six)
form_unobscured_three : PredecessorCount(form_unobscured,three)
form_unobscured_six : SuccessorCount(form_unobscured,six)
formless_unobscured : PredecessorCount(formless_unobscured,three) & SuccessorCount(formless_unobscured,six)
opening : WholesomeCaseOpened(formless_realm)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(PredecessorCount(form_obscured,eight) & SuccessorCount(form_obscured,six) & PredecessorCount(form_unobscured,three) & SuccessorCount(form_unobscured,six) & PredecessorCount(formless_unobscured,three) & SuccessorCount(formless_unobscured,six) & WholesomeCaseOpened(formless_realm))

# THEORY prose_form_obscured
# EXPECT prose_form_obscured T
-Includes(eight_predecessors,afflicted_desire_two) & -Includes(eight_predecessors,uncontaminated_two) & Includes(six_form_obscured,own_three) & -Includes(six_form_obscured,desire_unobscured)

# THEORY prose_form_unobscured
# EXPECT prose_form_unobscured T
Includes(three_predecessors,own_three) & Includes(six_form_unobscured,own_three) & Includes(six_form_unobscured,afflicted_desire_two) & Includes(six_form_unobscured,formless_obscured)

# THEORY rejected_formless_obscured_eight
# EXPECT rejected_formless_obscured_eight F
PredecessorCount(formless_unobscured,three) & PredecessorCount(formless_unobscured,eight)

# THEORY rejected_form_unobscured_eight
# EXPECT rejected_form_unobscured_eight F
SuccessorCount(form_unobscured,six) & PredecessorCount(form_unobscured,eight)
```

```nltk-valuation
form_obscured => form_obscured_kind
form_unobscured => form_unobscured_kind
formless_unobscured => formless_unobscured_kind
formless_realm => formless_domain
eight => eight_count
six => six_count
three => three_count
eight_predecessors => eight_group
six_form_obscured => six_obsc_group
three_predecessors => three_group
six_form_unobscured => six_unobsc_group
afflicted_desire_two => desire_afflicted_pair
uncontaminated_two => uncontaminated_pair
own_three => own_three_group
desire_unobscured => desire_unobscured_kind
formless_obscured => formless_obscured_kind
PredecessorCount => {(form_obscured_kind,eight_count),(form_unobscured_kind,three_count),(formless_unobscured_kind,three_count)}
SuccessorCount => {(form_obscured_kind,six_count),(form_unobscured_kind,six_count),(formless_unobscured_kind,six_count)}
WholesomeCaseOpened => {formless_domain}
Includes => {(six_obsc_group,own_three_group),(three_group,own_three_group),(six_unobsc_group,own_three_group),(six_unobsc_group,desire_afflicted_pair),(six_unobsc_group,formless_obscured_kind)}
```

The finite valuation witnesses the six counts and the open wholesome
fragment. Removing a count falsifies the verse. The prose groups
compress multiple kinds; they do not identify every individual
successor or predecessor.

## 9. Interpretive Note

**Translation note.** Form obscured arises from eight kinds, excluding
the two afflicted desire kinds and the trainee and beyond-training
kinds. Six follow it: three of its own level and three desire kinds
other than unobscured-indeterminate. Form unobscured arises from its
three own-level kinds; six follow it, comprising its own three, the
two afflicted desire kinds, and formless obscured. The Bhāṣya applies
the same three-predecessor/six-successor rule to formless unobscured.

*Śubhāt punaḥ* opens the formless wholesome calculation completed in
2.70. The verse gives no number for it here.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_69 a vak:Karika ; vak:hasTopic vak:FormAndFormlessUnobscuredSuccession .
vak:FormObscured vak:predecessorCount 8 ; vak:successorCount 6 .
vak:FormUnobscured vak:predecessorCount 3 ; vak:successorCount 6 .
vak:FormlessUnobscured vak:predecessorCount 3 ; vak:successorCount 6 .
```
