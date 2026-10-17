# VAK_8.34 — Release Objects and the Test of Mastery

## 1. Sanskrit (Devanāgarī)

```sanskrit
कामाप्तदृश्यविषयाः प्रथमाः ये त्वारूपिणः ।
तेऽन्वयज्ञानपक्षोर्ध्वस्वभूदुःखादिगोचराः ॥ ८.३४ ॥
```

## 2. Sanskrit (IAST)

```text
kāmāptadṛśyaviṣayāḥ prathamāḥ ye tv arūpiṇaḥ |
te 'nvayajñānapakṣordhvasvabhūduḥkhādigocarāḥ || 8.34 ||
```

The verse follows the local IAST witness with
analytical hyphens removed. Its Devanāgarī prints
त्वारूपिणः while the IAST and running source
have tv arūpiṇaḥ; that script difference is
retained and disclosed rather than treated as
a distinct doctrinal reading.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `kāmāptadṛśyaviṣayāḥ` | nominative plural masculine compound adjective | having desire-domain visible form as object |
| `prathamāḥ` | nominative plural masculine ordinal | the first releases, here the first three |
| `ye … te` | relative-correlative pronouns | those which … those |
| `arūpiṇaḥ` | nominative plural masculine | formless [releases] |
| `anvayajñānapakṣa` | compound member | the anvayajñāna side, specified as path in prose |
| `ūrdhva / svabhū` | compound members | higher / own level |
| `duḥkhādi` | compound member | suffering and the associated following items |
| `gocarāḥ` | nominative plural compound ending | having as their object-field |

Sandhi: `kāma + āpta` > `kāmāpta`; `pakṣa + ūrdhva` > `pakṣordhva`;
`duḥkha + ādi` > `duḥkhādi`. The prose unpacks the final compound into distinct
object categories rather than one unrestricted truth-field.

## 4. Grammar

The relative-correlative pair separates the first three form-object releases from the four formless releases. The Bhāṣya restricts the knowledge-side qualifier to the path and explicitly expands the remaining object list.

```nltk-fcfg
% start S
# tokens: kāmāptadṛśyaviṣayāḥ ∅-rūpāyatanam ∅-yathāyogam prathamāḥ ∅-trayaḥ ye tu arūpiṇaḥ te anvayajñānapakṣordhvasvabhūduḥkhādigocarāḥ ∅-duḥkham ∅-taddhetuḥ ∅-nirodhau ∅-mārgaḥ ∅-apratisaṃkhyānirodhaḥ ∅-ākāśam
S[SEM=<?a & ?b>] -> CL[K=visible,SEM=?a] CL[K=formless,SEM=?b]

CL[K=visible,SEM=<FirstThree(formgroup) & all g.(FirstThree(g) -> Includes(g,visible))>] -> ADJ[CASE=?c,NUM=?n,GEN=?g,OBJ=yes] N[CASE=acc,NUM=sg,GEN=n,SUPPLIED=prose] ADV[SUPPLIED=prose] N[CASE=?c,NUM=?n,GEN=?g] NUMR[CASE=?c,NUM=?n,GEN=?g,SUPPLIED=prose]
CL[K=formless,SEM=<FormlessFour(formlessgroup) & all g.(FormlessFour(g) -> Includes(g,ownhigher))>] -> PRON[CASE=?c,NUM=?n,GEN=?g,REL=yes] PTCL[CONTRAST=yes] N[CASE=?c,NUM=?n,GEN=?g] PRON[CASE=?c,NUM=?n,GEN=?g,CORR=yes] ADJ[CASE=?c,NUM=?n,GEN=?g,OBJ=yes] OBJSEQ
OBJSEQ -> OBJ[K=dukkha] OBJ[K=hetu] OBJ[K=nirodha] OBJ[K=marga] OBJ[K=cessation] OBJ[K=space]

ADJ[CASE=nom,NUM=pl,GEN=m,OBJ=yes] -> 'kāmāptadṛśyaviṣayāḥ'
N[CASE=acc,NUM=sg,GEN=n,SUPPLIED=prose] -> '∅-rūpāyatanam'
ADV[SUPPLIED=prose] -> '∅-yathāyogam'
N[CASE=nom,NUM=pl,GEN=m] -> 'prathamāḥ'
NUMR[CASE=nom,NUM=pl,GEN=m,SUPPLIED=prose] -> '∅-trayaḥ'
PRON[CASE=nom,NUM=pl,GEN=m,REL=yes] -> 'ye'
PTCL[CONTRAST=yes] -> 'tu'
N[CASE=nom,NUM=pl,GEN=m] -> 'arūpiṇaḥ'
PRON[CASE=nom,NUM=pl,GEN=m,CORR=yes] -> 'te'
ADJ[CASE=nom,NUM=pl,GEN=m,OBJ=yes] -> 'anvayajñānapakṣordhvasvabhūduḥkhādigocarāḥ'
OBJ[K=dukkha,SUPPLIED=prose] -> '∅-duḥkham'
OBJ[K=hetu,SUPPLIED=prose] -> '∅-taddhetuḥ'
OBJ[K=nirodha,SUPPLIED=prose] -> '∅-nirodhau'
OBJ[K=marga,SUPPLIED=prose] -> '∅-mārgaḥ'
OBJ[K=cessation,SUPPLIED=prose] -> '∅-apratisaṃkhyānirodhaḥ'
OBJ[K=space,SUPPLIED=prose] -> '∅-ākāśam'
```

