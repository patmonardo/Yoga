# VAK_8.14 — Acquisition According to Mode and Prior Possession

## 1. Sanskrit (Devanāgarī)

```sanskrit
अतद्वान् लभते शुद्धं वैराग्येणोपपत्तितः ।
अनास्रवं तु वैराग्यात् क्लिष्टं हान्युपपत्तितः ॥ ८.१४ ॥
```

## 2. Sanskrit (IAST)

```text
atadvān labhate śuddhaṃ vairāgyeṇopapattitaḥ |
anāsravaṃ tu vairāgyāt kliṣṭaṃ hānyupapattitaḥ || 8.14 ||
```

The Sanskrit follows the local kārikā witness. The
prose controls the direction of rebirth, the restriction
to a non-possessor, and the additional cases that the
compressed verse does not enumerate.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `atadvān` | nominative singular masculine of negated tad-vat | one not possessing that |
| `labhate` | third-person singular present middle of √labh | acquires, obtains |
| `śuddham` | accusative singular neuter | pure [dhyāna or formless attainment] |
| `vairāgyeṇa` | instrumental singular neuter | through dispassion |
| `upapattitaḥ` | ablatival adverb | through rebirth |
| `anāsravam` | accusative singular neuter | uncontaminated [attainment] |
| `tu` | contrast particle | however |
| `vairāgyāt` | ablative singular neuter | through dispassion |
| `kliṣṭam` | accusative singular neuter | defiled [attainment] |
| `hānyupapattitaḥ` | compressed coordinated causal expression | through decline or rebirth |

`Vairāgyeṇa + upapattitaḥ` yields
`vairāgyeṇopapattitaḥ`; `hāni + upapattitaḥ` yields
`hānyupapattitaḥ`. The prose treats the acquisition
routes as alternatives, not as jointly required causes.

## 4. Grammar

The acquisition clauses share their overt subject and finite verb, while their three objects differ in mode; the prose fixes the direction of rebirth and excludes the summit.

```nltk-fcfg
% start S
# tokens: atadvān labhate śuddhaṃ vairāgyeṇopapattitaḥ anāsravaṃ tu vairāgyāt kliṣṭaṃ hānyupapattitaḥ
S -> SUBJ[CASE=nom,NUM=?n,GEN=?g] V[PERS=3,NUM=?n,TENSE=pres,VOICE=mid] CL[K=pure] CL[K=uncontaminated] CL[K=defiled]
CL[K=pure] -> OBJ[CASE=acc,NUM=sg,GEN=n,MODE=pure] CAUSE[ROUTE=or]
CL[K=uncontaminated] -> OBJ[CASE=acc,NUM=sg,GEN=n,MODE=uncontaminated] PTCL[CONTRAST=yes] CAUSE[ROUTE=dispassion]
CL[K=defiled] -> OBJ[CASE=acc,NUM=sg,GEN=n,MODE=defiled] CAUSE[ROUTE=decline_or_rebirth]
SUBJ[CASE=nom,NUM=sg,GEN=m] -> 'atadvān'
V[PERS=3,NUM=sg,TENSE=pres,VOICE=mid] -> 'labhate'
OBJ[CASE=acc,NUM=sg,GEN=n,MODE=pure] -> 'śuddhaṃ'
CAUSE[ROUTE=or] -> 'vairāgyeṇopapattitaḥ'
OBJ[CASE=acc,NUM=sg,GEN=n,MODE=uncontaminated] -> 'anāsravaṃ'
PTCL[CONTRAST=yes] -> 'tu'
CAUSE[ROUTE=dispassion] -> 'vairāgyāt'
OBJ[CASE=acc,NUM=sg,GEN=n,MODE=defiled] -> 'kliṣṭaṃ'
CAUSE[ROUTE=decline_or_rebirth] -> 'hānyupapattitaḥ'
```

```nltk-dep
'labhate' -> 'atadvān' | 'śuddhaṃ' | 'anāsravaṃ' | 'kliṣṭaṃ'
'śuddhaṃ' -> 'vairāgyeṇopapattitaḥ'
'anāsravaṃ' -> 'tu' | 'vairāgyāt'
'kliṣṭaṃ' -> 'hānyupapattitaḥ'
```

The three modes qualify objects, not successive levels. Upapattitaḥ is an alternative
route, not an additional cause: prose specifies lower-level rebirth for pure attainment
and higher-to-lower rebirth for defiled attainment. The shared verb preserves the
non-possessor restriction; uncontaminated acquisition is by dispassion.

