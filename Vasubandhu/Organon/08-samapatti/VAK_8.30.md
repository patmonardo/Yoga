# VAK_8.30 — Equanimity, Aspiration, and the Immeasurables' Object-Field

## 1. Sanskrit (Devanāgarī)

```sanskrit
उपेक्षालोभः आकारः सुखिता दुःखिता वत ।
मोदन्तामिति सत्त्वाश्च कामसत्त्वास्तु गोचरः ॥ ८.३० ॥
```

## 2. Sanskrit (IAST)

```text
upekṣālobhaḥ ākāraḥ sukhitā duḥkhitā vata |
modantām iti sattvāś ca kāmasattvās tu gocaraḥ || 8.30 ||
```

The Sanskrit follows the local kārikā witness. The
running source quotes `upekṣā 'lobhaḥ`, explicitly
showing the alobha division. The prose supplies
all four contemplative forms, including equanimity's
attention simply to beings.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `upekṣā` | nominative singular feminine | equanimity, here the immeasurable |
| `alobhaḥ` | nominative singular masculine | non-greed |
| `ākāraḥ` | nominative singular masculine | aspect or contemplative form |
| `sukhitāḥ` | nominative plural masculine adjective | happy [beings] |
| `duḥkhitāḥ` | nominative plural masculine adjective | suffering [beings] |
| `vata` | exclamatory particle | indeed; alas, according to context |
| `modantām` | third-person plural imperative middle of √mud | may they rejoice |
| `iti` | quotation marker | thus |
| `sattvāḥ` | nominative plural masculine | beings |
| `kāmasattvāḥ` | nominative plural masculine compound | beings of the desire domain |
| `gocaraḥ` | nominative singular masculine | object-field or range |

`Upekṣā + alobhaḥ` yields `upekṣālobhaḥ`;
`sattvāḥ + ca` yields `sattvāś ca`; `kāmasattvāḥ
+ tu` yields `kāmasattvās tu`. Sukhitāḥ is
an adjective, not itself an optative verb: the
prose's later santu supplies the aspirational construe.

## 4. Grammar

The opening nominal clause names equanimity's nature; the subsequent quoted forms distribute across the four immeasurables. The surface adjective “happy” is interpreted aspirationally from the Bhāṣya, and the final clause restricts the object-field to desire-domain beings.

```nltk-fcfg
% start S
# tokens: upekṣā alobhaḥ ākāraḥ ∅-maitrī sukhitāḥ vata ∅-santu ∅-karuṇā duḥkhitāḥ vata ∅-muditā modantām iti sattvāḥ ca kāmasattvāḥ tu gocaraḥ
S -> CL[K=nature] CL[K=friendliness] CL[K=compassion] CL[K=joy] CL[K=equanimity_form] CL[K=field]
CL[K=nature] -> N[CASE=nom,NUM=sg,GEN=f] N[CASE=nom,NUM=sg,GEN=m] N[CASE=nom,NUM=sg,GEN=m,ROLE=aspect]
CL[K=friendliness] -> N[CASE=nom,NUM=sg,GEN=f,SUPPLIED=prose] ADJ[CASE=nom,NUM=pl,GEN=m] PTCL[EXCL=yes] V[CASE=none,NUM=pl,GEN=none,PERS=3,TENSE=pres,MOOD=subj,SUPPLIED=prose]
CL[K=compassion] -> N[CASE=nom,NUM=sg,GEN=f,SUPPLIED=prose] ADJ[CASE=nom,NUM=pl,GEN=m] PTCL[EXCL=yes]
CL[K=joy] -> N[CASE=nom,NUM=sg,GEN=f,SUPPLIED=prose] V[CASE=none,NUM=pl,GEN=none,PERS=3,TENSE=pres,MOOD=imper,VOICE=mid] PTCL[QUOTE=yes]
CL[K=equanimity_form] -> N[CASE=nom,NUM=pl,GEN=m] PTCL[ADD=yes]
CL[K=field] -> N[CASE=nom,NUM=pl,GEN=m] PTCL[CONTRAST=yes] N[CASE=nom,NUM=sg,GEN=m]
N[CASE=nom,NUM=sg,GEN=f] -> 'upekṣā'
N[CASE=nom,NUM=sg,GEN=m] -> 'alobhaḥ' | 'ākāraḥ'
N[CASE=nom,NUM=sg,GEN=f,SUPPLIED=prose] -> '∅-maitrī' | '∅-karuṇā' | '∅-muditā'
ADJ[CASE=nom,NUM=pl,GEN=m] -> 'sukhitāḥ' | 'duḥkhitāḥ'
PTCL[CASE=none,NUM=none,GEN=none,EXCL=yes] -> 'vata'
V[CASE=none,NUM=pl,GEN=none,PERS=3,TENSE=pres,MOOD=subj,SUPPLIED=prose] -> '∅-santu'
V[CASE=none,NUM=pl,GEN=none,PERS=3,TENSE=pres,MOOD=imper,VOICE=mid] -> 'modantām'
PTCL[CASE=none,NUM=none,GEN=none,QUOTE=yes] -> 'iti'
N[CASE=nom,NUM=pl,GEN=m] -> 'sattvāḥ' | 'kāmasattvāḥ'
PTCL[CASE=none,NUM=none,GEN=none,ADD=yes] -> 'ca'
PTCL[CASE=none,NUM=none,GEN=none,CONTRAST=yes] -> 'tu'
N[CASE=nom,NUM=sg,GEN=m] -> 'gocaraḥ'
```

