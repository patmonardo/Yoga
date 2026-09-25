# VAK_1.23

## 1. Sanskrit (Devanāgarī)

> प्राक्पञ्च वार्त्तमानार्थ्यात् भौतिकार्थ्याच्चतुष्टयम् ।
>
> दूराशुतरवृत्त्यान्यत् यथास्थानं क्रमोऽथवा ॥ १.२३ ॥

## 2. Sanskrit (IAST)

> prāk pañca vārttamānārthyāt bhautikārthyāc catuṣṭayam /
>
> dūrāśutaravṛttyānyat yathāsthānaṃ kramo 'thavā // 1.23 //

## 3. Lexical Analysis

```text
prāk pañca            → prāk pañca
vārttamānārthyāt      → vārttamāna-arthyāt
bhautikārthyāc        → bhautika-arthyāt ca
catuṣṭayam            → catuṣṭayam
dūrāśutaravṛttyānyat → dūra-āśutara-vṛttyā anyat
yathāsthānam          → yathā-sthānam
kramo 'thavā          → kramaḥ athavā
```

| Form | Morphology | Lexical force here |
|---|---|---|
| prāk | indeclinable adverb | first, earlier in the sequence |
| pañca | numeral | the five sensory faculties |
| vārttamāna | adjective in compound | present, presently occurring |
| arthyāt | ablatival compound ending | because of having such an object |
| bhautika | adjective in compound | derivative from the great elements |
| catuṣṭayam | nominative/accusative neuter singular collective | the group of four: eye, ear, nose, and tongue |
| dūra | adjective/adverb in compound | far, operating at a distance |
| āśutara | comparative adjective in compound | quicker, operating sooner |
| vṛttyā | instrumental feminine singular | by operation or functioning |
| anyat | nominative/accusative neuter singular | the remaining ordering |
| yathā-sthānam | indeclinable adverbial compound | according to location |
| kramaḥ | nominative masculine singular | order, sequence |
| athavā | alternative particle | or alternatively |

The Sanskrit witnesses support `vṛttyā anyat`, contracted as
`vṛttyānyat`. The long instrumental `-yā` must be preserved in both IAST and
Devanāgarī.

## 4. Grammar

The verse compresses a nested ordering of the six faculties. The Bhāṣya
first states the governing dependency:

```text
faculty order
    → corresponding object-domain order
    → corresponding cognition-domain order (in parallel)
```

The first ablative gives a temporal criterion:

```text
prāk pañca vārttamāna-arthyāt
    the five sensory faculties come first
    because they take present objects
```

Manas has an unrestricted object-range. The further division of its objects
appears to include present, other temporal, and non-temporal dharmas, but the
running source's compound is damaged; the Bhāṣya study marks that construal
as provisional.

The second ablative selects four within the five:

```text
bhautika-arthyāt catuṣṭayam
    eye, ear, nose, and tongue come first
    because their objects are derivative matter
```

The body faculty follows because its tactile domain may contain the great
elements themselves, derivative material form, or both.

The instrumental `dūra-āśutara-vṛttyā` supplies two comparative operational
criteria for the remaining internal order:

```text
eye before ear
    → operation at a greater distance

nose before tongue
    → quicker apprehension before food contacts the tongue
```

`Athavā` introduces an alternative explanation. The faculties may instead
be ordered according to the bodily location of their supports: eye, ear,
nose, tongue, and then a damaged clause concerning the body. The reading
that places the body mostly below is provisional. Manas depends upon the
sense faculties but has no determinate spatial site in this account.

## 5. Translation

### Close syntactic construe

> The five come first because they have present objects; the group of four because they have derivative-material objects. The remaining order follows operation at a greater distance or more quickly—or, alternatively, according to location.

### Bhāṣya-informed translation

> The five sensory faculties precede manas because their objects are restricted to the present, whereas mind has a wider object-range. Among the five, eye, ear, nose, and tongue precede body because their objects are derivative matter, while touch may apprehend the great elements, derivative matter, or both. Eye precedes ear by the comparison of distance and nose precedes tongue by the earlier apprehension of food's odor; alternatively, bodily location explains the order, though the body-site clause is damaged.

The Bhāṣya orders objects and cognitions through the faculties; it does not
claim that faculties temporally produce their objects.

## 6. Philosophical Translation

> The established domains are displayed in an order explained through determinate relations: temporal restriction, material constitution of the object, operational reach, priority in the cited food example, and embodied location. Manas concludes the sequence because its object-range is wider than that of the five senses; the alternative account also calls it non-localized.

Organon rendering:

> The Discriminator does not merely decide membership; it produces an intelligible order of presentation. Every position in the domain-system is justified by how a faculty relates to time, content, reach, priority, and embodiment. Sequence is the displayed rationality of the classified whole.

