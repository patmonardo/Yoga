# VAK_1.11 — The Continuity Called Avijñapti

## 1. Sanskrit (Devanāgarī)

```sanskrit
विक्षिप्ताचित्तकस्यापि योऽनुबन्धः शुभाशुभः ।
महाभूतान्युपादाय स ह्यविज्ञप्तिरुच्यते ॥ १.११ ॥
```

## 2. Sanskrit (IAST)

```text
vikṣiptācittakasyāpi yo 'nubandhaḥ śubhāśubhaḥ /
mahābhūtāny upādāya sa hy avijñaptir ucyate // 1.11 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| vikṣipta-acittakasya | genitive singular | of one otherwise directed, or without consciousness |
| api | particle | even; the scope is wider |
| yaḥ | nominative masculine singular relative pronoun | which continuity |
| anubandhaḥ | nominative masculine | the continuity |
| śubha-aśubhaḥ | nominative masculine | wholesome or unwholesome |
| mahābhūtāni | accusative plural | the Great Elements |
| upādāya | absolutive | depending on |
| saḥ | nominative masculine singular correlative pronoun | that same continuity |
| hi | particle | indeed; the naming |
| avijñaptiḥ | nominative feminine | the name |
| ucyate | passive | is called |

The compound is compressed. The commentary separates *vikṣiptacittakasya*
and *acittakasya*. *Api* also brings in one whose consciousness is present
and not otherwise directed.

**Grammar tokens.** Verse-order IAST with external sandhi opened. The
compressed compound remains one leaf; its two cases are interpreted with
the Bhāṣya. No consciousness noun is inserted as an overt token.

```text
# tokens: vikṣipta-acittakasya api yaḥ anubandhaḥ śubha-aśubhaḥ mahābhūtāni upādāya saḥ hi avijñaptiḥ ucyate
```

## 4. Grammar

The relative *yaḥ* and correlative *saḥ* keep the same continuity in
view. *Śubhāśubhaḥ* agrees with masculine *anubandhaḥ*; feminine
*avijñaptiḥ* supplies its name, not another agreeing description.
*Mahābhūtāni* is the accusative complement of *upādāya*.

```nltk-fcfg
% start S
# tokens: vikṣipta-acittakasya api yaḥ anubandhaḥ śubha-aśubhaḥ mahābhūtāni upādāya saḥ hi avijñaptiḥ ucyate
S[SEM=<?relative(?naming)>] -> RELATIVE[NUM=?n,GEN=?g,SEM=?relative] NAMING[NUM=?n,GEN=?g,SEM=?naming]
RELATIVE[NUM=?n,GEN=?g,SEM=<\Q.all x.((?stream(x) & ?ethical(x) & ?depend(x)) -> (?scope(x) & Q(x)))>] -> HOLDER[CASE=gen,NUM=sg,SEM=?scope] EVEN REL[CASE=nom,NUM=?n,GEN=?g] STREAM[CASE=nom,NUM=?n,GEN=?g,SEM=?stream] ETHICAL[CASE=nom,NUM=?n,GEN=?g,SEM=?ethical] DEPENDENCE[SEM=?depend]
DEPENDENCE[SEM=<?verb(?basis)>] -> ELEMENTS[CASE=?case,NUM=pl,SEM=?basis] DEPEND[FORM=absolutive,OBJCASE=?case,SEM=?verb]
NAMING[NUM=?n,GEN=?g,SEM=<?verb(?name)>] -> CORREL[CASE=nom,NUM=?n,GEN=?g] NAMINGMARK NAME[CASE=nom,NUM=?n,SEM=?name] CALLED[NUM=?n,PERSON=third,VOICE=passive,SEM=?verb]
HOLDER[CASE=gen,NUM=sg,SEM=<\x.(ScopeIncludes(x,otherwise_directed) & ScopeIncludes(x,absent))>] -> 'vikṣipta-acittakasya'
EVEN -> 'api'
REL[CASE=nom,NUM=sg,GEN=m] -> 'yaḥ'
STREAM[CASE=nom,NUM=sg,GEN=m,SEM=<\x.Stream(x)>] -> 'anubandhaḥ'
ETHICAL[CASE=nom,NUM=sg,GEN=m,SEM=<\x.(Wholesome(x) | Unwholesome(x))>] -> 'śubha-aśubhaḥ'
ELEMENTS[CASE=acc,NUM=pl,SEM=<great_elements>] -> 'mahābhūtāni'
DEPEND[FORM=absolutive,OBJCASE=acc,SEM=<\b.\x.DependsOn(x,b)>] -> 'upādāya'
CORREL[CASE=nom,NUM=sg,GEN=m] -> 'saḥ'
NAMINGMARK -> 'hi'
NAME[CASE=nom,NUM=sg,GEN=f,SEM=<\x.CalledAvijnapti(x)>] -> 'avijñaptiḥ'
CALLED[NUM=sg,PERSON=third,VOICE=passive,SEM=<\P.\x.P(x)>] -> 'ucyate'
```

```nltk-dep
'ucyate' -> 'saḥ' | 'hi' | 'avijñaptiḥ'
'saḥ' -> 'anubandhaḥ'
'anubandhaḥ' -> 'vikṣipta-acittakasya' | 'yaḥ' | 'śubha-aśubhaḥ' | 'upādāya'
'vikṣipta-acittakasya' -> 'api'
'upādāya' -> 'mahābhūtāni'
```

**Close construe.** Which wholesome or unwholesome continuity belongs
even to one otherwise directed or without consciousness, depending on
the Great Elements—that indeed is called *avijñapti*.

The logical projection treats the relative as a classification rule:
ethical stream plus Elemental dependence warrants the name. Its scope
includes the two conspicuous consciousness cases; the Bhāṣya expands
*api* to the undistracted case too. `ScopeIncludes` marks applicability,
not an assertion that every stream actually traverses every state.
Dependence is not silently strengthened into the Vaibhāṣika cause-gloss.
The nominal name is feminine without forcing masculine continuity to
change gender. Naming and *hi*'s explanatory emphasis do not by themselves
prove a separate substance.

## 5. Translation

### Literal Translation

> The wholesome or unwholesome continuity which, depending on the
> Great Elements, belongs even to one whose consciousness is otherwise
> directed or absent: that indeed is called *avijñapti*.

### Bhāṣya-informed study translation

> The wholesome or unwholesome continuity that persists even when
> consciousness is directed elsewhere or absent depends on the Great
> Elements and is called *avijñapti*.

## 6. Philosophical Translation

Again, a definition. Named at 1.09. Counted around at 1.10. Defined here.
The word stays Sanskrit.

The continuity is the subject. Wholesome or unwholesome is its character.
*Api* keeps the minded case. The conspicuous cases are not the whole class:
otherwise directed, without consciousness, and also present and undistracted.
The commentary reads the first as a different consciousness, and the second
as the attainment of non-perception or the attainment of cessation. Continuity
is a stream.

Ethical continuity alone would also fit acquisition. *Mahābhūtāny upādāya*
is the differentiator. The Vaibhāṣikas take *upādāya* as cause, because the
Great Elements produce and the rest. That reading is marked. It is not the verse's
only word.

The name is the contrast. Form and action, and yet it does not inform another
as *vijñapti* does. The summary adds two origins, *vijñapti* or absorption.
The verse does not. Outward action is not the whole.

Which Great Elements are meant is the next question. Not this verse.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| avijñapti | *avijñapti* | the name stays |
| anubandha | continuity | glossed as stream |
| pravāha | stream | the commentary's word |
| śubha / aśubha | wholesome / unwholesome | *kuśala* / *akuśala* |
| citta | consciousness | otherwise directed, absent, or present |
| vikṣipta | otherwise directed | a different consciousness |
| acittaka | without consciousness | two attainments |
| api | even | includes the undistracted |
| mahābhūta | Great Element | the differentiator; defined next |
| upādāya | depending on | causal reading is Vaibhāṣika |
| prāpti-vāha | stream of acquisition | the similar, distinguished |
| vijñapti | *vijñapti* | informs another; the contrast |
| samādhi | absorption | one origin, in the summary |

## 8. Logical Determination

**Kārikā, derived.** The same variable carries continuity, ethical
character, dependence, scope, and naming. The disjunction does not require
one stream to be both wholesome and unwholesome.

```nltk-sem
# derived by the section 4 parse
all x.((Stream(x) & (Wholesome(x) | Unwholesome(x)) & DependsOn(x,great_elements)) -> ((ScopeIncludes(x,otherwise_directed) & ScopeIncludes(x,absent)) & CalledAvijnapti(x)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
all x.((Stream(x) & (Wholesome(x) | Unwholesome(x)) & DependsOn(x,great_elements)) -> ((ScopeIncludes(x,otherwise_directed) & ScopeIncludes(x,absent)) & CalledAvijnapti(x)))
# THEORY prose
# EXPECT prose T
all x.(CalledAvijnapti(x) -> (ScopeIncludes(x,undistracted) & FormAndAction(x) & -InformsAnother(x)))
all x.(CalledAvijnapti(x) -> (Origin(x,vijnapti) | Origin(x,absorption)))
exists x.(Stream(x) & Wholesome(x) & AcquisitionStream(x) & -DependsOn(x,great_elements) & -CalledAvijnapti(x))
# THEORY rejected_ethical_stream_alone_suffices
# EXPECT rejected_ethical_stream_alone_suffices F
all x.((Stream(x) & (Wholesome(x) | Unwholesome(x))) -> CalledAvijnapti(x))
# THEORY rejected_elemental_dependence_alone_suffices
# EXPECT rejected_elemental_dependence_alone_suffices F
all x.(DependsOn(x,great_elements) -> CalledAvijnapti(x))
# THEORY rejected_avijnapti_informs_another
# EXPECT rejected_avijnapti_informs_another F
all x.(CalledAvijnapti(x) -> InformsAnother(x))
# THEORY rejected_only_absent_consciousness
# EXPECT rejected_only_absent_consciousness F
all x.(CalledAvijnapti(x) -> -ScopeIncludes(x,undistracted))
```

```nltk-valuation
great_elements => elemental_basis
otherwise_directed => other_consciousness_case
absent => no_consciousness_case
undistracted => undistracted_consciousness_case
vijnapti => manifestation_origin
absorption => absorption_origin
Stream => {wholesome_continuity,unwholesome_continuity,acquisition_case}
Wholesome => {wholesome_continuity,acquisition_case}
Unwholesome => {unwholesome_continuity}
DependsOn => {(wholesome_continuity,elemental_basis),(unwholesome_continuity,elemental_basis),(neutral_form_case,elemental_basis)}
CalledAvijnapti => {wholesome_continuity,unwholesome_continuity}
ScopeIncludes => {(wholesome_continuity,other_consciousness_case),(wholesome_continuity,no_consciousness_case),(wholesome_continuity,undistracted_consciousness_case),(unwholesome_continuity,other_consciousness_case),(unwholesome_continuity,no_consciousness_case),(unwholesome_continuity,undistracted_consciousness_case)}
AcquisitionStream => {acquisition_case}
FormAndAction => {wholesome_continuity,unwholesome_continuity}
InformsAnother => {}
Origin => {(wholesome_continuity,absorption_origin),(unwholesome_continuity,manifestation_origin)}
```

**Model checks.** Two representative streams make the rule non-vacuous
and exercise each ethical alternative. Acquisition supplies the ethical
stream without Elemental dependence; a neutral Form case supplies
Elemental dependence without the defining ethical stream. Neither is
therefore classified as *avijñapti*. Removing a qualifying stream's name
or either verse-scope relation must fail. The finite examples do not
assign absorption exclusively to wholesome streams or manifestation
exclusively to unwholesome ones; the prose rule allows either origin.

**Bhāṣya determination.** Undistracted consciousness, non-disclosure,
and the two origins are prose elaborations, not extra Sanskrit leaves.
The Vaibhāṣika interpretation of dependence as causal is attributed in
§6; `DependsOn` does not derive production or its temporal mechanism.
The model does not derive eternal persistence from continuity.

**Organon interpretation.** An operator account can begin from
continuing efficacy without present disclosure. But no composition of
two meanings is specified by this definition. *Saṃyoga* is not a token
in the verse or its paired prose. To develop that comparison, distinguish
a rule for combining meanings from the stream that bears an ethical
determination: 1.11 explicitly defines the latter. The earlier overview
follows.

```text
named at 1.09
counted around at 1.10
defined here

wholesome or unwholesome stream
    could also be acquisition

stream depending on the Great Elements
    → avijñapti

api
    otherwise directed
    without consciousness
    also present and undistracted

Form and action
    and does not inform another

summary, not the verse
    from vijñapti or from absorption

1.12 not opened
```

## 9. Interpretive Note

**Translation note.** The Bhāṣya explains that *api* also includes a person whose consciousness is present and not otherwise directed; it specifies non-perception and cessation attainments as examples of absence of consciousness. It further glosses *avijñapti* as Form and action that does not inform another as *vijñapti* does.

The hinge is *upādāya*, then *api*. Interpretation of the name is in the
Bhāṣya.

**Meaning-operator inquiry.** Non-disclosure is not meaninglessness or
inactivity. The passage gives the inquiry a constraint: an operator reading
must account for ethical continuity, dependence, and persistence beyond
present attention, not merely the combination of two presented meanings.
This makes *avijñapti* a candidate for investigating retained determination
in the system, not yet a Sanskrit synonym for *saṃyoga*.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_11 a vak:Karika ;
    vak:hasTopic vak:Avijnapti ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Avijnapti vak:is vak:WholesomeOrUnwholesomeStream ;
    vak:dependsOn vak:GreatElements ;
    vak:distinctFrom vak:AcquisitionStream ;
    vak:informsAnother false ;
    vak:continuesWhenConsciousnessOtherwiseDirected true ;
    vak:continuesWithoutConsciousness true ;
    vak:continuesUndistracted true .

vak:UpadayaCausalReading vak:attributedTo vak:Vaibhasika .
```
