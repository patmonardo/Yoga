# VAK_8.16 — Defiled Predecessors, Prior Resolve, and Death-Time Succession

## 1. Sanskrit (Devanāgarī)

```sanskrit
क्लिष्टात् स्वं शुद्धकं क्लिष्टम् एवं चाधरशुद्धकम् ।
च्युतौ तु शुद्धकात् क्लिष्टं सर्वं क्लिष्टात् तु नोत्तरम् ॥ ८.१६ ॥
```

## 2. Sanskrit (IAST)

```text
kliṣṭāt svaṃ śuddhakaṃ kliṣṭam evaṃ cādharaśuddhakam |
cyutau tu śuddhakāt kliṣṭaṃ sarvaṃ kliṣṭāt tu nottaram || 8.16 ||
```

The verse follows the local kārikā witness. The
Bhāṣya explicitly distinguishes attainment-time from
death-time and qualifies the pure predecessor in
the latter case as acquired through rebirth.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `kliṣṭāt` | ablative singular neuter | immediately after a defiled attainment |
| `svam` | nominative singular neuter adjective | of its own level |
| `śuddhakam` | nominative singular neuter | pure [attainment] |
| `kliṣṭam` | nominative singular neuter | defiled [attainment or state] |
| `evam` | adverb | likewise |
| `ca` | conjunction | and |
| `adharaśuddhakam` | nominative singular neuter compound | a lower-level pure attainment |
| `cyutau` | locative singular of cyuti | at death |
| `tu` | contrast particle | however |
| `śuddhakāt` | ablative singular neuter | after a pure [state] |
| `sarvam` | nominative singular neuter adjective | all; here extending across levels |
| `na uttaram` | negation and nominative singular neuter adjective | not a higher-level [defiled state] |

`Ca + adhara-` yields `cādhara-`; `na + uttaram`
yields `nottaram`. The recurring ablatives mark the
predecessor, while the nominatives name possible successors.

## 4. Grammar

The first succession applies at attainment-time; cyutau introduces the separate death-time rule, and the prose supplies the omitted arising verbs.

```nltk-fcfg
% start S
# tokens: kliṣṭāt ∅-utpadyete svaṃ śuddhakaṃ kliṣṭam evaṃ cādharaśuddhakam cyutau tu śuddhakāt ∅-utpadyate kliṣṭaṃ sarvaṃ kliṣṭāt tu nottaram ∅-utpadyate
S -> CL[K=attainment_time] CL[K=death_pure] CL[K=death_defiled]
CL[K=attainment_time] -> PREP[CASE=abl] V[PERS=3,NUM=du,TENSE=pres,VOICE=mid,SUPPLIED=prose] ADJ[CASE=nom,NUM=?n,GEN=?g,LEVEL=same] N[CASE=nom,NUM=?n,GEN=?g,MODE=pure] N[CASE=nom,NUM=?n,GEN=?g,MODE=defiled] ADV[ANAPH=likewise] ADJ[CASE=nom,NUM=sg,GEN=n,LEVEL=lower,MODE=pure]
CL[K=death_pure] -> LOC[CASE=loc,EVENT=death] PTCL[CONTRAST=yes] PREP[CASE=abl,MODE=pure] V[PERS=3,NUM=sg,TENSE=pres,VOICE=mid,SUPPLIED=prose] N[CASE=nom,NUM=?n,GEN=?g,MODE=defiled] ADJ[CASE=nom,NUM=?n,GEN=?g,DOMAIN=all_levels]
CL[K=death_defiled] -> PREP[CASE=abl,MODE=defiled] PTCL[CONTRAST=yes] ADJ[CASE=nom,NUM=sg,GEN=n,DOMAIN=not_higher] V[PERS=3,NUM=sg,TENSE=pres,VOICE=mid,SUPPLIED=prose]
PREP[CASE=abl] -> 'kliṣṭāt'
V[PERS=3,NUM=du,TENSE=pres,VOICE=mid,SUPPLIED=prose] -> '∅-utpadyete'
ADJ[CASE=nom,NUM=sg,GEN=n,LEVEL=same] -> 'svaṃ'
N[CASE=nom,NUM=sg,GEN=n,MODE=pure] -> 'śuddhakaṃ'
N[CASE=nom,NUM=sg,GEN=n,MODE=defiled] -> 'kliṣṭam'
ADV[ANAPH=likewise] -> 'evaṃ'
ADJ[CASE=nom,NUM=sg,GEN=n,LEVEL=lower,MODE=pure] -> 'cādharaśuddhakam'
LOC[CASE=loc,EVENT=death] -> 'cyutau'
PTCL[CONTRAST=yes] -> 'tu'
PREP[CASE=abl,MODE=pure] -> 'śuddhakāt'
V[PERS=3,NUM=sg,TENSE=pres,VOICE=mid,SUPPLIED=prose] -> '∅-utpadyate'
N[CASE=nom,NUM=sg,GEN=n,MODE=defiled] -> 'kliṣṭaṃ'
ADJ[CASE=nom,NUM=sg,GEN=n,DOMAIN=all_levels] -> 'sarvaṃ'
PREP[CASE=abl,MODE=defiled] -> 'kliṣṭāt'
ADJ[CASE=nom,NUM=sg,GEN=n,DOMAIN=not_higher] -> 'nottaram'
```

