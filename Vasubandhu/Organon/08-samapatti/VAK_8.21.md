# VAK_8.21 — Principal Attainment, Access, and Abandonment

## 1. Sanskrit (Devanāgarī)

```sanskrit
न मौलाः कुशलारूप्याः सास्रवाधरगोचराः ।
अनास्रवेण हीयन्ते क्लेशाः सामन्तकेन च ॥ ८.२१ ॥
```

## 2. Sanskrit (IAST)

```text
na maulāḥ kuśalārūpyāḥ sāsravādharagocarāḥ |
anāsraveṇa hīyante kleśāḥ sāmantakena ca || 8.21 ||
```

The Sanskrit follows the local kārikā witness. The
running source quotes `samantakena` in the final clause,
while its explanatory prose uses `sāmantakena`; the
local verse's long vowel is retained.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `na` | negation | not |
| `maulāḥ` | nominative plural adjective | principal, as distinct from access attainments |
| `kuśalārūpyāḥ` | nominative plural compound designation | wholesome formless attainments |
| `sāsravādharagocarāḥ` | nominative plural compound adjective | having lower-level contaminated objects as their range |
| `anāsraveṇa` | instrumental singular neuter | by uncontaminated attainment |
| `hīyante` | third-person plural passive of √hā | are abandoned |
| `kleśāḥ` | nominative plural masculine | defilements |
| `sāmantakena` | instrumental singular neuter | by the neighboring or access attainment |
| `ca` | conjunction | and; also |

`Kuśala + ārūpya` yields `kuśalārūpya`;
`sāsrava + adhara` yields `sāsravādhara`.
The prose resolves the object compound as
`adhobhūmikaṃ sāsravaṃ vastu`: a contaminated object
belonging to a lower level.

## 4. Grammar

Negation restricts the object-range claim to principal wholesome formless attainments; a distinct passive clause states what abandons defilements.

```nltk-fcfg
% start S
# tokens: na maulāḥ kuśalārūpyāḥ sāsravādharagocarāḥ anāsraveṇa hīyante kleśāḥ sāmantakena ca ∅-śuddhakenāpi
S -> CL[K=object_restriction] CL[K=abandonment]
CL[K=object_restriction] -> NEG ADJ[CASE=nom,NUM=?n,GEN=?g,STATUS=principal] N[CASE=nom,NUM=?n,GEN=?g,QUALITY=wholesome] ADJ[CASE=nom,NUM=?n,GEN=?g,RANGE=lower_contaminated]
CL[K=abandonment] -> INSTR[CASE=ins,MODE=uncontaminated] V[PERS=3,NUM=pl,TENSE=pres,VOICE=passive] N[CASE=nom,NUM=pl,GEN=m,ROLE=agent] INSTR[CASE=ins,ROLE=access] CONJ COV[CASE=ins,MODE=pure,SUPPLIED=prose]
NEG -> 'na'
ADJ[CASE=nom,NUM=pl,GEN=m,STATUS=principal] -> 'maulāḥ'
N[CASE=nom,NUM=pl,GEN=m,QUALITY=wholesome] -> 'kuśalārūpyāḥ'
ADJ[CASE=nom,NUM=pl,GEN=m,RANGE=lower_contaminated] -> 'sāsravādharagocarāḥ'
INSTR[CASE=ins,MODE=uncontaminated] -> 'anāsraveṇa'
V[PERS=3,NUM=pl,TENSE=pres,VOICE=passive] -> 'hīyante'
N[CASE=nom,NUM=pl,GEN=m,ROLE=agent] -> 'kleśāḥ'
INSTR[CASE=ins,ROLE=access] -> 'sāmantakena'
CONJ -> 'ca'
COV[CASE=ins,MODE=pure,SUPPLIED=prose] -> '∅-śuddhakenāpi'
```

```nltk-dep
'kuśalārūpyāḥ' -> 'na' | 'maulāḥ' | 'sāsravādharagocarāḥ'
'hīyante' -> 'kleśāḥ' | 'anāsraveṇa' | 'sāmantakena' | 'ca' | '∅-śuddhakenāpi'
```

Object-taking is not abandonment: access can abandon lower-level defilements even when
pure, while principal pure attainment is not thereby an antidote. The prose extends the
second half to dhyāna as well.

