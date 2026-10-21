# VAK_2.51 — Followers of Consciousness

## 1. Sanskrit (Devanāgarī)

```sanskrit
चैत्ता द्वौ संवरौ तेषां चेतसो लक्षणानि च ।
चित्तानुवर्तिनः कालफलादिशुभतादिभिः ॥ २.५१ ॥
```

## 2. Sanskrit (IAST)

```text
caittā dvau saṃvarau teṣāṃ cetaso lakṣaṇāni ca /
cittānuvartinaḥ kālaphalādiśubhatādibhiḥ // 2.51 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| caittāḥ | masculine nominative plural | mental factors associated with consciousness |
| dvau | masculine nominative dual numeral | two; constrains the restraint group |
| saṃvarau | masculine nominative dual | the two restraints, specified in the Bhāṣya |
| teṣām | genitive plural pronoun | of the preceding factors and restraints |
| cetasaḥ | genitive singular | of consciousness; distinct from *teṣām* |
| lakṣaṇāni ca | neuter nominative plural + conjunction | and their marks |
| cittānuvartinaḥ | masculine nominative plural compound adjective | followers of consciousness |
| kāla-phala-ādi-śubhatā-ādibhiḥ | instrumental plural compound with *ādi* | by time, result, ethical status, and further respects; Bhāṣya spells out ten |

**Grammar tokens.** External sandhi is opened at *caittā dvau* and *cetaso lakṣaṇāni* without changing the witness. The final instrumental compound stays one token: its two occurrences of *ādi* announce further respects whose tenfold detail comes from the Bhāṣya.

```text
# tokens: caittāḥ dvau saṃvarau teṣām cetasaḥ lakṣaṇāni ca cittānuvartinaḥ kālaphalādiśubhatādibhiḥ
```

## 4. Grammar

The nominative subjects name mental factors, exactly two restraints, and marks belonging to the preceding group and to consciousness. *Cittānuvartinaḥ* predicates follower status of these groups. The instrumental compound says the following is in respects including time, result, and ethical status. The grammar preserves the open *ādi* in the verse; the Bhāṣya later specifies ten correspondences and the 58/54 causal counts.

```nltk-fcfg
% start S
# tokens: caittāḥ dvau saṃvarau teṣām cetasaḥ lakṣaṇāni ca cittānuvartinaḥ kālaphalādiśubhatādibhiḥ
S[SEM=<(?subjects & ?follower & ?respects)>] -> SUBJECTS[SEM=?subjects] FOLLOWERS[CASE=nom,NUM=pl,SEM=?follower] RESPECTS[CASE=inst,NUM=pl,OPEN=true,SEM=?respects]
SUBJECTS[SEM=<(?factors & ?restraints & ?marks)>] -> FACTORS[CASE=nom,NUM=pl,SEM=?factors] RESTRAINTS[CASE=nom,NUM=du,CNT=2,SEM=?restraints] MARKS[CASE=nom,NUM=pl,SEM=?marks]
FACTORS[CASE=nom,NUM=pl,SEM=<FollowerKind(mental_factors)>] -> 'caittāḥ'
RESTRAINTS[CASE=nom,NUM=du,CNT=2,SEM=<(FollowerKind(meditative_restraint) & FollowerKind(uncontaminated_restraint))>] -> TWO[CASE=nom,NUM=du,CNT=2] RESTRAINT[CASE=nom,NUM=du]
TWO[CASE=nom,NUM=du,CNT=2] -> 'dvau'
RESTRAINT[CASE=nom,NUM=du] -> 'saṃvarau'
MARKS[CASE=nom,NUM=pl,SEM=<(FollowerKind(group_marks) & FollowerKind(citta_marks) & MarkOf(group_marks,preceding_group) & MarkOf(citta_marks,citta))>] -> THEIR[CASE=gen,NUM=pl,REF=preceding_group] MIND[CASE=gen,NUM=sg,REF=citta] MARK[CASE=nom,NUM=pl] AND
THEIR[CASE=gen,NUM=pl,REF=preceding_group] -> 'teṣām'
MIND[CASE=gen,NUM=sg,REF=citta] -> 'cetasaḥ'
MARK[CASE=nom,NUM=pl] -> 'lakṣaṇāni'
AND -> 'ca'
FOLLOWERS[CASE=nom,NUM=pl,SEM=<all x.(FollowerKind(x) -> Follows(x,citta))>] -> 'cittānuvartinaḥ'
RESPECTS[CASE=inst,NUM=pl,OPEN=true,SEM=<all x.(FollowerKind(x) -> (TimeAligned(x,citta) & ResultAligned(x,citta) & EthicalAligned(x,citta)))>] -> 'kālaphalādiśubhatādibhiḥ'
```

```nltk-dep
'cittānuvartinaḥ' -> 'caittāḥ' | 'saṃvarau' | 'lakṣaṇāni' | 'kālaphalādiśubhatādibhiḥ'
'saṃvarau' -> 'dvau'
'lakṣaṇāni' -> 'teṣām' | 'cetasaḥ' | 'ca'
```

**Feature chart checkpoints.** The subject inventory spans [0, 7), the follower predicate [7, 8), and the instrumental respects [8, 9). The root yields one closed `SEM`. Changing the dual count, either genitive reference, or the instrumental case blocks this parse.

| Span | Constituent | Result |
|---|---|---|
| [0, 1) | `FACTORS` | mental factors |
| [1, 3) | `RESTRAINTS[CNT=2]` | exactly two restraints |
| [3, 7) | `MARKS` | marks of the group and of consciousness |
| [0, 9) | `S` | followers determined by stated respects |

## 5. Translation

### Literal Translation

> The mental factors, the two restraints, and the marks of those and of
> consciousness are followers of consciousness, by time, result, and the
> rest, and by wholesomeness and the rest.

### Bhāṣya-informed study translation

> The mental factors, the two restraints, and their marks, together with
> the marks of consciousness, follow consciousness in time, result, and
> ethical status, and related respects.

## 6. Philosophical Translation

> Consciousness and its followers share a determinate course in time, result, and ethical character. Their co-arising calls for a causal account, but co-arising alone does not settle which dharma is a cause of which.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| cittānuvartin | follower of consciousness | verse names the groups; Bhāṣya specifies ten correspondences |
| dhyāna-saṃvara / anāsrava-saṃvara | meditative / uncontaminated restraint | the two restraints named elliptically in the verse |
| lakṣaṇa / anulakṣaṇa | mark / secondary mark | Bhāṣya's 58/54 counts exclude consciousness's own secondary marks from the reverse direction |
| niḥṣyanda | homogeneous outflow | one shared result respect; distinct from *āsrava* (influx) |
| sahabhū / sahabhūhetu | co-arisen / co-arisen cause | co-arising is wider than this causal relation |
| satkāya-dṛṣṭi | identity-view | occurs in the Bhāṣya's cited objection, not in the verse |

## 8. Logical Determination

**Kārikā, derived.** The root `SEM` names the follower groups and states their alignment with consciousness in time, result, and ethical status. Its two occurrences of *ādi* remain open. The Bhāṣya expands those headings into ten respects and supplies the asymmetric counts of co-arisen causality; those prose claims are separate theories.

```nltk-sem
follower_respects : all x.(FollowerKind(x) -> (TimeAligned(x,citta) & ResultAligned(x,citta) & EthicalAligned(x,citta)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(((FollowerKind(mental_factors) & (FollowerKind(meditative_restraint) & FollowerKind(uncontaminated_restraint)) & (FollowerKind(group_marks) & FollowerKind(citta_marks) & MarkOf(group_marks,preceding_group) & MarkOf(citta_marks,citta))) & all x.(FollowerKind(x) -> Follows(x,citta))) & all x.(FollowerKind(x) -> (TimeAligned(x,citta) & ResultAligned(x,citta) & EthicalAligned(x,citta))))

# THEORY prose_ten_respects
# EXPECT prose_ten_respects T
all x.(Respect(x) -> (TimeRespect(x) | ResultRespect(x) | EthicalRespect(x)))
all x.(TimeRespect(x) -> (x = arising | x = persistence | x = cessation | x = period))
all x.(ResultRespect(x) -> (x = fruit | x = maturation | x = outflow))
all x.(EthicalRespect(x) -> (x = wholesome | x = unwholesome | x = indeterminate))
Respect(arising) & Respect(persistence) & Respect(cessation) & Respect(period) & Respect(fruit) & Respect(maturation) & Respect(outflow) & Respect(wholesome) & Respect(unwholesome) & Respect(indeterminate)

# THEORY prose_causal_directions
# EXPECT prose_causal_directions T
CausesCount(citta,fifty_eight) & CausedByCount(citta,fifty_four)
CountPart(fifty_eight,ten_major) & CountPart(fifty_eight,forty_marks) & CountPart(fifty_eight,eight_own_marks)
ExcludesReverse(citta,own_secondary_marks) & RejectedCount(fourteen)

# THEORY prose_coarisen_is_wider
# EXPECT prose_coarisen_is_wider T
all x.all y.(CoarisenCauseFor(x,y) -> CoarisenWith(x,y))
CoarisenWith(citta,own_secondary_marks) & -CoarisenCauseFor(own_secondary_marks,citta)

# THEORY rejected_one_restraint
# EXPECT rejected_one_restraint F
-FollowerKind(uncontaminated_restraint) & FollowerKind(meditative_restraint)

# THEORY rejected_same_genitive_referent
# EXPECT rejected_same_genitive_referent F
preceding_group = citta

# THEORY rejected_counts_symmetric
# EXPECT rejected_counts_symmetric F
CausesCount(citta,fifty_eight) & CausedByCount(citta,fifty_eight)

# THEORY rejected_fourteen
# EXPECT rejected_fourteen F
CausedByCount(citta,fourteen) & RejectedCount(fourteen)

# THEORY rejected_all_coarisen_are_causes
# EXPECT rejected_all_coarisen_are_causes F
all x.all y.(CoarisenWith(x,y) -> CoarisenCauseFor(x,y))
```

```nltk-valuation
citta => consciousness
preceding_group => factors_and_restraints
mental_factors => mental_factor_group
meditative_restraint => meditative_restraint_kind
uncontaminated_restraint => uncontaminated_restraint_kind
group_marks => marks_of_factors_and_restraints
citta_marks => marks_of_consciousness
own_secondary_marks => own_secondary_marks_kind
arising => arising_respect
persistence => persistence_respect
cessation => cessation_respect
period => period_respect
fruit => fruit_respect
maturation => maturation_respect
outflow => outflow_respect
wholesome => wholesome_respect
unwholesome => unwholesome_respect
indeterminate => indeterminate_respect
fifty_eight => fifty_eight_count
fifty_four => fifty_four_count
fourteen => fourteen_count
ten_major => ten_major_count
forty_marks => forty_marks_count
eight_own_marks => eight_own_marks_count
FollowerKind => {mental_factor_group,meditative_restraint_kind,uncontaminated_restraint_kind,marks_of_factors_and_restraints,marks_of_consciousness}
MarkOf => {(marks_of_factors_and_restraints,factors_and_restraints),(marks_of_consciousness,consciousness)}
Follows => {(mental_factor_group,consciousness),(meditative_restraint_kind,consciousness),(uncontaminated_restraint_kind,consciousness),(marks_of_factors_and_restraints,consciousness),(marks_of_consciousness,consciousness)}
TimeAligned => {(mental_factor_group,consciousness),(meditative_restraint_kind,consciousness),(uncontaminated_restraint_kind,consciousness),(marks_of_factors_and_restraints,consciousness),(marks_of_consciousness,consciousness)}
ResultAligned => {(mental_factor_group,consciousness),(meditative_restraint_kind,consciousness),(uncontaminated_restraint_kind,consciousness),(marks_of_factors_and_restraints,consciousness),(marks_of_consciousness,consciousness)}
EthicalAligned => {(mental_factor_group,consciousness),(meditative_restraint_kind,consciousness),(uncontaminated_restraint_kind,consciousness),(marks_of_factors_and_restraints,consciousness),(marks_of_consciousness,consciousness)}
Respect => {arising_respect,persistence_respect,cessation_respect,period_respect,fruit_respect,maturation_respect,outflow_respect,wholesome_respect,unwholesome_respect,indeterminate_respect}
TimeRespect => {arising_respect,persistence_respect,cessation_respect,period_respect}
ResultRespect => {fruit_respect,maturation_respect,outflow_respect}
EthicalRespect => {wholesome_respect,unwholesome_respect,indeterminate_respect}
CausesCount => {(consciousness,fifty_eight_count)}
CausedByCount => {(consciousness,fifty_four_count)}
CountPart => {(fifty_eight_count,ten_major_count),(fifty_eight_count,forty_marks_count),(fifty_eight_count,eight_own_marks_count)}
ExcludesReverse => {(consciousness,own_secondary_marks_kind)}
RejectedCount => {fourteen_count}
CoarisenCauseFor => {(consciousness,mental_factor_group),(consciousness,own_secondary_marks_kind)}
CoarisenWith => {(consciousness,mental_factor_group),(consciousness,own_secondary_marks_kind),(own_secondary_marks_kind,consciousness)}
```

The model checks the source's ten named respects and opposite causal directions, while the count predicates record the Bhāṣya's 58 = 10 + 40 + 8 and 54 with exclusions. They are finite witnesses to the stated accounting, not an arithmetic proof. The false theories reject conflating the two genitives, reversing the 58/54 distinction, restoring the refused fourteen, and treating every co-arisen relation as a co-arisen cause.

## 9. Interpretive Note

**Translation note.** The Bhāṣya specifies ten correspondences: shared arising, persistence, cessation, and period; shared fruit, maturation, and homogeneous outflow; and matching wholesome, unwholesome, or indeterminate status. The count is directional: the least consciousness is co-arisen cause for fifty-eight dharmas (ten major factors, forty marks, eight of its own marks and secondary marks), while fifty-four dharmas are co-arisen causes for it, excluding its own secondary marks. Another count of fourteen is refused. These figures belong to the Bhāṣya, not the kārikā's verse `SEM`.

The later exchange admits co-arising without the co-arisen-cause relation, and it disputes the inference from simultaneity alone to causation. The closing defense of co-arisen cause remains attributed to the Bhāṣya's argument; it does not erase the objection. The next question introduces homogeneous cause. The Sanskrit witness still requires collation.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_51 a vak:Karika ; vak:hasTopic vak:FollowersOfConsciousness .
vak:CoArisen vak:widerThanCause true .
```
