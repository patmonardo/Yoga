# VAK_1.46

## 1. Sanskrit (Devanāgarī)

> न कायस्याधरं चक्षुरूर्ध्वं रूपं न चक्षुषः ।
>
> विज्ञानं चास्य रूपं तु कायस्योभे च सर्वतः ॥ १.४६ ॥

## 2. Sanskrit (IAST)

> na kāyasyādharaṃ cakṣur ūrdhvaṃ rūpaṃ na cakṣuṣaḥ /
>
> vijñānaṃ cāsya rūpaṃ tu kāyasyobhe ca sarvataḥ // 1.46 //

## 3. Padaccheda

```text
kāyasyādharam     → kāyasya adharam
cakṣur ūrdhvam    → cakṣuḥ ūrdhvam
vijñānaṃ cāsya    → vijñānam ca asya
kāyasyobhe        → kāyasya ubhe
```

| Form | Morphology | Lexical force here |
|---|---|---|
| na | negative particle | not; never within the stated relation |
| kāyasya | genitive masculine singular | relative to the body |
| adharam | nominative neuter singular adjective | lower; belonging to a lower plane |
| cakṣuḥ | nominative neuter singular | eye-faculty / eye-Domain |
| ūrdhvam | nominative neuter singular adjective | higher; belonging to a higher plane |
| rūpam | nominative neuter singular | visible form / visible-form Domain |
| na cakṣuṣaḥ | negative particle with genitive neuter singular | not higher relative to the eye |
| vijñānam | nominative neuter singular | eye-knowledge / eye-knowledge Domain |
| ca | conjunction | and; extends the preceding restriction |
| asya | genitive neuter singular pronoun | relative to this, namely eye-knowledge |
| tu | contrastive particle | but; introduces the unrestricted relation |
| ubhe | nominative neuter dual | both: visible form and eye-knowledge |
| sarvataḥ | indeclinable adverb | in every plane-relation: higher, lower, or equal |

The surface verse omits repeated relational terms. The Bhāṣya supplies the
governing comparisons and fixes `asya` as referring to the immediately
preceding eye-knowledge.

## 4. Grammar

The first pāda states a relation between body and eye:

```text
na kāyasya adharam cakṣuḥ
    the eye is not lower than the body
```

For a body belonging to a given plane, the eye may be on that plane or a
higher one, never a lower one.

The next restriction coordinates two subjects under the comparison with the
eye:

```text
ūrdhvaṃ rūpaṃ na cakṣuṣaḥ
    visible form is not higher than the eye

vijñānaṃ ca [ūrdhvaṃ na cakṣuṣaḥ]
    and eye-knowledge is not higher than the eye
```

The final half-verse reverses the restrictive construction:

```text
asya [vijñānasya] rūpaṃ tu sarvataḥ
    relative to this eye-knowledge, visible form may stand in every relation

kāyasya ubhe ca sarvataḥ
    relative to the body, both visible form and eye-knowledge may stand
    in every relation
```

Here `sarvataḥ` is not a vague universality. The Bhāṣya explicitly distributes
it as higher plane, lower plane, or the same plane. The verse therefore
contains five exact relational rules, not one general hierarchy.

## 5. Translation

### Close syntactic construe

> The eye is not lower than the body; visible form is not higher than the eye, nor is its knowledge. But relative to that [eye-knowledge], visible form may be in every relation; and relative to the body, both may be in every relation.

### Bhāṣya-informed translation

> The eye may belong to the body's own plane or to a higher plane, but never to a lower one. Visible form and eye-knowledge may each belong to the eye's own plane or to a lower plane, but never to a higher one. Relative to eye-knowledge, however, visible form may be higher, lower, or equal; and relative to the body, both visible form and eye-knowledge may be higher, lower, or equal.

The Bhāṣya extends this same distribution to ear, sound, and auditory
knowledge.

## 6. Philosophical Translation

> A cognitive relation is ordered not by one uniform scale but by the role of each term. The faculty may exceed the plane of embodiment, but it cannot fall below it. The object and its corresponding knowledge cannot exceed the faculty, which therefore bounds their reach. Yet object and knowledge may vary freely in level relative to one another, and both may vary freely relative to the body.

Organon rendering:

