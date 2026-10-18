# VAK_1.04 — Impure and Pure

## 1. Sanskrit (Devanāgarī)

```sanskrit
सास्रवानास्रवा धर्माः संस्कृता मार्गवर्जिताः ।
सास्रवाः आस्रवास्तेषु यस्मात्समनुशेरते ॥ १.०४ ॥
```

## 2. Sanskrit (IAST)

```text
sāsravānāsravā dharmāḥ saṃskṛtā mārgavarjitāḥ /
sāsravāḥ āsravās teṣu yasmāt samanuśerate // 1.04 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sāsravānāsravāḥ | sāsravāḥ + anāsravāḥ; nominative plural | impure and pure; the first division of the dharmas |
| dharmāḥ | nominative masculine plural | the dharmas so divided |
| saṃskṛtāḥ | participial adjective; nominative plural | conditioned |
| mārgavarjitāḥ | mārga-varjitāḥ; nominative plural | excluding the Path |
| sāsravāḥ | nominative plural | impure; the predicate resumed |
| āsravāḥ | nominative masculine plural | the *āsravas*; subject of the persistence clause |
| teṣu | locative masculine plural pronoun | in those dharmas; refers to the conditioned other than the Path |
| yasmāt | causal indeclinable | because |
| samanuśerate | 3rd plural middle, present | persist |

**Grammar tokens.** Verse-order IAST with sandhi opened. The coordinated
first table row becomes two leaves; the repeated *sāsravāḥ* is retained.
No covert word is inserted.

```text
# tokens: sāsravāḥ anāsravāḥ dharmāḥ saṃskṛtāḥ mārgavarjitāḥ sāsravāḥ āsravāḥ teṣu yasmāt samanuśerate
```

## 4. Grammar

The feature grammar parses a normalized, compound-divided token sequence.
It separates *sāsravānāsravāḥ* into its coordinated members and resolves
external sandhi; it does not change the Sanskrit witness. The nominal
clauses supply a copula semantically, without adding a spoken token.

```nltk-fcfg
% start S
# tokens: sāsravāḥ anāsravāḥ dharmāḥ saṃskṛtāḥ mārgavarjitāḥ sāsravāḥ āsravāḥ teṣu yasmāt samanuśerate
S[SEM=<(?division & ?classification & ?reason)>] -> CL[K=divide,SEM=?division] CL[K=classify,SEM=?classification] CL[K=reason,SEM=?reason]
CL[K=divide,SEM=<all x.(?d(x) -> ((?i(x) | ?p(x)) & -(?i(x) & ?p(x))))>] -> ADJ[CASE=nom,NUM=?n,GEN=?g,STATUS=impure,SEM=?i] ADJ[CASE=nom,NUM=?n,GEN=?g,STATUS=pure,SEM=?p] N[CASE=nom,NUM=?n,GEN=?g,K=dharma,SEM=?d]
CL[K=classify,SEM=<all x.(Dharma(x) -> (?i(x) <-> (?c(x) & ?e(x))))>] -> ADJ[CASE=nom,NUM=?n,GEN=?g,K=conditioned,SEM=?c] ADJ[CASE=nom,NUM=?n,GEN=?g,K=exclusion,SEM=?e] ADJ[CASE=nom,NUM=?n,GEN=?g,STATUS=impure,SEM=?i]
CL[K=reason,SEM=<?l(\x.?q(?v(x)))>] -> N[CASE=nom,NUM=?n,GEN=m,K=asrava,SEM=?q] PRON[CASE=loc,NUM=pl,GEN=m,REF=classified,SEM=?l] CAUS[LINK=reason] V[NUM=?n,PERSON=third,VOICE=middle,LOC=required,SEM=?v]
ADJ[CASE=nom,NUM=pl,GEN=m,STATUS=impure,SEM=<\x.Impure(x)>] -> 'sāsravāḥ'
ADJ[CASE=nom,NUM=pl,GEN=m,STATUS=pure,SEM=<\x.Pure(x)>] -> 'anāsravāḥ'
N[CASE=nom,NUM=pl,GEN=m,K=dharma,SEM=<\x.Dharma(x)>] -> 'dharmāḥ'
ADJ[CASE=nom,NUM=pl,GEN=m,K=conditioned,SEM=<\x.Conditioned(x)>] -> 'saṃskṛtāḥ'
ADJ[CASE=nom,NUM=pl,GEN=m,K=exclusion,SEM=<\x.-PathTruth(x)>] -> 'mārgavarjitāḥ'
N[CASE=nom,NUM=pl,GEN=m,K=asrava,SEM=<\P.exists a.(Asrava(a) & P(a))>] -> 'āsravāḥ'
PRON[CASE=loc,NUM=pl,GEN=m,REF=classified,SEM=<\P.all x.((Dharma(x) & Conditioned(x) & -PathTruth(x)) -> P(x))>] -> 'teṣu'
CAUS[LINK=reason] -> 'yasmāt'
V[NUM=pl,PERSON=third,VOICE=middle,LOC=required,SEM=<\x.\a.PersistsIn(a,x)>] -> 'samanuśerate'
```

```nltk-dep
'dharmāḥ' -> 'sāsravāḥ' | 'anāsravāḥ'
'sāsravāḥ' -> 'saṃskṛtāḥ' | 'mārgavarjitāḥ'
'samanuśerate' -> 'āsravāḥ' | 'teṣu' | 'yasmāt'
```

**Feature chart checkpoints.** Half-open spans index the normalized
ten-token sequence. `FeatureChartParser` must return exactly one complete
parse; the simplified root `SEM` must occur in section 8.

| Span | Constituent | Unified features / semantic result |
|---|---|---|
| [0, 3) | `CL[K=divide]` | nominative plural masculine agreement; exclusive division |
| [3, 6) | `CL[K=classify]` | nominative plural masculine agreement; conditioned with Path excluded |
| [6, 10) | `CL[K=reason]` | third-person plural subject–verb agreement; locative anaphor |
| [0, 10) | `S` | conjunction of division, classification, and stated persistence |

The dependency block records local heads, not a second semantic derivation.
The FOL conjunction records the reason-clause's content; the grammatical
`LINK=reason` preserves its explanatory role. Conjunction itself does not
formalize explanatory grounding.

The copula and the repeated noun *dharmāḥ* are supplied in English. The
Path-exclusion qualifies the conditioned dharmas; it is not a third
predicate interchangeable with conditioned and impure. *Yasmāt* introduces
the reason for calling those dharmas impure.

The change of subject is decisive. Dharmas receive the classification;
the *āsravas* perform the persistence. The verse does not say that dharmas
are impure because dharmas persist. The locative identifies the terms
through which the stated persistence is related, but does not by itself
explain its mechanism.

The Bhāṣya tests this relation against *ālambana*. An *āsrava* can arise
taking Cessation or the Path as *ālambana* without persisting in either.
The pure member is not enumerated in this verse.

## 5. Translation

### Literal Translation

> Dharmas are impure and pure. Conditioned, excluding the Path, are impure,
> because the *āsravas* persist in them.

### Bhāṣya-informed study translation

> Dharmas are impure and pure. Conditioned dharmas other than the Truth of
> the Path are impure, because the *āsravas* persist in them.

## 6. Philosophical Translation

> A dharma's impurity is determined by the persistence of the *āsravas* in
> it, not by conditioned existence alone and not merely by being taken as
> *ālambana*. The conditioned Path is pure: conditioned operation and the
> persistence of impurity are distinguishable.

The Grammar–Logic pilot moves from classification to its stated reason,
then to the commentary's counterexample. This is a determination of all
dharmas, not yet an identification of their classification with the later
Dharma Principle.

In the Organon reading, the predicate impure must be understood through the
relation that warrants it. It is not explained by imagining impurity as a
property sealed inside an isolated thing. Yet relation alone is too broad:
the commentary distinguishes taking as *ālambana* from persistence. Hegel's
Ground supplies the question of what warrants the predicate; it does not
license replacing these distinct relations with one generic dependency.

The Path makes the distinction effective. It is conditioned without being
a locus of the stated persistence. Purification therefore cannot mean
simply abolishing conditioned existence. The precise account of why the
*āsravas* do not persist in the Path or Cessation is deferred by the Bhāṣya.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| dharma | dharma | not a second word for the division |
| sāsrava | impure | conditioned, excluding the Path |
| anāsrava | pure | the Path, and the unconditioned of the next verse |
| saṃskṛta | conditioned | produced through conditions |
| mārga | Path | the commentary: the Truth of the Path |
| āsrava | *āsrava* | subject of the persistence clause; distinct from *sāsrava*, the classification |
| samanuśerate | persist | technical persistence of the *āsravas*, not mere temporal duration |
| teṣu | in those dharmas | locative relation, not a separate enduring bearer |
| ālambana | *ālambana* | what an arising takes; that relation does not entail persistence |

## 8. Logical Determination

The section 4 feature chart composes the verse's three clauses by lambda
application. `[verse]` identifies verse content; `[prose]` identifies the
Bhāṣya's specification or counterexample. The model is a finite witness
for these distinctions, not a derivation of conditioned genesis.

**Signature.** `Dharma(x)`, `Impure(x)`, `Pure(x)`, `Conditioned(x)`,
`PathTruth(x)`, `CessationTruth(x)`, `Asrava(a)`, `PersistsIn(a,x)`,
and `CanTakeAsAlambana(a,x)`. The last predicate represents possible taking,
not a presently occurring episode or a modal-logic analysis. `PersistsIn`
is a relation between an *āsrava* and a dharma, not a unary predicate of
duration. Constants `ordinary`, `path`, `cessation`, and `influx` name
representative cases.

**Lambda composition.** The anaphor's restriction comes from the preceding
classification; *mārga* is resolved as the Truth of the Path by the prose.
Existential quantification of the *āsravas* records participation in the
relation, not that every *āsrava* persists in every impure dharma.

```nltk-sem
impure : \x.Impure(x)
conditioned : \x.Conditioned(x)
excluded : \x.-PathTruth(x)
asravas : \P.exists a.(Asrava(a) & P(a))
locus : \P.all x.((Dharma(x) & Conditioned(x) & -PathTruth(x)) -> P(x))
persist : \x.\a.PersistsIn(a,x)
reason : (\P.all x.((Dharma(x) & Conditioned(x) & -PathTruth(x)) -> P(x)))(\x.(\P.exists a.(Asrava(a) & P(a)))((\x.\a.PersistsIn(a,x))(x)))
```

**Root `SEM`, after beta-reduction.** This is the conjunction derived by
the complete feature parse, not an independently substituted paraphrase.
The biconditional reads the verse as specification of the impure class;
exclusivity reads impure / pure as a division, as the prose confirms.

```nltk-fol
# THEORY verse
# EXPECT verse T
# [verse] division, class specification, and reason-clause content
(all x.(Dharma(x) -> ((Impure(x) | Pure(x)) & -(Impure(x) & Pure(x)))) & all x.(Dharma(x) -> (Impure(x) <-> (Conditioned(x) & -PathTruth(x)))) & all x.((Dharma(x) & Conditioned(x) & -PathTruth(x)) -> exists a.(Asrava(a) & PersistsIn(a,x))))

