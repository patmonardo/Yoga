# VAK_8.03 — Formless Naming, Absence of Form, and Its Renewed Arising

## 1. Sanskrit (Devanāgarī)

```sanskrit
विभूतरूपसंज्ञाख्याः सह सामन्तकैस्त्रिभिः ।
नारूप्ये रूपसद्भावः रूपोत्पत्तिस्तु चित्ततः ॥ ८.०३ ॥
```

## 2. Sanskrit (IAST)

```text
vibhūtarūpasaṃjñākhyāḥ saha sāmantakais tribhiḥ |
nārūpye rūpasadbhāvaḥ rūpotpattis tu cittataḥ || 8.03 ||
```

The Sanskrit follows the local kārikā witness. The
Devanāgarī renders the same reading. The running source
varies in vowel length in `ārupya` and `rupotpatti`;
the local study's forms are retained with that difference
explicit.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `vibhūta-rūpa-saṃjñā-ākhyāḥ` | nominative plural masculine compound adjective (`saṃjñā + ākhyāḥ` → `saṃjñākhyāḥ`) | designated as having form-perception passed away; the prose glosses `vibhūtā` with `vigatā`, gone away: disappearance, not manifestation |
| `saha` | indeclinable governing instrumental | together with |
| `sāmantakaiḥ` | instrumental plural neuter | neighboring or access attainments |
| `tribhiḥ` | instrumental plural numeral | three |
| `na` | negative particle (`na + ārūpye` → `nārūpye`) | negates presence of Form |
| `ārūpye` | locative singular | in the formless domain |
| `rūpa-sadbhāvaḥ` | nominative singular masculine compound | presence or existence of Form |
| `rūpa-utpattiḥ` | nominative singular feminine compound (`rūpotpattiḥ`) | arising of Form |
| `tu` | contrastive particle | however |
| `cittataḥ` | ablatival adverb | from citta, consciousness |

## 4. Grammar

The parse keeps absence in the formless domain distinct from later arising.
The locative scopes the negative claim; the source ablative retains the
Bhāṣya's maturation-condition on renewed Form.

```nltk-fcfg
% start S
# tokens: ∅-ārūpyāḥ vibhūtarūpasaṃjñākhyāḥ saha sāmantakaiḥ tribhiḥ na ārūpye rūpasadbhāvaḥ rūpotpattiḥ tu cittataḥ
S[SEM=<?absence & ?arising>] -> CL[K=designate] CL[K=absence,SEM=?absence] CL[K=arising,SEM=?arising]
CL[K=designate] -> N[SUPPLIED=prose,NUM=?n,GEN=?g] ADJ[NUM=?n,GEN=?g] P[CASE=ins] N[CASE=ins,GEN=n] NUMR[CASE=ins]
CL[K=absence,SEM=<?loc(?noun)>] -> NEG[SEM=<\P.P>] LOC[CASE=loc,SEM=?loc] N[CASE=nom,NUM=sg,GEN=m,SEM=?noun]
CL[K=arising,SEM=<?event(?source)>] -> N[CASE=nom,NUM=sg,GEN=f,SEM=?event] PTCL[CONTRAST=yes] ABL[SOURCE=cause,QUAL=prose,SEM=?source]
N[SUPPLIED=prose,NUM=pl,GEN=m] -> '∅-ārūpyāḥ'
ADJ[NUM=pl,GEN=m,GONE=yes] -> 'vibhūtarūpasaṃjñākhyāḥ'
P[CASE=ins] -> 'saha'
N[CASE=ins,NUM=pl,GEN=n] -> 'sāmantakaiḥ'
NUMR[CASE=ins,NUM=pl] -> 'tribhiḥ'
NEG[SEM=<\P.P>] -> 'na'
LOC[CASE=loc,SEM=<\P.-P(formlessdomain)>] -> 'ārūpye'
N[CASE=nom,NUM=sg,GEN=m,SEM=<\x.FormPresent(x)>] -> 'rūpasadbhāvaḥ'
N[CASE=nom,NUM=sg,GEN=f,SEM=<\P.all x.(Arises(x,form) -> P(x))>] -> 'rūpotpattiḥ'
PTCL[CONTRAST=yes] -> 'tu'
ABL[SOURCE=cause,QUAL=prose,SEM=<\x.(CittaSource(x) & ConditionedBy(x,maturation))>] -> 'cittataḥ'
```

