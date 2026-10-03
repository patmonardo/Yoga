# VAK_1.46

## 1. Sanskrit (Devanāgarī)

> न कायस्याधरं चक्षुरूर्ध्वं रूपं न चक्षुषः ।
>
> विज्ञानं चास्य रूपं तु कायस्योभे च सर्वतः ॥ १.४६ ॥

## 2. Sanskrit (IAST)

> na kāyasyādharaṃ cakṣur ūrdhvaṃ rūpaṃ na cakṣuṣaḥ /
>
> vijñānaṃ cāsya rūpaṃ tu kāyasyobhe ca sarvataḥ // 1.46 //

## 3. Lexical Analysis

```text
kāyasyādharam     → kāyasya adharam
cakṣur ūrdhvam    → cakṣuḥ ūrdhvam
vijñānaṃ cāsya    → vijñānam ca asya
kāyasyobhe        → kāyasya ubhe
```

| Form | Morphology | Lexical force here |
|---|---|---|
| na | negative particle | not; never within the stated relation |
| kāyasya | genitive masculine singular | relative to the Body Principle |
| adharam | nominative neuter singular adjective | lower; belonging to a lower plane |
| cakṣuḥ | nominative neuter singular | Eye Faculty Principle |
| ūrdhvam | nominative neuter singular adjective | higher; belonging to a higher plane |
| rūpam | nominative neuter singular | visible Form field |
| na cakṣuṣaḥ | negative particle with genitive neuter singular | not higher relative to the eye |
| vijñānam | nominative neuter singular | Eye-Cognition Principle |
| ca | conjunction | and; extends the preceding restriction |
| asya | genitive neuter singular pronoun | relative to this, namely Eye-Cognition |
| tu | contrastive particle | but; introduces the unrestricted relation |
| ubhe | nominative neuter dual | both: visible Form and Eye-Cognition |
| sarvataḥ | indeclinable adverb | across all three plane-relations: higher, lower, or same |

The surface verse omits repeated relational terms. The Bhāṣya supplies the
governing comparisons and fixes `asya` as referring to the immediately
preceding Eye-Cognition.

## 4. Grammar

The first pāda states a relation between Body and Eye:

```text
na kāyasya adharam cakṣuḥ
    the Eye is not lower than the Body
```

For a Body belonging to a given plane, the Eye may be on that plane or a
higher one, never a lower one.

The next restriction coordinates two subjects under the comparison with the
eye:

```text
ūrdhvaṃ rūpaṃ na cakṣuṣaḥ
    visible Form is not higher than the Eye

vijñānaṃ ca [ūrdhvaṃ na cakṣuṣaḥ]
    and Eye-Cognition is not higher than the Eye
```

The final half-verse reverses the restrictive construction:

```text
asya [vijñānasya] rūpaṃ tu sarvataḥ
    relative to this Eye-Cognition, visible Form may stand in every relation

kāyasya ubhe ca sarvataḥ
    relative to the Body, both visible Form and Eye-Cognition may stand
    in every relation
```

Here `sarvataḥ` is not a vague universality. The Bhāṣya explicitly distributes
it as higher plane, lower plane, or the same plane. The verse therefore
states five plane-relations, not one general hierarchy.

## 5. Translation

### Close syntactic construe

> The Eye is not lower than the Body; visible Form is not higher than the Eye, nor is its Cognition. But relative to that [Eye-Cognition], visible Form may be higher, lower, or on the same plane; and relative to the Body, both may be in any of those three relations.

### Bhāṣya-informed translation

> The Eye may belong to the Body's own plane or to a higher plane, but never to a lower one. Visible Form and Eye-Cognition may each belong to the Eye's own plane or to a lower plane, but never to a higher one. Relative to Eye-Cognition, however, visible Form may be higher, lower, or on the same plane; relative to the Body, both visible Form and Eye-Cognition may stand on any of the three planes.

The Bhāṣya extends this same distribution to the Ear, sound, and auditory
Cognition.

## 6. Philosophical Translation

> These plane-relations have distinct bounds. The Eye may be at or above the Body's plane, while the visible Form field and Eye-Cognition may be at or below the Eye's. Visible Form and Eye-Cognition may each stand higher, lower, or on the same plane relative to the Body and to one another.

Organon rendering:

