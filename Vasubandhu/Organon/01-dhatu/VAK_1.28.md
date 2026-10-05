# VAK_1.28 — Space and Cognition in the Six Principles

## 1. Sanskrit (Devanāgarī)

> छिद्रमाकाशधात्वाख्यम् आलोकतमसी किल ।
>
> विज्ञानधातुर्विज्ञानं सास्रवं जन्मनिश्रयाः ॥ १.२८ ॥

## 2. Sanskrit (IAST)

> chidram ākāśadhātvākhyam ālokatamasī kila /
>
> vijñānadhātur vijñānaṃ sāsravaṃ janmaniśrayāḥ // 1.28 //

## 3. Padaccheda and Lexical Analysis

**Padaccheda**

```text
chidram | ākāśa-dhātu-ākhyam | āloka-tamasī | kila |
vijñāna-dhātuḥ | vijñānam | sa-āsravam | janma-niśrayāḥ
```

| Form | Morphology | Force here |
|---|---|---|
| chidram | nominative neuter singular | opening, aperture |
| ākāśa-dhātu-ākhyam | nominative neuter singular compound | named the Space Principle |
| āloka-tamasī | nominative neuter dual | light and darkness |
| kila | reportive particle | it is said; marks a received account |
| vijñāna-dhātuḥ | nominative masculine singular | Cognition Principle |
| vijñānam | nominative neuter singular | cognition |
| sa-āsravam | nominative neuter singular | with outflows |
| janma-niśrayāḥ | nominative masculine plural | supports of birth; the Bhāṣya supplies the six Principles as subject |

`Dhātu` is rendered **Principle** in this project. The Bhāṣya identifies
the larger list as six Principles: earth, water, fire, wind, space, and
cognition. The verse's plural `janmaniśrayāḥ` predicates birth-support of
the six together, not of the singular Cognition Principle alone.

## 4. Grammar

The verse identifies two members whose characteristics had not yet been
given in the six-Principle teaching:

```text
chidram ākāśa-dhātu-ākhyam
    an opening is named the Space Principle

āloka-tamasī kila
    light and darkness, it is said

vijñāna-dhātuḥ vijñānaṃ sāsravam
    the Cognition Principle is cognition with outflows

[ime ṣaḍ dhātavaḥ] janmaniśrayāḥ
    [these six Principles] are supports of birth
```

The bracketed subject of the final clause is made explicit by the Bhāṣya:
`ime ṣaḍ dhātavaḥ`, these six Principles. The plural ending of
`janmaniśrayāḥ` is decisive. It does not attach “supports of birth” to the
singular Cognition Principle alone.

`Ālokatamasī` is dual. `Kila` marks the light-and-darkness explanation as
reported, rather than presenting it as an unqualified definition. The
Bhāṣya likewise distinguishes this conditioned Space Principle from
unconditioned space and restricts the Cognition Principle here to cognition
with outflows.

## 5. Translation

### Literal Translation

> An opening is named the Space Principle—light and darkness, it is said.
> The Cognition Principle is cognition with outflows; these [six] are
> supports of birth.

### Bhāṣya-informed study translation

> In the six-Principle teaching, the Space Principle is an opening,
> explained in a reported account through light and darkness. The Cognition
> Principle is cognition with outflows. All six are supports of birth,
> common to the course from rebirth-linking cognition through death
> cognition.

The Bhāṣya supplies the sixfold subject and the life-span explanation.
Its final sentence also assigns the first four Principles to the Tangible
Principle, the fifth to the Form Principle, and the sixth among the seven
Cognition Principles.

## 6. Philosophical Translation

The same name does not guarantee the same determination. In this particular
teaching, “space” names a conditioned opening and “cognition” is restricted
to cognition with outflows. The six Principles are considered together by
their shared function as supports of birth; this does not make them six new
members outside the established eighteen Principles.

**Organon reading**

