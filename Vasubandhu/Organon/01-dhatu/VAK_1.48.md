# VAK_1.48

## 1. Sanskrit (Devanāgarī)

> पञ्च बाह्या द्विविज्ञेया नित्या धर्मा असंस्कृताः ।
>
> धर्मार्धमिन्द्रियं ये च द्वादशाध्यात्मिकाः स्मृताः ॥ १.४८ ॥

The immediate source's `दिविज्ञेयाः` is read as the compound
`द्विविज्ञेयाः`, confirmed by the Bhāṣya: each of the five is knowable by two
knowledge-Domains.

## 2. Sanskrit (IAST)

> pañca bāhyā dvivijñeyā nityā dharmā asaṃskṛtāḥ /
>
> dharmārdham indriyaṃ ye ca dvādaśādhyātmikāḥ smṛtāḥ // 1.48 //

## 3. Lexical Analysis

```text
bāhyāḥ              → bāhyāḥ
dvivijñeyāḥ         → dvi-vijñeyāḥ
nityāḥ               → nityāḥ
dharmāḥ asaṃskṛtāḥ  → dharmāḥ asaṃskṛtāḥ
dharmārdham          → dharma-ardham
dvādaśādhyātmikāḥ   → dvādaśa adhyātmikāḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| pañca | numeral | five: visible form, sound, smell, taste, and tangible object |
| bāhyāḥ | nominative masculine plural adjective | external Domains |
| dvi-vijñeyāḥ | nominative masculine plural compound | knowable by two knowledge-Domains |
| nityāḥ | nominative masculine plural adjective | permanent |
| dharmāḥ | nominative masculine plural | dharmas / determinations |
| asaṃskṛtāḥ | nominative masculine plural adjective | unconditioned; not produced by conditions |
| dharma-ardham | nominative neuter singular compound | a portion of the Dharma-Domain |
| indriyam | nominative neuter singular | possessing faculty-status / a faculty |
| ye | nominative masculine plural relative pronoun | those which |
| ca | conjunction | and; joins the internal twelve to the faculty-distribution |
| dvādaśa | numeral | twelve |
| adhyātmikāḥ | nominative masculine plural adjective | internal |
| smṛtāḥ | nominative masculine plural past participle | taught, recognized, or recalled as |

The agreement alternates according to the supplied head: `dhātavaḥ` is
understood with the masculine plurals, while `dharmārdham` is neuter singular.

## 4. Grammar

The verse condenses answers to three successive questions. First, which of
the eighteen Domains are knowable by which kinds of knowledge?

```text
pañca bāhyāḥ dvi-vijñeyāḥ
    the five external Domains are knowable by two
```

The Bhāṣya identifies the two: each external object is experienced by its
corresponding sensory knowledge and known by mental knowledge. The remaining
thirteen Domains are objects only of mental knowledge.

Second, which Domains are permanent?

```text
nityāḥ dharmāḥ asaṃskṛtāḥ
    the permanent dharmas are the unconditioned
```

The sentence does not say that the entire Dharma-Domain is permanent. The
Bhāṣya explicitly states that no complete Domain (`sakalo dhātuḥ`) is
permanent. Only the unconditioned portion of the Dharma-Domain is permanent;
the remainder is impermanent.

Third, what in the eighteen-Domain system has faculty-status?

```text
dharma-ardham indriyam
    a portion of the Dharma-Domain has faculty-status

ye ca dvādaśa adhyātmikāḥ smṛtāḥ
    as do [elements among] those twelve taught as internal
```

The Bhāṣya supplies the exact mapping. `Ardha` here is a non-mathematical
“portion.” Faculty-status belongs to complete Domains in some cases and to
portions of Domains in others.

## 5. Translation

### Close syntactic construe

> The five external [Domains] are knowable by two. The permanent dharmas are the unconditioned. A portion of the Dharma-Domain has faculty-status, as do those [among] the twelve taught as internal.

### Bhāṣya-informed translation

> Each of the five external object-Domains is knowable both by its corresponding sensory knowledge and by mental knowledge; the other thirteen are knowable only by mental knowledge. No entire Domain is permanent: only the unconditioned dharmas, which form a portion of the Dharma-Domain, are permanent. Faculty-status belongs to portions of the Dharma-Domain and to the relevant Domains or portions contained among the twelve internal Domains.

## 6. Philosophical Translation

> The completed system distinguishes Domain from mode of access, whole from part, conditioned status from permanence, and classification from function. One external object can enter both sensory and mental knowledge. One Domain can contain both impermanent conditioned dharmas and permanent unconditioned dharmas. Faculty-status can occupy a whole Domain or only part of one. The classifications overlap without collapsing into one another.

Organon rendering:

> The Dhātu System closes as a System of Knowledge whose classifications are mutually articulated but irreducible. Externality does not mean exclusion from mind; permanence does not belong to an entire Domain; and faculty does not name a second inventory beside the Domains. Dhātu supplies the stable architecture through which objects, knowledges, conditions, and powers can be cross-classified. The Kośa is logical in this articulated operation, but it neither makes Logic nor becomes a Science of Logic.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| bāhya | external | the five sensory object-Domains |
| dvi-vijñeya | knowable by two | accessible to corresponding sensory knowledge and mental knowledge |
| anubhūta | sensorily experienced | Bhāṣya term for the first mode of access |
| manovijñāna | mental knowledge | the second mode of access to the external five; sole access to the remaining thirteen |
| nitya | permanent | predicated only of unconditioned dharmas here |
| anitya | impermanent | status of all conditioned dharmas |
| asaṃskṛta | unconditioned | not produced through conditioning causes |
| sakala dhātu | complete Domain | no complete Domain is permanent |
| dharmadhātvekadeśa | portion of the Dharma-Domain | locus of the unconditioned and of several faculties |
| dharmārdha | portion of the Dharma-Domain | non-arithmetic expression for the relevant part |
| indriya | faculty / governing power | functional status distributed across Domains and Domain-parts |
| sālambana | possessing an object-support | Bhāṣya's reason for placing mind among object-directed faculties |
| adhyātmika | internal | the twelve faculty- and knowledge-side Domains recalled from 1.39 |

## 8. Logical Determination

The knowability partition is:

```text
ExternalFive
    = {VisibleForm, Sound, Smell, Taste, TangibleObject}

