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
| `sāsravādharagocarāḥ` | nominative plural compound adjective | ranging over lower-ground contaminated Things |
| `anāsraveṇa` | instrumental singular neuter | by uncontaminated attainment |
| `hīyante` | third-person plural passive of √hā | are abandoned |
| `kleśāḥ` | nominative plural masculine | defilements |
| `sāmantakena` | instrumental singular neuter | by the neighboring or access attainment |
| `ca` | conjunction | and; also |

`Kuśala + ārūpya` yields `kuśalārūpya`;
`sāsrava + adhara` yields `sāsravādhara`.
The prose resolves the range compound as
`adhobhūmikaṃ sāsravaṃ vastu`: a contaminated Thing
belonging to a lower ground.

## 4. Grammar

Negation restricts the range claim to principal wholesome formless attainments; the prose explains it through Support. A distinct passive clause states what abandons defilements.

```nltk-fcfg
% start S
# tokens: na maulāḥ kuśalārūpyāḥ sāsravādharagocarāḥ anāsraveṇa hīyante kleśāḥ sāmantakena ca ∅-śuddhakenāpi
S[SEM=?sem] -> CL[K=support_restriction,SEM=?sem] CL[K=abandonment]
CL[K=support_restriction,SEM=<?neg(?principal(?base))(?range)>] -> NEG[SEM=?neg] ADJ[CASE=nom,NUM=?n,GEN=?g,STATUS=principal,SEM=?principal] N[CASE=nom,NUM=?n,GEN=?g,QUALITY=wholesome,SEM=?base] ADJ[CASE=nom,NUM=?n,GEN=?g,RANGE=lower_contaminated,SEM=?range]
CL[K=abandonment] -> INSTR[CASE=ins,MODE=uncontaminated] V[PERS=3,NUM=pl,TENSE=pres,VOICE=passive] N[CASE=nom,NUM=pl,GEN=m,ROLE=agent] INSTR[CASE=ins,ROLE=access] CONJ COV[CASE=ins,MODE=pure,SUPPLIED=prose]
NEG[SEM=<\P.\Q.all a.all x.((P(a) & Q(x)) -> -TakesAsSupport(a,x))>] -> 'na'
ADJ[CASE=nom,NUM=pl,GEN=m,STATUS=principal,SEM=<\P.P>] -> 'maulāḥ'
N[CASE=nom,NUM=pl,GEN=m,QUALITY=wholesome,SEM=<\a.PrincipalWholesomeArupya(a)>] -> 'kuśalārūpyāḥ'
ADJ[CASE=nom,NUM=pl,GEN=m,RANGE=lower_contaminated,SEM=<\x.LowerContaminated(x)>] -> 'sāsravādharagocarāḥ'
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

Taking a Support is not abandonment: access can abandon lower-ground defilements even when
pure, while principal pure attainment is not thereby an antidote. The prose extends the
second half to dhyāna as well.

**Close construe.** Principal wholesome formless attainments
do not range over contaminated Things of a lower ground. Defilements are abandoned by uncontaminated
attainment and also by access attainment, which can
perform this work even when pure.

## 5. Translation

### Literal Translation

> The principal wholesome formless attainments do not
> range over contaminated Things of a lower ground.
> Defilements are abandoned by uncontaminated attainment
> and also by the neighboring attainment.

### Bhāṣya-informed study translation

> The principal wholesome formless attainments do not range
> over contaminated Things of a lower ground. Defilements are
> abandoned by uncontaminated attainment and also by access attainment,
> even when it is pure.

## 6. Philosophical Translation

> Purity alone does not determine an attainment's
> work. Principal attainment and access attainment
> differ in their relation to the lower level:
> the access path can take that ground as Support
> and act against its defilements. Its ability to
> abandon is explained through this antidotal relation,
> not merely through the adjective “pure.”

The passage distinguishes modes and functions. It
does not prescribe a universal sequence in which
access always starts an abandonment that an uncontaminated
principal attainment must then finish.

## 7. Technical Vocabulary

**Source.** Complete [447|08]–[447|17] unit checked against
`kosabhasya.txt`; [447|07] closes 8.20 and [447|18] opens 8.22. The Bhāṣya adds that the principal formless
attainments take their own or higher level as contaminated range;
uncontaminated Supports are admitted with qualification (the anvayajñāna
side, not the dharmajñāna side nor lower-ground cessation), whereas the
uninterrupted Paths of access take the lower ground as Support. Among the
principal attainments only the uncontaminated abandons defilements; access
abandons lower-level defilements even when pure, as antidote to that
lower level. The knowledge-side qualification is compressed in the prose.

**`Maula`.** Principal or fundamental attainment. It
is contrasted with the neighboring access stage.
The contrast qualifies both the Support analysis and
the interpretation of the abandonment discussion.

**`Kuśala`.** Wholesome. As in the preceding study,
pure and uncontaminated remain distinct within the
wholesome class. The existence of both modes is
subject to the already established summit restriction.

**`Gocara / ālambana`.** Range / Support.
The verse's *gocara* is explained through *ālambana*
in prose. The latter names what is taken as Support,
while *āśraya* in 8.19 names the being as Basis.

**`Sāmantaka`.** Neighboring or access attainment. Its
antidotal function toward the lower level explains
why a pure access attainment can abandon defilements
where a principal pure attainment cannot.

**`Ānantaryamārga`.** Uninterrupted path, the path directly
effecting abandonment. The lower-ground Support statement
specifically names these paths in access attainment;
it should not be extended without qualification to
every moment associated with an access stage.

**`Pratipakṣa`.** Antidote or counteragent. The expression
adhobhūmipratipakṣatva states the relational ground of
the access attainment's efficacy.

**`Anvayajñānapakṣya / dharmajñānapakṣa`.** Belonging
to the anvayajñāna side / the dharmajñāna side.
These inherited knowledge distinctions qualify the
uncontaminated Support range. The present passage does
not replace them with a generic distinction between
all mental and all sensory Things.

## 8. Logical Determination

The first clause restricts the principal attainment’s Support range; the second identifies two antidotal routes to abandonment, including pure access against lower-ground defilements. Taking a Support and abandoning defilements are distinct relations. Provenance: `[verse]`, `[prose]`.

**Signature.** `PrincipalWholesomeArupya/1(a)`—principal wholesome formless attainment; `LowerContaminated/1(x)`—x is a lower-ground contaminated Thing; `TakesAsSupport/2(a,x)`—a takes x as Support; `Uncontaminated/1(a)`—uncontaminated attainment; `Defilement/1(d)`—defilement; `Abandons/2(a,d)`—a abandons d; `PureAccess/1(a)`—pure access attainment; `LowerDefilement/1(d)`—lower-level defilement; `AntidoteTo/2(a,d)`—a is d’s antidote.

```nltk-sem
# derived by the section 4 parse, not typed by hand
all a.all x.((PrincipalWholesomeArupya(a) & LowerContaminated(x)) -> -TakesAsSupport(a,x))
```

```nltk-fol
# THEORY shared
# [verse, prose] principal wholesome formless attainments exclude lower contaminated Supports
all a.all x.((PrincipalWholesomeArupya(a) & LowerContaminated(x)) -> -TakesAsSupport(a,x))
# [verse] uncontaminated attainment abandons defilements it counteracts
all a.all d.((Uncontaminated(a) & Defilement(d) & AntidoteTo(a,d)) -> Abandons(a,d))
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
TakesAsSupport => {}
Uncontaminated => {nobleDhyana}
Defilement => {lowerStain}
Abandons => {(nobleDhyana,lowerStain),(pureAccess,lowerStain)}
PureAccess => {pureAccess}
LowerDefilement => {lowerStain}
AntidoteTo => {(nobleDhyana,lowerStain),(pureAccess,lowerStain)}
```

**Results (NLTK).** `Model.satisfy` checks the exclusions and the two abandonment rules. The pure-access case works through the explicit lower-level antidote relation.

**Scope cautions.** The prose extends the second clause to dhyāna access as well as formless access. `Anvayajñāna` qualifies which uncontaminated Supports are admitted; that fine-grained qualification and uninterrupted-Path timing are not formalized here. Pure principal attainment does not abandon defilements in this account. The negative range claim concerns lower contaminated Things, not every possible lower-ground Support.

## 9. Interpretive Note

**Qualifications carry the argument.** Removing maula
would wrongly extend the Support prohibition to access
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
Support, and target ground. Yoga Technē, its kriyā–karma
companion, concerns the effective antidotal operation.
Here the shared designation “pure” permits different
functions because principal and access attainments
stand differently toward the lower level.

For Organon representation, keep Support eligibility
and abandonment efficacy as separate relations, joined
by the stated antidotal explanation where appropriate.
Do not infer efficacy from purity alone or convert
all access activity into one uniform path event.
This is project reconstruction, not additional doctrine
attributed to Vasubandhu.

**Review status.** Complete [447|08]–[447|17] natural unit collated
with `kosabhasya.txt`; [447|07] closes 8.20 and [447|18] opens 8.22.
The threefold-attainment transition and split verse are restored in the
Bhāṣya study. The compressed *anvayajñāna* clause remains grammatically
uncertain; the witness is preserved without reconstructing its endings.

## 10. OWL++ Seed

```text
Class: PrincipalWholesomeFormlessAttainment
Class: PrincipalPureAttainment
Class: PrincipalUncontaminatedAttainment
Class: AccessAttainment
Class: AccessUninterruptedPath
Class: AntidotalRelation

ObjectProperty: hasEligibleSupportRange
ObjectProperty: excludesSupportCategory
ObjectProperty: actsAsAntidoteTo
ObjectProperty: abandonsDefilementsOf

PrincipalWholesomeFormlessAttainment:
    excludesSupports: LowerGroundContaminatedThings,
                     DharmaJnanaSide, LowerLevelCessation
    qualifiedUncontaminatedSupportRange: AnvayaJnanaSide

AccessUninterruptedPath:
    supportGround: LowerGround

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
ProjectConstraint: Support selection alone does not establish antidotal efficacy.
ProjectConstraint: Access Support claim specifically names uninterrupted Paths.
ProjectConstraint: Do not impose a universal access-to-uncontaminated itinerary.
ProjectConstraint: Formless Support range differs from the wholesome-dhyana range.
```

This is a declarative project seed, not executable OWL.
VAK 8.22 next counts the access attainments and
determines their modes and associated feeling.
