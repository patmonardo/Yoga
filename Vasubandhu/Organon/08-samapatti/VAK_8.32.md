# VAK_8.32 — Eight Releases and Their Attainment Bases

## 1. Sanskrit (Devanāgarī)

```sanskrit
अष्टौ विमोक्षाः प्रथमावशुभा ध्यानयोर्द्वयोः ।
तृतीयोऽन्त्ये स चालोभः शुभारूप्याः समाहिताः ॥ ८.३२ ॥
```

## 2. Sanskrit (IAST)

```text
aṣṭau vimokṣāḥ prathamāv aśubhā dhyānayor dvayoḥ |
tṛtīyo 'ntye sa cālobhaḥ śubhārūpyāḥ samāhitāḥ || 8.32 ||
```

The Sanskrit follows the local kārikā witness. Its
aśubhā is retained as the designation of unattractive
contemplation, not silently changed to the adjective
aśubhau. The commentary explains the first two
as having aśubhā as their nature.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `aṣṭau` | numeral | eight |
| `vimokṣāḥ` | nominative plural masculine | releases or deliverances |
| `prathamau` | nominative dual masculine ordinal | the first two |
| `aśubhā` | nominative singular feminine designation | unattractive contemplation |
| `dhyānayoḥ dvayoḥ` | locative dual | in the two dhyānas |
| `tṛtīyaḥ` | nominative singular masculine ordinal | the third release |
| `antye` | locative singular | in the last [dhyāna] |
| `saḥ` | nominative singular masculine pronoun | that third release |
| `alobhaḥ` | nominative singular masculine | non-greed |
| `śubhārūpyāḥ` | nominative plural compound designation | wholesome formless attainments |
| `samāhitāḥ` | nominative plural adjective | collected |

`Prathamau + aśubhā` yields `prathamāv aśubhā`;
`tṛtīyaḥ + antye` yields `tṛtīyo 'ntye`;
`ca + alobhaḥ` yields `cālobhaḥ`; `śubha +
ārūpya` yields `śubhārūpya`.

## 4. Grammar

The eight-count heads three explicit groupings: first two, third, and wholesome collected formless states. The prose jointly locates the first two in first and second dhyāna; `antye` is specifically fourth dhyāna, and the third's non-greed nature is not its aspect.

```nltk-fcfg
% start S
# tokens: aṣṭau vimokṣāḥ prathamau aśubhā dhyānayoḥ dvayoḥ ∅-prathama-dvitīya tṛtīyaḥ antye saḥ ca alobhaḥ śubhārūpyāḥ samāhitāḥ
S -> CL[K=count] CL[K=first_two] CL[K=third] CL[K=formless]
CL[K=count] -> NUMR[CASE=nom,NUM=pl,GEN=m] N[CASE=nom,NUM=pl,GEN=m]
CL[K=first_two] -> NUMR[CASE=nom,NUM=du,GEN=m] N[CASE=nom,NUM=sg,GEN=f] N[CASE=loc,NUM=du,GEN=n] NUMR[CASE=loc,NUM=du,GEN=n] N[CASE=loc,NUM=du,GEN=n,SUPPLIED=prose]
CL[K=third] -> NUMR[CASE=nom,NUM=sg,GEN=m] ADJ[CASE=loc,NUM=sg,GEN=n,FINAL=yes] PRON[CASE=nom,NUM=sg,GEN=m] PTCL[ADD=yes] N[CASE=nom,NUM=sg,GEN=m,NATURE=non_greed]
CL[K=formless] -> ADJ[CASE=nom,NUM=pl,GEN=m,QUALITY=wholesome] ADJ[CASE=nom,NUM=pl,GEN=m,STATE=collected]
NUMR[CASE=nom,NUM=pl,GEN=m] -> 'aṣṭau'
N[CASE=nom,NUM=pl,GEN=m] -> 'vimokṣāḥ'
NUMR[CASE=nom,NUM=du,GEN=m] -> 'prathamau'
N[CASE=nom,NUM=sg,GEN=f] -> 'aśubhā'
N[CASE=loc,NUM=du,GEN=n] -> 'dhyānayoḥ'
NUMR[CASE=loc,NUM=du,GEN=n] -> 'dvayoḥ'
N[CASE=loc,NUM=du,GEN=n,SUPPLIED=prose] -> '∅-prathama-dvitīya'
NUMR[CASE=nom,NUM=sg,GEN=m] -> 'tṛtīyaḥ'
ADJ[CASE=loc,NUM=sg,GEN=n,FINAL=yes] -> 'antye'
PRON[CASE=nom,NUM=sg,GEN=m] -> 'saḥ'
PTCL[CASE=none,NUM=none,GEN=none,ADD=yes] -> 'ca'
N[CASE=nom,NUM=sg,GEN=m,NATURE=non_greed] -> 'alobhaḥ'
ADJ[CASE=nom,NUM=pl,GEN=m,QUALITY=wholesome] -> 'śubhārūpyāḥ'
ADJ[CASE=nom,NUM=pl,GEN=m,STATE=collected] -> 'samāhitāḥ'
```

