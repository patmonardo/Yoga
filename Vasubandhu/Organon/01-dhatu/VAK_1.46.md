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

| Pada | Morphology | Force in this passage |
|---|---|---|
| na | negative particle | not |
| kāyasya | genitive masculine singular | relative to the Body |
| adharam | nominative neuter singular adjective | on a lower plane |
| cakṣuḥ | nominative neuter singular | the Eye Faculty |
| ūrdhvam | nominative neuter singular adjective | on a higher plane |
| rūpam | nominative neuter singular | visible Form |
| na cakṣuṣaḥ | negative particle and genitive singular | not higher than the Eye |
| vijñānam | nominative neuter singular | Cognition; here, Eye-Cognition |
| ca | conjunction | and; carries forward the restriction |
| asya | genitive neuter singular pronoun | relative to that Cognition |
| tu | contrastive particle | but; introduces the broader comparisons |
| ubhe | nominative neuter dual | both visible Form and Cognition |
| sarvataḥ | indeclinable adverb | in all three relations: higher, lower, or same plane |

The verse omits repeated comparison terms. The commentary supplies them
and resolves the pronoun as referring to the immediately preceding
Eye-Cognition.

## 4. Grammar

The commentary first asks whether Body, Eye, visible Form, and
Eye-Cognition always belong to one plane or can belong to different
planes. It states three restrictions:

```text
Body plane ≤ Eye plane
Visible Form plane ≤ Eye plane
Eye-Cognition plane ≤ Eye plane
```

The Eye is therefore on the Body's plane or a higher plane. Visible Form
and Eye-Cognition are each on the Eye's plane or a lower plane. The final
comparisons allow three relations:

```text
Visible Form relative to Eye-Cognition
Visible Form relative to Body
Eye-Cognition relative to Body
    each may be higher, lower, or on the same plane
```

These comparisons do not remove the stated restrictions or the distinct
plane ranges assigned to the four terms.

## 5. Translation

### Close syntactic construe

> The Eye is not lower than the Body; visible Form is not higher than the Eye, nor is its Cognition. But relative to that [Eye-Cognition], visible Form may be higher, lower, or on the same plane; and relative to the Body, both may be in any of those three relations.

### Commentary-informed translation

> The Eye Faculty may be on the Body's plane or a higher plane, but never a lower one. Visible Form and Eye-Cognition may each be on the Eye's plane or a lower one, but never a higher one. Relative to Eye-Cognition, visible Form may be higher, lower, or on the same plane; relative to the Body, both visible Form and Eye-Cognition may stand in any of those three relations.

The commentary assigns Body, Eye, and visible Form five possible planes:
the Desire Realm and the first through fourth meditative levels.
Eye-Cognition is restricted to two: the Desire Realm and the first
meditative level.

## 6. Logical Determination

Let `P(x)` denote the plane of an item in the comparison. The restrictions
are:

```text
P(Body) ≤ P(EyeFaculty)
P(VisibleForm) ≤ P(EyeFaculty)
P(EyeCognition) ≤ P(EyeFaculty)

```

The unrestricted comparisons are:

```text
Compare(P(VisibleForm), P(EyeCognition))
    ∈ {higher, lower, equal}

Compare(P(VisibleForm), P(Body))
    ∈ {higher, lower, equal}

Compare(P(EyeCognition), P(Body))
    ∈ {higher, lower, equal}
```

Thus:

```text
EyeFaculty
    → sets the upper plane limit for Body, VisibleForm,
      and Eye-Cognition
```

The free comparisons do not cancel these limits or show that every
combination satisfying them occurs.

## 7. Interpretation

This verse specifies plane-relations among Body, the Eye Faculty, visible
Form, and Eye-Cognition. The Eye Faculty is not below the Body, while visible
Form and Eye-Cognition are not above the Eye Faculty.

This Principle analysis treats the plane relations as comparisons among
distinct factors, not as another inventory. The other comparisons are not
fixed by the shared upper limit. Visible Form may be
higher, lower, or on the same plane as Eye-Cognition; each may likewise
stand in any of those three relations to the Body. These are relations among
the stated levels, not measurements of physical height.

In the governing model, Vijñāna as Discriminative Cognition joins and
governs Perception and Conception. Their unity is Inconceivable as a
homogeneous operation, and its Idea is disclosed in Cognition Base.
Vijñāna governs Manas and guides the reading of Dharma Base. Form Base
and Dharma Base classify the same *avijñapti* distinctly; Vijñāna bears
a *prati* relation to it and remains distinct from consciousness and Mind.

## 8. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_46
    a vak:Karika ;
    rdfs:label "VAK 1.46" ;
    vak:hasTopic vak:PlaneRelationsAmongPrinciples ;
    vak:belongsTo vak:PrincipleAnalysis .

vak:EyeFaculty
    a vak:Faculty ;
    vak:planeNotBelow vak:Body ;
    vak:planeUpperBoundFor vak:VisibleForm,
        vak:EyeCognition .

vak:VisibleForm
    a vak:Form ;
    vak:conditionFor vak:EyeCognition ;
    vak:planeNotAbove vak:EyeFaculty ;
    vak:hasUnrestrictedPlaneRelationTo vak:EyeCognition,
        vak:Body .

vak:EyeCognition
    a vak:Cognition ;
    vak:planeNotAbove vak:EyeFaculty ;
    vak:hasUnrestrictedPlaneRelationTo vak:Body .

vak:UnrestrictedPlaneRelation
    vak:allows vak:HigherPlane,
        vak:LowerPlane,
        vak:SamePlane .

```
