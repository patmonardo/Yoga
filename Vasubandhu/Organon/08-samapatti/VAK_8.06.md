# VAK_8.06 — Savoring the Immediately Past Pure Attainment

## 1. Sanskrit (Devanāgarī)

```sanskrit
आस्वादनासंप्रयुक्तं सतृष्णं लौकिकं शुभम् ।
शुद्धकं तत्तदास्वाद्यं लोकोत्तरमनास्रवम् ॥ ८.०६ ॥
```

## 2. Sanskrit (IAST)

```text
āsvādanāsaṃprayuktaṃ satṛṣṇaṃ laukikaṃ śubham |
śuddhakaṃ tattadāsvādyaṃ lokottaramanāsravam || 8.06 ||
```

The Sanskrit follows the local kārikā witness. The
Devanāgarī renders the same reading. The running source
has `lokattaram` where the local verse and explanatory
prose establish `lokottaram`.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `āsvādanā-saṃprayuktam` | nominative singular neuter compound adjective | associated with savoring |
| `sa-tṛṣṇam` | nominative singular neuter compound adjective | accompanied by craving |
| `laukikam` | nominative singular neuter adjective | worldly |
| `śubham` | nominative singular neuter adjective | wholesome |
| `śuddhakam` | nominative singular neuter adjective | pure |
| `tat` | nominative singular neuter pronoun (`tat + tad-` → `tattad-`) | that pure attainment |
| `tad-āsvādyam` | nominative singular neuter compound with gerundive | to be savored by the savoring-associated attainment, which takes the pure attainment as object |
| `lokottaram` | nominative singular neuter adjective | supramundane |
| `anāsravam` | nominative singular neuter adjective | uncontaminated, without influxes |

The understood noun is `samāpatti-dravyam`, the attainment under classification.

## 4. Grammar

The line break does not divide the definition of the pure attainment: worldly wholesome is its description. The prose equates savoring with craving and identifies the savored item and the savoring attainment as distinct.

```nltk-fcfg
% start S
# tokens: āsvādanāsaṃprayuktam satṛṣṇaṃ ∅-samāpattidravyam laukikam śubham śuddhakam tat tadāsvādyam ∅-āsvādanāsaṃprayuktam lokottaram anāsravam
S -> CL[K=savoring] CL[K=pure] CL[K=relation] CL[K=supramundane]
CL[K=savoring] -> ADJ[CASE=nom,NUM=sg,GEN=n,MODE=craving] ADJ[CASE=nom,NUM=sg,GEN=n,ACCOMP=yes] N[CASE=nom,NUM=sg,GEN=n,SUPPLIED=prose]
CL[K=pure] -> ADJ[CASE=nom,NUM=sg,GEN=n] ADJ[CASE=nom,NUM=sg,GEN=n,QUALITY=wholesome] ADJ[CASE=nom,NUM=sg,GEN=n,QUALITY=pure]
CL[K=relation] -> PRON[CASE=nom,NUM=sg,GEN=n,REF=pure] ADJ[CASE=nom,NUM=sg,GEN=n,ROLE=object] N[CASE=nom,NUM=sg,GEN=n,SUPPLIED=prose,ROLE=agent]
CL[K=supramundane] -> ADJ[CASE=nom,NUM=sg,GEN=n] ADJ[CASE=nom,NUM=sg,GEN=n,QUALITY=uncontaminated]
ADJ[CASE=nom,NUM=sg,GEN=n,MODE=craving] -> 'āsvādanāsaṃprayuktam'
ADJ[CASE=nom,NUM=sg,GEN=n,ACCOMP=yes] -> 'satṛṣṇaṃ'
N[CASE=nom,NUM=sg,GEN=n,SUPPLIED=prose] -> '∅-samāpattidravyam'
ADJ[CASE=nom,NUM=sg,GEN=n] -> 'laukikam'
ADJ[CASE=nom,NUM=sg,GEN=n,QUALITY=wholesome] -> 'śubham'
ADJ[CASE=nom,NUM=sg,GEN=n,QUALITY=pure] -> 'śuddhakam'
PRON[CASE=nom,NUM=sg,GEN=n,REF=pure] -> 'tat'
ADJ[CASE=nom,NUM=sg,GEN=n,ROLE=object] -> 'tadāsvādyam'
N[CASE=nom,NUM=sg,GEN=n,SUPPLIED=prose,ROLE=agent] -> '∅-āsvādanāsaṃprayuktam'
ADJ[CASE=nom,NUM=sg,GEN=n] -> 'lokottaram'
ADJ[CASE=nom,NUM=sg,GEN=n,QUALITY=uncontaminated] -> 'anāsravam'
```