```nltk-dep
'prathamāḥ' -> 'kāmāptadṛśyaviṣayāḥ' | '∅-rūpāyatanam' | '∅-yathāyogam' | '∅-trayaḥ'
'te' -> 'ye' | 'tu' | 'arūpiṇaḥ'
'anvayajñānapakṣordhvasvabhūduḥkhādigocarāḥ' -> 'te' | '∅-duḥkham' | '∅-taddhetuḥ' | '∅-nirodhau' | '∅-mārgaḥ' | '∅-apratisaṃkhyānirodhaḥ' | '∅-ākāśam'
```

`Prathamāḥ` means the first three; the correlates select the four formless releases, not cessation-release.
`Anvayajñānapakṣa` qualifies the path alone; *ādi* also includes non-analytical cessation and space for one release.
**Close construe.** The first three releases have
visible desire-domain form as object. The formless
releases have own-/higher-level suffering, its cause
and cessation, and the anvayajñāna-side path as
their field, with the further objects specified
in the commentary.

## 5. Translation

### Literal Translation

> The first releases have desire-domain visible
> objects. Those that are formless have as
> their field the anvayajñāna side and suffering
> and the following items of higher and own levels.

### Bhāṣya-informed study translation

> The first three releases have as their object visible form of the
> desire domain, unpleasant or pleasant as the case may be. The formless
> releases have as their field suffering of their own and higher levels
> and its cause and cessation, together with the whole path on the
> anvayajñāna side, and also non-analytical cessation and, for one of them, space.

## 6. Philosophical Translation

> The release classification includes the object
> as well as the attainment's level and mode.
> Its practical explanation also supplies a test:
> accomplishment of the unattractive releases is
> shown when attention to the beautiful no longer
> brings forth affliction. Sustaining an unattractive
> aspect alone is not the complete criterion given here.

This is a specific contemplative test in the
source's account. It does not establish universal
immunity to every affliction in every circumstance.

## 7. Technical Vocabulary

**`Rūpāyatana`.** The visible-form Essence, not every
material phenomenon without distinction. The prose
specifies this as the first three releases' object.

**`Amanojña / manojña`.** Unpleasant / pleasant.
These qualify the visible objects as appropriate
to the particular release and preserve the
unattractive/beautiful contrast.

**`Anvayajñānapakṣa`.** Belonging to the anvayajñāna
side. The commentary attaches this explicitly to
the path object. A loose substitution such
as “inferential thinking” would obscure the technical scope.

**`Apratisaṃkhyānirodha / ākāśa`.** Non-analytical cessation /
space. These are additional object categories in
the prose, not simply new names for the
cessation-truth object. The short sentence says
space belongs to one release without naming
that member explicitly here.

**`Līna saṃtati`.** A sunken or contracted continuum.
Brightening such a continuum after unattractive contemplation
is one reason supplied for cultivating the beautiful release.

**`Jijñāsā`.** Desire to ascertain or test. The
second reason concerns determining whether the first
two releases have been accomplished.

**`Kleśadūrīkaraṇa / samāpattivaśitva`.** Keeping defilements
at a distance / mastery of attainment. These
are the two general purposes explicitly named
for cultivating releases and related qualities.

## 8. Logical Determination

The verse classifies the object-fields of the first three releases and the formless four; the Bhāṣya supplies the list's additional limits. `[verse]` marks the two groups; `[prose]` marks the expanded fields and the space exception.

**Signature.** `FirstThree(g)`, `FormlessFour(g)`, `Includes(g,f)`, and `SpaceForOne(g)` describe object-fields at group level; these are not claims that every individual release takes every listed item at once.

```nltk-sem
# derived by the section 4 parse, not typed by hand
FirstThree(formgroup) & all g.(FirstThree(g) -> Includes(g,visible)) & FormlessFour(formlessgroup) & all g.(FormlessFour(g) -> Includes(g,ownhigher))
```

