# VAK_2.55 — Times of the Causes

## 1. Sanskrit (Devanāgarī)

```sanskrit
सर्वत्रगः सभागश्च द्वयध्वगौ त्र्यध्वगास्त्रयः ।
संस्कृतं सविसंयोगं फलं नासंस्कृतस्य ते ॥ २.५५ ॥
```

## 2. Sanskrit (IAST)

```text
sarvatragaḥ sabhāgaś ca dvayadhvagau tryadhvagās trayaḥ /
saṃskṛtaṃ savisaṃyogaṃ phalaṃ nāsaṃskṛtasya te // 2.55 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sarvatragaḥ sabhāgaḥ | masculine nominative singular cause names | pervasive and homogeneous causes |
| dvayadhvagau | masculine nominative dual compound adjective | the two causes occur in past and present, as the Bhāṣya specifies |
| tryadhvagāḥ trayaḥ | masculine nominative plural compound adjective + numeral | three causes range over all three times; the Bhāṣya names them |
| saṃskṛtam | neuter nominative singular substantive | conditioned dharma as fruit |
| savisaṃyogam | neuter nominative singular compound | with disconnection included among fruits |
| phalam | neuter nominative singular | fruit |
| na asaṃskṛtasya te | negative particle + genitive singular + nominative dual pronoun | cause and fruit do not belong to an unconditioned dharma, as the Bhāṣya resolves *te* |

**Grammar tokens.** External sandhi is opened at *sabhāgaś ca*, *tryadhvagās trayaḥ*, and *nāsaṃskṛtasya*. The Bhāṣya supplies which two times and which three causes are meant. The final dual *te* resumes cause and fruit, not the previously named three causes.

```text
# tokens: sarvatragaḥ sabhāgaḥ ca dvayadhvagau tryadhvagāḥ trayaḥ saṃskṛtam savisaṃyogam phalam na asaṃskṛtasya te
```

## 4. Grammar

```nltk-fcfg
% start S
# tokens: sarvatragaḥ sabhāgaḥ ca dvayadhvagau tryadhvagāḥ trayaḥ saṃskṛtam savisaṃyogam phalam na asaṃskṛtasya te
S[SEM=<(?two & ?three & ?fruits & ?exclusion)>] -> TWO[SEM=?two] THREE[SEM=?three] FRUITS[SEM=?fruits] EXCLUSION[SEM=?exclusion]
TWO[SEM=<(TimeOf(pervasive,past) & TimeOf(pervasive,present) & TimeOf(homogeneous,past) & TimeOf(homogeneous,present))>] -> PERVASIVE[CASE=nom,NUM=sg] HOMOGENEOUS[CASE=nom,NUM=sg] AND TWO_TIMES[CASE=nom,NUM=du,COUNT=2]
PERVASIVE[CASE=nom,NUM=sg] -> 'sarvatragaḥ'
HOMOGENEOUS[CASE=nom,NUM=sg] -> 'sabhāgaḥ'
AND -> 'ca'
TWO_TIMES[CASE=nom,NUM=du,COUNT=2] -> 'dvayadhvagau'
THREE[SEM=<(ThreeTimes(coarisen) & ThreeTimes(associated) & ThreeTimes(maturation))>] -> THREE_TIMES[CASE=nom,NUM=pl,COUNT=3] COUNT_THREE[CASE=nom,NUM=pl,COUNT=3]
THREE_TIMES[CASE=nom,NUM=pl,COUNT=3] -> 'tryadhvagāḥ'
COUNT_THREE[CASE=nom,NUM=pl,COUNT=3] -> 'trayaḥ'
FRUITS[SEM=<(Fruit(conditioned) & Fruit(disconnection))>] -> CONDITIONED[CASE=nom,NUM=sg] WITH_DISCONNECTION[CASE=nom,NUM=sg] FRUIT[CASE=nom,NUM=sg]
CONDITIONED[CASE=nom,NUM=sg] -> 'saṃskṛtam'
WITH_DISCONNECTION[CASE=nom,NUM=sg] -> 'savisaṃyogam'
FRUIT[CASE=nom,NUM=sg] -> 'phalam'
EXCLUSION[SEM=<(-HasCause(unconditioned) & -HasFruit(unconditioned))>] -> NEG UNCONDITIONED[CASE=gen,NUM=sg] BOTH[CASE=nom,NUM=du,REF=cause_fruit]
NEG -> 'na'
UNCONDITIONED[CASE=gen,NUM=sg] -> 'asaṃskṛtasya'
BOTH[CASE=nom,NUM=du,REF=cause_fruit] -> 'te'
```

```nltk-dep
'dvayadhvagau' -> 'sarvatragaḥ' | 'sabhāgaḥ' | 'ca'
'trayaḥ' -> 'tryadhvagāḥ'
'phalam' -> 'saṃskṛtam' | 'savisaṃyogam'
'te' -> 'na' | 'asaṃskṛtasya'
```

**Feature chart checkpoints.** The two-cause group spans [0, 4), the three-cause group [4, 6), fruits [6, 9), and the dual exclusion [9, 12). The root spans [0, 12). The dual `te` is bound to `cause_fruit`; changing it to a plural three-cause reference blocks the parse.

## 5. Translation

### Literal Translation

> The pervasive and homogeneous range over two times; three causes range
> over three. The conditioned, together with disconnection, is fruit;
> cause and fruit do not belong to an unconditioned dharma.
### Bhāṣya-informed study translation

> The pervasive and homogeneous causes occur in past and present; the
> co-arisen, associated, and maturation causes occur in all three times.
> Conditioned dharmas and disconnection count as fruits; an unconditioned
> dharma has neither cause nor fruit.

## 6. Philosophical Translation

> The causal series is classified by temporal range. Conditioned dharmas and disconnection count as fruits, yet an unconditioned dharma does not itself enter the six-cause/five-fruit relation as a possessor of cause or fruit. The Bhāṣya must therefore explain how the Path leads to disconnection without producing it.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| adhvan | time | past, present, future |
| visaṃyoga | disconnection | counted as fruit; the Path brings one to it without producing it |
| pratisaṃkhyā | Discrimination | the cessation's name |
| prapaṇa | bringing to | Bhāṣya term for the Path’s relation to disconnection, distinct from producing acquisition |
| prāpti | acquisition | what is produced |

## 8. Logical Determination

**Kārikā, derived.** The root `SEM` distinguishes the two-time and three-time cause groups, includes disconnection among fruits, and denies cause and fruit *of* an unconditioned dharma. The conditioning cause's unrestricted temporal range and the Path/acquisition/disconnection explanation are Bhāṣya determinations, modeled separately.

```nltk-sem
two : TimeOf(pervasive,past) & TimeOf(pervasive,present) & TimeOf(homogeneous,past) & TimeOf(homogeneous,present)
three : ThreeTimes(coarisen) & ThreeTimes(associated) & ThreeTimes(maturation)
fruits : Fruit(conditioned) & Fruit(disconnection)
exclusion : -HasCause(unconditioned) & -HasFruit(unconditioned)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(TimeOf(pervasive,past) & TimeOf(pervasive,present) & TimeOf(homogeneous,past) & TimeOf(homogeneous,present)) & (ThreeTimes(coarisen) & ThreeTimes(associated) & ThreeTimes(maturation)) & (Fruit(conditioned) & Fruit(disconnection)) & (-HasCause(unconditioned) & -HasFruit(unconditioned))

