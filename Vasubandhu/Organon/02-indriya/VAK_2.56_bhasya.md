# VAK_2.56 Bhāṣya — Principal Fruits

## 1. Kārikā Anchor

> vipākaphalam antyasya pūrvasya adhipajaṃ phalam /
>
> sabhāgasarvatragayor niṣyandaḥ pauruṣaṃ dvayoḥ // 2.56 //

> The last, maturation cause, has maturation as its fruit; the first,
> conditioning cause, has predominance-born fruit. The homogeneous and
> pervasive have homogeneous outflow; the co-arisen and associated have
> efficacy as fruit.

## 2. Continuous Sanskrit Witness

> vipākaphalam antyasya /
> tasya vipākaphalam /
> pūrvasya adhipajaṃ phalam /
> kāraṇahetuḥ pūrvam uktatvāt pūrvaḥ /
> tasyādhipajaṃ phalam /
> sabhāgasarvatragayor niṣyandaḥ /
> sadṛśaphalatvād anayor niḥṣyandaphalam /
> pauruṣaṃ dvayoḥ // 2.56 //
> sahabhūsaṃprayuktakahetvoḥ puruṣakāraphalam /
> ko 'yaṃ puruṣakāro nāma / yasya dharmasya yat kāritram /
> kimanyeṣāmapyasti puruṣakāraphāmutāho dvayoreva /
> anyeṣāmapyastyanyatra vipākahetoḥ /
> tasyāpyasti viprakṛṣṭapuruṣakāraphalam / yathā karṣakāṇāṃ sasyamityapare /

The selected witness extends through 95.08; the unit begins at 94.19 in `Vasubandhu/Sources/kosabhasya.txt`. Defects remain. Not a collation.

## 3. Continuous Conventional Translation

The last has maturation-fruit. The first has predominance. What predominance has mere non-obstruction? That very non-obstruction. A contributory role too. Homogeneous and pervasive have a similar fruit. Homogeneous outflow. The two are co-arisen and associated. Fruit of efficacy. Efficacy is the activity a dharma performs. Called a person's activity by resemblance. The later question shows the assignment is not exclusive: other causes can also have efficacy-fruit, except maturation cause in the main reply. A further opinion gives maturation cause a distant efficacy-fruit, likened to farmers' crop; it is reported without being made the principal assignment.

## 4. Interpretation

The verse assigns each cause its characteristic fruit. The Bhāṣya then distinguishes principal assignment from further fruit relations and attributes the distant-crop alternative. *Puruṣakāra* names a dharma's activity by figure; it does not introduce an external Puruṣa agent.

### Grammar of the Bhāṣya determination

The selected [095|05–06] reply, *anyeṣām apy asti anyatra vipākahetoḥ*, limits the verse's apparent exclusivity. Sandhi is opened for the normalized parse. The following distant-crop opinion remains a separate reported claim.

```text
# tokens: anyeṣām api asti anyatra vipākahetoḥ
```

```nltk-fcfg
% start S
# tokens: anyeṣām api asti anyatra vipākahetoḥ
S[SEM=<(OtherEfficacyFruit(conditioning_cause) & OtherEfficacyFruit(homogeneous_cause) & OtherEfficacyFruit(pervasive_cause) & -OtherEfficacyFruit(maturation_cause))>] -> OTHERS[CASE=gen,NUM=pl] ALSO EXISTS EXCEPT MATURATION[CASE=gen,NUM=sg]
OTHERS[CASE=gen,NUM=pl] -> 'anyeṣām'
ALSO -> 'api'
EXISTS -> 'asti'
EXCEPT -> 'anyatra'
MATURATION[CASE=gen,NUM=sg] -> 'vipākahetoḥ'
```

```nltk-dep
'asti' -> 'anyeṣām' | 'api' | 'anyatra' | 'vipākahetoḥ'
```

### Logic of the Bhāṣya argument

The root records the main reply's extension of efficacy-fruit beyond the two principal causes, excluding maturation cause. The alternative at [095|07–08] is represented as a report. The reply and report can coexist as textual facts without making the rival claims jointly true.

```nltk-sem
additional_efficacy : OtherEfficacyFruit(conditioning_cause) & OtherEfficacyFruit(homogeneous_cause) & OtherEfficacyFruit(pervasive_cause) & -OtherEfficacyFruit(maturation_cause)
```

```nltk-fol
# THEORY bhasya_additional_efficacy
# EXPECT bhasya_additional_efficacy T
OtherEfficacyFruit(conditioning_cause) & OtherEfficacyFruit(homogeneous_cause) & OtherEfficacyFruit(pervasive_cause) & -OtherEfficacyFruit(maturation_cause)

# THEORY bhasya_principal_pair
# EXPECT bhasya_principal_pair T
PrincipalFruit(coarisen_cause,efficacy_fruit) & PrincipalFruit(associated_cause,efficacy_fruit)

# THEORY reported_distant_crop
# EXPECT reported_distant_crop T
Reports(others,distant_crop_view) & Claims(distant_crop_view,maturation_cause)

# THEORY bhasya_person_figure
# EXPECT bhasya_person_figure T
ActivityOf(dharma,activity) & FigurativePersonLanguage(efficacy_fruit)

# THEORY rejected_exclusive_pair
# EXPECT rejected_exclusive_pair F
-OtherEfficacyFruit(conditioning_cause) & PrincipalFruit(coarisen_cause,efficacy_fruit)

# THEORY rejected_alternative_as_main_reply
# EXPECT rejected_alternative_as_main_reply F
OtherEfficacyFruit(maturation_cause) & Claims(distant_crop_view,maturation_cause)

# THEORY rejected_external_agent
# EXPECT rejected_external_agent F
ExternalAgent(purusha) & ActivityOf(dharma,activity)
```

```nltk-valuation
conditioning_cause => cc
homogeneous_cause => hc
pervasive_cause => pc
maturation_cause => mc
coarisen_cause => coc
associated_cause => ac
efficacy_fruit => ef
others => ot
distant_crop_view => dv
dharma => dh
activity => act
purusha => pu
OtherEfficacyFruit => {cc,hc,pc}
PrincipalFruit => {(coc,ef),(ac,ef)}
Reports => {(ot,dv)}
Claims => {(dv,mc)}
ActivityOf => {(dh,act)}
FigurativePersonLanguage => {ef}
ExternalAgent => {}
```

The countertests reject an exclusive reading of *dvayoḥ*, importing the distant-crop report into the main reply, and treating the person figure as an external agent. This finite valuation tests attribution and scope, not the correctness of the alternative view.

## 5. Review Status

Grammar and Logic added for the selected [095|05–06] Bhāṣya reply and its attributed alternative. The Sanskrit witness is still partial and uncollated. The assignment is principal, not exclusive.
