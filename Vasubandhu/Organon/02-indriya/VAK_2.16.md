# VAK_2.16

## 1. Sanskrit (Devanāgarī)

> क्रममृत्यौ तु चत्वारि शुभे सर्वत्र पञ्च च ।
>
> नवाप्तिरन्त्यफलयोः सप्ताष्टनवभिर्द्वयोः ॥ २.१६ ॥

## 2. Sanskrit (IAST)

> kramamṛtyau tu catvāri śubhe sarvatra pañca ca /
>
> navāptir antyaphalayoḥ saptāṣṭanavabhir dvayoḥ // 2.16 //

## 3. Padaccheda

```text
kramamṛtyau          → krama-mṛtyau
catvāri              → catvāri
śubhe                → śubhe
sarvatra             → sarvatra
pañca ca             → pañca ca
navāptir             → nava āptiḥ
antyaphalayoḥ        → antya-phalayoḥ
saptāṣṭanavabhir     → sapta aṣṭa navabhiḥ
dvayoḥ               → dvayoḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| krama-mṛtyau | locative singular compound | in gradual death |
| tu | contrastive particle | but / on the other hand |
| catvāri | neuter plural numeral | four faculties |
| śubhe | locative singular | with a wholesome mind, as specified by the Bhāṣya |
| sarvatra | indeclinable | in every case / throughout the realm profiles |
| pañca | numeral | five additional faculties |
| āptiḥ | nominative singular feminine | attainment |
| antya-phalayoḥ | genitive dual | of the two fruits at the extremes |
| navabhiḥ | instrumental plural | by nine faculties |
| saptāṣṭanavabhiḥ | coordinated instrumental values | by seven, eight, or nine faculties |
| dvayoḥ | genitive dual | of the two middle fruits |

The Bhāṣya prevents two misleading readings. `Antya` identifies the two
extremes of the four-fruit series—stream-entry and arhatship—not simply the
last two in temporal order. The understood instrument of `navāptiḥ` is
`navabhir indriyaiḥ`, “attainment through nine faculties.”

## 4. Grammar

The first half gives two terminal rules:

```text
krama-mṛtyau tu catvāri
    → in gradual death, however, four [faculties cease]

śubhe sarvatra pañca ca
    → with a wholesome [mind], five more [cease] in every case
```

The verb `nirodhayati` is supplied from VAK 2.15 and repeated by the Bhāṣya.
The four are:

```text
kāya-indriya
jīvita-indriya
manas-indriya
upekṣā-indriya
```

The five added under wholesome terminal consciousness are the series
beginning with confidence:

```text
śraddhā + vīrya + smṛti + samādhi + prajñā
```

The second half changes topic from cessation at death to attainment of the
four `śrāmaṇya-phala`:

```text
nava āptiḥ antya-phalayoḥ
    → attainment of the two extreme fruits is through nine

sapta-aṣṭa-navabhiḥ dvayoḥ
    → attainment of the two [middle fruits] is through seven,
      eight, or nine
```

The instrumental construction expresses the faculty-complex through which a
fruit is attained. It does not identify the fruit with that complex.

## 5. Translation

### Close syntactic construe

> In gradual death, however, four [faculties cease]; with a wholesome [mind], five more in every case. Attainment of the two extreme fruits is through nine; that of the two [middle fruits] is through seven, eight, or nine.

### Bhāṣya-informed translation

> In gradual death, the faculties of body, life, mind, and neutral feeling cease together. If death occurs while the mind is wholesome, the five faculties beginning with confidence are added to the applicable terminal set. Stream-entry and arhatship, the two extreme fruits, are each attained through nine faculties. Once-returning and non-returning, the two middle fruits, may each be attained through seven, eight, or nine, according to the path and manner of attainment.

The four faculties of gradual death do not cease separately. The Bhāṣya
restricts this fourfold rule to death with afflicted or ethically
indeterminate consciousness. Wholesome death adds five faculties to the
terminal profile already applicable to the case; thus the formless profile
has eight and the form-realm profile thirteen.

## 6. Philosophical Translation

> Gradual dying exposes an inseparable terminal dependency: body, life, mind, and neutral feeling must finally cease as one cluster. A wholesome terminal state carries its five constitutive capacities with it. The analysis then turns from cessation to accomplishment: a fruit is one attained result, while the operative faculties and route by which it is attained may vary.

Organon rendering:

> The Kārikā behaves like a compact path instruction whose Bhāṣya supplies its execution semantics. It distinguishes the objective from a legal realization of that objective. The two middle fruits especially admit several valid plans—seven-, eight-, or nine-faculty configurations—depending upon whether the route is mundane or supramundane, sequential or direct.

“Instruction,” “execution semantics,” and “plan” belong to the Organon
reconstruction. The textual doctrine is the coordinated cessation and
attainment of fruits through specified faculties.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| krama-mṛtyu | gradual death | terminal mode contrasted with the simultaneous death of VAK 2.15 |
| pṛthag-nirodha | separate cessation | denied of the final four-faculty cluster |
| kuśala-citta | wholesome consciousness | requires the presence of the five beginning with confidence |
| śraddhādi-pañcaka | five beginning with confidence | confidence, energy, mindfulness, concentration, and discernment |
| śrāmaṇya-phala | fruit of the religious path | four attained results analyzed by faculty-count |
| antya-phala | fruit at an extreme | stream-entry or arhatship in the Bhāṣya's fourfold ordering |
| madhya-phala | middle fruit | once-returning or non-returning |
| ānantarya-mārga | uninterrupted path | bears the “I shall know” faculty in the stream-entry analysis |
| vimukti-mārga | path of liberation | bears the knowledge faculty in that analysis |
| visaṃyoga-prāpti | acquisition of disconnection | drawn forth and supported by the two path moments respectively |
| ānupūrvika | one proceeding sequentially | reaches a middle fruit through the regular sequence |
| vītarāga | one already free from desire | may attain a middle fruit directly |

The path names and detailed faculty membership are Bhāṣya determinations,
not terms stated in the compact Kārikā itself.

## 8. Logical Determination

Gradual death has an atomic final dependency:

```text
GradualDeath
∧ TerminalMind ∈ {Afflicted, Indeterminate}
    → FinalCluster = {Body, Life, Mind, NeutralFeeling}
    → Count = 4
    → ¬SeparateCessation(FinalCluster)