```nltk-dep
'upekṣā' -> 'alobhaḥ' | 'ākāraḥ'
'∅-maitrī' -> 'sukhitāḥ' | 'vata' | '∅-santu'
'∅-karuṇā' -> 'duḥkhitāḥ' | 'vata'
'∅-muditā' -> 'modantām' | 'iti' | 'sattvāḥ' | 'ca'
'gocaraḥ' -> 'kāmasattvāḥ' | 'tu'
```

`Sukhitāḥ` itself is not imperative; `∅-santu` records the Bhāṣya's wish-reading.
“Beings” is the fourth form, not a second description of the first three; the
object-field is not the practitioner's level.


**Close construe.** Equanimity is non-greed. The
forms concern beings as happy, suffering, rejoicing,
and simply beings. Their object-field consists of
beings of the desire domain.

## 5. Translation

### Literal Translation

> [The nature of] equanimity is non-greed. The forms are “happy,”
> “alas, suffering,” “may they rejoice,” and “beings.”
> Beings of the desire domain are their object-field.

### Bhāṣya-informed study translation

> Equanimity has non-greed as its nature. The aspects of the immeasurables
> are: “How happy beings are!”, “Alas, beings suffer!”, “May beings
> rejoice!”, and simply “beings.” Their object-field is beings of the desire
> domain.

## 6. Philosophical Translation

> The cultivation's mental nature, contemplated form,
> intention, and object-field are distinct determinations.
> Wishing beings happiness does not require asserting
> that they already possess it. Equanimity's minimal
> form, simply beings, expresses impartiality within
> the specified field rather than absence of an object.

The source's own account distinguishes aspiration
from factual description. Its further replies concern
this wholesome cultivation; they do not license
arbitrary false assertions on the grounds of good intention.

## 7. Technical Vocabulary

**`Alobha`.** Non-greed. This is the verse's nature
assignment for equanimity. “Non-appropriation” can serve
as a project interpretation, but should not erase
the established mental-factor term.

**`Lobhākṛṣṭa`.** Drawn by greed. The prose uses
this relation to explain how non-greed counters
ill will. It then adds that a nature comprising
both factors is fitting.

**`Ubhayasvabhāva`.** Having both as its nature.
In context, the pair is non-greed and non-hatred.
The expositor's preferred refinement deserves more
than an unqualified repetition of the verse's
single-factor identification.

**`Mādhyasthya`.** Impartiality or neutrality of stance.
This explains equanimity's “beings” form. It does
not identify this immeasurable with the neutral-feeling
faculty merely because English uses neutral for both.

**`Āśaya / abhiprāya`.** Disposition / intention.
These terms help explain the happiness aspiration
without converting it into an assertion about
beings' present condition.

**`Adhimukti / adhimokṣa`.** Resolve or imaginative
determination. The prose invokes this character of
the cultivation in its discussion of apparent error.
It is not a claim that wished-for happiness
has already been externally produced.

**`Bhājana / bhājanagata`.** Container / what is
contained. The instruction concerning a direction
indicates beings within that spatial field through
reference to the field containing them.

## 8. Logical Determination

**Mental nature and contemplative form.**

| Immeasurable | Contemplative form in the prose |
|---|---|
| Friendliness | May beings be happy |
| Compassion | Alas, beings suffer |
| Sympathetic joy | May beings rejoice |
| Equanimity | Beings, attended to impartially |

