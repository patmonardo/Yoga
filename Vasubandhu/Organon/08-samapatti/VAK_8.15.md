# VAK_8.15 — Immediate Successors of Wholesome Attainments

## 1. Sanskrit (Devanāgarī)

```sanskrit
तृतीयाद्यावदूर्ध्वाधोऽनास्रवानन्तरं शुभम् ।
उत्पद्यते तथा शुद्धात् क्लिष्टं चापि स्वभूमिकम् ॥ ८.१५ ॥
```

## 2. Sanskrit (IAST)

```text
tṛtīyādyāvad ūrdhvādho 'nāsravānantaraṃ śubham |
utpadyate tathā śuddhāt kliṣṭaṃ cāpi svabhūmikam || 8.15 ||
```

The Sanskrit follows the local kārikā study, which
explicitly normalizes the running source's `kliṭaṃ`
to `kliṣṭaṃ`. The prose's repeated kliṣṭa forms support
that reading. The compressed opening is retained;
its range is determined by the commentary's examples.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `tṛtīyāt` | ablative singular ordinal | the third, marking the limit in the compressed expression |
| `yāvat` | limiting particle | as far as; up to |
| `ūrdhvādhaḥ` | paired adverbial expression | upward and downward |
| `anāsravānantaram` | adverbial compound | immediately after an uncontaminated attainment |
| `śubham` | nominative singular neuter | wholesome [attainment] |
| `utpadyate` | third-person singular present middle of ud-√pad | arises |
| `tathā` | adverb | likewise; in the same manner |
| `śuddhāt` | ablative singular neuter | after a pure attainment |
| `kliṣṭam` | nominative singular neuter | defiled [attainment] |
| `ca api` | additive particles | and also |
| `svabhūmikam` | nominative singular neuter adjective | belonging to the same level |

`Tṛtīyāt + yāvat` yields `tṛtīyād yāvat` in the
continuous text. It should not be segmented into
“third and following.” `Yāvat + ūrdhva-` yields
`yāvad ūrdhva-`; `adhaḥ + anāsrava-` yields
`adho 'nāsrava-`; `ca + api` yields `cāpi`.

## 4. Grammar

The first clause limits successors by distance; the second carries that wholesome rule forward and adds a same-level defiled successor.

```nltk-fcfg
% start S
# tokens: tṛtīyādyāvad ūrdhvādho anāsravānantaram śubham utpadyate tathā śuddhāt ∅-śubham ∅-utpadyate kliṣṭaṃ cāpi svabhūmikam
S -> CL[K=after_uncontaminated] CL[K=after_pure]
CL[K=after_uncontaminated] -> LIMIT[COUNT=relative] RANGE[DIR=both] PREP[REL=after] N[CASE=nom,NUM=?n,GEN=?g,QUAL=wholesome] V[PERS=3,NUM=?n,TENSE=pres,VOICE=mid]
CL[K=after_pure] -> ADV[ANAPH=anaphoric] PREP[CASE=abl] N[CASE=nom,NUM=sg,GEN=n,SUPPLIED=prose,QUAL=wholesome] V[PERS=3,NUM=sg,TENSE=pres,VOICE=mid,SUPPLIED=prose] N[CASE=nom,NUM=?n,GEN=?g,QUAL=defiled] ADD[FORCE=also] ADJ[CASE=nom,NUM=?n,GEN=?g,LEVEL=same]
LIMIT[COUNT=relative] -> 'tṛtīyādyāvad'
RANGE[DIR=both] -> 'ūrdhvādho'
PREP[REL=after] -> 'anāsravānantaram'
N[CASE=nom,NUM=sg,GEN=n,QUAL=wholesome] -> 'śubham'
V[PERS=3,NUM=sg,TENSE=pres,VOICE=mid] -> 'utpadyate'
ADV[ANAPH=anaphoric] -> 'tathā'
PREP[CASE=abl] -> 'śuddhāt'
N[CASE=nom,NUM=sg,GEN=n,SUPPLIED=prose,QUAL=wholesome] -> '∅-śubham'
V[PERS=3,NUM=sg,TENSE=pres,VOICE=mid,SUPPLIED=prose] -> '∅-utpadyate'
N[CASE=nom,NUM=sg,GEN=n,QUAL=defiled] -> 'kliṣṭaṃ'
ADD[FORCE=also] -> 'cāpi'
ADJ[CASE=nom,NUM=sg,GEN=n,LEVEL=same] -> 'svabhūmikam'
```

