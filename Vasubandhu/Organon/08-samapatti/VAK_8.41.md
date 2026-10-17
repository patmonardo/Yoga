# VAK_8.41 — Witnesses and the Disordering of the Teaching

## 1. Sanskrit (Devanāgarī)

```sanskrit
निमीलिते शास्तरि लोकचक्षुषि क्षयं गते साक्षिजने च भूयसा ।
अदृष्टतत्त्वैर्निरवग्रहैः कृतं कुतार्किकैः शासनमेतदाकुलम् ॥ ८.४१ ॥
```

## 2. Sanskrit (IAST)

```text
nimīlite śāstari lokacakṣuṣi kṣayaṃ gate sākṣijane ca bhūyasā |
adṛṣṭatattvair niravagrahaiḥ kṛtaṃ kutārkikaiḥ śāsanam etad ākulam || 8.41 ||
```

The local scripts agree with the verse in
the running source. No separate prose gloss
follows this verse in the witness used here;
the next transmitted unit is VAK 8.42.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `nimīlite` | locative singular participle | having closed; here of the Teacher as world-eye |
| `śāstari` | locative singular masculine of `śāstṛ` | when the Teacher |
| `lokacakṣuṣi` | locative singular compound epithet | the Eye of the World |
| `kṣayam` | accusative singular masculine | disappearance, passing away; complement of `gate` |
| `gate` | locative singular past passive participle of √gam | having gone |
| `sākṣijane` | locative singular masculine collective | when the body of witnesses |
| `bhūyasā` | instrumental singular comparative used adverbially | for the most part; largely |
| `adṛṣṭatattvaiḥ` | instrumental plural masculine possessive compound | by those who have not seen reality |
| `niravagrahaiḥ` | instrumental plural masculine adjective | unchecked, unrestrained |
| `kṛtam` | nominative singular neuter past passive participle of √kṛ | made |
| `kutārkikaiḥ` | instrumental plural masculine | by bad reasoners or sophistical disputants |
| `śāsanam` | nominative singular neuter | teaching, dispensation |
| `etat` | nominative singular neuter demonstrative | this |
| `ākulam` | nominative singular neuter predicate adjective | confused, disordered |

Sandhi: the endings in `adṛṣṭatattvair` and `etad` reflect
sandhi; the analytical forms are `adṛṣṭatattvaiḥ` and
etat. Ku- supplies the pejorative force in
kutārkika; it must not disappear in translation.

## 4. Grammar

Two locative absolutes set the circumstance for a passive main clause. The three instrumental descriptions unify as one group of agents; `bhūyasā` limits the disappearance of witnesses, and the pejorative `ku-` remains in the lexicon.

```nltk-fcfg
% start S
# tokens: nimīlite śāstari lokacakṣuṣi kṣayaṃ gate sākṣijane ca bhūyasā adṛṣṭatattvair niravagrahaiḥ kṛtaṃ kutārkikaiḥ śāsanam etat ākulam
S -> CL[K=setting] CL[K=disorder]

CL[K=setting] -> PTCP[CASE=?c,NUM=?n,GEN=?g,TENSE=past] N[CASE=?c,NUM=?n,GEN=?g] N[CASE=?c,NUM=?n,GEN=?g,APPOS=yes] N[CASE=acc,NUM=sg,GEN=m] PTCP[CASE=?c,NUM=?n,GEN=?g,TENSE=past] N[CASE=?c,NUM=?n,GEN=?g] CONJ[ADD=yes] ADV[DEGREE=limited]
CL[K=disorder] -> ADJ[CASE=ins,NUM=?n,GEN=?g] ADJ[CASE=ins,NUM=?n,GEN=?g] PTCP[CASE=nom,NUM=sg,GEN=n,TENSE=past,VOICE=pass] N[CASE=ins,NUM=?n,GEN=?g,ROLE=agent] N[CASE=nom,NUM=?p,GEN=?h,ROLE=patient] PRON[CASE=nom,NUM=?p,GEN=?h] ADJ[CASE=nom,NUM=?p,GEN=?h]

PTCP[CASE=loc,NUM=sg,GEN=m,TENSE=past] -> 'nimīlite'
N[CASE=loc,NUM=sg,GEN=m] -> 'śāstari'
N[CASE=loc,NUM=sg,GEN=m,APPOS=yes] -> 'lokacakṣuṣi'
N[CASE=acc,NUM=sg,GEN=m] -> 'kṣayaṃ'
PTCP[CASE=loc,NUM=sg,GEN=m,TENSE=past] -> 'gate'
N[CASE=loc,NUM=sg,GEN=m] -> 'sākṣijane'
CONJ[ADD=yes] -> 'ca'
ADV[DEGREE=limited] -> 'bhūyasā'
ADJ[CASE=ins,NUM=pl,GEN=m] -> 'adṛṣṭatattvair'
ADJ[CASE=ins,NUM=pl,GEN=m] -> 'niravagrahaiḥ'
PTCP[CASE=nom,NUM=sg,GEN=n,TENSE=past,VOICE=pass] -> 'kṛtaṃ'
N[CASE=ins,NUM=pl,GEN=m,ROLE=agent] -> 'kutārkikaiḥ'
N[CASE=nom,NUM=sg,GEN=n,ROLE=patient] -> 'śāsanam'
PRON[CASE=nom,NUM=sg,GEN=n] -> 'etat'
ADJ[CASE=nom,NUM=sg,GEN=n] -> 'ākulam'
```

