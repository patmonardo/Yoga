# VAK_8.25 — Modes, Gates of Liberation, and Three Further Samādhis

## 1. Sanskrit (Devanāgarī)

```sanskrit
शुद्धामलाः निर्मलास्तु ते विमोक्षमुखत्रयम् ।
शून्यताशून्यताद्याख्यास्त्रयोऽपरसमाधयः ॥ ८.२५ ॥
```

## 2. Sanskrit (IAST)

```text
śuddhāmalāḥ nirmalās tu te vimokṣamukhatrayam |
śūnyatāśūnyatādyākhyās trayo 'parasamādhayaḥ || 8.25 ||
```

The Sanskrit follows the local kārikā witness. The
second half introduces names whose precise Supports
and aspects are determined in VAK 8.26. Its brief
naming explanation must be read with that continuation.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `śuddhāmalāḥ` | nominative plural compound | pure and stainless, as alternative modes |
| `nirmalāḥ` | nominative plural masculine adjective | stainless, here uncontaminated |
| `tu` | contrast particle | however |
| `te` | nominative plural masculine pronoun | those three samādhis |
| `vimokṣamukhatrayam` | nominative singular neuter collective expression | the triad of liberation gates |
| `śūnyatāśūnyatādyākhyāḥ` | nominative plural masculine compound adjective | named emptiness-of-emptiness and so forth |
| `trayaḥ` | nominative plural masculine numeral | three |
| `aparasamādhayaḥ` | nominative plural masculine compound | further samādhis |

`Śuddha + amala` yields `śuddhāmala`;
`śūnyatāśūnyatā + ādi + ākhyāḥ` yields
`śūnyatāśūnyatādyākhyāḥ`; `trayaḥ + apara-`
yields `trayo 'para-`. The transmitted compound
aparasamādhayaḥ is retained rather than silently
replaced with the two-word apare samādhayaḥ.

## 4. Grammar

The first clause continues the three-samādhi subject and gives its two modes; the gate clause restricts the designation to the uncontaminated forms. The last clause introduces three further named samādhis.

```nltk-fcfg
% start S
# tokens: te śuddhāmalāḥ nirmalāḥ tu vimokṣamukhatrayam śūnyatāśūnyatādyākhyāḥ trayaḥ aparasamādhayaḥ
S[SEM=?formula] -> CL[K=modes] CL[K=gates,SEM=?formula] CL[K=further]
CL[K=modes] -> N[CASE=?c,NUM=?n,GEN=?g] ADJ[CASE=?c,NUM=?n,GEN=?g,MODES=two]
CL[K=gates,SEM=<?q(?p)>] -> ADJ[CASE=nom,NUM=pl,GEN=m,MODE=uncontaminated,SEM=?q] PTCL[CASE=none,NUM=none,GEN=none,CONTRAST=yes] N[CASE=nom,NUM=sg,GEN=n,COLLECTIVE=yes,SEM=?p]
CL[K=further] -> ADJ[CASE=nom,NUM=pl,GEN=m,NAME=examples] NUMR[CASE=nom,NUM=pl,GEN=m] N[CASE=nom,NUM=pl,GEN=m]
N[CASE=nom,NUM=pl,GEN=m] -> 'te'
ADJ[CASE=nom,NUM=pl,GEN=m,MODES=two] -> 'śuddhāmalāḥ'
ADJ[CASE=nom,NUM=pl,GEN=m,MODE=uncontaminated,SEM=<\P.all x.((Triad(x) & Uncontaminated(x)) -> P(x))>] -> 'nirmalāḥ'
PTCL[CASE=none,NUM=none,GEN=none,CONTRAST=yes] -> 'tu'
N[CASE=nom,NUM=sg,GEN=n,COLLECTIVE=yes,SEM=<\x.Gate(x)>] -> 'vimokṣamukhatrayam'
ADJ[CASE=nom,NUM=pl,GEN=m,NAME=examples] -> 'śūnyatāśūnyatādyākhyāḥ'
NUMR[CASE=nom,NUM=pl,GEN=m] -> 'trayaḥ'
N[CASE=nom,NUM=pl,GEN=m] -> 'aparasamādhayaḥ'
```

```nltk-dep
'te' -> 'śuddhāmalāḥ' | 'nirmalāḥ' | 'vimokṣamukhatrayam'
'nirmalāḥ' -> 'tu'
'aparasamādhayaḥ' -> 'trayaḥ' | 'śūnyatāśūnyatādyākhyāḥ'
```

