# VAK_2.68 — Desire Unobscured and Form Wholesome

## 1. Sanskrit (Devanāgarī)

```sanskrit
पञ्चभ्योऽनिवृतं तस्मात्सप्त चित्तान्यनन्तरम् /
रूपे दशैकं च शुभात् नवभ्यस्तदनन्तरम् // २.६८ //
```

## 2. Sanskrit (IAST)

```text
pañcabhyo 'nivṛtaṃ tasmāt sapta cittāny anantaram /
rūpe daśaikaṃ ca śubhāt navabhyas tadanantaram // 2.68 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| pañcabhyaḥ | abl. pl. numeral | From five predecessor kinds. |
| anivṛtam | n. nom. sg. | Unobscured-indeterminate mind in desire. |
| tasmāt | abl. sg. | From that mind. |
| sapta | numeral | Seven successors. |
| cittāni | n. nom. pl. | Minds or consciousnesses. |
| anantaram | adverb | Immediately after. |
| rūpe | loc. sg. | In the Form realm. |
| daśaikam | n. nom. sg. numeral compound | Eleven. |
| ca | conjunction | And. |
| śubhāt | abl. sg. | From wholesome Form-realm mind. |
| navabhyaḥ | abl. pl. numeral | From nine predecessor kinds. |
| tadanantaram | adverb | Immediately after those; resumes the wholesome mind. |

The [running witness](../../Sources/kosabhasya.txt) reads
*pañcabhyo 'nivṛtaṃ tasmāt sapta cittāny anantaram* in two
fragments. The former Organon verse reordered that line and omitted
*tasmāt*. The normalized tokens open the sandhi in *cittāny
anantaram* and *navabhyas tadanantaram*.

```text
# tokens: pañcabhyaḥ anivṛtam tasmāt sapta cittāni anantaram rūpe daśaikam ca śubhāt navabhyaḥ tadanantaram
```

## 4. Grammar

Desire-realm unobscured mind follows five kinds, and seven minds
follow it. In the Form realm, eleven follow wholesome mind, which
itself follows nine. The Bhāṣya enumerates and qualifies the
successor and predecessor sets.

```nltk-fcfg
% start S
# tokens: pañcabhyaḥ anivṛtam tasmāt sapta cittāni anantaram rūpe daśaikam ca śubhāt navabhyaḥ tadanantaram
S[SEM=<(?five & ?seven & ?eleven & ?nine)>] -> FIVE[SEM=?five] SEVEN[SEM=?seven] ELEVEN[SEM=?eleven] NINE[SEM=?nine]
FIVE[SEM=<PredecessorCount(unobscured_desire,five)>] -> FROM_FIVE[CASE=abl,NUM=pl,COUNT=5] UNOBSC[CASE=nom,NUM=sg]
FROM_FIVE[CASE=abl,NUM=pl,COUNT=5] -> 'pañcabhyaḥ'
UNOBSC[CASE=nom,NUM=sg] -> 'anivṛtam'
SEVEN[SEM=<SuccessorCount(unobscured_desire,seven)>] -> FROM_THAT[CASE=abl,NUM=sg] SEVEN_NUM[COUNT=7] MINDS[CASE=nom,NUM=pl] AFTER
FROM_THAT[CASE=abl,NUM=sg] -> 'tasmāt'
SEVEN_NUM[COUNT=7] -> 'sapta'
MINDS[CASE=nom,NUM=pl] -> 'cittāni'
AFTER -> 'anantaram'
ELEVEN[SEM=<SuccessorCount(form_wholesome,eleven)>] -> IN_FORM[CASE=loc,NUM=sg] ELEVEN_NUM[CASE=nom,NUM=sg,COUNT=11] AND FROM_GOOD[CASE=abl,NUM=sg]
IN_FORM[CASE=loc,NUM=sg] -> 'rūpe'
ELEVEN_NUM[CASE=nom,NUM=sg,COUNT=11] -> 'daśaikam'
AND -> 'ca'
FROM_GOOD[CASE=abl,NUM=sg] -> 'śubhāt'
NINE[SEM=<PredecessorCount(form_wholesome,nine)>] -> FROM_NINE[CASE=abl,NUM=pl,COUNT=9] AFTER_THAT
FROM_NINE[CASE=abl,NUM=pl,COUNT=9] -> 'navabhyaḥ'
AFTER_THAT -> 'tadanantaram'
```

```nltk-dep
'anivṛtam' -> 'pañcabhyaḥ'
'cittāni' -> 'tasmāt' | 'sapta' | 'anantaram'
'daśaikam' -> 'rūpe' | 'ca' | 'śubhāt'
'navabhyaḥ' -> 'tadanantaram'
```

**Feature chart checkpoints.** Five predecessors span [0, 2), seven
successors [2, 6), eleven successors [6, 10), and nine predecessors
[10, 12); the root spans [0, 12). The ablatives mark sources of
arising, while the nominative numerals mark successor counts.

## 5. Translation

### Literal Translation

> The unobscured [mind] arises from five; immediately after it, seven
> minds [arise]. In the Form realm, eleven [arise] after the wholesome;
> it, in turn, arises immediately after nine.

### Bhāṣya-informed study translation

> Desire-realm unobscured-indeterminate mind follows five kinds, and
> seven follow it. In the Form realm, eleven kinds follow wholesome
> mind, which itself follows nine.

## 6. Philosophical Translation

> The verse extends the directed succession matrix from 2.67. The
> Bhāṣya identifies the five predecessors and seven successors of
> desire unobscured, then excludes formless unobscured from the
> successors and predecessors relevant to Form wholesome.

## 7. Technical Vocabulary

| Term | Rendering |
|---|---|
| anivṛta | Unobscured-indeterminate desire-realm mind; five predecessors, seven successors. |
| śubha | Wholesome Form-realm mind; eleven successors, nine predecessors. |
| nirmāṇa-citta | Creation mind; a desire-realm unobscured successor of Form wholesome. |
| tasmāt | From it; points back to desire unobscured mind. |
| tadanantaram | Immediately after those; points back to Form wholesome as arising mind. |

## 8. Logical Determination

**Kārikā, derived.** The root `SEM` records four directed counts.
The identities of their members, the creation-mind example, and the
exclusion of formless unobscured are Bhāṣya determinations.

```nltk-sem
five : PredecessorCount(unobscured_desire,five)
seven : SuccessorCount(unobscured_desire,seven)
eleven : SuccessorCount(form_wholesome,eleven)
nine : PredecessorCount(form_wholesome,nine)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(PredecessorCount(unobscured_desire,five) & SuccessorCount(unobscured_desire,seven) & SuccessorCount(form_wholesome,eleven) & PredecessorCount(form_wholesome,nine))