```nltk-fol
# THEORY shared
# [verse] prathamāḥ / ye ... te: group-level object-field claims, derived in section 4
FirstThree(formgroup) & all g.(FirstThree(g) -> Includes(g,visible)) & FormlessFour(formlessgroup) & all g.(FormlessFour(g) -> Includes(g,ownhigher))
# [prose] own- and higher-level truths, the anvaya-side Path, and additions
all g.(FormlessFour(g) -> (Includes(g,causefield) & Includes(g,cessationfield) & Includes(g,anvayapath) & Includes(g,nonanalytical)))
SpaceForOne(formlessgroup)
```

**Finite object-field valuation.** `SpaceForOne` deliberately does not assign space to all four or name the one release.

```nltk-valuation
formgroup => formgroup
formlessgroup => formlessgroup
visible => visible
ownhigher => ownhigher
causefield => causefield
cessationfield => cessationfield
anvayapath => anvayapath
nonanalytical => nonanalytical
spacefield => spacefield
FirstThree => {formgroup}
FormlessFour => {formlessgroup}
Includes => {(formgroup,visible),(formlessgroup,ownhigher),(formlessgroup,causefield),(formlessgroup,cessationfield),(formlessgroup,anvayapath),(formlessgroup,nonanalytical)}
SpaceForOne => {formlessgroup}
```

**Results (NLTK).** The session checker loaded the FOL and valuation; the shared theory is true in this finite model. No prover entailment was tested.

**Scope cautions.** The source says *anvayajñāna* qualifies the Path; it is not generalized to every object. The added space item belongs to one unspecified release. The Bhāṣya's beautiful-object test for mastery is not converted into a universal immunity rule.

## 9. Interpretive Note

**The path qualification is sharper than the earlier draft.**
The research's general “on the side of subsequent
knowledge” leaves unclear what it qualifies. The
prose explicitly names the anvayajñāna-side path
alongside the other truth objects. This study
retains that structure and the two additional
object categories.

**Witness cautions.** The running source's
`sukhamaṇḍeñjitatvāt` is compressed in the explanation
of third dhyāna; the local study understands
disturbance by pleasure. The short space clause
names only “one,” so its identity is not
silently supplied as an explicit statement of
this unit. The script discrepancy in the verse
is disclosed above. Originals remain untouched.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates object category, contemplative
aspect, and criterion of accomplishment. Yoga Technē,
its kriyā–karma companion, concerns the shift to
the beautiful aspect and observation of whether
affliction arises. The object-aspect can change while
the sought freedom from affliction remains the
criterion in this account.

The research's distinction between field-content and
governing relation is a useful project interpretation.
Its scope should remain tied to the stated
contemplative test rather than expanded into a
complete theory of appearance. For Organon representation,
record the two purposes and alternative reasons
for beautiful-release cultivation separately from the
object-range inventory.

**Review status.** Provisional, Bhāṣya-controlled study.
The visible-form objects, qualified formless range,
additional objects, third-dhyāna explanation, beautiful-release
test, general purposes, and direct-realization explanation
have been checked against the local research
and running source.

## 10. OWL++ Seed

```text
Class: ReleaseObjectRange
Class: ContemplativeAspect
Class: AccomplishmentCriterion
Class: CultivationPurpose

ObjectProperty: takesAsObject
ObjectProperty: testedBy
ObjectProperty: cultivatedFor

FirstThreeReleases:
    objects: DesireDomainVisibleForm
    objectQuality: UnpleasantOrPleasantAsAppropriate

FormlessReleases:
    truthObjects: OwnAndHigherLevelSufferingItsCauseAndCessation
    pathObject: EntireAnvayaJnanaSidePath
    additionalObject: NonAnalyticalCessation
    spaceObject: OneMemberSpecifiedWithoutNameInThisUnit

BeautifulReleaseCultivation:
    alternativePurposes: BrightenSunkenContinuum, TestFirstTwoReleases
    test: NoAfflictionArisesEvenUnderBeautifulAspect

GeneralReleaseCultivation:
    purposes: DistanceDefilements, MasterAttainment

ProjectConstraint: Preserve the path-specific knowledge-side qualification.
ProjectConstraint: Do not omit the additional unconditioned objects.
ProjectConstraint: Beautiful-release purposes are alternatives, not a mandatory sequence.
ProjectConstraint: Local mastery test is not universal immunity in every circumstance.
ProjectConstraint: Special realization wording does not invalidate other releases.
```

This is a declarative project seed, not executable OWL.
VAK 8.35 next introduces the eight Essences of mastery.
