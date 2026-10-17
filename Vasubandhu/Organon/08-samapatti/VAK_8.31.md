# VAK_8.31 — Immeasurable Levels, Training, and Limits of Counteraction

## 1. Sanskrit (Devanāgarī)

```sanskrit
ध्यानयोर्मुदिता अन्यानि षट्सु केचित्तु पञ्चसु ।
न तैः प्रहाणं नृष्वेव जन्यन्ते त्र्यन्वितो ध्रुवम् ॥ ८.३१ ॥
```

## 2. Sanskrit (IAST)

```text
dhyānayor muditā anyāni ṣaṭsu kecit tu pañcasu |
na taiḥ prahāṇaṃ nṛṣv eva janyante tryanvito dhruvam || 8.31 ||
```

The Sanskrit follows the local kārikā witness. The
Bhāṣya supplies the identities behind the level
counts, an additional ten-level account, and the
subject of the final possession statement.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `dhyānayoḥ` | locative dual | in the two dhyānas |
| `muditā` | nominative singular feminine | sympathetic joy |
| `anyāni` | nominative plural neuter | the other three immeasurables |
| `ṣaṭsu / pañcasu` | locative plural numerals | on six / five levels |
| `kecit` | nominative plural masculine | some authorities |
| `taiḥ` | instrumental plural | by these immeasurables |
| `prahāṇam` | nominative singular neuter | abandonment |
| `nṛṣu eva` | locative plural and restriction | only among humans |
| `janyante` | third-person plural passive | are generated |
| `tryanvitaḥ` | nominative singular masculine compound | endowed with three |
| `dhruvam` | adverb | certainly; invariably |

`Dhyānayoḥ + muditā` yields `dhyānayor muditā`;
`nṛṣu + eva` yields `nṛṣv eva`; `tri + anvitaḥ`
yields `tryanvitaḥ`; before dhruvam this appears
as `tryanvito`. The final masculine predicate concerns
the attainer, not an immeasurable accompanied by
three simultaneous mental events.

## 4. Grammar

The first locative fixes sympathetic joy to two dhyānas; the six/five disagreement applies to the other three. The denial concerns abandonment, while human generation and later possession are separate claims; the final masculine predicate describes the attainer.

