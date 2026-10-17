# VAK_8.40 — Expository Method, Error, and Authority

## 1. Sanskrit (Devanāgarī)

```sanskrit
काश्मीरवैभाषिकनीतिसिद्धः प्रायो मयायं कथितोऽभिधर्मः ।
यद्दुर्गृहीतं तदिहास्मदागः सद्धर्मनीतौ मुनयः प्रमाणम् ॥ ८.४० ॥
```

## 2. Sanskrit (IAST)

```text
kāśmīravaibhāṣikanītisiddhaḥ prāyo mayāyaṃ kathito 'bhidharmaḥ |
yad durgṛhītaṃ tad ihāsmadāgaḥ saddharmanītau munayaḥ pramāṇam || 8.40 ||
```

The local kārikā supplies munayaḥ, “sages,” in
both scripts. The running verse prints manayaḥ;
its commentary explicitly names Buddhas and Buddha-sons.
The local reading is therefore retained with the
running-source discrepancy disclosed.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `kāśmīravaibhāṣikanītisiddhaḥ` | nominative singular masculine compound adjective | established according to the Kāśmīra Vaibhāṣika method |
| `prāyaḥ` | adverbial form | chiefly; for the most part |
| `mayā` | instrumental singular first-person pronoun | by me |
| `ayam` | nominative singular masculine demonstrative | this |
| `kathitaḥ` | nominative singular masculine past passive participle | expounded, related |
| `abhidharmaḥ` | nominative singular masculine | Abhidharma |
| `yat … tat` | neuter singular relative-correlative pair | whatever … that |
| `durgṛhītam` | neuter singular participial expression, `dur-` + `gṛhīta` | badly grasped or misunderstood |
| `iha` | indeclinable | here, in this exposition |
| `asmadāgaḥ` | neuter singular compound, ending in `āgas` | our fault |
| `saddharmanītau` | locative singular feminine compound | in the interpretation or guidance of the true Dharma |
| `munayaḥ` | nominative plural masculine | sages |
| `pramāṇam` | nominative singular neuter predicate noun | authority, authoritative measure |

Sandhi: `mayā + ayam` > `mayāyam`; `iha + asmadāgaḥ`
> `ihāsmadāgaḥ`. In the analytical `asmat-āgas`
compound, the final consonant of `asmat` is
voiced before the following vowel. Āgaḥ is
the surface singular form of the neuter āgas,
not a plural list of separate errors.

## 4. Grammar

The opening subject and passive predicate frame the author's method; the relative-correlative pair assigns responsibility for misunderstanding. The final predicate makes plural sages authoritative without turning the author's limited `prāyaḥ` claim into school-wide identity.

```nltk-fcfg
% start S
# tokens: kāśmīravaibhāṣikanītisiddhaḥ prāyaḥ mayā ayam kathito abhidharmaḥ yad durgṛhītam tat iha asmadāgaḥ saddharmanītau munayaḥ ∅-buddhāḥ ∅-buddhaputrāḥ pramāṇam
S[SEM=?sem] -> CL[K=exposition] CL[K=responsibility,SEM=?sem] CL[K=authority]

CL[K=exposition,SEM=<all x.(Exposition(x) -> (UsesMethod(x,kashmira) & Predominantly(x,kashmira)))>] -> ADJ[CASE=?c,NUM=?n,GEN=?g,METHOD=school] ADV[DEGREE=limited] PRON[CASE=ins,NUM=sg,PERS=1] PRON[CASE=?c,NUM=?n,GEN=?g] PTCP[CASE=?c,NUM=?n,GEN=?g,TENSE=past,VOICE=pass] N[CASE=?c,NUM=?n,GEN=?g]
CL[K=responsibility,SEM=<?rel(?pred)(?corr)>] -> PRON[CASE=?c,NUM=?n,GEN=?g,REL=yes,SEM=?rel] PTCP[CASE=?c,NUM=?n,GEN=?g,TENSE=past,SEM=?pred] PRON[CASE=?c,NUM=?n,GEN=?g,CORR=yes] ADV[PLACE=here] N[CASE=?c,NUM=?n,GEN=?g,FAULT=ours,SEM=?corr]
CL[K=authority,SEM=<AuthorityFor(sages,truedharma)>] -> N[CASE=loc,NUM=sg,GEN=f,TOPIC=law] N[CASE=nom,NUM=pl,GEN=m,ROLE=authority] N[SUPPLIED=prose,ROLE=authority] N[SUPPLIED=prose,ROLE=authority] N[CASE=nom,NUM=sg,GEN=n,PRED=measure]

ADJ[CASE=nom,NUM=sg,GEN=m,METHOD=school] -> 'kāśmīravaibhāṣikanītisiddhaḥ'
ADV[DEGREE=limited] -> 'prāyaḥ'
PRON[CASE=ins,NUM=sg,PERS=1] -> 'mayā'
PRON[CASE=nom,NUM=sg,GEN=m] -> 'ayam'
PTCP[CASE=nom,NUM=sg,GEN=m,TENSE=past,VOICE=pass] -> 'kathito'
N[CASE=nom,NUM=sg,GEN=m] -> 'abhidharmaḥ'
PRON[CASE=nom,NUM=sg,GEN=n,REL=yes,SEM=<\P.\Q.all x.(P(x)->Q(x))>] -> 'yad'
PTCP[CASE=nom,NUM=sg,GEN=n,TENSE=past,SEM=<\x.MisgraspedHere(x)>] -> 'durgṛhītam'
PRON[CASE=nom,NUM=sg,GEN=n,CORR=yes] -> 'tat'
ADV[PLACE=here] -> 'iha'
N[CASE=nom,NUM=sg,GEN=n,FAULT=ours,SEM=<\x.AuthorFault(x)>] -> 'asmadāgaḥ'
N[CASE=loc,NUM=sg,GEN=f,TOPIC=law] -> 'saddharmanītau'
N[CASE=nom,NUM=pl,GEN=m,ROLE=authority] -> 'munayaḥ'
N[SUPPLIED=prose,ROLE=authority] -> '∅-buddhāḥ'
N[SUPPLIED=prose,ROLE=authority] -> '∅-buddhaputrāḥ'
N[CASE=nom,NUM=sg,GEN=n,PRED=measure] -> 'pramāṇam'
```

