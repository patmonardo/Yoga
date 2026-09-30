# VAK_3.62

## 1. Sanskrit (Devanāgarī)

> लवशो रात्र्यहर्वृद्धी दक्षिणोत्तरगे रवौ ।
>
> स्वच्छाययार्कसामीप्याद्विकलेन्दुसमीक्षणम् ॥ ३.६२ ॥

## 2. Sanskrit (IAST)

> lavaśo rātryaharvṛddhī dakṣiṇottarage ravau /
>
> svacchāyayārkasāmīpyād vikalendusamīkṣaṇam // 3.62 //

## 3. Lexical Analysis

```text
lavaśaḥ                    → lavaśo
rātri-ahaḥ-vṛddhī          → rātryaharvṛddhī
dakṣiṇa-uttara-ge          → dakṣiṇottarage
ravau                      → ravau
sva-chāyayā                → svacchāyayā
arka-sāmīpyāt              → 'rkasāmīpyād
vikala-indu-samīkṣaṇam     → vikalendusamīkṣaṇam
```

| Form | Morphology | Lexical force here |
|---|---|---|
| lavaśaḥ | adverbial distributive | lava by lava, one minute increment at a time |
| rātryaharvṛddhī | nominative feminine dual compound | increases of night and day |
| dakṣiṇottarage | locative masculine singular compound | when going southward and northward |
| ravau | locative masculine singular | when the sun [moves] |
| svacchāyayā | instrumental feminine singular | by shadow; qualified relationally by the Bhāṣya |
| arkasāmīpyāt | ablative neuter singular compound | because of proximity to the sun |
| vikalendusamīkṣaṇam | nominative/accusative neuter singular compound | seeing the lunar disk as incomplete |

## 4. Grammar

The first line relates incremental change to solar direction:

```text
ravau dakṣiṇa-uttara-ge
    rātri-ahaḥ-vṛddhī
    lavaśaḥ [bhavataḥ]
```

The Bhāṣya applies the ordered terms `rātri–ahaḥ` to `dakṣiṇa–uttara`:

```text
sun moving southward → increase of night
sun moving northward → increase of day
```

The second line gives a causal construe of an appearance:

```text
arka-sāmīpyāt
    chāyayā
    vikala-indu-samīkṣaṇam [bhavati]
```

The Bhāṣya does not support treating `sva-chāyā` as a wholly intrinsic lunar
shadow independent of the sun. In the principal explanation, solar rays strike
the nearby lunar vehicle and shadow falls upon its opposite side.

## 5. Translation

### Close syntactic construe

> As the sun moves south and north, night and day increase lava by lava. Owing
> to shadow in proximity to the sun, the moon is seen as incomplete.

### Bhāṣya-informed study translation

> Night increases one lava at a time while the sun moves toward the southern
> side of Jambūdvīpa; day increases one lava at a time while it moves northward.
> At the beginning of the bright fortnight, the lunar disk appears incomplete.
> According to the Prajñapti account, when the lunar vehicle approaches the
> solar vehicle, solar rays fall upon it and shadow on the opposite side makes
> only part of the disk visible. According to earlier teachers, the
> configuration of the lunar vehicle's motion is itself such that only part of
> it is seen.

The exact increment, ordered direction–duration mapping, bright-fortnight
location, causal mechanism, and alternative motion-configuration account are
Bhāṣya determinations.

## 6. Philosophical Translation

> The calendrical trend of 3.61 is now given an update rule: change proceeds in
> minimal increments, and the sign of the update is selected by the direction
> of the sun's course. The verse then separates visible state from causal
> explanation. One incomplete lunar appearance is held constant while two
> models compete to explain it—shadow produced through solar proximity, or a
> configuration of motion that restricts visibility. The Physical World is
> therefore modeled through measurable updates and explanation-sensitive
> appearances, not through unexamined visual immediacy.

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| lava | lava / minute temporal increment | quantum of day–night duration change |
| lavaśaḥ | increment by increment | distributive update rule |
| dakṣiṇagati | southward course | selects increase of night |
| uttaragati | northward course | selects increase of day |
| śuklapakṣa | bright fortnight | calendrical context of incomplete lunar appearance |
| vikala | incomplete / lacking a part | observed state of the lunar disk |
| indu-maṇḍala | lunar disk | object whose visible completeness varies |
| arka-sāmīpya | proximity to the sun | relational condition in the Prajñapti explanation |
| chāyā | shadow | mediating condition of partial visibility |
| prājñaptika-nirdeśa | Prajñapti explanation | attributed ray-and-shadow model |
| vāhayoga | configuration of motion / conveyance | basis of the earlier-teacher model |
| pūrvācārya | earlier teacher | authority for the alternative account |