```nltk-fcfg
% start S
# tokens: dhyānayoḥ ∅-prathama-dvitīya muditā anyāni ∅-trīṇi ṣaṭsu kecit tu pañcasu na taiḥ prahāṇam ∅-apramāṇāni nṛṣu eva janyante ∅-apramāṇalābhī tryanvitaḥ dhruvam
S -> CL[K=joy_level] CL[K=other_levels] CL[K=no_abandonment] CL[K=generation] CL[K=possession]
CL[K=joy_level] -> N[CASE=loc,NUM=du,GEN=n] N[CASE=loc,NUM=du,GEN=n,SUPPLIED=prose] N[CASE=nom,NUM=sg,GEN=f]
CL[K=other_levels] -> ADJ[CASE=nom,NUM=pl,GEN=n] NUMR[CASE=nom,NUM=pl,GEN=n,SUPPLIED=prose] N[CASE=loc,NUM=pl,GEN=n] PRON[CASE=nom,NUM=pl,GEN=m,ATTR=yes] PTCL[CONTRAST=yes] N[CASE=loc,NUM=pl,GEN=n]
CL[K=no_abandonment] -> NEG[CASE=none,NUM=none,GEN=none] PRON[CASE=ins,NUM=pl,GEN=m] N[CASE=nom,NUM=sg,GEN=n]
CL[K=generation] -> N[CASE=nom,NUM=pl,GEN=n,SUPPLIED=prose] N[CASE=loc,NUM=pl,GEN=m] PTCL[RESTRICT=yes] V[PERS=3,NUM=pl,TENSE=pres,VOICE=pass]
CL[K=possession] -> N[CASE=nom,NUM=sg,GEN=m,SUPPLIED=prose] ADJ[CASE=nom,NUM=sg,GEN=m] ADV[CASE=none,NUM=none,GEN=none,CERTAIN=yes]
N[CASE=loc,NUM=du,GEN=n] -> 'dhyānayoḥ'
N[CASE=loc,NUM=du,GEN=n,SUPPLIED=prose] -> '∅-prathama-dvitīya'
N[CASE=nom,NUM=sg,GEN=f] -> 'muditā'
ADJ[CASE=nom,NUM=pl,GEN=n] -> 'anyāni'
NUMR[CASE=nom,NUM=pl,GEN=n,SUPPLIED=prose] -> '∅-trīṇi'
N[CASE=loc,NUM=pl,GEN=n] -> 'ṣaṭsu' | 'pañcasu'
PRON[CASE=nom,NUM=pl,GEN=m,ATTR=yes] -> 'kecit'
PTCL[CASE=none,NUM=none,GEN=none,CONTRAST=yes] -> 'tu'
NEG[CASE=none,NUM=none,GEN=none] -> 'na'
PRON[CASE=ins,NUM=pl,GEN=m] -> 'taiḥ'
N[CASE=nom,NUM=sg,GEN=n] -> 'prahāṇam'
N[CASE=nom,NUM=pl,GEN=n,SUPPLIED=prose] -> '∅-apramāṇāni'
N[CASE=loc,NUM=pl,GEN=m] -> 'nṛṣu'
PTCL[CASE=none,NUM=none,GEN=none,RESTRICT=yes] -> 'eva'
V[CASE=none,NUM=pl,GEN=none,PERS=3,TENSE=pres,VOICE=pass] -> 'janyante'
N[CASE=nom,NUM=sg,GEN=m,SUPPLIED=prose] -> '∅-apramāṇalābhī'
ADJ[CASE=nom,NUM=sg,GEN=m] -> 'tryanvitaḥ'
ADV[CASE=none,NUM=none,GEN=none,CERTAIN=yes] -> 'dhruvam'
```

```nltk-dep
'muditā' -> 'dhyānayoḥ' | '∅-prathama-dvitīya'
'anyāni' -> '∅-trīṇi' | 'ṣaṭsu' | 'kecit' | 'tu' | 'pañcasu'
'prahāṇam' -> 'na' | 'taiḥ'
'janyante' -> '∅-apramāṇāni' | 'nṛṣu' | 'eva'
'∅-apramāṇalābhī' -> 'tryanvitaḥ' | 'dhruvam'
```

`Viṣkambhaṇa` by preparatory cultivation is not `prahāṇa` by abandonment-path.
`Tryanvitaḥ` is the attainer, not an immeasurable; the attributed five-level count is
preserved alongside six.


**Close construe.** Sympathetic joy belongs to the
first two dhyānas; the other three to six
levels, or five according to some. They do
not themselves effect abandonment. They are generated
among humans, and their attainer is invariably
endowed with three.

## 5. Translation

### Literal Translation

> Sympathetic joy is in the two dhyānas; the
> others on six levels, though some say five.
> Abandonment is not effected by them. They are
> generated only among humans. [Their attainer] is
> certainly endowed with three.

### Bhāṣya-informed study translation

> Sympathetic joy is in the two dhyānas; the other three are on six levels,
> though some say five. There is no abandonment by them. They are generated
> only among humans. One who has attained them is invariably endowed with three.

## 6. Philosophical Translation

> The immeasurables have a determinate range and
> a substantial counteractive role without being
> identified with the abandoning path. Their cultivation
> can progressively equalize a response across friendly,
> neutral, and hostile persons before extending it
> spatially. Possession, initial generation, and current
> meditative level remain separate questions.

The source does not reduce their value to a
failure to liberate. It explains preparatory suppression
and subsequent protection from being overcome by
the opposed tendencies, while assigning abandonment
its own path-function.

## 7. Technical Vocabulary