The prose specifies śuddha/amala as worldly-pure/uncontaminated, and `nirmalās tu te`
limits the gate designation to uncontaminated forms. `Ādi` supplies the two other doubled
names; their exact Supports are deferred to 8.26.


**Close construe.** The preceding three samādhis have
pure and uncontaminated forms; in their uncontaminated
forms they are the three gates of liberation.
There are three further samādhis, beginning with
the one named emptiness-of-emptiness.

## 5. Translation

### Literal Translation

> [The three samādhis] are pure or stainless; those that are stainless,
> however, are the triad of gates of liberation. There are three further
> samādhis named emptiness-of-emptiness and so forth.

### Bhāṣya-informed study translation

> The three samādhis are of two kinds, worldly-pure and uncontaminated;
> but the uncontaminated ones are called the three gates of liberation.
> There are three further samādhis, named emptiness-of-emptiness and so forth.

## 6. Philosophical Translation

> A samādhi's named aspect-structure and its worldly
> or supramundane mode are distinct determinations.
> The gate designation belongs to the uncontaminated
> forms. The further triad then introduces another
> Support relation associated with the preceding samādhis,
> whose doubled names require the next verse's
> detailed explanation.

The further triad is not established here as a
superior grade of uncontaminated attainment. “Further”
introduces another group; its own modal classification
must be taken from the subsequent source discussion.

## 7. Technical Vocabulary

**`Śuddha / śuddhaka`.** Pure, here worldly and
wholesome but contaminated. The earlier aspect definitions
can occur in this mode without receiving the
technical liberation-gate designation used here.

**`Amala / nirmala / anāsrava`.** Stainless /
untainted / uncontaminated. The commentary resolves
the verse's two stainless expressions through anāsrava,
not through an additional scale of psychological purity.

**`Laukika / lokottara`.** Worldly / supramundane.
These explain the two modes and their distinct
level-distributions. The verse's mode distinction must
not be treated as simply lower versus higher rebirth.

**`Vimokṣamukha / mokṣadvāra`.** Gate of liberation /
door of liberation. The prose uses the second
to explain the first. It identifies a liberative
function, not a physical location or a fourth
samādhi added to the three.

**`Śūnyatāśūnyatā`.** Emptiness-of-emptiness, the first
further samādhi. Its precise Support and aspect
are reserved for VAK 8.26 rather than inferred
from the doubled name alone.

**`Apraṇihitāpraṇihita`.** Non-directedness-of-non-directedness,
the second further samādhi. “Non-directed” retains
the established study rendering of apraṇihita.

**`Ānimittānimitta`.** Signlessness-of-signlessness, the
third further samādhi. Its Support specification
in the following verse requires special care;
it is not adequately represented by copying the
same direct-Support rule from the first two.

## 8. Logical Determination

The verse distinguishes mode from designation: the three earlier samādhis can be worldly-pure or uncontaminated, while the liberation-gate name belongs to the uncontaminated forms. It also names a further triad without yet fixing its full Support relation. `[verse]`; the mode gloss and gate restriction are `[prose]`.

**Signature.** `Triad(x)`; `WorldlyPure(x)`; `Uncontaminated(x)`; `Gate(x)`; `Further(x)`; `Named(x,n)`.

```nltk-sem
# derived by the section 4 parse, not typed by hand
all x.((Triad(x) & Uncontaminated(x)) -> Gate(x))
```

```nltk-valuation
signlessWorld => signlessWorld
emptinessWorld => emptinessWorld
nondirectedWorld => nondirectedWorld
signlessPure => signlessPure
emptinessPure => emptinessPure
nondirectedPure => nondirectedPure
emptyOfEmpty => emptyOfEmpty
nonDirectedOfNonDirected => nonDirectedOfNonDirected
signlessOfSignless => signlessOfSignless
signless => signless
emptiness => emptiness
nondirected => nondirected
Triad => {signlessWorld, emptinessWorld, nondirectedWorld, signlessPure, emptinessPure, nondirectedPure}
WorldlyPure => {signlessWorld, emptinessWorld, nondirectedWorld}
Uncontaminated => {signlessPure, emptinessPure, nondirectedPure}
Gate => {signlessPure, emptinessPure, nondirectedPure}
Further => {emptyOfEmpty, nonDirectedOfNonDirected, signlessOfSignless}
Named => {(emptyOfEmpty,emptiness),(nonDirectedOfNonDirected,nondirected),(signlessOfSignless,signless)}
```

