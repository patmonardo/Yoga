# VAK_8.20 — The Summit Exception and Attainment Support Range

## 1. Sanskrit (Devanāgarī)

```sanskrit
आर्याकिञ्चन्यसांमुख्याद् भवाग्रे त्वास्रवक्षयः ।
सतृष्णाः स्वभवालम्बाः ध्यानं सद्विषयं शुभम् ॥ ८.२० ॥
```

## 2. Sanskrit (IAST)

```text
āryākiñcanyasāṃmukhyād bhavāgre tv āsravakṣayaḥ |
satṛṣṇāḥ svabhavālambāḥ dhyānaṃ sadviṣayaṃ śubham || 8.20 ||
```

The official verse follows the running source's
`sadviṣayam`, not the research kārikā's emendation
`ṣaḍviṣayam`. Its Bhāṣya study explicitly withdraws
the six-object interpretation. Devanāgarī सद्विषयं
renders the adopted reading. The running source's
ākiñcanya and the research IAST ākiṃcanya differ in
nasal spelling; the former is used here.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `āryākiñcanyasāṃmukhyāt` | ablative singular compound | through making noble nothingness directly present |
| `bhavāgre` | locative singular neuter compound | at the summit of existence |
| `tu` | contrast particle | however; marks the exception |
| `āsravakṣayaḥ` | nominative singular masculine compound | destruction of the outflows |
| `satṛṣṇāḥ` | nominative plural adjective | accompanied by craving |
| `svabhavālambāḥ` | nominative plural compound adjective | taking existence of their own ground as Support |
| `dhyānam` | nominative singular neuter | dhyāna |
| `sadviṣayam` | nominative singular neuter compound adjective | having what exists as its Condition |
| `śubham` | nominative singular neuter adjective | wholesome |

`Sat + viṣaya` yields `sadviṣaya`; it is not
`ṣaṭ + viṣaya`, six objects. `Ārya + ākiñcanya`
yields `āryākiñcanya`; `sāṃmukhyāt + bhavāgre`
yields `sāṃmukhyād bhavāgre`; `tu + āsrava-`
yields `tv āsrava-`. The compound sva-bhava contains
bhava, existence, not svabhāva, intrinsic nature.

## 4. Grammar

The verse moves from the summit exception to two clauses about the range of attainment. The Bhāṣya explains *sadviṣaya* through possible Supports, not six sensory fields.

```nltk-fcfg
% start S
# tokens: āryākiñcanyasāṃmukhyād ∅-anāsravākiñcanyāyatana bhavāgre tv āsravakṣayaḥ satṛṣṇāḥ ∅-dhyānārūpyāḥ svabhavālambāḥ dhyānaṃ sadviṣayaṃ śubham
S[SEM=?sem] -> CL[K=summit_exception] CL[K=craving_range] CL[K=wholesome_dhyana,SEM=?sem]
CL[K=summit_exception] -> CAUSE[CASE=abl,MODE=noble] N[CASE=nom,NUM=sg,GEN=n,EXPANSION=yes,SUPPLIED=prose] LOC[CASE=loc,GROUND=summit] PTCL[CONTRAST=yes] N[CASE=nom,NUM=sg,GEN=m,EVENT=destruction]
CL[K=craving_range] -> ADJ[CASE=nom,NUM=?n,GEN=?g,QUALITY=craving] N[CASE=nom,NUM=?n,GEN=?g,SUPPLIED=prose] ADJ[CASE=nom,NUM=?n,GEN=?g,SUPPORT=own_level]
CL[K=wholesome_dhyana,SEM=<?r(?q(?n))>] -> N[CASE=nom,NUM=sg,GEN=n,KIND=dhyana,SEM=?n] ADJ[CASE=nom,NUM=sg,GEN=n,CONDITION=existent,SEM=?r] ADJ[CASE=nom,NUM=sg,GEN=n,QUALITY=wholesome,SEM=?q]
CAUSE[CASE=abl,MODE=noble] -> 'āryākiñcanyasāṃmukhyād'
N[CASE=nom,NUM=sg,GEN=n,EXPANSION=yes,SUPPLIED=prose] -> '∅-anāsravākiñcanyāyatana'
LOC[CASE=loc,GROUND=summit] -> 'bhavāgre'
PTCL[CONTRAST=yes] -> 'tv'
N[CASE=nom,NUM=sg,GEN=m,EVENT=destruction] -> 'āsravakṣayaḥ'
ADJ[CASE=nom,NUM=pl,GEN=m,QUALITY=craving] -> 'satṛṣṇāḥ'
N[CASE=nom,NUM=pl,GEN=m,SUPPLIED=prose] -> '∅-dhyānārūpyāḥ'
ADJ[CASE=nom,NUM=pl,GEN=m,SUPPORT=own_level] -> 'svabhavālambāḥ'
N[CASE=nom,NUM=sg,GEN=n,KIND=dhyana,SEM=<\a.Dhyana(a)>] -> 'dhyānaṃ'
ADJ[CASE=nom,NUM=sg,GEN=n,CONDITION=existent,SEM=<\P.all a.all x.((P(a) & Exists(x)) -> EligibleCondition(a,x))>] -> 'sadviṣayaṃ'
ADJ[CASE=nom,NUM=sg,GEN=n,QUALITY=wholesome,SEM=<\P.\a.(P(a) & Wholesome(a))>] -> 'śubham'
```