```nltk-dep
'śāstari' -> 'nimīlite' | 'lokacakṣuṣi'
'sākṣijane' -> 'kṣayaṃ' | 'gate' | 'ca' | 'bhūyasā'
'śāsanam' -> 'adṛṣṭatattvair' | 'niravagrahaiḥ' | 'kṛtaṃ' | 'kutārkikaiḥ' | 'etat' | 'ākulam'
```

No separate Bhāṣya prose supplements the verse, so no agent roster is added.
The claim is “largely” rather than total disappearance; it does not say that the teaching vanished or that reasoning as such is bad.
`Lokacakṣuṣi` is appositional to `śāstari`, not a second agent.
**Close construe.** With the Teacher, the Eye
of the World, closed, and the body
of witnesses largely passed away, this teaching
has been made confused by unchecked bad
reasoners who have not seen reality.

## 5. Translation

### Literal Translation

> With the Teacher, the Eye of the
> World, closed, and the body of witnesses
> largely passed away, this teaching has been
> made confused by unrestrained bad reasoners who
> have not seen reality.

### Bhāṣya-informed study translation

> With the Teacher, the Eye of the World, closed, and the body of
> witnesses largely passed away, this teaching has been made confused
> by unrestrained bad reasoners who have not seen reality.

## 6. Philosophical Translation

> Vasubandhu portrays the loss of the Teacher
> and most witnesses as the setting in
> which unchecked reasoning without sight of reality
> disorders the teaching. The criticism concerns the
> quality and discipline of the reasoning and
> the agents' lack of realization; it does
> not erase the distinction between reasoned exposition
> and sophistical dispute.

This is an interpretive reconstruction of the
closing polemic. The verse supplies no detailed
positive theory of the relation between inference,
testimony, and direct realization.

## 7. Technical Vocabulary

**`Śāstṛ / lokacakṣus`.** Teacher / Eye of
the World. The epithet gives the passing
of the Teacher the imagery of lost
vision. It is poetic and honorific here,
not a new technical faculty in the
previous analysis of cognition.

**`Nimīlita`.** Closed. Applied to the world-eye,
it evokes the Teacher's passing. Treating the
line as ordinary sleep would miss its
context beside the disappearance of witnesses.

**`Sākṣijana`.** Body or community of witnesses.
The contrast with those who have not
seen reality supports the relevance of direct
witnessing or realization. The verse does not
name a roster or settle whether every
witness was personally present during the Buddha's life.

**`Bhūyasā`.** Largely, for the most part.
The qualification prevents turning a lament over
great loss into an explicit assertion that
no witnesses whatever remain.

**`Adṛṣṭatattva`.** One who has not seen
reality or truth. “Uninformed” would weaken the
claimed contrast. The verse does not specify
a new list of objects constituting tattva.

**`Niravagraha`.** Unchecked, unrestrained. The adjective characterizes
the disputants. It does not identify a
particular institution or formal disciplinary rule that
has ceased to restrain them.

**`Kutārkika`.** Bad reasoner, sophistical disputant. The
pejorative compound is narrower than “reasoner” without
qualification; translating all reasoning as the target
would discard an explicit feature of the word.

**`Śāsana / ākula`.** Teaching or dispensation /
disordered. The result concerns the condition of
the teaching as expounded and sustained. Confusion
is not itself a statement of complete disappearance.

