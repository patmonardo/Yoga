# VAK_2.17

## 1. Sanskrit (Devanāgarī)

> एकादशभिरर्हत्त्वमुक्तं त्वेकस्य संभवात् ।
>
> उपेक्षाजीवितमनोयुक्तोऽवश्यं त्रयान्वितः ॥ २.१७ ॥

## 2. Sanskrit (IAST)

> ekādaśabhir arhattvam uktaṃ tv ekasya saṃbhavāt /
>
> upekṣājīvitamanoyukto 'vaśyaṃ trayānvitaḥ // 2.17 //

## 3. Padaccheda

```text
ekādaśabhir          → ekādaśabhiḥ
arhattvam            → arhattvam
uktaṃ                → uktam
tv                    → tu
ekasya               → ekasya
saṃbhavāt            → saṃbhavāt
upekṣājīvitamanoyukto
                      → upekṣā-jīvita-manas-yuktaḥ
avaśyaṃ              → avaśyam
trayānvitaḥ          → traya-anvitaḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| ekādaśabhiḥ | instrumental plural numeral | through eleven faculties |
| arhattvam | nominative/accusative neuter singular | arhatship |
| uktam | nominative/accusative neuter singular past passive participle | is stated |
| tu | contrastive particle | however |
| ekasya | genitive singular | for one person |
| saṃbhavāt | ablative singular | because of the possibility |
| upekṣā-jīvita-manas-yuktaḥ | nominative masculine singular compound | one endowed with neutral feeling, life, or mind, as resolved by the Bhāṣya |
| avaśyam | indeclinable | necessarily |
| traya-anvitaḥ | nominative masculine singular | accompanied by the three |

The compound in the second line is compressed. The Bhāṣya resolves it as
possession of any one among neutral feeling, life, and mind: possession of
one necessarily entails possession of all three.

## 4. Grammar

The first line answers an apparent contradiction with VAK 2.16:

```text
ekādaśabhiḥ arhattvam uktam
    → arhatship is stated [in the Abhidharma] to be attained through eleven

tu ekasya saṃbhavāt
    → but [this is] because all eleven are possible for one person
```

The ablative `saṃbhavāt` gives the reason for the statement. The Bhāṣya
supplies the omitted distinction between two scopes of counting:

```text
one attainment-event → 9 faculties
one person across repeated attainment-events → 11 possible faculties
```

The second line begins a new question concerning necessary co-possession:

```text
upekṣā-jīvita-manas-yuktaḥ
    → one endowed with any one of neutral feeling, life, and mind

avaśyaṃ traya-anvitaḥ
    → is necessarily endowed with the three
```

The distributive “any one” is explicit in the Bhāṣya (`eṣām anyatamena`),
not separately expressed in the compact Kārikā.

## 5. Translation

### Close syntactic construe

> Arhatship is stated [to be attained] through eleven, however, because of their possibility for one person. One endowed with [any of] neutral feeling, life, or mind is necessarily accompanied by the three.

### Bhāṣya-informed translation

> Although a single attainment of arhatship occurs through nine faculties, eleven are stated because one person may, after repeated losses and reattainments, attain arhatship at different times with pleasure, gladness, and neutral feeling. These three feelings never operate together in one attainment. In the analysis of possession, anyone endowed with neutral feeling, life, or mind is necessarily endowed with all three; none can be possessed without the other two.

The eleven-faculty statement is cumulative, not simultaneous. It unites the
alternative feeling faculties that may occur across several attainment-events
in the history of one person.

## 6. Philosophical Translation

> A count is intelligible only after its domain has been fixed. Nine describes the faculties operating in a single attainment of arhatship. Eleven describes the total range that can be instantiated by one person across repeated attainments. The verse then identifies a different relation altogether: within a presently possessed living mental configuration, neutral feeling, life, and mind entail one another.

Organon rendering:

> The Kośa distinguishes event-local state from agent-history. Alternative feeling faculties are mutually exclusive within one execution, yet cumulatively possible across the history of one Agent. At each living mental state, however, the possession invariant requires persistence, mental coordination, and neutral affect to occur as an inseparable minimum triad.

“Execution,” “agent-history,” and “possession invariant” are Organon
reconstructions. The textual claims concern repeated attainment and necessary
co-possession of faculties.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| arhattva | arhatship | fruit whose event-local and cumulative counts are distinguished |
| ekādaśa | eleven | total possible faculty-types across repeated attainments by one person |
| saṃbhava | possibility / possible occurrence | explains why the cumulative total is stated |
| parihāya | after falling away | Bhāṣya condition enabling repeated reattainment |
| samanvāgata | endowed with / presently possessing | Bhāṣya term governing the new co-possession analysis |
| upekṣā-indriya | neutral-feeling faculty | one member of the necessary triad |
| jīvita-indriya | life faculty | one member of the necessary triad |
| manas-indriya | mind faculty | one member of the necessary triad |
| avaśyam | necessarily | marks exceptionless entailment within the specified possession-domain |
| aniyama | absence of a fixed rule | Bhāṣya characterization of the remaining faculties |

The Bhāṣya's subsequent exclusions show that other faculties vary with realm,
birth, loss, meditative level, ethical condition, and path-stage. Those
examples justify the contrast with the triad; they are not separate claims of
the Kārikā.

## 8. Logical Determination

The apparent numerical conflict is resolved by separating count scopes:

```text
ForEvery ArhatshipAttainmentEvent e:
    OperativeFacultyCount(e) = 9

