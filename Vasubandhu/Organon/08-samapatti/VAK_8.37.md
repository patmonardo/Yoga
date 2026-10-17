# VAK_8.37 — Acquisition, Habituation, and Support

## 1. Sanskrit (Devanāgarī)

```sanskrit
निरोध उक्तः वैराग्यप्रयोगाप्तं तु शेषितम् ।
त्रिधात्वाश्रयमारूप्यसंज्ञं शेषं मनुष्यजम् ॥ ८.३७ ॥
```

## 2. Sanskrit (IAST)

```text
nirodha uktaḥ vairāgyaprayogāptaṃ tu śeṣitam |
tridhātvāśrayam ārūpyasaṃjñaṃ śeṣaṃ manuṣyajam || 8.37 ||
```

The local verse is retained with analytical hyphens
removed. The running source presents the same
clauses separately within the explanatory prose.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `nirodhaḥ` | nominative singular masculine | cessation, here cessation-release |
| `uktaḥ` | nominative singular masculine past passive participle of √vac | has been explained |
| `vairāgyaprayogāptam` | nominative singular neuter compound predicate | acquired through dispassion or application |
| `tu` | indeclinable | but; as for |
| `śeṣitam` | nominative singular neuter, substantivized | what remains after setting cessation aside |
| `tridhātvāśrayam` | nominative singular neuter compound adjective | having support in the three domains |
| `ārūpyasaṃjñam` | nominative singular neuter compound adjective, substantivized | what bears the designation “formless” |
| `śeṣam` | nominative singular neuter, substantivized | the rest after the formless group is distinguished |
| `manuṣyajam` | nominative singular neuter compound adjective | human-born; generated on human support |

Sandhi: `dhātu + āśraya` > `dhātvāśraya`; `prayoga + āpta`
> `prayogāpta`. Āpta is the acquired/obtained
participle of √āp. The neuter singulars collect
several practices under one description.

## 4. Grammar

The neuter singulars classify the remainder and distinguish the formless group from what is human-born. Acquisition is through dispassion or application, depending on habituation; the two `śeṣa` forms have different scopes.

```nltk-fcfg
% start S
# tokens: nirodha uktaḥ ∅-nirodhavimokṣaḥ vairāgyaprayogāptam tu śeṣitam ∅-ucitānucitatvāt tridhātvāśrayam ārūpyasaṃjñam ∅-ārūpyavimokṣāḥ ∅-ārūpyakṛtsnāni śeṣam manuṣyajam ∅-manuṣyāśrayam
S -> CL[K=cessation] CL[K=acquisition] CL[K=formlesssupport] CL[K=humansupport]

CL[K=cessation] -> N[CASE=?c,NUM=?n,GEN=?g] PTCP[CASE=?c,NUM=?n,GEN=?g,TENSE=past] N[CASE=?c,NUM=?n,GEN=?g,SUPPLIED=prose]
CL[K=acquisition] -> ADJ[CASE=?c,NUM=?n,GEN=?g,ROUTE=either] PTCL[CONTRAST=yes] ADJ[CASE=?c,NUM=?n,GEN=?g,REMAINDER=yes] N[CASE=abl,NUM=sg,GEN=n,SUPPLIED=prose]
CL[K=formlesssupport] -> ADJ[CASE=?c,NUM=?n,GEN=?g,SUPPORT=threedomain] ADJ[CASE=?c,NUM=?n,GEN=?g,DESIGNATION=formless] N[CASE=nom,NUM=pl,GEN=m,SUPPLIED=prose] N[CASE=nom,NUM=pl,GEN=n,SUPPLIED=prose]
CL[K=humansupport] -> ADJ[CASE=?c,NUM=?n,GEN=?g,REMAINDER=yes] ADJ[CASE=?c,NUM=?n,GEN=?g,ORIGIN=human] N[CASE=loc,NUM=sg,GEN=n,SUPPLIED=prose]

N[CASE=nom,NUM=sg,GEN=m] -> 'nirodha'
PTCP[CASE=nom,NUM=sg,GEN=m,TENSE=past] -> 'uktaḥ'
N[CASE=nom,NUM=sg,GEN=m,SUPPLIED=prose] -> '∅-nirodhavimokṣaḥ'
ADJ[CASE=nom,NUM=sg,GEN=n,ROUTE=either] -> 'vairāgyaprayogāptam'
PTCL[CONTRAST=yes] -> 'tu'
ADJ[CASE=nom,NUM=sg,GEN=n,REMAINDER=yes] -> 'śeṣitam'
N[CASE=abl,NUM=sg,GEN=n,SUPPLIED=prose] -> '∅-ucitānucitatvāt'
ADJ[CASE=nom,NUM=sg,GEN=n,SUPPORT=threedomain] -> 'tridhātvāśrayam'
ADJ[CASE=nom,NUM=sg,GEN=n,DESIGNATION=formless] -> 'ārūpyasaṃjñam'
N[CASE=nom,NUM=pl,GEN=m,SUPPLIED=prose] -> '∅-ārūpyavimokṣāḥ'
N[CASE=nom,NUM=pl,GEN=n,SUPPLIED=prose] -> '∅-ārūpyakṛtsnāni'
ADJ[CASE=nom,NUM=sg,GEN=n,REMAINDER=yes] -> 'śeṣam'
ADJ[CASE=nom,NUM=sg,GEN=n,ORIGIN=human] -> 'manuṣyajam'
N[CASE=loc,NUM=sg,GEN=n,SUPPLIED=prose] -> '∅-manuṣyāśrayam'
```

