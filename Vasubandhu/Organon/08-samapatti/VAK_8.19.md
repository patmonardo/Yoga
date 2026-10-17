# VAK_8.19 — Completed Skipping Attainment and Its Supports

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
The general support rule receives an explicitly announced
exception in the following verse.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `vyutkrāntakasamāpattiḥ` | nominative singular feminine compound | skipping attainment |
| `visabhāgatṛtīyagā` | nominative singular feminine compound adjective | going to the third attainment in a dissimilar mode |
| `svādhobhūmyāśrayāḥ` | nominative plural compound adjective | having supports at their own or lower levels |
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

The verse completes the previous preparation, then states a general support rule and a prose-restricted exception for a person reborn above.

```nltk-fcfg
% start S
# tokens: vyutkrāntakasamāpattir visabhāgatṛtīyagā svādhobhūmyāśrayā eva dhyānārūpyāḥ ∅-ūrdhvopapannaḥ vṛthādharam
S[SEM=?sem] -> CL[K=accomplishment] CL[K=support,SEM=?sem] CL[K=exception]
CL[K=accomplishment] -> N[CASE=nom,NUM=sg,GEN=f,KIND=skip] ADJ[CASE=nom,NUM=sg,GEN=f,MODE=dissimilar,DEST=third]
CL[K=support,SEM=<?q(?noun)>] -> ADJ[CASE=nom,NUM=?n,GEN=?g,SUPPORT=own_or_lower,SEM=?q] PTCL[RESTRICT=yes] N[CASE=nom,NUM=?n,GEN=?g,KIND=attainment,SEM=?noun]
CL[K=exception] -> N[CASE=nom,NUM=sg,GEN=m,STATUS=reborn_above,SUPPLIED=prose] ADJ[CASE=nom,NUM=sg,GEN=n,UTILITY=none]
N[CASE=nom,NUM=sg,GEN=f,KIND=skip] -> 'vyutkrāntakasamāpattir'
ADJ[CASE=nom,NUM=sg,GEN=f,MODE=dissimilar,DEST=third] -> 'visabhāgatṛtīyagā'
ADJ[CASE=nom,NUM=pl,GEN=m,SUPPORT=own_or_lower,SEM=<\P.all a.(P(a) -> SupportedOwnOrLower(a))>] -> 'svādhobhūmyāśrayā'
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
formless attainments generally have supports at their
own or lower levels; for one reborn above, a
lower attainment serves no purpose in the stated account.

## 5. Translation

### Literal Translation

> Skipping attainment goes to the third in a dissimilar
> mode. The dhyānas and formless attainments have
> supports only at their own or lower levels.
> The lower is without use.

### Bhāṣya-informed study translation

> Skipping attainment is accomplished by going to the third item in a
> dissimilar mode. Dhyānas and formless attainments are made present
> only on supports belonging to their own or a lower level; for one
> reborn above, a lower attainment is without use.

## 6. Philosophical Translation

> Completion requires command of both level-distance
> and difference of mode. The commentary also distinguishes
> freedom from affliction from mastery of samādhi:
> neither qualification alone suffices for this accomplishment.
> A separate inquiry then concerns the existential
> support upon which an attainment can be made present.

Rebirth-support and a currently entered attainment must
remain distinct. The support rule cannot be generalized
into a prohibition on descending in practice after
having mastered a higher attainment, since reverse
traversal is explicitly part of this very account.

## 7. Technical Vocabulary

**Source.** Pradhan 446|06–446|21, checked against the local Bhāṣya
study and running source. The Bhāṣya's example runs from contaminated
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

**`Dṛṣṭiprāpta`.** The one attained through view. In
the contrast here, sharp faculties yield mastery
of samādhi, but complete freedom from defilements
is lacking.

**`Samayavimukta`.** Liberated depending on occasion.
In the present contrast, freedom from defilements
is present but the required mastery of samādhi is lacking.

**`Āśraya`.** Support, here determined through the
level of rebirth. It must not be equated with
the immediately preceding attainment in a traversal.

**`Saṃmukhīkaroti`.** Makes present, brings into operation.
The question concerns actual manifestation of the
attainment on a support, not merely its abstract
availability or acquisition of possession.

**`Prayojana`.** Purpose or use. The prose explains
the general exclusion of a lower attainment for
a higher-born support through lack of a relevant
purpose, and immediately proceeds to an exception.

## 8. Logical Determination

The verse completes the skipping sequence and states the general level of support for dhyāna and formless attainments. The Bhāṣya also gives the qualified practitioner who accomplishes the skip. Provenance: `[verse]`, `[prose]`.

**Signature.** `SkipStep/2(a,b)`—one step in the skipping sequence; `InThreeContinents/1(p)`—practitioner in the Bhāṣya’s stated scope; `FreeOfDefilement/1`, `MasteryOfSamadhi/1`, `ProducesSkip/1`—eligibility and capacity; `RebornAbove/1(p)`—rebirth above the lower attainment; `LowerAttainment/1(a)`—attainment below that support; `Useful/2(p,a)`—a is useful to p there; `DhyanaArupya/1(a)` and `SupportedOwnOrLower/1(a)`—the derived general support relation.

```nltk-sem
# derived by the section 4 parse, not typed by hand
all a.(DhyanaArupya(a) -> SupportedOwnOrLower(a))
```

```nltk-valuation
firstContaminated => firstContaminated
thirdUncontaminated => thirdUncontaminated
spaceContaminated => spaceContaminated
nothingnessUncontaminated => nothingnessUncontaminated
adept => adept
upperBorn => upperBorn
lowerDhyana => lowerDhyana
representativeAttainment => representativeAttainment
DhyanaArupya => {representativeAttainment}
SupportedOwnOrLower => {representativeAttainment}
SkipStep => {(firstContaminated,thirdUncontaminated),(thirdUncontaminated,spaceContaminated),(spaceContaminated,nothingnessUncontaminated),(nothingnessUncontaminated,spaceContaminated),(spaceContaminated,thirdUncontaminated),(thirdUncontaminated,firstContaminated)}
InThreeContinents => {adept}
FreeOfDefilement => {adept}
MasteryOfSamadhi => {adept}
ProducesSkip => {adept}
RebornAbove => {upperBorn}
LowerAttainment => {lowerDhyana}
Useful => {}
```

```nltk-fol
# THEORY shared
# [verse] derived own-or-lower support restriction from the section 4 parse
all a.(DhyanaArupya(a) -> SupportedOwnOrLower(a))
# [verse] third-in-a-dissimilar-mode pattern; the list records the Bhāṣya's example and reverse
SkipStep(firstContaminated,thirdUncontaminated)
SkipStep(thirdUncontaminated,spaceContaminated)
SkipStep(spaceContaminated,nothingnessUncontaminated)
SkipStep(nothingnessUncontaminated,spaceContaminated)
SkipStep(spaceContaminated,thirdUncontaminated)
SkipStep(thirdUncontaminated,firstContaminated)
# [prose] within the three continents, both qualifications are stated for the producer
all p.((InThreeContinents(p) & FreeOfDefilement(p) & MasteryOfSamadhi(p)) -> ProducesSkip(p))
# [verse, prose] general support rule's upper-born lower-attainment case
all p.all a.((RebornAbove(p) & LowerAttainment(a)) -> -Useful(p,a))
```

**Results (NLTK).** `Model.satisfy` checks the skip-step facts, the derived own-or-lower support rule, and both general rules in the finite example. The support example encodes the lower attainment as useless for the one reborn above, not as impossible to enter in every context.

**Scope cautions.** The three-continent eligibility is Bhāṣya-only. `vṛthā` is limited to the upper-born case; reverse practice traversal is not rebirth above. The exception is the next verse and is deliberately not folded into the general support rule.

## 9. Interpretive Note

**Two inquiries share the verse.** The opening completes
the skipping-attainment account; the second part opens
the support inquiry. Practitioner eligibility for the
special accomplishment and support eligibility for
dhyāna/ārūpya manifestation answer different questions.
Neither should silently replace the other.

**Witness cautions.** The running source contains the
isolated `dhyānāśrayā eva` between quoted verse fragments,
and its final reference marker reverses page numbers.
The following explicit bhavāgra example and generalization
to the remaining attainments control the support reading.
The verse's vṛthādharam and the running vṛthā'dharam
are understood through the same prose explanation;
no critical emendation of the witnesses is undertaken.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates the distance, mode difference,
practitioner qualifications, and support relation. Yoga
Technē, its kriyā–karma companion, concerns the effective
exercise that distinguishes preparation from accomplishment.
The completed example requires the coordinated operation
of distinctions already established in the preceding studies.

For Organon representation, separate traversal position
from rebirth-support. Preserve the general rule together
with its announced exception, rather than turning
“only” into an unqualified prohibition detached from
the next sentence. This is project reconstruction,
not a further system attributed to the Bhāṣya.

**Review status.** Provisional, Bhāṣya-controlled study.
The alternating-mode example, skip limit, practitioner
contrasts, three-continent restriction, support examples,
rebirth scope, and announced exception have been checked
against the local research and running source.

## 10. OWL++ Seed

```text
Class: CompletedSkippingAttainment
Class: PractitionerQualification
Class: RebirthSupport
Class: GeneralSupportRule

