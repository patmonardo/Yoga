# VAK_8.33 — Cessation-Attainment: Entry and Emergence

## 1. Sanskrit (Devanāgarī)

```sanskrit
निरोधस्तु समापत्तिः सूक्ष्मसूक्ष्मादनन्तरम् ।
स्वशुद्धकाधरार्येण व्युत्थानं चेतसा ततः ॥ ८.३३ ॥
```

## 2. Sanskrit (IAST)

```text
nirodhas tu samāpattiḥ sūkṣmasūkṣmād anantaram |
svaśuddhakādharāryeṇa vyutthānaṃ cetasā tataḥ || 8.33 ||
```

The Sanskrit follows the local kārikā witness. A
material conflict occurs in the emergence explanation:
the verse specifies adhara-ārya, lower noble,
while the running prose prints sāsraveṇa for
that alternative. The official study retains the
verse's noble determination and marks the prose
conflict rather than silently changing either witness.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `nirodhaḥ` | nominative singular masculine | cessation, here the eighth release |
| `samāpattiḥ` | nominative singular feminine | attainment |
| `sūkṣmasūkṣmāt` | ablative singular compound | from the extremely subtle, made subtler still |
| `anantaram` | adverb | immediately afterward |
| `svaśuddhakādharāryeṇa` | instrumental singular compound qualifier of cetasā | with own-level pure or lower-level noble mind |
| `vyutthānam` | nominative singular neuter | emergence |
| `cetasā` | instrumental singular neuter of cetas | through mind |
| `tataḥ` | pronominal adverb | from that attainment |

`Nirodhaḥ + tu` yields `nirodhas tu`;
`sūkṣmasūkṣmāt + anantaram` yields
`sūkṣmasūkṣmād anantaram`; `śuddhaka + adhara`
yields `śuddhakādhara`; `adhara + ārya`
yields `adharārya`.

## 4. Grammar

The first nominal clause identifies the eighth release; the Bhāṣya supplies entry after a perception already made subtler. Emergence has one instrumental mind with two paired alternatives, own-level pure or lower-level noble; the verse/prose conflict is retained.

```nltk-fcfg
% start S
# tokens: nirodhaḥ tu samāpattiḥ sūkṣmasūkṣmāt anantaram ∅-nirodham ∅-samāpadyante vyutthānam cetasā svaśuddhakādharāryeṇa tataḥ
S[SEM=?formula] -> CL[K=definition,SEM=?formula] CL[K=entry] CL[K=emergence]
CL[K=definition,SEM=<?q(?p)>] -> N[CASE=nom,NUM=sg,GEN=m,SEM=?q] PTCL[CONTRAST=yes] N[CASE=nom,NUM=sg,GEN=f,SEM=?p]
CL[K=entry] -> ADJ[CASE=abl,NUM=sg,GEN=n,DEGREE=superlative] ADV[ORDER=after] N[CASE=acc,NUM=sg,GEN=n,SUPPLIED=prose] V[PERS=3,NUM=pl,TENSE=pres,VOICE=mid,SUPPLIED=prose]
CL[K=emergence] -> N[CASE=nom,NUM=sg,GEN=n] N[CASE=ins,NUM=sg,GEN=n] ADJ[CASE=ins,NUM=sg,GEN=n,PAIR=own_pure_or_lower_noble] ADV[SOURCE=attainment]
N[CASE=nom,NUM=sg,GEN=m,SEM=<\P.(Cessation(cessationAttainment) & P(cessationAttainment))>] -> 'nirodhaḥ'
PTCL[CASE=none,NUM=none,GEN=none,CONTRAST=yes] -> 'tu'
N[CASE=nom,NUM=sg,GEN=f,SEM=<\x.Attainment(x)>] -> 'samāpattiḥ'
ADJ[CASE=abl,NUM=sg,GEN=n,DEGREE=superlative] -> 'sūkṣmasūkṣmāt'
ADV[CASE=none,NUM=none,GEN=none,ORDER=after] -> 'anantaram'
N[CASE=acc,NUM=sg,GEN=n,SUPPLIED=prose] -> '∅-nirodham'
V[CASE=none,NUM=pl,GEN=none,PERS=3,TENSE=pres,VOICE=mid,SUPPLIED=prose] -> '∅-samāpadyante'
N[CASE=nom,NUM=sg,GEN=n] -> 'vyutthānam'
N[CASE=ins,NUM=sg,GEN=n] -> 'cetasā'
ADJ[CASE=ins,NUM=sg,GEN=n,PAIR=own_pure_or_lower_noble] -> 'svaśuddhakādharāryeṇa'
ADV[CASE=none,NUM=none,GEN=none,SOURCE=attainment] -> 'tataḥ'
```