> The Principles have typed relations across planes. The Eye Principle bounds the plane of the visible Form field and Eye-Cognition from above; the Body Principle does not impose that same bound. `Sarvataḥ` here means the three defined relations—higher, lower, and same plane—not unrestricted access.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| kāya | Body Principle | embodied basis used as one term of plane-comparison |
| cakṣus | Eye Principle | visual Faculty and the governing support in this relation |
| rūpa | visible Form field | field accessible to the visual Faculty |
| vijñāna | Cognition Principle | here, Eye-Cognition |
| bhūmi | plane | existential or meditative level, not geometric position |
| kāmāvacara | belonging to the Desire Realm | one possible plane of Body, Eye, Form, and Eye-Cognition |
| dhyānabhūmi | absorption-plane | higher meditative plane involved in the distribution |
| adhara | lower | belonging to a lower plane than the comparison-term |
| ūrdhva | higher | belonging to a higher plane than the comparison-term |
| svabhūmika | belonging to the same plane | the equality case supplied by the Bhāṣya |
| sarvataḥ | in every plane-relation | higher, lower, or equal |

The Bhāṣya gives Body, Eye, and visible Form five possible planes: the Desire
Realm and the four absorptions. Eye-Cognition belongs only to two: the Desire
Realm and the first absorption.

## 8. Logical Determination

Let `P(x)` denote the plane of a Principle. The restrictive rules are:

```text
P(Body) ≤ P(EyePrinciple)

P(VisibleFormField) ≤ P(EyePrinciple)

P(EyeCognition) ≤ P(EyePrinciple)
```

The unrestricted comparisons are:

```text
Compare(P(VisibleFormField), P(EyeCognition))
    ∈ {higher, lower, equal}

Compare(P(VisibleFormField), P(Body))
    ∈ {higher, lower, equal}

Compare(P(EyeCognition), P(Body))
    ∈ {higher, lower, equal}
```

Thus:

```text
EyePrinciple
    → UpperBounds(VisibleFormField)
    ∧ UpperBounds(EyeCognition)

BodyPrinciple
    ↛ UpperBounds(VisibleFormField)
    ∧ ↛ UpperBounds(EyeCognition)
```

The three restrictive relations share the Eye Principle as their bound:

```text
BodyPrinciple ≤ EyePrinciple
VisibleFormField ≤ EyePrinciple
EyeCognition ≤ EyePrinciple
```

This diagram does not order visible Form and Eye-Cognition relative to each
other. Their plane-relation remains three-valued.

## 9. Interpretive Note

VAK 1.45 established that alteration in a Faculty corresponds to alteration
in its Cognition. VAK 1.46 specifies plane-relations among Body, Eye, visible
Form, and Eye-Cognition. The Eye Principle is the shared upper bound: Body
cannot be on a higher plane than Eye, while visible Form and Eye-Cognition
cannot be higher than Eye.

The other comparisons are not fixed by that bound. Visible Form may be
higher, lower, or on the same plane as Eye-Cognition; each may likewise
stand in any of those three relations to Body. `Bhūmi` names a realm or
meditative plane, not geometric height.

In the Organon model, these are relational rules among Principles, not a
flat inventory. Dhātu is Pure Principle—Abhidharma itself—and the
differentiated Cognitions are impure *prajñā* products situated within
the Principle Pipeline. This is project interpretation, not a claim
attributed to the Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_46
    a vak:Karika ;
    rdfs:label "VAK 1.46" ;
    vak:hasTopic vak:PlaneRelationsAmongPrinciples ;
    vak:belongsTo vak:Dhatunirdesa .

vak:EyePrinciple
    a vak:FacultyPrinciple ;
    vak:notLowerThan vak:BodyPrinciple ;
    vak:upperBoundsPlaneOf vak:VisibleFormField,
        vak:EyeCognition .

vak:VisibleFormField
    a vak:Field ;
    vak:notHigherThan vak:EyePrinciple ;
    vak:hasUnrestrictedPlaneRelationTo vak:EyeCognition,
        vak:BodyPrinciple .

vak:EyeCognition
    a vak:CognitionPrinciple ;
    vak:notHigherThan vak:EyePrinciple ;
    vak:hasUnrestrictedPlaneRelationTo vak:BodyPrinciple .

vak:UnrestrictedPlaneRelation
    vak:allows vak:HigherPlane,
        vak:LowerPlane,
        vak:SamePlane .

organon:PrinciplePlaneRelations
    organon:mayCarry vak:PlaneConstraint .
```
