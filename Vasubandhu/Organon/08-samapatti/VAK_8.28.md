# VAK_8.28 — Completing the Four Cultivations of Samādhi

## 1. Sanskrit (Devanāgarī)

```sanskrit
दर्शनायाक्ष्यभिज्ञेष्टा धीभेदाय प्रयोगजाः ।
वज्रोपमोऽन्त्ये यो ध्याने सास्रवक्षयभावना ॥ ८.२८ ॥
```

## 2. Sanskrit (IAST)

```text
darśanāyākṣyabhijñeṣṭā dhībhedāya prayogajāḥ |
vajropamo 'ntye yo dhyāne sāsravakṣayabhāvanā || 8.28 ||
```

The Sanskrit follows the local kārikā witness. The
final continuous expression must be resolved through
the prose as sā āsravakṣayabhāvanā, not as a
compound beginning with sāsrava, contaminated.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `darśanāya` | dative singular neuter | for seeing, expanded as knowledge-and-seeing |
| `akṣyabhijñā` | nominative singular feminine compound | superknowledge of the eye |
| `iṣṭā` | nominative singular feminine participle | held or intended [as the cultivation] |
| `dhībhedāya` | dative singular masculine compound | for differentiation of understanding, glossed as prajñā |
| `prayogajāḥ` | nominative plural masculine adjective | born of application [qualities] |
| `vajropamaḥ` | nominative singular masculine adjective | vajra-like [samādhi] |
| `antye` | locative singular adjective | in the last |
| `yaḥ` | nominative singular masculine relative pronoun | which [samādhi] |
| `dhyāne` | locative singular neuter | dhyāna |
| `sā` | nominative singular feminine demonstrative | that [cultivation] |
| `āsravakṣayabhāvanā` | nominative singular feminine compound | cultivation for destruction of the outflows |

`Darśanāya + akṣi-` yields `darśanāyākṣi-`;
`akṣi + abhijñā + iṣṭā` yields `akṣyabhijñeṣṭā`;
`vajra + upama` yields `vajropama`; `sā +
āsrava-` yields `sāsrava-` in continuous writing.
The last sandhi does not classify this cultivation
as contaminated.

## 4. Grammar

Three cultivation bases are stated with distinct purposes; the last relative clause identifies a samādhi in the fourth dhyāna. The Bhāṣya supplies the divine-eye and qualities heads and forces the final sandhi break at feminine `sā`.

```nltk-fcfg
% start S
# tokens: ∅-divyacakṣurabhijñā darśanāya akṣyabhijñeṣṭā ∅-sarve-guṇāḥ prayogajāḥ dhībhedāya yaḥ ∅-samādhiḥ vajropamaḥ antye dhyāne sā āsravakṣayabhāvanā
S -> CL[K=vision] CL[K=qualities] CL[K=vajra]
CL[K=vision] -> N[CASE=nom,NUM=sg,GEN=f,SUPPLIED=prose] N[CASE=dat,NUM=sg,GEN=n,PURPOSE=seeing] N[CASE=nom,NUM=sg,GEN=f,DESIG=yes]
CL[K=qualities] -> N[CASE=nom,NUM=pl,GEN=m,SUPPLIED=prose] ADJ[CASE=nom,NUM=pl,GEN=m,ORIGIN=application] N[CASE=dat,NUM=sg,GEN=m,PURPOSE=discernment]
CL[K=vajra] -> PRON[CASE=nom,NUM=sg,GEN=m,REL=yes] N[CASE=nom,NUM=sg,GEN=m,SUPPLIED=prose] ADJ[CASE=nom,NUM=sg,GEN=m] ADJ[CASE=loc,NUM=sg,GEN=n,FINAL=yes] N[CASE=loc,NUM=sg,GEN=n] PRON[CASE=nom,NUM=sg,GEN=f,RESUME=yes] N[CASE=nom,NUM=sg,GEN=f]
N[CASE=nom,NUM=sg,GEN=f,SUPPLIED=prose] -> '∅-divyacakṣurabhijñā'
N[CASE=dat,NUM=sg,GEN=n,PURPOSE=seeing] -> 'darśanāya'
N[CASE=nom,NUM=sg,GEN=f,DESIG=yes] -> 'akṣyabhijñeṣṭā'
N[CASE=nom,NUM=pl,GEN=m,SUPPLIED=prose] -> '∅-sarve-guṇāḥ'
ADJ[CASE=nom,NUM=pl,GEN=m,ORIGIN=application] -> 'prayogajāḥ'
N[CASE=dat,NUM=sg,GEN=m,PURPOSE=discernment] -> 'dhībhedāya'
PRON[CASE=nom,NUM=sg,GEN=m,REL=yes] -> 'yaḥ'
N[CASE=nom,NUM=sg,GEN=m,SUPPLIED=prose] -> '∅-samādhiḥ'
ADJ[CASE=nom,NUM=sg,GEN=m] -> 'vajropamaḥ'
ADJ[CASE=loc,NUM=sg,GEN=n,FINAL=yes] -> 'antye'
N[CASE=loc,NUM=sg,GEN=n] -> 'dhyāne'
PRON[CASE=nom,NUM=sg,GEN=f,RESUME=yes] -> 'sā'
N[CASE=nom,NUM=sg,GEN=f] -> 'āsravakṣayabhāvanā'
```

