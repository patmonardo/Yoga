# VAK_8.38 — Three Powers of Attainment Production

## 1. Sanskrit (Devanāgarī)

```sanskrit
हेतुकर्मबलाद्धात्वोरारूप्योत्पादनं द्वयोः ।
ध्यानानां रूपधातौ तु ताभ्यां धर्मतयापि च ॥ ८.३८ ॥
```

## 2. Sanskrit (IAST)

```text
hetukarmabalād dhātvor ārūpyotpādanaṃ dvayoḥ |
dhyānānāṃ rūpadhātau tu tābhyāṃ dharmatayāpi ca || 8.38 ||
```

The local verse is retained with analytical hyphens
removed. The running source embeds the two lines
in the commentary explaining their respective conditions.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `hetukarmabalāt` | ablative singular neuter compound | through the power of cause and karma |
| `dhātvoḥ` | locative dual masculine in this construction | in the two domains |
| `ārūpyotpādanam` | nominative singular neuter compound | production of formless attainments |
| `dvayoḥ` | locative dual numeral agreeing with `dhātvoḥ` | in the two |
| `dhyānānām` | genitive plural neuter | of the dhyānas |
| `rūpadhātau` | locative singular masculine compound | in the form domain |
| `tu` | indeclinable | however; marking the contrast |
| `tābhyām` | instrumental dual pronoun | through those two powers |
| `dharmatayā` | instrumental singular feminine | through dharmatā, lawful regularity |
| `api ca` | indeclinables | and also |

Sandhi: `ārūpya + utpādana` > `ārūpyotpādana`; `dharmatayā +
api` > `dharmatayāpi`. Dhātvoḥ is formally compatible
with genitive or locative dual, but the
production-in-a-domain construction supplies its locative function.

## 4. Grammar

The first production statement names two domains; the second elides production and contrasts its conditions. The Bhāṣya fixes the domains as form and formless and makes `tābhyām` refer to the two powers, not the domains.

```nltk-fcfg
% start S
# tokens: hetukarmabalāt dhātvoḥ ārūpyotpādanam dvayoḥ ∅-rūpadhātuḥ ∅-ārūpyadhātuḥ dhyānānām ∅-utpādanam rūpadhātau tu tābhyām dharmatayā api ca
S -> CL[K=formlessproduction] CL[K=dhyanaproduction]

CL[K=formlessproduction] -> ABL[CAUSE=?cause] N[CASE=?c,NUM=?n,GEN=?g,DOMAIN=?d] N[CASE=nom,NUM=sg,GEN=n,EVENT=formless] NUMR[CASE=?c,NUM=?n,GEN=?g] N[CASE=loc,NUM=sg,GEN=m,SUPPLIED=prose] N[CASE=loc,NUM=sg,GEN=m,SUPPLIED=prose]
CL[K=dhyanaproduction] -> N[CASE=gen,NUM=pl,GEN=n,EVENT=dhyana] N[SUPPLIED=prose,EVENT=production] N[CASE=loc,NUM=sg,GEN=m,DOMAIN=form] PTCL[CONTRAST=yes] PRON[CASE=ins,NUM=du,GEN=n,REF=twopowers] N[CASE=ins,NUM=sg,GEN=f,CAUSE=regularity] PTCL[ADDITIVE=yes] CONJ[ADDITIVE=yes]

ABL[CAUSE=power] -> 'hetukarmabalāt'
N[CASE=loc,NUM=du,GEN=m,DOMAIN=two] -> 'dhātvoḥ'
N[CASE=nom,NUM=sg,GEN=n,EVENT=formless] -> 'ārūpyotpādanam'
NUMR[CASE=loc,NUM=du,GEN=m] -> 'dvayoḥ'
N[CASE=loc,NUM=sg,GEN=m,SUPPLIED=prose] -> '∅-rūpadhātuḥ'
N[CASE=loc,NUM=sg,GEN=m,SUPPLIED=prose] -> '∅-ārūpyadhātuḥ'
N[CASE=gen,NUM=pl,GEN=n,EVENT=dhyana] -> 'dhyānānām'
N[SUPPLIED=prose,EVENT=production] -> '∅-utpādanam'
N[CASE=loc,NUM=sg,GEN=m,DOMAIN=form] -> 'rūpadhātau'
PTCL[CONTRAST=yes] -> 'tu'
PRON[CASE=ins,NUM=du,GEN=n,REF=twopowers] -> 'tābhyām'
N[CASE=ins,NUM=sg,GEN=f,CAUSE=regularity] -> 'dharmatayā'
PTCL[ADDITIVE=yes] -> 'api'
CONJ[ADDITIVE=yes] -> 'ca'
```

