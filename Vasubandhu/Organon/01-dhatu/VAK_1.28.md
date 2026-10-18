# VAK_1.28 — Space and Cognition within the Six Supports of Birth

## 1. Sanskrit (Devanāgarī)

```sanskrit
छिद्रमाकाशधात्वाख्यम् आलोकतमसी किल ।
विज्ञानधातुर्विज्ञानं सास्रवं जन्मनिश्रयाः ॥ १.२८ ॥
```

## 2. Sanskrit (IAST)

```text
chidram ākāśadhātvākhyam ālokatamasī kila /
vijñānadhātur vijñānaṃ sāsravaṃ janmaniśrayāḥ // 1.28 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| chidram | nominative neuter singular | opening, aperture; subject of the first clause |
| ākāśa-dhātu-ākhyam | bahuvrīhi; nominative neuter singular | named the Space Principle; agrees with *chidram* |
| āloka-tamasī | dvandva; nominative neuter dual | light and darkness; the reported nature of the opening |
| kila | reportive particle | it is said; marks a received account |
| vijñāna-dhātuḥ | nominative masculine singular | Cognition Principle; subject of the second clause |
| vijñānam | nominative neuter singular | Cognition; predicate |
| sa-āsravam | nominative neuter singular | Impure; agrees with *vijñānam* |
| janma-niśrayāḥ | nominative masculine plural | supports of birth; the Bhāṣya supplies the six Principles as subject |

`Dhātu` is Principle. *Vijñāna* is Cognition. The Bhāṣya identifies
the larger list as six Principles: earth, water, fire, wind, space, and
Cognition. The verse's plural `janmaniśrayāḥ` predicates birth-support of
the six together, not of the singular Cognition Principle alone.

**Grammar tokens.** Verse-order IAST with sandhi opened (`vijñānadhātur`
→ *vijñāna-dhātuḥ*, `vijñānaṃ` → *vijñānam*, `sāsravaṃ` → *sa-āsravam*)
and compound boundaries marked. The subject of the last clause, *ime ṣaḍ
dhātavaḥ*, is supplied by the Bhāṣya inside the rule (`SUPPLIED=prose`),
not as a covert leaf.

```text
# tokens: chidram ākāśa-dhātu-ākhyam āloka-tamasī kila vijñāna-dhātuḥ vijñānam sa-āsravam janma-niśrayāḥ
```

## 4. Grammar

Three clauses. The first identifies an opening as what is named the Space
Principle, with a reported dual nature. The second identifies the Cognition
Principle as Impure Cognition. The third, with its plural predicate, needs
the six Principles as subject. Agreement binds *chidram* with its naming
compound, and *vijñānam* with *sa-āsravam*; the final predicate must be
plural.

```nltk-fcfg
% start S
# tokens: chidram ākāśa-dhātu-ākhyam āloka-tamasī kila vijñāna-dhātuḥ vijñānam sa-āsravam janma-niśrayāḥ
S[SEM=<(?space & ?cognition & ?support)>] -> SPACE[SEM=?space] COGNITION[SEM=?cognition] SUPPORT[SUPPLIED=prose,SEM=?support]
SPACE[SEM=<exists x.(?opening(x) & ?named(x) & ?report(?nature)(x))>] -> OPENING[CASE=nom,NUM=?n,GEN=?g,SEM=?opening] NAMED[CASE=nom,NUM=?n,GEN=?g,SEM=?named] NATURE[CASE=nom,NUM=du,GEN=n,SEM=?nature] KILA[SEM=?report]
COGNITION[SEM=<exists y.(?cog(y) & ?impure(y) & ?principle(y))>] -> PRINCIPLE[CASE=nom,NUM=sg,GEN=m,SEM=?principle] COG[CASE=nom,NUM=?n,GEN=?g,SEM=?cog] IMPURE[CASE=nom,NUM=?n,GEN=?g,SEM=?impure]
SUPPORT[SUPPLIED=prose,SEM=<all p.(InSixfold(p) -> ?supports(p))>] -> SUPPORTS[CASE=nom,NUM=pl,GEN=m,SEM=?supports]
OPENING[CASE=nom,NUM=sg,GEN=n,SEM=<\x.Opening(x)>] -> 'chidram'
NAMED[CASE=nom,NUM=sg,GEN=n,SEM=<\x.Named(x,space_principle)>] -> 'ākāśa-dhātu-ākhyam'
NATURE[CASE=nom,NUM=du,GEN=n,SEM=<light_and_darkness>] -> 'āloka-tamasī'
KILA[SEM=<\n x.ReportedNature(x,n)>] -> 'kila'
PRINCIPLE[CASE=nom,NUM=sg,GEN=m,SEM=<\y.Named(y,cognition_principle)>] -> 'vijñāna-dhātuḥ'
COG[CASE=nom,NUM=sg,GEN=n,SEM=<\y.Cognition(y)>] -> 'vijñānam'
IMPURE[CASE=nom,NUM=sg,GEN=n,SEM=<\y.Impure(y)>] -> 'sa-āsravam'
SUPPORTS[CASE=nom,NUM=pl,GEN=m,SEM=<\p.SupportOfBirth(p)>] -> 'janma-niśrayāḥ'
```

```nltk-dep
'ākāśa-dhātu-ākhyam' -> 'chidram' | 'āloka-tamasī'
'āloka-tamasī' -> 'kila'
'vijñānam' -> 'vijñāna-dhātuḥ' | 'sa-āsravam'
'janma-niśrayāḥ' -> 'ākāśa-dhātu-ākhyam' | 'vijñānam'
```

**Close construe.** An opening is what is named the Space Principle:
light and darkness, it is said. The Cognition Principle is Impure
Cognition. [These six Principles] are supports of birth.

`Named(x,n)` is designation within this six-Principle teaching, not an
identity of the classified Dharma with everything bearing the name.
`ReportedNature` keeps *kila*: the light-and-darkness account is received,
not asserted outright. The Cognition clause restricts by conjunction
(Cognition, Impure); it does not define Cognition. The plural predicate
ranges over all six, not only over the Cognition Principle.

`Ālokatamasī` is dual. The bracketed subject of the final clause is made
explicit by the Bhāṣya: `ime ṣaḍ dhātavaḥ`, these six Principles.

## 5. Translation

### Literal Translation

> An opening is named the Space Principle—light and darkness, it is said.
> The Cognition Principle is Impure Cognition; these [six] are
> supports of birth.

### Bhāṣya-informed study translation

> In the teaching of six Principles, an opening is called the Space
> Principle—light and darkness, it is said. The Cognition Principle is Impure
> Cognition; these six Principles are supports of birth.

## 6. Philosophical Translation

The same name does not guarantee the same determination. In this particular
teaching, “space” names a conditioned opening and “Cognition” is restricted
to Impure Cognition. The six Principles are considered together by
their shared function as supports of birth; this does not make them six new
members outside the established eighteen Principles.

**Interpretation**

Four of the six Principles enter the Tangible Principle. The conditioned
Space Principle enters the Form Principle. Impure Cognition is placed among
the seven Cognition Principles: the six Cognition Principles, and the
Mind Principle. The restriction does not define Cognition in every context.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| dhātu | Principle | not Cognition |
| ṣaḍ-dhātu | six Principles | earth, water, fire, wind, space, and Cognition in the sūtra teaching |
| chidra | opening; aperture | conditioned referent named as the Space Principle here |
| ākāśa | unconditioned space; non-obstruction | distinct from the conditioned opening of this verse |
| ākāśadhātu | Space Principle | opening explained through light and darkness; assigned to Form |
| āloka | light | one reported determination of the opening |
| tamas | darkness | the other reported determination |
| kila | according to a received account | reportive; does not itself identify a school |
| vijñāna | Cognition | not Principle |
| vijñānadhātu | Cognition Principle | Impure Cognition in this six; one of the seven |
| sāsrava | Impure | the Cognition selected for this birth-support teaching |
| anāsrava | Pure | excluded from the Cognition Principle in this particular list |
| janmaniśraya | support of birth | shared function of the six Principles |
| pratisandhicitta | rebirth-linking Cognition | opening Cognition in the life-continuum described by the Bhāṣya |
| cyuticitta | death Cognition | terminal Cognition in that life-continuum |

## 8. Logical Determination

**Kārikā, derived.** An opening named the Space Principle with a reported
nature; an Impure Cognition named the Cognition Principle; every member of
the six supports birth.

```nltk-sem
# derived by the section 4 parse
(exists x.(Opening(x) & Named(x,space_principle) & ReportedNature(x,light_and_darkness)) & exists y.(Cognition(y) & Impure(y) & Named(y,cognition_principle)) & all p.(InSixfold(p) -> SupportOfBirth(p)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(exists x.(Opening(x) & Named(x,space_principle) & ReportedNature(x,light_and_darkness)) & exists y.(Cognition(y) & Impure(y) & Named(y,cognition_principle)) & all p.(InSixfold(p) -> SupportOfBirth(p)))
# THEORY prose
# EXPECT prose T
InSixfold(earth) & InSixfold(water) & InSixfold(fire) & InSixfold(wind) & InSixfold(space_member) & InSixfold(cognition_member)
all x.(Named(x,space_principle) -> (Opening(x) & -Unconditioned(x) & IncludedIn(x,form_principle)))
Unconditioned(unconditioned_space) & -Named(unconditioned_space,space_principle)
all y.(Named(y,cognition_principle) -> (Impure(y) & IncludedIn(y,seven_cognition_principles)))
exists z.(Cognition(z) & Pure(z) & -Named(z,cognition_principle) & -Unconditioned(z))
all x.((InSixfold(x) & ElementPrinciple(x)) -> IncludedIn(x,tangible_principle))
ElementPrinciple(earth) & ElementPrinciple(water) & ElementPrinciple(fire) & ElementPrinciple(wind)
all x.(InSixfold(x) -> exists t.(Eighteenfold(t) & IncludedIn(x,t)))
SpansFrom(birth_span,rebirth_linking) & SpansTo(birth_span,death_cognition)
AttributedToOthers(second_agha_account) & -Resolved(cittastha)
# THEORY rejected_space_principle_is_unconditioned
# EXPECT rejected_space_principle_is_unconditioned F
exists x.(Named(x,space_principle) & Unconditioned(x))
# THEORY rejected_every_cognition_is_the_principle_here
# EXPECT rejected_every_cognition_is_the_principle_here F
all y.(Cognition(y) -> Named(y,cognition_principle))
# THEORY rejected_only_cognition_supports_birth
# EXPECT rejected_only_cognition_supports_birth F
all p.(SupportOfBirth(p) -> Named(p,cognition_principle))
# THEORY rejected_pure_means_unconditioned
# EXPECT rejected_pure_means_unconditioned F
all z.(Pure(z) -> Unconditioned(z))
# THEORY rejected_six_add_principles
# EXPECT rejected_six_add_principles F
exists x.(InSixfold(x) & -exists t.(Eighteenfold(t) & IncludedIn(x,t)))
# THEORY rejected_cittastha_resolved
# EXPECT rejected_cittastha_resolved F
exists w.(w = cittastha & Resolved(w))
```

```nltk-valuation
space_principle => space_name
cognition_principle => cognition_name
light_and_darkness => aloka_tamas
earth => earth_m
water => water_m
fire => fire_m
wind => wind_m
space_member => opening_m
cognition_member => impure_cognition_m
unconditioned_space => akasa_asamskrta
form_principle => rupa_dhatu
tangible_principle => sprastavya_dhatu
seven_cognition_principles => seven_vijnana_dhatu
birth_span => janma_span
rebirth_linking => pratisandhi_citta
death_cognition => cyuti_citta
second_agha_account => apare_agha
cittastha => cittastha_reading
Opening => {opening_m}
Named => {(opening_m,space_name),(impure_cognition_m,cognition_name)}
ReportedNature => {(opening_m,aloka_tamas)}
Cognition => {impure_cognition_m,pure_cognition_m}
Impure => {impure_cognition_m}
Pure => {pure_cognition_m}
InSixfold => {earth_m,water_m,fire_m,wind_m,opening_m,impure_cognition_m}
SupportOfBirth => {earth_m,water_m,fire_m,wind_m,opening_m,impure_cognition_m}
Unconditioned => {akasa_asamskrta}
ElementPrinciple => {earth_m,water_m,fire_m,wind_m}
Eighteenfold => {rupa_dhatu,sprastavya_dhatu,seven_vijnana_dhatu}
IncludedIn => {(earth_m,sprastavya_dhatu),(water_m,sprastavya_dhatu),(fire_m,sprastavya_dhatu),(wind_m,sprastavya_dhatu),(opening_m,rupa_dhatu),(impure_cognition_m,seven_vijnana_dhatu)}
SpansFrom => {(janma_span,pratisandhi_citta)}
SpansTo => {(janma_span,cyuti_citta)}
AttributedToOthers => {apare_agha}
Resolved => {}
```

**Model checks.** Six distinct members map four/one/one: the four
Element Principles to the Tangible Principle, the opening to the Form Principle,
Impure Cognition among the seven Cognition Principles. Removing the
reported nature, the Impure restriction, or birth-support from any member
falsifies the derived formula. Unconditioned space is not named the Space
Principle here; a Pure Cognition exists, is not named the Cognition
Principle in this list, and is not unconditioned. No member is left
outside the eighteen. *Cittastha* stays unresolved.

**Bhāṣya determination.** The opening is located in doors, windows, mouth,
nose, and the like; nothing other than light and darkness, night and day,
is apprehended as opening. Two accounts of *aghasāmantaka* follow; the
second is attributed to others. Pure Dharmas are excluded because they
are not common to the course from rebirth-linking Cognition through death
Cognition.

**Organon interpretation.** This is the worked demonstration of the
classification engine. A received six-Principle teaching enters; each
member's scope is determined (conditioned opening, Impure Cognition); the
assignment function maps four/one/one into the eighteen; no new Principle
results. Scope is set by the teaching's purpose: support of birth. Name
alone never fixes identity. With 1.24–1.28 the engine is specified:
naming, closure, measure, assignment, demonstration. From 1.29 the chapter
examines how the classification is applied. The earlier schematic follows.

The verse and Bhāṣya reject two unrestricted inferences:

```text
Named(x, SpacePrinciple)
    ↛ IdenticalTo(x, UnconditionedSpace)

Named(y, CognitionPrinciple)
    ↛ IncludesEveryKindOfCognition(y)
```

The local determinations and cross-mapping are:

```text
SpacePrincipleInSixfoldTeaching
    = ConditionedOpening
    → ReportedAs(LightAndDarkness)
    → IncludedIn(FormPrinciple)

CognitionPrincipleInSixfoldTeaching
    = ImpureCognition
    → IncludedAmong(SevenCognitionPrinciples)

Earth | Water | Fire | Wind Principles
    → IncludedIn(TangiblePrinciple)
```

Their shared function is:

```text
MemberOf(x, SixPrincipleTeaching)
    → Supports(x, BirthContinuum)

Pure(x)
    → NotCommonTo(x, BirthSpanDescribedHere)
    → ExcludedFrom(CognitionPrincipleInThisTeaching)
```

Thus the sixfold teaching is reintegrated within the eighteen Principles;
its entries do not become additional Principles outside that arrangement.

## 9. Interpretive Note

**Translation note.** Kila marks the reported light-and-darkness explanation;
the Bhāṣya locates the opening in doors, windows, mouth, nose, and similar
places, and explains light and darkness as night and day. It restricts the
Cognition Principle here to Impure Cognition and treats the six as supports
from rebirth-linking through death; their assignments are four in the tangible
Principle, the fifth in the visible-Form Principle, and the sixth among the
seven Cognition Principles. The Bhāṣya's reading cittasthaṃ is retained but
remains difficult; the local HTML does not independently confirm it.

VAK 1.28 is the worked case following the assignment procedure of 1.27.
The *Bahudhātuka* teaching gives six Principles. The Bhāṣya specifies the
two initially unexplained members: the Space Principle is an opening
apprehended through light and darkness, and the Cognition Principle is
Impure Cognition. It then maps the six into the eighteen Principles:
four into the Tangible Principle, one into the Form Principle, and one
among the seven Cognition Principles.

The Space Principle here is not unconditioned space. The shared word
*ākāśa* does not erase the distinction between non-obstruction and the
conditioned opening described in this passage. Likewise, the restriction
to Impure Cognition applies to this birth-support list; it does not
define Cognition in every context.

The six-Principle teaching is assigned into the eighteen. The Space Principle
here is the conditioned opening, not unconditioned space. The Cognition Principle
here is Impure Cognition, one member among the seven, not Cognition as such.

The six Principles are supports of a life-continuum extending, in the
Bhāṣya's account, from rebirth-linking Cognition through death Cognition.
The classification is functional as well as referential: the included
Cognition is the Cognition common to that birth-span. The difficult
`cittasthaṃ` belongs to the Bhāṣya's explanation of *aghasāmantaka-rūpa*,
not to this kārikā's wording, and remains unresolved in the separate
commentary study.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_28
    a vak:Karika ;
    rdfs:label "VAK 1.28" ;
    vak:hasTopic vak:ReintegrationOfSixPrinciples ;
    vak:belongsTo vak:Dhatunirdesa .

vak:UnconditionedSpace
    a vak:AsamskrtaDharma ;
    vak:hasCharacteristic vak:NonObstruction ;
    vak:distinctFrom vak:ConditionedSpacePrinciple .

vak:ConditionedSpacePrinciple
    a vak:ConditionedOpening ;
    vak:reportedAs vak:Light , vak:Darkness ;
    vak:includedIn vak:FormPrinciple .

vak:CognitionPrincipleInSixfoldTeaching
    a vak:ImpureCognition ;
    vak:supports vak:BirthContinuum ;
    vak:includedAmong vak:SevenCognitionPrinciples ;
    vak:excludes vak:PureCognition .

vak:SixPrincipleTeaching vak:assignedInto vak:EighteenPrinciples .
```
