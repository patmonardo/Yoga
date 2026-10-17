# VAK_8.43 — The Liberation-Seeker Must Not Be Negligent

## 1. Sanskrit (Devanāgarī)

```sanskrit
इति कण्ठगतप्राणं विदित्वा शासनं मुनेः ।
बलकालं मलानां च न प्रमाद्यं मुमुक्षुभिः ॥ ८.४३ ॥
```

## 2. Sanskrit (IAST)

```text
iti kaṇṭhagataprāṇaṃ viditvā śāsanaṃ muneḥ |
balakālaṃ malānāṃ ca na pramādyaṃ mumukṣubhiḥ || 8.43 ||
```

The local scripts agree with the running verse.
No separate prose gloss follows it. The source
next supplies the colophon closing the eighth
Kośasthāna, the exposition of attainments.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `iti` | indeclinable | thus, taking up the preceding account |
| `kaṇṭhagataprāṇam` | accusative singular neuter possessive compound | with life-breath gone to the throat |
| `viditvā` | absolutive of √vid | having known, having understood |
| `śāsanam` | accusative singular neuter | the teaching or dispensation |
| `muneḥ` | genitive singular masculine of `muni` | of the Sage |
| `balakālam` | accusative singular masculine compound | a time of strength |
| `malānām` | genitive plural neuter of `mala` | of the stains or defilements |
| `ca` | conjunction | and |
| `na` | negative particle | not |
| `pramādyam` | neuter singular gerundive used impersonally, from pra-√mad | negligence is to be avoided; one must not be negligent |
| `mumukṣubhiḥ` | instrumental plural of `mumukṣu` | by those desiring liberation |

Kaṇṭha-gata-prāṇa describes the teaching through a
bodily image. Mumukṣu is a desiderative formation
related to √muc, “release”: its sense is
one who wishes to be liberated, not
one whose liberation is already asserted. Source: Pradhan
460|12–14; the verse occupies the first two numbered lines, the final line
is the chapter colophon, and there is no separate prose gloss.

## 4. Grammar

The absolutive takes two coordinated contents: the Sage's precarious teaching and a time of strength for the defilements. Its implicit knowers are unified with the liberation-seekers who bear the impersonal gerundive obligation.

```nltk-fcfg
% start S
# tokens: iti kaṇṭhagataprāṇaṃ viditvā śāsanaṃ muneḥ ∅-etam balakālaṃ malānāṃ ca na pramādyam mumukṣubhiḥ
S[SEM=<?rule(?condition)>] -> CL[K=knowing,AGENT=seekers,COND=?condition] CL[K=injunction,AGENT=seekers,SEM=?rule]

CL[K=knowing,AGENT=seekers,COND=<\x.(Knows(x,riskcondition) & TeachingAtRisk(riskcondition) & DefilementsStrong(riskcondition))>] -> PTCL[REPORT=yes] ADJ[CASE=acc,NUM=?n,GEN=?g,CONTENT=teaching,SEM=?teaching] ABS[COMP=knowing,TENSE=prior,SEM=?know] N[CASE=acc,NUM=?n,GEN=?g,CONTENT=teaching] N[CASE=gen,NUM=sg,GEN=m,OWNER=sage] PRON[CASE=acc,NUM=sg,GEN=m,SUPPLIED=prose] N[CASE=acc,NUM=sg,GEN=m,CONTENT=time,SEM=?strength] N[CASE=gen,NUM=pl,GEN=n,OWNER=defilements] CONJ[ADD=yes]
CL[K=injunction,AGENT=seekers,SEM=<\P.all x.((?seek(x) & P(x)) -> ?ought(x))>] -> NEG[POLARITY=no] VERB[CASE=nom,NUM=sg,GEN=n,MOOD=gerundive,VOICE=impersonal,SEM=?ought] N[CASE=ins,NUM=pl,GEN=m,ROLE=agent,AGENT=seekers,SEM=?seek]

PTCL[REPORT=yes] -> 'iti'
ADJ[CASE=acc,NUM=sg,GEN=n,CONTENT=teaching,SEM=<\c.TeachingAtRisk(c)>] -> 'kaṇṭhagataprāṇaṃ'
ABS[COMP=knowing,TENSE=prior,SEM=<\P.\x.(Knows(x,riskcondition) & P(x))>] -> 'viditvā'
N[CASE=acc,NUM=sg,GEN=n,CONTENT=teaching] -> 'śāsanaṃ'
N[CASE=gen,NUM=sg,GEN=m,OWNER=sage] -> 'muneḥ'
PRON[CASE=acc,NUM=sg,GEN=m,SUPPLIED=prose] -> '∅-etam'
N[CASE=acc,NUM=sg,GEN=m,CONTENT=time,SEM=<\c.DefilementsStrong(c)>] -> 'balakālaṃ'
N[CASE=gen,NUM=pl,GEN=n,OWNER=defilements] -> 'malānāṃ'
CONJ[ADD=yes] -> 'ca'
NEG[POLARITY=no] -> 'na'
VERB[CASE=nom,NUM=sg,GEN=n,MOOD=gerundive,VOICE=impersonal,SEM=<\x.OughtNotNeglect(x)>] -> 'pramādyam'
N[CASE=ins,NUM=pl,GEN=m,ROLE=agent,AGENT=seekers,SEM=<\x.LiberationSeeker(x)>] -> 'mumukṣubhiḥ'
```

