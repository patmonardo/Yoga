# VAK_2.70 — Formless and Uncontaminated Succession

## 1. Sanskrit (Devanāgarī)

```sanskrit
नव चित्तानि तत् षण्णां निवृतात्सप्त तत्तथा /
चतुर्भ्यः शैक्षमस्मात्तु पञ्च अशैक्षं तु पञ्चकात् // २.७० //
```

## 2. Sanskrit (IAST)

```text
nava cittāni tat ṣaṇṇāṃ nivṛtāt sapta tat tathā /
caturbhyaḥ śaikṣam asmāt tu pañca aśaikṣaṃ tu pañcakāt // 2.70 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| nava | numeral | Nine successor consciousnesses from the formless wholesome named in 2.69. |
| cittāni | n. nom. pl. | Consciousnesses. |
| tat | n. nom. sg. pronoun | That formless wholesome mind, then that obscured mind. |
| ṣaṇṇām | gen. pl. numeral | Of six predecessor kinds. |
| nivṛtāt | abl. sg. | From formless obscured mind. |
| sapta | numeral | Seven successor kinds. |
| tathā | adverb | Likewise; carries seven to predecessors of obscured. |
| caturbhyaḥ | abl. pl. numeral | From four predecessor kinds. |
| śaikṣam | n. nom. sg. | Trainee mind. |
| asmāt | abl. sg. | From this trainee mind. |
| tu | particle | Then or but; distinguishes the next relation. |
| pañca | numeral | Five successors. |
| aśaikṣam | n. nom. sg. | Beyond-training mind. |
| pañcakāt | abl. sg. collective numeral | From the five-member predecessor group. |

The [running witness](../../Sources/kosabhasya.txt) prints the verse
in seven fragments, beginning after 2.69's *śubhāt punaḥ*. The
former Organon file substituted *tasmāt ṣaḍbhiḥ* for *tat ṣaṇṇām*
and *tad eva* for *tat tathā*. The normalized tokens open sandhi but
retain the witnessed genitive *ṣaṇṇām*.

```text
# tokens: nava cittāni tat ṣaṇṇām nivṛtāt sapta tat tathā caturbhyaḥ śaikṣam asmāt tu pañca aśaikṣam tu pañcakāt
```

## 4. Grammar

Nine minds follow formless wholesome, which itself follows six.
Seven follow formless obscured, which likewise follows seven.
Trainee mind follows four and has five successors. Beyond-training
mind follows the group of five. The Bhāṣya then states that four
follow beyond-training; that count lies outside this kārikā's words.

```nltk-fcfg
% start S
# tokens: nava cittāni tat ṣaṇṇām nivṛtāt sapta tat tathā caturbhyaḥ śaikṣam asmāt tu pañca aśaikṣam tu pañcakāt
S[SEM=<(?nine & ?six & ?seven_s & ?seven_p & ?four & ?five_s & ?five_p)>] -> NINE[SEM=?nine] SIX[SEM=?six] SEVEN_S[SEM=?seven_s] SEVEN_P[SEM=?seven_p] FOUR[SEM=?four] FIVE_S[SEM=?five_s] FIVE_P[SEM=?five_p]
NINE[SEM=<SuccessorCount(formless_wholesome,nine)>] -> NINE_NUM[COUNT=9] MINDS[CASE=nom,NUM=pl]
NINE_NUM[COUNT=9] -> 'nava'
MINDS[CASE=nom,NUM=pl] -> 'cittāni'
SIX[SEM=<PredecessorCount(formless_wholesome,six)>] -> THAT1[CASE=nom,NUM=sg] OF_SIX[CASE=gen,NUM=pl,COUNT=6]
THAT1[CASE=nom,NUM=sg] -> 'tat'
OF_SIX[CASE=gen,NUM=pl,COUNT=6] -> 'ṣaṇṇām'
SEVEN_S[SEM=<SuccessorCount(formless_obscured,seven)>] -> FROM_OBSC[CASE=abl,NUM=sg] SEVEN_NUM[COUNT=7]
FROM_OBSC[CASE=abl,NUM=sg] -> 'nivṛtāt'
SEVEN_NUM[COUNT=7] -> 'sapta'
SEVEN_P[SEM=<PredecessorCount(formless_obscured,seven)>] -> THAT2[CASE=nom,NUM=sg] LIKEWISE
THAT2[CASE=nom,NUM=sg] -> 'tat'
LIKEWISE -> 'tathā'
FOUR[SEM=<PredecessorCount(trainee,four)>] -> FROM_FOUR[CASE=abl,NUM=pl,COUNT=4] TRAINEE[CASE=nom,NUM=sg]
FROM_FOUR[CASE=abl,NUM=pl,COUNT=4] -> 'caturbhyaḥ'
TRAINEE[CASE=nom,NUM=sg] -> 'śaikṣam'
FIVE_S[SEM=<SuccessorCount(trainee,five)>] -> FROM_THIS[CASE=abl,NUM=sg] BUT1 FIVE_NUM[COUNT=5]
FROM_THIS[CASE=abl,NUM=sg] -> 'asmāt'
BUT1 -> 'tu'
FIVE_NUM[COUNT=5] -> 'pañca'
FIVE_P[SEM=<PredecessorCount(beyond_training,five)>] -> BEYOND[CASE=nom,NUM=sg] BUT2 FROM_FIVE[CASE=abl,NUM=sg,COUNT=5]
BEYOND[CASE=nom,NUM=sg] -> 'aśaikṣam'
BUT2 -> 'tu'
FROM_FIVE[CASE=abl,NUM=sg,COUNT=5] -> 'pañcakāt'
```

```nltk-dep
'cittāni' -> 'nava'
'tat' -> 'ṣaṇṇām' | 'tathā'
'sapta' -> 'nivṛtāt'
'śaikṣam' -> 'caturbhyaḥ'
'pañca' -> 'asmāt' | 'tu'
'aśaikṣam' -> 'tu' | 'pañcakāt'
```

**Feature chart checkpoints.** The seven fragments span [0, 2),
[2, 4), [4, 6), [6, 8), [8, 10), [10, 13), and [13, 16); the
root spans [0, 16). Genitive *ṣaṇṇām* and ablatives
*caturbhyaḥ/pañcakāt* constrain predecessor counts. The
beyond-training successor count is not in this verse.

## 5. Translation

### Literal Translation

> Nine consciousnesses [follow formless wholesome]; that [mind arises]
> after six. Seven follow the obscured; it likewise
> [follows seven]. Trainee [mind] follows four; from it, five [follow].
> Beyond-training [mind] follows the group of five.

### Bhāṣya-informed study translation

> Nine minds follow formless wholesome, which follows six. Seven
> follow formless obscured, which likewise follows seven. Trainee mind
> follows four and is followed by five; beyond-training follows that
> group of five.

## 6. Philosophical Translation

> The verse finishes the directional counts for formless wholesome,
> formless obscured, trainee, and beyond-training mind. Its final
> count is five predecessors of beyond-training. The Bhāṣya continues
> with four successors of beyond-training and closes the twelve-kind
> inventory.

## 7. Technical Vocabulary

| Term | Rendering |
|---|---|
| ṣaṇṇām | Of six; predecessor count for formless wholesome. |
| śaikṣa | Trainee mind; four predecessors, five successors. |
| aśaikṣa | Beyond-training mind; five predecessors in the verse. |
| pañcaka | Group of five predecessors; four leading to trainee plus beyond-training. |
| tathā | Likewise; transfers seven to formless obscured's predecessors. |

## 8. Logical Determination

**Kārikā, derived.** The root `SEM` records seven directed counts.
The identities of the groups, beyond-training's four successors, and
the closure of the twelve-kind inventory are in the Bhāṣya
continuation. The verse itself has no beyond-training successor count.

```nltk-sem
formless_wholesome_successors : SuccessorCount(formless_wholesome,nine)
formless_wholesome_predecessors : PredecessorCount(formless_wholesome,six)
formless_obscured_successors : SuccessorCount(formless_obscured,seven)
formless_obscured_predecessors : PredecessorCount(formless_obscured,seven)
trainee_predecessors : PredecessorCount(trainee,four)
trainee_successors : SuccessorCount(trainee,five)
beyond_predecessors : PredecessorCount(beyond_training,five)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(SuccessorCount(formless_wholesome,nine) & PredecessorCount(formless_wholesome,six) & SuccessorCount(formless_obscured,seven) & PredecessorCount(formless_obscured,seven) & PredecessorCount(trainee,four) & SuccessorCount(trainee,five) & PredecessorCount(beyond_training,five))

