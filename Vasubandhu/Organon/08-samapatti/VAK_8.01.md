# VAK_8.01 — Dhyāna as Attainment and the Question of Collectedness

## 1. Sanskrit (Devanāgarī)

```sanskrit
द्विधा ध्यानानि चत्वारि प्रोक्तास्तदुपपत्तयः ।
समापत्तिः शुभैकाग्र्यं पञ्चस्कन्धास्तु सानुगम् ॥ ८.०१ ॥
```

## 2. Sanskrit (IAST)

```text
dvidhā dhyānāni catvāri proktās tadupapattayaḥ |
samāpattiḥ śubhaikāgryaṃ pañcaskandhās tu sānugam || 8.01 ||
```

The Sanskrit follows the normalized reading already
adopted in the local kārikā study. The running source
has `śubhaikāgyraṃ`; `śubhaikāgryaṃ` corrects the
transposed consonants, with the prose's `kuśalacittaikāgratā`
controlling the meaning. This normalization is disclosed,
not presented as a mechanically identical transcription.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `dvidhā` | adverb | twofold, as birth and attainment |
| `dhyānāni` | nominative plural neuter | dhyānas |
| `catvāri` | nominative plural neuter numeral | four |
| `proktāḥ` | nominative plural feminine participle (with `proktās tad-` sandhi) | already explained; agrees with the rebirths, not with neuter `dhyānāni` |
| `tad-upapattayaḥ` | nominative plural feminine compound | the births corresponding to those dhyānas |
| `samāpattiḥ` | nominative singular feminine | attainment, here attainment-dhyāna |
| `śubha-ekāgryam` | nominative singular neuter compound (`śubha + ekāgrya` → `śubhaikāgrya`) | wholesome one-pointedness |
| `pañca-skandhāḥ` | nominative plural masculine | the five Bases |
| `tu` | particle | contrast: defining nature versus accompanied constitution |
| `sa-anugam` | neuter singular compound adjective (`sa + anuga` → `sānuga`) | with its accompaniment |

## 4. Grammar

Case, number, and gender unify across the clauses; the definition is local to
attainment-dhyāna. The §4 parse composes only that definitional clause; the
classification and five-Base tally remain non-semantic.

```nltk-fcfg
% start S
# tokens: dvidhā dhyānāni catvāri proktāḥ tadupapattayaḥ samāpattiḥ śubhaikāgryam pañcaskandhāḥ tu sānugam ∅-samāpattidhyānam
S[SEM=?definition] -> CL[K=classify] CL[K=state] CL[K=define,SEM=?definition] CL[K=contrast]
CL[K=classify] -> ADV[MODE=twofold] N[CASE=nom,NUM=?n,GEN=?g] NUMR[NUM=?n,GEN=?g]
CL[K=state] -> PTCP[CASE=nom,NUM=?n,GEN=?g,TENSE=past] N[CASE=nom,NUM=?n,GEN=?g]
CL[K=define,SEM=<?subject(?property)>] -> N[CASE=nom,NUM=sg,GEN=f,LOCAL=yes,SEM=?subject] N[CASE=nom,NUM=sg,GEN=n,SEM=?property]
CL[K=contrast] -> N[CASE=nom,NUM=pl,GEN=m] PTCL[CONTRAST=yes] ADJ[GEN=?g] N[GEN=?g,SUPPLIED=prose]
ADV[MODE=twofold] -> 'dvidhā'
N[CASE=nom,NUM=pl,GEN=n] -> 'dhyānāni'
NUMR[NUM=pl,GEN=n] -> 'catvāri'
PTCP[CASE=nom,NUM=pl,GEN=f,TENSE=past] -> 'proktāḥ'
N[CASE=nom,NUM=pl,GEN=f] -> 'tadupapattayaḥ'
N[CASE=nom,NUM=sg,GEN=f,LOCAL=yes,SEM=<\P.all x.(SamapattiDhyana(x) -> P(x))>] -> 'samāpattiḥ'
N[CASE=nom,NUM=sg,GEN=n,SEM=<\x.exists c.(Kusala(c) & Ekagra(c) & Constitutes(c,x))>] -> 'śubhaikāgryam'
N[CASE=nom,NUM=pl,GEN=m] -> 'pañcaskandhāḥ'
PTCL[CONTRAST=yes] -> 'tu'
ADJ[GEN=n] -> 'sānugam'
N[GEN=n,SUPPLIED=prose] -> '∅-samāpattidhyānam'
```