**Close construe.** One not possessing the relevant
attainment acquires its pure mode through dispassion
or rebirth; its uncontaminated mode through dispassion;
and its defiled mode through decline or rebirth.
The commentary determines the scope of each route.

## 5. Translation

### Literal Translation

> One who does not possess it acquires the pure [dhyāna or formless
> attainment] through dispassion or rebirth; the uncontaminated,
> however, through dispassion; the defiled through decline or rebirth.

### Bhāṣya-informed study translation

> One who does not yet possess an attainment acquires its pure form
> through dispassion toward a lower level or through rebirth at a
> lower level, except at the summit of existence; acquires its
> uncontaminated form through dispassion; and acquires its defiled
> form through decline from that dispassion or through rebirth from a
> higher level into a lower.

## 6. Philosophical Translation

> Acquisition is determined by what is acquired,
> whether it is already possessed, and the relation
> between levels. Dispassion, decline, and rebirth
> can yield different acquisitions under different
> conditions. The causal label alone does not determine
> the ethical mode or the precise attainment gained.

Lābha concerns coming to possess an attainment. It
should not automatically be equated with entering it
in the next moment. The following verses pose the
separate question of immediate succession between attainments.

## 7. Technical Vocabulary

**Source.** Pradhan 442|19–443|12, checked against the local Bhāṣya
study and running source. The supplemental possessor cases and the
objection about entry into certainty are unfolded in the Bhāṣya rather
than in the verse's compact formulation.

**`Atadvān / tadvān`.** Non-possessor / possessor of
that which is under discussion. These are relational
qualifications, not permanent classes of persons.
The Bhāṣya explains why the verse names the former
and then supplements the rules for the latter.

**`Śuddha / śuddhaka`.** Pure, here wholesome but
contaminated. It remains distinct from anāsrava.
A pure attainment may also be classified according
to its tendency toward decline or penetration.

**`Vairāgya`.** Dispassion. In the pure case the prose
specifies dispassion toward the lower level. In the
defiled case, decline from the relevant dispassion
supplies an acquisition condition.

**`Upapatti`.** Rebirth. Its direction is essential
here. The research explanation of simple upward
birth does not adequately render the running prose's
lower-level rebirth qualification.

**`Bhavāgra`.** Summit of existence. It is excluded
from acquisition of the pure attainment through the
rebirth route for a non-possessor. This does not say
that beings reborn there cannot possess its attainment.

**`Nirvedhabhāgīya / hānabhāgīya`.** Conducive to
penetration / tending toward decline. Both qualify
pure attainment in the supplemental discussion.
Hānabhāgīya must not be silently replaced with kliṣṭa.

**`Kṣayajñāna / indriyasaṃcāra`.** Knowledge of destruction /
change or transformation of faculties. These furnish
additional acquisitions for one already possessing
uncontaminated attainment: respectively, an adept's
attainment and a trainee's or adept's attainment.

**`Niyāmāvakrānti`.** Entry into certainty, the fixed
course. The objection invokes this as another occasion
of first acquiring uncontaminated attainment. The reply
distinguishes an acquisition that is not universal
from the necessary route stated in the verse.

## 8. Logical Determination

The verse gives mode-sensitive acquisition routes for a non-possessor; the Bhāṣya specifies lower-level rebirth and higher-to-lower rebirth. It states necessary routes, not an exhaustive history of every acquisition. Provenance: `[verse]`, `[prose]`.

**Signature.** `NonPossessor/2(p,a)`—p lacks a; `Acquires/3(p,a,m)`—p gains a in mode m; `LowerDispassion/2`, `RebornLower/2`, `Dispassion/2`, `Declines/2`, `RebornFromHigher/2`—the respective route holds for p and a; `Summit/1(a)`—a is bhavāgra.

```nltk-fol
# THEORY shared
# [verse] śuddha through dispassion or lower-level rebirth; [prose] the summit exception
all p.all a.((NonPossessor(p,a) & LowerDispassion(p,a)) -> Acquires(p,a,puremode))
all p.all a.((NonPossessor(p,a) & RebornLower(p,a) & -Summit(a)) -> Acquires(p,a,puremode))
# [verse] anāsrava through dispassion
all p.all a.((NonPossessor(p,a) & Dispassion(p,a)) -> Acquires(p,a,uncontaminated))
# [verse] kliṣṭa through decline or rebirth; direction from prose
all p.all a.((NonPossessor(p,a) & (Declines(p,a) | RebornFromHigher(p,a))) -> Acquires(p,a,defiledmode))
```

