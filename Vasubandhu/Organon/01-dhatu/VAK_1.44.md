# VAK_1.44

## 1. Sanskrit (Devanāgarī)

> त्रिभिर्घ्राणादिभिस्तुल्यविषयग्रहणं मतम् ।
>
> चरमस्याश्रयोऽतीतः पञ्चानां सहजश्च तैः ॥ १.४४ ॥

## 2. Sanskrit (IAST)

> tribhir ghrāṇādibhis tulyaviṣayagrahaṇaṃ matam /
>
> caramasyāśrayo 'tītaḥ pañcānāṃ sahajaś ca taiḥ // 1.44 //

## 3. Lexical Analysis

```text
tribhir ghrāṇādibhiḥ       → tribhiḥ ghrāṇa-ādibhiḥ
tulyaviṣayagrahaṇam        → tulya-viṣaya-grahaṇam
caramasyāśrayaḥ            → caramasya āśrayaḥ
'tītaḥ                     → atītaḥ
pañcānāṃ sahajaḥ          → pañcānām sahajaḥ
ca taiḥ                    → ca taiḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| tribhiḥ | instrumental plural numeral | by the three Faculties |
| ghrāṇa-ādibhiḥ | instrumental masculine plural | by Nose, Tongue, and Body |
| tulya-viṣaya-grahaṇam | nominative neuter singular compound | Cognition of a field equal in extent |
| matam | nominative neuter singular past passive participle | is held or accepted by the relevant school |
| caramasya | genitive masculine singular | of the last Cognition Principle, Mind-Cognition |
| āśrayaḥ | nominative masculine singular | support |
| atītaḥ | nominative masculine singular | past; ceased immediately before |
| pañcānām | genitive plural | of the five sensory Cognitions |
| sahajaḥ | nominative masculine singular | co-born, simultaneous |
| ca | conjunction | and; also, preserving the past support |
| taiḥ | instrumental masculine plural | with those five Cognitions |

The conjunction `ca` is important. The Bhāṣya explains that the five sensory
Cognitions have both the co-born Faculty support named here and the
immediately past Mind support.

## 4. Grammar

The first line specifies an extent relation for the three Faculties that
operate through contact, continuing the classification of VAK 1.43:

```text
Nose, Tongue, Body
    → contact a field equal in extent to the participating Faculty

```

The Bhāṣya makes equality quantitative: as many Faculty atoms as participate,
so many field atoms come together to generate Cognition. This equal-count
relation applies to the three contact Faculties.

The Bhāṣya says Eye and Ear have no fixed equality of extent. The Eye may
disclose a hair-tip, a grape, or a mountain; the Ear may hear a mosquito or
thunder. Mind is not Form, so spatial magnitude does not delimit its field.

The second line distinguishes temporal supports:

```text
caramasya āśrayaḥ atītaḥ
    the support of the last Cognition Principle,
    Mind-Cognition, is past

pañcānāṃ sahajaḥ ca taiḥ
    for the five sensory Cognitions, their respective Faculty
    is a co-born support—and the past Mind support also applies
```

The immediately preceding Mind-Cognition ceases and functions as the Mind
Principle supporting the next mental or sensory Cognition. Each sensory
Cognition also depends on its corresponding co-born Faculty.

## 5. Translation

### Close syntactic construe

> The three beginning with the Nose are held to Cognize a field equal [in extent]. The support of the last [Cognition Principle] is past; for the five, a support is also co-born with them.

### Bhāṣya-informed translation

> Nose, Tongue, and Body Cognize contacted fields through an equal conjunction of Faculty atoms and field atoms. Mind-Cognition is supported by the Mind-Cognition that ceased immediately before it. Each of the five sensory Cognitions has that past Mind support together with a second, simultaneous support—its own co-born sensory Faculty.

The second rendering makes the force of `ca` explicit: the sensory Cognitions
have a co-born Faculty support as well as the immediately past Mind support.

## 6. Philosophical Translation

> For Nose, Tongue, and Body, contact Cognition coordinates the extent of the Faculty and its field. Sensory Cognition also depends on a past Mind support as well as its co-born Faculty. Mind-Cognition depends on the immediately preceding Mind support. The verse thus distinguishes extent in contact from temporal and co-born support.

Organon rendering:

> Within the Principle Pipeline, contact Faculties impose an equal-extent relation between Faculty and field. A sensory Cognition stands on both immediately past Mind and its co-born Faculty; Mind-Cognition stands on immediately past Mind. The verse specifies different support relations without collapsing Faculty, field, and Cognition.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| tulya-viṣaya-grahaṇa | Cognition of an equal-extent field | quantitative contact relation for Nose, Tongue, and Body |
| ātma-parimāṇa | a Faculty's own extent | measure against which contact-field equality is considered |
| indriya-paramāṇu | Faculty atom | unit on the Faculty side of contact |
| viṣaya-paramāṇu | field atom | unit on the field side of contact |
| sametya | having come together | conjunction through which equal atoms generate Cognition |
| aniyama | absence of a fixed rule | no fixed extent relation for Eye and Ear |
| parimāṇa-pariccheda | delimitation by spatial magnitude | inapplicable to Mind, which is not Form |
| āśraya | support | condition on which Cognition depends |
| atīta-āśraya | past support | immediately preceding Mind-Cognition that has ceased |
| sahaja-āśraya | co-born support | sensory Faculty arising with its Cognition |
| samanantara-niruddha | ceased immediately before | temporal specification of Mind as support |
| indriya-dvaya-āśraya | having two supports | sensory Cognition supported by past Mind and present sensory Faculty |

`Āśraya`, `ālambana`, and `viṣaya` remain distinct:

```text
āśraya
    support on which Cognition depends