**`Viṣkambhaṇa`.** Suppression or blocking. The prose
uses this to explain the preparation's counteractive
effect. It must remain distinct from prahāṇa.

**`Prahāṇamārga`.** Path of abandonment. After preparatory
suppression, abandonment is effected by these paths.
The immeasurables' counterforce designation does not
make them identical with those paths.

**`Adhimuktimanaskāra`.** Attention through resolve or
imaginative determination. Together with principal-dhyāna
status and beings as object, it appears among
the reasons given for denying abandonment by the
principal immeasurables.

**`Mitrapakṣa / udāsīnapakṣa / śatrupakṣa`.** Friendly,
neutral, and hostile classes of persons. The
prose uses graded relations to explain how friendliness
is stabilized when immediate general extension is difficult.

**`Guṇagrāhin`.** One who attends to qualities or
virtues. Such a person produces equal friendliness
quickly in the commentary's account. This does
not require denying every fault or harmful action.

**`Samanvāgata`.** Endowed with or possessing. This
controls the final accompaniment statement. It is
not a claim of simultaneous entry into three immeasurables.

## 8. Logical Determination

Sympathetic joy belongs to the first two dhyānas; the other three immeasurables receive attributed six-, five-, and ten-level accounts. The verse denies that these immeasurables themselves effect abandonment, restricts their generation to humans, and says their attainer is endowed with three. `[verse]`; counts and scope are `[prose]`.

**Signature.** `OnLevel(x,l)`; `SixLevel(l)`; `FiveLevel(l)`; `SixAccount(g,l)` and `FiveAccount(g,l)` (attributed scopes); `Immeasurable(x)`; `NoAbandonment(x)`; `GeneratedOnlyHuman(x)`; `AttainerOfFour(a)`; `EndowedWithThree(a)`.

```nltk-valuation
joy => joy
otherThree => otherThree
attainerOne => attainerOne
friendliness => friendliness
compassion => compassion
equanimity => equanimity
firstDhyana => firstDhyana
secondDhyana => secondDhyana
anagamya => anagamya
intermediateDhyana => intermediateDhyana
thirdDhyana => thirdDhyana
fourthDhyana => fourthDhyana
OnLevel => {(joy,firstDhyana),(joy,secondDhyana)}
SixLevel => {anagamya, intermediateDhyana, firstDhyana, secondDhyana, thirdDhyana, fourthDhyana}
FiveLevel => {intermediateDhyana, firstDhyana, secondDhyana, thirdDhyana, fourthDhyana}
SixAccount => {(otherThree,anagamya),(otherThree,intermediateDhyana),(otherThree,firstDhyana),(otherThree,secondDhyana),(otherThree,thirdDhyana),(otherThree,fourthDhyana)}
FiveAccount => {(otherThree,intermediateDhyana),(otherThree,firstDhyana),(otherThree,secondDhyana),(otherThree,thirdDhyana),(otherThree,fourthDhyana)}
Immeasurable => {friendliness,compassion,joy,equanimity}
NoAbandonment => {friendliness,compassion,joy,equanimity}
GeneratedOnlyHuman => {friendliness,compassion,joy,equanimity}
AttainerOfFour => {attainerOne}
EndowedWithThree => {attainerOne}
```

```nltk-fol
# THEORY shared
# [verse, prose] the level of sympathetic joy
OnLevel(joy,firstDhyana)
OnLevel(joy,secondDhyana)
# [verse] na taiḥ prahāṇam; [prose] suppression is not path-abandonment
all x.(Immeasurable(x) -> NoAbandonment(x))
all x.(Immeasurable(x) -> GeneratedOnlyHuman(x))
all a.(AttainerOfFour(a) -> EndowedWithThree(a))
# THEORY six_level
# [prose, attributed account] exactly the reported six-level range
all l.(SixLevel(l) -> SixAccount(otherThree,l))
all l.(SixAccount(otherThree,l) -> SixLevel(l))
# THEORY some_five
# [prose, some authorities] exactly their reported five-level range
all l.(FiveLevel(l) -> FiveAccount(otherThree,l))
all l.(FiveAccount(otherThree,l) -> FiveLevel(l))
```