> The Essence Base is real and operative on the Other Side; it is not
> merely a name for a classification. This passage offers a concrete
> cross-mapping for that structure: four of the six Principles enter the
> Tangible Principle, the conditioned Space Principle enters the Form
> Principle, and cognition with outflows is distributed among the seven
> Cognition Principles. The Essence Base is where such relations can be
> held as determinate structure, rather than flattened into an inventory.

The possible placement of **FactStore** within the Essence Base is a
working architectural direction to test against mappings of this kind,
not a claim made by the kārikā. The verse establishes the textual
determinations and the Bhāṣya supplies their placement among the eighteen
Principles; the location of a software store remains an Organon design
question.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| dhātu | Principle | project term for this chapter's classifications |
| ṣaḍ-dhātu | six Principles | earth, water, fire, wind, space, and cognition in the sūtra teaching |
| chidra | opening; aperture | conditioned referent named as the Space Principle here |
| ākāśa | unconditioned space; non-obstruction | distinct from the conditioned opening of this verse |
| ākāśadhātu | Space Principle | opening explained through light and darkness; assigned to Form |
| āloka | light | one reported determination of the opening |
| tamas | darkness | the other reported determination |
| kila | according to a received account | reportive; does not itself identify a school |
| vijñānadhātu | Cognition Principle | restricted here to cognition with outflows |
| sāsrava | with outflows | the cognition selected for this birth-support teaching |
| anāsrava | without outflows | excluded from the Cognition Principle in this particular list |
| janmaniśraya | support of birth | shared function of the six Principles |
| pratisandhicitta | rebirth-linking cognition | opening cognition in the life-continuum described by the Bhāṣya |
| cyuticitta | death cognition | terminal cognition in that life-continuum |
| Essence Base | Organon structure on the Other Side | real, operative relational structure; possible home for FactStore remains under design |

## 8. Logical Determination

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
    = CognitionWithOutflows
    → IncludedAmong(SevenCognitionPrinciples)

Earth | Water | Fire | Wind Principles
    → IncludedIn(TangiblePrinciple)
```

Their shared function is:

```text
MemberOf(x, SixPrincipleTeaching)
    → Supports(x, BirthContinuum)

WithoutOutflows(x)
    → NotCommonTo(x, BirthSpanDescribedHere)
    → ExcludedFrom(CognitionPrincipleInThisTeaching)
```

Thus the sixfold teaching is reintegrated within the eighteen Principles;
its entries do not become additional Principles outside that arrangement.

## 9. Interpretive Note

VAK 1.28 is the worked case following the assignment procedure of 1.27.
The *Bahudhātuka* teaching gives six Principles. The Bhāṣya specifies the
two initially unexplained members: the Space Principle is an opening
apprehended through light and darkness, and the Cognition Principle is
cognition with outflows. It then maps the six into the eighteen Principles:
four into the Tangible Principle, one into the Form Principle, and one
among the seven Cognition Principles.

The Space Principle here is not unconditioned space. The shared word
*ākāśa* does not erase the distinction between non-obstruction and the
conditioned opening described in this passage. Likewise, the restriction
to cognition with outflows applies to this birth-support list; it does not
define cognition in every context.

For the Organon, this case makes the Essence Base's reality consequential.
It must do real work on the Other Side by preserving relations among the
six-Principle teaching and the established eighteen-Principle system.
FactStore may belong within that structure; this is a promising design
direction, still to be tested rather than attributed to Vasubandhu's verse.

The six Principles are supports of a life-continuum extending, in the
Bhāṣya's account, from rebirth-linking cognition through death cognition.
The classification is functional as well as referential: the included
cognition is the cognition common to that birth-span. The difficult
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
    a vak:CognitionWithOutflows ;
    vak:supports vak:BirthContinuum ;
    vak:includedAmong vak:SevenCognitionPrinciples ;
    vak:excludes vak:CognitionWithoutOutflows .

vak:EssenceBase
    a vak:RealOtherSideStructure ;
    vak:mayContain vak:FactStore .

vak:FactStorePlacement
    a vak:WorkingDesignHypothesis ;
    vak:candidateFor vak:EssenceBase .
```