This is an order of cognitive architecture, not a ranking of spiritual worth
among the senses.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| vārttamāna-viṣayatva | present-object restriction | defining temporal range of the five sensory faculties |
| aniyata-viṣaya | unrestricted object-range | manas can take temporally varied and non-temporal objects |
| bhautika | derivative material form | materiality dependent upon the great elements |
| bhautika-viṣayatva | derivative-material objecthood | criterion grouping eye, ear, nose, and tongue |
| bhūta | great element | direct possible content within the tactile field |
| dūra-viṣaya | distance-accessible object | object available without direct bodily contact |
| dūratara-vṛtti | farther operation | places eye before ear |
| āśutara-vṛtti | quicker operation | places nose before tongue |
| adhiṣṭhāna | bodily support or site | localized basis of a sensory faculty |
| yathā-sthāna | according to location | alternative topological ordering principle |
| adeśa-stha | not situated in one place | characterization of manas in the alternative account |
| krama | ordered display | sequence of faculties, objects, and cognitions |

## 8. Logical Determination

The ordering begins with a dependency rule:

```text
Order(Faculties)
    → DeterminesOrder(CorrespondingObjects)
    → DeterminesOrder(CorrespondingCognitions)
```

The first discriminator separates sensory faculty from manas:

```text
SensoryFaculty(f)
    → TakesOnlyPresentObjects(f)
    → OrderedBefore(f, Manas)

Manas(m)
    → HasUnrestrictedObjectRange(m)
```

The second discriminates within the senses:

```text
MemberOf(f, EyeEarNoseTongueGroup)
    → HasDerivativeMaterialObject(f)

BodyFaculty(b)
    → MayTake(b, GreatElement | DerivativeMatter | Both)
```

Operational comparisons refine the order:

```text
Reach(Eye) > Reach(Ear)
    → EyeBeforeEar

AccessPriority(Nose) > AccessPriority(Tongue)
    → NoseBeforeTongue
```

The alternative topological sort is:

```text
eye → ear → nose → tongue → distributed body → non-localized manas
```

For the Organon reconstruction, the Discriminator also arranges an ordered
display:

```text
Classify(x)
    → DetermineRelevantRelations(x)
    → PlaceInOrderedDisplay(x)
```

## 9. Interpretive Note

VAK 1.23 continues the chapter's system setup. Verses 1.18–1.22 determine
membership, unity, classificatory form, causal salience, and category-fit.
This verse explains how the finished domain-system is ordered for exposition.

Its method is plural but not arbitrary. No one relation can order the entire
system. Temporal range separates the senses from mind; material object-type
places touch; reach and speed distinguish paired sensory groups; bodily
topology offers an alternative global sequence. The correct discriminator
selects the criterion appropriate to the local comparison.

Manas is especially important for the inward presentation. It is not placed
last because it is least real. It exceeds the restrictions governing the
five sensory faculties:

```text
sense
    → present object
    → localized material support

manas
    → wider object-range (further details depend on a damaged reading)
    → no single bodily location
```

VAK 1.17 already defined manas as immediately past cognition functioning as
support. The
two determinations belong together: manas is temporally mediating rather than
anatomically localized.

The preparatory method through six verses is:

```text
1.18  intrinsic membership and determinate difference
1.19  domain-unity across numerical multiplicity
1.20  collection, access, and intrinsic source-kind
1.21  causal and systematic salience
1.22  category-fit, justified number, and sequence
1.23  relational ordering and display
```

VAK 1.24 can now ask why the established system gives one
material domain the special designation `rūpa` and gathers the vast Dharma-
field into a single dharma-āyatana.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_23
    a vak:Karika ;
    rdfs:label "VAK 1.23" ;
    vak:hasTopic vak:RelationalOrderingOfDomains ;
    vak:belongsTo vak:Dhatunirdesa .

vak:FacultyOrder
    vak:determines vak:ObjectDomainOrder , vak:CognitionDomainOrder ;
    vak:usesCriterion vak:TemporalRange , vak:MaterialObjectType ,
        vak:OperationalReach , vak:AccessPriority , vak:BodilyLocation .

vak:SensoryFaculty
    vak:takesTemporalObject vak:PresentObject .

vak:Manas
    vak:mayTakeTemporalObject vak:PresentObject , vak:PastObject ,
        vak:FutureObject , vak:NonTemporalObject ;
    vak:hasSpatialStatus vak:NonLocalized .

vak:BodyFaculty
    vak:mayTakeMaterialObject vak:GreatElement , vak:DerivativeMatter .

vak:CoreDiscriminator
    vak:hasTerminalOperation vak:OrderedDomainDisplay .
```