```nltk-dep
'āsravakṣayaḥ' -> 'āryākiñcanyasāṃmukhyād' | '∅-anāsravākiñcanyāyatana' | 'bhavāgre' | 'tu'
'∅-dhyānārūpyāḥ' -> 'satṛṣṇāḥ' | 'svabhavālambāḥ'
'dhyānaṃ' -> 'sadviṣayaṃ' | 'śubham'
```

The first clause is not a native uncontaminated summit attainment: rebirth at bhavāgra
and the cultivated lower nothingness resource matter. The broad Condition range belongs here
to wholesome dhyāna alone, not wholesome formless attainments.

**Close construe.** At the summit, however, destruction
of the outflows occurs through making noble nothingness
present. Craving-associated attainments take their own
ground's existence as Support. Wholesome dhyāna has
what exists as its Condition.

## 5. Translation

### Literal Translation

> At the summit of existence, however, destruction
> of the outflows occurs through the direct presence
> of noble nothingness. Those accompanied by craving
> take own-ground existence as Support. Wholesome
> dhyāna has what exists as its Condition.

### Bhāṣya-informed study translation

> At the summit of existence, however, the destruction of the outflows
> occurs through the direct presence of noble nothingness. Those
> accompanied by craving take own-ground existence as Support. Wholesome
> dhyāna has what exists as its Condition; conditioned and unconditioned
> Things are eligible Supports.

## 6. Philosophical Translation

> The higher rebirth Basis does not itself supply
> the required uncontaminated attainment. A previously
> cultivated lower attainment has a liberating purpose
> there, constituting the stated exception to the
> preceding general rule. The discussion then turns
> from the Basis of attainment to what it
> takes as Support, distinguishing craving-bound range
> from the broader range of wholesome dhyāna.

Basis, operative attainment, Condition, and Support are separate
relations. Their distinction is essential both to
the summit exception and to the new Support and Condition analysis.

## 7. Technical Vocabulary

**Source.** Pradhan 446|22–447|07, checked against the local Bhāṣya
study and running source. For one reborn at the summit, the nothingness
made present is an uncontaminated attainment, because the summit has no
uncontaminated attainment of its own and that attainment has been
cultivated. “Those accompanied by craving” are the savoring-associated
attainments; their Support is contaminated existence of their own ground,
not a lower, higher, or uncontaminated Support. “Whatever exists” states
the class-level range given by *sarvālambana* (conditioned or
unconditioned); it does not assert simultaneous apprehension of
everything.

**`Utsarga / apavāda`.** General rule / exception.
The prose explicitly uses this structure to connect
VAK 8.19 with the present first half. The exception
is not an editorial reconciliation imposed afterward.

**`Sāṃmukhya / saṃmukhībhāva`.** Direct presence or
making present. Here it concerns bringing an attainment
into operation, rather than merely remembering its name
or possessing it without entering it.