## 8. Logical Determination

### Incremental update rule

Let `L` be one lava and let the current durations be `N` for night and `D` for
day:

```text
southward solar motion:
    Nₜ₊₁ = Nₜ + L
    Dₜ₊₁ = Dₜ − L

northward solar motion:
    Nₜ₊₁ = Nₜ − L
    Dₜ₊₁ = Dₜ + L
```

The second equation in each pair follows from the inverse relation established
in 3.61. The verse supplies the increment and direction selector; together the
two verses define the transition function.

### Direction controls sign, not magnitude

```text
update magnitude = one lava
update direction = selected by solar course
```

This separates how much the state changes from which member increases. A
single update mechanism can therefore govern both halves of the annual cycle.

### Observation and explanation

```text
shared observation:
    lunar disk appears incomplete

Prajñapti explanation:
    solar proximity → incident rays → opposite-side shadow → partial appearance

earlier-teacher explanation:
    motion configuration → only part of lunar vehicle visible
```

Agreement on the observed predicate does not entail agreement on its causal
model. The knowledge representation must preserve both levels separately.

### Relation-mediated appearance

Under the principal account:

```text
moon alone
    ≠ sufficient explanation of visible phase

moon–sun proximity
    + illumination relation
    + shadow distribution
        → observed incompleteness
```

The appearance belongs to a relational configuration, not to an isolated
object considered without its conditions.

## 9. Interpretive Note

VAK 3.62 completes the temporal process begun in 3.60–3.61:

```text
3.60  locale index → current phase
3.61  calendar index → trend reversal
3.62  solar direction + lava → incremental update
```

Together they specify state, trend, transition point, and update magnitude.
The cosmological calendar has become a genuine state-transition system rather
than a loose collection of seasonal observations.

The lunar half gives an equally important scientific method:

```text
observation
    ≠ explanation
```

The Bhāṣya holds the appearance steady and preserves two attributed causal
models. That is exactly how our Semantic pipeline should treat contested
explanations: store the observed determination once, attach competing models
with provenance, and do not silently promote one account into the observation
itself.

```ts
interface ExplainedAppearance {
  observation: "incomplete-lunar-disk";
  context: "beginning-of-bright-fortnight";
  models: readonly {
    authority: "Prajnapti" | "EarlierTeachers";
    causalSequence: readonly string[];
  }[];
}
```

This is explanatory notation, not Vasubandhu's vocabulary. It extracts the
methodical distinction between a stable datum and revisable explanations of
that datum.

The Agential dimension remains implicit in `samīkṣaṇa`, seeing. The system is
not complete with celestial positions alone; it accounts for how an embodied
observer encounters the moon under determinate relational conditions. Yet the
visible result does not disclose its own causal history without further
analysis.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:VAK_3_62
    a vak:Karika ;
    vak:describes loka:IncrementalDayNightVariation,
        loka:IncompleteLunarAppearance ;
    vak:preservesExplanation loka:PrajnaptiLunarModel,
        loka:EarlierTeacherLunarModel .

loka:IncrementalDayNightVariation
    loka:hasIncrement loka:OneLava ;
    loka:mapsSouthwardMotionTo loka:NightIncrease ;
    loka:mapsNorthwardMotionTo loka:DayIncrease .

loka:IncompleteLunarAppearance
    loka:hasCalendarContext loka:BeginningOfBrightFortnight ;
    loka:hasObject loka:LunarDisk .

loka:PrajnaptiLunarModel
    vak:attributedTo vak:PrajnaptiTradition ;
    loka:hasCondition loka:SolarProximity,
        loka:IncidentSolarRays,
        loka:OppositeSideShadow .

loka:EarlierTeacherLunarModel
    vak:attributedTo vak:EarlierTeachers ;
    loka:hasCondition loka:MotionConfiguration,
        loka:PartialVisibility .

organon:ObservationExplanationSeparation
    a organon:ProjectInterpretation ;
    organon:preserves organon:SharedObservation ;
    organon:allows organon:MultipleCausalModels ;
    organon:requires organon:ModelProvenance .
```
