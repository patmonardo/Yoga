# VAK 5.27

## Sanskrit

किं विघ्नं तत्कथं नान्यदध्वयोगस्तथा सतः ।
अजातनष्टता केन गम्भीरा खलु धर्मता ॥ ५.२७ ॥

## IAST

kiṃ vighnaṃ tat kathaṃ nānyad adhvāyogas tathā sataḥ |
ajātanaṣṭatā kena gambhīrā khalu dharmatā || 5.27 ||

## Padaccheda

```text
kim
vighnam
tat
katham
na
anyat
adhva-yogaḥ
tathā
sataḥ
ajāta-naṣṭatā
kena
gambhīrā
khalu
dharmatā
```

Normalized:

```text
kiṃ vighnaṃ tat kathaṃ na anyat adhvayogaḥ tathā sataḥ |
ajāta-naṣṭatā kena gambhīrā khalu dharmatā ||
```

## Grammar

- `kim` — interrogative nominative or accusative neuter singular: what?
- `vighnam` — obstacle, impediment, blocking condition.
- `tat` — that; referring to the dharma or its operative function under discussion.
- `katham` — how?
- `na anyat` — not another; how does it not become something numerically or specifically different?
- `adhvayogaḥ` — conjunction or assignment to a temporal course (`adhvan`): past, present, or future.
- `tathā sataḥ` — while existing in that manner; of that which exists thus.
- `ajāta-naṣṭatā` — the condition of being unborn and destroyed, or the predicates “not yet arisen” and “ceased.”
- `kena` — by what? through what ground?
- `gambhīrā` — profound, difficult to penetrate.
- `khalu` — indeed, certainly.
- `dharmatā` — the nature, law, or suchness of dharmas.

## Literal translation

What is the obstacle [to its operation]? How then is it not another? How does that which exists thus become connected with a temporal course? By what [ground] does it possess the condition of being unborn and destroyed? Indeed, the nature of dharmas is profound.

## Philosophical translation

If a dharma exists across all three times, what prevents it from operating continuously? If its operative state changes, how does it remain the same dharma rather than becoming another? How can an always-existent dharma genuinely belong to past, present, or future, and in what sense can it still be called not yet arisen or already destroyed? The structure of dharma is indeed profound.

## Analysis

Verse 5.26 preferred the `avasthānyathika` theory:

```text
same dharma
    different temporal state
        according to kāritra
```

Verse 5.27 immediately subjects that account to four objections.

### 1. What blocks operation?

If the dharma exists in the future and past as well as the present, why is its `kāritra` not continuously active?

```text
existence in all times
    does not yet explain
restriction of operation to one time
```

The theory therefore requires a real distinction between:

```text
being present in the ontological inventory
and
being presently efficacious
```

### 2. How does it not become another?

If a dharma changes from non-operating to operating and then to no-longer-operating, how is it still one dharma?

```text
change of state
    threatens
identity of bearer
```

The theory must preserve identity without reducing temporal difference to mere verbal relabeling.

### 3. How is temporal assignment possible?

If the dharma exists equally in all three times, what makes it future, present, or past?

```text
tri-temporal existence
    requires
non-arbitrary temporal indexing
```

The prior answer was `kāritra`, but the present verse asks whether that criterion is sufficient.

### 4. How can it be unborn and destroyed?

A future dharma is called `ajāta`, not yet arisen. A past dharma is called `naṣṭa`, destroyed or ceased. But if both still exist, what do these predicates mean?

```text
ajāta
    cannot mean absolute nonbeing

naṣṭa
    cannot mean absolute nonbeing
```

They must instead describe modes of efficacy or manifestation.

## Technical vocabulary

```text
vighna
    obstacle
    condition preventing operation

adhvayoga
    assignment to a temporal course
    relation to past, present, or future

ajāta
    not yet arisen
    existent without present operation

naṣṭa
    ceased or destroyed
    existent without continuing present operation

dharmatā
    the law or nature of dharmas
    the profound structure by which identity,
    temporality, and efficacy coexist
```