**`Abhyāsa`.** Cultivation or habituation. Prior cultivation
of the lower uncontaminated attainment forms part
of the explanation. The passage does not promise
outflow destruction to every being merely by rebirth
at the summit.

**`Āśraya / ālambana`.** Basis / Support.
The first concerns the being for
whom an attainment operates; the second concerns
what the attainment takes as Support. The Bhāṣya's
new question expressly moves to ālambana.

**`Satṛṣṇa / āsvādanāsaṃprayukta`.** Accompanied by
craving / associated with savoring. The prose identifies
the mode concerned. Its own-level restriction does
not assert that its Support must be the very same
mental event taking that Support.

**`Bhava`.** Existence, here explicitly glossed as
sāsrava-vastu, contaminated Thing. “Own
existence” must retain the level qualification supplied
by the prose; it is not automatically autobiographical
self-contemplation.

**`Sarvālambana`.** Taking all as Support. The
prose specifies whatever exists, conditioned or unconditioned.
This is the controlling explanation of sadviṣaya,
not a six-member sensory inventory.

## 8. Logical Determination

The verse states the summit exception, then moves from Basis to Support and Condition: craving-associated attainments take own-ground contaminated existence as Support; wholesome dhyāna has what exists as its Condition, with every conditioned or unconditioned Thing eligible as Support. Provenance: `[verse]`, `[prose]`.

**Signature.** `UpperBorn/1(p)`—p is reborn at bhavāgra; `MakesPresent/2(p,a)`—p brings a into operation; `NobleNothingness/1(a)`—noble nothingness attainment; `DestroysOutflows/1(p)`—outflows are destroyed for p; `CravingAssociated/1(a)`—a is savoring-associated; `OwnLevelExistenceSupport/1(a)`—a takes own-ground existence as Support; `WholesomeDhyana/1(a)`—wholesome dhyāna; `Dhyana/1(a)` and `Wholesome/1(a)`—the composed subject properties; `Exists/1(x)`—what exists; `Vastu/1(x)`—x is a Thing in the prose range; `EligibleCondition/2(a,x)`—x is in a’s possible Condition range; `MayTakeAsSupport/2(a,x)`—x is an eligible Support of a.

```nltk-sem
# derived by the section 4 parse, not typed by hand
all a.all x.((Dhyana(a) & Wholesome(a) & Exists(x)) -> EligibleCondition(a,x))
```

```nltk-fol
# THEORY shared
# [verse] derived Condition-range rule from the section 4 parse
all a.all x.((Dhyana(a) & Wholesome(a) & Exists(x)) -> EligibleCondition(a,x))
# [prose] exception at bhavāgra: cultivated noble nothingness is made present
all p.all a.((UpperBorn(p) & MakesPresent(p,a) & NobleNothingness(a)) -> DestroysOutflows(p))
# [verse, prose] satṛṣṇa attainments take own-ground contaminated existence as Support
all a.(CravingAssociated(a) -> OwnLevelExistenceSupport(a))
# [prose] sarvālambana: every conditioned or unconditioned Thing is an eligible Support
all a.all x.((WholesomeDhyana(a) & Vastu(x)) -> MayTakeAsSupport(a,x))
```

**Finite model.** `Vastu` is the class of Things eligible as Supports, not a claim of simultaneous apprehension.

```nltk-valuation
upperBorn => upperBorn
nobleNothingness => nobleNothingness
cravingAttainment => cravingAttainment
wholesomeDhyana => wholesomeDhyana
conditionedThing => conditionedThing
unconditionedThing => unconditionedThing
UpperBorn => {upperBorn}
MakesPresent => {(upperBorn,nobleNothingness)}
NobleNothingness => {nobleNothingness}
DestroysOutflows => {upperBorn}
CravingAssociated => {cravingAttainment}
OwnLevelExistenceSupport => {cravingAttainment}
WholesomeDhyana => {wholesomeDhyana}
Dhyana => {wholesomeDhyana}
Wholesome => {wholesomeDhyana}
Exists => {conditionedThing,unconditionedThing}
Vastu => {conditionedThing,unconditionedThing}
EligibleCondition => {(wholesomeDhyana,conditionedThing),(wholesomeDhyana,unconditionedThing)}
MayTakeAsSupport => {(wholesomeDhyana,conditionedThing),(wholesomeDhyana,unconditionedThing)}
```

