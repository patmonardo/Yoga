# VAK_2.64 — Through How Many Conditions

## 1. Sanskrit (Devanāgarī)

```sanskrit
चतुर्भिश्चित्तचैत्ता हि समापत्तिद्वयं त्रिभिः /
द्वाभ्यामन्ये तु जायन्ते नेश्वरादेः क्रमादिभिः // २.६४ //
```

## 2. Sanskrit (IAST)

```text
caturbhiś cittacaittā hi samāpattidvayaṃ tribhiḥ /
dvābhyām anye tu jāyante neśvarādeḥ kramādibhiḥ // 2.64 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| caturbhiḥ | instrumental plural numeral | Through four conditions. |
| cittacaittāḥ | masculine nominative plural | Mind and mental factors. |
| hi | particle | Indeed; confirms the preceding four-condition account. |
| samāpattidvayam | neuter nominative singular compound | The pair of attainments. |
| tribhiḥ | instrumental plural numeral | Through three conditions. |
| dvābhyām | instrumental dual numeral | Through two conditions. |
| anye | masculine nominative plural | The other dharmas. |
| tu | particle | But; contrasts this range with the preceding two. |
| jāyante | third plural present middle | Arise. |
| na | negation | Not. |
| īśvarādeḥ | ablative/genitive singular | From Īśvara and similar proposed causes. |
| kramādibhiḥ | instrumental plural | On grounds including observed succession. |

The running [Sanskrit witness](../../Sources/kosabhasya.txt) has
*cattacaittā* in its first fragment; the older VAK study normalizes
this to *cittacaittā*. The former Organon text also omitted *hi* and
*tu*, lengthened *samāpattidvayam*, and replaced *jāyante*.

```text
# tokens: caturbhiḥ cittacaittāḥ hi samāpattidvayam tribhiḥ dvābhyām anye tu jāyante na īśvarādeḥ kramādibhiḥ
```

## 4. Grammar

The first three clauses give counts of four, three, and two conditions
for mind and mental factors, the two attainments, and the other
dharmas. The final clause rejects a proposed single world-cause such
as Īśvara, with succession among the reasons. The identities of the
applicable conditions and the extended argument are in the Bhāṣya.

```nltk-fcfg
% start S
# tokens: caturbhiḥ cittacaittāḥ hi samāpattidvayam tribhiḥ dvābhyām anye tu jāyante na īśvarādeḥ kramādibhiḥ
S[SEM=<(?four & ?three & ?two & ?reject)>] -> FOUR[SEM=?four] THREE[SEM=?three] TWO[SEM=?two] REJECT[SEM=?reject]
FOUR[SEM=<all x.(CittaCaitta(x) -> ArisesThrough(x,four))>] -> THROUGH4[CASE=ins,CNT=4] CITTA[CASE=nom,NUM=pl] INDEED
THROUGH4[CASE=ins,CNT=4] -> 'caturbhiḥ'
CITTA[CASE=nom,NUM=pl] -> 'cittacaittāḥ'
INDEED -> 'hi'
THREE[SEM=<all x.(AttainmentPair(x) -> ArisesThrough(x,three))>] -> ATTAIN[CASE=nom,NUM=sg] THROUGH3[CASE=ins,CNT=3]
ATTAIN[CASE=nom,NUM=sg] -> 'samāpattidvayam'
THROUGH3[CASE=ins,CNT=3] -> 'tribhiḥ'
TWO[SEM=<all x.(Other(x) -> ArisesThrough(x,two))>] -> THROUGH2[CASE=ins,NUM=du] OTHER[CASE=nom,NUM=pl] BUT ARISE[NUM=pl]
THROUGH2[CASE=ins,NUM=du] -> 'dvābhyām'
OTHER[CASE=nom,NUM=pl] -> 'anye'
BUT -> 'tu'
ARISE[NUM=pl] -> 'jāyante'
REJECT[SEM=<(-ArisesFrom(isvara_and_like) & Reason(succession))>] -> NOT FROM[CASE=abl] REASON[CASE=ins,NUM=pl]
NOT -> 'na'
FROM[CASE=abl] -> 'īśvarādeḥ'
REASON[CASE=ins,NUM=pl] -> 'kramādibhiḥ'
```

```nltk-dep
'cittacaittāḥ' -> 'caturbhiḥ' | 'hi'
'samāpattidvayam' -> 'tribhiḥ'
'anye' -> 'dvābhyām' | 'tu' | 'jāyante'
'īśvarādeḥ' -> 'na' | 'kramādibhiḥ'
```

**Feature chart checkpoints.** The four-condition clause spans [0,
3), the three-condition clause [3, 5), the two-condition clause [5,
9), the rejection [9, 12), and the root [0, 12). Instrumental count
and number features constrain the three ranges. The source text and
the model keep the single-cause objection distinct from those counts.

## 5. Translation

### Literal Translation

> Consciousness and mental factors arise through four conditions; the pair
> of attainments through three; the rest through two. They do not arise
> from Īśvara and the like, given succession and the rest.

### Bhāṣya-informed study translation

> Consciousness and mental factors arise through four conditions, the pair
> of attainments through three, and the rest through two. The world does
> not arise from Īśvara and the like as one cause, given observed
> succession.

## 6. Philosophical Translation

> The verse states the number of conditions for three ranges of dharmas and rejects a single world-cause on the grounds of succession. The Bhāṣya identifies the conditions and names Īśvara, Puruṣa, and Pradhāna among the rejected proposals.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| caturbhiḥ | through four | cause, antecedent, object, predominant |
| tribhiḥ | through three | the attainments lack object |
| dvābhyām | through two | Form and dissociated: cause and predominant |
| īśvarādi | Īśvara and the like | rejected single causes |
| krama | succession | the observed reason against one cause |

## 8. Logical Determination

**Kārikā, derived.** The root SEM states the three ranges and the objection to a single world-cause from succession. The identities of the conditions, the lack of object for the attainments, the named proposals, and the claim that beings' own actions generate them in their births are prose elaborations.

```nltk-sem
four : all x.(CittaCaitta(x) -> ArisesThrough(x,four))
three : all x.(AttainmentPair(x) -> ArisesThrough(x,three))
two : all x.(Other(x) -> ArisesThrough(x,two))
reject : -ArisesFrom(isvara_and_like) & Reason(succession)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.(CittaCaitta(x) -> ArisesThrough(x,four)) & all x.(AttainmentPair(x) -> ArisesThrough(x,three)) & all x.(Other(x) -> ArisesThrough(x,two)) & -ArisesFrom(isvara_and_like) & Reason(succession))