**Close construe.** Principal wholesome formless attainments
do not have contaminated lower-level objects as their
range. Defilements are abandoned by uncontaminated
attainment and also by access attainment, which can
perform this work even when pure.

## 5. Translation

### Literal Translation

> The principal wholesome formless attainments do not
> take contaminated lower-level objects as their range.
> Defilements are abandoned by uncontaminated attainment
> and also by the neighboring attainment.

### Bhāṣya-informed study translation

> The principal wholesome formless attainments do not take
> contaminated lower-level objects as their range. Defilements are
> abandoned by uncontaminated attainment and also by access attainment,
> even when it is pure.

## 6. Philosophical Translation

> Purity alone does not determine an attainment's
> work. Principal attainment and access attainment
> differ in their relation to the lower level:
> the access path can take that level as object
> and act against its defilements. Its ability to
> abandon is explained through this antidotal relation,
> not merely through the adjective “pure.”

The passage distinguishes modes and functions. It
does not prescribe a universal sequence in which
access always starts an abandonment that an uncontaminated
principal attainment must then finish.

## 7. Technical Vocabulary

**Source.** Pradhan 447|08–447|17, checked against the local Bhāṣya
study and running source. The Bhāṣya adds that the principal formless
attainments take their own or higher level as contaminated range;
uncontaminated objects are admitted with qualification (the anvayajñāna
side, not the dharmajñāna side nor lower-level cessation), whereas the
uninterrupted paths of access take the lower level as object. Among the
principal attainments only the uncontaminated abandons defilements; access
abandons lower-level defilements even when pure, as antidote to that
lower level. The knowledge-side qualification is compressed in the prose.

**`Maula`.** Principal or fundamental attainment. It
is contrasted with the neighboring access stage.
The contrast qualifies both the object analysis and
the interpretation of the abandonment discussion.

**`Kuśala`.** Wholesome. As in the preceding study,
pure and uncontaminated remain distinct within the
wholesome class. The existence of both modes is
subject to the already established summit restriction.

**`Gocara / ālambana`.** Object-range / object-support.
The verse's gocara is explained through ālambana
in prose. Their use here concerns what is taken
as object, not the rebirth-support of VAK 8.19–8.20.

**`Sāmantaka`.** Neighboring or access attainment. Its
antidotal function toward the lower level explains
why a pure access attainment can abandon defilements
where a principal pure attainment cannot.

**`Ānantaryamārga`.** Uninterrupted path, the path directly
effecting abandonment. The lower-level object statement
specifically names these paths in access attainment;
it should not be extended without qualification to
every moment associated with an access stage.

**`Pratipakṣa`.** Antidote or counteragent. The expression
adhobhūmipratipakṣatva states the relational ground of
the access attainment's efficacy.

**`Anvayajñānapakṣya / dharmajñānapakṣa`.** Belonging
to the anvayajñāna side / the dharmajñāna side.
These inherited knowledge distinctions qualify the
uncontaminated object range. The present passage does
not replace them with a generic distinction between
all mental and all sensory objects.

## 8. Logical Determination

The first clause restricts object-range; the second identifies two antidotal routes to abandonment, including pure access against lower-level defilements. Object-taking and abandonment are not the same relation. Provenance: `[verse]`, `[prose]`.

**Signature.** `PrincipalWholesomeArupya/1(a)`—principal wholesome formless attainment; `LowerContaminated/1(x)`—lower-level contaminated object; `TakesAsObject/2(a,x)`—a takes x as object; `Uncontaminated/1(a)`—uncontaminated attainment; `Defilement/1(d)`—defilement; `Abandons/2(a,d)`—a abandons d; `PureAccess/1(a)`—pure access attainment; `LowerDefilement/1(d)`—lower-level defilement; `AntidoteTo/2(a,d)`—a is d’s antidote.

```nltk-fol
# THEORY shared
# [verse] principal wholesome formless attainments exclude lower contaminated objects
all a.all x.((PrincipalWholesomeArupya(a) & LowerContaminated(x)) -> -TakesAsObject(a,x))
# [verse] defilements are abandoned by uncontaminated attainment
all a.all d.((Uncontaminated(a) & Defilement(d)) -> Abandons(a,d))
# [verse, prose] access, even when pure, abandons the lower level as its antidote
all a.all d.((PureAccess(a) & LowerDefilement(d) & AntidoteTo(a,d)) -> Abandons(a,d))
```