**Results (NLTK).** The shared rules are checked against the finite model. The Condition and Support formulas state eligibility, not simultaneous apprehension.

**Scope cautions.** The noble nothingness is cultivated uncontaminated attainment made present at the summit, not a native uncontaminated summit attainment. `sadviṣayam` is retained; the withdrawn six-object reading is not encoded. Wholesome formless attainments are not included in this broad-range clause.

## 9. Interpretive Note

**Substantive correction of the earlier draft.** The
research kārikā emends sadviṣaya to ṣaḍviṣaya and
translates six object-fields. Its Bhāṣya study reverses
that interpretation. The running witness and the
explicit “whatever exists, conditioned or unconditioned”
gloss support retaining sadviṣaya. This official study
makes that choice visible; research witnesses remain intact.

**Avoid an unsupported reflexive interpretation.** The
research's language of self-enclosure can suggest that
the attainment necessarily contemplates itself. The
source instead gives a level-bounded contaminated
Support range. The relational restriction is sufficient
and should remain primary.

**Witness cautions.** The running source prints
`utsarga kṛtvā`, `tṛṣṇāparichinnatvāt`, and `śubhakamanāsravaṃ ca`.
These readings are not silently altered in the
witness. The explicit exception, repeated anāsrava
identification, and broad Support gloss make the main
argument clear despite the textual irregularities.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates Basis, operative resource,
result, Condition, and Support range. Yoga Technē, its kriyā–karma
companion, concerns bringing the cultivated attainment
into effective operation. At the summit, the lower
resource has a specific purpose that qualifies the
general Basis rule.

For Organon representation, preserve the exception's
conditions and keep Support eligibility distinct from
actual selection. A broad class-level range
is not a claim of universal knowledge in every
instance. This is project reconstruction, not a
further doctrine attributed to Vasubandhu.

**Review status.** Complete natural unit [446|22]–[447|07] collated
with `kosabhasya.txt`; [446|21] closes 8.19 and [447|08] opens 8.21.
The explicit summit-access question, contaminated-Thing gloss, and three
Support exclusions are restored in the paired Bhāṣya study. The local
`utsarga kṛtvā`, `tṛṣṇāparichinnatvāt`, and `śubhakamanāsravaṃ` remain
visible. The witness supports `sadviṣaya`, while the exact force of the
damaged prose spelling is not reconstructed.

## 10. OWL++ Seed

```text
Class: RebirthBasis
Class: OperativeAttainment
Class: AttainmentSupportRange
Class: GeneralRuleException

ObjectProperty: madePresentForBasis
ObjectProperty: hasPriorCultivation
ObjectProperty: hasEligibleSupportRange
ObjectProperty: supportsResult

SummitException:
    rebirthBasis: Bhavagra
    operativeAttainment: UncontaminatedNothingness
    result: OutflowDestruction
    explanation: NoNativeUncontaminatedAttainment, PriorCultivation

CravingAssociatedAttainment:
    eligibleSupports: OwnGroundContaminatedThings
    excludedSupports: LowerGround, HigherGround, Uncontaminated

WholesomeDhyana:
    modes: Pure, Uncontaminated
    classSupportRange: ConditionedAndUnconditionedThings
    sourceReading: Sadvisaya

ProjectConstraint: Preserve the summit case as an explicit Basis-rule exception.
ProjectConstraint: No uncontaminated bhavagra attainment is posited.
ProjectConstraint: Basis, Condition, and Support are distinct relations.
ProjectConstraint: Own-ground Supports do not imply mandatory self-reference.
ProjectConstraint: Sadvisaya is not a six-object count.
ProjectConstraint: Class Support range does not imply simultaneous omniscience.
ProjectConstraint: Formless Support restrictions continue in VAK 8.21.
```

This is a declarative project seed, not executable OWL.
VAK 8.21 next specifies formless Support restrictions
and which attainments abandon defilements.