```nltk-dep
'viditvā' -> 'iti' | 'kaṇṭhagataprāṇaṃ' | 'śāsanaṃ' | 'muneḥ' | '∅-etam' | 'balakālaṃ' | 'malānāṃ' | 'ca'
'pramādyam' -> 'na' | 'mumukṣubhiḥ'
```

`Muneḥ` belongs with `śāsanam`, while `malānām` belongs with `balakālam`; the added demonstrative resolves the second content as “this [time].” `Mumukṣubhiḥ` identifies both the implied knowers and the agents of the injunction; liberation is desired, not already attained.
**Close construe.** Having understood the Sage's teaching
thus to have its life-breath at the
throat, and this to be a time
of strength for defilements, those who desire
liberation must not be negligent.

## 5. Translation

### Literal Translation

> Having thus known the Sage's teaching to
> have its life-breath at the throat, and
> this to be a time of strength
> for the defilements, those desiring liberation must
> not be negligent.

### Bhāṣya-informed study translation

> Having thus known the Sage's teaching to be near death, with its
> life-breath at the throat, and this to be a time of strength for the
> defilements, those who wish for liberation must not be negligent.

## 6. Philosophical Translation

> The closing lament becomes an obligation for
> the person seeking liberation. The precarious state
> of the teaching and the strength of
> defilements are presented as reasons for vigilance.
> Understanding these conditions is directed toward how
> one must practice, rather than left as
> a description of decline alone.

This reconstructs the verse's exhortative movement. It
does not claim that negligence is thereby
eliminated, or that vigilance by itself exhausts
all the conditions of liberation.

## 7. Technical Vocabulary

**`Kaṇṭhagataprāṇa`.** With life-breath at the throat;
idiomatically at the point of death. The
bodily image represents the teaching's precarious condition.
It should retain its urgency without becoming
a claim that the teaching is already wholly extinct.

**`Śāsanaṃ muneḥ`.** The Sage's teaching or dispensation.
In the closing context the Sage is
the Buddha. Śāsana includes the teaching being
sustained and practiced, not merely one physical
manuscript whose survival is at issue.

**`Balakāla`.** Time or season of strength.
The genitive malānām identifies what is strong.
The verse does not provide a calendrical
scheme or a quantified measure of that strength.

**`Mala`.** Stain, impurity, defilement. The plural
has a collective force here. It does
not introduce a newly enumerated list of
kleśas or identify one named defilement as
the sole threat to liberation.

**`Pramāda / na pramādyam`.** Negligence or heedlessness /
one must not be negligent. The verse's
form is injunctive. “Vigilance” gives its positive
practical implication; the explicit wording prohibits heedlessness.

**`Mumukṣu`.** One who desires liberation. The
addressee is determined by that aim. The
term does not by itself assign a
particular noble-person status or assert that the
person has completed the path.

**`Viditvā`.** Having known or recognized. It
connects awareness of the described conditions to
the following obligation. Here it is not
a separate classification of jñāna or a
new knowledge-attainment added to the preceding chapters.

## 8. Logical Determination

The closing verse links recognition of two conditions—the Sage's teaching at the point of death and a time of strength for the defilements—to an injunction against negligence for liberation-seekers. `[verse]`; no separate Bhāṣya prose follows. The norm is represented as a predicate because ordinary FOL has no deontic operator here.

**Signature.** `LiberationSeeker(x)`, `Knows(x,c)`, `TeachingAtRisk(c)`, `DefilementsStrong(c)`, and `OughtNotNeglect(x)`.

