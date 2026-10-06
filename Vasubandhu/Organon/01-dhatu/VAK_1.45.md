# VAK_1.45

## 1. Sanskrit (Devanāgarī)

> तद्विकारविकारित्वादाश्रयाश्चक्षुरादयः ।
>
> अतोऽसाधारणत्वाद्धि विज्ञानं तैर्निरुच्यते ॥ १.४५ ॥

## 2. Sanskrit (IAST)

> tadvikāravikāritvād āśrayāś cakṣurādayaḥ /
>
> ato 'sādhāraṇatvād dhi vijñānaṃ tair nirucyate // 1.45 //

## 3. Lexical Analysis

```text
tadvikāravikāritvāt    → tad-vikāra-vikāritvāt
āśrayāś cakṣurādayaḥ   → āśrayāḥ cakṣus-ādayaḥ
ato 'sādhāraṇatvāt     → ataḥ a-sādhāraṇa-tvāt
vijñānaṃ taiḥ          → vijñānam taiḥ
nirucyate              → nirucyate
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| tad-vikāra | compound member | alteration of those Faculties |
| vikāritvāt | ablative neuter singular abstract noun | because Cognition is altered when they are altered |
| āśrayāḥ | nominative masculine plural | supports |
| cakṣus-ādayaḥ | nominative masculine plural compound | Eye and the other Faculties |
| ataḥ | adverb | therefore, for this reason |
| a-sādhāraṇa-tvāt | ablative neuter singular abstract noun | because of being specific, not common |
| hi | explanatory particle | indeed, for |
| vijñānam | nominative neuter singular | Cognition |
| taiḥ | instrumental masculine plural | by those Faculties |
| nirucyate | third-person singular present passive | is designated or named |

The first ablative gives the criterion for support-status. The second gives
the criterion for naming. They are related but not identical arguments.

## 4. Grammar

The commentary begins from dependence on both Faculty and Object.
Its restored opening clause establishes “Principles” as the governing
topic:

```text
Cognition depends upon Faculty
Cognition depends upon Object
```

It then asks why only Eye and the other Faculties are called supports.
The verse answers:

```text
corresponding Faculty alteration
    → corresponding Cognition alteration

Eye and the other Faculties
    → SupportsTheirCorrespondingCognitions
```

The relevant Faculty alterations are benefit or improvement, injury,
acuity, and dullness. Cognition follows these changes. The verse preserves
dependence on both Faculty and Object; the commentary distinguishes the
Object by saying that its alteration does not produce the corresponding
change in Cognition.

The second line answers a naming question. Why say Eye-Cognition,
Ear-Cognition, and so on, rather than Form-Cognition, sound-Cognition, and
so on?

```text
Faculty specificity
    not common to other Cognitions

designation by Faculty
    Cognition is designated by those Faculties
```

One Eye Faculty supports its corresponding Eye-Cognition. Visible Form,
by contrast, may serve as an Object for another person's visual Cognition
and for Mind-Cognition. The Faculty support is specific; the Object is
shareable.

## 5. Translation

### Close syntactic construe

> Eye and the other Faculties are supports because Cognition is altered by their alteration. Therefore Cognition is designated by them, for they are specific and not common.

### Commentary-informed translation

> The Faculties are called supports because benefit, injury, acuity, or dullness in a Faculty produces a corresponding alteration in its Cognition. Cognition is named from its Faculty—Eye-Cognition, Ear-Cognition, and so forth—because each Faculty supports its own specific kind of Cognition, whereas an Object such as visible Form can be shared by many sensory and mental Cognitions.

## 6. Specific Support and Shared Object

The Faculty is the specific support whose alteration corresponds to
alteration in Cognition. An Object such as visible Form can be shared by
Mind-Cognition and another Eye-Cognition. This naming rule distinguishes
the Faculty's support relation from the Object relation without denying
that Cognition depends on both.

## 7. Scope of the Naming Rule

“Support” names the Faculty relation; “Object” names what Cognition is
directed toward. The commentary explicitly contrasts them here; do not
add another relation to this account. The specific Faculty gives
Cognition its name, while an Object may be shared across kinds of
Cognition and across individuals.

## 8. Logical Determination

Cognition has dual dependence:

```text
Arises(Cognition)
    → Requires(FacultySupport)
    ∧ Requires(ObjectRelation)
```

But the dependencies have different functions:

```text
Alter(Faculty,
    Improvement | Injury | Acuity | Dullness)
    → CorrespondinglyAlter(Cognition)
    → DeterminingSupport(Faculty)

ObjectRelation(Object)
    → MayBeSharedAcrossCognitions(Object)
```

The naming rule is:

```text
SupportsOnly(EyeFaculty, EyeCognition)
    → NonCommon(EyeFaculty)
    → NamedFrom(EyeCognition, EyeFaculty)
```

The Object is shareable:

```text
VisibleForm(x)
    → MayBeObjectOf(x, ThisEyeCognition)
    ∧ MayBeObjectOf(x, AnotherPersonEyeCognition)
    ∧ MayBeObjectOf(x, MindCognition)
    → ShareableObject(x)
```

Therefore:

```text
HowCognitionOccurs
    → determined by Support

TowardWhatCognitionIsDirected
    → determined by Object

SpecificSupport
    ≠ ShareableObjectRelation
```

The relation is:

```text
DependsOn(Cognition, SpecificFacultySupport)
    ∧ DependsOn(Cognition, ShareableObjectRelation)
```

## 9. Interpretive Note

VAK 1.45 completes the support analysis begun in 1.44. Cognition does not
arise without an Object, but not every necessary condition has the same
systematic role. The Faculty is called a support because alteration in
the Faculty governs corresponding alteration in Cognition.

Faculty-capacity is therefore graded, not merely present or absent:

```text
benefited or injured
sharp or dull
    → correspondingly altered Cognition
```

The verse also explains the naming of Cognition. Eye-Cognition is named
from the specific Eye Faculty, not from visible Form, which can be an
Object for Cognitions in multiple individuals and for Mind-Cognition.
The account preserves both dependence relations without treating their
roles as interchangeable.

In the governing model, Vijñāna as Discriminative Cognition joins and
governs Perception and Conception. Their unity is Inconceivable as a
homogeneous operation, and its Idea is disclosed in Cognition Base.
Vijñāna governs Manas and guides the reading of Dharma Base. Form Base
and Dharma Base classify the same *avijñapti* distinctly; Vijñāna bears
a *prati* relation to it and remains distinct from consciousness and Mind.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_45
    a vak:Karika ;
    rdfs:label "VAK 1.45" ;
    vak:hasTopic vak:SpecificSupportAndCognitionNaming ;
    vak:belongsTo vak:PrincipleAnalysis .

vak:FacultySupport
    a vak:Support ;
    vak:hasProperty vak:Specificity .

vak:ObjectRelation
    a vak:CognitiveRelation ;
    vak:hasProperty vak:Shareability .

vak:FacultyAlteration
    vak:causesCorrespondingAlterationIn vak:Cognition .

vak:VisibleForm
    a vak:Object ;
    vak:mayBeObjectOf vak:MindCognition,
        vak:AnotherEyeCognition .

vak:Cognition
    vak:namedFrom vak:SpecificFacultySupport ;
    vak:requires vak:FacultySupport,
        vak:ObjectRelation .

organon:SupportObjectDistinction
    a organon:ProjectInterpretation ;
    organon:distinguishes vak:FacultySupport,
        vak:ObjectRelation .
```
