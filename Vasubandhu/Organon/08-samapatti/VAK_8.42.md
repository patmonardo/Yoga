# VAK_8.42 — The Loss of the Teaching's Bearers

## 1. Sanskrit (Devanāgarī)

```sanskrit
गतेऽथ शान्तिं परमां स्वयंभुवि स्वयंभुवः शासनधूर्धरेषु च ।
जगत्यनाथे गणघातिभिर्मतैर्निरङ्कुशैः स्वैरमिहाद्य चर्यते ॥ ८.४२ ॥
```

## 2. Sanskrit (IAST)

```text
gate 'tha śāntiṃ paramāṃ svayaṃbhuvi svayaṃbhuvaḥ śāsanadhūrdhareṣu ca |
jagaty anāthe gaṇaghātibhir matair niraṅkuśaiḥ svairam ihādya caryate || 8.42 ||
```

The local research verse is retained provisionally.
The running source prints śāsanadhurdhareṣu and gunaghātibhir,
where the local verse has śāsanadhūrdhareṣu and
gaṇaghātibhir. The latter difference affects the meaning:
“destructive of the community” depends on gaṇa.
The running spelling gunaghātibhir, does not by itself establish that reading.
There is no separate prose gloss in the
running source to settle the compound.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `gate` | locative singular past passive participle of √gam | having gone |
| `atha` | indeclinable | then; continuing the lament |
| `śāntim` | accusative singular feminine | peace, as the destination of going |
| `paramām` | accusative singular feminine superlative adjective | supreme |
| `svayaṃbhuvi` | locative singular of `svayaṃbhū` | when the Self-Arisen |
| `svayaṃbhuvaḥ` | genitive singular | of the Self-Arisen |
| `śāsanadhūrdhareṣu` | locative plural masculine compound | when the bearers of the teaching's burden |
| `jagati` | locative singular neuter of `jagat` | in the world |
| `anāthe` | locative singular adjective | without a protector |
| `gaṇaghātibhiḥ` | instrumental plural of a compound in `-ghātin` | destructive of the community, on the local reading |
| `mataiḥ` | instrumental plural neuter of `mata` | by views or doctrines |
| `niraṅkuśaiḥ` | instrumental plural adjective | unrestrained, without a check |
| `svairam` | adverbial accusative | freely, at will |
| `iha / adya` | indeclinables | here / now, today |
| `caryate` | third-person singular present passive of √car | impersonal: movement or activity takes place |

Sandhi: `jagati + anāthe` > `jagaty anāthe`; `iha +
adya` > `ihādya`. Text: the translations provisionally follow the local
`gaṇaghātin`; the running source (Pradhan 460|07–11) prints `gunaghātin`,
so the kind of harm remains unsettled. No separate prose gloss accompanies
the verse. The instrumental forms `gaṇaghātibhiḥ`,
mataiḥ, and niraṅkuśaiḥ undergo the displayed visarga
sandhi. Their shared case connects the description
of harm and lack of restraint to the views.

## 4. Grammar

The singular locative absolute belongs to the Self-Arisen; the teaching-bearers share an elided plural departure predicate. The world locative frames an impersonal passive, while the local `gaṇa` reading remains textually unsettled against the running witness.