```nltk-dep
'nirodha' -> 'uktaḥ' | '∅-nirodhavimokṣaḥ'
'śeṣitam' -> 'vairāgyaprayogāptam' | 'tu' | '∅-ucitānucitatvāt'
'ārūpyasaṃjñam' -> 'tridhātvāśrayam' | '∅-ārūpyavimokṣāḥ' | '∅-ārūpyakṛtsnāni'
'śeṣam' -> 'manuṣyajam' | '∅-manuṣyāśrayam'
```

`Nirodha` is already explained, not subjected to the acquisition rule.
`Tridhātvāśrayam` attaches only to what is called formless; the final human-production clause excludes that group and the source explains it through instruction.
**Close construe.** Cessation has been explained. The
remaining practices are acquired through dispassion or
application. Those designated formless have support in
the three domains; the rest are generated
on human support.

## 5. Translation

### Literal Translation

> Cessation has been explained. The remainder, however,
> is acquired through dispassion or application.
> What is designated formless has support in
> the three domains; the rest is human-born.

### Bhāṣya-informed study translation

> Cessation-release has been explained. The remainder, however, is
> acquired through dispassion or through application. What is designated
> formless has support in the three domains; the rest is human-born,
> produced on human support.

## 6. Philosophical Translation

> An attainment's acquisition depends on the practitioner's
> formation as well as the practice's classification.
> Habituation permits one acquisition account; lack of
> habituation calls for deliberate cultivation. The support
> on which a practice is produced is a
> further condition, with instruction explicitly explaining
> the human support of the non-formless remainder.

This is a reconstruction of the commentary's
practical argument. It does not turn the two
acquisition routes into two different kinds of
ultimate attainment or an exhaustive theory of learning.

## 7. Technical Vocabulary

**`Nirodhavimokṣa`.** Cessation-release. It is set aside
here by reference to its previous explanation.
It should not be included in the remainder
merely because it is the eighth release.

**`Vairāgya / vairāgyalābhika`.** Dispassion / obtained
through dispassion. These name an acquisition route.
The local contrast does not establish that
every dispassion-related acquisition is an uncontaminated attainment.

**`Prayoga / prāyogika`.** Deliberate application /
acquired through such application. Here prayoga concerns
cultivation as an acquisition route, not a new
assignment to one of the access-attainment levels.

**`Ucita / anucita`.** Habituated / unhabituated.
The prose's ucitānucitatvāt gives the reason for
the two acquisition descriptions. Its ordered pairing
supports dispassion-acquisition for the habituated case and
application for the unhabituated case.

**`Ārūpyasaṃjña`.** Designated as formless. Saṃjñā
functions here in the sense of a designation;
the compound does not introduce another perception-attainment
or a new formless level.

**`Traidhātukāśraya`.** Having support across the three
domains: desire, form, and formless. These are
the three existential domains, not the eighteen
dhātus of the earlier cognition-domain classification.

**`Manuṣyāśraya`.** Human support. The predicate concerns
the bearer/support on which the practice is
produced; it does not mean that humans
are its contemplative object.

**`Upadeśasāmarthya`.** Efficacy of instruction. This
is the source's reason for the human-production
rule. It is more specific than a general
appeal to human intelligence or superior motivation.

## 8. Logical Determination

The verse sets cessation aside, gives two acquisition routes for the remainder, then divides support: formless-designated practices have three-domain support; the remainder is human-born. The Bhāṣya ties the two routes to habituation. `[verse]` / `[prose]`.

**Signature.** `Cessation(x)`, `Remaining(x)`, `Habituated(x)`, `ViaDispassion(x)`, `ViaApplication(x)`, `FormlessDesignated(x)`, `ThreeDomainSupport(x)`, `HumanRemainder(x)`, and `HumanSupport(x)`.