```nltk-sem
# derived by the section 4 parse, not typed by hand
all x.((LiberationSeeker(x) & Knows(x,riskcondition) & TeachingAtRisk(riskcondition) & DefilementsStrong(riskcondition)) -> OughtNotNeglect(x))
```

```nltk-valuation
seekerone => seekerone
riskcondition => riskcondition
LiberationSeeker => {seekerone}
Knows => {(seekerone,riskcondition)}
TeachingAtRisk => {riskcondition}
DefilementsStrong => {riskcondition}
OughtNotNeglect => {seekerone}
```

```nltk-fol
# THEORY verse
# [verse] recognition of both conditions governs the injunction
all x.((LiberationSeeker(x) & Knows(x,riskcondition) & TeachingAtRisk(riskcondition) & DefilementsStrong(riskcondition)) -> OughtNotNeglect(x))
```

**Results (NLTK).** The checker reports the rule true in the finite model. This verifies model satisfaction only; no deontic theorem prover or entailment check was run.

**Scope cautions.** The rule states an obligation, not that a seeker actually avoids negligence or has attained liberation. `Balakāla` supplies no calendar measure. The imperative does not reduce the preceding chapter's attainment taxonomy to the path in its entirety.

## 9. Interpretive Note

**Source voice.** Vasubandhu's closing voice is directly
exhortative. The description of decline belongs to
that voice; the study does not convert
it into an independently verified assessment of
the present historical period.

**No added prose doctrine.** The research file
labeled Bhāṣya supplies the verse, colophon, and
modern analysis. Its statement that doctrinal mastery
is “subordinated” to vigilance is a research
interpretation. The source explicitly commands non-negligence;
it does not formulate a separate hierarchy
in which knowledge or classification loses its value.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates the conditions and distinctions
that study makes intelligible. Yoga Technē, its
kriyā–karma companion, concerns their effective bearing on
practice. The closing connection between viditvā and
na pramādyam offers the project a precise
point of contact: recognized conditions inform an
obligation for the agent seeking liberation.

For the Organon, completion of an articulated
study and accomplishment of its practical aim
remain different determinations. Completing these chapter files
is an editorial result, not evidence of
the compiler's or reader's liberation. This distinction
preserves the verse's practical address without replacing
its Buddhist content with a generic productivity rule.

**Colophon.** The running source closes with:

```text
abhidharmakośabhāṣye samāpattīnirdeśo nāmāṣṭamakośasthānam iti
```

Thus ends the eighth Kośasthāna, called the
Exposition of Attainments, in the Abhidharmakośabhāṣya.
The source's samāpattīnirdeśa spelling is retained in
the quotation; the chapter title elsewhere follows
the project's Samāpattinirdeśa convention.

**Review status.** Provisional, source-controlled verse study.
The breath metaphor, coordinated objects of knowing,
gerundive obligation, desiderative addressee, absence of a
prose gloss, and chapter colophon have been
checked against the local witnesses and running
source. Earlier flagged textual questions remain open
for critical review. Research originals remain untouched.

## 10. OWL++ Seed

```text
Class: ClosingExhortation
Class: RecognizedCondition
Class: PracticalObligation
Class: LiberationSeeker
Class: ChapterColophon

ObjectProperty: addressedTo
ObjectProperty: takesAccountOf
ObjectProperty: enjoins

FinalChapterEightExhortation:
    voice: Vasubandhu
    addressedTo: ThoseDesiringLiberation
    recognizedConditions: TeachingNearDeath, DefilementsInSeasonOfStrength
    injunction: DoNotBeNegligent

TeachingNearDeathImage:
    literalImage: LifeBreathAtThroat
    force: ExtremePrecariousness

ChapterClosure:
    chapterNumber: 8
    title: SamapattiNirdesa
    work: Abhidharmakosabhasya
    followingSourceUnit: NinthKosasthana

SourceStatus:
    transmittedUnit: VerseFollowedByColophon
    separateProseGloss: NoneInLocalRunningWitness

ProjectConstraint: Near death is not already complete extinction.
ProjectConstraint: Desire for liberation does not assert attained liberation.
ProjectConstraint: Injunction does not report accomplished freedom from negligence.
ProjectConstraint: Vigilance is not presented as an exhaustive replacement for path analysis.
ProjectConstraint: Chapter closure does not close every unit of the running source.
ProjectConstraint: Editorial completion and practical realization remain distinct.
```

This is a declarative project seed, not executable OWL.
VAK 8.43 completes the Chapter 8 verse sequence.