# THEORY prose_formless_wholesome
# EXPECT prose_formless_wholesome T
Includes(nine_successors,own_three) & Includes(nine_successors,form_wholesome) & Includes(nine_successors,form_obscured) & Includes(nine_successors,afflicted_desire_two) & Includes(nine_successors,trainee) & Includes(nine_successors,beyond_training) & Includes(six_predecessors,own_three) & Includes(six_predecessors,form_wholesome)

# THEORY prose_formless_obscured
# EXPECT prose_formless_obscured T
Includes(seven_successors,own_three) & Includes(seven_successors,form_wholesome) & Includes(seven_successors,form_obscured) & Includes(seven_successors,afflicted_desire_two)

# THEORY prose_trainee_and_beyond
# EXPECT prose_trainee_and_beyond T
Includes(four_predecessors,realm_wholesome_three) & Includes(four_predecessors,trainee) & Includes(five_successors,four_plus_beyond) & SuccessorCount(beyond_training,four)

# THEORY rejected_beyond_five_successors
# EXPECT rejected_beyond_five_successors F
PredecessorCount(beyond_training,five) & SuccessorCount(beyond_training,five)

# THEORY rejected_formless_wholesome_six_successors
# EXPECT rejected_formless_wholesome_six_successors F
PredecessorCount(formless_wholesome,six) & SuccessorCount(formless_wholesome,six)
```

```nltk-valuation
formless_wholesome => formless_good
formless_obscured => formless_obscured_kind
trainee => trainee_kind
beyond_training => beyond_kind
nine => nine_count
six => six_count
seven => seven_count
four => four_count
five => five_count
nine_successors => nine_group
six_predecessors => six_group
seven_successors => seven_group
four_predecessors => four_group
five_successors => five_group
own_three => own_three_group
form_wholesome => form_good
form_obscured => form_obscured_kind
afflicted_desire_two => desire_afflicted_pair
realm_wholesome_three => realm_good_triple
four_plus_beyond => four_plus_beyond_group
SuccessorCount => {(formless_good,nine_count),(formless_obscured_kind,seven_count),(trainee_kind,five_count),(beyond_kind,four_count)}
PredecessorCount => {(formless_good,six_count),(formless_obscured_kind,seven_count),(trainee_kind,four_count),(beyond_kind,five_count)}
Includes => {(nine_group,own_three_group),(nine_group,form_good),(nine_group,form_obscured_kind),(nine_group,desire_afflicted_pair),(nine_group,trainee_kind),(nine_group,beyond_kind),(six_group,own_three_group),(six_group,form_good),(seven_group,own_three_group),(seven_group,form_good),(seven_group,form_obscured_kind),(seven_group,desire_afflicted_pair),(four_group,realm_good_triple),(four_group,trainee_kind),(five_group,four_plus_beyond_group)}
```

The finite valuation witnesses the seven verse counts. It also
records the Bhāṣya continuation's four successors of beyond-training;
that relation is tested as prose and is absent from the verse `SEM`.

## 9. Interpretive Note

**Translation note.** Nine kinds follow formless wholesome, with
desire wholesome and the desire and Form unobscured kinds excluded.
It follows six: three of its own level, Form wholesome, trainee, and
beyond-training. Seven follow formless obscured: its own three, Form
wholesome and obscured, and two afflicted desire kinds. Seven also
precede it. Trainee follows the three realm-wholesome kinds and
itself; five follow it, those four plus beyond-training.

Beyond-training follows that five-member group. The subsequent prose
says four follow beyond-training and declares the twelve-kind
inventory complete. Those are not extra words in the kārikā.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_70 a vak:Karika ; vak:hasTopic vak:FormlessAndUncontaminatedSuccession .
vak:FormlessWholesome vak:successorCount 9 ; vak:predecessorCount 6 .
vak:FormlessObscured vak:successorCount 7 ; vak:predecessorCount 7 .
vak:Trainee vak:predecessorCount 4 ; vak:successorCount 5 .
vak:BeyondTraining vak:predecessorCount 5 .
```