## 8. Logical Determination

**The verse's stated relations.**

| Feature | Determination |
|---|---|
| First circumstance | Passing of the Teacher, expressed through the closed world-eye |
| Second circumstance | Largely diminished body of witnesses |
| Agents of disorder | Bad reasoners, lacking sight of reality and restraint |
| Action and result | This teaching made confused |

The locative absolutes supply the setting. The
instrumentals explicitly identify the agents of the
main action. A larger causal theory about
institutions, historical periods, or transmission mechanisms would
require more than this grammatical structure.

**The judgment is attributed.** The verse presents
Vasubandhu's strongly evaluative closing voice. It does
not name the disputants or provide case-by-case
evidence for their alleged faults. The study
records the judgment without assigning it to
an unnamed contemporary group on its own authority.

**Bad reasoning is not reasoning without qualification.**
The ku- compound and its two adjectives
specify the target. This supports retaining a
distinction between critical argument and the reasoning
condemned here. It does not, by itself,
supply a full account of which arguments
are valid or how realization is to
be independently authenticated.

**Connection with the preceding two verses.** VAK 8.39
distinguished transmission and realization with their bearers;
8.40 distinguished expository method, error, and authority.
This verse laments disorder after the loss
of authoritative presence and most witnesses. The
connection is intelligible without treating the three
verses as a formal proof that every
later interpreter must necessarily be mistaken.

**Loss and disorder remain distinct.** The witnesses
have largely disappeared; the teaching has been
made confused. Neither predicate is identical to
the other. The verse leaves room for
remaining witnesses and does not state that
every transmitted teaching has become false.

## 9. Interpretive Note

**Verse-only source control.** The research file labeled
Bhāṣya contains this verse and modern study
analysis. The running source supplies no intervening
prose before 8.42. Consequently its diagrams and
positive claims about the indispensability of reason
are research interpretation, not transmitted commentary attributed
to Vasubandhu as separate prose.

**Limits of the research reconstruction.** The image
of reasoning answerable to living realization is
a useful reading of the contrast. “Self-authorizing
speculation” and “systemic failure” develop that reading;
they are not additional Sanskrit predicates. Likewise
the term sākṣijana does not justify silently
identifying all witnesses with one named group
of historical disciples.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā distinguishes textual claims, their interpretation,
and the grounds invoked for them. Yoga
Technē, its kriyā–karma companion, concerns disciplined practice
and correction in the exercise of those
capacities. The passage offers the project a
warning against confusing elaboration of an argument
with the realization that the argument discusses.

For the Organon, formal articulation and accountable
practice can remain related without being identified.
This is a project application. The verse
neither validates a later technical architecture nor
supplies a general prohibition on reasoning by
those still learning the path.

**Review status.** Provisional, source-controlled study of
a verse without a separate transmitted prose gloss.
The locative absolutes, world-eye image, partial-loss qualification,
instrumental agents, and polemical scope have been
checked against the local witnesses and running
source. The research originals remain untouched.

## 10. OWL++ Seed

```text
Class: ClosingVerseJudgment
Class: Circumstance
Class: AgentDescription
Class: ConditionOfTeaching

ObjectProperty: attributedTo
ObjectProperty: hasCircumstance
ObjectProperty: namesAgents
ObjectProperty: statesResult

PresentClosingJudgment:
    voice: Vasubandhu
    circumstances: TeacherPassedAway, WitnessCommunityLargelyPassedAway
    agents: UnrestrainedBadReasonersWithoutSightOfReality
    result: TeachingMadeDisordered

TeacherImage:
    epithet: EyeOfTheWorld
    passingExpressedAs: Closing

WitnessLoss:
    extent: ForTheMostPart
    namedRoster: NotSpecified

SourceStatus:
    transmittedUnit: Verse
    separateProseGloss: NoneInLocalRunningWitness

ProjectConstraint: Preserve the qualification on witness loss.
ProjectConstraint: Do not replace bad reasoners with all reasoners.
ProjectConstraint: Agent descriptions qualify the same instrumental group.
ProjectConstraint: Attributed polemic is not an independently verified historical inventory.
ProjectConstraint: Disordered teaching does not mean every teaching has disappeared.
ProjectConstraint: Research reconstruction is not a transmitted prose gloss.
```

This is a declarative project seed, not executable OWL.
VAK 8.42 next continues the lament over the
loss of the Teacher and bearers of the teaching.