```nltk-fcfg
% start S
# tokens: gate atha śāntiṃ paramāṃ svayaṃbhuvi svayaṃbhuvaḥ śāsanadhūrdhareṣu ∅-gateṣu ca jagaty anāthe gaṇaghātibhir mataiḥ niraṅkuśaiḥ svairam iha adya caryate
S[SEM=<?a & ?b & ?c>] -> CL[K=departures,SEM=?a] CL[K=world,SEM=?b] CL[K=activity,SEM=?c]

CL[K=departures,SEM=<GoneToPeace(selfarisen) & all b.(TeachingBearer(b) -> Departed(b))>] -> PTCP[CASE=?c,NUM=?n,GEN=?g,TENSE=past] PTCL[SEQUENCE=yes] N[CASE=acc,NUM=sg,GEN=f] ADJ[CASE=acc,NUM=sg,GEN=f] N[CASE=?c,NUM=?n,GEN=?g] N[CASE=gen,NUM=sg,GEN=m] N[CASE=loc,NUM=pl,GEN=m] PTCP[CASE=loc,NUM=pl,GEN=m,SUPPLIED=ellipsis] CONJ[ADD=yes]
CL[K=world,SEM=<Unprotected(world)>] -> N[CASE=?c,NUM=?n,GEN=?g] ADJ[CASE=?c,NUM=?n,GEN=?g,STATE=unprotected]
CL[K=activity,SEM=<all v.((View(v) & Unrestrained(v) & Unprotected(world)) -> RoamsHereNow(v))>] -> ADJ[CASE=?c,NUM=?n,GEN=?g,HARM=yes] N[CASE=?c,NUM=?n,GEN=?g,ROLE=agent] ADJ[CASE=?c,NUM=?n,GEN=?g,RESTRAINT=no] ADV[FREE=yes] ADV[PLACE=here] ADV[TIME=now] VERB[PERS=3,NUM=sg,TENSE=pres,VOICE=pass,MOOD=indicative]

PTCP[CASE=loc,NUM=sg,GEN=m,TENSE=past] -> 'gate'
PTCL[SEQUENCE=yes] -> 'atha'
N[CASE=acc,NUM=sg,GEN=f] -> 'śāntiṃ'
ADJ[CASE=acc,NUM=sg,GEN=f] -> 'paramāṃ'
N[CASE=loc,NUM=sg,GEN=m] -> 'svayaṃbhuvi'
N[CASE=gen,NUM=sg,GEN=m] -> 'svayaṃbhuvaḥ'
N[CASE=loc,NUM=pl,GEN=m] -> 'śāsanadhūrdhareṣu'
PTCP[CASE=loc,NUM=pl,GEN=m,SUPPLIED=ellipsis] -> '∅-gateṣu'
CONJ[ADD=yes] -> 'ca'
N[CASE=loc,NUM=sg,GEN=n] -> 'jagaty'
ADJ[CASE=loc,NUM=sg,GEN=n,STATE=unprotected] -> 'anāthe'
ADJ[CASE=ins,NUM=pl,GEN=n,HARM=yes] -> 'gaṇaghātibhir'
N[CASE=ins,NUM=pl,GEN=n,ROLE=agent] -> 'mataiḥ'
ADJ[CASE=ins,NUM=pl,GEN=n,RESTRAINT=no] -> 'niraṅkuśaiḥ'
ADV[FREE=yes] -> 'svairam'
ADV[PLACE=here] -> 'iha'
ADV[TIME=now] -> 'adya'
VERB[PERS=3,NUM=sg,TENSE=pres,VOICE=pass,MOOD=indicative] -> 'caryate'
```

```nltk-dep
'gate' -> 'atha' | 'śāntiṃ' | 'paramāṃ' | 'svayaṃbhuvi'
'śāsanadhūrdhareṣu' -> 'svayaṃbhuvaḥ' | '∅-gateṣu' | 'ca'
'jagaty' -> 'anāthe'
'caryate' -> 'gaṇaghātibhir' | 'mataiḥ' | 'niraṅkuśaiḥ' | 'svairam' | 'iha' | 'adya'
```

The verse does not name a school or give separate prose to settle `gaṇa`/`guṇa`; the dependency tree preserves the local reading without suppressing the variant.
The plural `∅-gateṣu` is ellipsis, not the form of the overt `gate`.
Genitive `svayaṃbhuvaḥ` identifies whose teaching is borne; singular `caryate` remains impersonal.
**Close construe.** With the Self-Arisen gone to
supreme peace, and the bearers of his
teaching also departed, in a world without
a protector, there is now free roaming
by unrestrained views destructive of the community—if
the local gaṇa reading is retained.

## 5. Translation

### Literal Translation

> Then, with the Self-Arisen gone to supreme
> peace, and the bearers of the Self-Arisen's
> teaching also departed, in a world without
> a protector, there is free roaming here
> now by unrestrained views destructive of the community.

### Bhāṣya-informed study translation

> Then, with the Self-Arisen gone to supreme peace, and the bearers of the
> Self-Arisen's teaching also departed, in a world without a protector,
> unrestrained views destructive of the community now roam freely here.

## 6. Philosophical Translation

> The lament associates the departure of the
> Teacher and those who sustained his teaching
> with a loss of protection. In that
> condition, views characterized as harmful and unchecked
> move freely. The verse expresses the author's
> judgment about the teaching's vulnerability after its
> bearers have gone.

This reconstruction leaves the precise object of
harm open because of the witness discrepancy.
It does not turn doctrinal plurality as such
into the target of the verse.

## 7. Technical Vocabulary

**`Svayaṃbhū`.** Self-Arisen, an epithet of the
Buddha in this context. It is not
an argument here for a creator deity or
a new cosmological account of the Buddha's origin.

**`Paramā śāntiḥ`.** Supreme peace. In this
closing sequence it characterizes the Teacher's final
departure. It does not describe an ordinary
pause in teaching or a temporary meditative session.

**`Śāsanadhūrdhara`.** Bearer of the burden or
yoke of the teaching. The local spelling
with long ū is retained, while the
running dhurdhara is recorded. Both witnesses place
the expression in the teaching-bearer context.

**`Anātha`.** Without a protector or guardian.
The world is described through the loss
of protective presence, not merely through a
private feeling of loneliness.

**`Mata`.** View, opinion, or doctrine. The
negative force comes from its modifiers in
this sentence; mata itself does not mean
a false or destructive doctrine in every context.

**`Gaṇaghātin / running gunaghātin`.** The local
reading means destructive of the group or
community. The running form is unresolved. A
possible guṇa-ghātin would instead concern destruction of
good qualities or virtues, but that is
a candidate reading, not an established correction
from an independently checked edition here.