```nltk-dep
'dhyānāni' -> 'dvidhā' | 'catvāri'
'proktāḥ' -> 'tadupapattayaḥ'
'śubhaikāgryam' -> 'samāpattiḥ'
'pañcaskandhāḥ' -> 'tu' | 'sānugam'
```

The supplied head restricts the definition to attainment-dhyāna. `sānugam`
agrees with that neuter supplied head, not with feminine `samāpattiḥ`.

**Close construe.** The four dhyānas are twofold. Their corresponding
births have been explained. As attainment, dhyāna is wholesome
one-pointedness; with its accompaniment, however, it has the constitution
of the five Bases.

## 5. Translation

### Literal Translation

> The four dhyānas are twofold; their corresponding
> births have been explained. Attainment is wholesome
> one-pointedness; with its accompaniment, however,
> it is the five Bases.

### Bhāṣya-informed study translation

> The four dhyānas are twofold, as corresponding rebirths
> and as attainment; the rebirths have been explained.
> Attainment-dhyāna is wholesome one-pointedness of mind;
> taken with its accompaniment, however, it has the
> nature of the five Bases.

## 6. Philosophical Translation

> The attainment has a defining cognitive determination
> and a fuller accompanied constitution. Its unity is
> then examined: does collectedness name the minds
> themselves, or a distinct factor through which they
> operate one-pointedly? The exposition preserves both
> positions and tests the meaning of unity rather than
> treating one object as a sufficient explanation of dhyāna.

The excellence receiving the dhyāna designation is
explained through its factors and through tranquillity
and insight operating together. The passage connects
collected mind with knowing things as they are.

## 7. Technical Vocabulary

**`Upapattidhyāna / samāpattidhyāna`.** Dhyāna as
corresponding birth and as meditative attainment. The
first belongs to the already given cosmological account;
the second is the present focus. Attaining dhyāna and
being reborn in its corresponding domain are not identical.

**`Kuśalacittaikāgratā`.** Wholesome one-pointedness of
mind, the prose expansion of `śubhaikāgrya`. The ethical
qualification is part of the definition, not an optional
adjective added after concentration has been defined.

**`Ekālambanatā`.** Having one object-support. This
explains `ekāgratā`, but immediately raises the question
whether samādhi is distinct from the minds so supported.
The definition initiates argument rather than settling
all questions of cognitive constitution.

**`Caitasika dharmāntara`.** A distinct mental factor.
The dispute asks whether samādhi is such a factor or
the one-pointed minds themselves. It is not a dispute
about whether collected cognition occurs at all.

**`Mahābhūmika`.** A mental factor counted as occurring
throughout minds in the position under discussion.
The objection asks whether universal samādhi would imply
universal developed collectedness; the reply invokes
weakness of samādhi. Presence and strength are distinguished.

**`Saparivāra / sānuga`.** With accompaniment or retinue.
The accompanied dhyāna is five-Base in constitution.
The passage does not enumerate every accompanying dharma
here or turn the five Bases into five dhyāna factors.

**`Aṅgasamāyukta`.** Endowed with factors. This identifies
the excellent samādhi to which the name dhyāna applies
in the ensuing explanation. The detailed factor analysis
must be allowed to develop in the following verses.

**`Śamatha / vipaśyanā`.** Tranquillity and insight.
Their yoked operation explains the excellent attainment's
pleasant abiding here and now and its happy mode of
progress. Neither is silently replaced by a project
faculty or an external philosophical category.

**`Yathābhūtaprajñāna`.** Knowing things as they are.
The prose uses the collected mind's capacity for such
knowing to explain `dhyāyanti` through `prajānanti`.
This is an attributed lexical-doctrinal explanation,
not a claim that every form of attention is liberating insight.

## 8. Logical Determination

Feature grammar (§4) yields syntax; this section composes it into logic.
Each lexical entry carries a lambda `SEM`; beta-reduction over the §4 parse
gives the formula. Provenance tags: `[verse]`, `[prose]` (Bhāṣya-supplied),
and the speaker of a position. In NLTK a single letter plus digits (`c1`) is a
variable, so individual constants carry longer names (`mind1`).

**Signature.** `Dhyana(x)` (four), `SamapattiDhyana(x)` (the attainment
respect), `Citta(c)`, `Kusala(c)`, `Ekagra(c)`, `Constitutes(c,x)`,
`Retinue(p,x)`, `FiveBases(p)`, `Samadhi(s)`, `Factor(s)`, `By(c,s)`,
`Excellent(s)`, `Yoked(s)` (tranquillity and insight together), `Named(x,n)`.

