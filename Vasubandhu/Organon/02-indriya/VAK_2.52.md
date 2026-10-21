# VAK_2.52 — Homogeneous Cause

## 1. Sanskrit (Devanāgarī)

```sanskrit
सभागहेतुः सदृशाः स्वनिकायभुवोऽग्रजाः ।
अन्योऽन्यं नवभूमिस्तु मार्गः समविशिष्टयोः ॥ २.५२ ॥
```

## 2. Sanskrit (IAST)

```text
sabhāgahetuḥ sadṛśāḥ svanikāyabhuvo 'grajāḥ /
anyo 'nyaṃ navabhūmis tu mārgaḥ samaviśiṣṭayoḥ // 2.52 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sabhāga-hetuḥ | masculine nominative singular compound | heading for the homogeneous-cause definition |
| sadṛśāḥ | masculine nominative plural adjective | similar dharmas; the Bhāṣya supplies their causal relation |
| sva-nikāya-bhuvaḥ | masculine nominative plural compound adjective | same class and level in the ordinary case; the Bhāṣya scopes this restriction to influx-bearing dharmas |
| agrajāḥ | masculine nominative plural adjective | arisen earlier than the effect; excludes a future homogeneous cause |
| anyo 'nyam | reciprocal pronouns, nominative and accusative singular after sandhi | across Path instances; direction remains constrained by priority |
| nava-bhūmiḥ mārgaḥ | masculine nominative singular compound + masculine nominative singular | Path across nine levels, the exception to the ordinary same-level rule |
| sama-viśiṣṭayoḥ | genitive dual compound adjective | of an equal or superior result; conflicts with one following witness line |

**Grammar tokens.** Sandhi is opened at *anyo ’nyam* and *navabhūmis tu*; *svanikāyabhuvaḥ* is normalized from *svanikāyabhuvo ’grajāḥ*. The plural qualities define the singular heading *sabhāgahetuḥ* by ellipsis. The Path clause relaxes only the same-level requirement; temporal priority remains operative in the Bhāṣya.

```text
# tokens: sabhāgahetuḥ sadṛśāḥ svanikāyabhuvaḥ agrajāḥ anyaḥ anyam navabhūmiḥ tu mārgaḥ samaviśiṣṭayoḥ
```

## 4. Grammar

```nltk-fcfg
% start S
# tokens: sabhāgahetuḥ sadṛśāḥ svanikāyabhuvaḥ agrajāḥ anyaḥ anyam navabhūmiḥ tu mārgaḥ samaviśiṣṭayoḥ
S[SEM=<(?ordinary & ?path)>] -> ORDINARY[SEM=?ordinary] PATH_CLAUSE[SEM=?path]
ORDINARY[SEM=<(Similar(ordinary_cause,ordinary_result) & SameClass(ordinary_cause,ordinary_result) & SameLevel(ordinary_cause,ordinary_result) & Prior(ordinary_cause,ordinary_result))>] -> HEAD[CASE=nom,NUM=sg] SIMILAR[CASE=nom,NUM=pl] OWN[CASE=nom,NUM=pl,CLASS=own,LEVEL=own] PRIOR[CASE=nom,NUM=pl,TIME=prior]
HEAD[CASE=nom,NUM=sg] -> 'sabhāgahetuḥ'
SIMILAR[CASE=nom,NUM=pl] -> 'sadṛśāḥ'
OWN[CASE=nom,NUM=pl,CLASS=own,LEVEL=own] -> 'svanikāyabhuvaḥ'
PRIOR[CASE=nom,NUM=pl,TIME=prior] -> 'agrajāḥ'
PATH_CLAUSE[SEM=<(NineLevels(path) & PathCauseFor(path_cause,path_equal) & PathCauseFor(path_cause,path_superior) & CrossLevel(path_cause,path_superior) & EqualGrade(path_cause,path_equal) & SuperiorGrade(path_superior,path_cause) & Prior(path_cause,path_equal) & Prior(path_cause,path_superior))>] -> RECIPROCAL[CASE=nom,ACC=acc] NINE[CASE=nom,NUM=sg,COUNT=9] CONTRAST PATH[CASE=nom,NUM=sg] RANGE[CASE=gen,NUM=du,GRADES=equal_superior]
RECIPROCAL[CASE=nom,ACC=acc] -> OTHER_NOM[CASE=nom] OTHER_ACC[CASE=acc]
OTHER_NOM[CASE=nom] -> 'anyaḥ'
OTHER_ACC[CASE=acc] -> 'anyam'
NINE[CASE=nom,NUM=sg,COUNT=9] -> 'navabhūmiḥ'
CONTRAST -> 'tu'
PATH[CASE=nom,NUM=sg] -> 'mārgaḥ'
RANGE[CASE=gen,NUM=du,GRADES=equal_superior] -> 'samaviśiṣṭayoḥ'
```

```nltk-dep
'sabhāgahetuḥ' -> 'sadṛśāḥ' | 'svanikāyabhuvaḥ' | 'agrajāḥ'
'mārgaḥ' -> 'anyaḥ' | 'navabhūmiḥ' | 'tu' | 'samaviśiṣṭayoḥ'
'anyaḥ' -> 'anyam'
```

**Feature chart checkpoints.** The ordinary definition spans [0, 4); the reciprocal Path exception spans [4, 10). One root `SEM` holds the ordinary same-class/same-level/prior relation and the Path's equal/superior cases, including an allowed cross-level case. The `COUNT`, `GRADES`, case, and prior-time features constrain their respective constituents.

| Span | Constituent | Result |
|---|---|---|
| [0, 4) | `ORDINARY` | similar, own class and level, prior |
| [4, 6) | `RECIPROCAL` | nominative and accusative participants |
| [6, 10) | Path restriction | nine levels, equal or superior |
| [0, 10) | `S` | ordinary definition and Path exception |

## 5. Translation

### Literal Translation

> Homogeneous causes are similar, of their own class and level, and
> prior-born. The Path of nine levels is of one another, at the equal and
> superior levels.

### Bhāṣya-informed study translation

> A homogeneous cause is similar, of its own class and level, and
> prior-born. The Path crosses the nine levels as cause for the equal or
> the superior.

## 6. Philosophical Translation

> Similarity becomes a homogeneous causal relation only with a direction: an earlier dharma conditions a later one. The ordinary case retains its own class and level; the Path can connect levels while retaining priority and the equal-or-superior range stated by the verse.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| sabhāga-hetu | homogeneous cause | similarity plus causal priority, not resemblance alone |
| agraja | prior-born | earlier than its effect; future dharmas cannot satisfy it here |
| āgantuka | adventitious | Bhāṣya reason the Path is not appropriated by craving of one level |
| hetūpacaya | accumulation of causes | Bhāṣya explains superiority through faculties and accumulated causes |

## 8. Logical Determination

**Kārikā, derived.** The root `SEM` records the ordinary definition and the Path exception. The ordinary same-class/same-level condition is not copied into the Path clause. The Path's priority and cross-level permission are resolved through the Bhāṣya.
An equal-grade example is not thereby forced to cross levels. These named examples witness the verse's positive cases; they do not settle the contradictory prose line about an inferior result.

```nltk-sem
ordinary : Similar(ordinary_cause,ordinary_result) & SameClass(ordinary_cause,ordinary_result) & SameLevel(ordinary_cause,ordinary_result) & Prior(ordinary_cause,ordinary_result)
path : NineLevels(path) & PathCauseFor(path_cause,path_equal) & PathCauseFor(path_cause,path_superior) & CrossLevel(path_cause,path_superior) & EqualGrade(path_cause,path_equal) & SuperiorGrade(path_superior,path_cause) & Prior(path_cause,path_equal) & Prior(path_cause,path_superior)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(Similar(ordinary_cause,ordinary_result) & SameClass(ordinary_cause,ordinary_result) & SameLevel(ordinary_cause,ordinary_result) & Prior(ordinary_cause,ordinary_result)) & (NineLevels(path) & PathCauseFor(path_cause,path_equal) & PathCauseFor(path_cause,path_superior) & CrossLevel(path_cause,path_superior) & EqualGrade(path_cause,path_equal) & SuperiorGrade(path_superior,path_cause) & Prior(path_cause,path_equal) & Prior(path_cause,path_superior))

