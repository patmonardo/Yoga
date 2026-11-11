# VAK_8.19 — Completed Skipping Attainment and Its Bases

## 1. Sanskrit (Devanāgarī)

```sanskrit
व्युत्क्रान्तकसमापत्तिर्विसभागतृतीयगा ।
स्वाधोभूम्याश्रया एव ध्यानारूप्याः वृथाधरम् ॥ ८.१९ ॥
```

## 2. Sanskrit (IAST)

```text
vyutkrāntakasamāpattir visabhāgatṛtīyagā |
svādhobhūmyāśrayā eva dhyānārūpyāḥ vṛthādharam || 8.19 ||
```

The Sanskrit follows the local kārikā witness, with
analytical hyphens removed in continuous IAST. The
opening completes the construction begun in VAK 8.18.
The general basis rule receives an explicitly announced
exception in the following verse.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `vyutkrāntakasamāpattiḥ` | nominative singular feminine compound | skipping attainment |
| `visabhāgatṛtīyagā` | nominative singular feminine compound adjective | going to the third attainment in a dissimilar mode |
| `svādhobhūmyāśrayāḥ` | nominative plural compound adjective | taking beings at their own or lower grounds as Basis |
| `eva` | restrictive particle | only, in the stated general rule |
| `dhyānārūpyāḥ` | transmitted nominative plural collective designation | dhyānas and formless attainments |
| `vṛthā` | indeclinable | without use; to no purpose |
| `adharam` | nominative singular neuter | the lower [attainment] |

`Samāpattiḥ + visabhāga-` yields `samāpattir
visabhāga-`; `bhūmi + āśraya` yields `bhūmyāśraya`;
`āśrayāḥ + eva` yields `āśrayā eva`;
`vṛthā + adharam` yields `vṛthādharam`.
The verse's collective dhyānārūpyāḥ is retained rather
than silently regularized to another inflection.

## 4. Grammar

The verse completes the previous preparation, then states a general basis rule and a prose-restricted exception for a person reborn above.

```nltk-fcfg
% start S
# tokens: vyutkrāntakasamāpattir visabhāgatṛtīyagā svādhobhūmyāśrayā eva dhyānārūpyāḥ ∅-ūrdhvopapannaḥ vṛthādharam
S[SEM=?sem] -> CL[K=accomplishment] CL[K=basis,SEM=?sem] CL[K=upper_born_case]
CL[K=accomplishment] -> N[CASE=nom,NUM=sg,GEN=f,KIND=skip] ADJ[CASE=nom,NUM=sg,GEN=f,MODE=dissimilar,DEST=third]
CL[K=basis,SEM=<?q(?noun)>] -> ADJ[CASE=nom,NUM=?n,GEN=?g,BASIS=own_or_lower,SEM=?q] PTCL[RESTRICT=yes] N[CASE=nom,NUM=?n,GEN=?g,KIND=attainment,SEM=?noun]
CL[K=upper_born_case] -> N[CASE=nom,NUM=sg,GEN=m,STATUS=reborn_above,SUPPLIED=prose] ADJ[CASE=nom,NUM=sg,GEN=n,UTILITY=none]
N[CASE=nom,NUM=sg,GEN=f,KIND=skip] -> 'vyutkrāntakasamāpattir'
ADJ[CASE=nom,NUM=sg,GEN=f,MODE=dissimilar,DEST=third] -> 'visabhāgatṛtīyagā'
ADJ[CASE=nom,NUM=pl,GEN=m,BASIS=own_or_lower,SEM=<\P.all a.(P(a) -> BasedOwnOrLower(a))>] -> 'svādhobhūmyāśrayā'
PTCL[RESTRICT=yes] -> 'eva'
N[CASE=nom,NUM=pl,GEN=m,KIND=attainment,SEM=<\a.DhyanaArupya(a)>] -> 'dhyānārūpyāḥ'
N[CASE=nom,NUM=sg,GEN=m,STATUS=reborn_above,SUPPLIED=prose] -> '∅-ūrdhvopapannaḥ'
ADJ[CASE=nom,NUM=sg,GEN=n,UTILITY=none] -> 'vṛthādharam'
```