```nltk-dep
'∅-utpadyete' -> 'kliṣṭāt' | 'śuddhakaṃ' | 'kliṣṭam' | 'svaṃ'
'śuddhakaṃ' -> 'cādharaśuddhakam' | 'evaṃ'
'∅-utpadyate' -> 'cyutau' | 'śuddhakāt' | 'kliṣṭaṃ' | 'sarvaṃ' | 'nottaram'
'kliṣṭaṃ' -> 'kliṣṭāt' | 'tu'
```

The lower successor is pure, with no stated level-distance; the prose explains it
through prior resolve, not a newly interposed delimitation. Sarvam ranges over possible
defiled levels, not simultaneous states, and the final ban is immediate, not permanent.

**Close construe.** After a defiled attainment arise
the same-level pure or defiled attainment, and also
a lower pure attainment. At death, however, a pure
predecessor permits defiled succession across levels;
a defiled predecessor does not permit a higher-level
defiled successor.

## 5. Translation

### Literal Translation

> After a defiled [attainment], its own pure and
> defiled [attainments], and likewise a lower pure
> [attainment]. At death, however, after a pure
> [state], every [level of] defiled [state]; after
> a defiled [state], however, not a higher one.

### Bhāṣya-informed study translation

> After a defiled attainment, a pure or defiled attainment of its own
> level arises, and likewise a lower pure attainment. At the time of
> death, however, after a pure attainment acquired through rebirth a
> defiled state of any level may arise, while after a defiled
> attainment no higher defiled state arises.

## 6. Philosophical Translation

> Level, mode, and occasion jointly determine the
> permitted successor. A lower pure attainment can
> be preferred to a higher defiled one. The commentary
> explains this transition through a resolve formed
> earlier and continuing to influence the stream.
> At death, a different level-range applies to defiled
> succession than during attainment.

The account distinguishes an immediate predecessor
from an earlier conditioning intention. It does not
make temporal adjacency a complete explanation of
why the successor occurs.

## 7. Technical Vocabulary

**Source.** Pradhan 444|09–445|02, checked against the local Bhāṣya
study and running source. The explanation by prior resolve belongs to
the lower-pure transition and is developed in the Bhāṣya.

**`Samāpattikāla`.** Attainment-time, the context to
which the first succession rules apply. The prose
explicitly places the same-level restriction on defiled
successors within this context.

**`Cyutikāla`.** Death-time. This introduces a separate
rule and must not be confused with ending a meditation
session or losing an attainment through decline.

**`Upapattilābhika`.** Acquired through rebirth. This
qualifies the pure predecessor in the death-time
rule. Omitting it would generalize beyond the stated case.

**`Kleśotpīḍita`.** Oppressed by defilements. The commentary
uses this condition to explain why a practitioner
values a lower pure attainment over a higher defiled one.

**`Pūrvāvedha`.** Prior impulse or previously established
momentum. The answer invokes this to explain a
transition that need not wait for a new, immediately
preceding wholesome deliberation.

**`Pūrvābhiprāya`.** Prior intention or resolve. The
continuum follows an earlier preference for lower
purity over higher defilement.

**`Saṃtati`.** Continuum or stream. It is the continuity
through which the earlier intention bears on the
later transition in the commentary's explanation.

## 8. Logical Determination

**Attainment-time successors of a defiled predecessor.**

| Successor mode | Level relation | Status in this passage |
|---|---|---|
| Pure | Same | Permitted |
| Defiled | Same | Permitted |
| Pure | Lower | Permitted, with prior-resolve explanation |
| Uncontaminated | Any | Immediate succession excluded |

The prose also restates that a defiled successor
after either a pure or defiled predecessor during
attainment belongs to the same level, not another.
The lower exception concerns a pure successor.

**The objection concerns immediacy.** If the practitioner
first discriminates or delimits the defiled condition
and then turns downward, the move would proceed
from a wholesome state, not immediately from the
defiled one. If that discrimination does not occur,
how does the transition take place? The objection
must remain visible: it is not merely advice to
interrupt defilement and then choose another attainment.