```nltk-dep
'abhidharmaḥ' -> 'kāśmīravaibhāṣikanītisiddhaḥ' | 'prāyaḥ' | 'mayā' | 'ayam' | 'kathito'
'asmadāgaḥ' -> 'yad' | 'durgṛhītam' | 'tat' | 'iha'
'pramāṇam' -> 'saddharmanītau' | 'munayaḥ' | '∅-buddhāḥ' | '∅-buddhaputrāḥ'
```

`Prāyaḥ` limits the method claim, and `mayā` shifts to `asmad-` in the admission of fault without establishing multiple authorship.
The Bhāṣya resolves `āgaḥ` as the expositor's fault and specifies the sages as Buddhas and Buddha-sons.
Plural `munayaḥ` is the subject of neuter singular predicate `pramāṇam`.
**Close construe.** This Abhidharma has been expounded
by me chiefly according to the method of
the Kāśmīra Vaibhāṣikas. Whatever is badly grasped
here is our fault. Concerning the true
Dharma's interpretation, the sages are the authority.

## 5. Translation

### Literal Translation

> This Abhidharma, established chiefly according to the
> method of the Kāśmīra Vaibhāṣikas, has been
> expounded by me. Whatever has been badly
> grasped here is our fault; in the
> interpretation of the true Dharma, the sages
> are the authority.

### Bhāṣya-informed study translation

> This Abhidharma has been expounded by me, established for the most
> part according to the method of the Kāśmīra Vaibhāṣikas. Whatever has
> been badly grasped here is our fault; in the guidance of the true
> Dharma, the sages, the Buddhas themselves and the Buddha-sons,
> are the authority.

## 6. Philosophical Translation

> A systematic exposition can acknowledge its predominant
> interpretive method while remaining answerable for its
> own mistakes. The school method, the author's
> grasp of it, and the authority invoked
> concerning the true Dharma are distinct. Naming
> the method neither guarantees an infallible exposition
> nor transfers the author's errors to the teaching.

This is a reconstruction of the verse's methodological
relations. It does not establish that every
Vaibhāṣika claim is rejected, or independently identify
which particular statements Vasubandhu regards as mistaken.

## 7. Technical Vocabulary

**`Kāśmīravaibhāṣika`.** The Kāśmīra Vaibhāṣika tradition
whose method predominantly informs the exposition. The
qualification concerns the work as presented here.

**`Nīti`.** Method, interpretive procedure, or doctrinal
line. It occurs both in the school-method
compound and in saddharmanīti. “Opinion” would be
too loose; “guidance” is possible if its
doctrinal and interpretive context is preserved.

**`Siddha`.** Established. Within the opening compound,
it concerns establishment according to the stated
method. It is not a new assertion
that the author is a perfected practitioner.

**`Prāyaḥ / prāyeṇa`.** Chiefly / for the
most part. The verse and prose both
preserve the limited scope of the methodological attribution.

**`Durgṛhīta`.** Badly grasped, misunderstood. The primary
sense concerns faulty apprehension or interpretation, not
necessarily manuscript corruption or an accidental copying error.

**`Āgas / aparādha`.** Fault / error. The
prose's aparādha explains the verse's āgas and
attributes responsibility to the expositor. No separate
penalty or disciplinary procedure is introduced here.

**`Munayaḥ / buddhāḥ / buddhaputrāḥ`.** Sages /
Buddhas / Buddha-sons. The latter two are
the prose's specification of the verse's authority.
The unit supplies no named roster of Buddha-sons.

**`Pramāṇa`.** Authority or authoritative measure. The
predicate here identifies who is authoritative concerning
the true Dharma. It does not enumerate
means of knowledge or supply a new
formal proof procedure in this closing verse.