```nltk-dep
'akṣyabhijñeṣṭā' -> '∅-divyacakṣurabhijñā' | 'darśanāya'
'prayogajāḥ' -> '∅-sarve-guṇāḥ' | 'dhībhedāya'
'∅-samādhiḥ' -> 'yaḥ' | 'vajropamaḥ' | 'antye' | 'dhyāne'
'āsravakṣayabhāvanā' -> 'sā'
```

`Antye` is the fourth dhyāna, not bhavāgra; prayogajāḥ covers all application-born
qualities. The prose parses the final phrase as `sā āsravakṣayabhāvanā`, not as a
cultivation classified sāsrava.


**Close construe.** Divine-eye superknowledge is intended
for knowledge-and-seeing; application-born qualities for
differentiation of prajñā. The vajra-like samādhi
in fourth dhyāna is cultivation for destruction
of the outflows.

## 5. Translation

### Literal Translation

> For seeing, the superknowledge of the eye is
> intended; for differentiation of understanding, those
> born of application. The vajra-like [samādhi]
> in the last dhyāna is cultivation for destruction
> of the outflows.

### Bhāṣya-informed study translation

> Cultivation of samādhi is intended in the divine-eye superknowledge, for
> knowledge-and-seeing, and in the qualities born of application, for the
> differentiation of understanding. The vajra-like samādhi in the last,
> fourth dhyāna is the cultivation for destruction of the outflows.

## 6. Philosophical Translation

> The four cultivations are distinguished by purpose:
> present pleasant abiding, knowledge-and-seeing, differentiation
> of prajñā, and destruction of the outflows.
> The third has a broad basis in application-born
> qualities; the fourth names a specific vajra-like
> samādhi. The text then moves from samādhis to
> the qualities supported by them.

The four purposes do not themselves establish four
mandatory consecutive steps. In particular, the verse
does not state that divine-eye superknowledge is
an obligatory predecessor of liberation for every practitioner.

## 7. Technical Vocabulary

**`Akṣyabhijñā / divyacakṣurabhijñā`.** Eye-superknowledge /
divine-eye superknowledge. The prose supplies the
full technical designation. Ordinary visual perception
is not the operative basis named here.

**`Jñānadarśana`.** Knowledge-and-seeing, the commentary's
expansion of darśana. Its pairing must remain
visible rather than being reduced to generic vision.

**`Dhībheda / prajñāprabheda`.** Differentiation of
understanding / differentiation of prajñā. The latter
is the explicit prose gloss and controls the
technical study translation.

**`Prayogaja guṇa`.** Quality born from application.
The source says all such qualities, including
those belonging to the three domains and those
that are uncontaminated. This is not a claim
that all application-born qualities are simultaneously
worldly and uncontaminated.

**`Vajropama samādhi`.** Vajra-like samādhi. The
present formulation identifies it in fourth dhyāna
with cultivation for outflow destruction. Its name
is retained as the established Path term rather
than replaced with a new physical or metaphysical mechanism.

**`Ātmopanāyikī … dharmadeśanā`.** Teaching related
to the Buddha's own case. Kila marks the remark
as reported. This contextual explanation should not
be omitted when assessing the specificity of the
fourth-dhyāna designation.

**`Samādhisaṃniśrita guṇa`.** Quality dependent upon
samādhi. This phrase announces the next section;
it does not terminate Chapter 8.

## 8. Logical Determination

The verse completes the fourfold cultivation list with three further purposes and their bases: knowledge-and-seeing, prajñā-differentiation, and outflow-destruction. The Bhāṣya resolves divine-eye superknowledge, all application-born qualities, and vajra-like samādhi in fourth dhyāna; its final sandhi is `sā āsravakṣayabhāvanā`. `[verse]` / `[prose]`.

**Signature.** `Purpose(p)`; `Basis(b)`; `Serves(b,p)`; `ApplicationBorn(b)`; `FourthDhyana(b)`.