```nltk-dep
'∅-samāpattidravyam' -> 'āsvādanāsaṃprayuktam' | 'satṛṣṇaṃ' | 'laukikam' | 'śubham' | 'śuddhakam'
'tadāsvādyam' -> 'tat' | '∅-āsvādanāsaṃprayuktam'
'anāsravam' -> 'lokottaram'
```

The gerundive marks the pure attainment as object, savored by the savoring-associated attainment; it is not an injunction. Supramundane status is not simply a higher meditative level.


**Close construe.** Savoring-associated attainment has
craving. Worldly wholesome attainment is pure. That
pure attainment is savored by the savoring-associated
one. Supramundane attainment is uncontaminated.

## 5. Translation

### Literal Translation

> Savoring-associated attainment is accompanied by craving.
> Worldly wholesome attainment is pure; that is what
> the savoring-associated attainment savors. Supramundane
> attainment is uncontaminated.

### Bhāṣya-informed study translation

> Savoring-associated attainment is accompanied by craving.
> Worldly wholesome attainment is pure; that pure attainment is
> what the savoring-associated attainment savors. Supramundane
> attainment is uncontaminated.

## 6. Philosophical Translation

> A wholesome attainment can become the object of a
> subsequent craving-associated attainment. The former's
> purity does not determine the character of the later
> cognition that takes it as object. The classification
> requires both the present mode and its relation to
> the immediately preceding state.

This does not retroactively make the past pure attainment
craving-associated. The prose distinguishes what is
savored from that by which it is savored, and emergence
from the former from entry into the latter.

## 7. Technical Vocabulary

**`Āsvādanā`.** Savoring or relish, explicitly identified
here with craving. It should not be equated with every
occurrence of joy or pleasure. Those can be factors
of wholesome dhyāna without being identical with craving.

**`Satṛṣṇa`.** Accompanied by craving. This specifies
the present savoring-associated attainment, not the
immediately past pure attainment that it takes as object.

**`Śuddhaka`.** Pure, here worldly and wholesome. The
prose explains its name through conjunction with pure
dharmas beginning with non-greed. It remains distinct
from the supramundane category in the same verse.

**`Alobha`.** Non-greed, the named example of a pure
dharma. `Ādi`, “and so forth,” indicates that the
example is not a complete inventory of associated factors.

**`Samanantarātīta`.** Immediately past. This gives the
temporal determination of the pure attainment being
savored. The present passage does not extend this
specific relation to every remote memory of meditation.

**`Vyutthita / samāpanna`.** Emerged from and entered
into an attainment. The pair distinguishes the two
successive modes. Emergence here does not require a
return to an ordinary nonmeditative condition: the
practitioner is described as entered into the savoring-
associated attainment.

**`Lokottara / anāsrava`.** Supramundane and uncontaminated.
The source correlates these in the attainment classification.
They do not mean unconditioned simply by contrast with
worldly wholesome attainment.

## 8. Logical Determination

The verse defines three modes of attainment and distinguishes the pure attainment that is savored from the craving-associated attainment that savors it [verse; prose]. The relation is temporal and intentional, not an identity of modes.

**Signature.** `Savoring(x)`; `Craving(x)`; `Worldly(x)`; `Wholesome(x)`; `Pure(x)`; `ImmediatelyPast(x,y)`; `SavoredBy(x,y)`; `Supramundane(x)`; `Uncontaminated(x)`.

**Finite data.** The two occurrences are modeled separately; the pure occurrence is worldly and wholesome, and the third mode is supramundane and uncontaminated.

```nltk-valuation
savoringnow => savoringnow
purepast => purepast
uncontaminatedattainment => uncontaminatedattainment
Savoring => {savoringnow}
Craving => {savoringnow}
Worldly => {purepast}
Wholesome => {purepast}
Pure => {purepast}
ImmediatelyPast => {(purepast,savoringnow)}
SavoredBy => {(purepast,savoringnow)}
Supramundane => {uncontaminatedattainment}
Uncontaminated => {uncontaminatedattainment}
```

**Rules (verse and prose).**