```nltk-dep
'∅-ārūpyāḥ' -> 'vibhūtarūpasaṃjñākhyāḥ' | 'sāmantakaiḥ'
'sāmantakaiḥ' -> 'saha' | 'tribhiḥ'
'rūpasadbhāvaḥ' -> 'na' | 'ārūpye'
'rūpotpattiḥ' -> 'cittataḥ' | 'tu'
```

`vibhūta` is glossed `vigata` (gone), not manifestation. Access to infinite
space is excluded because it takes the fourth dhyāna as object, leaving three
access stages. `cittataḥ` retains the Bhāṣya's maturation-cause qualification.

**Close construe.** The formless attainments, together with three access
attainments, receive the designation that form-perception has disappeared.
Form is not present in the formless domain; its renewed arising, however, is
from causally conditioned citta.

## 5. Translation

### Literal Translation

> They are designated as having form-perception passed
> away, together with three access attainments. There
> is no presence of Form in the formless domain; the
> arising of Form, however, is from consciousness.

### Bhāṣya-informed study translation

> The four formless attainments, together with the access
> stages of the latter three, are designated as having
> form-perception passed away. There is no presence of Form
> in the formless domain; the arising of Form, however, is
> from consciousness conditioned by the cause whose maturation
> that Form is.

## 6. Philosophical Translation

> Absence of a constituent does not by itself establish
> impossibility of its later arising. The account denies
> form in the formless domain while locating the conditions
> for renewed form in a causally determined citta. Naming,
> present constitution, and future genesis remain distinct.

The renewed form need not be numerically the same form
that existed before. The passage explains arising after
an interruption; it does not establish identity of a
material object across that interruption.

## 7. Technical Vocabulary

**`Vibhūtarūpasaṃjña`.** Having perception of form passed
away. The designation has a specific extension among
principal and access attainments; proximity to a formless
attainment alone is insufficient for the name.

**`Sāmantaka`.** Neighboring or access attainment. The
first access stage's fourth-dhyāna object explains its
exclusion. The main infinite-space attainment remains
included; access and principal attainment must not be
confused.

**`Rūpajāti`.** The class of material form. The reply
insists that this entire class is transcended, whereas
the classes of feeling and the other nonmaterial Bases
are not. This supports the four-Base constitution
stated in VAK 8.02.

**`Bhūta / bhautika`.** Material Elements and what is
derived from them. The objection proposing bodily and
verbal restraint as residual form is challenged because
derivative materiality cannot stand without its Elemental
basis.

**`Tadvipākahetuparibhāvita`.** Conditioned by the cause
whose maturation is that form. This qualifies the mind
from which form later arises. It does not describe
arbitrary creation by a present wish.

**`Labdhavṛtti`.** Having obtained functioning or an
occasion for activity. The precise attachment and causal
nuance of this compressed phrase remain provisional,
while its role in the qualified arising account is clear.

**`Analpakalpocchinna`.** Interrupted for many kalpas.
The question expressly rules out explaining renewed
form by a merely short gap in its present occurrence.
It introduces no modern chronological measurement.

## 8. Logical Determination

Three connected questions remain distinct: which attainments receive the “form-perception gone” name, whether Form is present in the formless domain, and how Form can arise again later [verse; prose]. The Bhāṣya excludes access to infinite space, scopes canonical dependencies, and qualifies renewed arising by a maturation cause.

**Signature.** `Principal(x)` (principal formless attainment); `NamedAccess(x)` (eligible access attainment); `NameGone(x)` (form-perception-gone designation); `FormPresent(x)`; `Arises(x,y)`; `CittaSource(x)`; `ConditionedBy(x,c)`.

**Finite data.** The principal four and latter three access stages receive the designation; the first access stage does not. Present absence and later genesis are separate relations.

```nltk-valuation
space => space
consciousness => consciousness
nothingness => nothingness
neither => neither
accessspace => accessspace
accessconsciousness => accessconsciousness
accessnothingness => accessnothingness
accessneither => accessneither
formlessdomain => formlessdomain
returningmind => returningmind
form => form
maturation => maturation
Principal => {space, consciousness, nothingness, neither}
NamedAccess => {accessconsciousness, accessnothingness, accessneither}
NameGone => {space, consciousness, nothingness, neither, accessconsciousness, accessnothingness, accessneither}
FormPresent => {}
Arises => {(returningmind,form)}
CittaSource => {returningmind}
ConditionedBy => {(returningmind,maturation)}
```

**Parse composition (absence plus qualified arising).**

```nltk-sem
# derived by the section 4 parse, not typed by hand
(-FormPresent(formlessdomain) & all x.(Arises(x,form) -> (CittaSource(x) & ConditionedBy(x,maturation))))
```