**Finite valuation.** The example distinguishes a principal wholesome formless attainment from a pure access attainment.

```nltk-valuation
principalSpace => principalSpace
lowerObject => lowerObject
nobleDhyana => nobleDhyana
pureAccess => pureAccess
lowerStain => lowerStain
PrincipalWholesomeArupya => {principalSpace}
LowerContaminated => {lowerObject}
TakesAsObject => {}
Uncontaminated => {nobleDhyana}
Defilement => {lowerStain}
Abandons => {(nobleDhyana,lowerStain),(pureAccess,lowerStain)}
PureAccess => {pureAccess}
LowerDefilement => {lowerStain}
AntidoteTo => {(pureAccess,lowerStain)}
```

**Results (NLTK).** `Model.satisfy` checks the exclusions and the two abandonment rules. The pure-access case works through the explicit lower-level antidote relation.

**Scope cautions.** The prose extends the second clause to dhyāna access as well as formless access. `Anvayajñāna` qualifies which uncontaminated objects are admitted; that fine-grained qualification and uninterrupted-path timing are not formalized here. Pure principal attainment is not asserted to abandon defilements. The negative object claim concerns lower contaminated objects, not every object associated with a lower level.

## 9. Interpretive Note

**Qualifications carry the argument.** Removing maula
would wrongly extend the object prohibition to access
paths. Removing śuddhakenāpi would hide the fact
that contaminated wholesome access can perform abandonment.
Removing the lower-level target would turn a specific
antidotal role into an unrestricted power.

**Witness cautions.** The running prose's
`sarvānvayajñānapakṣyo na dharmajñānapakṣo` is grammatically
compressed beside the preceding anāsravaṃ. The study
preserves the contextual knowledge-side distinction
without claiming to reconstruct every ending. Its
`samantakena` verse reading and subsequent `sāmantakena`
prose reading are disclosed above. Research and source
files remain unchanged.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates mode, principal/access status,
object, and target level. Yoga Technē, its kriyā–karma
companion, concerns the effective antidotal operation.
Here the shared designation “pure” permits different
functions because principal and access attainments
stand differently toward the lower level.

For Organon representation, keep object eligibility
and abandonment efficacy as separate relations, joined
by the stated antidotal explanation where appropriate.
Do not infer efficacy from purity alone or convert
all access activity into one uniform path event.
This is project reconstruction, not additional doctrine
attributed to Vasubandhu.

**Review status.** Provisional, Bhāṣya-controlled study.
The principal/access distinction, qualified formless
object-range, access uninterrupted-path object, three
reasons concerning principal purity, and pure access
antidotal role have been checked against the local
research and running source.

## 10. OWL++ Seed

```text
Class: PrincipalWholesomeFormlessAttainment
Class: PrincipalPureAttainment
Class: PrincipalUncontaminatedAttainment
Class: AccessAttainment
Class: AccessUninterruptedPath
Class: AntidotalRelation

ObjectProperty: hasPermittedObjectRange
ObjectProperty: excludesObjectCategory
ObjectProperty: actsAsAntidoteTo
ObjectProperty: abandonsDefilementsOf

PrincipalWholesomeFormlessAttainment:
    excludesObjects: LowerLevelContaminatedObjects,
                     DharmaJnanaSide, LowerLevelCessation
    qualifiedUncontaminatedRange: AnvayaJnanaSide

AccessUninterruptedPath:
    objectLevel: LowerLevel

PrincipalPureAttainment:
    abandonmentEfficacy: NotAssertedByPurity
    sourceDetermination: DoesNotAbandonDefilements

PrincipalUncontaminatedAttainment:
    sourceDetermination: AbandonsDefilements

PureAccessAttainment:
    antidoteTarget: LowerLevel
    abandonsDefilementsOf: LowerLevel

ProjectConstraint: Preserve principal versus access scope.
ProjectConstraint: Pure is not equivalent to uncontaminated.
ProjectConstraint: Object selection alone does not establish antidotal efficacy.
ProjectConstraint: Access object claim specifically names uninterrupted paths.
ProjectConstraint: Do not impose a universal access-to-uncontaminated itinerary.
ProjectConstraint: Formless object range is not unrestricted wholesome-dhyana range.
```

This is a declarative project seed, not executable OWL.
VAK 8.22 next counts the access attainments and
determines their modes and associated feeling.
