# VAK_1.25

## 1. Sanskrit (Devanāgarī)

> धर्मस्कन्धसहस्राणि यान्यशीतिं जगौ मुनिः ।
>
> तानि वाङ्नाम वेत्येषां रूपसंस्कारसंग्रहः ॥ १.२५ ॥

## 2. Sanskrit (IAST)

> dharmaskandhasahasrāṇi yāny aśītiṃ jagau muniḥ /
>
> tāni vāṅnāma vety eṣāṃ rūpasaṃskārasaṃgrahaḥ // 1.25 //

## 3. Padaccheda

```text
dharmaskandhasahasrāṇi → dharma-skandha-sahasrāṇi
yāny aśītim            → yāni aśītim
vāṅnāma vā             → vāk nāma vā
vety eṣām              → vā iti eṣām
rūpasaṃskārasaṃgrahaḥ → rūpa-saṃskāra-saṃgrahaḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| dharma-skandha-sahasrāṇi | nominative neuter plural compound | thousands of Dharma-collections or teaching-divisions |
| yāni | relative pronoun, nominative neuter plural | which |
| aśītim | numeral | eighty; with the thousands, eighty thousand |
| jagau | third-person singular perfect of `√gai` | proclaimed, declared, taught |
| muniḥ | nominative masculine singular | the Sage, the Buddha |
| tāni | demonstrative pronoun, nominative neuter plural | those Dharma-collections |
| vāk | nominative feminine singular | speech, articulated audible utterance |
| nāma | nominative neuter singular | name, linguistic designation |
| vā | alternative particle | or |
| iti | quotative particle | thus; closes the reported alternatives |
| eṣām | genitive plural | of these collections |
| rūpa-saṃskāra-saṃgrahaḥ | nominative masculine singular compound | inclusion within form and formations respectively |

`Dharmaskandha` here is a scriptural designation for a body or division of
teaching. It must not be mistaken for an additional ontological aggregate
beside the canonical five.

## 4. Grammar

The first line is a relative construction completed by its antecedent in the
second:

```text
yāni ... jagau muniḥ
    which the Sage proclaimed

tāni
    those [Dharma-collections]
```

The middle phrase presents alternatives:

```text
vāk vā
    either speech

nāma vā
    or name
```

The Bhāṣya does not say that every Dharma-collection is simultaneously
speech and name. It reports two accounts of the intrinsic nature of
`buddha-vacana`:

```text
if Buddha-word has speech as svabhāva
    → included in rūpa-skandha

if Buddha-word has name as svabhāva
    → included in saṃskāra-skandha
```

The compound `rūpa-saṃskāra-saṃgrahaḥ` is therefore distributive. Speech is
material sound and enters form; name is linguistic determination and enters
formations.

The natural Bhāṣya unit begins with the wider question: when sūtras mention
additional things called skandhas, āyatanas, or dhātus, are they new classes
outside the five, twelve, and eighteen? Vasubandhu answers `na vyatirekaḥ`:
they are not distinct from the established exhaustive systems.

## 5. Translation

### Close syntactic construe

> The eighty thousand Dharma-collections which the Sage proclaimed—whether they are speech or name—are included respectively within form and formations.

### Bhāṣya-informed translation

> The eighty thousand divisions of the Buddha's teaching do not add new aggregates to the canonical five. If Buddha-word is analyzed as audible speech, they belong to the form aggregate; if it is analyzed as linguistic name, they belong to the formations aggregate.

The second translation exposes the classificatory problem and retains the
conditional character of the two reported positions.

## 6. Philosophical Translation

> The teaching is not exempt from the system it teaches. As an audible occurrence, Buddha-word has material form; as an articulated name-structure, it is a formation. The same teaching is classified according to the determination selected for analysis without becoming an entity outside the established Dharma-field.

Organon rendering:

> Doctrine has both a material vehicle and a symbolic articulation. The Discriminator asks which aspect is being posited as intrinsic in the present analysis and assigns it accordingly. Exhaustiveness does not erase levels of presentation; it makes their distinct classifications explicit.

The verse therefore folds the map back into the territory classified by the
map. Speech and naming are themselves dharmas answerable to the system.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| dharma-skandha | Dharma-collection / teaching-division | scriptural body of teaching, not a sixth ontological aggregate |
| buddha-vacana | Buddha-word | teaching whose intrinsic status is disputed here |
| vāk | speech | articulated audible occurrence included within rūpa |
| vāk-svabhāva | speech as intrinsic nature | first reported analysis of Buddha-word |
| nāman | name / linguistic designation | structured naming included within saṃskāra |
| nāma-svabhāva | name as intrinsic nature | second reported analysis of Buddha-word |
| rūpa-skandha | form aggregate | includes the material sound of speech |
| saṃskāra-skandha | formations aggregate | includes name as linguistic determination |
| saṃgraha | strict inclusion | placement according to the selected intrinsic determination |
| vyatireka | existence outside or apart from | denied of additional scriptural classifications |
| pramāṇa | measure / extent | transition question concerning one Dharma-collection in VAK 1.26 |

## 8. Logical Determination

The exhaustiveness problem is:

```text
ScriptureMentions(x, AdditionalSkandhaAyatanaOrDhatuName)
    → NewOntologicalCategory(x)?