**Rules and answer (verse and prose).**

```nltk-fol
# THEORY shared
# [verse] vibhūtarūpasaṃjñākhyāḥ; [prose] the four principal attainments
all x.(Principal(x) -> NameGone(x))
# [prose] the latter three access attainments
all x.(NamedAccess(x) -> NameGone(x))
# [verse] nārūpye rūpasadbhāvaḥ and rūpotpattiḥ tu cittataḥ; [prose] maturation-conditioned
(-FormPresent(formlessdomain) & all x.(Arises(x,form) -> (CittaSource(x) & ConditionedBy(x,maturation))))
# [prose] access to infinite space retains the fourth-dhyāna object
-NameGone(accessspace)
```

**Results (NLTK).** `check_logic.py` reports the shared theory true in this finite valuation; this checks model satisfaction, not a proof of the cosmological claim or a contradiction proof against the objector.

**Scope cautions.** The objection about slight Form and the canonical-dependence debate are not universalized into rules: the prose tests their quantifier scope. Absence now does not imply impossibility of later genesis, and the latter does not imply hidden Form now. The account does not say citta creates Form at will or that a practitioner's body disappears during attainment.

## 9. Interpretive Note

**Complete passage control.** The local Bhāṣya excerpt
omits portions of the material-basis and scriptural-scope
debates. The running source supplies those portions,
including the smallness, transparency, heat, external
form, and food examples. The study therefore treats
the excerpt as a selection, not a complete transcription.

**Witness cautions.** The running text contains forms
such as `smāpattāvapi`, `hyaṣmaṇa`, `binā`, `kutsnām`,
and the awkward `kavaḍīkārāntareṇā 'pi vinā`. The
comparative argument about gross food is intelligible
from its context, but the final expression is not a
clean transmitted construction. The `īṣadrūpa` analogy
also has an irregular junction around `dāpiṅgalavat`.
No conjectural restoration is substituted into the witnesses.

**Scope of the absence claim.** The argument concerns
formless-domain constitution and return from formless
existence. It should not become an assertion that the
physical body of a human meditator disappears whenever
that person enters a formless attainment. The birth
and attainment distinction remains essential.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates the difference between current
constitution and the conditions of later genesis. Yoga
Technē, its kriyā–karma companion, concerns the operative
causal determination through which a later form can arise.
The source keeps those relations together without retaining
a hidden material constituent in the formless interval.

For Organon, the useful distinction is between preserving
an instantiated form and retaining conditions for a
new formation. The research analogy to regeneration
can be developed from that distinction, but numerical
identity of the earlier and later form is not supplied
by the text. Nor does the passage define Meaning simply
as the ability to regenerate an output.

The source's own explanation is karmic and specifically
qualified: citta conditioned by a maturation cause.
A project model must preserve that attribution instead
of presenting an unrestricted idealism or a software
storage theory as Vasubandhu's doctrine.

**Review status.** Provisional, Bhāṣya-controlled study.
The seven included principal/access states, first-access
exclusion, subtle-form challenge, scriptural-scope debate,
Base argument, and qualified renewed-form account
have been checked against the local excerpt and complete
running passage. Compressed causal wording and source
defects remain explicit.

## 10. OWL++ Seed

```text
Class: FormlessAttainment
Class: AccessAttainment
Class: NamingCondition
Class: MaterialForm
Class: CausallyConditionedCitta

ObjectProperty: receivesDesignation
ObjectProperty: hasObjectGround
ObjectProperty: conditionedByMaturationCause
ObjectProperty: givesRiseTo

FormPerceptionPassedAway:
    included: FourPrincipalFormlessAttainments
    alsoIncluded: AccessToLatterThreeFormlessAttainments
    excluded: AccessToInfiniteSpace

AccessToInfiniteSpace:
    objectGround: FourthDhyana

FormlessDomain:
    materialFormPresent: No

RenewedMaterialForm:
    source: CittaConditionedByRelevantMaturationCause
    causalFunctioningQualification: LabdhaVrtti

ProjectConstraint: Access state differs from principal attainment.
ProjectConstraint: Denial of present form does not deny later arising.
ProjectConstraint: Later arising does not prove hidden present form.
ProjectConstraint: Do not assert numerical identity across the interruption.
ProjectConstraint: Cittatah is qualified by the maturation-cause account.
ProjectConstraint: Domain constitution does not imply disappearance of a meditator's body.
```

This is a declarative project seed, not executable OWL.
VAK 8.04 next determines the formless attainments through
their modes of attention and naming.
