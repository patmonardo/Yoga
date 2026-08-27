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

## 3. Padaccheda

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
| śrotram | nominative neuter singular | ear-faculty / ear-Domain |
| trayāṇām | genitive masculine plural | of the three: nose, tongue, and body faculties |
| tu | contrastive particle | but; marks a different rule for the remaining three senses |
| sarvam | nominative neuter singular | everything: faculty, object, and knowledge |
| eva | restrictive-emphatic particle | precisely; only |
| svabhūmikam | nominative neuter singular | belonging to its own plane |
| kāyavijñānam | nominative neuter singular compound | body-knowledge; tactile knowledge |
| adhara-sva-bhūmi | compound predicate | belonging to a lower plane or its own plane |
| aniyatam | nominative neuter singular adjective | not fixed to one plane-relation |
| manaḥ | nominative neuter singular | mind / mind-Domain |

`Sarvam` is distributive over the triads belonging to the three faculties.
The Bhāṣya identifies the included terms as faculty, object, and knowledge.

## 4. Grammar

`Tathā śrotram` carries forward the complete relational structure of the eye
from 1.46:

```text
ear is not lower than body
sound is not higher than ear
auditory knowledge is not higher than ear
```

The remaining relations also carry over: sound may be higher, lower, or equal
relative to auditory knowledge; both sound and auditory knowledge may bear
any of these relations to the body.

The contrastive `tu` introduces a general rule (`utsarga`) for the three
contact faculties:

```text
trayāṇām tu sarvam eva svabhūmikam
    for the three, everything belongs to its own plane
```

The Bhāṣya distributes this over:

```text
nose + smell + olfactory knowledge
tongue + taste + gustatory knowledge
body + tangible object + body-knowledge
```

The next phrase introduces an exception (`apavāda`) to the third triad. Body
and tangible object remain own-plane, but:

```text
kāyavijñānam adhara-sva-bhūmi
    body-knowledge belongs to a lower plane or its own plane
```

Finally, `aniyataṃ manaḥ` is an independent nominal clause. The Bhāṣya defines
“not fixed” relationally: mind may be on the same, a higher, or a lower plane
relative to body, mental knowledge, and Dharma-Domains.

## 5. Translation

### Close syntactic construe

> Likewise the ear. But for the three, everything belongs precisely to its own plane. Body-knowledge belongs to a lower plane or its own plane. Mind is not fixed.

### Bhāṣya-informed translation

> The ear, sound, and auditory knowledge follow the same plane-relations as the eye, visible form, and visual knowledge. For nose, tongue, and body, the faculty, object, and knowledge normally belong to the same plane. Body-knowledge is the exception: it may belong either to the being's own plane or to a lower one, although body and tangible object remain own-plane. Mind has no single fixed plane-relation; it may be on the same, a higher, or a lower plane.

## 6. Philosophical Translation

> The sensory system does not impose one invariant relation upon every mode of knowledge. Vision and hearing can coordinate across planes under the faculty's limit. Smell, taste, and touch normally require identity of plane because their operation is by contact. Even here knowledge is not reducible to its bodily pair: tactile knowledge may operate from below the plane of the body and tangible object. Mind is still more mobile, since its plane-relation varies with embodiment, rebirth, and meditative attainment.

Organon rendering:

> The System of Knowledge differentiates its powers by their admissible range. A Domain carries not merely a name but an operating condition: distant sensory disclosure, contact-bound disclosure, exceptional lower-plane knowledge, or variable mental reach. The system thereby specifies how the Rational Agent can know under different conditions without pretending to derive the categories of knowing from a Science of Logic.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| śrotra | ear / ear-Domain | governed by the plane-relations already stated for the eye |
| trayāṇām | of the three | nose, tongue, and body faculties |
| ghrāṇa | nose / olfactory Domain | contact faculty normally restricted to its own plane |
| jihvā | tongue / gustatory Domain | contact faculty normally restricted to its own plane |
| kāyadhātu | body-Domain | tactile faculty; always own-plane in this discussion |
| spraṣṭavya | tangible object-Domain | tactile object; always own-plane here |
| kāyavijñāna | body-knowledge Domain | own-plane or lower-plane tactile knowledge |
| svabhūmika | belonging to its own plane | identity between operative plane and the relevant being's plane |
| adharabhūmika | belonging to a lower plane | the exceptional range of body-knowledge |
| aniyata | not fixed by plane | permits same-, higher-, or lower-plane relation |
| manas | mind / mind-Domain | variable in plane according to the operative situation |
| utsarga | general rule | the initial own-plane classification |
| apavāda | exception | the qualification concerning body-knowledge |
| samāpatti | meditative attainment | one context of cross-plane mental operation |
| upapatti | rebirth / arising | another context of cross-plane operation |