```nltk-dep
'vyutkrāntakasamāpattir' -> 'visabhāgatṛtīyagā'
'dhyānārūpyāḥ' -> 'svādhobhūmyāśrayā' | 'eva'
'vṛthādharam' -> '∅-ūrdhvopapannaḥ'
```

Tṛtīya is relative to the predecessor and visabhāga marks the alternation of
contaminated/uncontaminated mode. “Without use” is locally scoped to the reborn-above
case, not every lower attainment.

**Close construe.** Skipping attainment goes to the
third attainment in a dissimilar mode. Dhyānas and
formless attainments have beings of their own or
lower grounds as Basis; for one reborn above, a
lower attainment serves no purpose in the stated account.

## 5. Translation

### Literal Translation

> Skipping attainment goes to the third in a dissimilar
> mode. The dhyānas and formless attainments have
> as Basis only beings of their own or lower grounds.
> The lower is without use.

### Bhāṣya-informed study translation

> Skipping attainment is accomplished by going to the third item in a
> dissimilar mode. Dhyānas and formless attainments can be made present
> with beings of their own or a lower ground as Basis; for one reborn
> above, a lower attainment is without use.

## 6. Philosophical Translation

> Completion requires command of both level-distance
> and difference of mode. The commentary also distinguishes
> freedom from affliction from mastery of samādhi:
> neither qualification alone suffices for this accomplishment.
> A separate inquiry then asks which beings can serve
> as Basis for an attainment.

A being serving as Basis and a currently entered attainment must
remain distinct. The basis rule cannot be generalized
into a prohibition on descending in practice after
having mastered a higher attainment, since reverse
traversal is explicitly part of this very account.

## 7. Technical Vocabulary

**Source.** The shared skipping account begins at [445|16];
the 8.19 Basis discussion ends at the malformed [445|21–446|21]
label. The complete span is checked against the local witness.
The Bhāṣya's example runs from contaminated
first dhyāna to uncontaminated third dhyāna, to contaminated infinite
space, to uncontaminated nothingness, and likewise in reverse; a fourth
relative station is too distant. In the three continents only an arhat
liberated independently of occasion produces it, requiring both freedom
from defilement and mastery over samādhi. The transition at 446|22
announces the exception analyzed in VAK 8.20.

**`Visabhāga`.** Dissimilar in mode: contaminated versus
uncontaminated in the example. It does not mean
opposed ethical qualities such as wholesome versus defiled.

**`Abhiniṣpanna`.** Accomplished or perfected. This marks
the passage from the preparation of VAK 8.18 to
the alternating-mode skip sequence.

**`Asamayavimukta`.** Liberated independently of occasion.
Retained as a technical arhat classification: it is
not a claim about existence outside time. The
prose identifies this practitioner by the conjunction
of freedom from defilement and mastery of samādhi.

**`Dṛṣṭiprāpta`.** Attained through Seeing. In
the contrast here, sharp faculties yield mastery
of samādhi, but complete freedom from defilements
is lacking.

**`Samayavimukta`.** Liberated in dependence on occasion.
In the present contrast, freedom from defilements
is present but the required mastery of samādhi is lacking.

**`Āśraya`.** Basis: here the bearer is a being
reborn at the attainment's own or a lower ground. It must not be
equated with the immediately preceding attainment in a traversal.

**`Saṃmukhīkaroti`.** Makes present, brings into operation.
The question concerns actual manifestation of the
attainment on a basis, not merely its abstract
availability or acquisition of possession.

**`Prayojana`.** Purpose or use. The prose explains
the general exclusion of a lower attainment for
a higher-born basis through lack of a relevant
purpose, and immediately proceeds to an exception.

## 8. Logical Determination