```nltk-dep
'utpadyate' -> 'śubham' | 'anāsravānantaram' | 'ūrdhvādho' | 'tṛtīyādyāvad'
'∅-utpadyate' -> '∅-śubham' | 'śuddhāt' | 'tathā' | 'kliṣṭaṃ'
'kliṣṭaṃ' -> 'cāpi' | 'svabhūmikam'
```

The limit counts the starting level as first (at most two level-steps); same-level
successions remain included. Tathā resumes the wholesome successors, not a new
unrestricted rule; svabhūmika qualifies only the added defiled item.

**Close construe.** Immediately after an uncontaminated
attainment, wholesome attainment arises on the same
level or within two levels above or below. Likewise
after a pure attainment; additionally, a defiled
attainment of its own level may arise.

## 5. Translation

### Literal Translation

> Immediately after an uncontaminated [attainment],
> a wholesome [attainment] arises upward or downward
> as far as the third. Likewise after a pure
> [attainment]; also a defiled [attainment] belonging
> to its own level.

### Bhāṣya-informed study translation

> Immediately after an uncontaminated attainment, a wholesome
> attainment, whether pure or uncontaminated, arises on the same
> level or upward or downward as far as the third, counting the
> starting level as the first. Likewise after a pure attainment, and
> in addition a defiled attainment belonging to its own level may
> arise.

## 6. Philosophical Translation

> An attainment is situated not only by its level
> and mode but also by its permitted immediate successors.
> A change of level can preserve wholesomeness; a
> change from pure to defiled can occur on the same
> level. Uncontaminated attainment excludes that immediate
> defiled successor.

“May follow” describes a permitted succession, not
an inevitable event. The prohibition concerns immediate
succession and does not by itself settle every later
state in a person's continuum.

## 7. Technical Vocabulary

**Source.** Pradhan 443|13–444|08, checked against the local Bhāṣya
study and running source. These are general mode-and-level rules: at the
summit of existence only the pure mode is available; entry into the
formless attainments follows anvayajñāna; later analysis differentiates
pure attainments by subtype.

**`Anantara / samanantara`.** Immediately following.
This concerns the next occurrence, not simply an
attainment reached eventually through intermediate states.
It differs from VAK 8.14's acquisition of possession.

**`Śubha`.** Wholesome, encompassing pure and uncontaminated
attainments in this passage. Translating it as pure
alone would remove half of the stated alternatives.

**`Śuddha`.** Pure but contaminated. Its possible
same-level defiled successor distinguishes it here
from anāsrava. The later subtype analysis prevents
treating every pure attainment as interchangeable.

**`Vyutkrāntaka-samāpatti`.** Attainment involving skipping
levels. The prose invokes these practitioners to
explain the upper bound on a leap. It does not
state that any practitioner can perform every permitted transition.

**`Anvayajñāna / dharmajñāna`.** The established knowledge
categories from Chapter 7. In the uncontaminated predecessor
context, formless attainments are entered after anvayajñāna,
not dharmajñāna; the latter's lower support and object
supply the stated reason.

**`Samāpattidravya`.** A distinct attainment item in
the present enumeration, specified by level and mode.
The counts here are not the eleven distinct dhyāna
factors of VAK 8.09.

## 8. Logical Determination

The verse restricts which wholesome attainments may immediately follow, then permits a same-level defiled successor only after a pure predecessor. The relation records permission, not inevitable succession. Provenance: `[verse]`, `[prose]`.

**Signature.** `MayWholesomeFollow/2(p,s)`, `MayDefiledFollow/2(p,s)`—s is a permitted immediate successor of p in the named mode; `Uncontaminated/1`, `Pure/1`, `Wholesome/1`, `Defiled/1`—attainment mode; `WithinTwo/2(p,s)`—bounded level range; `SameLevel/2(p,s)`—same level.

**Dataset (selected permitted pairs).** The pair relation is the finite matrix side; no person or actual sequence is asserted.

```nltk-valuation
uncontamPred => uncontamPred
purePred => purePred
wholesomeSame => wholesomeSame
wholesomeTwo => wholesomeTwo
defiledSame => defiledSame
Uncontaminated => {uncontamPred}
Pure => {purePred}
Wholesome => {wholesomeSame,wholesomeTwo}
Defiled => {defiledSame}
WithinTwo => {(uncontamPred,wholesomeSame),(uncontamPred,wholesomeTwo),(purePred,wholesomeSame),(purePred,wholesomeTwo)}
SameLevel => {(purePred,defiledSame)}
MayWholesomeFollow => {(uncontamPred,wholesomeSame),(uncontamPred,wholesomeTwo),(purePred,wholesomeSame),(purePred,wholesomeTwo)}
MayDefiledFollow => {(purePred,defiledSame)}
```