## 8. Logical Determination

The verse separates predominant method, the author's responsibility for what is badly grasped, and the sages' authority concerning true-Dharma guidance. Its `yat … tat` clause is represented as a conditional, not as an unrestricted confession. `[verse]`; the identity of sages is specified in `[prose]`.

**Signature.** `Exposition(x)`, `UsesMethod(x,m)`, `Predominantly(x,m)`, `MisgraspedHere(x)`, `AuthorFault(x)`, and `AuthorityFor(a,d)`.

```nltk-sem
# derived by the section 4 parse, not typed by hand
all x.(MisgraspedHere(x) -> AuthorFault(x))
```

**Composition (`yat … tat`).** The relative-correlative contributes conditional mapping from the class of badly grasped items to the author's-fault class.

```nltk-valuation
abhidharma => abhidharma
author => author
kashmira => kashmira
itemone => itemone
sages => sages
truedharma => truedharma
Exposition => {abhidharma}
UsesMethod => {(abhidharma,kashmira)}
Predominantly => {(abhidharma,kashmira)}
MisgraspedHere => {itemone}
AuthorFault => {itemone}
AuthorityFor => {(sages,truedharma)}
```

```nltk-fol
# THEORY shared
# [verse] kāśmīravaibhāṣikanīti-siddhaḥ prāyaḥ
all x.(Exposition(x) -> (UsesMethod(x,kashmira) & Predominantly(x,kashmira)))
# [verse] yad durgṛhītaṃ tad asmadāgaḥ; shared with the section 4 derivation
all x.(MisgraspedHere(x) -> AuthorFault(x))
# [verse] saddharmanītau munayaḥ pramāṇam; [prose] Buddhas and Buddha-sons
AuthorityFor(sages,truedharma)
```

**Results (NLTK).** The checker loaded the lambda expressions and reports the shared theory true in this finite model. No theorem-prover result was run.

**Scope cautions.** `Prāyaḥ` means for the most part, not exclusively. The local witness reads *munayaḥ*; the running witness's *manayaḥ* is disclosed in §1–7, and no resolution is imposed here. The sages' authority is restricted to interpretation of true Dharma; it is not transferred to the Organon.

## 9. Interpretive Note

**Authorial voice.** Vasubandhu speaks explicitly of
his own exposition. The commentary's Buddhas and
Buddha-sons are an explanation of the authority
named in the verse, not a competing
school's objection to the author's statement.

**Witness cautions.** The running verse's manayaḥ
is not adopted over the local munayaḥ,
which is supported by both scripts and
the explanatory prose. The running commentary also
has nītyādisiddha and abidharma. The study retains
the clear method attribution without treating the
compressed nītyādi wording as a new independent
doctrinal category. The opening question's exact reading
remains qualified rather than silently reconstructed.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā distinguishes source authority, interpretive method,
and the actual exposition. Yoga Technē, its
kriyā–karma companion, concerns the disciplined work of
learning, articulating, checking, and correcting that exposition.
This comparison makes responsibility for interpretation visible.

The research's distinction between a system's construction
and its criterion of truth is useful
project language. It does not authorize the
Organon to claim the source's authority for
its own later architecture. The source's named
criterion remains the Buddhas and Buddha-sons concerning
saddharmanīti; the comparison remains separately labeled.

**Review status.** Provisional, Bhāṣya-controlled study.
The predominant school-method attribution, conditional responsibility
for error, and prose specification of the
sages have been checked against the local
witnesses and running source. The opening question's
compressed wording remains a philological review point.
Research originals remain untouched.

## 10. OWL++ Seed

```text
Class: AbhidharmaExposition
Class: InterpretiveMethod
Class: ExpositoryError
Class: AuthorityAttribution

ObjectProperty: predominantlyFollows
ObjectProperty: expoundedBy
ObjectProperty: errorResponsibilityAssignedTo
ObjectProperty: authorityIn

PresentExposition:
    expositor: Vasubandhu
    predominantMethod: KasmiraVaibhasikaNiti
    qualification: ForTheMostPart

FaultyGraspInPresentExposition:
    responsibility: Expositor
    specificErrorsEnumeratedHere: None

AuthorityConcerningSaddharmaNiti:
    verseDesignation: Sages
    commentarySpecification: Buddhas, BuddhaSons

OpeningQuestion:
    exactConstrual: RequiresPhilologicalReview

ProjectConstraint: Predominant method does not mean every claim has that school attribution.
ProjectConstraint: Conditional fault statement is not a list of retractions.
ProjectConstraint: Interpretive method, exposition, and authority remain distinct.
ProjectConstraint: Durgrihita does not automatically mean manuscript corruption.
ProjectConstraint: Pramana here is not an enumerated epistemological taxonomy.
ProjectConstraint: Organon reconstruction does not inherit the source's authority attribution.
```

This is a declarative project seed, not executable OWL.
VAK 8.41 next turns to the loss of the
Teacher and witnesses and the disordering of the teaching.