ForSome Person p:
    Union({OperativeFacultySet(e) |
           e is an ArhatshipAttainmentEvent of p})
        has Count = 11
```

The three feeling faculties are alternatives at the event level:

```text
ForEvery ArhatshipAttainmentEvent e:
    exactlyOneOf{Pleasure, Gladness, NeutralFeeling} ∈ FacultySet(e)
```

They may all occur in the historical union:

```text
RepeatedFallAndReattainment(p)
    → possibly {
        event with Pleasure,
        event with Gladness,
        event with NeutralFeeling
      }
```

Necessary co-possession is a separate relation:

```text
T = {NeutralFeeling, Life, Mind}

ForEvery living configuration s:
    Possesses(s, NeutralFeeling)
    ∨ Possesses(s, Life)
    ∨ Possesses(s, Mind)
        → PossessesAll(s, T)
```

Equivalently, within this possession-domain:

```text
NeutralFeeling ↔ Life ↔ Mind
```

No analogous universal equivalence is asserted for the remaining faculties:

```text
Faculty f ∉ T
    → possession of f is condition-dependent
```

## 9. Interpretive Note

VAK 2.17 performs a logical cleanup essential to the faculty calculus. The
previous verse said that arhatship is attained through nine faculties. The
Abhidharma also says eleven. Vasubandhu does not weaken either claim; he shows
that they quantify over different units.

Nine belongs to a single attainment-event. Eleven belongs to the union of
possible faculties across several attainments by one person who falls away
and reattains arhatship under different feeling faculties. Pleasure,
gladness, and neutral feeling are never simultaneous in the relevant event.
The larger count is therefore diachronic rather than synchronic.

This gives the karmic ISA a required type distinction:

```text
RuntimeState
    ≠ ExecutionHistory

operands active in one transition
    ≠ union of operands possible across an Agent's transitions
```

Without that distinction, eleven would falsely appear to contradict nine.
The Bhāṣya instead shows that both counts are valid projections of the same
person at different levels of aggregation.

The second half establishes the first strict co-possession invariant. The
triad should not be inflated into an unqualified metaphysics of all possible
experience. Textually, Vasubandhu is calculating present endowment with
faculties. Within that domain, however, the claim is strong: none of neutral
feeling, life, and mind is possessed without the other two.

For the Kośa Technē Agent, these become two different validation tasks:

```text
validateState(state)
    → enforce mutual entailment of the necessary triad

summarizeHistory(agent)
    → union mutually exclusive alternatives across valid events
```

The Model must therefore preserve time-indexed states. Logic can then compute
either a simultaneous configuration or a cumulative capability-set without
confusing them.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_17
    a vak:Karika ;
    rdfs:label "VAK 2.17" ;
    vak:hasTopic vak:ArhatshipFacultyCount,
        vak:NecessaryCopossession ;
    vak:belongsTo vak:Indriyanirdesa .

vak:ArhatshipAttainmentEvent
    vak:hasOperativeFacultyCount 9 ;
    vak:selectsOneFrom vak:PleasureFaculty,
        vak:GladnessFaculty,
        vak:NeutralFeelingFaculty .

vak:ArhatshipAttainmentHistory
    vak:hasPossibleFacultyCount 11 ;
    vak:aggregates vak:RepeatedAttainmentEvent .

vak:NecessaryTriad
    vak:hasMember vak:NeutralFeelingFaculty,
        vak:LifeFaculty,
        vak:MindFaculty ;
    vak:hasRelation vak:MutualCopossession .

organon:TimeIndexedFacultyModel
    a organon:InterpretiveReconstruction ;
    organon:distinguishes organon:RuntimeState,
        organon:AgentHistory ;
    organon:validates vak:NecessaryTriad ;
    organon:inferredFrom vak:ArhatshipFacultyCount,
        vak:NecessaryCopossession .
```