The verse completes the skipping sequence and states the general level of basis for dhyāna and formless attainments. The Bhāṣya also gives the qualified practitioner who accomplishes the skip. Provenance: `[verse]`, `[prose]`.

**Signature.** `SkipStep/2(a,b)`—one step in the skipping sequence; `InThreeContinents/1(p)`—practitioner in the Bhāṣya’s stated scope; `FreeOfDefilement/1`, `MasteryOfSamadhi/1`, `ProducesSkip/1`—eligibility and capacity; `MayManifest/2(p,a)`—a being can make an attainment present; `OwnOrLowerBasis/2(p,a)`—that being is on the attainment's own or a lower ground; `BasedOwnOrLower/1(a)`—the verse's compressed eligibility condition; `OrdinaryCase/2(p,a)`—the case before 8.20's exception; `RebornAbove/1(p)`, `LowerAttainment/1(a)`, and `Useful/2(p,a)`—the no-purpose explanation.

```nltk-sem
# derived by the section 4 parse, not typed by hand
all a.(DhyanaArupya(a) -> BasedOwnOrLower(a))
```

```nltk-valuation
firstContaminated => firstContaminated
thirdUncontaminated => thirdUncontaminated
spaceContaminated => spaceContaminated
nothingnessUncontaminated => nothingnessUncontaminated
adept => adept
upperBorn => upperBorn
desireBeing => desireBeing
lowerDhyana => lowerDhyana
summitAttainment => summitAttainment
representativeAttainment => representativeAttainment
DhyanaArupya => {representativeAttainment,summitAttainment,lowerDhyana}
BasedOwnOrLower => {representativeAttainment,summitAttainment,lowerDhyana}
OwnOrLowerBasis => {(upperBorn,summitAttainment),(desireBeing,summitAttainment),(desireBeing,lowerDhyana)}
MayManifest => {(upperBorn,summitAttainment),(desireBeing,summitAttainment),(desireBeing,lowerDhyana)}
SkipStep => {(firstContaminated,thirdUncontaminated),(thirdUncontaminated,spaceContaminated),(spaceContaminated,nothingnessUncontaminated),(nothingnessUncontaminated,spaceContaminated),(spaceContaminated,thirdUncontaminated),(thirdUncontaminated,firstContaminated)}
InThreeContinents => {adept}
FreeOfDefilement => {adept}
MasteryOfSamadhi => {adept}
ProducesSkip => {adept}
RebornAbove => {upperBorn}
LowerAttainment => {lowerDhyana}
OrdinaryCase => {(upperBorn,lowerDhyana)}
Useful => {}
```

```nltk-fol
# THEORY shared
# [verse] derived own-or-lower basis restriction from the section 4 parse
all a.(DhyanaArupya(a) -> BasedOwnOrLower(a))
# [prose] the Basis is a being on the attainment's own or a lower ground
all p.all a.((MayManifest(p,a) & DhyanaArupya(a)) -> OwnOrLowerBasis(p,a))
# [verse] third-in-a-dissimilar-mode pattern; the list records the Bhāṣya's example and reverse
SkipStep(firstContaminated,thirdUncontaminated)
SkipStep(thirdUncontaminated,spaceContaminated)
SkipStep(spaceContaminated,nothingnessUncontaminated)
SkipStep(nothingnessUncontaminated,spaceContaminated)
SkipStep(spaceContaminated,thirdUncontaminated)
SkipStep(thirdUncontaminated,firstContaminated)
# [prose] within the three continents, both qualifications are stated for the producer
all p.((InThreeContinents(p) & FreeOfDefilement(p) & MasteryOfSamadhi(p)) -> ProducesSkip(p))
# [verse, prose] the ordinary upper-born case, before the announced exception
all p.all a.((OrdinaryCase(p,a) & RebornAbove(p) & LowerAttainment(a)) -> -Useful(p,a))
```

**Results (NLTK).** `Model.satisfy` checks the skip-step facts, the derived verse condition, the being–attainment Basis pairs, and the scoped no-purpose rule. The model does not turn the ordinary case into an exceptionless prohibition.