```

Vasubandhu's rule is:

```text
AdditionalScripturalDesignation(x)
    → DetermineSvabhava(x)
    → IncludeWithinEstablishedSystem(x)
    → ¬OntologicallyAdditional(x)
```

Applied to the Buddha-word:

```text
HasSvabhava(BuddhaWord, AudibleSpeech)
    → MaterialSound(BuddhaWord)
    → IncludedIn(BuddhaWord, RupaSkandha)

HasSvabhava(BuddhaWord, LinguisticName)
    → LinguisticFormation(BuddhaWord)
    → IncludedIn(BuddhaWord, SamskaraSkandha)
```

The alternatives must not be conflated:

```text
SpeechAnalysis(x) ≠ NameAnalysis(x)

SameTeaching(x)
    → MayBeClassifiedBy(x, MaterialVehicle)
    ∨ MayBeClassifiedBy(x, LinguisticFormation)
```

This is an application of the Core Discriminator to an inherited scriptural
designation.

## 9. Interpretive Note

VAK 1.25 begins the reconciliation of inherited sūtra language with the
Triadic Abhidharma. Scripture speaks of eighty thousand `dharmaskandhas`, but
the shared word `skandha` does not automatically make them eighty thousand
additional ontological aggregates. The system first determines what the
designation refers to and only then assigns it.

This is precisely the kind of problem that an English inventory can conceal.
If every occurrence of “aggregate” is treated as the same sort of item, the
method disappears. Vasubandhu instead distinguishes:

```text
skandha as one of five ontological classifications

dharmaskandha as a division of teaching
```

The spoken/name distinction then shows two valid analytical levels. The
sound of the teaching is rūpa; its articulated designation is saṃskāra. The
meaning of Dharma is not declared material merely because its audible vehicle
is material.

For the Oculus image, we may cautiously say:

```text
speech
    = perceptible mark-vehicle

name
    = structured linguistic determination

Dharma taught
    = not exhausted by either aspect alone
```

But the present verse's exact achievement is narrower: either analysis fits
within the exhaustive five-skandha system. The classification changes with
the selected svabhāva without becoming arbitrary.

VAK 1.25 therefore adds the first problem-solving rule:

```text
an inherited label does not determine its category;
first identify the existent and the aspect under analysis
```

The closing Bhāṣya question—what measures one Dharma-collection?—opens VAK
1.26.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_25
    a vak:Karika ;
    rdfs:label "VAK 1.25" ;
    vak:hasTopic vak:InclusionOfDharmaCollections ;
    vak:belongsTo vak:Dhatunirdesa .

vak:DharmaCollection
    a vak:ScripturalTeachingDivision ;
    vak:distinctFrom vak:AdditionalOntologicalAggregate .

vak:BuddhaWordAsSpeech
    a vak:AudibleMaterialOccurrence ;
    vak:includedIn vak:RupaSkandha .

vak:BuddhaWordAsName
    a vak:LinguisticFormation ;
    vak:includedIn vak:SamskaraSkandha .

vak:AdditionalScripturalDesignation
    vak:requires vak:SvabhavaDetermination ;
    vak:includedWithin vak:EstablishedTriadicSystem .
```
