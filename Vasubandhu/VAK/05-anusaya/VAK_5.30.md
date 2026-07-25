# VAK 5.30

## Sanskrit

स्वकाधरत्रयोर्ध्वैकामलानां रूपधातुजाः ।
आरूप्यजास्त्रिधात्वाप्तत्रयानास्रवगोचराः ॥ ५.३० ॥

## IAST

svakādharatrayordhvaikāmalānāṃ rūpadhātujāḥ |
ārūpyajāstridhātvāptatrayānāsravagocarāḥ || 5.30 ||

## Padaccheda

```text
svaka
adhara-traya
ūrdhva-eka
amalānām
rūpa-dhātu-jāḥ
ārūpya-jāḥ
tri-dhātu-āpta-traya
anāsrava-gocarāḥ
```

Normalized:

```text
svaka-adhara-traya-ūrdhva-eka-amalānāṃ rūpadhātujāḥ |
ārūpyajāḥ tri-dhātu-āpta-traya-anāsrava-gocarāḥ ||
```

## Grammar

- `svaka` — belonging to their own domain.
- `adhara-traya` — the three lower consciousness-categories.
- `ūrdhva-eka` — one consciousness-category belonging to the higher domain.
- `amalānām` — of the undefiled consciousnesses.
- `rūpadhātujāḥ` — those born in the form-domain; nominative masculine plural.
- `ārūpyajāḥ` — those born in the formless-domain; nominative masculine plural.
- `tridhātvāpta` — belonging to or obtained in the three domains.
- `traya` — three consciousness-categories.
- `anāsrava-gocarāḥ` — objects of undefiled consciousness.

The omitted governing term throughout is `vijñāna`: the verse specifies which consciousness-categories can take the indicated afflictions as objects.

## Literal translation

Those born in the form-domain are objects of the three consciousness-categories of their own domain, the three lower ones, one higher one, and the undefiled consciousnesses. Those born in the formless-domain are objects of three consciousness-categories belonging to the three domains and of undefiled consciousness.

## Philosophical translation

Form-domain afflictions can be cognitively reached from below, from within their own domain, from one category above them, and by undefiled cognition. Formless-domain afflictions can be taken as objects by appropriate consciousness from each of the three domains and by undefiled cognition.

## Analysis

Verse 5.29 established that desire-domain afflictions may become objects of several consciousness-categories, including undefiled cognition. Verse 5.30 extends that object-map upward through the form and formless domains.

For afflictions born in the form-domain, the relevant consciousness-categories are:

```text
three of their own domain
three belonging to the lower desire-domain
one belonging to the higher formless-domain
undefiled consciousness
```

Thus form-domain defilements are not cognitively sealed within their own level. They can be taken as objects from below, within, and above.

For afflictions born in the formless-domain, the relevant range is expressed more compactly:

```text
three consciousness-categories
    distributed across the three domains

plus
    undefiled consciousness
```

The important point is not merely the count. The verse maps the admissible reach of cognition across domains.

## Technical vocabulary

```text
rūpadhātujā
    born in the form-domain

ārūpyajā
    born in the formless-domain

adhara
    lower domain

ūrdhva
    higher domain

gocara
    object-range
    what a cognition can take as its object

anāsrava
    undefiled
    free from outflows
```

## Doctrinal determination

The verse distinguishes the domain in which an affliction belongs from the domain in which a cognition capable of knowing it arises.

```text
domain of the object
    ≠
domain of the knowing consciousness
```

A defilement may belong to a higher domain while remaining accessible to cognition arising in a lower one. Conversely, a higher consciousness may take a lower-domain defilement as its object.

Therefore the three domains are not isolated ontological compartments. They are linked by determinate object-relations.

The inclusion of undefiled cognition remains decisive:

```text
contaminated object
    can be known by
undefiled cognition
```

Knowledge of contamination does not require renewed contamination.

## Logical determination

Verse 5.30 constructs a cross-domain accessibility relation.

```text
Cognition
    belongsToDomain
    possessesCategory
    hasObjectRange

Affliction
    belongsToDomain
    isAdmissibleObjectOf
```

The logical relation is not simple containment:

```text
same domain
    is one condition of access

but not
    the universal condition of access
```

The higher and lower domains remain distinguishable, yet cognition can traverse the distinction under specified rules.

This gives a structure of reflective reach:

```text
object situated in domain D
    → cognition from D
    → cognition from lower domain
    → cognition from higher domain
    → undefiled cognition
```

The field is therefore ordered without being cognitively closed.

## Organon note

The architectural result is a distinction between storage location and observation capability.

```text
belongsToDomain
    ≠
canObserveFromDomain
```

For a system, a state may be generated or hosted in one layer while remaining inspectable from another layer.

This suggests separate relations:

```text
hasDomain
isObjectOf
hasAccessTo
hasPurityStatus
```

The verse also protects reflective diagnosis:

```text
observing a contaminated state
    does not imply
sharing its contamination
```

A knowing system must be able to inspect states outside its own current operational layer without collapsing the distinction between observer and observed.

## OWL++ seed

```text
Class: ConsciousnessCategory
Class: Affliction
Class: Domain

Individual: DesireDomain
    Types: Domain

Individual: FormDomain
    Types: Domain

Individual: FormlessDomain
    Types: Domain

ObjectProperty: belongsToDomain
    Domain: Dharma
    Range: Domain

ObjectProperty: isObjectOf
    Domain: Dharma
    Range: ConsciousnessCategory

ObjectProperty: cognizesAcrossDomain
    Domain: ConsciousnessCategory
    Range: Dharma

DataProperty: hasPurityStatus
    Range: {defiled, undefiled}

Rule:
    Affliction(?x)
    belongsToDomain(?x, FormDomain)
    ConsciousnessCategory(?c)
    permitsFormDomainObject(?c, true)
    -> isObjectOf(?x, ?c)

Rule:
    Affliction(?x)
    ConsciousnessCategory(?c)
    hasPurityStatus(?c, undefiled)
    permitsAfflictionAsObject(?c, true)
    -> isObjectOf(?x, ?c)
```

## Bhāṣya questions

1. What exactly are the three consciousness-categories designated for the form-domain afflictions in their own and lower domains?
2. Which single higher consciousness-category is indicated by `ūrdhvaika`?
3. How does the Bhāṣya distribute the three consciousness-categories for formless-domain afflictions across the three domains?
4. Why can lower-domain cognition take higher-domain afflictions as objects?
5. Does the Bhāṣya distinguish mere object-access from the capacity to abandon the affliction known?

## Commit

```text
Add VAK 5.30 analysis
```