# THEORY prose
# EXPECT prose T
# [prose] the Path is conditioned and pure; no asrava persists in either Truth
all x.(PathTruth(x) -> (Dharma(x) & Conditioned(x) & Pure(x)))
all x.(CessationTruth(x) -> Dharma(x))
all a x.((Asrava(a) & (PathTruth(x) | CessationTruth(x))) -> -PersistsIn(a,x))
# [prose] taking either Truth as alambana is nevertheless possible
all x.((PathTruth(x) | CessationTruth(x)) -> exists a.(Asrava(a) & CanTakeAsAlambana(a,x)))

# THEORY counterexamples
# EXPECT counterexamples T
# [prose] possible taking does not require persistence in what is taken
exists a x.(Asrava(a) & CanTakeAsAlambana(a,x) & -PersistsIn(a,x))
# [prose] conditioned and pure is an admitted case
exists x.(Dharma(x) & Conditioned(x) & Pure(x))

# THEORY rejected_taking_entails_persistence
# EXPECT rejected_taking_entails_persistence F
all a x.((Asrava(a) & CanTakeAsAlambana(a,x)) -> PersistsIn(a,x))

# THEORY rejected_conditioned_entails_impure
# EXPECT rejected_conditioned_entails_impure F
all x.((Dharma(x) & Conditioned(x)) -> Impure(x))

