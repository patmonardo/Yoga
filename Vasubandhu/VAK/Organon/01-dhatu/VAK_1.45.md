# VAK_1.45

## 1. Sanskrit (Devanāgarī)

> तद्विकारविकारित्वादाश्रयाश्चक्षुरादयः ।
>
> अतोऽसाधारणत्वाद्धि विज्ञानं तैर्निरुच्यते ॥ १.४५ ॥

## 2. Sanskrit (IAST)

> tadvikāravikāritvād āśrayāś cakṣurādayaḥ /
>
> ato 'sādhāraṇatvād dhi vijñānaṃ tair nirucyate // 1.45 //

## 3. Padaccheda

```text
tadvikāravikāritvāt    → tad-vikāra-vikāritvāt
āśrayāś cakṣurādayaḥ   → āśrayāḥ cakṣus-ādayaḥ
ato 'sādhāraṇatvāt     → ataḥ a-sādhāraṇa-tvāt
vijñānaṃ taiḥ          → vijñānam taiḥ
nirucyate              → nirucyate
```

| Form | Morphology | Lexical force here |
|---|---|---|
| tad-vikāra | compound member | alteration of those faculties |
| vikāritvāt | ablative neuter singular abstract noun | because of undergoing corresponding alteration |
| āśrayāḥ | nominative masculine plural | supports; determining bases of knowledge |
| cakṣus-ādayaḥ | nominative masculine plural compound | eye and the other faculties |
| ataḥ | adverb | therefore, for this reason |
| a-sādhāraṇa-tvāt | ablative neuter singular abstract noun | because of being non-common or specific |
| hi | explanatory particle | indeed, for |
| vijñānam | nominative neuter singular | knowledge |
| taiḥ | instrumental masculine plural | by those faculties |
| nirucyate | third-person singular present passive | is designated or named |

The first ablative gives the criterion for support-status. The second gives
the criterion for naming. They are related but not identical arguments.

## 4. Grammar

The Bhāṣya begins from dual dependence:

```text
knowledge depends upon faculty
knowledge depends upon object
```

It then asks why only eye and the other faculties are called `āśraya`.
The Kārikā answers:

```text
tad-vikāra-vikāritvāt
    because knowledge is altered when those faculties are altered

āśrayāḥ cakṣur-ādayaḥ
    eye and the others are supports
```

The relevant faculty alterations are benefit or improvement, injury,
acuity, and dullness. Knowledge follows these changes. The object remains an
indispensable condition, but its alteration does not determine the capacity
and quality of knowing in this same support-specific manner.

The second line answers a naming question. Why say eye-knowledge,
ear-knowledge, and so on, rather than form-knowledge, sound-knowledge, and
so on?

```text
asādhāraṇatvāt
    because each faculty is non-common to other kinds of knowledge

vijñānaṃ taiḥ nirucyate
    knowledge is designated by those faculties
```

One eye-faculty can support only its corresponding eye-knowledge. Visible
form, by contrast, may become object-support for another person's visual
knowledge and for a subsequent mental knowledge. The support is specific;
the object is shareable.

## 5. Translation

### Close syntactic construe

> Eye and the other faculties are supports because knowledge is altered by their alteration. Therefore knowledge is designated by them, for they are non-common.

### Bhāṣya-informed translation

> The faculties are called determining supports because benefit, injury, acuity, or dullness in a faculty produces a corresponding alteration in its knowledge. Knowledge is named from its faculty—eye-knowledge, ear-knowledge, and so forth—because each faculty supports only its own specific kind of knowledge, whereas an object such as visible form can be shared by many sensory and mental acts of knowledge.

## 6. Philosophical Translation

> A condition becomes the determining support of knowledge when variation in that condition governs variation in the knowing capacity. The object supplies what is apprehended, but the faculty supplies the specific mode through which it can be known. Knowledge therefore receives its name from the non-common faculty rather than from its shareable object.

Organon rendering:

> The Agent's knowledge-event unites specific capacity with common content. The faculty determines how knowing occurs; the object determines toward what it is directed. Alteration of the faculty alters the disclosure, while one object may remain available across several knowers and later mental acts. The Kośa's Domain science thus preserves form of access and shareable objectivity as distinct relations.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| ubhayādhīna | dependent upon both | knowledge depends upon faculty and object |
| tadvikāra-vikāritva | being altered through alteration of that | criterion establishing the faculty as determining support |
| āśraya | support / determining support | specific basis whose condition governs the knowledge-event |
| ālambana | object-support | that upon which knowledge is cognitively directed |
| viṣaya | determinate object-field | kind and range of content appropriate to a faculty |
| anugraha | benefit / improvement | positive modification of faculty-capacity |
| upaghāta | injury / impairment | negative modification of faculty-capacity |
| paṭutā | acuity / sharpness | strengthened precision of faculty and knowledge |
| mandatā | dullness / weakness | diminished precision of faculty and knowledge |
| tadadhīnatva | dependence upon that | stronger dependence grounding support-status |
| asādhāraṇa | non-common / specific | faculty restricted to one corresponding knowledge-kind |
| sādhāraṇa | common / shareable | object available to multiple knowledge-events and continua |
| nirucyate | is designated | principled naming from the specific support |