# THEORY prose_five_predecessors
# EXPECT prose_five_predecessors T
Includes(five_predecessors,own_four) & Includes(five_predecessors,form_wholesome)

# THEORY prose_seven_successors
# EXPECT prose_seven_successors T
Includes(seven_successors,own_four) & Includes(seven_successors,form_wholesome) & Includes(seven_successors,form_obscured) & Includes(seven_successors,formless_obscured)

# THEORY prose_form_wholesome_exclusions
# EXPECT prose_form_wholesome_exclusions T
SuccessorCount(form_wholesome,eleven) & -Includes(eleven_successors,formless_unobscured) & PredecessorCount(form_wholesome,nine) & -Includes(nine_predecessors,formless_unobscured)

# THEORY rejected_formless_unobscured_successor
# EXPECT rejected_formless_unobscured_successor F
SuccessorCount(form_wholesome,eleven) & Includes(eleven_successors,formless_unobscured)

# THEORY rejected_counts_reversed
# EXPECT rejected_counts_reversed F
PredecessorCount(unobscured_desire,seven) & SuccessorCount(unobscured_desire,five)
```

```nltk-valuation
unobscured_desire => unobsc_des
form_wholesome => form_good
five => five_count
seven => seven_count
eleven => eleven_count
nine => nine_count
five_predecessors => five_group
seven_successors => seven_group
eleven_successors => eleven_group
nine_predecessors => nine_group
own_four => own_four_group
form_obscured => form_obscured_kind
formless_obscured => formless_obscured_kind
formless_unobscured => formless_unobscured_kind
PredecessorCount => {(unobsc_des,five_count),(form_good,nine_count)}
SuccessorCount => {(unobsc_des,seven_count),(form_good,eleven_count)}
Includes => {(five_group,own_four_group),(five_group,form_good),(seven_group,own_four_group),(seven_group,form_good),(seven_group,form_obscured_kind),(seven_group,formless_obscured_kind)}
```

The finite valuation witnesses all four directed counts. Removing
any one count falsifies the verse. The prose groups compress the
Bhāṣya's enumerations; *own_four* stands for four kinds, not one
additional kind.

## 9. Interpretive Note

**Translation note.** The five predecessors of desire unobscured are
its four own-level kinds and Form wholesome, from which creation
mind can arise. Seven successors are the four own-level kinds, Form
wholesome after creation mind, and Form and formless obscured at
rebirth-linking. Eleven follow Form wholesome except formless
unobscured-indeterminate. Its nine predecessors exclude the two
afflicted desire kinds and formless unobscured-indeterminate.

The verse states the four counts; the Bhāṣya explains their membership
and contexts. The next verse takes up Form obscured and unobscured.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_68 a vak:Karika ; vak:hasTopic vak:UnobscuredAndFormWholesome .
vak:DesireUnobscured vak:predecessorCount 5 ; vak:successorCount 7 .
vak:FormWholesome vak:successorCount 11 ; vak:predecessorCount 9 .
```