**Composition (the definitional clause, `K=define`).** The two lexical meanings
combine under the clause rule; the outer quantifier restricts the assertion to
attainment-dhyāna.

```nltk-sem
# derived by the section 4 parse, not typed by hand
all x.(SamapattiDhyana(x) -> exists c.(Kusala(c) & Ekagra(c) & Constitutes(c,x)))
```

**Facts (extension of the Dataset).** The table of questions becomes a
`Valuation`: rows in a frame, one relation per column. The model is a witness
for `shared` plus the `vaibhāṣika` theory: one attainment-dhyāna `att1`, its
one-pointed wholesome mind `mind1`, and a distinct weak factor `sam1`. It
makes the `apare` rule false (`mind1` is a `Citta` and `Ekagra` but not
`Samadhi`), which is the dispute seen from the Dataset side.

```nltk-valuation
first => first
second => second
third => third
fourth => fourth
birth => birth
attainment => attainment
dhyana => dhyana
att1 => att1
mind1 => mind1
sam1 => sam1
ret1 => ret1
Dhyana => {first, second, third, fourth, att1}
Respect => {(first, birth), (first, attainment), (second, birth), (second, attainment), (third, birth), (third, attainment), (fourth, birth), (fourth, attainment), (att1, birth), (att1, attainment)}
SamapattiDhyana => {att1}
Kusala => {mind1}
Ekagra => {mind1}
Constitutes => {(mind1, att1)}
Retinue => {(ret1, att1)}
FiveBases => {ret1}
Citta => {mind1}
Samadhi => {sam1}
Factor => {sam1}
By => {(mind1, sam1)}
Occurs => {(sam1, mind1)}
Weak => {sam1}
Developed => {attainment}
Named => {(sam1, dhyana)}
Excellent => {sam1}
Yoked => {sam1}
Afflicted => {}
Resembles => {}
```

**Rules (verse and prose).**

```nltk-fol
# THEORY shared
# [verse] dvidhā: each of the four is considered in both respects
all x.(Dhyana(x) -> (Respect(x,birth) & Respect(x,attainment)))
# [verse] samāpattiḥ śubhaikāgryam; [prose] ∅-samāpattidhyānam
all x.(SamapattiDhyana(x) -> Dhyana(x))
all x.(SamapattiDhyana(x) -> exists c.(Kusala(c) & Ekagra(c) & Constitutes(c,x)))
# [verse] pañcaskandhās tu sānugam; [prose] saparivāra
all x.(SamapattiDhyana(x) -> exists p.(Retinue(p,x) & FiveBases(p)))
```

**Theories (one per attributed position; never merged).**

```nltk-fol
# THEORY vaibhāṣika — samādhi is the dharma by which minds are one-pointed
all c.(Citta(c) -> -Samadhi(c))
all c.(Ekagra(c) -> exists s.(Samadhi(s) & Factor(s) & By(c,s)))
all s.(Factor(s) -> -Citta(s))
# the weakness reply: universal occurrence does not give developed strength
all c.(Citta(c) -> exists s.(Samadhi(s) & Occurs(s,c)))
exists s.(Samadhi(s) & Weak(s))
all s.(Weak(s) -> -Developed(s))

# THEORY apare — the one-pointed minds themselves are samādhi
all c.((Citta(c) & Ekagra(c)) -> Samadhi(c))
```

**Naming and the afflicted case.**

```nltk-fol
# THEORY shared
# [prose] bhāskara: the name dhyāna is reserved for the excellent samādhi
all s.(Named(s,dhyana) -> (Samadhi(s) & Excellent(s)))
all s.(Excellent(s) <-> (Samadhi(s) & Factor(s) & Yoked(s)))
# [prose] afflicted dhyāna: named by resemblance (rotten seed), not by definition
all a.((Afflicted(a) & Named(a,dhyana)) -> (Resembles(a,dhyana) & -SamapattiDhyana(a)))
```

**Consistency results (NLTK `ResolutionProver`).** The definition entails
`exists c.(Kusala(c) & Ekagra(c))` from any attainment-dhyāna. The vaibhāṣika
and `apare` theories are each consistent with a one-pointed mind `mind1`; their
union is contradictory, because the first denies that any `Citta` is `Samadhi`
and the second asserts it. This is the formal content of “not harmonized into
one doctrine”: the dispute is whether the explanatory entity is a distinct
factor, not a difference of wording.

