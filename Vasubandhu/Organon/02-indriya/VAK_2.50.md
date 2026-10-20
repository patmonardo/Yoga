# VAK_2.50 — Co-arisen Cause

## 1. Sanskrit (Devanāgarī)

```sanskrit
स्वतोऽन्ये कारणं हेतुः सहभूर्ये मिथःफलाः ।
भूतवच्चित्तचित्तानुवर्तिलक्षणलक्ष्यवत् ॥ २.५० ॥
```

## 2. Sanskrit (IAST)

```text
svato 'nye kāraṇaṃ hetuḥ sahabhūr ye mithaḥphalāḥ /
bhūtavac cittacittānuvartilakṣaṇalakṣyavat // 2.50 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| svataḥ | ablative singular of *sva* | from itself; comparison base for *anye* |
| anye | masculine nominative plural adjective | the other [dharmas], excluding the dharma itself |
| kāraṇaṃ hetuḥ | neuter nominative singular + masculine nominative singular | conditioning cause; definition carried from the prior Bhāṣya |
| sahabhūḥ | masculine nominative singular adjective | co-arisen cause |
| ye | masculine nominative plural relative pronoun | those that; binds the mutual-result criterion |
| mithaḥphalāḥ | masculine nominative plural compound adjective | one another's results |
| bhūtavat | indeclinable comparative adverb | as with the Great Elements; the Bhāṣya specifies four |
| citta-cittānuvarti-lakṣaṇa-lakṣya-vat | compressed compound with comparative *-vat* | as with consciousness and its followers, and with marks and what is marked; two pairings |

**Grammar tokens.** External sandhi is opened in *svato 'nye* and *sahabhūr ye*. The final compound remains one token: its two pairings share the comparative ending. The count of four Great Elements is supplied by the Bhāṣya, not an expressed numeral in the verse.

```text
# tokens: svataḥ anye kāraṇaṃ hetuḥ sahabhūḥ ye mithaḥphalāḥ bhūtavat cittacittānuvartilakṣaṇalakṣyavat
```

## 4. Grammar

The first four tokens complete the conditioning-cause definition introduced in the prior Bhāṣya. The relative *ye* gives the criterion for the co-arisen cause: being one another's results. *Bhūtavat* and the final compound supply examples under that criterion. The grammar derives reciprocal causality from mutual result; the secondary-mark exception is Bhāṣya prose and stays outside the verse parse.

```nltk-fcfg
% start S
# tokens: svataḥ anye kāraṇaṃ hetuḥ sahabhūḥ ye mithaḥphalāḥ bhūtavat cittacittānuvartilakṣaṇalakṣyavat
S[SEM=<(?prior & ?mutual & ?examples)>] -> PRIOR[SEM=?prior] MUTUAL[SEM=?mutual] EXAMPLES[SEM=?examples]
PRIOR[SEM=<(all x.((Dharma(x) & -(x = target)) -> ConditioningCauseFor(x,target)) & -ConditioningCauseFor(target,target))>] -> FROM[CASE=abl] OTHERS[CASE=nom,NUM=pl] CONDITIONING[CASE=nom,NUM=sg,GEN=n] CAUSE[CASE=nom,NUM=sg,GEN=m]
FROM[CASE=abl] -> 'svataḥ'
OTHERS[CASE=nom,NUM=pl] -> 'anye'
CONDITIONING[CASE=nom,NUM=sg,GEN=n] -> 'kāraṇaṃ'
CAUSE[CASE=nom,NUM=sg,GEN=m] -> 'hetuḥ'
MUTUAL[SEM=<all x.all y.(MutualResult(x,y) -> (MutualResult(y,x) & CoarisenCauseFor(x,y) & CoarisenCauseFor(y,x)))>] -> COARISEN[CASE=nom,NUM=sg,GEN=m] REL[CASE=nom,NUM=pl,GEN=m] RESULT[CASE=nom,NUM=pl,GEN=m,FORCE=reciprocal]
COARISEN[CASE=nom,NUM=sg,GEN=m] -> 'sahabhūḥ'
REL[CASE=nom,NUM=pl,GEN=m] -> 'ye'
RESULT[CASE=nom,NUM=pl,GEN=m,FORCE=reciprocal] -> 'mithaḥphalāḥ'
EXAMPLES[SEM=<?elements & ?pairings>] -> ELEMENTS[FORCE=simile,COUNT=4,SEM=?elements] PAIRINGS[FORCE=simile,PAIRS=2,SEM=?pairings]
ELEMENTS[FORCE=simile,COUNT=4,SEM=<all x.all y.((GreatElement(x) & GreatElement(y) & -(x = y)) -> MutualResult(x,y))>] -> 'bhūtavat'
PAIRINGS[FORCE=simile,PAIRS=2,SEM=<(MutualResult(citta,follower) & MutualResult(follower,citta) & MutualResult(mark,marked) & MutualResult(marked,mark))>] -> 'cittacittānuvartilakṣaṇalakṣyavat'
```

```nltk-dep
'hetuḥ' -> 'svataḥ' | 'anye' | 'kāraṇaṃ'
'sahabhūḥ' -> 'ye' | 'mithaḥphalāḥ' | 'hetuḥ' | 'bhūtavat' | 'cittacittānuvartilakṣaṇalakṣyavat'
```

**Feature chart checkpoints.** The carried definition spans [0, 4), the mutual-result criterion [4, 7), and its examples [7, 9). The root has one closed `SEM`. Ablative and nominative features constrain the first clause; nominative plural and reciprocal force constrain *ye mithaḥphalāḥ*. The example features distinguish the Bhāṣya's four elements from the two compound pairings.

| Span | Constituent | Result |
|---|---|
| [0, 4) | `PRIOR` | conditioning cause excludes the dharma itself |
| [4, 7) | `MUTUAL` | mutual result entails reciprocal co-arisen causality |
| [7, 9) | `EXAMPLES` | Great Elements and two paired examples |
| [0, 9) | `S` | carried definition joined to the new cause-definition |

## 5. Translation

### Literal Translation

> Other than itself is the conditioning cause. Co-arisen causes are those
> mutually resulting, as the Great Elements, consciousness and its
> followers, and mark and marked.
### Bhāṣya-informed study translation

> What is other than itself is the conditioning cause. Co-arisen causes
> are mutually resultant: the four Great Elements; consciousness and the
> dharmas that follow it, each of the other; and the marks and what is
> marked, each of the other.
## 6. Philosophical Translation

> The cause that excludes itself gives way to reciprocal determination: where dharmas are one another's results, they are co-arisen causes. The Bhāṣya then tests the reach of that reciprocity against secondary marks.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| kāraṇa-hetu / svato 'nye | conditioning cause / other than itself | first clause resumes the definition begun in the 2.49 Bhāṣya |
| sahabhū-hetu | co-arisen cause | here defined by mutual result, not mere simultaneity |
| mithaḥphala | one another's results | reciprocal criterion; Bhāṣya spells out *parasparaphala* |
| mahābhūta | Great Element | four specified in the Bhāṣya; pairwise example |
| citta / cittānuvartin | consciousness / its follower | reciprocal example; followers are specified next |
| lakṣaṇa / lakṣya | mark / what is marked | reciprocal example, qualified by the prose's secondary marks |
| anulakṣaṇa | secondary mark | Bhāṣya-only one-way cause relation from dharma to secondary mark |

## 8. Logical Determination

**Kārikā, derived.** The first conjunct carries the prior conditioning-cause definition into this verse. The second makes mutual result the criterion for reciprocal co-arisen causality. The examples instantiate mutual result; the model also tests the Bhāṣya's four-element specification. The one-way secondary-mark case is stated separately as a prose qualification.

```nltk-sem
mutual_criterion : all x.all y.(MutualResult(x,y) -> (MutualResult(y,x) & CoarisenCauseFor(x,y) & CoarisenCauseFor(y,x)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(((all x.((Dharma(x) & -(x = target)) -> ConditioningCauseFor(x,target)) & -ConditioningCauseFor(target,target)) & all x.all y.(MutualResult(x,y) -> (MutualResult(y,x) & CoarisenCauseFor(x,y) & CoarisenCauseFor(y,x)))) & (all x.all y.((GreatElement(x) & GreatElement(y) & -(x = y)) -> MutualResult(x,y)) & (MutualResult(citta,follower) & MutualResult(follower,citta) & MutualResult(mark,marked) & MutualResult(marked,mark))))

# THEORY prose_examples
# EXPECT prose_examples T
all x.(GreatElement(x) -> (x = earth | x = water | x = fire | x = wind))
GreatElement(earth) & GreatElement(water) & GreatElement(fire) & GreatElement(wind)
all x.all y.((GreatElement(x) & GreatElement(y) & -(x = y)) -> (CoarisenCauseFor(x,y) & CoarisenCauseFor(y,x)))

# THEORY prose_secondary_marks
# EXPECT prose_secondary_marks T
SecondaryMark(secondary_mark) & CoarisenCauseFor(marked,secondary_mark) & -CoarisenCauseFor(secondary_mark,marked)
-MutualResult(marked,secondary_mark) & -MutualResult(secondary_mark,marked)

# THEORY rejected_mere_simultaneity_suffices
# EXPECT rejected_mere_simultaneity_suffices F
all x.all y.(Cooccurs(x,y) -> CoarisenCauseFor(x,y))

# THEORY rejected_one_way_mutual_result
# EXPECT rejected_one_way_mutual_result F
MutualResult(citta,follower) & -MutualResult(follower,citta)

# THEORY rejected_secondary_marks_are_reciprocal
# EXPECT rejected_secondary_marks_are_reciprocal F
CoarisenCauseFor(marked,secondary_mark) & CoarisenCauseFor(secondary_mark,marked)

# THEORY rejected_every_conditioned_pair_is_coarisen_cause
# EXPECT rejected_every_conditioned_pair_is_coarisen_cause F
all x.all y.((Conditioned(x) & Conditioned(y) & -(x = y)) -> CoarisenCauseFor(x,y))

# THEORY rejected_self_conditioning
# EXPECT rejected_self_conditioning F
ConditioningCauseFor(target,target) & Conditioned(target)
```

```nltk-valuation
target => target_dharma
other => other_dharma
citta => consciousness_dharma
follower => follower_dharma
mark => mark_dharma
marked => marked_dharma
secondary_mark => secondary_mark_dharma
earth => earth_element
water => water_element
fire => fire_element
wind => wind_element
extra => extra_conditioned_dharma
Dharma => {target_dharma,other_dharma,consciousness_dharma,follower_dharma,mark_dharma,marked_dharma,secondary_mark_dharma,earth_element,water_element,fire_element,wind_element,extra_conditioned_dharma}
Conditioned => {target_dharma,consciousness_dharma,follower_dharma,mark_dharma,marked_dharma,secondary_mark_dharma,extra_conditioned_dharma}
ConditioningCauseFor => {(other_dharma,target_dharma),(consciousness_dharma,target_dharma),(follower_dharma,target_dharma),(mark_dharma,target_dharma),(marked_dharma,target_dharma),(secondary_mark_dharma,target_dharma),(earth_element,target_dharma),(water_element,target_dharma),(fire_element,target_dharma),(wind_element,target_dharma),(extra_conditioned_dharma,target_dharma)}
GreatElement => {earth_element,water_element,fire_element,wind_element}
MutualResult => {(earth_element,water_element),(earth_element,fire_element),(earth_element,wind_element),(water_element,earth_element),(water_element,fire_element),(water_element,wind_element),(fire_element,earth_element),(fire_element,water_element),(fire_element,wind_element),(wind_element,earth_element),(wind_element,water_element),(wind_element,fire_element),(consciousness_dharma,follower_dharma),(follower_dharma,consciousness_dharma),(mark_dharma,marked_dharma),(marked_dharma,mark_dharma)}
CoarisenCauseFor => {(earth_element,water_element),(earth_element,fire_element),(earth_element,wind_element),(water_element,earth_element),(water_element,fire_element),(water_element,wind_element),(fire_element,earth_element),(fire_element,water_element),(fire_element,wind_element),(wind_element,earth_element),(wind_element,water_element),(wind_element,fire_element),(consciousness_dharma,follower_dharma),(follower_dharma,consciousness_dharma),(mark_dharma,marked_dharma),(marked_dharma,mark_dharma),(marked_dharma,secondary_mark_dharma)}
SecondaryMark => {secondary_mark_dharma}
Cooccurs => {(consciousness_dharma,extra_conditioned_dharma)}
```

The false theories distinguish mutual result from mere simultaneity, reject a one-way reading of the verse's reciprocal examples, preserve the Bhāṣya's asymmetric secondary-mark qualification, and block an unrestricted all-conditioned-pairs inference. The finite valuation checks these relations, not an independent proof of causation.

## 9. Interpretive Note

**Translation note.** The Bhāṣya also qualifies the reciprocal account: even
without mutual result, a dharma is a co-arisen cause of its secondary marks,
though they are not causes of it. The examples do not make every conditioned
dharma a cause of every other.

Here *pāraṃparya* explains reciprocal result in the co-arisen examples; it should not be identified with the successive mediated-cause account reported in the preceding Bhāṣya. The verse's first clause remains part of the conditioning-cause account, while the rest opens the co-arisen account. In the larger Indriya inquiry, this is one specific *hetu* relation; it does not yet settle the later four *pratyayas*. The Sanskrit witness still requires collation.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_50 a vak:Karika ; vak:hasTopic vak:CoArisenCause .
vak:SecondaryMark vak:reciprocal false .
```
