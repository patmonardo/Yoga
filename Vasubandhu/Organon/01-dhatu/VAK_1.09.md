# VAK_1.09 — The Form Base

## 1. Sanskrit (Devanāgarī)

```sanskrit
रूपं पञ्चेन्द्रियाण्यर्थाः पञ्चाविज्ञप्तिरेव च ।
तद्विज्ञानाश्रया रूपप्रसादाश्चक्षुरादयः ॥ १.०९ ॥
```

## 2. Sanskrit (IAST)

```text
rūpaṃ pañcendriyāṇy arthāḥ pañcāvijñaptir eva ca /
tadvijñānāśrayā rūpaprasādāś cakṣurādayaḥ // 1.09 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| rūpam | nominative neuter singular | Form; the Form Base |
| pañcendriyāṇi | pañca + indriyāṇi; nominative neuter plural | five Faculties |
| arthāḥ | nominative masculine plural | meanings |
| pañca | numeral | counts the meanings, not the faculties again |
| avijñaptiḥ | nominative feminine singular | one member; named, not defined |
| eva ca | particles | and just that |
| tadvijñānāśrayāḥ | tad-vijñāna-āśrayāḥ; nominative plural | supports of the corresponding Cognition |
| rūpaprasādāḥ | rūpa-prasādāḥ; nominative plural | clarities of Form |
| cakṣurādayaḥ | cakṣus-ādayaḥ; nominative plural | beginning with the eye |

## 4. Grammar

The feature chart parses the enumeration and the Faculty predication.
The root `SEM` composes the latter only; the enumeration is represented
separately in section 8. Tokens normalize external sandhi and divide
*pañcendriyāṇi*, without altering the witness.

```nltk-fcfg
% start S
# tokens: rūpam pañca indriyāṇi arthāḥ pañca avijñaptiḥ eva ca tadvijñānāśrayāḥ rūpaprasādāḥ cakṣurādayaḥ
S[SEM=?definition] -> CL[K=enumerate] CL[K=define,SEM=?definition]
CL[K=enumerate] -> N[CASE=nom,NUM=sg,GEN=n,K=form] NUMR[COUNT=five] N[CASE=nom,NUM=pl,GEN=n,K=faculty] N[CASE=nom,NUM=pl,GEN=m,K=meaning] NUMR[COUNT=five] N[CASE=nom,NUM=sg,GEN=f,K=avijnapti] PTCL[FOCUS=yes] CONJ[COORD=and]
CL[K=define,SEM=<?q(\x.(?s(x) & ?p(x)))>] -> N[CASE=nom,NUM=?n,GEN=?g,K=support,SEM=?s] N[CASE=nom,NUM=?n,GEN=?g,K=clarity,SEM=?p] N[CASE=nom,NUM=?n,GEN=?g,K=faculties,SEM=?q]
N[CASE=nom,NUM=sg,GEN=n,K=form] -> 'rūpam'
NUMR[COUNT=five] -> 'pañca'
N[CASE=nom,NUM=pl,GEN=n,K=faculty] -> 'indriyāṇi'
N[CASE=nom,NUM=pl,GEN=m,K=meaning] -> 'arthāḥ'
N[CASE=nom,NUM=sg,GEN=f,K=avijnapti] -> 'avijñaptiḥ'
PTCL[FOCUS=yes] -> 'eva'
CONJ[COORD=and] -> 'ca'
N[CASE=nom,NUM=pl,GEN=m,K=support,SEM=<\x.exists c.(Cognition(c) & Corresponds(c,x) & Supports(x,c))>] -> 'tadvijñānāśrayāḥ'
N[CASE=nom,NUM=pl,GEN=m,K=clarity,SEM=<\x.ClarityOfForm(x)>] -> 'rūpaprasādāḥ'
N[CASE=nom,NUM=pl,GEN=m,K=faculties,SEM=<\P.all x.(Faculty(x) -> P(x))>] -> 'cakṣurādayaḥ'
```

```nltk-dep
'rūpam' -> 'indriyāṇi' | 'arthāḥ' | 'avijñaptiḥ'
'indriyāṇi' -> 'pañca'
'arthāḥ' -> 'pañca'
'avijñaptiḥ' -> 'eva' | 'ca'
'cakṣurādayaḥ' -> 'tadvijñānāśrayāḥ' | 'rūpaprasādāḥ'
```

**Feature chart checkpoints.** Half-open spans index the eleven normalized
tokens. The parser must produce one complete parse.

| Span | Constituent | Feature / semantic determination |
|---|---|---|
| [0, 8) | `CL[K=enumerate]` | heterogeneous nominal enumeration; two counts of five |
| [8, 11) | `CL[K=define]` | nominative plural masculine agreement across three terms |
| [0, 11) | `S` | Faculty predication's composed `SEM` |

The singular *rūpam* names the collection, not an agreement controller
requiring all its members to be singular neuter. The second line is a
nominal predication with an understood copula. Its three terms agree.
The Bhāṣya resolves *cakṣurādayaḥ* as the five named Faculties and the
*tad-* reference as the corresponding sensory Cognitions. The grammar
does not insert Cognition into the Form enumeration.

## 5. Translation

### Literal Translation

> Form is the five Faculties, the five meanings, and *avijñapti*. The
> clarities of Form, beginning with the eye, are supports of the
> corresponding Cognition.

### Bhāṣya-informed study translation

> The Form Base comprises five Faculties—eye, ear, nose, tongue, and
> body—their five corresponding meanings—visible Form, sound, odor, taste,
> and the tangible—and *avijñapti*. The five Faculties are clarities of
> Form, each serving as the support of the Cognition corresponding to its
> meaning.

## 6. Philosophical Translation

Eleven, and no twelfth. Form collects five Faculties, five meanings, and *avijñapti*.

The Faculty is a clarity of Form. It supports the corresponding Cognition; the eye supports Eye-Cognition. Cognition is supported, not counted.

Meaning stays lowercase. The commentary glosses it as condition. Faculty and meaning are the two sides, not two inventories. *Avijñapti* is the eleventh, singular, and not yet defined.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| rūpa | Form | the Form Base; eleven |
| skandha | Base | the first collection; not the whole |
| indriya | Faculty | one of the five; not a synonym for an anatomical organ |
| artha | meaning | the five |
| viṣaya | condition | the commentary’s gloss of meaning; not a second list |
| avijñapti | *avijñapti* | named, not defined |
| rūpa-prasāda | clarity of Form | what the five Faculties are |
| vijñāna | Cognition | not Principle |
| āśraya | support | of the corresponding Cognition; not a twelfth member |
| āyatana | Essence | cited for the eye; not enumerated |
| upādāya | depending on | the four Great Elements; not the appropriation of 1.08 |
| dhātu | Principle | not a member of this count |

## 8. Logical Determination

The feature grammar follows the Chapter 8 pattern: lambda composition
derives the Faculty definition; explicit FOL records the enumeration and
the Bhāṣya's correspondence. `[verse]` and `[prose]` distinguish provenance.
This is a formal analysis of classification and support, not an account
of the genesis of Cognition.

**Signature.** `FormMember(x)` (membership in the Form Base here),
`Faculty(x)`, `Meaning(x)` (one of the five sensory meanings),
`Avijnapti(x)`, `ClarityOfForm(x)`, `Cognition(c)`,
`Corresponds(c,f)`, and `Supports(f,c)`. `VisibleMeaning(x)` singles out
visible Form among the meanings. The constants name representative kinds,
not an eleven-item census of concrete occurrences.

**Lambda composition.** The subject quantifies over the five Faculties
specified by the prose. The compound's support relation is binary;
it is not identity between Faculty and Cognition.

```nltk-sem
faculties : \P.all x.(Faculty(x) -> P(x))
clarities : \x.ClarityOfForm(x)
supports : \x.exists c.(Cognition(c) & Corresponds(c,x) & Supports(x,c))
definition : (\P.all x.(Faculty(x) -> P(x)))(\x.((\x.exists c.(Cognition(c) & Corresponds(c,x) & Supports(x,c)))(x) & ClarityOfForm(x)))
```

**Root `SEM` and source-controlled theory.** The first formula is exactly
the simplified semantic result of the feature parse.

```nltk-fol
# THEORY verse
# [verse; prose resolves the five Faculties and corresponding Cognitions]
all x.(Faculty(x) -> (exists c.(Cognition(c) & Corresponds(c,x) & Supports(x,c)) & ClarityOfForm(x)))
# [verse; prose: etavan rupaskandhah] exhaustive membership by the three groups
all x.(FormMember(x) <-> (Faculty(x) | Meaning(x) | Avijnapti(x)))