**Scope cautions.**
- `sarvaguṇāśrayatvāt` is restricted to the qualities treated under knowledge
  (`all q.(Quality7(q) -> Supports(dhyana,q))`); the inflated reading
  `all q.(Property(q) -> DerivesFrom(q,samadhi))` is not asserted.
- The momentariness and non-distraction exchange is not assigned to further
  speakers beyond what the Bhāṣya secures; the weakness reply stands only
  as stated.
- Afflicted naming does not remove `kusala` from the definition: the
  last rule leaves `SamapattiDhyana` untouched.
- The `apare` appeal (higher-mind training, purification of mind) is
  evidence offered by that position, not a premise of the vaibhāṣika theory.

## 9. Interpretive Note

**Definition and accompaniment.** “Five Bases” must
not erase the defining samādhi determination, while
“one-pointedness” must not erase the accompanied constitution.
These answer different questions. Likewise, the five
Bases are not the numerical list of limbs of the
first dhyāna.

**Voice discipline.** The associated-factor reply and
the alternative attributed to `apare` remain distinct.
The study does not assign an unnamed school to the
alternative merely from its philosophical resemblance
to another known position. The source's own attribution
is sufficient for this provisional pass.

**Witness cautions.** The opening `asya svabhāvānāṃ tu
kartavya` is awkward; its exact restoration remains
unresolved although the turn to dhyāna as support is
explicit. The running source has `śubhaikāgyraṃ`,
`smādhiḥ`, and `tatpratirūpa eva tatsaṃjñāvineveśāt`;
the local extract regularizes some forms. The momentariness
exchange around `dvitīyasya tasmādavikṣepa` is compressed
and warrants caution in assigning every clause to a
speaker. No silent restoration is imposed on the witnesses.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates what collected knowing is and
how its unity is determined. Yoga Technē, its kriyā–karma
companion, concerns the cultivated operation through
which this knowing becomes effective. The source supplies
a precise meeting point in the yoked functioning of
tranquillity and insight.

For Organon, mere numerical unity of object is not
yet a complete account of unified cognitive operation.
The debate asks what explains that operation, while
the excellence discussion connects its developed form
to knowing as things are. The project can develop this
relation without erasing the source's dispute over whether
a distinct samādhi factor is required.

Chapter 8 therefore begins with its own distinctions:
birth and attainment, defining nature and accompaniment,
one-object support and operative collectedness, and the
excellence of factor-endowed samādhi. These should guide
our reconstruction before a larger architecture is imposed.

**Review status.** Provisional, Bhāṣya-controlled study.
The twofold four-dhyāna classification, local attainment
definition, accompanied five-Base constitution,
samādhi dispute, strength distinction, knowing-based
explanation, and qualified use of the dhyāna name have
been checked against the local extract and running source.
Damaged prose remains marked for review.

## 10. OWL++ Seed

```text
Class: Dhyana
Class: DhyanaAspect
Class: AccompaniedAttainment
Class: SamadhiAccount

ObjectProperty: hasAspect
ObjectProperty: hasDefiningNature
ObjectProperty: hasAccompaniedConstitution
ObjectProperty: explainsCollectednessBy

FourDhyanas:
    aspects: CorrespondingBirth, MeditativeAttainment
    birthAccount: PreviouslyExplainedInLokanirdesa

AttainmentDhyana:
    definingNature: WholesomeOnePointednessOfMind
    accompaniedConstitution: FiveBases

OnePointedness:
    initialExplanation: OneObjectSupport

DistinctFactorAccount:
    explanation: SamadhiFactorMakesMindsOnePointed
    universalOccurrenceDoesNotImply: EqualStrength

OtherTeachersAccount:
    explanation: OnePointedMindsThemselvesAreSamadhi

ExcellentSamadhi:
    qualification: EndowedWithFactors
    operation: TranquillityAndInsightYokedTogether
    cognitiveRelation: CollectedMindKnowsAsThingsAre

ProjectConstraint: Birth-dhyana differs from attainment-dhyana.
ProjectConstraint: Five Bases are not five dhyana factors.
ProjectConstraint: Preserve the competing samadhi accounts.
ProjectConstraint: One object alone does not settle the explanation of collectedness.
ProjectConstraint: Qualified afflicted naming does not erase the wholesome definition.
```

This is a declarative project seed, not executable OWL.
VAK 8.02 next differentiates the dhyānas and introduces
the formless attainments.