ObjectProperty: changesModeBetweenEntries
ObjectProperty: skipsInterveningLevel
ObjectProperty: requiresQualification
ObjectProperty: manifestedOnSupport

CompletedSkippingAttainment:
    skippedInterveningLevelsPerMove: 1
    modePattern: Contaminated, Uncontaminated, Contaminated, Uncontaminated
    directions: Forward, Reverse
    practitioner: AsamayavimuktaArhat
    qualifications: FreedomFromDefilements, SamadhiMastery
    statedLocation: ThreeContinents

GeneralDhyanaArupyaSupportRule:
    supportRelativeToAttainment: SameLevelOrLower
    status: GeneralRuleWithExceptionContinuingInVAK8_20

LowerAttainmentForHigherBornSupport:
    generalExplanation: NoRelevantPurposeBecauseInferior

ProjectConstraint: Third counts the starting level as first.
ProjectConstraint: Fourth-relative-station exclusion is not fourth-dhyana exclusion.
ProjectConstraint: Rebirth-support is not the preceding attainment in practice.
ProjectConstraint: Higher attainment mastery does not prohibit reverse traversal.
ProjectConstraint: Preserve both qualifications for completed skipping attainment.
ProjectConstraint: Lower knowledge operation is not necessarily lower samapatti.
ProjectConstraint: Do not make the general support rule exceptionless.
```

This is a declarative project seed, not executable OWL.
VAK 8.20 next gives the summit exception and begins
the analysis of the attainments' objects.