# THEORY prose_prior_not_future
# EXPECT prose_prior_not_future T
all x.all y.(HomogeneousCause(x,y) -> Prior(x,y)) & -HomogeneousCause(future_cause,ordinary_result)

# THEORY prose_path_adventitious
# EXPECT prose_path_adventitious T
Adventitious(path) & -AppropriatedAtOneLevel(path)

# THEORY rejected_similarity_alone
# EXPECT rejected_similarity_alone F
HomogeneousCause(similar_wrong_class,ordinary_result) & Similar(similar_wrong_class,ordinary_result)

# THEORY rejected_ordinary_cross_class
# EXPECT rejected_ordinary_cross_class F
SameClass(similar_wrong_class,ordinary_result) & Similar(similar_wrong_class,ordinary_result)

# THEORY rejected_ordinary_cross_level
# EXPECT rejected_ordinary_cross_level F
SameLevel(similar_wrong_level,ordinary_result) & Similar(similar_wrong_level,ordinary_result)

# THEORY rejected_future_cause
# EXPECT rejected_future_cause F
HomogeneousCause(future_cause,ordinary_result) & -Prior(future_cause,ordinary_result)

# THEORY rejected_path_same_level_only
# EXPECT rejected_path_same_level_only F
SameLevel(path_cause,path_superior) & CrossLevel(path_cause,path_superior)