# THEORY prose_conditioning_range
# EXPECT prose_conditioning_range T
TimeOf(conditioning,past) & TimeOf(conditioning,present) & TimeOf(conditioning,future) & OutsideTime(conditioning)

# THEORY prose_path_distinction
# EXPECT prose_path_distinction T
Produces(path,acquisition) & BringsTo(path,disconnection) & -Produces(path,disconnection)

# THEORY rejected_future_homogeneous
# EXPECT rejected_future_homogeneous F
TimeOf(homogeneous,future) & TimeOf(homogeneous,present)

# THEORY rejected_three_are_two
# EXPECT rejected_three_are_two F
-ThreeTimes(maturation) & ThreeTimes(coarisen)

# THEORY rejected_disconnection_produced
# EXPECT rejected_disconnection_produced F
Produces(path,disconnection) & BringsTo(path,disconnection)

# THEORY rejected_unconditioned_has_cause
# EXPECT rejected_unconditioned_has_cause F
HasCause(unconditioned) & Fruit(disconnection)
```

```nltk-valuation
pervasive => pv
homogeneous => hg
coarisen => co
associated => as
maturation => ma
conditioning => cn
past => pa
present => pr
future => fu
conditioned => cd
disconnection => dc
unconditioned => uc
path => pt
acquisition => aq
TimeOf => {(pv,pa),(pv,pr),(hg,pa),(hg,pr),(cn,pa),(cn,pr),(cn,fu)}
ThreeTimes => {co,as,ma}
Fruit => {cd,dc}
HasCause => {}
HasFruit => {}
OutsideTime => {cn}
Produces => {(pt,aq)}
BringsTo => {(pt,dc)}
```

The finite valuation tests the intended temporal memberships and the difference between a fruit *being* disconnection and an unconditioned dharma *having* a cause or fruit. The Path's relation to disconnection is a Bhāṣya explanation. The wider debate over whether the unconditioned is an entity or absence remains attributed and open.

## 9. Interpretive Note

The Bhāṣya names pervasive and homogeneous causes as past or present, and co-arisen, associated, and maturation causes as belonging to all three times. The conditioning cause is described separately as occurring across all times and as dissociated from time. The verse calls conditioned dharmas and disconnection fruits, then denies cause and fruit *of* an unconditioned dharma. The Bhāṣya explicitly resolves *te* as the cause-and-fruit pair; this prevents “those causes are not fruits” from reversing the grammar.

The Bhāṣya calls disconnection cessation through discriminative comprehension. It says the Path produces acquisition but brings one to disconnection; the Path is not a productive cause of disconnection. Subsequent objections dispute how the unconditioned can be called a fruit, or a nonobstructing cause, and whether disconnection is an entity or an absence. Those positions remain attributed. The assignment of individual fruits to causes starts in 2.56.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_55 a vak:Karika ; vak:hasTopic vak:TemporalScope .
vak:Disconnection vak:produced false .
```