```nltk-dep
'ārūpyotpādanam' -> 'hetukarmabalāt' | 'dhātvoḥ' | 'dvayoḥ' | '∅-rūpadhātuḥ' | '∅-ārūpyadhātuḥ'
'∅-utpādanam' -> 'dhyānānām' | 'rūpadhātau' | 'tu' | 'tābhyām' | 'dharmatayā' | 'api' | 'ca'
```

`Dhātvoḥ` is interpreted locatively here.
`Dharmatā` adds a route for dhyāna production at cosmic contraction, not a universal third condition; production of an attainment is distinct from a rebirth event.
**Close construe.** In the two domains, form
and formless, formless attainments are produced through
causal and karmic power. In the form domain,
dhyānas are produced through those two powers
and also through dharmatā.

## 5. Translation

### Literal Translation

> Through the power of cause and karma,
> formless attainments are produced in the two domains.
> The dhyānas, however, are produced in the
> form domain through those two and also
> through dharmatā.

### Bhāṣya-informed study translation

> Through the power of cause and of karma, formless attainments are
> produced in the two domains, form and formless. The dhyānas are
> produced in the form domain through those two powers and also through
> dharmatā, the lawful course at the time of cosmic contraction.

## 6. Philosophical Translation

> The account distinguishes efficacy of cultivation,
> impending karmic maturation, and a specific regularity
> of the world-process. Their scope is unequal:
> the first two explain formless production in
> both higher domains; the third is additionally
> invoked for dhyāna production in the form
> domain at cosmic contraction.

This reconstruction keeps the source's distribution of
conditions. It does not make dharmatā an
unrestricted explanation of every contemplative event.

## 7. Technical Vocabulary

**`Hetubala`.** Causal power. The commentary specifies
recent and repeated cultivation, rather than leaving
hetu as an abstract cause with no local content.

**`Āsannābhīkṣṇābhyāsa`.** Recent and frequent or repeated
practice. Both proximity and repetition qualify the
cultivation supporting the causal-power explanation.

**`Karmabala`.** Karmic power. Here it concerns
higher-level karma whose maturation is impending, not
a generic measure of accumulated merit or effort.

**`Aparaparyāyavedanīya`.** To be experienced in a
later existence. This technical karmic qualification should
not be flattened into the immediately next rebirth;
the point here is that the relevant result
has now drawn near.

**`Pratyupasthitavipākatva`.** Having maturation at hand.
The karmic account joins a higher-level karmic
assignment with the imminence of its result.

**`Dharmatā`.** Lawful regularity. The prose invokes
it at cosmic contraction. “Suchness” without this
context would obscure the specific explanatory work
performed by the term in this passage (Pradhan 458|18–459|07,
ending kṛtsnānāṃ dharmāṇām udbhūtavṛttitvāt; that final explanatory
phrase is compressed and is not used to derive a separate cosmology).

**`Saṃvartanīkāla`.** Time of cosmic contraction or
dissolution. The research's “re-formation” is corrected
here; contraction is consistent with the Chapter 3
account of saṃvartanī and its successive evacuations
and destructions of world domains.

**`Udbhūtavṛtti`.** Manifest or arisen operation.
The source's kṛtsnānāṃ dharmāṇāmudbhūtavṛttitvāt gives
a compressed reason in terms of all the
dharmas' manifest operation. The passage supplies no
further internal analysis of that phrase.

## 8. Logical Determination

**The distribution of powers.**

| Attainment produced | Support domain | Powers specified |
|---|---|---|
| Formless samāpatti | Form domain | Causal power; karmic power |
| Formless samāpatti | Formless domain | Causal power; karmic power |
| Dhyāna | Form domain | Causal power; karmic power; additionally dharmatā at contraction |

These are explanatory possibilities within the stated
scope. The table does not assign dhyāna
production to a formless-domain support or extend
the contraction route to every formless attainment.

