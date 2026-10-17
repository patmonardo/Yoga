# VAK_3.44 — The Three Determinations of the Sentient World

## 1. Sanskrit (Devanāgarī)

```sanskrit
सम्यङ्मिथ्यात्वनियता आर्यानन्तर्यकारिणः ॥ ३.४४ ॥
```

## 2. Sanskrit (IAST)

```text
samyaṅmithyātvaniyatā āryānantaryakāriṇaḥ // 3.44 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| samyaktva | neuter abstract noun | rightness; defined by the Bhāṣya as complete abandonment of the afflictions |
| mithyātva | neuter abstract noun | wrongness; here determined through the three bad destinies |
| niyatāḥ | nominative masculine plural | fixed, determined, established upon a course |
| āryāḥ | nominative masculine plural | noble ones; those in whom the path without outflows has arisen |
| ānantarya-kāriṇaḥ | nominative masculine plural compound | performers of an action bearing an immediate result |

`Samyaṅmithyātvaniyatāḥ` compresses two coordinated predicates:
`samyaktva-niyatāḥ` and `mithyātva-niyatāḥ`. The two following nouns supply
their respective subjects.

## 4. Grammar

The elliptical verse resolves as two parallel clauses:

```text
āryāḥ
    samyaktva-niyatāḥ [santi]

ānantarya-kāriṇaḥ
    mithyātva-niyatāḥ [santi]
```

Thus the ordered correlation is:

```text
āryāḥ                 → samyaktva-niyatāḥ
ānantarya-kāriṇaḥ     → mithyātva-niyatāḥ
```

The copula is understood. The third class, `aniyata`, is stated in the
Bhāṣya's framing prose rather than in the compressed Kārikā.

## 5. Translation

### Literal Translation
> The noble ones are fixed in rightness; performers of immediate-result
> actions are fixed in wrongness.

### Bhāṣya-informed study translation

> The noble ones and those who perform immediate-result actions are fixed,
> respectively, in rightness and wrongness.

## 6. Philosophical Translation

> The Human World culminates in a classification of the Rational Moral Agent
> by trajectory rather than by a merely present mental state. One course has
> become irreversible toward the exhaustion of affliction; another has become
> fixed toward a destructive maturation; the remaining course is still open
> to determination through conditions. The third class is therefore not an
> empty remainder. It is the field in which Practical Reason can alter the
> Agent's course before it becomes fixed.

“Human World” is the Organon framing of this investigation. The textual scope
is `sattvaloka`, the broader sentient world.

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| sattvaloka | sentient world | the world whose arising, persistence, death, and path-determination have now been explained |
| rāśi | group / class | one of three classes established according to fixity |
| samyaktva | rightness | complete abandonment of attachment, hatred, delusion, and all afflictions |
| samyaktva-niyata | fixed in rightness | irreversibly determined toward exhaustion of affliction |
| mithyātva | wrongness | here specified through hell, preta, and animal destinies |
| mithyātva-niyata | fixed in wrongness | determined toward a bad destiny |
| aniyata | not fixed | dependent upon conditions for participation in either course or neither |
| ārya | noble one | one in whom the path without outflows has arisen |
| anāsrava-mārga | path without outflows | criterion used by the Bhāṣya to identify the noble ones |
| kleśakṣaya | exhaustion of affliction | terminus with respect to which the noble ones are fixed |
| ānantarya-karman | immediate-result action | action determining the agent toward hell |
| mokṣabhāgīya | conducive to liberation | sufficient for eventual liberation, but not by itself for present fixity in rightness |
| pratyayāpekṣa | dependent upon conditions | modal status of those who are not fixed |
| bhājanaloka | container-world | the physical world announced as the next subject |

The threefold matrix is:

```text
fixed in rightness     → āryas
fixed in wrongness     → performers of immediate-result actions
not fixed              → all others, according to conditions
```

## 8. Logical Determination

### Classification of the sentient world

```text
sattvaloka
    → samyaktva-niyata-rāśi
    or mithyātva-niyata-rāśi
    or aniyata-rāśi
```

The classes concern determination of course, not three kinds of substance.

### Rightness is not mere correct opinion

The quoted sūtra gives the criterion:

```text
complete abandonment of attachment
  + complete abandonment of hatred
  + complete abandonment of delusion
  + complete abandonment of all afflictions
    → samyaktva
```

Accordingly:

```text
arising of the path without outflows
    → final disjunction from harmful dharmas
        → fixity toward exhaustion of affliction
```

The predicate describes operative path-determination, not assent to a
proposition.

### Eventual liberation is not present fixity

The Bhāṣya expressly distinguishes:

```text
possession of liberation-conducive dharmas
    → eventual parinirvāṇa

but not necessarily

possession of liberation-conducive dharmas
    → already fixed in rightness
```

The latter requires a stronger determination: the course and its relevant
temporal orientation are established so that contrary fixity cannot intervene.

### Wrongness as destination-fixity

```text
performance of an immediate-result action
    → determination toward hell
        → fixed in wrongness
```

Here `mithyātva` is not reduced to holding a false belief. Its force is
practical and consequential.

### The condition-dependent class

```text
not fixed
    + relevant conditions
        → either determination
          or neither determination
```

`Aniyata` therefore marks genuine conditional openness. It does not mean that
the Agent lacks causes; it means that the causal course has not acquired one
of the two specified fixed forms.

## 9. Interpretive Note

**Translation note.** The Bhāṣya gives a third class, those not fixed: only whether
they enter rightness, wrongness, or neither depends on conditions. Noble ones are
fixed in rightness because the path without Influx has arisen and their course leads
to exhaustion of afflictions; performers of an immediate-result action are fixed in
wrongness because their course leads to hell. The three groups, the definitions of
rightness and wrongness, and the reasons for each determination are supplied by the
Bhāṣya.

At the project level, the sentient-world account distinguishes fixed trajectory from condition-dependent course. The Bhāṣya’s transition to the container-world marks the boundary between those inquiries; the Agent schema is an Organon model, not Vasubandhu’s terminology.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:VAK_3_44
    a vak:Karika ;
    vak:completes vak:SentientWorldAccount ;
    vak:classifies vak:RightnessFixedGroup,
        vak:WrongnessFixedGroup,
        vak:NotFixedGroup ;
    vak:precedes vak:ContainerWorldAccount .

vak:NobleOne
    vak:hasTrajectory vak:RightnessFixed ;
    vak:hasPath vak:PathWithoutOutflows ;
    vak:isFixedToward vak:ExhaustionOfAffliction .

vak:PerformerOfImmediateResultAction
    vak:hasTrajectory vak:WrongnessFixed ;
    vak:isFixedToward vak:HellDestination .

vak:NotFixedAgent
    vak:hasTrajectory vak:ConditionDependent ;
    vak:dependsUpon vak:Conditions .

organon:TrajectoryClassification
    a organon:ProjectInterpretation ;
    organon:distinguishes organon:PresentState,
        organon:EventualResult,
        organon:FixedCourse ;
    organon:locatesPracticalReasonIn vak:NotFixedGroup .
```
