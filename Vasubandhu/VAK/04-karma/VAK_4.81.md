# VAK 4.81

## 1. Sanskrit — Devanāgarī

युगपद्यावदष्टाभिरशुभैः सह वर्तते ।  
चेतना दशभिर्यावच्छुभैर्नैकाष्टपञ्चभिः ॥ ४.८१ ॥

## 2. Sanskrit — IAST

*yugapad yāvad aṣṭābhir aśubhaiḥ saha vartate |*  
*cetanā daśabhir yāvac chubhair naikāṣṭapañcabhiḥ || 4.81 ||*

The verse states the possible simultaneous conjunctions of intention with karmic courses:

- with unwholesome courses, intention occurs with as many as eight;
- with wholesome courses, intention occurs with as many as ten;
- wholesome totals of one, five, and eight are excluded.

## 3. Padaccheda

- yugapat
- yāvat
- aṣṭābhiḥ
- aśubhaiḥ
- saha
- vartate
- cetanā
- daśabhiḥ
- yāvat
- śubhaiḥ
- na
- eka-aṣṭa-pañcabhiḥ

Expanded syntax:

> cetanā aśubhaiḥ karmapathaiḥ yugapat yāvad aṣṭābhiḥ saha vartate; śubhaiḥ karmapathaiḥ yāvad daśabhiḥ saha vartate, na tu ekena, pañcabhiḥ, aṣṭābhiḥ.

## 4. Grammar

- **yugapat** — simultaneously, in one practical occurrence.
- **yāvat** — as many as, up to.
- **aṣṭābhiḥ** — instrumental plural, “with eight.”
- **aśubhaiḥ** — instrumental plural, “with unwholesome [karmic courses].”
- **saha vartate** — occurs together with, operates in conjunction with.
- **cetanā** — intention, volitional or practical direction.
- **daśabhiḥ** — instrumental plural, “with ten.”
- **śubhaiḥ** — instrumental plural, “with wholesome [karmic courses].”
- **eka-aṣṭa-pañcabhiḥ** — compressed numerical compound representing exactly one, eight, and five as excluded wholesome totals.

## 5. Literal Translation

> Intention occurs simultaneously with as many as eight unwholesome courses. With wholesome courses it occurs with as many as ten, but not with one, five, or eight.

## 6. Philosophical Translation

> A single practical intention can organize several unwholesome courses at once, although no occurrence contains all ten unwholesome courses together. Wholesome intention can integrate the complete tenfold course, but the possible wholesome configurations are structurally constrained: they do not occur as arbitrary collections of one, five, or eight. Practical unity is therefore neither an isolated inner act nor an accidental heap of behaviors; it is a determinate conjunction whose permitted combinations depend upon the form of the action and its conditions.

## 7. Technical Vocabulary

### yugapat

Real simultaneity within one practical event: one governing intention with several jointly operative determinations.

### cetanā

The directional activity that selects an end, organizes preparation, coordinates expression, and carries action toward completion. It is not merely a private mental wish.

### aśubha / śubha

- **aśubha** — unwholesome, practically unfavorable, productive of unfavorable result.
- **śubha** — wholesome, practically favorable.

### Cardinality

The verse asks how many determinate courses may coexist under one intention. Number here expresses the possible structure of a practical whole.

## 8. Doctrinal Determination

The verse distinguishes governing intention from the determinate courses with which it operates. An unwholesome intention may coexist with as many as eight of the ten courses; therefore the ten unwholesome courses are not all mutually compossible in one practical occurrence. The exact maximal configuration belongs to the Bhāṣya.

Wholesome intention can coexist with all ten wholesome courses. This means complete tenfold integration is possible. Yet the totals one, five, and eight are excluded, showing that the wholesome courses are not freely selectable as arbitrary independent units. Their combinations are governed by structural conditions.

A provisional asymmetry appears:

- unwholesome multiplicity may be extensive, but complete tenfold unity is unavailable;
- wholesome activity can form complete tenfold integration, but not every partial cardinality is possible.

## 9. Logical Determination

Let:

- **I** = one occurrence of intention;
- **U** = the set of unwholesome courses conjoined with I;
- **W** = the set of wholesome courses conjoined with I.

Then:

- |U| ≤ 8
- |W| ≤ 10
- |W| ≠ 1
- |W| ≠ 5
- |W| ≠ 8

The verse concerns simultaneous manifestation, not mere endowment. Possessing a course in the continuum is not identical with its co-occurrence in the present intention-event.

A practical event is better modeled as a constrained multi-place structure than as a single binary relation. Not every subset of courses is valid; compatible objects, roots, modes, completion conditions, and a shared intention are required.

## 10. Light Organon Interpretation

Primary interpretation: this belongs to the Kernel’s rational possibility-space, not directly to the free TS Agent.

The Kernel must represent:

- one intention-event with multiple jointly instantiated courses;
- upper bounds on composition;
- excluded cardinalities;
- compatibility constraints;
- the distinction between endowment and present co-occurrence.

A suitable Kernel-level structure is:

```text
PracticalEvent {
    governingIntention
    bodilyCourses[]
    verbalCourses[]
    mentalCourses[]
    objectSupports[]
    completionStates[]
    compatibilityConstraints[]
}
```

The central design rule is:

> one event does not imply one determination, and individually valid components do not automatically form a valid conjunction.

This is Logic as substrate: the Kernel defines what can co-occur, what cannot, and what combinations form a possible practical whole. The Agent may later navigate this field freely, but the verse itself first specifies the strict possibility-space in which rational agency can be represented.

## 11. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_81
    a vak:Karika ;
    rdfs:label "VAkK 4.81" ;
    vak:hasTopic vak:SimultaneousKarmicCourseConjunction .

vak:Intention
    rdfs:label "cetanā" ;
    vak:mayCoOccurWith
        vak:WholesomeKarmicCourse,
        vak:UnwholesomeKarmicCourse .

vak:UnwholesomeCourseConjunction
    a logic:ConstrainedPracticalComposition ;
    vak:hasMaximumCardinality 8 .

vak:WholesomeCourseConjunction
    a logic:ConstrainedPracticalComposition ;
    vak:hasMaximumCardinality 10 ;
    vak:excludesCardinality 1, 5, 8 .

vak:SimultaneousKarmicCourseConjunction
    rdfs:subClassOf logic:EventLevelComposition ;
    vak:requires vak:SharedGoverningIntention ;
    vak:requires vak:CourseCompatibility .
```

Rules:

```text
SingleIntentionEvent(?event)
    does not imply
SingleKarmicDetermination(?event)
```

```text
IndividuallyValid(?a)
and IndividuallyValid(?b)
    does not imply
ValidConjunction(?a, ?b)
```

## 12. Commit Note

VAK_4.81 — Define simultaneous conjunctions of intention and karmic courses

- introduce yugapat as simultaneous practical conjunction;
- specify an eightfold maximum for unwholesome courses;
- specify a tenfold maximum for wholesome courses;
- record the exclusion of wholesome totals one, five, and eight;
- distinguish simultaneous manifestation from mere endowment;
- model one intention as the unity of multiple practical determinations;
- interpret the verse primarily as Kernel-level practical logic and constrained composition.