```nltk-dep
'vimokṣāḥ' -> 'aṣṭau' | 'prathamau' | 'tṛtīyaḥ' | 'śubhārūpyāḥ'
'aśubhā' -> 'dhyānayoḥ' | 'dvayoḥ' | '∅-prathama-dvitīya'
'alobhaḥ' -> 'saḥ' | 'ca' | 'antye'
'śubhārūpyāḥ' -> 'samāhitāḥ'
```

The first-two construction is jointly locative, not a one-to-one assignment. The third is
non-greed but explicitly not aśubhā; the formless-release label is restricted to wholesome,
collected states.


**Close construe.** There are eight releases. The
first two are unattractive contemplations in the
first two dhyānas. The third is in fourth
dhyāna and has non-greed as its nature. Wholesome,
collected formless attainments constitute the formless releases.

## 5. Translation

### Literal Translation

> There are eight releases. The first two are
> unattractive contemplation in the two dhyānas.
> The third is in the last, and it is
> non-greed. The wholesome formless [releases] are collected.

### Bhāṣya-informed study translation

> There are eight releases. The first two, in the first two dhyānas, are
> unattractive contemplation. The third, in the last dhyāna, is non-greed.
> The formless releases are wholesome and collected.

## 6. Philosophical Translation

> The release classification depends on aspect,
> mental nature, level, and collected operation.
> The third release's beautiful aspect does not
> make it greedy, just as the first two's
> unattractive aspects do not supply the entire
> constitution of their associated Base complexes.
> Formless level membership alone does not suffice
> for the release designation.

Vimokṣa in this eightfold inventory must not be
identified automatically with final destruction of all
outflows. The commentary gives a specific turning-away
explanation and qualifies which attainments receive the name.

## 7. Technical Vocabulary

**`Aśubhā`.** Unattractive contemplation. The prose
invokes bluish and related aspects and directs
that the method be understood as in the earlier
aśubhā analysis. It does not equate unattractiveness
with ethical unwholesomeness.

**`Śubha`.** Beautiful or pure as the third
release's aspect; wholesome as the qualification
of formless attainments. The prose's contrast
with aśubhā in one clause and gloss kuśala
in the other control these contextual senses.

**`Alobha`.** Non-greed. The third release shares
this underlying determination while differing in aspect.
Its occurrence here should not be reduced to
a subjective report of feeling pleasant or unpleasant.

**`Saparivāra`.** With associated factors or accompaniment.
The first three, considered in this full manner,
have the five Bases as their nature. This
is a different scope from identifying their central
mental factor as non-greed.

**`Samāhita / asamāhita`.** Collected / uncollected.
These qualify the formless states eligible for
the release name. They are not interchangeable
with wholesome / defiled, which supply another condition.

**`Vimuktimārga / ānantaryamārga`.** Liberation path /
uninterrupted path. Their distinct object relations
matter to the access-stage release designation.
Exclusion from this particular designation does not
deny the uninterrupted path's abandonment function.

**`Vaimukhya`.** Turning away. This is the explicit
local explanation of vimokṣa. “Release from domination”
can interpret its practical significance but should
remain distinguishable from the short source gloss.

## 8. Logical Determination

The verse states an eightfold release inventory and gives conditions for its groups: first two as unattractive contemplation in the first two dhyānas, third in fourth dhyāna with non-greed nature, and formless releases only when wholesome and collected. The prose also grants the designation to some access liberation paths, not uninterrupted paths. `[verse]` / `[prose]`.

**Signature.** `Release(x)`; `Unattractive(x)`; `InFirstTwo(x)`; `ThirdRelease(x)`; `InFourth(x)`; `Nature(x,n)`; `Formless(x)`; `Wholesome(x)`; `Collected(x)`; `EighthRelease(x)`; `AccessPath(x)`; `UninterruptedPath(x)`; `NamedRelease(x)`.