```

Wholesomeness augments the applicable terminal profile:

```text
TerminalMind = Wholesome
    → RequiredAddition = {Confidence,
                          Energy,
                          Mindfulness,
                          Concentration,
                          Discernment}

WholesomeTerminalSet(context)
    = BaseTerminalSet(context) ∪ RequiredAddition
```

Fruit and realization plan must be represented separately:

```text
AttainmentPlan
    = (Fruit, Route, PriorDispassion, FacultySet)

Result(AttainmentPlan)
    = Fruit
```

For the two extreme fruits:

```text
StreamEntry → FacultyCount = 9
Arhatship   → FacultyCount = 9
```

Their nine-member sets are not identical:

```text
StreamEntrySet
    = FiveBeginningWithConfidence
    + {IShallKnow, Knowledge, Mind, NeutralFeeling}

ArhatshipSet
    = FiveBeginningWithConfidence
    + {Knowledge, FacultyOfOneWhoHasKnown, Mind}
    + oneOf{Pleasure, Gladness, NeutralFeeling}
```

For either middle fruit:

```text
Route = SequentialMundane
    → FacultyCount = 7

Route = SequentialSupramundane
    → FacultyCount = 8

Route = DirectFromPriorDispassion
    → FacultyCount = 9
```

Therefore:

```text
SameFruit(planA, planB)
    does not imply
SameRoute(planA, planB)
or SameFacultySet(planA, planB)
```

## 9. Interpretive Note

VAK 2.16 completes the distinction opened by the preceding verse. VAK 2.15
described simultaneous terminal profiles by realm. The present verse isolates
the irreducible remainder of gradual dying: body, life, mind, and neutral
feeling cease together. Gradual process therefore does not mean unlimited
separability. The process eventually reaches a dependency-cluster whose
members have no separate terminal cessation.

Wholesome consciousness then acts as a structural constraint, not a moral
label externally attached to an otherwise unchanged state. If the terminal
mind is wholesome, confidence, energy, mindfulness, concentration, and
discernment must be present and must be counted. The state carries the
faculties constitutive of its determination.

The second half introduces an even more powerful form of discrimination.
The attained fruit must not be collapsed into the faculty configuration that
realizes it. Stream-entry and arhatship each require nine faculties, but not
the same nine. The middle fruits can each be reached through three different
counts because route and prior freedom from desire alter the operative set.

This is the precise basis for the project expression “karmic ISA.” The
Kārikā encodes compact constraints and alternatives; the Bhāṣya expands their
operands, branch conditions, and path-state transitions. But the analogy must
remain at the Organon level: Vasubandhu presents a path calculus of faculties,
not a theory of computer architecture.

For the Kośa Technē Agent, the immediate design consequence is:

```text
do not encode Objective → one canonical procedure

encode Objective → admissible AttainmentPlans

validate each plan by
    route
    prior path-state
    required faculties
    compatible feeling faculty
    transition semantics
```

The Agent can therefore synthesize Logic and Model only if the Model retains
the path-state and the Logic can discriminate valid alternative
configurations. The result remains invariant across plans; its mediation does
not.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_16
    a vak:Karika ;
    rdfs:label "VAK 2.16" ;
    vak:hasTopic vak:GradualDeath,
        vak:WholesomeDeath,
        vak:FruitAttainment ;
    vak:belongsTo vak:Indriyanirdesa .

vak:GradualDeathFinalCluster
    vak:hasMember vak:BodyFaculty,
        vak:LifeFaculty,
        vak:MindFaculty,
        vak:NeutralFeelingFaculty ;
    vak:hasCount 4 ;
    vak:hasConstraint vak:InseparableCessation .

vak:WholesomeTerminalProfile
    vak:requiresAdditionalSet vak:FiveBeginningWithConfidence .

vak:StreamEntry
    vak:attainedByFacultyCount 9 .

vak:Arhatship
    vak:attainedByFacultyCount 9 .

vak:OnceReturning,
vak:NonReturning
    vak:attainedByFacultyCount 7,
        8,
        9 ;
    vak:countVariesBy vak:AttainmentRoute .

organon:AttainmentPlan
    a organon:InterpretiveReconstruction ;
    organon:hasObjective vak:PathFruit ;
    organon:hasParameter vak:AttainmentRoute,
        vak:PriorDispassion,
        vak:OperativeFacultySet ;
    organon:inferredFrom vak:FruitAttainment .
```