```nltk-fol
# THEORY shared
# [prose] tṛṣṇā hy āsvādanā
all x.(Savoring(x) -> Craving(x))
# [verse] laukikaṃ śubham śuddhakam; [prose] alobha and other pure dharmas
all x.(Pure(x) -> (Worldly(x) & Wholesome(x)))
# [verse] tattadāsvādyam; [prose] the immediately past pure item is the object
SavoredBy(purepast,savoringnow)
ImmediatelyPast(purepast,savoringnow)
# [verse] lokottaram anāsravam
all x.(Supramundane(x) -> Uncontaminated(x))
```

**Results (NLTK).** The checker reports the shared rules true in the supplied finite model. This is a model check of the represented assignments, not a theorem that every pure attainment is subsequently savored.

**Scope cautions.** `tat` is the pure object and the savoring-associated occurrence is the agent. Emergence from the former and entry into the latter do not say that every practitioner's course follows this sequence. Pure is not synonymous with uncontaminated, and joy in wholesome dhyāna is not thereby craving.

## 9. Interpretive Note

**Reading the pronouns through the prose.** The local
Bhāṣya's introductory translation uses “each corresponding
pure attainment.” The direct prose relation is more
specific: that pure attainment, immediately past, is
savored by the craving-associated one. The study therefore
keeps the two referents and the temporal qualification
explicit rather than relying on a loose distributive
reading of `tattad`.

**The source transition.** At 437|13–14 the running
source begins a compressed sentence contrasting dhyānas
with formless attainments before the factor enumeration.
That transition must not be used here to deny the
uncontaminated formless attainments already admitted
in VAK 8.05. Its exact role belongs with the following
aṅga discussion rather than with a new exception to
the present mode definitions.

**Witness cautions.** The running source prints
`śuddhakamuccayate` and `lokattaram`; the local extract
regularizes these while preserving the clear definition
of worldly wholesome as pure and supramundane as
uncontaminated. The temporal expression and the paired
emergence/entry statement are intact. The underlying
witnesses are unchanged.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates the distinction between an
attainment's own character and that of a later cognition
which takes it as object. Yoga Technē, its kriyā–karma
companion, concerns the exercise and succession of
these modes. Their relation matters because the object
of a cognition does not determine its ethical character
by simple transmission.

For Organon, a refined or wholesome state can be
related to a later operation whose determination differs.
The source gives a concrete case: immediately past
pure attainment is the object of present savoring.
A representation must keep the two occurrences, their
modes, and their temporal relation distinct.

This is a project use of the source's practical analysis,
not a universal theory that every valuable experience
produces attachment. The positive source determination
is narrower: what savoring is, what it savors here,
and which attainment the practitioner has left and entered.

**Review status.** Provisional, Bhāṣya-controlled study.
The craving definition, worldly-wholesome pure mode,
non-greed explanation, immediately past object, emergence/
entry distinction, and supramundane classification have
been checked against the local extract and running
source. The factor-analysis transition remains for 8.07.

## 10. OWL++ Seed

```text
Class: AttainmentOccurrence
Class: AttainmentMode
Class: SavoringRelation

ObjectProperty: hasMode
ObjectProperty: conjoinedWith
ObjectProperty: savorsOccurrence
ObjectProperty: immediatelyPrecededBy
ObjectProperty: emergedFrom
ObjectProperty: enteredInto

SavoringAssociated:
    definingAssociation: Craving

Pure:
    character: WorldlyWholesome
    associatedPureDharmaExample: NonGreed

Uncontaminated:
    character: Supramundane

DescribedSavoringSequence:
    previousOccurrence: PureAttainment
    currentOccurrence: SavoringAssociatedAttainment
    objectOfCurrentSavoring: ImmediatelyPastPureAttainment
    practitionerEmergedFrom: PreviousOccurrence
    practitionerEnteredInto: CurrentOccurrence

ProjectConstraint: Joy and pleasure are not automatically craving.
ProjectConstraint: Pure and uncontaminated remain distinct.
ProjectConstraint: Past pure occurrence is not retroactively craving-associated.
ProjectConstraint: The sequence is not compulsory after every pure attainment.
ProjectConstraint: Emergence from one attainment may accompany entry into another.
ProjectConstraint: VAK 8.05's eighth-attainment exclusion remains in force.
```

This is a declarative project seed, not executable OWL.
VAK 8.07 next enumerates the factors of the first and
second dhyānas.