```nltk-valuation
release1 => release1
release2 => release2
release3 => release3
release4 => release4
release5 => release5
release6 => release6
release7 => release7
release8 => release8
nonGreed => nonGreed
accessLiberationPath => accessLiberationPath
uninterruptedPath => uninterruptedPath
Release => {release1, release2, release3, release4, release5, release6, release7, release8}
Unattractive => {release1, release2}
InFirstTwo => {release1, release2}
ThirdRelease => {release3}
InFourth => {release3}
Nature => {(release3,nonGreed)}
Formless => {release4, release5, release6, release7}
Wholesome => {release4, release5, release6, release7}
Collected => {release4, release5, release6, release7}
EighthRelease => {release8}
AccessPath => {accessLiberationPath}
UninterruptedPath => {uninterruptedPath}
NamedRelease => {accessLiberationPath}
```

```nltk-fol
# THEORY shared
# [verse, prose] inventory groups and eighth release
all x.(Release(x) -> (Unattractive(x) | ThirdRelease(x) | Formless(x) | EighthRelease(x)))
all x.(Unattractive(x) -> InFirstTwo(x))
all x.(ThirdRelease(x) -> (InFourth(x) & Nature(x,nonGreed)))
# [verse, prose] formless releases require both conditions
all x.(Formless(x) -> (Wholesome(x) & Collected(x)))
# [prose] access liberation paths may be releases; uninterrupted paths are excluded
all x.(AccessPath(x) -> NamedRelease(x))
all x.(UninterruptedPath(x) -> -NamedRelease(x))
```

**Results (NLTK).** `check_logic.py` reports `shared: T` for the finite valuation and its group-eligibility rules.

**Scope cautions.** The uncertain second introductory release formula is intentionally not formalized; no negation or corrected reading is supplied here. Uncollected occurrence claims remain attributed. Eligibility is not inferred from formless level membership alone, and *vimokṣa* is not equated with final destruction of outflows.

## 9. Interpretive Note

**Corrections and unresolved witness evidence.** The
final compound is interpreted as wholesome formless
attainments, following the explicit prose. The
local verse's aśubhā is preserved instead of
being replaced with aśubhau in padaccheda. The
second introductory release formula remains textually
flagged; a full critical reconstruction would require
additional witness comparison beyond this local study.

**Keep interpretation proportional.** The research
reads the third release as freedom within positive
appearance. Its non-greed nature and beautiful
aspect support that project comparison. The passage
does not itself declare every encounter with beauty
a release or supply a universal ranking of
all forms of non-attachment.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates aspect, mental nature,
level, accompaniment, and naming conditions. Yoga
Technē, its kriyā–karma companion, concerns the
contemplative operation specified through unattractive and
beautiful aspects. The contrast illustrates how
a shared mental nature can receive different
determinations through aspect and level.

For Organon representation, keep central-factor identity
separate from the five-Base accompanied complex,
and preserve both eligibility conditions for formless
release. A disputed introductory formula must remain
marked rather than converted into a definitive
axiom. This is project reconstruction, not additional
doctrine attributed to Vasubandhu.

**Review status.** Provisional, Bhāṣya-controlled study.
The eightfold outline, first-two method and levels,
third-release distinctions, five-Base accompaniment,
formless eligibility, reported uncollected extension,
and access-path distinction have been checked against
the local research and running source. The second
release's introductory formula remains unresolved.

## 10. OWL++ Seed

```text
Class: Release
Class: ContemplativeAspect
Class: AttainmentLevel
Class: CollectedFormlessAttainment

ObjectProperty: hasAspect
ObjectProperty: hasMentalNature
ObjectProperty: hasEligibleLevelRange
ObjectProperty: receivesReleaseDesignation

EightReleases:
    groups: ThreeFormRelated, FourFormless, CessationOfPerceptionAndFeeling
    count: 8

FirstTwoReleases:
    method: AsubhaContemplation
    levelRange: FirstAndSecondDhyana
    exclusiveOneToOneLevelAssignment: NotEstablishedHere

ThirdRelease:
    level: FourthDhyana
    mentalNature: NonGreed
    aspect: Beautiful

FirstThreeWithAccompaniment:
    constitution: FiveBases

FormlessReleaseEligibility:
    requiredConditions: Wholesome, Collected

AccessPaths:
    liberationPath: ReleaseDesignationAdmitted
    uninterruptedPath: ExcludedBecauseLowerLevelObject

ProjectConstraint: Beautiful aspect and wholesome mode are contextual senses of subha.
ProjectConstraint: Preserve the uncertain second-release introductory formula.
ProjectConstraint: Factor nature differs from accompanied Base constitution.
ProjectConstraint: Release naming does not alone establish final outflow destruction.
ProjectConstraint: Preserve the attributed extension of uncollected occurrences.
```

This is a declarative project seed, not executable OWL.
VAK 8.33 next continues with cessation as the eighth release.