**Results (NLTK).** The checker reports `shared: T`, `six_level: T`, and `some_five: T` in the model. The six- and five-level ranges are model-checked as separate attributed sets; the ten-level account is reported without inventing an explicit ten-member list.

**Scope cautions.** The ten-level account's compressed inclusion is not reconstructed here. Suppression, path-abandonment, and later protection are distinct. `Tryanvitaḥ` describes an attainer said to be endowed with three; the source's shorthand is not specified further here.

## 9. Interpretive Note

**Limits clarify rather than erase the earlier function.**
VAK 8.29 called the immeasurables counterforces.
This unit supplies the distinction needed to
interpret that claim: preparation suppresses, paths
abandon, and acquired principal immeasurables have
a protective role. “They do nothing to defilements”
would be as inaccurate as calling them the
abandoning paths themselves.

**Witness cautions.** The running source has irregular
forms including `maulalprayoga`, `kleśagrahaṇaṃ` in
the abandonment question, and the separated
`prahāṇa dūrīkaraṇācca`. The ensuing explicit
prahāṇamārga and viṣkambhaṇa sentences control the
central distinction. The study does not silently
reconstruct every damaged compound or the full
alternative ten-level inventory. Originals remain unchanged.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates level, object, function,
and possession; Yoga Technē, its kriyā–karma companion,
concerns the graduated equalization and extension
described in the training. Equal friendliness across
relations precedes spatial expansion in the difficulty-conditioned
procedure, so breadth alone does not establish
the required steadiness.

The research's Buddha-Mind, Arhat-function, and
Theory of Māyā comparisons remain project hypotheses.
The source provides the particular suppression/abandonment
distinction and training sequence. For Organon representation,
preserve those operations and their order without
turning a graded cultivation account into a universal
metaphysical theory.

**Review status.** Provisional, Bhāṣya-controlled study.
The level alternatives, muditā restriction, suppression/path
abandonment distinction, beginner sequence, equanimity's
neutral starting point, human generation, and possession
guarantee have been checked against the local
research and running source.

## 10. OWL++ Seed

```text
Class: Immeasurable
Class: PreparatoryCultivation
Class: AbandonmentPath
Class: PossessionCondition
Class: ReportedLevelAccount

ObjectProperty: supportedAtLevel
ObjectProperty: suppressesTendency
ObjectProperty: abandonsDefilement
ObjectProperty: initiallyGeneratedAmong

Mudita:
    levels: FirstDhyana, SecondDhyana
    reason: GladnessNature

OtherThreeImmeasurables:
    principalCountAccount: SixLevels
    alternativeAccounts: FiveLevels, BroaderTenLevelReckoning

FunctionalDistinction:
    preparation: Suppression
    abandonmentPaths: Abandonment
    acquiredPrincipalImmeasurables: ProtectionAgainstOpposedTendencies

GenerationAndPossession:
    initialGeneration: Humans
    guaranteedPossession: Maitri, Karuna, Upeksa
    higherRebirthException: MuditaAbsentInThirdOrFourthDhyanaRebirth

TrainingWhenGeneralExtensionIsDifficult:
    friendlinessOrder: StrongToMildFriends, NeutralPersons,
                       MildToStrongEnemies, SpatialExpansion
    equanimityStartingClass: NeutralPersons

ProjectConstraint: Counteraction is not identical with abandonment.
ProjectConstraint: Preserve differing scopes of the level accounts.
ProjectConstraint: Human generation does not prohibit later nonhuman possession.
ProjectConstraint: Threefold possession does not mean simultaneous entry.
ProjectConstraint: Guarantee of three does not exclude possession of all four.
ProjectConstraint: Graduated fallback does not erase the initial general aspiration.
```

This is a declarative project seed, not executable OWL.
VAK 8.32 next begins the eight liberations.