## 8. Logical Determination

Knowledge has dual dependence:

```text
Arises(KnowledgeEvent)
    → Requires(FacultySupport)
    ∧ Requires(ObjectSupport)
```

But the dependencies have different functions:

```text
Alter(Faculty,
    Improvement | Injury | Acuity | Dullness)
    → CorrespondinglyAlter(KnowledgeEvent)
    → DeterminingSupport(Faculty)

ObjectSupport(Object)
    → SuppliesDirectionAndContent(KnowledgeEvent)
```

The naming rule is:

```text
SupportsOnly(EyeFaculty, EyeKnowledge)
    → NonCommon(EyeFaculty)
    → NamedFrom(EyeKnowledge, EyeFaculty)
```

The object fails this uniqueness test:

```text
VisibleForm(x)
    → MayBeObjectOf(x, ThisEyeKnowledge)
    ∧ MayBeObjectOf(x, AnotherContinuumEyeKnowledge)
    ∧ MayBeObjectOf(x, SubsequentMentalKnowledge)
    → CommonObjectSupport(x)
```

Therefore:

```text
HowKnowledgeOccurs
    → determined by Asraya

TowardWhatKnowledgeOccurs
    → determined through Alambana and Visaya

SpecificSupport
    ≠ ShareableObjectSupport
```

The Agent-side knowledge signature is:

```text
KnowledgeEvent
    = SpecificFacultyDetermination
    + ShareableObjectDirection
```

## 9. Interpretive Note

VAK 1.45 completes the support analysis begun in 1.44. Knowledge does not
arise without an object, but not every necessary condition has the same
systematic role. The faculty earns the name `āśraya` because alteration in
the faculty governs alteration in knowledge.

This makes faculty-capacity graded rather than merely present or absent:

```text
benefited or injured
sharp or dull
    → correspondingly altered knowledge
```

The verse then explains the lineage-name of each knowledge-Domain. Eye-
knowledge is not named from visible form because visible form is common: it
can be seen by many continua and later taken by mental knowledge. The eye is
non-common: it supports only its corresponding visual knowledge within one
continuum.

This is why Dhātu is the indispensable machinery of the chapter. The system
cannot express the result through a generic opposition of subject and
object. It requires distinct Domains and relations:

```text
faculty-Domain
    → specific determining support

object-Domain
    → common object-support and content-field

knowledge-Domain
    → event joining the two relations
```

The Kośa remains Agent-technē. It has not discovered Sāṃkhya Buddhi,
Puruṣa, Prakṛti, or Self-realization. Yet its limited science is powerful:
it determines why cognition varies with its instrument and how one object
can remain shareable across multiple acts of knowledge.

For the later Organon Vārttika, this will support a precise Agent model of
capacity and objectivity. It should not be promoted into Yoga metaphysics or
allowed to touch the Logic infrastructure. The present achievement belongs
entirely to the high-level scientific modeling of the Rational Agent.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_45
    a vak:Karika ;
    rdfs:label "VAK 1.45" ;
    vak:hasTopic vak:DeterminingSupportAndKnowledgeNaming ;
    vak:belongsTo vak:Dhatunirdesa .

vak:FacultySupport
    a vak:Asraya ;
    vak:hasProperty vak:NonCommonness ;
    vak:determines vak:KnowledgeMode .

vak:Object
    a vak:Alambana ;
    vak:hasProperty vak:Commonness ;
    vak:supplies vak:KnowledgeDirection .

vak:FacultyAlteration
    vak:causesCorrespondingAlterationIn vak:KnowledgeEvent .

vak:KnowledgeEvent
    vak:namedFrom vak:SpecificFacultySupport ;
    vak:requires vak:FacultySupport,
        vak:ObjectSupport .

organon:AgentKnowledgeModel
    a vak:AgentSideModel ;
    organon:distinguishes vak:DeterminingSupport,
        vak:ObjectSupport,
        vak:ObjectField .
```
