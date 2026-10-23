# VAK_2.56 Bhāṣya — Principal Fruits

## 1. Kārikā Anchor

> vipākaphalam antyasya pūrvasyādhipataṃ phalam /
>
> sabhāgasarvatragayor niṣyandaḥ pauruṣaṃ dvayoḥ // 2.56 //

> The last, maturation cause, has maturation as its fruit; the first,
> conditioning cause, has predominance-born fruit. The homogeneous and
> pervasive have homogeneous outflow; the co-arisen and associated have
> efficacy as fruit.

## 2. Continuous Sanskrit Witness

> athaiṣāṃ phalānāṃ katamat phalaṃ kasya hetoḥ /
> vipākaphalamantyasya
> vipākaheturantye 'bhihitatvāt antyaḥ /
> tasya vipākaphalam /
> pūrvasyādhipataṃ phalam /
> kāraṇahetuḥ pūrvamuktatvāt pūrvaḥ /
> tasyādhipajaṃ phalam /
> anāvaraṇabhāvamātreṇāvasthitasya kimādhipatyam /
> etadeva aṅgībhāvo 'pi cāsti kāraṇahetostadyathā "pañcasu vijñānakāyeṣudaśānāmāyatanānāṃ bhājanaloke ca karmaṇām /
> śrotrādīnāmapyasti cakṣurvijñānotpattau pāraṃparyeṇādhipatyam /
> śrutvā draṣṭukāmatotpatte" rityevamādi yojyam /
> sabhāga sarvatragayorniṣyandaḥ
> sadṛśaphalatvādanayorniḥṣyandaphalam /
> pauruṣaṃ dvayoḥ // VAkK_2.56 //
> sahabhūsaṃprayuktakahetvoḥ puruṣakāraphalam /
> puruṣabhāvavyatirekāt puruṣakāraḥ puruṣaṃ eva /
> tasya phalaṃ pauruṣam /
> ko 'yaṃ puruṣakāro nāma /
> yasya dharmasya yat kāritram /
> puruṣakāra iva hi puruṣakāraḥ /
> tadyathā kākajaṅghā oṣadhirmattahastī manuṣya iti /
> kimanyeṣāmapyasti puruṣakāraphāmutāho dvayoreva /
> anyeṣāmapyastyanyatra vipākahetoḥ /
> yasmātsahotpannaṃ vā samanantarotpannaṃ vā puruṣakāraphalaṃ bhavati /
> na caivaṃ vipākaḥ /
> tasyāpyasti viprakṛṣṭapuruṣakāraphalam /
> yathā karṣakāṇāṃ sasyamityapare /

The witness follows [the local running source](../../Sources/kosabhasya.txt)
from 94.18 through 95.08. The kārikā reads `adhipataṃ` at
94.21, while the prose reads `adhipajaṃ` at 94.22. Both are
retained. The question defining the fruits begins at 95.09.

## 3. Continuous Conventional Translation

Which fruit belongs to which of these causes? The last cause has
maturation as its fruit. “Last” means the maturation cause, named
last in the list. The first has predominance-born fruit: “first”
means the conditioning cause, named first. What predominance does
one have by mere non-obstruction? That itself counts, and a
conditioning cause can also make a positive contribution. Thus
ten Essences have predominance in relation to the five groups of
Cognition, and actions in relation to the surrounding world.
Ear and the other Faculties can also have an indirect predominance
in the arising of eye Cognition: after hearing, for example,
one may wish to see. Extend the account in this way.

Homogeneous and pervasive causes have homogeneous outflow as fruit,
because each produces a similar result. The two co-arisen and
associated causes have the fruit of activity (*puruṣakāra*). What
is this activity? It is whatever work a dharma performs. The
expression is figurative, like other names that compare one thing
to another [the source gives the herb “crow's leg” and a person
called “mad elephant”].

Do only these two causes have activity as fruit, or do the others
also? The others do too, except the maturation cause, says the
first reply. An activity-fruit arises together with, or immediately
after, its cause; maturation does neither. Others hold that even
the maturation cause has a remote activity-fruit, as a crop is the
fruit of farmers' work. That is an attributed alternative, not
the verse's principal assignment.

## 4. Reading Control

The verse assigns each cause its characteristic fruit. The Bhāṣya
then distinguishes that principal assignment from further fruit
relations and attributes the remote-crop alternative to others.
*Puruṣakāra* describes the work of a dharma by a figure of speech;
the prose explicitly asks what that work is before considering
whether other causes also have such a fruit.

### Grammar of the Bhāṣya determination

The [095|05–06] reply, *anyeṣām apy asti anyatra vipākahetoḥ*, limits the verse's apparent exclusivity. Sandhi is opened for the normalized parse. The following distant-crop opinion remains a separate reported claim.

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

The complete Sanskrit witness has been checked against the local
source from 94.18 through 95.08. The continuous translation covers
the four principal fruit assignments, the examples of predominance,
the activity figure, and the two answers on further activity-fruits.
The embedded study grammar and logic have not been re-tested in this
pass, and the separate kārikā Grammar and Logic files were not changed.
