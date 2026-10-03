# VAK_1.47

## 1. Sanskrit (Devanāgarī)

> तथा श्रोत्रं त्रयाणां तु सर्वमेव स्वभूमिकम् ।
>
> कायविज्ञानमधरस्वभूम्यनियतं मनः ॥ १.४७ ॥

The immediate source file prints `अधरसवभूमि`, which is mechanically
irregular. The study text follows the IAST witness and the Bhāṣya's explicit
analysis: `adhara-svabhūmi`, “of a lower or its own plane.”

## 2. Sanskrit (IAST)

> tathā śrotraṃ trayāṇāṃ tu sarvam eva svabhūmikam /
>
> kāyavijñānam adharasvabhūmy aniyataṃ manaḥ // 1.47 //

## 3. Lexical Analysis

```text
sarvam eva          → sarvam eva
svabhūmikam         → sva-bhūmikam
kāyavijñānam        → kāya-vijñānam
adharasvabhūmi      → adhara-sva-bhūmi
aniyataṃ manaḥ      → aniyatam manaḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| tathā | indeclinable adverb | likewise; the ear follows the eye-rule of 1.46 |
| śrotram | nominative neuter singular | Ear Faculty Principle |
| trayāṇām | genitive masculine plural | of the three: nose, tongue, and body faculties |
| tu | contrastive particle | but; marks a different rule for the remaining three senses |
| sarvam | nominative neuter singular | all three components: Faculty, field, and Cognition |
| eva | restrictive-emphatic particle | precisely; only |
| svabhūmikam | nominative neuter singular | belonging to its own plane |
| kāyavijñānam | nominative neuter singular compound | Body-Cognition Principle |
| adhara-sva-bhūmi | compound predicate | belonging to a lower plane or its own plane |
| aniyatam | nominative neuter singular adjective | not fixed to one plane-relation |
| manaḥ | nominative neuter singular | Mind Principle |

`Sarvam` is distributive over the Nose, Tongue, and Body triads. The Bhāṣya
identifies their three components as Faculty, field, and Cognition.

## 4. Grammar

`Tathā śrotram` carries forward the complete relational structure of the eye
from 1.46:

```text
the Ear Principle is not lower than the Body Principle
the sound field is not higher than the Ear Principle
Ear-Cognition is not higher than the Ear Principle
```

The remaining relations also carry over: the sound field may be higher, lower,
or on the same plane as Ear-Cognition; both may bear any of these relations to
the Body Principle.

The contrastive `tu` introduces a general rule (`utsarga`) for the three
contact faculties:

```text
trayāṇām tu sarvam eva svabhūmikam
    for the three, everything belongs to its own plane
```

The Bhāṣya distributes this over:

```text
Nose Faculty + smell field + Nose-Cognition
Tongue Faculty + taste field + Tongue-Cognition
Body Faculty + tangible Form field + Body-Cognition
```

The next phrase qualifies the third triad. The Body Faculty and tangible Form
field remain on the being's own plane, but:

```text
kāyavijñānam adhara-sva-bhūmi
    Body-Cognition belongs to a lower plane or its own plane
```

Finally, `aniyataṃ manaḥ` is an independent nominal clause. The Bhāṣya defines
“not fixed” relationally: Mind may be on the same, a higher, or a lower plane
relative to the Body Principle, Mind-Cognition, and Essence Principles.

## 5. Translation

### Close syntactic construe

> Likewise the Ear. For the three, all belong precisely to their own plane. Body-Cognition belongs to a lower plane or its own plane. Mind is not fixed.

### Bhāṣya-informed translation

> The Ear Principle, sound field, and Ear-Cognition follow the same plane-relations as the Eye Principle, visible Form field, and Eye-Cognition. For Nose, Tongue, and Body, each Faculty, field, and Cognition belongs to its own plane. Body-Cognition is qualified: it may belong either to the being's own plane or to a lower one, although the Body Faculty and tangible Form field remain on the own plane. Mind has no single fixed plane-relation; it may be on the same, a higher, or a lower plane relative to the Body Principle, Mind-Cognition, and Essence Principles.

## 6. Philosophical Translation

> The plane rules are not identical for every Faculty-Cognition relation. Eye and Ear share the bounded relations stated in 1.46. Nose, Tongue, and Body are generally own-plane triads; Body-Cognition alone may be on a lower plane while its Faculty and tangible Form field remain on the being's own plane. Mind's plane-relation may be same, higher, or lower, with the Bhāṣya pointing to meditative attainment and rebirth as contexts for that variation.

Organon reading:

> The verse classifies plane-relations among differentiated Principles, Faculties, and fields. In the project's Principle Pipeline reading, these secondary Principles remain Principles because they arise within and stand on the recursive Principle structure; that does not make every Cognition the Pure Principle itself. Mind's variable plane-relation is still a conditioned rule, not freedom from the Principle system.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| śrotra | Ear Faculty Principle | governed by the plane-relations already stated for the Eye |
| trayāṇām | of the three | nose, tongue, and body faculties |
| ghrāṇa | Nose Faculty Principle | in the own-plane Nose-Cognition triad |
| jihvā | Tongue Faculty Principle | in the own-plane Tongue-Cognition triad |
| kāyadhātu | Body Faculty Principle | own-plane in this discussion |
| spraṣṭavya | tangible Form field | own-plane in this discussion |
| kāyavijñāna | Body-Cognition Principle | own-plane or lower-plane |
| svabhūmika | belonging to its own plane | the same plane as the relevant being or triad |
| adhara-sva-bhūmi | lower-plane or own-plane | the two permitted planes for Body-Cognition |
| aniyata | not fixed to one plane-relation | permits same-, higher-, or lower-plane relations |
| manas | Mind Principle | variable in plane-relation, but not unconditioned |
| utsarga | general rule | the own-plane classification for the three triads |
| apavāda | qualification | the lower-or-own-plane range of Body-Cognition |
| samāpatti | meditative attainment | one context of cross-plane mental operation |
| upapatti | rebirth / arising | another context of cross-plane operation |

## 8. Logical Determination

The auditory rule imports the structure of 1.46:

```text
Plane(BodyPrinciple) ≤ Plane(EarPrinciple)
Plane(SoundField) ≤ Plane(EarPrinciple)
Plane(EarCognition) ≤ Plane(EarPrinciple)
```

The general contact rule is:

```text
For S in {Nose, Tongue}:
    Plane(Faculty(S))
        = Plane(Field(S))
        = Plane(Cognition(S))
        = OwnPlane