# THEORY rejected_path_drops_priority
# EXPECT rejected_path_drops_priority F
-Prior(path_cause,path_superior)
```

```nltk-valuation
ordinary_cause => oc
ordinary_result => or
similar_wrong_class => wc
similar_wrong_level => wl
future_cause => fc
path => p
path_cause => pc
path_equal => pe
path_superior => ps
Similar => {(oc,or),(wc,or),(wl,or),(pc,pe),(pc,ps)}
SameClass => {(oc,or),(wl,or)}
SameLevel => {(oc,or),(wc,or)}
Prior => {(oc,or),(wc,or),(wl,or),(pc,pe),(pc,ps)}
HomogeneousCause => {(oc,or),(pc,pe),(pc,ps)}
NineLevels => {p}
PathCauseFor => {(pc,pe),(pc,ps)}
CrossLevel => {(pc,ps)}
EqualGrade => {(pc,pe)}
SuperiorGrade => {(ps,pc)}
Adventitious => {p}
AppropriatedAtOneLevel => {}
```

The finite model witnesses the positive ordinary and Path cases and rejects similarity without the ordinary class/level restriction, a future cause, and a Path case that discards priority. The equal-grade case
remains level-neutral; the model witnesses one cross-level superior case. It deliberately does not decide the printed *nyūnasya hetur bhavati* at [087|11]: the verse and the later *na nyūnasya* at [087|23] conflict with that line. A collation is needed before turning the inferior case into a source-grounded negative theory.

## 9. Interpretive Note

The Bhāṣya treats *sabhāgahetu* as a prior similar dharma causing a later one, not similarity by itself. For influx-bearing dharmas, it restricts the relation to the same class and level. It refuses a future homogeneous cause because homogeneous outflow needs earlier and later; its comparison with maturation cause is a distinct argument. The Path, described as *āgantuka* (adventitious), crosses its nine levels because it is not appropriated by the craving of one level. The Bhāṣya still uses prior arising when describing the Path case.

**Source conflict.** The kārikā's *samaviśiṣṭayoḥ* says “of the equal and superior”; examples at [087|11–14] run in that direction. The source witness nevertheless prints *nyūnasya hetur bhavati* at [087|11], “is a cause of the inferior,” while [087|23] explicitly prints *na nyūnasya*. No negative has been supplied to [087|11] here. The verse translation follows the verse; whether [087|11] is corrupt remains open pending collation. Worldly qualities produced by application belong to the next verse.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_52 a vak:Karika ; vak:hasTopic vak:HomogeneousCause .
vak:PathSabhaga vak:spansNineLevels true .
```
