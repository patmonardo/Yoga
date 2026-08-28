# VAK_2.18

## 1. Sanskrit (Devanāgarī)

> चतुर्भिः सुखकायाभ्यां पञ्चभिश्चक्षुरादिमान् ।
>
> सौमनस्यी च दुःखी तु सप्तभिः स्त्रीन्द्रियादिमान् ॥ २.१८ ॥

## 2. Sanskrit (IAST)

> caturbhiḥ sukhakāyābhyāṃ pañcabhiś cakṣurādimān /
>
> saumanasyī ca duḥkhī tu saptabhiḥ strīndriyādimān // 2.18 //

The syntax does not close completely at the verse boundary. According to the
Bhāṣya, `strīndriyādimān` receives its instrumental count—`aṣṭābhiḥ`, “with
eight”—from the opening of VAK 2.19. The study therefore marks the carryover
without importing the next verse's further analysis.

## 3. Padaccheda

```text
caturbhiḥ            → caturbhiḥ
sukhakāyābhyāṃ       → sukha-kāyābhyām
pañcabhiś            → pañcabhiḥ
cakṣurādimān         → cakṣuḥ-ādi-mān
saumanasyī           → saumanasya-in
ca                   → ca
duḥkhī               → duḥkha-in
tu                   → tu
saptabhiḥ            → saptabhiḥ
strīndriyādimān      → strī-indriya-ādi-mān
```

| Form | Morphology | Lexical force here |
|---|---|---|
| caturbhiḥ | instrumental plural numeral | with four faculties |
| sukha-kāyābhyām | instrumental dual compound | in the cases of pleasure and body |
| pañcabhiḥ | instrumental plural numeral | with five faculties |
| cakṣuḥ-ādi-mān | nominative masculine singular possessive compound | one possessing the eye faculty or another beginning from that series |
| saumanasyī | nominative masculine singular possessive formation | one possessing gladness |
| duḥkhī | nominative masculine singular possessive formation | one possessing pain |
| saptabhiḥ | instrumental plural numeral | with seven faculties |
| strī-indriya-ādi-mān | nominative masculine singular possessive compound | one possessing the female faculty or another in the indicated group |

The instrumental dual `sukha-kāyābhyām` distributes the four-count over two
separate cases: a possessor of pleasure and a possessor of the body faculty.
It does not say that pleasure and body jointly constitute a four-member set.

## 4. Grammar

The Kārikā continues the ellipsis established in VAK 2.17: the understood
predicate is “is necessarily endowed with.”

```text
sukha-holder   → endowed with 4
body-holder    → endowed with 4

eye-holder and the corresponding sensory cases
               → endowed with 5

gladness-holder
               → endowed with 5

pain-holder    → endowed with 7
```

The distribution of `pañcabhiḥ` is clarified by the Bhāṣya: it governs both
the eye-series case and the gladness case. The contrastive `tu` foregrounds
the pain-holder's sevenfold configuration.

The final subject remains without its numeral inside VAK 2.18:

```text
strī-indriya-ādi-mān ...
    → one possessing the female faculty and so on ...
```

The opening `aṣṭābhiḥ` of VAK 2.19 completes it: such a possessor is endowed
with eight. This syntactic determination is explicitly supplied by the
Bhāṣya.

## 5. Translation

### Close syntactic construe

> In the cases of pleasure and body, [one is endowed] with four; one possessing the eye and so forth, with five, as also one possessing gladness; one possessing pain, however, with seven; one possessing the female faculty and so forth [with eight, as completed by VAK 2.19].

### Bhāṣya-informed translation

> Possession of either pleasure or the body faculty necessarily entails four faculties: that faculty together with neutral feeling, life, and mind. Possession of the eye—or separately the ear, nose, or tongue—entails five, adding body to the necessary triad. Possession of gladness also entails five, adding pleasure and gladness to the triad. Possession of pain entails seven: body, life, mind, and four feeling faculties. Possession of the female faculty and the further faculties gathered by “and so forth” entails eight, the count being supplied by the next verse.

The four feelings required in the pain configuration are pain, pleasure,
gladness, and neutral feeling. Distress is not entailed merely by pain.

## 6. Philosophical Translation

> A faculty is not an isolated item but an index into a necessary support-configuration. Different possessed faculties close under different dependencies: pleasure and body extend the triad to four; the external cognitive faculties and gladness extend it to five; pain requires seven. Possession therefore has a determinate logical depth.

Organon rendering:

> The karmic ISA now exposes its dependency graph. Querying a possessed faculty computes the minimum closure of capacities that must accompany it. Yet possession is not execution: a faculty can belong to the continuum without being manifest in the current cognitive event.