> The Domain-system now determines the vertical reach of a sensory power. Embodiment, faculty, object, and knowledge are distinct coordinates. The eye-Domain governs the maximal plane accessible to visual disclosure; the body-Domain alone does not. A Smart Domain is therefore not merely a classified item: it bears typed constraints governing which other Domains it can support, disclose, and coordinate across planes.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| kāya | body / body-Domain | embodied basis used as one term of plane-comparison |
| cakṣus | eye / eye-Domain | visual faculty and the governing support in this relation |
| rūpa | visible form / visible-form Domain | object accessible to the visual faculty |
| vijñāna | knowledge / knowledge-Domain | here, eye-knowledge |
| bhūmi | plane | existential or meditative level, not geometric position |
| kāmāvacara | belonging to the Desire Realm | one possible plane of body, eye, form, and eye-knowledge |
| dhyānabhūmi | absorption-plane | higher meditative plane involved in the distribution |
| adhara | lower | belonging to a lower plane than the comparison-term |
| ūrdhva | higher | belonging to a higher plane than the comparison-term |
| svabhūmika | belonging to the same plane | the equality case supplied by the Bhāṣya |
| sarvataḥ | in every plane-relation | higher, lower, or equal |

The Bhāṣya gives body, eye, and visible form five possible planes: the Desire
Realm and the four absorptions. Eye-knowledge belongs only to two: the Desire
Realm and the first absorption.

## 8. Logical Determination

Let `P(x)` denote the plane of a Domain-instance. The restrictive rules are:

```text
P(Body) ≤ P(Eye)

P(VisibleForm) ≤ P(Eye)

P(EyeKnowledge) ≤ P(Eye)
```

The unrestricted comparisons are:

```text
Compare(P(VisibleForm), P(EyeKnowledge))
    ∈ {higher, lower, equal}

Compare(P(VisibleForm), P(Body))
    ∈ {higher, lower, equal}

Compare(P(EyeKnowledge), P(Body))
    ∈ {higher, lower, equal}
```

Thus:

```text
EyeDomain
    → UpperBounds(VisibleFormDomain)
    ∧ UpperBounds(EyeKnowledgeDomain)

BodyDomain
    ↛ UpperBounds(VisibleFormDomain)
    ∧ ↛ UpperBounds(EyeKnowledgeDomain)
```

The eye occupies the determining middle:

```text
Body
    ≤ Eye
    ≥ VisibleForm
    ≥ EyeKnowledge
```

This diagram does not order visible form and eye-knowledge relative to each
other. Their plane-relation remains three-valued.

## 9. Interpretive Note

VAK 1.45 established the faculty as the determining support of its knowledge.
VAK 1.46 gives that determination a vertical range. The eye does more than
differentiate visual from auditory knowledge: its own plane sets the upper
limit for the visual object and knowledge-event.

The body does not exercise the same constraint. A lower-plane body may employ
a higher-plane eye; both visible form and eye-knowledge may also stand above,
below, or level with the body. Consequently, `body`, `faculty`, `object`, and
`knowledge` cannot be collapsed into a single material or subjective layer.
Each is a Domain with its own admissible relations.

This is indeed Dhātu all the way down—or, in this verse, all the way up and
down. The chapter's power lies less in naming eighteen items than in giving
their lineages a relational grammar. What appears in a flat English list as
“elements” is operating here as a typed system of cognitive reach.

The comparison remains internal to Kośa science. `Bhūmi` identifies realms and
meditative planes, not spatial height, Sāṃkhya guṇas, Buddhi, or Puruṣa. The
result belongs to the Agent's acquired technē: it specifies lawful sensory
operation without becoming Yoga metaphysics or Kernel Logic.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_46
    a vak:Karika ;
    rdfs:label "VAK 1.46" ;
    vak:hasTopic vak:PlaneRelationOfVisualDomains ;
    vak:belongsTo vak:Dhatunirdesa .

vak:EyeDomain
    a vak:FacultyDomain ;
    vak:notLowerThan vak:BodyDomain ;
    vak:upperBoundsPlaneOf vak:VisibleFormDomain,
        vak:EyeKnowledgeDomain .

vak:VisibleFormDomain
    a vak:ObjectDomain ;
    vak:notHigherThan vak:EyeDomain ;
    vak:hasUnrestrictedPlaneRelationTo vak:EyeKnowledgeDomain,
        vak:BodyDomain .

vak:EyeKnowledgeDomain
    a vak:KnowledgeDomain ;
    vak:notHigherThan vak:EyeDomain ;
    vak:hasUnrestrictedPlaneRelationTo vak:BodyDomain .

vak:UnrestrictedPlaneRelation
    vak:allows vak:HigherPlane,
        vak:LowerPlane,
        vak:SamePlane .

organon:SmartDomain
    organon:mayCarry vak:PlaneConstraint,
        vak:SupportConstraint,
        vak:ObjectReachConstraint .
```