**Finite valuation (sample acquisition routes).** This is a checkable sample, not an exhaustive count of attainment cases.

```nltk-valuation
personA => personA
firstDhyana => firstDhyana
puremode => puremode
uncontaminated => uncontaminated
defiledmode => defiledmode
NonPossessor => {(personA,firstDhyana)}
LowerDispassion => {(personA,firstDhyana)}
RebornLower => {(personA,firstDhyana)}
Dispassion => {(personA,firstDhyana)}
Declines => {(personA,firstDhyana)}
RebornFromHigher => {}
Summit => {}
Acquires => {(personA,firstDhyana,puremode),(personA,firstDhyana,uncontaminated),(personA,firstDhyana,defiledmode)}
```

**Results (NLTK).** `Model.satisfy` checks the shared acquisition rules against the displayed valuation. The rebirth rule is guarded by `-Summit`; no conclusion here says summit rebirth yields pure acquisition. Each mode remains a distinct acquisition label, not a scalar ranking.

**Scope cautions.** Possessors' supplemental routes, penetration-/decline-conducive subclasses, and entry into certainty are Bhāṣya-only expansions, not encoded as verse rules. `Acquires` does not mean immediate succession.

## 9. Interpretive Note

**Corrections controlled by the running source.** The
research exposition describes the pure rebirth route
as birth into a corresponding higher sphere. The
running text instead specifies lower-level rebirth.
Its first-dhyāna example concerns hānabhāgīya, a qualification
needed throughout the gain-and-loss illustration.
Both points are retained here without editing the
research witnesses.

**Witness cautions.** The running text has forms such
as `dhayanam`, `dhayānam`, and `śaikṣaśaikṣam`.
The local extract supplies the intelligible trainee/adept
pair `śaikṣāśaikṣam`. The verse, repeated prose subjects,
and contextual contrast control the exposition. This
study does not claim a critical reconstruction of
every irregular form.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates the mode, level, subtype, and
prior possession involved in an acquisition. Yoga
Technē, its kriyā–karma companion, concerns the effective
conditions under which such possession is obtained,
changed, or lost. Here the same causal word acquires
its meaning through a specific relation between levels.

For Organon representation, record an acquisition as
a conditioned change in possession, with its subject,
object, and route explicit. Keep a change of subtype
for an existing possessor distinct from acquisition
by a non-possessor. This is project reconstruction,
not an additional theory attributed to the Bhāṣya.

**Review status.** Provisional, Bhāṣya-controlled study.
The non-possession restriction, rebirth direction,
bhavāgra exception, possessor supplements, qualified
first-dhyāna illustration, and niyāma objection have
been checked against the local research and running source.

## 10. OWL++ Seed

```text
Class: AttainmentAcquisition
Class: PriorPossessionCondition
Class: AttainmentMode
Class: AttainmentSubtype
Class: AcquisitionRoute

ObjectProperty: acquiresAttainment
ObjectProperty: hasPriorPossessionCondition
ObjectProperty: hasMode
ObjectProperty: hasSubtype
ObjectProperty: occursThrough

NonPossessorPureAcquisition:
    routes: LowerLevelDispassion, LowerLevelRebirth
    rebirthRouteException: Bhavagra

NonPossessorUncontaminatedAcquisition:
    statedNecessaryRoute: Dispassion
    qualification: PreserveNiyamaEntryDiscussion

NonPossessorDefiledAcquisition:
    routes: DeclineFromRelevantDispassion, HigherToLowerRebirth

PurePossessorSupplement:
    practiceResult: NirvedhabhagiyaPureAttainment
    declineResult: HanabhagiyaPureAttainment

UncontaminatedPossessorSupplement:
    destructionKnowledgeResult: AdeptAttainment
    facultyTransformationResult: TraineeOrAdeptAttainment

ProjectConstraint: Non-possession need not mean never previously possessed.
ProjectConstraint: Preserve the direction of rebirth and dispassion.
ProjectConstraint: Preserve hanabhagiya in the gain-and-loss example.
ProjectConstraint: Pure and uncontaminated remain distinct modes.
ProjectConstraint: Do not infer an uncontaminated bhavagra attainment.
ProjectConstraint: Acquisition is distinct from immediate attainment succession.
ProjectConstraint: The compact verse is not an exhaustive rule for possessors.
```

This is a declarative project seed, not executable OWL.
VAK 8.15 next begins the rules for which attainments
can arise immediately after another attainment.