**Scope cautions.** The three-continent eligibility is Bhāṣya-only. `vṛthā` is stated for the ordinary upper-born case; reverse practice traversal is not rebirth above. `BasedOwnOrLower` abbreviates the verse, while `OwnOrLowerBasis` records the bearer relation. The exception is the next verse and is deliberately not folded into the general Basis rule.

## 9. Interpretive Note

**Two inquiries share the verse.** The opening completes
the skipping-attainment account; the second part opens
the basis inquiry. Practitioner eligibility for the
special accomplishment and basis eligibility for
dhyāna/ārūpya manifestation answer different questions.
Neither should silently replace the other.

**Witness cautions.** The running source contains the
isolated `dhyānāśrayā eva` between quoted verse fragments,
and its final reference marker reverses page numbers. The
phrase's syntax remains open. [Pruden's parallel](https://dhamma-library.cdn.winmetta.org/13.%20Rear-Buddhist-Books-1/Abhidharmakosa%20Bhasyam%20IV%20%28Leo%20M.%20Pruden%29.pdf)
identifies beings of the attainment's own or lower ground
as its Basis; this corroborates the bearer reading without
repairing the local phrase.
The following explicit bhavāgra example and generalization
to the remaining attainments control the basis reading.
The verse's vṛthādharam and the running vṛthā'dharam
are understood through the same prose explanation;
no critical emendation of the witnesses is undertaken.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates the distance, mode difference,
practitioner qualifications, and basis relation. Yoga
Technē, its kriyā–karma companion, concerns the effective
exercise that distinguishes preparation from accomplishment.
The completed example requires the coordinated operation
of distinctions already established in the preceding studies.

For Organon representation, separate traversal position
from rebirth-basis. Preserve the general rule together
with its announced exception, rather than turning
“only” into an unqualified prohibition detached from
the next sentence. This is project reconstruction,
not a further system attributed to the Bhāṣya.

**Review status.** Complete shared [445|16]–[445|21–446|21]
unit collated and translated in the paired Bhāṣya study. The first
8.19 pāda at [445|18] overlaps 8.18's preparatory unit; [446|22]
opens 8.20. The alternating-mode example, skip limit, practitioner
contrasts, three-continent restriction, basis examples,
rebirth scope, and announced exception have been checked
against the local research and running source.

## 10. OWL++ Seed

```text
Class: CompletedSkippingAttainment
Class: PractitionerQualification
Class: BeingAsBasis
Class: GeneralBasisRule

ObjectProperty: changesModeBetweenEntries
ObjectProperty: skipsInterveningLevel
ObjectProperty: requiresQualification
ObjectProperty: manifestedOnBasis

CompletedSkippingAttainment:
    skippedInterveningLevelsPerMove: 1
    modePattern: Contaminated, Uncontaminated, Contaminated, Uncontaminated
    directions: Forward, Reverse
    practitioner: AsamayavimuktaArhat
    qualifications: FreedomFromDefilements, SamadhiMastery
    statedLocation: ThreeContinents

GeneralDhyanaArupyaBasisRule:
    basisRelativeToAttainment: SameLevelOrLower
    status: GeneralRuleWithExceptionContinuingInVAK8_20

LowerAttainmentForHigherBornBasis:
    generalExplanation: NoRelevantPurposeBecauseInferior

ProjectConstraint: Third counts the starting level as first.
ProjectConstraint: Fourth-relative-station exclusion is not fourth-dhyana exclusion.
ProjectConstraint: A being serving as Basis is not the preceding attainment in practice.
ProjectConstraint: Higher attainment mastery does not prohibit reverse traversal.
ProjectConstraint: Preserve both qualifications for completed skipping attainment.
ProjectConstraint: Lower Cognition operation is not necessarily lower samapatti.
ProjectConstraint: Do not make the general basis rule exceptionless.
```

This is a declarative project seed, not executable OWL.
VAK 8.20 next gives the summit exception and begins
the analysis of the attainments' objects.