**The answer invokes an earlier resolve.** Previously,
the practitioner has preferred a lower pure attainment
to a higher defiled one. The stream follows that
prior intention. The commentary compares this to
someone who resolves before sleeping to awaken at
a particular time and then awakens as intended.
This is an explanatory analogy, not a guarantee
that every resolve unfailingly produces its object.

**The two temporal relations.** The defiled attainment
is the immediate predecessor; the previously formed
resolve supplies the explanation of the subsequent
lower-pure transition. A new intervening wholesome
act of discrimination would change which predecessor
is immediate. The Bhāṣya answers that difficulty
without abandoning the immediate-succession claim.

**Death-time defiled successors.**

| Predecessor at death | Possible level of defiled successor |
|---|---|
| Pure, acquired through rebirth | Any level, as a general range |
| Defiled dhyāna or ārūpya | Same or lower level; not higher |

This table expresses permissions and exclusions. It
does not say a person can choose any rebirth at
will, or give an exhaustive account of all conditions
determining rebirth. The source specifies the level-range
of the defiled successor in the stated cases.

**Immediate exclusion has a precise scope.** The prose
emphatically excludes uncontaminated attainment immediately
after a defiled attainment. That does not mean a
person who has had a defiled attainment can never
subsequently attain an uncontaminated one through
an intervening sequence.

## 9. Interpretive Note

**Two tables are necessary.** Merging the death-time
and attainment-time rules would falsely permit other-level
defiled successors within the ordinary meditative rule.
The commentary explicitly marks the change of context;
the exposition and formal seed retain it.

**Refinements of the research reading.** The lower-pure
successor is retained without silently imposing an
adjacent-level-only condition. The death-time pure
predecessor retains its rebirth-acquired qualification.
The question concerning discrimination of defilement
is treated as an objection about immediate succession,
followed by the answer from prior resolve.

**Witness control.** The local verse and quoted running
source agree on the operative clauses. The prose
supplies the otherwise elliptical arising verbs,
expands sarvam as a level-range, and resolves nottaram
as exclusion of a higher-level defiled successor.
No emendation of the research files is needed.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates predecessor, successor, level,
mode, occasion, and earlier conditioning resolve.
Yoga Technē, its kriyā–karma companion, concerns the
effective exercise through which a prior determination
can bear on a later transition. The source's account
keeps that earlier conditioning distinct from the
immediately preceding defiled state.

For Organon representation, attach a context to each
succession permission and retain the prior-intention
explanation separately from the adjacency relation.
A single unqualified arrow would conceal both distinctions.
This is project reconstruction, not a further causal
system attributed to Vasubandhu.

**Review status.** Provisional, Bhāṣya-controlled study.
The same-level alternatives, lower-pure transition,
objection and prior-resolve answer, sleeping analogy,
uncontaminated exclusion, and qualified death-time rules
have been checked against the local research and
running source.

## 10. OWL++ Seed

```text
Class: SuccessionPermission
Class: TransitionContext
Class: PriorResolve
Class: AttainmentMode

ObjectProperty: hasPredecessorMode
ObjectProperty: hasSuccessorMode
ObjectProperty: appliesInContext
ObjectProperty: hasLevelRelation
ObjectProperty: explainedByPriorResolve

DefiledPredecessorAtAttainmentTime:
    permittedSuccessors: SameLevelPure, SameLevelDefiled, LowerPure
    immediateUncontaminatedSuccessor: forbidden

LowerPureTransitionExplanation:
    priorPreference: LowerPureOverHigherDefiled
    analogy: AwakeningAtPreviouslyIntendedTime

PurePredecessorAtDeathTime:
    requiredQualification: AcquiredThroughRebirth
    defiledSuccessorLevelRange: AllLevels

DefiledPredecessorAtDeathTime:
    defiledSuccessorLevelRange: SameOrLower
    higherDefiledSuccessor: forbidden

ProjectConstraint: Keep attainment-time and death-time rules separate.
ProjectConstraint: Preserve rebirth-acquired in the pure death-time case.
ProjectConstraint: Prior conditioning and immediate succession are distinct.
ProjectConstraint: Lower pure does not mean lower defiled.
ProjectConstraint: Do not add an adjacent-level-only restriction without support.
ProjectConstraint: A possible successor is not an inevitable successor.
ProjectConstraint: Immediate exclusion does not assert permanent impossibility.
```

This is a declarative project seed, not executable OWL.
VAK 8.17 next distinguishes the subtypes of pure
attainment and further qualifies their succession possibilities.