# THEORY prose
# [prose] the two fivefold lists, with avijnapti named but not defined
all x.(Faculty(x) <-> (x = eye | x = ear | x = nose | x = tongue | x = body))
all x.(Meaning(x) <-> (x = visible | x = sound | x = odor | x = taste | x = tangible))
all x.(Avijnapti(x) <-> x = avijnapti)
# [prose] corresponding support, not arbitrary support of any Cognition
Supports(eye,eyecognition) & Corresponds(eyecognition,eye)
Supports(ear,earcognition) & Corresponds(earcognition,ear)
Supports(nose,nosecognition) & Corresponds(nosecognition,nose)
Supports(tongue,tonguecognition) & Corresponds(tonguecognition,tongue)
Supports(body,bodycognition) & Corresponds(bodycognition,body)
# [verse enumeration; prose closure] supported Cognition is not an extra member
all c.(Cognition(c) -> -FormMember(c))

# THEORY counterexamples
exists f c.(Faculty(f) & Cognition(c) & Supports(f,c) & -(f = c))
exists x.(FormMember(x) & -VisibleMeaning(x))

# THEORY rejected_support_is_identity
all f c.(Supports(f,c) -> f = c)

# THEORY rejected_form_is_only_visible
all x.(FormMember(x) -> VisibleMeaning(x))
```

**Finite valuation.** Eleven distinct representatives instantiate the
Form classification: five Faculties, five meanings, and *avijñapti*.
Five Cognition representatives remain outside it. Distinct denotations
are a choice of this model; FOL does not supply a unique-names assumption.

```nltk-valuation
eye => eye
ear => ear
nose => nose
tongue => tongue
body => body
visible => visible
sound => sound
odor => odor
taste => taste
tangible => tangible
avijnapti => avijnapti
eyecognition => eyecognition
earcognition => earcognition
nosecognition => nosecognition
tonguecognition => tonguecognition
bodycognition => bodycognition
FormMember => {eye, ear, nose, tongue, body, visible, sound, odor, taste, tangible, avijnapti}
Faculty => {eye, ear, nose, tongue, body}
Meaning => {visible, sound, odor, taste, tangible}
Avijnapti => {avijnapti}
ClarityOfForm => {eye, ear, nose, tongue, body}
Cognition => {eyecognition, earcognition, nosecognition, tonguecognition, bodycognition}
Corresponds => {(eyecognition,eye), (earcognition,ear), (nosecognition,nose), (tonguecognition,tongue), (bodycognition,body)}
Supports => {(eye,eyecognition), (ear,earcognition), (nose,nosecognition), (tongue,tonguecognition), (body,bodycognition)}
VisibleMeaning => {visible}
```

**Expected checks.** `verse`, `prose`, and `counterexamples` evaluate true.
Both `rejected_...` theories evaluate false in this model. The test
distinguishes support from identity and Form Base from visible Form alone.
It does not prove that support suffices for Cognition to arise, define
*avijñapti*, or resolve *āśraya* throughout the system.

## 9. Interpretive Note

The hinge is the count, then the support. The five Faculties are indicated. The five meanings are named and left for the next verse. The scripture calls the eye an internal Essence, a clarity of Form depending on the four Great Elements. That citation is not this enumeration. The Prakaraṇa agrees: the eye is a clarity of Form that supports Eye-Cognition.

**Organon Light.** The passage makes Form more extensive than visible
appearance and gives the Faculties a relational determination through
the Cognition they support. These are positive grounds for metaphysical
inquiry, not merely a list of sensible things. The formal layer preserves
that opening without identifying a support with what it supports or
claiming a transcendental deduction. The scriptural Essence determination
and dependence on the four Great Elements remain commentary witnesses,
not silently added conclusions of the verse's feature parse.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_09 a vak:Karika ;
    vak:hasTopic vak:FormBase ;
    vak:belongsTo vak:Dhatunirdesa .

vak:FormBase vak:hasMember vak:FiveFaculties, vak:FiveMeanings, vak:Avijnapti ;
    vak:count 11 ;
    vak:includesCognition false .

vak:Eye vak:is vak:ClarityOfForm ;
    vak:supports vak:EyeCognition .

vak:Avijnapti vak:defined false .
vak:Meaning vak:glossedAs vak:Condition .
```