For each x in ExternalFive:
    KnowableBy(x, CorrespondingSensoryKnowledge)
    ∧ KnowableBy(x, MentalKnowledge)

For each x in RemainingThirteen:
    KnowableBy(x, MentalKnowledge)
    ∧ not KnowableBy(x, SensoryKnowledge)
```

The permanence partition requires part-whole precision:

```text
No x such that:
    CompleteDomain(x) ∧ Permanent(x)

UnconditionedDharma(x)
    → Permanent(x)
    ∧ PartOf(x, DharmaDomain)

ConditionedDharma(x)
    → Impermanent(x)
```

Thus it is invalid to infer:

```text
ContainsPermanentPart(DharmaDomain)
    → Permanent(DharmaDomain)
```

Faculty-status cross-cuts Domain identity:

```text
FacultyStatus(x)
    may apply to CompleteDomain(x)
    or DomainPart(x)

Domain(x)
    ↛ Faculty(x)

Faculty(x)
    ↛ CompleteDomain(x)
```

The Bhāṣya's principal mapping includes:

```text
FiveSensoryFacultyDomains
    → their five corresponding faculties

SevenCittaDomains
    → MindFaculty

PartOf(BodyDomain)
    → FemaleFaculty, MaleFaculty

RelevantPartsOf(DharmaDomain)
    → remaining mental, vital, affective, and path faculties
```

The completed System therefore operates through intersecting predicates:

```text
DomainIdentity
Knowability
ConditionStatus
PermanenceStatus
FacultyStatus
InternalExternalStatus

all cross-classify the same dharmic field
without becoming identical classifications
```

This architecture is logical in form. It presupposes and uses determinate
relations; it does not generate the Logic that makes such determination
possible.

## 9. Interpretive Note

The last verse does not culminate in one privileged substance. It completes a
matrix. The five external object-Domains are “external” yet remain available
to mental knowledge after sensory experience. The distinction between
external and internal is therefore a classification of Domain-role, not an
absolute barrier against mental appropriation.

The permanence result is equally exact. Space and the two cessations were
already placed among the unconditioned dharmas, but they occupy only a portion
of the Dharma-Domain. Consequently the Dharma-Domain contains both permanent
and impermanent dharmas. The Domain is not itself converted into an eternal
whole by containing an unconditioned part.

The final faculty-mapping displays the chapter's mature method. The eighteen
Domains and twenty-two faculties are not competing inventories. `Indriya` is
a functional classification laid across the Domain-system. Five sensory
faculty-Domains bear faculty-status under their own names; the seven citta-
Domains together constitute the mind-faculty; sex faculties occupy portions
of the body-Domain; and numerous other faculties occupy portions of the
Dharma-Domain. Some Domains and Domain-parts are not faculties at all.

This finishes the Dhātu System as a System of Knowledge. It began from the
classification of dharmas and arrived at a structured field in which:

```text
faculty gives a specific capacity of access
object gives a determinate field of access
knowledge gives the event of disclosure
Dharma-Domain gathers non-sensory objects and determinations
cross-classifications specify status, range, and function
```

That is why “element” is so damaging when allowed to govern the imagination.
The chapter has not accumulated outward pieces. It has constructed Domains of
knowing and shown how their powers, objects, events, and statuses interlock.
Its reasoning is thoroughly logical; its achievement remains the Kośa's
systematic technē of knowledge, subordinate to the Organon's Logic and Yoga.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_48
    a vak:Karika ;
    rdfs:label "VAK 1.48" ;
    vak:hasTopic vak:CompletionOfDhatuSystem ;
    vak:belongsTo vak:Dhatunirdesa .

vak:ExternalFiveDomains
    a vak:DomainGroup ;
    vak:knowableBy vak:CorrespondingSensoryKnowledge,
        vak:MentalKnowledge .

vak:RemainingThirteenDomains
    a vak:DomainGroup ;
    vak:knowableBy vak:MentalKnowledge .

vak:UnconditionedDharmas
    vak:hasStatus vak:Permanent ;
    vak:partOf vak:DharmaDomain .

vak:DharmaDomain
    vak:hasPart vak:ConditionedDharmas,
        vak:UnconditionedDharmas,
        vak:FacultyBearingPart,
        vak:NonFacultyPart ;
    vak:notWholly vak:Permanent .

vak:FacultyStatus
    a vak:CrossDomainFunctionalClassification ;
    vak:mayClassify vak:CompleteDomain,
        vak:DomainPart .

organon:KosaDhatuSystem
    a organon:SystemOfKnowledge,
        organon:LogicalTechne ;
    organon:presupposes organon:Logic ;
    organon:notIdenticalWith organon:ScienceOfLogic ;
    organon:classifiesBy vak:DomainIdentity,
        vak:KnowabilityStatus,
        vak:ConditionStatus,
        vak:PermanenceStatus,
        vak:FacultyStatus,
        vak:InternalExternalStatus .
```