```nltk-valuation
cessationpractice => cessationpractice
habitpractice => habitpractice
newpractice => newpractice
formlessgroup => formlessgroup
humanremainder => humanremainder
Cessation => {cessationpractice}
Remaining => {habitpractice,newpractice}
Habituated => {habitpractice}
ViaDispassion => {habitpractice}
ViaApplication => {newpractice}
FormlessDesignated => {formlessgroup}
ThreeDomainSupport => {formlessgroup}
HumanRemainder => {humanremainder}
HumanSupport => {humanremainder}
```

```nltk-fol
# THEORY shared
# [verse] nirodha uktaḥ: cessation is distinguished from the remainder
Cessation(cessationpractice)
# [prose] ucita / anucita: habituated / unhabituated acquisition
all x.((Remaining(x) & Habituated(x)) -> ViaDispassion(x))
all x.((Remaining(x) & -Habituated(x)) -> ViaApplication(x))
# [verse] arūpyasaṃjña; [prose] formess attainments and totalities
all x.(FormlessDesignated(x) -> ThreeDomainSupport(x))
all x.(HumanRemainder(x) -> HumanSupport(x))
```

**Results (NLTK).** The checker reports the shared rules true in this finite model of both acquisition routes and both support classes. No entailment or exhaustive census was tested.

**Scope cautions.** The model's `Remaining` and `HumanRemainder` classes are not asserted to be coextensive: the verse's first `śeṣitam` excludes cessation from acquisition, while the later human-born `śeṣam` has a different scope. Three-domain support is not object-field or attainment-level.

## 9. Interpretive Note

**Construe of the support clause.** Three-domain
support belongs to the formless group only, not to the whole remainder, and
human-generation belongs to the rest. The Bhāṣya
prose explicitly confirms this: formless releases
and formless totalities have three-domain support; the
rest have human support. The translations
follow that controlled construe.

**Source voice and limits.** The passage is
expository and introduces no competing school authority.
Its short habituation clause supports the ordered
pairing used above, but gives no detailed
history of the practitioner's prior training. The
account should not be supplemented with an
invented schedule or automatic-acquisition mechanism.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates practice-type, acquisition route,
prior habituation, and support as separate determinations.
Yoga Technē, its kriyā–karma companion, concerns the
effective cultivation and instruction through which capacities
are produced in the specified circumstances.

The research's “history of formation” is useful
project language for the role of habituation.
The source gives conditions for acquiring these
particular practices. A general account of transcendental
training or the constitution of the agent would
be a further Organon development, not a translation
of ucitānucitatva or upadeśasāmarthya by themselves.

**Review status.** Provisional, Bhāṣya-controlled study.
The cessation exclusion, two acquisition routes, habituation
explanation, restricted three-domain support, human-production rule,
and instructional reason have been checked against
the local witnesses and running source. The
support reversal is excluded in this
study.

## 10. OWL++ Seed

```text
Class: ContemplativePractice
Class: AcquisitionRoute
Class: HabituationStatus
Class: RebirthSupport
Class: ProductionCondition

ObjectProperty: acquiredThrough
ObjectProperty: conditionedByHabituation
ObjectProperty: hasPossibleSupport
ObjectProperty: productionExplainedBy

PracticesOtherThanCessationRelease:
    acquisitionRoutes: Dispassion, DeliberateApplication
    routeVariation: HabituatedOrUnhabituated

HabituatedAcquisitionCase:
    route: Dispassion

UnhabituatedAcquisitionCase:
    route: DeliberateApplication

FormlessSupportGroup:
    members: FourFormlessReleases, TwoFormlessTotalities
    possibleSupportDomains: Desire, Form, Formless

HumanProductionGroup:
    members: FirstThreeReleases, EightMasteryEssences, FirstEightTotalities
    productionSupport: Human
    productionExplanation: EfficacyOfInstruction

CessationRelease:
    treatment: PreviouslyExplained
    excludedFrom: PresentRemainderAcquisitionRule

ProjectConstraint: Acquisition route is not a separate attainment species.
ProjectConstraint: Three-domain support applies to the specified formless group.
ProjectConstraint: Human production applies to the non-formless remainder.
ProjectConstraint: Support, object, and attainment-level remain distinct.
ProjectConstraint: Production rule does not itself settle all later possession cases.
ProjectConstraint: Local instruction explanation is not a universal denial of nonhuman teaching.
```

This is a declarative project seed, not executable OWL.
VAK 8.38 next examines the causes of attainment
production in the form and formless domains.