```nltk-dep
'nirodhaḥ' -> 'tu' | 'samāpattiḥ'
'∅-samāpadyante' -> 'sūkṣmasūkṣmāt' | 'anantaram' | '∅-nirodham'
'vyutthānam' -> 'cetasā' | 'svaśuddhakādharāryeṇa' | 'tataḥ'
'cetasā' -> 'svaśuddhakādharāryeṇa'
```

`Svaśuddhaka` and `adhara-ārya` are two paired alternatives, not four minds; the latter is
noble in the verse, while the running prose reads contaminated. Neither this emergence mind
nor the construction asserts cognition inside cessation.


**Close construe.** The eighth release is cessation-attainment,
entered immediately after the subtle is made still
subtler. From it emergence occurs through an
own-level pure mind or, according to the verse,
a lower-level noble mind.

## 5. Translation

### Literal Translation

> Cessation, however, is an attainment, immediately
> after the most subtle of the subtle. From
> it emergence occurs through an own-level pure
> or lower-level noble mind.

### Bhāṣya-informed study translation

> Cessation, however, is an attainment entered immediately after the
> subtlest of the subtle [perception]. From it, emergence occurs through a
> pure mind of its own [summit] level or through a noble mind of a lower level.

## 6. Philosophical Translation

> Cessation is identified as a particular attainment
> with a determinate entry condition and specified
> emergence alternatives. Its place in the release
> inventory does not make it an unqualified name
> for every kind of cessation. The text describes
> an attained cessation of perception and feeling,
> not merely a general absence of activity.

The named attainment should not be equated with
analytical or non-analytical cessation merely because
all use cessation vocabulary. Those distinctions
were operative in VAK 8.26 and remain separate.

## 7. Technical Vocabulary

**`Saṃjñāveditanirodha`.** Cessation of perception and
feeling. This is the prose's precise identification
of the eighth release.

**`Nirodhasamāpatti`.** Cessation-attainment. The commentary
refers back to its earlier exposition rather
than restating all eligibility and duration conditions.
This unit supplies no complete standalone practice manual.

**`Sūkṣmasūkṣma / sūkṣmatara`.** Extremely subtle /
still subtler. The comparative in the prose
expresses a further refinement before entry, not
an arbitrary jump from any ordinary mental state.

**`Svaśuddhaka`.** Own-level pure, specified as summit-level
pure mind. Pure retains the established wholesome
contaminated meaning and does not become uncontaminated
merely because it follows cessation.

**`Adharārya`.** Lower-level noble. The verse's
term indicates the noble alternative associated in
prose with nothingness. It must not be translated
as contaminated without disclosing the conflict.

**`Vyutthāna`.** Emergence. The mind named here
belongs to emergence from the attainment, not
a continuously operating observing mind asserted within it.

**`Samāpattyāvaraṇa`.** Obstruction to attainment. The
alternative explanation invokes release from this obstruction
to explain the vimokṣa designation. The attribution
to others must remain explicit.

## 8. Logical Determination

This verse distinguishes cessation-attainment, its entry condition, and two emergence alternatives. `[verse]` identifies the attainment and gives own-level pure or lower-level noble emergence; `[prose]` specifies perception made subtler at bhavāgra and conflicts with the verse on the lower-level alternative's mode.

**Signature.** `Attainment(x)`; `Cessation(x)`; `ImmediatelyBefore(x,y)`; `ExitLevel(x,l)`; `VerseExitMode(x,m)`; `ProseExitMode(x,m)`.

```nltk-sem
# derived by the section 4 parse, not typed by hand
(Cessation(cessationAttainment) & Attainment(cessationAttainment))
```

```nltk-valuation
cessationAttainment => cessationAttainment
subtlePerception => subtlePerception
subtlerPerception => subtlerPerception
entryMoment => entryMoment
ownLevelExit => ownLevelExit
lowerLevelExit => lowerLevelExit
bhavagra => bhavagra
nothingness => nothingness
pure => pure
noble => noble
contaminated => contaminated
Attainment => {cessationAttainment}
Cessation => {cessationAttainment}
ImmediatelyBefore => {(subtlePerception,subtlerPerception),(subtlerPerception,entryMoment)}
ExitLevel => {(ownLevelExit,bhavagra),(lowerLevelExit,nothingness)}
VerseExitMode => {(ownLevelExit,pure),(lowerLevelExit,noble)}
ProseExitMode => {(ownLevelExit,pure),(lowerLevelExit,contaminated)}
```

