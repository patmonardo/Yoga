# VAK_1.35

## 1. Sanskrit (Devanāgarī)

> स्प्रष्टव्यं द्विविधं शेषा रूपिणो नव भौतिकाः ।
>
> धर्मधात्वेकदेशश्च सञ्चिता दश रूपिणः ॥ १.३५ ॥

## 2. Sanskrit (IAST)

> spraṣṭavyaṃ dvividhaṃ śeṣā rūpiṇo nava bhautikāḥ /
>
> dharmadhātvekadeśaś ca saṃcitā daśa rūpiṇaḥ // 1.35 //

## 3. Lexical Analysis

```text
spraṣṭavyam             → spraṣṭavyam
dvividham               → dvi-vidham
rūpiṇaḥ                 → rūpiṇaḥ
bhautikāḥ               → bhautikāḥ
dharmadhātvekadeśaḥ     → dharma-dhātu-eka-deśaḥ
saṃcitāḥ                → sam-√ci + kta
```

| Form | Morphology | Lexical force here |
|---|---|---|
| spraṣṭavyam | nominative neuter singular | tangible object-Domain |
| dvi-vidham | nominative neuter singular compound | twofold in constitution |
| śeṣāḥ | nominative masculine plural | the other material Domains apart from the tangible |
| rūpiṇaḥ | nominative masculine plural adjective | material, form-bearing |
| nava | numeral | five faculties and four non-tangible sensory objects |
| bhautikāḥ | nominative masculine plural adjective | derivative-material; dependent upon the great elements |
| dharma-dhātu-eka-deśaḥ | nominative masculine singular compound | one portion of the Dharma-domain |
| ca | conjunction | and; adds avijñapti to what is derivative-material |
| saṃcitāḥ | nominative masculine plural participial adjective | accumulated; atomically aggregated |
| daśa rūpiṇaḥ | nominative masculine plural | the ten material faculty-and-object Domains |

The portion of the Dharma-domain is grammatically added to the derivative-
material classification. The Bhāṣya identifies it as `avijñapti`. It is not
added to the subsequent count of ten atomically accumulated Domains.

## 4. Grammar

The first predicate divides the tangible Domain:

```text
spraṣṭavyaṃ dvividham
    the tangible is twofold

    four great elements
    + seven derivative tangible qualities beginning with smoothness
```

The remaining nine material Domains are derivative-material:

```text
five sensory faculty-Domains
    eye, ear, nose, tongue, body

four non-tangible object-Domains
    visible form, sound, smell, taste
```

`Bhautika` is explicitly explained by `bhūteṣu bhavatvāt`: it exists in
dependence upon the great elements. Dependence does not mean identity.

The conjunction in `dharmadhātvekadeśaś ca` continues this predicate:

```text
one portion of the Dharma-domain
    = avijñapti
    = derivative-material
```

The final clause begins a separate question and predicate:

```text
saṃcitā daśa rūpiṇaḥ
    the ten material Domains are accumulated
```

The Bhāṣya defines `saṃcita` strictly as constitution by aggregates of atoms
(`paramāṇu-saṃghāta`). Avijñapti is material and derivative-material, but it
is not one of these ten atomic aggregates.

## 5. Translation

### Close syntactic construe

> The tangible Domain is twofold. The remaining nine material Domains are derivative-material, as is one portion of the Dharma-domain. The ten material Domains are accumulated.

### Bhāṣya-informed translation

> The tangible Domain comprises both the four great elements and seven derivative tangible qualities. The other nine material Domains are entirely derivative from the great elements, and avijñapti—the material portion of the Dharma-domain—is derivative-material as well. The five material faculties and five material objects are accumulated, meaning that they are constituted as atomic aggregates.

The expanded translation keeps avijñapti within derivative materiality while
excluding it from the atomic meaning of `saṃcita`.

## 6. Philosophical Translation

> Materiality has distinct genetic and constitutional determinations. The great elements are directly tangible bases. The faculties, sensory qualities, and avijñapti depend upon those bases without being identical with them. Atomic accumulation characterizes the ten ordinary material Domains, but not every derivative-material determination. Material dependence is therefore wider than atomic embodiment.

Organon rendering:

> The Smart Domain now receives a material-construction type. The system distinguishes basis, derivation, and aggregation. A derivative inherits material dependence from the great elements while preserving its own mode of apprehension and operation. Avijñapti is the decisive boundary case: Dharma-controlled material efficacy without atomic accumulation as an ordinary sensory Domain.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| spraṣṭavya-dhātu | tangible Domain | contains the four great elements and seven derivative tangible qualities |
| mahābhūta | great element | elemental tangible basis characterized by hardness and the other primary qualities |
| bhūta-svabhāva | having elemental nature | applies to the four great elements within the tangible Domain |
| bhautika | derivative-material | exists in dependence upon the great elements without being identical with them |
| bhūteṣu bhavatva | existence in dependence upon the elements | Bhāṣya's explanation of `bhautika` |
| rūpin | material / form-bearing | wider material classification |
| dharmadhātvekadeśa | portion of the Dharma-domain | avijñapti as subtle derivative-material determination |
| avijñapti | non-disclosive form | material Dharma not manifest as ordinary sensory disclosure |
| saṃcita | atomically accumulated | constituted as an aggregate of atoms |
| paramāṇu-saṃghāta | atomic aggregate | strict Bhāṣya definition of accumulated materiality |
| ślakṣṇatva | smoothness | first-listed derivative tangible quality |

