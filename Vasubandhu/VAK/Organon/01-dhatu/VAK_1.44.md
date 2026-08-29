# VAK_1.44

## 1. Sanskrit (Devanāgarī)

> त्रिभिर्घ्राणादिभिस्तुल्यविषयग्रहणं मतम् ।
>
> चरमस्याश्रयोऽतीतः पञ्चानां सहजश्च तैः ॥ १.४४ ॥

## 2. Sanskrit (IAST)

> tribhir ghrāṇādibhis tulyaviṣayagrahaṇaṃ matam /
>
> caramasyāśrayo 'tītaḥ pañcānāṃ sahajaś ca taiḥ // 1.44 //

## 3. Padaccheda

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
| tribhiḥ | instrumental plural numeral | by the three contact faculties |
| ghrāṇa-ādibhiḥ | instrumental masculine plural | by nose, tongue, and body |
| tulya-viṣaya-grahaṇam | nominative neuter singular compound | apprehension of an object-field equal in extent |
| matam | nominative neuter singular past passive participle | is held or accepted by the relevant school |
| caramasya | genitive masculine singular | of the last knowledge-Domain, mental knowledge |
| āśrayaḥ | nominative masculine singular | determining support or basis |
| atītaḥ | nominative masculine singular | past; ceased immediately before |
| pañcānām | genitive plural | of the five sensory knowledge-Domains |
| sahajaḥ | nominative masculine singular | co-born, simultaneous |
| ca | conjunction | and; adds the past support as well |
| taiḥ | instrumental masculine plural | with those five knowledges |

The conjunction `ca` is doctrinally important. The Bhāṣya explains that the
five sensory knowledges possess both the co-born faculty-support named here
and the immediately past mental support already stated for mental knowledge.

## 4. Grammar

The first line completes the contact classification of VAK 1.43:

```text
ghrāṇa, jihvā, kāya
    → apprehend a contacted object-field
      equal to the operative extent of the faculty
```

The Bhāṣya makes equality quantitative. As many faculty-atoms as participate,
so many object-atoms come together with them to generate knowledge. This
one-to-one rule applies to the three contact faculties.

Eye and ear have no fixed equality of extent. The eye may see a hair-tip, a
grape, or a mountain; the ear may hear a mosquito or thunder. Mind, being
non-material in this analysis, is not delimited by spatial magnitude at all.

The second line distinguishes temporal supports:

```text
caramasya āśrayaḥ atītaḥ
    the support of the last, mental knowledge,
    is immediately past mind

pañcānāṃ sahajaḥ ca taiḥ
    for the five sensory knowledges,
    the respective faculty is co-born with them as support—and past mind also
```

The immediately preceding cognition ceases and is designated `manodhātu`;
it then supports the next mental or sensory knowledge-event. Each sensory
knowledge additionally depends upon its present corresponding faculty.

## 5. Translation

### Close syntactic construe

> The three beginning with the nose are held to apprehend an object-field equal [to themselves]. The support of the last [knowledge-Domain] is past; for the five, a support is also co-born with them.

### Bhāṣya-informed translation

> Nose, tongue, and body apprehend contacted objects through an equal conjunction of faculty-atoms and object-atoms. Mental knowledge is supported by the mind-event that ceased immediately before it. Each of the five sensory knowledges has that past mental support together with a second, simultaneous support—its own co-born sensory faculty.

The second rendering makes the force of `ca` explicit and avoids the false
impression that sensory knowledge lacks the immediately past mental support.

## 6. Philosophical Translation

> Contact cognition is quantitatively coordinated at the point of material conjunction. Sensory knowledge nevertheless depends upon more than present contact: it joins an immediately past mental continuity to a co-arisen faculty. Mental knowledge lacks the second material support and arises through succession from prior mind. Cognitive operation therefore binds magnitude, embodiment, and temporality without reducing one to another.

Organon rendering:

> The Agent's knowledge-events now acquire a support signature. Sensory knowledge is doubly supported by past mental continuity and present faculty-capacity; mental knowledge is supported by the immediately preceding mind-event. Contact faculties additionally enforce equality at their active material interface. This is an instrumental science of cognitive succession and support.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| tulya-viṣaya-grahaṇa | apprehension of an equal object-field | quantitative contact relation for nose, tongue, and body |
| ātma-parimāṇa | a faculty's own extent | measure against which contact-object equality is considered |
| indriya-paramāṇu | faculty-atom | material unit on the faculty side of contact |
| viṣaya-paramāṇu | object-field atom | material unit on the object side of contact |
| sametya | having come together | conjunction through which equal atoms generate knowledge |
| aniyama | absence of a fixed rule | status of magnitude-relation for eye and ear |
| parimāṇa-pariccheda | delimitation by spatial magnitude | inapplicable to non-material mind |
| āśraya | determining support | basis whose condition governs the knowledge-event |
| atīta-āśraya | past support | immediately preceding mind that has ceased |
| sahaja-āśraya | co-born support | present sensory faculty arising with its knowledge |
| samanantara-niruddha | ceased immediately before | temporal specification of mind as support |
| indriya-dvaya-āśraya | having two supports/faculties | sensory knowledge supported by past mind and present sensory faculty |
| tadvikāra-vikāritva | changing when that changes | criterion by which a faculty is called the determining support |

`Āśraya`, `ālambana`, and `viṣaya` remain non-interchangeable:

```text
āśraya
    determining basis

ālambana
    apprehended object-support

viṣaya
    determinate object-field and functional range
```

## 8. Logical Determination

The contact-equality rule is:

```text
x ∈ {NoseFaculty, TongueFaculty, BodyFaculty}
∧ ContactApprehension(x, object)
    → Count(ParticipatingFacultyAtoms)
      = Count(ParticipatingObjectAtoms)
```

No equivalent fixed ratio applies to eye and ear:

```text
x ∈ {EyeFaculty, EarFaculty}
    → ObjectMagnitude(x)
      may be SmallerThan
      ∨ EqualTo
      ∨ GreaterThan FacultyMagnitude(x)
```

Mind is excluded from spatial comparison:

```text
NonMaterial(Mind)
    → ¬SpatialMagnitudeDelimited(Mind)
```

The temporal support chain is:

```text
MentalEvent(t−1)
    → Ceases
    → FunctionsAs(ManoDhatu)
    → Supports(MentalKnowledge(t))
```

Sensory knowledge has two supports:

```text
SensoryKnowledge(t)
    ← SupportedBy(ImmediatelyPastMind(t−1))
    ∧ SupportedBy(CobornSensoryFaculty(t))
```

Thus:

```text
MentalKnowledge
    → OnePastMentalSupport

SensoryKnowledge
    → PastMentalSupport
    + PresentFacultySupport
```

## 9. Interpretive Note

VAK 1.44 binds the faculty's spatial operation to the temporal generation of
knowledge without conflating them.

The contact faculties provide the clearest quantitative determination yet
in the chapter. Their operative material interface is modeled through equal
numbers of faculty-atoms and object-atoms. This equality is local to contact
apprehension. It must not be generalized to eye, ear, or mind.

The second half is still more important for the Principle of the Agent.
Sensory knowledge is not produced by a present faculty confronting an object
in isolation. It also inherits immediately past mind:

```text
past mental continuity
    + present sensory faculty
    + object relation
        → sensory knowledge-event
```

Mental knowledge differs because its determining support is the immediately
past mind alone. The present Dharma-object remains indispensable as object,
but it is not therefore called `āśraya`. VAK 1.45 will state why the faculty,
rather than the object, receives that technical name.

This distinction prevents several reductions:

```text
support
    ≠ object

past mental continuity
    ≠ present faculty

faculty
    ≠ knowledge-event

material magnitude
    ≠ universal measure of cognition
```

The Kośa here supplies a precise Agent-side technē of cognitive succession and
embodied support. Its temporal mental support and sensory instrumentation are
the positive determinations established by the verse.

That technē will be useful to our Yoga only after Yoga supplies its own
principles. The present study should therefore retain the Kośa's powerful
distinctions without granting them the role of Buddhi or the knowledge of
Puruṣa.

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
        vak:ParticipatingObjectAtoms .

vak:MentalKnowledge
    vak:hasSupport vak:ImmediatelyPastMind .

vak:SensoryKnowledge
    vak:hasSupport vak:ImmediatelyPastMind,
        vak:CobornSensoryFaculty .

vak:Asraya
    vak:distinctFrom vak:Alambana,
        vak:Visaya .

organon:AgentSupportSignature
    a vak:AgentSideModel ;
    organon:distinguishes vak:PastMentalSupport,
        vak:CobornFacultySupport,
        vak:ObjectRelation .
```