```nltk-fol
# THEORY shared
# [verse] śubha after anāsrava within the bounded level range
all p.all s.((MayWholesomeFollow(p,s) & Uncontaminated(p)) -> (Wholesome(s) & WithinTwo(p,s)))
# [verse] tathā carries the wholesome permission after śuddha
all p.all s.((MayWholesomeFollow(p,s) & Pure(p)) -> (Wholesome(s) & WithinTwo(p,s)))
# [verse] only the additional kliṣṭa successor is restricted to its own level
all p.all s.((MayDefiledFollow(p,s) & Pure(p)) -> (Defiled(s) & SameLevel(p,s)))
```

**Results (NLTK).** The session checker evaluates all three rules against the finite permission matrix. The matrix leaves out any defiled successor after an uncontaminated predecessor; the formalization does not turn “may follow” into “must follow.”

**Scope cautions.** The counted limit treats the starting ground as first, following the Bhāṣya. Special restrictions on formless entry after *anvayajñāna*, skipping practitioners, and attainment subtypes are not generalized here. Later states after intervening moments are outside `May…Follow`. `WithinTwo` abstracts the symmetric level bound; it does not encode a signed upward or downward trajectory.

## 9. Interpretive Note

**Corrections to the research first pass.** Its vague
“third and following” obscures the bounded range,
and its shortened pure-successor account can omit
uncontaminated successors. The commentary's examples,
definition of śubha, and `śeṣaṃ yathaivānāsravāt`
control the fuller reading here. Originals remain intact.

**Witness cautions.** The running source prints
`tṛtīvādyāvat` in prose and `kliṭaṃ` in the second
half of the verse. The local kārikā regularizes the
latter with notice. The preceding verse line, explicit
third-level limit, and enumerated examples secure the
range without relying on the irregular prose spelling.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates the predecessor, successor,
level-distance, mode, and knowledge-condition. Yoga
Technē, its kriyā–karma companion, concerns the effective
exercise of succession within those conditions. A
list of attainable levels alone does not specify
which passage from one to another is admissible.

For Organon representation, retain the directed relation
and its conditions. Separate the general permission
from an assertion that a particular transition actually
occurred. Include mode availability at the destination
and preserve later subtype refinements. This is a
project reconstruction, not a software architecture
attributed to the source.

**Review status.** Provisional, Bhāṣya-controlled study.
The inclusive third-level limit, successor counts,
śubha expansion, summit exception, knowledge-condition,
and additional same-level defiled successor have been
checked against the local research and running source.

## 10. OWL++ Seed

```text
Class: AttainmentOccurrence
Class: AttainmentLevel
Class: AttainmentMode
Class: ConditionalSuccessionPermission

ObjectProperty: mayImmediatelyFollow
ObjectProperty: hasLevel
ObjectProperty: hasMode
ObjectProperty: requiresKnowledgeCondition

WholesomeModes:
    members: Pure, Uncontaminated

GeneralUncontaminatedPredecessorRule:
    successorModes: WholesomeModes
    maximumLevelStepDistance: 2
    sameLevelIncluded: true
    immediateDefiledSuccessor: forbidden

GeneralPurePredecessorRule:
    wholesomeRange: SameGeneralBoundedRange
    additionalSuccessor: SameLevelDefiled
    qualification: PureSubtypeRestrictionsRemainApplicable

SummitOfExistence:
    availableWholesomeMode: PureOnly

FormlessEntryFromUncontaminatedKnowledge:
    permittedKnowledge: AnvayaJnana
    excludedKnowledge: DharmaJnana

ProjectConstraint: Count the starting level as first in the third-level limit.
ProjectConstraint: General permission does not assert actual occurrence.
ProjectConstraint: Distance alone is insufficient; preserve knowledge conditions.
ProjectConstraint: Do not infer an uncontaminated summit attainment.
ProjectConstraint: Immediate prohibition does not assert permanent impossibility.
ProjectConstraint: Treat defiled predecessors and death-time succession separately.
```

This is a declarative project seed, not executable OWL.
VAK 8.16 next treats successors of defiled attainment
and the distinct rules applying at death.
