# VAK_2.53 Bhāṣya — Application and Associated

## 1. Kārikā Anchor

> prayogajās tayor eva śrutacintāmayādikāḥ /
>
> saṃprayuktakahetus tu cittacaittāḥ samāśrayāḥ // 2.53 //

> Application-produced qualities are homogeneous causes of the equal or
> superior only: those born of hearing, thought, and cultivation.
> Associated cause is consciousness and mental factors sharing one
> support.

## 2. Continuous Sanskrit Witness

> prayogajās tayor eva /
> samaviśiṣṭayoḥ sabhāgahetur bhavanti na nyūnasya /
> śrutacintāmayādikāḥ /
> ete hi prāyogikāḥ śrutacintābhāvanāmayā guṇāḥ samaviśiṣṭayor eva hetur nanyūnānām /
> saṃprayuktakahetus tu cittacaittāḥ samāśrayāḥ // 2.53 //

The unit is printed 87.20–88.27 in `Vasubandhu/Sources/kosabhasya.txt`. Defects remain. Not a collation.

## 3. Continuous Conventional Translation

Worldly qualities produced by application are homogeneous causes of the equal or the superior only. Hearing, thought, cultivation, by realm, as each is present. Nine grades, downward in reach as the grade rises. Birth-acquired wholesome, and the afflicted, of one another. Four unobscured-indeterminate, of four, three, two, and one. Effort is not fruitless. Decline is still stated. Prior acquisition is not prior arising. A future dharma is not this cause.

Associated cause requires the same support. Aspect, object, and time are not enough. The new moon is the other-continuum case. Same means non-different: one faculty-moment. Associated is also co-arisen. Not the converse. Five equalities. The associated cause has been explained.

## 4. Interpretation

Application-produced is equal or superior only. Associated is the same support, five equalities. Also co-arisen, not the converse. Same support is non-different, not same kind.

### Grammar of the Bhāṣya determination

This selected proposition at [088|20] supplies the missing numerical force of *samāśrayāḥ*. Sandhi and inflection are normalized for parsing; the quoted witness above remains unchanged. The grammar derives association from the named consciousness/factor pair with identical support, rather than from merely similar support kinds.

```text
# tokens: samānaḥ āśrayaḥ yeṣām te cittacaittāḥ anyonyam saṃprayuktakahetuḥ
```

```nltk-fcfg
% start S
# tokens: samānaḥ āśrayaḥ yeṣām te cittacaittāḥ anyonyam saṃprayuktakahetuḥ
S[SEM=<(SameSupport(citta,caitta) & AssociatedCause(citta,caitta) & AssociatedCause(caitta,citta))>] -> SAME[CASE=nom,NUM=sg,IDENTITY=same] BASIS[CASE=nom,NUM=sg] RELATIVE[CASE=gen,NUM=pl] THEY[CASE=nom,NUM=pl] PAIR[CASE=nom,NUM=pl] RECIPROCAL[CASE=acc,NUM=sg] CAUSE[CASE=nom,NUM=sg]
SAME[CASE=nom,NUM=sg,IDENTITY=same] -> 'samānaḥ'
BASIS[CASE=nom,NUM=sg] -> 'āśrayaḥ'
RELATIVE[CASE=gen,NUM=pl] -> 'yeṣām'
THEY[CASE=nom,NUM=pl] -> 'te'
PAIR[CASE=nom,NUM=pl] -> 'cittacaittāḥ'
RECIPROCAL[CASE=acc,NUM=sg] -> 'anyonyam'
CAUSE[CASE=nom,NUM=sg] -> 'saṃprayuktakahetuḥ'
```

```nltk-dep
'saṃprayuktakahetuḥ' -> 'samānaḥ' | 'āśrayaḥ' | 'yeṣām' | 'te' | 'cittacaittāḥ' | 'anyonyam'
```

### Logic of the Bhāṣya argument

The source moves through objections: common aspect/object, then common time, then the different-continuum counterexample, before requiring the identical support moment at [088|20–22]. The five equalities and the relation to co-arisen cause are stated at [088|22–26]. The finite theories make those steps testable; they are not asserted to be an exhaustive parse of the full, uncollated prose unit.

```nltk-sem
association : SameSupport(citta,caitta) & AssociatedCause(citta,caitta) & AssociatedCause(caitta,citta)
```

```nltk-fol
# THEORY bhasya_association
# EXPECT bhasya_association T
SameSupport(citta,caitta) & AssociatedCause(citta,caitta) & AssociatedCause(caitta,citta)

# THEORY bhasya_shared_descriptions_insufficient
# EXPECT bhasya_shared_descriptions_insufficient T
SameAspect(citta,other_caitta) & SameObject(citta,other_caitta) & SameTime(citta,other_caitta) & -SameSupport(citta,other_caitta) & -AssociatedCause(citta,other_caitta)

# THEORY bhasya_five_equalities
# EXPECT bhasya_five_equalities T
FiveEqualities(citta,caitta) & SameSupport(citta,caitta)

# THEORY bhasya_cause_relation
# EXPECT bhasya_cause_relation T
all x.all y.(AssociatedCause(x,y) -> CoarisenCause(x,y)) & CoarisenCause(citta,caitta)

# THEORY rejected_shared_descriptions_suffice
# EXPECT rejected_shared_descriptions_suffice F
AssociatedCause(citta,other_caitta) & SameAspect(citta,other_caitta) & SameObject(citta,other_caitta)

# THEORY rejected_coarisen_converse
# EXPECT rejected_coarisen_converse F
all x.all y.(CoarisenCause(x,y) -> AssociatedCause(x,y))
```

```nltk-valuation
citta => consciousness
caitta => mental_factor
other_caitta => other_continuum_factor
mark => group_mark
SameSupport => {(consciousness,mental_factor)}
AssociatedCause => {(consciousness,mental_factor),(mental_factor,consciousness)}
SameAspect => {(consciousness,mental_factor),(consciousness,other_continuum_factor)}
SameObject => {(consciousness,mental_factor),(consciousness,other_continuum_factor)}
SameTime => {(consciousness,mental_factor),(consciousness,other_continuum_factor)}
FiveEqualities => {(consciousness,mental_factor)}
CoarisenCause => {(consciousness,mental_factor),(mental_factor,consciousness),(consciousness,group_mark)}
```

The first rejected theory tests the Bhāṣya's different-continuum objection. The second records its one-way implication: associated causes are co-arisen causes, while a co-arisen causal pair need not be associated. The source invokes five equalities without enumerating them in this unit; the model records that claim while testing identity of support separately.

## 5. Review Status

Grammar and Logic pass added for the selected [088|20] Bhāṣya proposition and its surrounding argument. The continuous Sanskrit witness remains partial and uncollated; the fuller source unit and disputed readings still need editorial review. The pervasive cause is next.
