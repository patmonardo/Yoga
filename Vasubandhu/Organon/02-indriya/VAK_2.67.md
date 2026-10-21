# VAK_2.67 — Desire-Realm Succession

## 1. Sanskrit (Devanāgarī)

```sanskrit
कामे नव शुभाच्चित्ताच्चित्तानि अष्टाभ्य एव तत् /
दशभ्योऽकुशलं तस्माच्चत्वारि निवृतं तथा // २.६७ //
```

## 2. Sanskrit (IAST)

```text
kāme nava śubhāc cittāc cittāni aṣṭābhya eva tat /
daśabhyo 'kuśalaṃ tasmāc catvāri nivṛtaṃ tathā // 2.67 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| kāme | loc. sg. | In the desire realm. |
| nava | numeral | Nine successor consciousnesses. |
| śubhāt | abl. sg. | From wholesome. |
| cittāt | abl. sg. | From consciousness. |
| cittāni | n. nom. pl. | Consciousnesses that arise. |
| aṣṭābhyaḥ | abl. pl. numeral | From eight predecessor kinds. |
| eva | particle | Precisely. |
| tat | n. nom. sg. | That wholesome consciousness. |
| daśabhyaḥ | abl. pl. numeral | From ten predecessor kinds. |
| akuśalam | n. nom. sg. | Unwholesome consciousness. |
| tasmāt | abl. sg. | From it, the unwholesome. |
| catvāri | n. nom. pl. numeral | Four successor kinds. |
| nivṛtam | n. nom. sg. | Obscured consciousness. |
| tathā | adverb | Likewise; repeats the ten/four pattern. |

The [running witness](../../Sources/kosabhasya.txt) and older VAK
study read *śubhāc cittāc cittāni*, *aṣṭābhya eva tat*, and
*daśabhyo 'kuśalaṃ tasmāc catvāri*. The former Organon text omitted
key words and reversed the direction of the unwholesome counts. The
normalized tokens open external sandhi without altering the witness.

```text
# tokens: kāme nava śubhāt cittāt cittāni aṣṭābhyaḥ eva tat daśabhyaḥ akuśalam tasmāt catvāri nivṛtam tathā
```

## 4. Grammar

Five tokens give nine successors of desire-realm wholesome mind. The
next three say that this mind arises from eight predecessors. The
unwholesome arises from ten predecessors; four follow it. *Tathā*
assigns the same ten-predecessor/four-successor pattern to obscured
desire-realm mind. The Bhāṣya enumerates the nine and eight and
explains the exclusions.

```nltk-fcfg
% start S
# tokens: kāme nava śubhāt cittāt cittāni aṣṭābhyaḥ eva tat daśabhyaḥ akuśalam tasmāt catvāri nivṛtam tathā
S[SEM=<(?nine & ?eight & ?ten & ?four)>] -> NINE[SEM=?nine] EIGHT[SEM=?eight] TEN[SEM=?ten] FOUR_SAME[SEM=?four]
NINE[SEM=<SuccessorCount(wholesome_desire,nine)>] -> IN_DESIRE[CASE=loc,NUM=sg] NINE_NUM[COUNT=9] FROM_GOOD[CASE=abl,NUM=sg] FROM_MIND[CASE=abl,NUM=sg] MINDS[CASE=nom,NUM=pl]
IN_DESIRE[CASE=loc,NUM=sg] -> 'kāme'
NINE_NUM[COUNT=9] -> 'nava'
FROM_GOOD[CASE=abl,NUM=sg] -> 'śubhāt'
FROM_MIND[CASE=abl,NUM=sg] -> 'cittāt'
MINDS[CASE=nom,NUM=pl] -> 'cittāni'
EIGHT[SEM=<PredecessorCount(wholesome_desire,eight)>] -> FROM_EIGHT[CASE=abl,NUM=pl,COUNT=8] ONLY THAT[CASE=nom,NUM=sg]
FROM_EIGHT[CASE=abl,NUM=pl,COUNT=8] -> 'aṣṭābhyaḥ'
ONLY -> 'eva'
THAT[CASE=nom,NUM=sg] -> 'tat'
TEN[SEM=<PredecessorCount(unwholesome_desire,ten)>] -> FROM_TEN[CASE=abl,NUM=pl,COUNT=10] BAD[CASE=nom,NUM=sg]
FROM_TEN[CASE=abl,NUM=pl,COUNT=10] -> 'daśabhyaḥ'
BAD[CASE=nom,NUM=sg] -> 'akuśalam'
FOUR_SAME[SEM=<(SuccessorCount(unwholesome_desire,four) & PredecessorCount(obscured_desire,ten) & SuccessorCount(obscured_desire,four))>] -> FROM_THAT[CASE=abl,NUM=sg] FOUR_NUM[CASE=nom,NUM=pl,COUNT=4] OBSC[CASE=nom,NUM=sg] LIKEWISE
FROM_THAT[CASE=abl,NUM=sg] -> 'tasmāt'
FOUR_NUM[CASE=nom,NUM=pl,COUNT=4] -> 'catvāri'
OBSC[CASE=nom,NUM=sg] -> 'nivṛtam'
LIKEWISE -> 'tathā'
```

```nltk-dep
'cittāni' -> 'kāme' | 'nava' | 'śubhāt' | 'cittāt'
'tat' -> 'aṣṭābhyaḥ' | 'eva'
'akuśalam' -> 'daśabhyaḥ'
'nivṛtam' -> 'tasmāt' | 'catvāri' | 'tathā'
```

**Feature chart checkpoints.** The nine-successor phrase spans [0,
5), eight-predecessor phrase [5, 8), ten-predecessor phrase [8, 10),
and four-successor/likewise phrase [10, 14). The root spans [0, 14).
Ablative and numeral features keep predecessor and successor counts
separate.

## 5. Translation

### Literal Translation

> In the desire realm, nine consciousnesses arise after wholesome
> consciousness; that [wholesome mind] arises from eight. The
> unwholesome arises from ten; from it, four [arise]. The obscured is
> likewise.

### Bhāṣya-informed study translation

> In the desire realm, nine kinds of consciousness follow wholesome
> mind, which itself follows eight. Unwholesome mind follows ten and
> is followed by four; obscured mind likewise follows ten and is
> followed by four.

## 6. Philosophical Translation

> Succession is directional: wholesome desire-realm mind has nine
> possible successors and eight predecessors; unwholesome and obscured
> mind each have ten predecessors and four successors. The Bhāṣya
> supplies the kinds behind the first two counts and the conditions
> under which higher-realm kinds can precede desire-realm mind.

## 7. Technical Vocabulary

| Term | Rendering |
|---|---|
| śubha | Wholesome desire-realm mind; nine successors, eight predecessors. |
| akuśala | Unwholesome desire-realm mind; ten predecessors, four successors. |
| nivṛta | Obscured desire-realm mind; the same ten/four pattern. |
| aṣṭābhyaḥ / daśabhyaḥ | From eight / from ten; both mark predecessors. |
| tasmāt | From it; marks successors of the unwholesome. |
| dūratā | Remoteness; four kinds exclude formless wholesome in the Bhāṣya. |

## 8. Logical Determination

**Kārikā, derived.** The root `SEM` keeps successor and predecessor
counts distinct for each kind. The Bhāṣya enumerates the nine and
eight, explains the four remotenesses, and details rebirth and
attainment contexts.

```nltk-sem
nine : SuccessorCount(wholesome_desire,nine)
eight : PredecessorCount(wholesome_desire,eight)
ten : PredecessorCount(unwholesome_desire,ten)
four_same : SuccessorCount(unwholesome_desire,four) & PredecessorCount(obscured_desire,ten) & SuccessorCount(obscured_desire,four)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(SuccessorCount(wholesome_desire,nine) & PredecessorCount(wholesome_desire,eight) & PredecessorCount(unwholesome_desire,ten) & SuccessorCount(unwholesome_desire,four) & PredecessorCount(obscured_desire,ten) & SuccessorCount(obscured_desire,four))

