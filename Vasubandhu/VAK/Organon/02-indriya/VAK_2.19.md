# VAK_2.19

## 1. Sanskrit (Devanāgarī)

> अष्टाभिरेकादशभिस्त्वाज्ञाज्ञातेन्द्रियान्वितः ।
>
> आज्ञास्यामीन्द्रियोपेतस्त्रयोदशभिरन्वितः ॥ २.१९ ॥

## 2. Sanskrit (IAST)

> aṣṭābhir ekādaśabhis tv ājñājñātendriyānvitaḥ /
>
> ājñāsyāmīndriyopetas trayodaśabhir anvitaḥ // 2.19 //

The opening `aṣṭābhiḥ` completes the subject `strīndriyādimān` carried over
from VAK 2.18. Only after that completion does `ekādaśabhiḥ` govern the two
realization-faculty cases introduced in this verse.

## 3. Padaccheda

```text
aṣṭābhir             → aṣṭābhiḥ
ekādaśabhis          → ekādaśabhiḥ
tv                   → tu
ājñājñātendriyānvitaḥ
                     → ājñā-ājñāta-indriya-anvitaḥ
ājñāsyāmīndriyopetas
                     → ājñāsyāmi-indriya-upetaḥ
trayodaśabhir        → trayodaśabhiḥ
anvitaḥ              → anvitaḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| aṣṭābhiḥ | instrumental plural numeral | with eight faculties; completes VAK 2.18 |
| ekādaśabhiḥ | instrumental plural numeral | with eleven faculties |
| tu | contrastive particle | but / whereas |
| ājñā-indriya | compound member | faculty of knowledge |
| ājñāta-indriya | compound member | faculty belonging to one who has known, as explained by the Bhāṣya |
| anvitaḥ | nominative masculine singular | accompanied by / endowed with |
| ājñāsyāmi-indriya | possessive compound member | faculty called “I shall know” |
| upetaḥ | nominative masculine singular | furnished with / possessing |
| trayodaśabhiḥ | instrumental plural numeral | with thirteen faculties |

The Bhāṣya explains `ājñāta-indriya` as an abbreviated designation of the
faculty belonging to one who has known, elsewhere termed
`ājñātāvīndriya`.

## 4. Grammar

The verse begins by closing the preceding construction:

```text
strī-indriya-ādi-mān aṣṭābhiḥ
    → one possessing the female faculty and the following group
      is endowed with eight
```

The Bhāṣya distributes this rule `pratyekam`, to each case separately. The
female faculty, male faculty, distress, and each of the five beginning with
confidence do not form one joint eightfold set.

The first line then introduces two parallel subjects under one count:

```text
ājñā-indriya-anvitaḥ
ājñāta-indriya-anvitaḥ
    → endowed with 11
```

The second line gives a third realization-faculty configuration:

```text
ājñāsyāmi-indriya-upetaḥ
    → trayodaśabhiḥ anvitaḥ
    → one possessing the “I shall know” faculty is endowed with 13
```

The possessive participles `anvitaḥ` and `upetaḥ` continue the chapter's
analysis of necessary endowment, not merely faculties activated in one
cognitive moment.

## 5. Translation

### Close syntactic construe

> [One possessing the female faculty and so forth is endowed] with eight; but one endowed with the knowledge faculty or the faculty of one who has known, with eleven. One possessing the faculty called “I shall know” is endowed with thirteen.

### Bhāṣya-informed translation

> Possession of the female faculty, the male faculty, distress, or any one of the five faculties beginning with confidence entails a minimum configuration of eight, calculated separately for each case. Possession of the knowledge faculty or the faculty of one who has known entails eleven. Possession of the faculty called “I shall know” entails thirteen.

The Kārikā states only the counts and faculty groups. The membership of each
supporting configuration below is supplied by the Bhāṣya.

## 6. Philosophical Translation

> The path faculties occur only within determinate supporting wholes. Each of the five practical faculties entails the coordinated five together with the necessary triad. The realization faculties then determine larger but distinct closures appropriate to prospective knowing, operative knowledge, and completed knowledge.

Organon rendering:

> The dependency graph now reaches its control states. A realization faculty is not an isolated flag attached to an Agent; it certifies that an entire capability configuration is present. Prospective realization, active knowledge, and completed knowledge are typed states with different validation requirements.

“Control state,” “flag,” “typed state,” and “validation” are Organon
reconstructions. The textual doctrine concerns the exact faculties necessarily
possessed with each path faculty.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| pratyekam | in each case separately | Bhāṣya qualifier preventing aggregation of the eightfold cases |
| śraddhādi-pañcaka | five beginning with confidence | confidence, energy, mindfulness, concentration, and discernment; mutually entailing here |
| ājñāsyāmi-indriya | “I shall know” faculty | prospective realization faculty; entails thirteen |
| ājñā-indriya | knowledge faculty | realization faculty; entails eleven |
| ājñātāvī-indriya | faculty of one who has known | completed-realization faculty; entails eleven |
| ājñāta-indriya | faculty belonging to one who has known | Bhāṣya's grammatical explanation of the preceding designation |
| samanvāgata | endowed with / possessing | Bhāṣya relation of lawful membership in a continuum |
| upeta | furnished with / possessing | Kārikā expression parallel to `anvita` |
| anvita | accompanied by / endowed with | Kārikā expression for the co-possession relation |

The associations with path of seeing, cultivation, and no-more-training are
doctrinal determinations supplied by the Bhāṣya context; they are not stated
in these two compact lines.

## 8. Logical Determination

The eight-count closes the group begun in VAK 2.18. Let:

```text
PainClosure
    = {Body, Life, Mind,
       Pain, Pleasure, Gladness, NeutralFeeling}