Plane(BodyFaculty) = Plane(TangibleFormField) = OwnPlane
```

The Bhāṣya then qualifies only the Body-Cognition term:

```text
Plane(BodyFaculty) = OwnPlane
Plane(TangibleFormField) = OwnPlane

Plane(BodyCognition)
    ∈ {OwnPlane, LowerPlane}
```

The condition is illustrated by the plane of birth:

```text
BornIn(DesireRealm | FirstAbsorption)
    → Plane(BodyCognition) = OwnPlane

BornIn(SecondOrHigherAbsorption)
    → Plane(BodyCognition) = LowerPlane
```

Mind receives no single ordering constraint:

```text
Compare(Plane(MindPrinciple), Plane(BodyPrinciple | MindCognition | EssencePrinciples))
    ∈ {SamePlane, HigherPlane, LowerPlane}
```

Accordingly:

```text
aniyata
    ≠ uncaused
    ≠ chaotic
    = no invariant plane-relation
```

These are plane constraints within the verse's classification of Principles;
they do not turn a variable relation into an unconditioned one.

## 9. Interpretive Note

VAK 1.47 completes the plane analysis begun in 1.46. It first transfers the
Eye, visible Form, and Eye-Cognition relations to hearing, then gives the
Nose, Tongue, and Body triads an own-plane rule. The Bhāṣya qualifies that
rule for Body-Cognition.

For a being born in the Desire Realm or first absorption, Body-Cognition is
own-plane. For one born in the second or higher absorptions, Body-Cognition is
lower-plane. The Body Faculty and tangible Form field remain on the being's
own plane. The Bhāṣya leaves the fuller account of Mind's plane variation to
its later discussion of meditative attainment.

`Aniyataṃ manaḥ` means that Mind has no single fixed plane-relation: it may be
same, higher, or lower relative to the named Principles. This does not mean
unconditioned or unlimited Cognition; the Bhāṣya points to meditative
attainment and rebirth but defers the full explanation.

In the Organon reading, this is a differentiated system of Principles: each
secondary Principle remains a Principle by standing within the Principle
Pipeline, while the Pure Principle is the recursive structure itself. The
verse's plane rules specify relations among those differentiated Principles;
they do not identify Mind with the Pure Principle.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_47
    a vak:Karika ;
    rdfs:label "VAK 1.47" ;
    vak:hasTopic vak:PlaneRelationsOfFacultiesFieldsAndCognitions ;
    vak:belongsTo vak:Dhatunirdesa .

vak:EarPrinciple
    vak:inheritsPlaneRuleFrom vak:EyePrinciple .

vak:SoundField
    vak:inheritsPlaneRuleFrom vak:VisibleFormField .

vak:EarCognition
    vak:inheritsPlaneRuleFrom vak:EyeCognition .

vak:NoseTriad
    vak:hasMembers vak:NoseFacultyPrinciple,
        vak:SmellField,
        vak:NoseCognition ;
    vak:hasPlaneRelation vak:OwnPlane .

vak:TongueTriad
    vak:hasMembers vak:TongueFacultyPrinciple,
        vak:TasteField,
        vak:TongueCognition ;
    vak:hasPlaneRelation vak:OwnPlane .

vak:BodyTriad
    vak:hasMembers vak:BodyFacultyPrinciple,
        vak:TangibleFormField,
        vak:BodyCognition ;
    vak:hasGeneralRule vak:OwnPlaneOperation .

vak:BodyFacultyPrinciple,
vak:TangibleFormField
    vak:hasPlaneRelation vak:OwnPlane .

vak:BodyCognition
    vak:hasPlaneRelation vak:OwnPlane,
        vak:LowerPlane ;
    vak:isExceptionTo vak:OwnPlaneOperation .

vak:MindPrinciple
    vak:hasVariablePlaneRelation vak:SamePlane,
        vak:HigherPlane,
        vak:LowerPlane ;
    rdfs:comment "Variable within the conditions described by the Bhāṣya; not unconditioned or unlimited." .

organon:KosaPrinciplePipeline
    rdfs:label "Kośa as the recursive Principle Pipeline" ;
    rdfs:comment "Project interpretation: differentiated Principles remain Principles through their grounding in the Principle Pipeline; this is not the literal wording of VAK 1.47." .
```
