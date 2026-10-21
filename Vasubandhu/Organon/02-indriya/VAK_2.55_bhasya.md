# VAK_2.55 Bhāṣya — Times and Disconnection

## 1. Kārikā Anchor

> sarvatragaḥ sabhāgaś ca dvayadhvagau tryadhvagās trayaḥ /
>
> saṃskṛtaṃ savisaṃyogaṃ phalaṃ nāsaṃskṛtasya te // 2.55 //

> The pervasive and homogeneous causes occur in past and present; the
> co-arisen, associated, and maturation causes occur in all three times.
> Conditioned dharmas and disconnection count as fruits; an unconditioned
> dharma has neither cause nor fruit.

## 2. Sanskrit Witness — Selected Passages

> sarvatragaḥ sabhāgaś ca dvayadhvagau /
> atītapratyutpannāv eva anāgatau na staḥ /
> tryadhvagās trayaḥ /
> sahabhūsaṃprayuktakavipākahetavas trikālāḥ /
> saṃskṛtaṃ savisaṃyogaṃ phalaṃ /
> phalaṃ dharmāḥ /
> katame /
> saṃskṛtā dharmāḥ pratisaṃkhyānirodhaś ceti śāstram /
> nāsaṃskṛtasya te // 2.55 //
> saṃskṛtasyaiva dharmasya hetuphale bhavataḥ /
> utpādanāt / kathaṃ visaṃyoge / prapaṇāt /
> tasmānna tāvadasya mārgaḥ kathañcidapi hetuḥ /
> phalaṃ cāsya visaṃyogaḥ /

These are selected lines from 90.23–92.22 in
[the running witness](../../Sources/kosabhasya.txt), not a complete
transcription or collation. The [091|04] sentence resolves the dual
*te* as cause and fruit. The [091|11–12] lines distinguish producing
acquisition from bringing to disconnection; they retain the source's
claim that the Path is not a productive cause of disconnection.

## 3. Conventional Argument Summary

Pervasive and homogeneous are past and present. Co-arisen, associated, and maturation are three times. The conditioning cause is all times and dissociated from time. The fruit is the conditioned and cessation by Discrimination. Cause and fruit belong only to a conditioned dharma in that matrix, although disconnection is itself counted among fruits. The Path produces the acquisition and brings one to disconnection. It is not the cause of disconnection. Entity or absence is disputed. Gone, for now.

## 4. Interpretation

A fruit need not be a product: the Path produces acquisition and brings one to disconnection without producing disconnection. The phrase *na asaṃskṛtasya te* denies cause and fruit belonging to an unconditioned dharma, while *savisaṃyogam phalam* includes disconnection among fruits. The objections about its ontological status remain attributed.

### Grammar of the Bhāṣya determination

The selected [091|04] sentence, *saṃskṛtasyaiva dharmasya hetuphale bhavataḥ*, resolves the kārikā's dual *te*: cause and fruit belong to a conditioned dharma. The normalized tokens open the emphatic particle and compound while preserving the quoted source form above.

```text
# tokens: saṃskṛtasya eva dharmasya hetuphale bhavataḥ
```

```nltk-fcfg
% start S
# tokens: saṃskṛtasya eva dharmasya hetuphale bhavataḥ
S[SEM=<(HasCause(conditioned) & HasFruit(conditioned) & -HasCause(unconditioned) & -HasFruit(unconditioned))>] -> CONDITIONED[CASE=gen,NUM=sg] ONLY DHARMA[CASE=gen,NUM=sg] PAIR[CASE=nom,NUM=du,REF=cause_fruit] ARE[NUM=du]
CONDITIONED[CASE=gen,NUM=sg] -> 'saṃskṛtasya'
ONLY -> 'eva'
DHARMA[CASE=gen,NUM=sg] -> 'dharmasya'
PAIR[CASE=nom,NUM=du,REF=cause_fruit] -> 'hetuphale'
ARE[NUM=du] -> 'bhavataḥ'
```

```nltk-dep
'bhavataḥ' -> 'saṃskṛtasya' | 'eva' | 'dharmasya' | 'hetuphale'
```

### Logic of the Bhāṣya argument

The root tests the selected proposition's exclusive scope. Other theories keep distinct the [090|26–29] temporal specification, [091|09–12] production/bringing distinction, and [091|26–092|04] competing accounts of disconnection. A finite model witnesses this reading; it cannot settle the disputed ontology of the unconditioned.

```nltk-sem
exclusive_pair : HasCause(conditioned) & HasFruit(conditioned) & -HasCause(unconditioned) & -HasFruit(unconditioned)
```

```nltk-fol
# THEORY bhasya_exclusive_pair
# EXPECT bhasya_exclusive_pair T
HasCause(conditioned) & HasFruit(conditioned) & -HasCause(unconditioned) & -HasFruit(unconditioned)

# THEORY bhasya_temporal_classes
# EXPECT bhasya_temporal_classes T
TwoTimes(pervasive) & TwoTimes(homogeneous) & ThreeTimes(coarisen) & ThreeTimes(associated) & ThreeTimes(maturation) & OutsideTime(conditioning)

# THEORY bhasya_path_distinction
# EXPECT bhasya_path_distinction T
Produces(path,acquisition) & BringsTo(path,disconnection) & -Produces(path,disconnection) & Fruit(disconnection)

# THEORY reported_entity_and_absence
# EXPECT reported_entity_and_absence T
Reports(vaibhasika,entity_reading) & Reports(sautrantika,absence_reading)

# THEORY rejected_te_refers_to_three_causes
# EXPECT rejected_te_refers_to_three_causes F
RefersTo(te,three_causes) & RefersTo(te,cause_fruit)

# THEORY rejected_path_produces_disconnection
# EXPECT rejected_path_produces_disconnection F
Produces(path,disconnection) & BringsTo(path,disconnection)

# THEORY rejected_unconditioned_has_fruit
# EXPECT rejected_unconditioned_has_fruit F
HasFruit(unconditioned) & Fruit(disconnection)
```

```nltk-valuation
conditioned => cd
unconditioned => uc
pervasive => pv
homogeneous => hg
coarisen => co
associated => as
maturation => ma
conditioning => cn
path => pt
acquisition => aq
disconnection => dc
vaibhasika => vb
sautrantika => st
entity_reading => er
absence_reading => ar
te => pronoun
three_causes => tc
cause_fruit => cf
HasCause => {cd}
HasFruit => {cd}
TwoTimes => {pv,hg}
ThreeTimes => {co,as,ma}
OutsideTime => {cn}
Produces => {(pt,aq)}
BringsTo => {(pt,dc)}
Fruit => {dc}
Reports => {(vb,er),(st,ar)}
RefersTo => {(pronoun,cf)}
```

The negative tests reject a three-cause antecedent for *te*, production of disconnection by the Path, and possession of fruit by an unconditioned dharma. The reported entity and absence readings are kept as distinct attributed positions rather than evaluated as one settled fact.

## 5. Review Status

Grammar and Logic added for selected [091|04] and its surrounding temporal and fruit argument. The selected Sanskrit witness remains partial and uncollated; disputed unconditioned ontology is not resolved by the finite model. The assignment of fruits is next.