## 8. Logical Determination

The auditory rule imports the structure of 1.46:

```text
Plane(Body) ≤ Plane(Ear)
Plane(Sound) ≤ Plane(Ear)
Plane(AuditoryKnowledge) ≤ Plane(Ear)
```

The general contact rule is:

```text
For each S in {Smell, Taste, Touch}:
    Plane(Faculty(S))
        = Plane(Object(S))
        = Plane(Knowledge(S))
```

The Bhāṣya then overrides only part of the touch case:

```text
Plane(BodyFaculty) = OwnPlane
Plane(TangibleObject) = OwnPlane

Plane(BodyKnowledge)
    ∈ {OwnPlane, LowerPlane}
```

The condition is illustrated by the plane of birth:

```text
BornIn(DesireRealm | FirstAbsorption)
    → Plane(BodyKnowledge) = OwnPlane

BornIn(SecondOrHigherAbsorption)
    → Plane(BodyKnowledge) = LowerPlane
```

Mind receives no single ordering constraint:

```text
Compare(Plane(Mind), Plane(Body | MentalKnowledge | DharmaObject))
    ∈ {SamePlane, HigherPlane, LowerPlane}
```

Accordingly:

```text
aniyata
    ≠ uncaused
    ≠ chaotic
    = no invariant plane-relation
```

This is a determination within the System of Knowledge. Its formal
expression records the Kośa's classifications; it does not elevate those
classifications into Logic itself.

## 9. Interpretive Note

VAK 1.47 completes the plane-analysis begun in 1.46. It first transfers the
visual pattern to hearing, then distinguishes the three contact senses. Nose,
tongue, and body ordinarily require faculty, object, and knowledge to belong
to one plane. The classification is not flat: the Bhāṣya explicitly states a
general rule and then installs an exception.

That exception is revealing. For a being born in the Desire Realm or first
absorption, body-knowledge is own-plane. For one born in the second or higher
absorptions, body-knowledge is lower-plane. Body and tangible object remain
on the being's own plane while the corresponding knowledge operates through
a lower one. The knowledge-Domain therefore has a determination that cannot
be read directly from the bodily faculty-object pair.

`Aniyataṃ manaḥ` then gives mind a wider range, but not transcendence. “Not
fixed” means that its plane may be equal, higher, or lower according to
meditative attainment and rebirth. It does not mean lawless, unconditioned,
or identical with Puruṣa or Buddhi. Vasubandhu postpones the full account to
the Samāpattinirdeśa because it belongs to the system's later treatment of
attainment.

This is why the proper title for the achievement is a System of Knowledge.
The Kośa classifies the powers, objects, and events of knowing and specifies
their lawful ranges. It may exhibit an orderly form, and OWL++ may preserve
that form, but the Kośa neither generates Logic's categories nor replaces the
Organon's Kernel and Agent Logic.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_47
    a vak:Karika ;
    rdfs:label "VAK 1.47" ;
    vak:hasTopic vak:PlaneRangesOfSensoryAndMentalDomains ;
    vak:belongsTo vak:Dhatunirdesa .

vak:EarDomain
    vak:inheritsPlaneRuleFrom vak:EyeDomain .

vak:ContactSenseTriad
    vak:hasMembers vak:NoseDomain,
        vak:TongueDomain,
        vak:BodyDomain ;
    vak:hasGeneralRule vak:OwnPlaneOperation .

vak:BodyDomain,
vak:TangibleObjectDomain
    vak:hasPlaneRelation vak:OwnPlane .

vak:BodyKnowledgeDomain
    vak:hasPlaneRelation vak:OwnPlane,
        vak:LowerPlane ;
    vak:isExceptionTo vak:OwnPlaneOperation .

vak:MindDomain
    vak:hasVariablePlaneRelation vak:SamePlane,
        vak:HigherPlane,
        vak:LowerPlane .

organon:KosaSystemOfKnowledge
    a organon:AgentTechne ;
    organon:representedBy vak:DomainClassifications ;
    organon:notIdenticalWith organon:ScienceOfLogic .
```