```

Then the female, male, and distress cases are separately:

```text
Closure(Female)   = PainClosure ∪ {Female}
Closure(Male)     = PainClosure ∪ {Male}
Closure(Distress) = PainClosure ∪ {Distress}

Count(each) = 8
```

For any one of the five beginning with confidence:

```text
PathFive = {Confidence, Energy, Mindfulness,
            Concentration, Discernment}

f ∈ PathFive
∧ Possesses(agent, f)
    → PossessesAll(agent,
        PathFive ∪ {NeutralFeeling, Life, Mind})
    → MinimumCount = 8
```

The two elevenfold realization closures share ten supports:

```text
LaterRealizationSupport
    = {Pleasure, Gladness, NeutralFeeling,
       Life, Mind}
      ∪ PathFive

Closure(Knowledge)
    = LaterRealizationSupport ∪ {Knowledge}
Count = 11

Closure(OneWhoHasKnown)
    = LaterRealizationSupport ∪ {OneWhoHasKnown}
Count = 11
```

The prospective realization faculty has a different support-set:

```text
SeeingPathSupport
    = {Mind, Life, Body,
       Pain, Pleasure, Gladness, NeutralFeeling}
      ∪ PathFive

Closure(IShallKnow)
    = SeeingPathSupport ∪ {IShallKnow}
Count = 13
```

Hence count does not determine configuration identity:

```text
Count(Closure(x)) = Count(Closure(y))
    ⇏ Closure(x) = Closure(y)
```

## 9. Interpretive Note

VAK 2.19 first repairs the open syntax of VAK 2.18. Its initial “with eight”
belongs to the female-faculty group left waiting at the prior verse boundary.
The Bhāṣya's `pratyekam` is logically decisive: each named faculty generates
its own minimum eightfold configuration. We must not merge female, male,
distress, and the five practical faculties into a single state.

The five beginning with confidence reveal an internally coordinated practical
system. Possession of any one entails possession of all five, and the five in
turn require neutral feeling, life, and mind. In the project's vocabulary,
this is a genuine agential Technē configuration: confidence, energy,
mindfulness, concentration, and discernment operate as discriminable powers
of one path-capacity. That is an Organon interpretation, while the exact
co-possession rule belongs to the Bhāṣya.

The three realization faculties then articulate stages of knowing through
different support closures. The prospective “I shall know” faculty requires
thirteen, including body and four feelings. Knowledge and the faculty of one
who has known each require eleven, with three feelings and no body in their
minimum set. The numerical increase or decrease must not by itself be read as
more or less realization. The sets encode the conditions of their respective
path states.

For the karmic ISA, realization is therefore not a scalar status code:

```text
RealizationState
    = discriminated FacultyClosure
    + path-stage determination

state.tag alone
    is insufficient
```

The Kośa Agent must be able to infer the whole required capability-state from
the realization faculty and reject configurations missing any entailed
support. It must also preserve exact set identity: an eight-count or
eleven-count without its membership and provenance is semantically
underdetermined.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_19
    a vak:Karika ;
    rdfs:label "VAK 2.19" ;
    vak:hasTopic vak:NecessaryCopossession,
        vak:RealizationFacultyConfiguration ;
    vak:belongsTo vak:Indriyanirdesa ;
    vak:syntacticallyCompletes vak:VAK_2_18 .

vak:FemaleFaculty,
vak:MaleFaculty,
vak:DistressFaculty,
vak:FiveBeginningWithConfidence
    vak:hasMinimumCopossessionCount 8 .

vak:KnowledgeFaculty,
vak:FacultyOfOneWhoHasKnown
    vak:hasMinimumCopossessionCount 11 .

vak:IShallKnowFaculty
    vak:hasMinimumCopossessionCount 13 .

vak:FiveBeginningWithConfidence
    vak:hasMember vak:ConfidenceFaculty,
        vak:EnergyFaculty,
        vak:MindfulnessFaculty,
        vak:ConcentrationFaculty,
        vak:DiscernmentFaculty ;
    vak:hasConstraint vak:MutualCopossession .

organon:RealizationCapabilityState
    a organon:InterpretiveReconstruction ;
    organon:requires organon:ExactFacultyClosure,
        organon:PathStageDetermination ;
    organon:rejects organon:CountOnlyRepresentation ;
    organon:inferredFrom vak:RealizationFacultyConfiguration .
```