**`Niraṅkuśa`.** Without a goad or check;
figuratively unrestrained. The restraint image does not
specify a particular institution or disciplinary mechanism.

**`Svairam / ihādya`.** Freely or at will /
here now. The temporal voice is that
of the verse's speaker. It is not
a date supplied by the modern study.

## 8. Logical Determination

The verse continues the lament: the Self-Arisen and teaching-bearers have departed; views roam unchecked in the unprotected world. The derived formula retains the world condition in the roaming rule. The target of the compound is textually unstable (`gaṇa`/`guṇa`), so the formalization records only claims common to the witness readings. `[verse]`; no separate Bhāṣya prose resolves the variant.

**Signature.** `GoneToPeace(x)`, `TeachingBearer(x)`, `Departed(x)`, `Unprotected(x)`, `View(x)`, `Unrestrained(x)`, and `RoamsHereNow(x)`.

```nltk-sem
# derived by the section 4 parse, not typed by hand
GoneToPeace(selfarisen) & all b.(TeachingBearer(b) -> Departed(b)) & Unprotected(world) & all v.((View(v) & Unrestrained(v) & Unprotected(world)) -> RoamsHereNow(v))
```

```nltk-valuation
selfarisen => selfarisen
bearergroup => bearergroup
world => world
views => views
GoneToPeace => {selfarisen}
TeachingBearer => {bearergroup}
Departed => {bearergroup}
Unprotected => {world}
View => {views}
Unrestrained => {views}
RoamsHereNow => {views}
```

```nltk-fol
# THEORY verse
# [verse] departure clauses and the unprotected-world roaming claim
GoneToPeace(selfarisen) & all b.(TeachingBearer(b) -> Departed(b)) & Unprotected(world) & all v.((View(v) & Unrestrained(v) & Unprotected(world)) -> RoamsHereNow(v))
```

**Results (NLTK).** The checker reports the common-core verse theory true in this finite model. The disputed compound's specific harm-target was deliberately not tested.

**Scope cautions.** Neither `HarmsCommunity` nor `HarmsVirtue` is asserted: the former depends on the local *gaṇa* reading, while the latter is only a possible construal of the running form. No school or class of views is named. The truth of the common lament does not settle the textual variant.

## 9. Interpretive Note

**A material witness difference.** The local research
recognizes the running gunaghātibhir but still translates
community-destruction confidently. The official study retains
that local reading only provisionally. Neither gaṇa
nor a possible guṇa is silently installed
as the unquestionably transmitted form across witnesses.
A critically established reading remains needed to
settle the exact kind of harm named.

**No separate prose explanation.** The research Bhāṣya
file includes a modern argument reconstruction, but
the running source moves directly to 8.43.
Its claims about communal fragmentation and regulating
centers are therefore research interpretations, not an
additional ancient prose gloss accompanying this verse.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates the claims and criteria
through which a teaching is understood. Yoga
Technē, its kriyā–karma companion, concerns the effective
practices by which its bearers sustain and
correct that understanding. The burden-bearing image offers
a useful comparison for accountable continuation of
a body of study and practice.

A broader Organon account of institutions and
correction can develop this comparison. It should
not depend on treating the disputed gaṇa
reading as settled or attributing a full
theory of system governance to this brief lament.

**Review status.** Provisional, source-controlled verse study.
The locative constructions, departure ellipsis, burden-bearing image,
impersonal verb, and absence of a prose
gloss have been checked against the local
witnesses and running source. The gaṇa/gunaghātin
difference remains an explicit philological uncertainty. Research
originals remain untouched.

## 10. OWL++ Seed

```text
Class: ClosingLament
Class: TeachingBearer
Class: HarmfulViewDescription
Class: TextualReading

ObjectProperty: attributedTo
ObjectProperty: hasCircumstance
ObjectProperty: qualifiedBy
ObjectProperty: dependsOnReading

PresentLament:
    voice: Vasubandhu
    circumstances: TeacherGoneToSupremePeace, TeachingBearersDeparted
    worldCondition: WithoutProtector
    describedActivity: UncheckedViewsCirculateFreely

LocalGanaReading:
    harmObject: Community
    status: ProvisionalLocalWitnessReading

RunningGunaSpelling:
    exactPrintedForm: gunaghatibhir
    interpretationStatus: Unresolved

CommunityFragmentationInterpretation:
    dependsOn: LocalGanaReading
    layer: ResearchInterpretation

SourceStatus:
    transmittedUnit: Verse
    separateProseGloss: NoneInLocalRunningWitness

ProjectConstraint: Preserve the consequential witness discrepancy.
ProjectConstraint: Candidate guna reading is not an established emendation.
ProjectConstraint: Mata is not intrinsically a negative term.
ProjectConstraint: Do not identify unnamed targets with a modern or historical group.
ProjectConstraint: Here-now belongs to the verse speaker's temporal voice.
ProjectConstraint: Governance comparison remains Organon reconstruction.
```

This is a declarative project seed, not executable OWL.
VAK 8.43 next concludes the chapter with an
exhortation to vigilance for those seeking liberation.