## Doctrinal determination

Verse 5.27 does not yet abandon Sarvāstivāda. It exposes the burden carried by the preferred theory.

The doctrine must jointly maintain:

```text
1. dharma identity
2. existence across three times
3. temporal difference
4. restricted operation
5. meaningful arising and cessation
```

The tension can be represented as:

```text
sarvakālāstitā
    all-time existence

kāritra-niyama
    time-specific operation

ajāta / naṣṭa
    non-arisen / ceased predicates
```

No one of these may erase the others.

The closing statement—`gambhīrā khalu dharmatā`—acknowledges that the law of dharmas exceeds a simple substantialist model. A dharma is neither an inert thing persisting unchanged nor an absolute nonentity outside the present.

## Logical determination

Verse 5.27 converts the preferred theory into a problem of identity through difference.

```text
same determination
    across distinct states
```

The required logical structure is:

```text
identity
    not identity without difference

state-difference
    not production of another entity
```

This is the exact point where a practical theory of efficacy becomes a theory of temporal identity.

The verse tests whether the following distinction can hold:

```text
DharmaIdentity
    invariant

OperationalState
    variant
```

But it also asks what mediates the two. A merely external state label would be insufficient. The state must belong intrinsically to the dharma without exhausting its identity.

The four questions correspond to four architectural failure modes:

```text
No operation constraint
    -> everything operates always

No identity constraint
    -> each state becomes another entity

No temporal criterion
    -> past, present, future become arbitrary labels

No modal account
    -> arising and cessation collapse into contradiction
```

## Organon note

For the Platform, this verse demands a richer state model than a timestamped object.

```text
Entity identity
    must persist across state transitions

Capability
    must not equal current activation

Temporal classification
    must be derived from operational status

Arising and cessation
    must describe state transitions,
    not creation from or collapse into absolute nothing
```

A minimal architecture would distinguish:

```text
existsAsDharma
hasOperationalState
hasTemporalMode
hasActivationCondition
hasCessationStatus
```

The profound point is that power can be real without being presently exercised.

```text
Power
    ≠ current operation

Current operation
    = power under determinate conditions
```

This directly supports the emerging practical theory: knowledge of a dharma includes knowledge of what prevents, enables, and terminates its efficacy.

## OWL++ seed

```text
Class: Dharma

Class: TemporalMode
    Individuals: Past, Present, Future

Class: OperationalState
    Individuals: NotYetOperating, Operating, NoLongerOperating

ObjectProperty: hasTemporalMode
    Domain: Dharma
    Range: TemporalMode

ObjectProperty: hasOperationalState
    Domain: Dharma
    Range: OperationalState

ObjectProperty: blockedBy
    Domain: Dharma
    Range: Condition

DataProperty: retainsIdentityAcrossState
    Domain: Dharma
    Range: xsd:boolean

Rule:
    Dharma(?x)
    hasOperationalState(?x, Operating)
    -> hasTemporalMode(?x, Present)

Rule:
    Dharma(?x)
    hasOperationalState(?x, NotYetOperating)
    -> hasTemporalMode(?x, Future)

Rule:
    Dharma(?x)
    hasOperationalState(?x, NoLongerOperating)
    -> hasTemporalMode(?x, Past)
```

## Bhāṣya questions

1. What exact `vighna` prevents the future or past dharma from exercising present `kāritra`?
2. How does the Bhāṣya answer the identity objection expressed by `tat kathaṃ nānyat`?
3. Is `adhvayoga` explained solely through `kāritra`, or through additional temporal characteristics?
4. How are `ajāta` and `naṣṭa` defined without reducing future and past dharmas to nonexistence?
5. Is `gambhīrā khalu dharmatā` Vasubandhu's acceptance of doctrinal profundity, an ironic suspension, or both?

## Commit

```text
Add VAK 5.27 analysis
```