These are not four additional feelings. They
specify the manner of attending to beings. The
mental-nature assignments of VAK 8.29 and the
opening of this verse answer a different question.

**The equanimity refinement.** The objection asks
how non-greed opposes ill will. The first reply
connects ill will with greed. The ensuing
`ubhayasvabhāvā tv asau yujyate` favors the
combined non-greed/non-hatred account. The study
preserves the verse assignment, explanation, and
preferred refinement as distinguishable steps.

**The apparent-error objection.** If beings do not
possess happiness, how is resolving upon their
happiness not erroneous? The commentary offers
several replies rather than a single undifferentiated answer:

- The intention is “may they be,” making the formula aspirational.
- Alternatively, the disposition is not erroneous, with the cognition understood as resolve.
- Even granting the proposed divergence, unwholesomeness does not follow here: the cultivation has wholesome roots and counteracts ill will and related tendencies.

The final reply is a conditional defense against
the charge of unwholesomeness, not a declaration
that every imagined state accurately describes the world.

**The object restriction is compatible with immeasurability.**
VAK 8.29 explains immeasurable through immeasurable
beings as objects. This verse identifies those
beings as desire-domain beings. Unbounded numerical
scope does not require abolishing the stated
category of objects.

**Direction denotes the beings in it.** The
prose explains the scriptural direction formula
through container and contained. Its spatial wording
does not make empty space or the world-container
itself the primary object in place of beings.

**The next question concerns levels.** The following
sentence asks on how many levels these immeasurables
occur. Those assignments belong to VAK 8.31;
they must not be inferred from the desire-domain
restriction on their objects.

## 9. Interpretive Note

**Refinements to earlier readings.** The
fourth form, simply beings, must be included.
The adjective sukhitāḥ acquires its aspirational
interpretation from the prose reply, not from
its morphology alone. The combined-nature proposal
for equanimity should also remain explicit rather
than being reduced to a vague possibility.

**Witness control.** The running source preserves
all four attention formulas, the santu explanation,
the alternative replies, and the container/contained
gloss. The clause concerning adhimukti is compressed;
its use here follows the immediate dispute about
resolve and apparent error without claiming a
critical reconstruction. Originals remain unchanged.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā distinguishes mental nature, aspect,
> intention, and object-field. Yoga Technē, its
kriyā–karma companion, concerns the cultivation of
those specific attitudes toward beings. The distinction
between wishing and asserting is especially useful:
a practical orientation can have a determinate
object without representing the desired condition
as already actual.

The research's “Buddha-Mind” and universal Recognition
language belongs to project interpretation. The
source here supplies four contemplative forms and
a qualified object-field; it does not itself
identify these with an unrestricted metaphysical
subject. For Organon representation, keep aspiration
separate from factual assertion and preserve each
attributed explanatory step.

**Review status.** Provisional, Bhāṣya-controlled study.
The alobha assignment and combined-nature refinement,
four forms, aspiration objection and replies,
desire-domain objects, and direction gloss have
been checked against the local research and running source.

## 10. OWL++ Seed

```text
Class: ImmeasurableCultivation
Class: ContemplativeForm
Class: AspirationalIntention
Class: ObjectField

ObjectProperty: attendsUnderForm
ObjectProperty: hasMentalNatureUnderAccount
ObjectProperty: hasObjectField

Maitri:
    form: MayBeingsBeHappy
    intentionalCharacter: Aspiration

Karuna:
    form: AlasBeingsSuffer

Mudita:
    form: MayBeingsRejoice

Upeksa:
    form: Beings
    stance: Impartiality
    verseNature: NonGreed
    preferredProseRefinement: NonGreedAndNonHatred

Immeasurables:
    objectField: DesireDomainBeings
    directionalFormula: ContainerIndicatesContainedBeings

ProjectConstraint: Preserve all four contemplative forms.
ProjectConstraint: Sukhita is adjectival; the prose supplies the wish interpretation.
ProjectConstraint: Aspiration does not assert present fulfillment.
ProjectConstraint: Impartiality is not automatically the neutral-feeling faculty.
ProjectConstraint: Wholesome-root defense is not a universal license for false assertion.
ProjectConstraint: Object domain and practitioner attainment level remain distinct.
```

This is a declarative project seed, not executable OWL.
VAK 8.31 next determines the immeasurables' levels
and qualifies their counteractive efficacy.