The three principal predicates must remain distinct:

```text
material
derivative-material
atomically accumulated
```

## 8. Logical Determination

The tangible Domain is internally divided:

```text
SprastavyaDhatu
    = FourGreatElements
      ∪ SevenDerivativeTangibleQualities
```

The derivative-material set is:

```text
Bhautika
    = FiveSenseFacultyDomains
      ∪ FourNonTangibleSensoryObjectDomains
      ∪ SevenDerivativeTangibleQualities
      ∪ Avijnapti
```

The accumulated set is narrower:

```text
SamcitaDomains
    = FiveSenseFacultyDomains
      ∪ FiveSensoryObjectDomains

Samcita(x)
    ↔ ConstitutedAs(x, AtomicAggregate)
```

The dependency rule is:

```text
Bhautika(x)
    → DependsOn(x, GreatElements)

DependsOn(x, GreatElements)
    ↛ IdenticalWith(x, GreatElements)
```

Avijñapti exposes the non-equivalence of predicates:

```text
Avijnapti
    → Material
    ∧ Bhautika
    ∧ ¬SamcitaDomain
```

Therefore:

```text
Samcita(x) → Material(x)

Material(x) ↛ Samcita(x)

Bhautika(x) ↛ Samcita(x)
```

The Smart-Domain material type has three layers:

```text
MaterialBasis
    → DerivativeMaterialDependency
    → OptionalAtomicAggregation
```

## 9. Interpretive Note

VAK 1.35 moves from the living incorporation of matter to its constitution.
The tangible Domain is unique because it includes both the great elements
themselves and derivative tangible qualities. The elemental characteristics
are apprehended through touch; visible form and the other sensory qualities
are apprehended through their own faculties. This differentiated access is
one reason the entire material field cannot be reduced to the great elements.

The Bhāṣya attributes precisely that reduction to Buddhadeva:

```text
ten material Spheres
    = nothing but the great elements
```

Vasubandhu rejects it. The sūtra fixes four great elements and says that the
faculties and other material objects arise in dependence upon them. The
relation is genetic dependence, not numerical or conceptual identity:

```text
derived from
    ≠
identical with
```

This directly sharpens our earlier discussion of elemental and derived
matter. Primal material conditions do not exhaust the determinations that
depend upon them. Faculty, quality, and non-disclosive efficacy have their
own Domain status even while inheriting material dependence from the great
elements.

Avijñapti is again the potent boundary case. It belongs to the Dharma-domain
and depends materially upon the great elements, yet it is not one of the ten
atomically accumulated sensory-material Domains. This gives textual
discipline to our Organon phrase “Dharma-controlled reality”:

```text
avijñapti
    = derivative-material efficacy
    + Dharma-domain membership
    − ordinary sensory disclosure
    − atomic Domain-aggregation
```

The last two negations should prevent us from turning avijñapti into either
gross matter or a merely mental fiction. Its exact later Vārttika role must
remain answerable to these Kośa constraints.

For the Smart Domain SDK, 1.35 supplies the material constructor:

```text
constructor inputs:
    elemental dependency
    mode of apprehension
    atomic aggregation status

constructor output:
    determinate material Domain
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_35
    a vak:Karika ;
    rdfs:label "VAK 1.35" ;
    vak:hasTopic vak:MaterialConstructionTypes ;
    vak:belongsTo vak:Dhatunirdesa .

vak:SprastavyaDhatu
    a vak:MaterialDomain ;
    vak:contains vak:FourGreatElements,
        vak:SevenDerivativeTangibleQualities .

vak:Bhautika
    a vak:DerivativeMaterialType ;
    vak:dependsOn vak:FourGreatElements ;
    vak:distinctFrom vak:ElementalIdentity .

vak:TenMaterialDomains
    a vak:DomainSet ;
    vak:hasConstitution vak:AtomicAggregation .

vak:Avijnapti
    a vak:MaterialDharma,
        vak:Bhautika ;
    vak:partOf vak:DharmaDhatu ;
    vak:notMemberOf vak:TenAtomicallyAccumulatedDomains .

organon:MaterialDomainConstructor
    a vak:SmartDomainCapability ;
    organon:requiresParameter vak:ElementalDependency,
        vak:ApprehensionMode,
        vak:AggregationStatus .
```