```nltk-fol
# THEORY shared
# [derived by the section 4 parse, not typed by hand] the named cessation-attainment is both cessation and an attainment
(Cessation(cessationAttainment) & Attainment(cessationAttainment))
# [prose] bhavāgra perception is made subtler immediately before entry
ImmediatelyBefore(subtlePerception,subtlerPerception)
ImmediatelyBefore(subtlerPerception,entryMoment)
# [verse, prose] own-level exit is pure
ExitLevel(ownLevelExit,bhavagra)
VerseExitMode(ownLevelExit,pure)
ProseExitMode(ownLevelExit,pure)
# THEORY verse_exit
# [verse] lower-level exit is noble
ExitLevel(lowerLevelExit,nothingness)
VerseExitMode(lowerLevelExit,noble)
# THEORY prose_exit
# [prose, conflicting witness] lower-level exit is called sāsrava
ExitLevel(lowerLevelExit,nothingness)
ProseExitMode(lowerLevelExit,contaminated)
```

**Results (NLTK).** The checker reports `shared: T`, `verse_exit: T`, and `prose_exit: T` in the finite model because the witness-specific mode predicates preserve the disagreement instead of identifying them as one value.

**Scope cautions.** This is an attributed witness conflict, not a harmonized mode claim. Entry/emergence do not assert cognition during cessation or a complete itinerary through every formless attainment. The prose's damaged final summary remains outside this formalization.

## 9. Interpretive Note

**The source conflict is material, not cosmetic.**
Sāsrava and ārya are not interchangeable spellings.
The earlier four-item construe is corrected to
two paired alternatives, but the running prose's
mode conflict cannot be solved merely by grammatical
segmentation. Additional witness comparison would be
needed for a critical settlement.

**Other witness cautions.** The sentence beginning
`bhavāgraṃ hi saṃjñā sūkṣmaṃ` has uneven agreement,
though its subsequent sūkṣmataraṃ kṛtvā securely
expresses further refinement. The study retains
the clear operation without presenting a normalized
sentence as the transmitted wording. Original files
remain unchanged.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates attainment identity, preceding
condition, and emergence alternatives. Yoga Technē,
its kriyā–karma companion, concerns the refinement
and entry described in the commentary. The fact
that cessation has specified transitions does not
itself identify it with the Organon Concept or
with Yoga's final nirodha.

The research's Māyā comparison remains project interpretation.
For Organon representation, store the conflicting
mode evidence with its source and status rather
than letting one unqualified edge conceal the
problem. A model of the passage should preserve
uncertainty where the textual determination remains incomplete.

**Review status.** Provisional, source-controlled study
with a material unresolved witness conflict. The
eighth-release identity, naming explanations, subtle-perception
refinement, and two emergence levels have been
checked against the local research and running
source. The second emergence mode and final
prose summary remain textually qualified.

## 10. OWL++ Seed

```text
Class: CessationAttainment
Class: EntryCondition
Class: EmergenceAlternative
Class: WitnessAssertion

ObjectProperty: immediatelyPrecededBy
ObjectProperty: hasEmergenceAlternative
ObjectProperty: supportedByWitness
ObjectProperty: hasTextualStatus

EighthRelease:
    identity: CessationOfPerceptionAndFeelingAttainment
    entryCondition: SummitPerceptionMadeStillSubtler

OwnLevelEmergence:
    level: Bhavagra
    mode: Pure
    evidenceAgreement: VerseAndProse

LowerLevelEmergence:
    level: Nothingness
    verseMode: Noble
    transmittedProseMode: Contaminated
    status: UnresolvedWitnessConflict

ProjectConstraint: The emergence compound gives two paired alternatives, not four.
ProjectConstraint: Preserve noble in the verse-led translation.
ProjectConstraint: Do not silently emend the conflicting prose mode.
ProjectConstraint: Do not posit an uncontaminated summit attainment.
ProjectConstraint: Emergence mind is not evidence of cognition during cessation.
ProjectConstraint: Cessation-attainment is distinct from the unconditioned cessations.
ProjectConstraint: Preserve the damaged closing summary as unresolved.
```

This is a declarative project seed, not executable OWL.
VAK 8.34 next specifies the releases' object ranges
and continues their practical explanation.