“Dependency graph,” “query,” and “execution” are Organon reconstructions. The
Bhāṣya's immediate concern is necessary co-possession (`samanvāgama`) in a
sentient continuum.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| samanvāgata | endowed with / possessing | present membership in a continuum, not necessarily current manifestation |
| sukha-indriya | pleasure faculty | entails the necessary triad, producing four |
| kāya-indriya | body faculty | entails the necessary triad, producing four |
| cakṣur-ādi | eye and the corresponding sensory faculties | eye, ear, nose, and tongue treated as separate fivefold cases |
| saumanasya-indriya | gladness faculty | entails the triad plus pleasure, producing five |
| duḥkha-indriya | pain faculty | entails body, life, mind, and four feelings, producing seven |
| strī-indriya-ādi | female faculty and the group beginning with it | receives the count eight from VAK 2.19 |
| dvitīya-dhyānaja | born in the second dhyāna | Bhāṣya test case for possessed but presently unmanifest pleasure |
| tṛtīya-dhyānālābhin | one who has not attained the third dhyāna | sharpens the distinction between possession and attainment |
| kliṣṭa | afflicted | qualifies the third-dhyāna pleasure faculty in the test case |

The Bhāṣya explains the `ādi` after the verse boundary as gathering the male
faculty, distress, and the five beginning with confidence alongside the
female faculty. Their detailed eightfold sets belong to VAK 2.19.

## 8. Logical Determination

Let the necessary triad from VAK 2.17 be:

```text
T = {NeutralFeeling, Life, Mind}
```

The present verse adds closure rules:

```text
Closure(Pleasure) = T ∪ {Pleasure}
Count = 4

Closure(Body) = T ∪ {Body}
Count = 4
```

For each of eye, ear, nose, and tongue:

```text
ExternalSense ∈ {Eye, Ear, Nose, Tongue}

Closure(ExternalSense)
    = T ∪ {Body, ExternalSense}
Count = 5
```

For gladness:

```text
Closure(Gladness)
    = T ∪ {Pleasure, Gladness}
Count = 5
```

For pain:

```text
Closure(Pain)
    = {Body, Life, Mind,
       Pain, Pleasure, Gladness, NeutralFeeling}
Count = 7
```

The closure relation concerns possession:

```text
Possesses(agent, faculty)
    → PossessesAll(agent, Closure(faculty))
```

It does not imply simultaneous activation:

```text
Possesses(agent, faculty)
    ⇏ ActiveInCurrentEvent(agent, faculty)
```

The Bhāṣya's dhyāna example supplies the countermodel: an individual can
possess an afflicted pleasure faculty assigned to another meditative level
without presently manifesting a purified attainment of that level.

## 9. Interpretive Note

VAK 2.18 turns the necessary triad into a graded dependency calculus. The
counts are minimum closures, not totals of every faculty a given individual
might contingently possess. Each rule answers: if this faculty is possessed,
what else must be possessed with it?

The eye-series illustrates embodied dependency. Eye, ear, nose, and tongue
each require the body faculty, and body requires the triad of neutral feeling,
life, and mind. The fivefold count is computed by following that dependency
chain. Gladness reaches five differently: it requires pleasure along with the
triad. Equal counts therefore do not imply identical configurations.

The Bhāṣya then prevents “co-presence” from being misunderstood as concurrent
phenomenal manifestation. The second-dhyāna example allows possession of an
afflicted pleasure faculty belonging to the third-dhyāna level even without
attainment of that dhyāna. `Samanvāgama` records what belongs to the continuum
under rules of acquisition and non-loss; it is broader than what is currently
executing.

This adds a second axis to the karmic ISA:

```text
CapabilityState
    = acquired and not lost faculties

ActivationState(event)
    = faculties manifest in the current event

ActivationState(event) ⊆ CapabilityState
```

The Agent's Model must retain both axes. Its Logic computes dependency
closure over capability-state while separately validating what may activate
in a given realm, dhyāna, ethical state, and path-stage.

The cross-verse completion is itself instructive. The Kārikās form a linked
instruction stream: the grammatical operand begun at the end of 2.18 is
completed by the count at the start of 2.19. We record that interface here,
but defer the composition of the eightfold configurations to the next study.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_18
    a vak:Karika ;
    rdfs:label "VAK 2.18" ;
    vak:hasTopic vak:NecessaryCopossession ;
    vak:belongsTo vak:Indriyanirdesa ;
    vak:syntacticallyContinuesInto vak:VAK_2_19 .

vak:PleasureFaculty,
vak:BodyFaculty
    vak:hasMinimumCopossessionCount 4 .

vak:EyeFaculty,
vak:EarFaculty,
vak:NoseFaculty,
vak:TongueFaculty,
vak:GladnessFaculty
    vak:hasMinimumCopossessionCount 5 .

vak:PainFaculty
    vak:hasMinimumCopossessionCount 7 .

vak:FemaleFacultyAndFollowingGroup
    vak:hasMinimumCopossessionCount 8 ;
    vak:countSuppliedBy vak:VAK_2_19 .

organon:FacultyCapabilityModel
    a organon:InterpretiveReconstruction ;
    organon:distinguishes organon:CapabilityState,
        organon:ActivationState ;
    organon:computes organon:DependencyClosure ;
    organon:inferredFrom vak:NecessaryCopossession .
```