```nltk-fol
# THEORY shared
# [verse] two modes; [prose] śuddha/amala distinguished as worldly-pure/uncontaminated
all x.(Triad(x) -> (WorldlyPure(x) | Uncontaminated(x)))
# [derived by the section 4 parse, not typed by hand] nirmalās tu te, scoped to the uncontaminated forms of the preceding triad
all x.((Triad(x) & Uncontaminated(x)) -> Gate(x))
# [verse, prose] gate designation is restricted to uncontaminated forms
all x.((Triad(x) & Gate(x)) -> Uncontaminated(x))
# [verse] three names, filled out as the further triad by the prose
all x.(Further(x) -> exists n.Named(x,n))
```

**Results (NLTK).** `check_logic.py` reports `shared: T` against the finite valuation. It checks these mode/gate and naming rules; no prover entailment or contradiction test is claimed.

**Scope cautions.** Worldly-pure and uncontaminated are distinct modes; the model's separate individuals are not a claim that one occurrence instantiates both. The doubled names introduce the next discussion but do not establish three identical self-observation relations or a mandatory sequence.

## 9. Interpretive Note

**Refinement of the research interpretation.** The
local study calls the further triad “reflexive
Recognition” and depicts the preceding samādhi becoming
a Support. This is useful as an introductory
project interpretation, but the next verse's third
case prevents treating the diagram as an exact
uniform source rule. The official study leaves
the Support relations open to their explicit qualifications.

**Source boundaries.** The eleven-level statement,
path-location statement, gate explanation, three names,
and compact Support-based naming explanation are all
present in this unit. The exact aspects, qualifications
of the Support samādhis, and further triad's own
modes are not settled merely by its introduction.
Original research and running-source files remain unchanged.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
The project's “Recognition” vocabulary can articulate
a further relation to an already determined samādhi.
Yoga Vidyā specifies the mode, aspect-structure,
and Support relation; Yoga Technē, its kriyā–karma
companion, concerns the effective operation through
which the source distinguishes worldly cultivation
from the uncontaminated gates.

The research's Yoga Sūtra III.3 and determinate-Concept
comparison remains a comparative project layer rather
than a gloss supplied by this Bhāṣya passage.
For Organon representation, keep a naming relation
separate from the exact Support specification, and
avoid treating “further” as an automatic increase
in liberative rank. This preserves the source's
own next step of determination.

**Review status.** Complete [450|01–02]–[450|10–11] unit collated
with `kosabhasya.txt`; [450|01] closes 8.24 and `teṣāṃ punaḥ` at
[450|11] opens 8.26. The split verse, gate recital, and all three
doubled names are restored in the paired Bhāṣya study. The compressed
recital and naming syntax remain visible without reconstruction.
The next unit differentiates the further triad's Supports.

## 10. OWL++ Seed

```text
Class: FirstTriadSamadhi
Class: SamadhiMode
Class: LiberationGate
Class: FurtherSamadhi
Class: SupportBasedNamingRelation

ObjectProperty: hasAvailableMode
ObjectProperty: designatedGateWhen
ObjectProperty: hasNamingRelation

FirstTriad:
    members: Sunyata, Apranihita, Animitta
    availableModes: WorldlyPure, UncontaminatedSupramundane
    worldlyLevelCount: 11
    supramundaneLocation: WhereThePathOccurs

GateDesignation:
    eligibleMode: Uncontaminated
    members: SunyataGate, ApranihitaGate, AnimittaGate
    explanation: DoorsOfLiberation

FurtherTriad:
    members: SunyataSunyata, ApranihitaApranihita, AnimittaAnimitta
    namingGround: SupportRelationBeginningWithSunyata
    exactSupportSpecifications: ContinueInVAK8_26

ProjectConstraint: Pure and uncontaminated are alternative modes.
ProjectConstraint: Amala and nirmala do not introduce additional modes.
ProjectConstraint: The technical gate designation requires uncontaminated mode.
ProjectConstraint: Further does not imply a higher uncontaminated grade.
ProjectConstraint: Do not impose one identical direct-Support rule on all three.
ProjectConstraint: Reflexive Recognition is a qualified project interpretation.
ProjectConstraint: Naming does not establish simultaneous self-apprehension.
```

This is a declarative project seed, not executable OWL.
VAK 8.26 next specifies the Supports and aspects
of the three further samādhis.