ālambana
    field-support toward which Cognition is directed

viṣaya
    determinate field and functional range
```

## 8. Logical Determination

The contact-equality rule is:

```text
x ∈ {NoseFaculty, TongueFaculty, BodyFaculty}
∧ ContactCognition(x, field)
    → Count(ParticipatingFacultyAtoms)
      = Count(ParticipatingFieldAtoms)
```

No equivalent fixed ratio applies to eye and ear:

```text
x ∈ {EyeFaculty, EarFaculty}
    → FieldExtent(x)
      may be SmallerThan
      ∨ EqualTo
      ∨ GreaterThan FacultyMagnitude(x)
```

Mind is excluded from spatial comparison:

```text
NotForm(Mind)
    → ¬SpatialMagnitudeDelimited(Mind)
```

The temporal support chain is:

```text
MindCognition(t−1)
    → Ceases
    → FunctionsAs(MindPrinciple)
    → Supports(MindCognition(t))
```

Each sensory Cognition has two supports:

```text
SensoryCognition(t)
    ← SupportedBy(ImmediatelyPastMind(t−1))
    ∧ SupportedBy(CoBornSensoryFaculty(t))
```

Thus:

```text
MindCognition
    → OnePastMentalSupport

SensoryCognition
    → PastMentalSupport
    + PresentFacultySupport
```

## 9. Interpretive Note

VAK 1.44 places two determinations within the Principle Pipeline without
collapsing them: extent at the contact interface, and the support relations
through which Cognition arises.

For Nose, Tongue, and Body, the Bhāṣya describes equal counts of participating
Faculty atoms and field atoms. It does not generalize that equality to Eye or
Ear, and Mind has no spatial measure in this account.

The verse's `ca` also matters: sensory Cognition does not stand on its
co-born Faculty alone. It inherits the immediately past Mind support:

```text
immediately past Mind
    + co-born sensory Faculty
    + field relation
        → sensory Cognition
```

Mind-Cognition depends on the immediately preceding Mind support. In project
terms, Dhātu is Pure Principle—Abhidharma itself—and these differentiated
Cognitions are impure *prajñā* products grounded in their support relations.
A product remains a Principle within the recursive Pipeline because it
stands on Principles. This is the Organon model, not wording attributed to
the Bhāṣya.

This distinction prevents several reductions:

```text
support
    ≠ field

past Mind support
    ≠ co-born Faculty support

Faculty
    ≠ Cognition

contact extent
    ≠ universal measure of Cognition
```

The verse's technical distinctions are the equal-extent contact relation,
past Mind support, and co-born sensory Faculty support. The pipeline model
keeps these relations explicit without turning the verse into a flat list
of Cognitions or attributing the project ontology to Vasubandhu.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_44
    a vak:Karika ;
    rdfs:label "VAK 1.44" ;
    vak:hasTopic vak:QuantitativeContactAndTemporalSupport ;
    vak:belongsTo vak:Dhatunirdesa .

vak:ContactFaculty
    vak:hasConstraint vak:EqualAtomicContact .

vak:EqualAtomicContact
    vak:requiresEqualCount vak:ParticipatingFacultyAtoms,
        vak:ParticipatingFieldAtoms .

vak:MindCognition
    vak:hasSupport vak:ImmediatelyPastMind .

vak:SensoryCognition
    vak:hasSupport vak:ImmediatelyPastMind,
        vak:CoBornSensoryFaculty .

vak:Asraya
    vak:distinctFrom vak:Alambana,
        vak:Visaya .

organon:PrinciplePipelineSupport
    a organon:PipelineRelationModel ;
    organon:distinguishes vak:PastMentalSupport,
        vak:CobornFacultySupport,
        vak:ObjectRelation .
```