# THEORY prose_identities
# EXPECT prose_identities T
Includes(four,cause) & Includes(four,antecedent) & Includes(four,object) & Includes(four,predominant)
Includes(three,cause) & Includes(three,antecedent) & Includes(three,predominant) & -Includes(three,object)
Includes(two,cause) & Includes(two,predominant) & -Includes(two,antecedent) & -Includes(two,object)

# THEORY prose_named
# EXPECT prose_named T
NamedProposal(isvara) & NamedProposal(purusa) & NamedProposal(pradhana)

# THEORY prose_karma
# EXPECT prose_karma T
OwnActionsGenerateBirths(beings) & -ArisesFrom(isvara_and_like)

# THEORY rejected_single_cause
# EXPECT rejected_single_cause F
Reason(succession) & ArisesFrom(isvara_and_like)

# THEORY rejected_simultaneous_world
# EXPECT rejected_simultaneous_world F
SingleSufficientCause(isvara) & SimultaneousArising(world)
```

```nltk-valuation
isvara_and_like => isvara_etc
isvara => isvara_item
purusa => purusa_item
pradhana => pradhana_item
succession => succession_reason
beings => beings_group
world => world_item
four => four_conditions
three => three_conditions
two => two_conditions
cause => cause_cond
antecedent => ant_cond
object => obj_cond
predominant => pred_cond
CittaCaitta => {citta_item}
AttainmentPair => {attain_item}
Other => {other_item}
ArisesThrough => {(citta_item,four_conditions),(attain_item,three_conditions),(other_item,two_conditions)}
ArisesFrom => {}
Reason => {succession_reason}
Includes => {(four_conditions,cause_cond),(four_conditions,ant_cond),(four_conditions,obj_cond),(four_conditions,pred_cond),(three_conditions,cause_cond),(three_conditions,ant_cond),(three_conditions,pred_cond),(two_conditions,cause_cond),(two_conditions,pred_cond)}
NamedProposal => {isvara_item,purusa_item,pradhana_item}
OwnActionsGenerateBirths => {beings_group}
SingleSufficientCause => {}
SimultaneousArising => {}
```

The finite model witnesses the three condition counts and the stated objection to a single world-cause. The Bhāṣya identifies the included conditions and adds the argument from simultaneous production. This model does not decide every alternative proposal.

## 9. Interpretive Note

**Translation note.** The Bhāṣya identifies the four as cause-condition, immediately antecedent, object, and predominant; the pair of attainments lacks an object-condition, while Form and dharmas dissociated from consciousness arise through cause and predominant conditions. It names Īśvara, Puruṣa, and Pradhāna among proposed world-causes: a single sufficient cause would produce the world at once, but succession is observed. It adds that beings' actions generate them in their births; this does not settle every position.

The verse states the ranges and the rejection. The next verse continues with the conditions for the elements.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_64 a vak:Karika ; vak:hasTopic vak:ThroughHowManyConditions .
vak:CittaCaitta vak:arisesThrough 4 .
vak:AttainmentPair vak:arisesThrough 3 .
vak:OneWorldCause vak:rejectedBy vak:Succession .
```