```nltk-valuation
firstDhyana => firstDhyana
divineEyeSuperknowledge => divineEyeSuperknowledge
applicationBornQualities => applicationBornQualities
vajraSamadhiFourth => vajraSamadhiFourth
presentAbiding => presentAbiding
knowledgeSeeing => knowledgeSeeing
prajnaDifferentiation => prajnaDifferentiation
outflowDestruction => outflowDestruction
Purpose => {presentAbiding, knowledgeSeeing, prajnaDifferentiation, outflowDestruction}
Basis => {firstDhyana, divineEyeSuperknowledge, applicationBornQualities, vajraSamadhiFourth}
Serves => {(firstDhyana,presentAbiding),(divineEyeSuperknowledge,knowledgeSeeing),(applicationBornQualities,prajnaDifferentiation),(vajraSamadhiFourth,outflowDestruction)}
ApplicationBorn => {applicationBornQualities}
FourthDhyana => {vajraSamadhiFourth}
```

```nltk-fol
# THEORY shared
# [verse 8.27, prose] first wholesome dhyāna is for present-life pleasant abiding
Serves(firstDhyana,presentAbiding)
# [prose] darśana = knowledge-and-seeing; divine-eye superknowledge is its basis
Serves(divineEyeSuperknowledge,knowledgeSeeing)
# [verse, prose] all application-born qualities serve prajñā-differentiation
Serves(applicationBornQualities,prajnaDifferentiation)
ApplicationBorn(applicationBornQualities)
# [verse, prose] vajra-like samādhi in fourth dhyāna serves outflow-destruction
Serves(vajraSamadhiFourth,outflowDestruction)
FourthDhyana(vajraSamadhiFourth)
```

**Results (NLTK).** `check_logic.py` reports `shared: T` against the finite valuation.

**Scope cautions.** The purposes are not encoded as a mandatory sequence. “All” application-born qualities is broader than one named analytic attainment. The text identifies a fourth-dhyāna vajra-like samādhi but does not make this verse a universal exclusion of other grounds for outflow-destruction.

## 9. Interpretive Note

**A significant segmentation correction.** The research
padaccheda gives sa-āsrava-kṣaya-bhāvanā. The running
prose instead clearly gives the relative-correlative
construction and the purpose āsravakṣayāya. The
official segmentation retains the demonstrative separately;
the continuous Sanskrit remains unchanged.

**Witness cautions.** The explanatory phrase following
the reported self-reference is retained as an unresolved
compressed reading. The main identifications are
explicit in the preceding prose. No uncertain
wording is used to create a restriction stronger
than the stated account, and originals remain untouched.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
The project's Recognition vocabulary can articulate
the distinct purposes of cultivation. Yoga Vidyā
specifies those purposes and their operative bases;
Yoga Technē, its kriyā–karma companion, concerns
the application and cultivation through which the
named functions are exercised.

The research's movement from abiding through disclosure
and differentiation to conclusive liberation remains
a proposed project interpretation. The Kośa passage
gives four functional identifications, not an explicit
universal itinerary or an equation of vajra-like
samādhi with the Organon determinate Concept. Keeping
those registers distinct preserves both the source
and the comparative work.

**Review status.** Provisional, Bhāṣya-controlled study.
The knowledge-and-seeing gloss, broad application-born
scope, prajñā determination, fourth-dhyāna identification,
final-clause segmentation, reported self-reference, and
section transition have been checked against the
local research and running source.

## 10. OWL++ Seed

```text
Class: SamadhiCultivation
Class: CultivationPurpose
Class: ApplicationBornQuality
Class: SamadhiDependentQuality

ObjectProperty: cultivatedFor
ObjectProperty: hasSpecifiedBasis
ObjectProperty: interpretedWithinReportedContext

KnowledgeAndSeeingCultivation:
    basis: DivineEyeSuperknowledge
    purpose: JnanaDarsana

PrajnaDifferentiationCultivation:
    basis: AllApplicationBornQualities
    scope: ThreeDomainsAndUncontaminated
    purpose: PrajnaPrabheda

OutflowDestructionCultivation:
    specifiedBasis: VajraLikeSamadhiInFourthDhyana
    purpose: AsravaKsaya
    reportedContext: TeachingRelatedToBuddhasOwnCase

ProjectConstraint: The final clause begins with a demonstrative, not sa-asrava.
ProjectConstraint: Antya dhyana here means fourth dhyana, not bhavagra.
ProjectConstraint: Preserve all application-born qualities in the third member.
ProjectConstraint: Four purposes do not establish a mandatory four-step sequence.
ProjectConstraint: Do not infer divine-eye superknowledge is required for all liberation.
ProjectConstraint: Keep the reported context distinct from a universal restriction.
ProjectConstraint: The chapter continues with samadhi-dependent qualities.
```

This is a declarative project seed, not executable OWL.
VAK 8.29 next introduces the four immeasurables.
