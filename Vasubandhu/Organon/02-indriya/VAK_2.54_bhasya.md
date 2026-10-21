# VAK_2.54 Bhāṣya — Pervasive and Maturation

## 1. Kārikā Anchor

> sarvatragākhyaḥ kliṣṭānāṃ svabhūmau pūrvasarvagāḥ /
>
> vipākahetur aśubhāḥ kuśalāś caiva sāsravāḥ // 2.54 //

> The cause called pervasive is the prior pervasive dharmas of a level,
> for later afflicted dharmas on that same level. Maturation cause is
> unwholesome and wholesome with influx.

## 2. Sanskrit Witness — Selected Passages

> sarvatragahetuḥ katamaḥ /
> sarvatragākhyaḥ kliṣṭānāṃ svabhūmau pūrvasarvagāḥ /
> svabhūmikāḥ pūrvotpannāḥ sarvatragā dharmāḥ paścimānāṃ kliṣṭānāṃ dharmāṇāṃ sarvatragahetuḥ /
> vipākahetur aśubhāḥ kuśalāś caiva sāsravāḥ // 2.54 //
> akuśalāḥ kuśalasāsravāśca dharmā vipākahetuḥ /
> kasmādavyākṛtā dharmāḥ vipākaṃ na nirvarttayanti /
> durbalatvāt / pūti bījavat /
> kasmānnānāsravāḥ / tṛṣṇānabhiṣyanditatvāt /
> visadṛśaḥ pāko vipākaḥ /
> ekasyobhayatheti vaibhāṣikāḥ /
> pāko hi nāma santatipariṇāmaviśeṣajaḥ phalaparyantaḥ /
> na ca karmaṇā saha vipāko vipacyate nāpyanantaraṃ samanantarapratyayākṛṣṭatvāt samanantarakṣaṇasya /
> pravāhāpekṣo hi vipākahetuḥ /

These are selected lines from 89.01–90.22 in
[the running witness](../../Sources/kosabhasya.txt), not a complete
transcription or collation. The excluded classes, reported Vaibhāṣika
view, and delayed-continuum conclusion are kept at prose level.

## 3. Conventional Argument Summary

Prior pervasive dharmas of a level cause later afflicted dharmas on that level, including another class. The list is later. A noble person's afflicted dharmas still have a seeing-abandoned cause, unmentioned because abandoned. Unwholesome and wholesome with influx mature. Indeterminate are weak. Uncontaminated are not moistened by craving. The prose first calls maturation a dissimilar ripening and reports the Vaibhāṣika allowance of two senses. It then argues that ripening, properly so called, reaches its result through a special transformation of a continuum; the other causal kinds lack that pattern. The cause depends on a series. Not together with the karma, and not immediately after.

## 4. Interpretation

Pervasive cause is prior, own-level, and directed to later affliction even across abandonment classes. Maturation cause is restricted to unwholesome and wholesome-with-influx dharmas. The Bhāṣya argues through exclusions and a contested definition of ripening before requiring a continuum and delayed result.

### Grammar of the Bhāṣya determination

The selected [089|03] prose sentence resolves the kārikā's compressed pervasive-cause clause: own level, prior arising, and later afflicted result. Its normalized tokens open compounds and inflection for the feature chart; they do not replace the source witness.

```text
# tokens: svabhūmikāḥ pūrvotpannāḥ sarvatragāḥ dharmāḥ paścimānām kliṣṭānām dharmāṇām sarvatragahetuḥ
```

```nltk-fcfg
% start S
# tokens: svabhūmikāḥ pūrvotpannāḥ sarvatragāḥ dharmāḥ paścimānām kliṣṭānām dharmāṇām sarvatragahetuḥ
S[SEM=<(Prior(prior_pervasive,later_afflicted) & SameLevel(prior_pervasive,later_afflicted) & PervasiveCause(prior_pervasive,later_afflicted))>] -> OWN[CASE=nom,NUM=pl,LEVEL=own] PRIOR[CASE=nom,NUM=pl,TIME=prior] PERVASIVE[CASE=nom,NUM=pl] DHARMAS[CASE=nom,NUM=pl] LATER[CASE=gen,NUM=pl,TIME=later] AFFLICTED[CASE=gen,NUM=pl] TARGET[CASE=gen,NUM=pl] CAUSE[CASE=nom,NUM=sg]
OWN[CASE=nom,NUM=pl,LEVEL=own] -> 'svabhūmikāḥ'
PRIOR[CASE=nom,NUM=pl,TIME=prior] -> 'pūrvotpannāḥ'
PERVASIVE[CASE=nom,NUM=pl] -> 'sarvatragāḥ'
DHARMAS[CASE=nom,NUM=pl] -> 'dharmāḥ'
LATER[CASE=gen,NUM=pl,TIME=later] -> 'paścimānām'
AFFLICTED[CASE=gen,NUM=pl] -> 'kliṣṭānām'
TARGET[CASE=gen,NUM=pl] -> 'dharmāṇām'
CAUSE[CASE=nom,NUM=sg] -> 'sarvatragahetuḥ'
```