# THEORY prose_nine_successors
# EXPECT prose_nine_successors T
Includes(nine_successors,own_four) & Includes(nine_successors,form_wholesome) & Includes(nine_successors,form_obscured) & Includes(nine_successors,formless_obscured) & Includes(nine_successors,trainee) & Includes(nine_successors,beyond_training)

# THEORY prose_eight_predecessors
# EXPECT prose_eight_predecessors T
Includes(eight_predecessors,own_four) & Includes(eight_predecessors,form_wholesome) & Includes(eight_predecessors,form_obscured) & Includes(eight_predecessors,trainee) & Includes(eight_predecessors,beyond_training)

# THEORY prose_remoteness
# EXPECT prose_remoteness T
Excludes(formless_wholesome,four_remotenesses) & Includes(nine_successors,formless_obscured)

# THEORY rejected_unwholesome_ten_successors
# EXPECT rejected_unwholesome_ten_successors F
PredecessorCount(unwholesome_desire,ten) & SuccessorCount(unwholesome_desire,ten)

# THEORY rejected_formless_wholesome_successor
# EXPECT rejected_formless_wholesome_successor F
Includes(nine_successors,own_four) & Includes(nine_successors,formless_wholesome)
```

```nltk-valuation
wholesome_desire => good_desire
unwholesome_desire => bad_desire
obscured_desire => obscured_desire_kind
nine => nine_count
eight => eight_count
ten => ten_count
four => four_count
nine_successors => nine_group
eight_predecessors => eight_group
own_four => own_four_group
form_wholesome => form_good
form_obscured => form_obscured
formless_obscured => formless_obscured_kind
formless_wholesome => formless_good
trainee => trainee_kind
beyond_training => beyond_kind
four_remotenesses => four_remotenesses_group
SuccessorCount => {(good_desire,nine_count),(bad_desire,four_count),(obscured_desire_kind,four_count)}
PredecessorCount => {(good_desire,eight_count),(bad_desire,ten_count),(obscured_desire_kind,ten_count)}
Includes => {(nine_group,own_four_group),(nine_group,form_good),(nine_group,form_obscured),(nine_group,formless_obscured_kind),(nine_group,trainee_kind),(nine_group,beyond_kind),(eight_group,own_four_group),(eight_group,form_good),(eight_group,form_obscured),(eight_group,trainee_kind),(eight_group,beyond_kind)}
Excludes => {(formless_good,four_remotenesses_group)}
```

The finite valuation witnesses the six directional counts. Removing
any one count falsifies the verse. The prose group memberships are
compressed descriptions of enumerated kinds; *own_four* stands for
four kinds, not one additional kind.

## 9. Interpretive Note

**Translation note.** The Bhāṣya enumerates the nine successors of
wholesome desire-realm mind: four of its own level, Form wholesome at
attainment-entry, Form obscured and formless obscured at rebirth,
and the trainee and beyond-training kinds. Formless wholesome is
excluded by remoteness of support, aspect, object, and counteragent.
The eight predecessors are four of the same level, Form wholesome and
obscured, and the two uncontaminated kinds.

Unwholesome and obscured desire-realm mind can each arise after ten
contaminated kinds, including higher-realm kinds in rebirth contexts;
only four of their own level can immediately follow either one. The
verse states these counts; the Bhāṣya supplies their circumstances.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_67 a vak:Karika ; vak:hasTopic vak:DesireRealmSuccession .
vak:DesireWholesome vak:successorCount 9 ; vak:predecessorCount 8 .
vak:DesireUnwholesome vak:predecessorCount 10 ; vak:successorCount 4 .
vak:DesireObscured vak:predecessorCount 10 ; vak:successorCount 4 .
```