# THEORY rejected_pure_entails_unconditioned
# EXPECT rejected_pure_entails_unconditioned F
all x.((Dharma(x) & Pure(x)) -> -Conditioned(x))
```

**Finite valuation.** `ordinary` represents a conditioned non-Path dharma,
not every ordinary cognition. The Path and Cessation provide the
commentary's contrasting cases. No domain census is asserted.

```nltk-valuation
ordinary => ordinary
path => path
cessation => cessation
influx => influx
Dharma => {ordinary, path, cessation}
Impure => {ordinary}
Pure => {path, cessation}
Conditioned => {ordinary, path}
PathTruth => {path}
CessationTruth => {cessation}
Asrava => {influx}
PersistsIn => {(influx,ordinary)}
CanTakeAsAlambana => {(influx,path), (influx,cessation)}
```

**Expected checks.** `verse`, `prose`, and `counterexamples` evaluate true
in this valuation. Each `rejected_...` theory evaluates false: its universal
claim has a counterexample here. A finite model does not prove that the
accepted formulas follow from Sanskrit grammar alone. The grounding force
of "because," the mechanism of persistence, and the proposed *sāra* and
emptiness determinations are not encoded as established conclusions.

## 9. Interpretive Note

**Translation note.** Both verse translations retain *āsrava* and distinguish
it from the classifying predicate impure. The study translation resolves
*mārga* as the Truth of the Path from the Bhāṣya. "In them" preserves the
locative; "through them" can express its relational force in commentary,
but should not silently add a causal mechanism.

**Pilot result.** The feature grammar, chart checkpoints, dependency
grammar, lambda composition, FOL theories, and valuation implement the
formal pattern used in Chapter 8. Grammar identifies what persists and in
what; the Bhāṣya shows why mere *ālambana*-relation is insufficient. The warranted
determination is persistence of the *āsravas*, not persistence as such.
This qualifies the proposed reading of an impure Dharma as a persisting
formation without abandoning the inquiry into how it sustains impurity.

**Open determination.** The proposed Dharma qua *sāra* and the Form–Emptiness
relation remain questions for the synthesis. Neither *sāra* nor emptiness
occurs in this unit. Their explanatory value must be tested against the
distinction established here, not inserted as meanings of *samanuśerate*.
Likewise, *āśraya* is not supplied as a missing word behind *teṣu*.
The paired [Bhāṣya study](VAK_1.04_bhasya.md) develops the argument and its
Hegelian Ground question. VAK 1.05 remains outside this pilot.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .

vak:VAK_1_04 a vak:Karika ;
    vak:hasTopic vak:PureImpureDivision ;
    vak:belongsTo vak:Dhatunirdesa .

vak:ImpureDharma a vak:ConditionedDharma ;
    vak:excludes vak:PathTruth ;
    vak:criterion vak:PersistenceOfAsravas .

vak:PathTruth a vak:ConditionedDharma, vak:PureDharma .

vak:TakingAsAlambana owl:differentFrom vak:PersistenceOfAsravas .
```