**Cultivation gives the first power its content.**
The prose directly equates the causal-power explanation
with recent and repeated practice. “Cause” should
therefore not be set against cultivation as
though it were a separate, untrained capacity.

**Karmic maturation retains the dispassion condition.**
The source explains that higher rebirth is
not possible while attachment to the lower
remains. The karmic route is therefore not
a bypass allowing higher rebirth with that
lower attachment intact. This sentence links the
attainment account to the conditions of higher
rebirth; it does not identify an attainment
session with the rebirth event itself.

**The third route has a cosmological occasion.**
The prose explicitly says saṃvartanīkāle. Its statement
that lower-level beings then produce the corresponding
dhyāna is tied to that occasion. It does
not assert that all beings continuously possess
all dhyānas, or that any practitioner can
invoke dharmatā as a substitute for practice.

**The scope of the present discussion.** VAK 8.37
classified acquisition and support for the release,
mastery, and totality complexes. Its following question
asks how special dhyāna and formless attainments
are produced in the higher domains. This
unit answers that question; it does not
cancel the preceding human-production rule for the
specified non-formless special practices.

## 9. Interpretive Note

**Correction of the cosmological wording.** Both the
research discussion and its argument reconstruction sometimes
use “cosmic re-formation.” The source says saṃvartanī,
contraction, not the re-expansion or formation of
the world. The official study corrects that
wording while leaving the research witnesses intact.

**Witness and explanatory limits.** The running text
prints sarvasttvā where the local Bhāṣya excerpt
has sarvasattvā; the contextual reading is “all
beings.” Its avīta rāgeṇa also has an
internal spacing break. Neither feature creates a
new doctrinal alternative. The final udbhūtavṛtti
explanation remains compressed; “the total configuration
of the dharmic order” is a research paraphrase,
not an independently established technical entity here.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā distinguishes practice history, karmic condition,
cosmological occasion, support domain, and attainment produced.
Yoga Technē, its kriyā–karma companion, concerns the
effective cultivation represented explicitly by recent and
repeated practice, while recognizing the other conditions
reported in this source account.

The research's distinction between genesis of cognitive
capacity, regulated field, and Principle of validity
is useful project analysis. This verse supplies
a bounded account of attainment production. It
does not derive the validity of knowledge from
its karmic origin or make cosmological regularity
the project's Principle of Knowledge.

**Review status.** Provisional, Bhāṣya-controlled study.
The two-domain reference, three powers and their
unequal distribution, cultivation specification, impending karmic
maturation, lower-attachment restriction, and contraction context
have been checked against the local witnesses
and running source. The final explanatory compound
is retained with its interpretive limit marked.

## 10. OWL++ Seed

```text
Class: AttainmentProduction
Class: ExplanatoryPower
Class: SupportDomain
Class: CosmologicalOccasion

ObjectProperty: explainedBy
ObjectProperty: occursOnSupport
ObjectProperty: occasionedAt

CausalPower:
    specification: RecentAndRepeatedCultivation

KarmicPower:
    specification: ImpendingMaturationOfHigherLevelKarma
    karmicTiming: ResultToBeExperiencedInALaterExistence
    accompanyingConstraint: HigherRebirthRequiresFreedomFromLowerAttachment

FormlessProduction:
    possibleSupportDomains: Form, Formless
    explanatoryPowers: CausalPower, KarmicPower

DhyanaProductionInFormDomain:
    explanatoryPowers: CausalPower, KarmicPower
    additionalPower: Dharmata

DharmataProductionCase:
    occasion: CosmicContraction
    statedEvent: RelevantLowerLevelBeingsProduceCorrespondingDhyana
    compressedExplanation: ManifestOperationOfAllDharmas

ProjectConstraint: The listed powers are not universally simultaneous requirements.
ProjectConstraint: Cosmic contraction is not cosmic re-formation.
ProjectConstraint: Dharmata route retains its stated occasion and support scope.
ProjectConstraint: Attainment production is distinct from the event of rebirth.
ProjectConstraint: Karmic route does not bypass freedom from lower attachment.
ProjectConstraint: Genesis of a capacity does not itself determine validity of knowledge.
```

This is a declarative project seed, not executable OWL.
VAK 8.39 next distinguishes transmission and realization
as the two forms of the true teaching.