```nltk-dep
'sarvatragahetuḥ' -> 'svabhūmikāḥ' | 'pūrvotpannāḥ' | 'sarvatragāḥ' | 'dharmāḥ' | 'paścimānām' | 'kliṣṭānām' | 'dharmāṇām'
```

### Logic of the Bhāṣya argument

The parsed sentence gives the causal core. Separate theories test the next explanation at [089|04–06], the exclusion questions at [089|19–22], and the delayed-continuum conclusion at [090|19–22]. The Vaibhāṣika two-sense statement at [089|27–090|01] is recorded as an attributed position, not a rule forced into the root `SEM`.

```nltk-sem
pervasive : Prior(prior_pervasive,later_afflicted) & SameLevel(prior_pervasive,later_afflicted) & PervasiveCause(prior_pervasive,later_afflicted)
```

```nltk-fol
# THEORY bhasya_pervasive
# EXPECT bhasya_pervasive T
Prior(prior_pervasive,later_afflicted) & SameLevel(prior_pervasive,later_afflicted) & PervasiveCause(prior_pervasive,later_afflicted)

# THEORY bhasya_cross_class
# EXPECT bhasya_cross_class T
DifferentClass(prior_pervasive,later_afflicted) & PervasiveCause(prior_pervasive,later_afflicted)

# THEORY bhasya_maturation_exclusions
# EXPECT bhasya_maturation_exclusions T
Weak(indeterminate) & -MaturationCause(indeterminate) & Unmoistened(uncontaminated) & -MaturationCause(uncontaminated)

# THEORY reported_two_senses
# EXPECT reported_two_senses T
Reports(vaibhasika,two_senses) & Argues(text,continuum_ripening)

# THEORY bhasya_continuum_delay
# EXPECT bhasya_continuum_delay T
DependsOnContinuum(karma,result) & -Simultaneous(karma,result) & -ImmediatelyAfter(karma,result)

# THEORY rejected_pervasive_requires_same_class
# EXPECT rejected_pervasive_requires_same_class F
SameClass(prior_pervasive,later_afflicted) & PervasiveCause(prior_pervasive,later_afflicted)

# THEORY rejected_indeterminate_maturation
# EXPECT rejected_indeterminate_maturation F
MaturationCause(indeterminate) & Weak(indeterminate)

# THEORY rejected_immediate_result
# EXPECT rejected_immediate_result F
ImmediatelyAfter(karma,result) & DependsOnContinuum(karma,result)
```

```nltk-valuation
prior_pervasive => pp
later_afflicted => la
indeterminate => id
uncontaminated => uc
vaibhasika => vb
two_senses => ts
text => tx
continuum_ripening => cr
karma => ka
result => re
Prior => {(pp,la)}
SameLevel => {(pp,la)}
PervasiveCause => {(pp,la)}
DifferentClass => {(pp,la)}
SameClass => {}
Weak => {id}
MaturationCause => {}
Unmoistened => {uc}
Reports => {(vb,ts)}
Argues => {(tx,cr)}
DependsOnContinuum => {(ka,re)}
Simultaneous => {}
ImmediatelyAfter => {}
```

The finite valuation is a behavioral witness to the attributed argument. It separates the reported Vaibhāṣika account from the text's subsequent reasoning, and it rejects same-class-only pervasive causation, indeterminate maturation, and an immediate result.

## 5. Review Status

Grammar and Logic added for the selected [089|03] Bhāṣya proposition and its surrounding exclusions and ripening argument. The selected Sanskrit witness remains partial and uncollated. The temporal classification is next.
