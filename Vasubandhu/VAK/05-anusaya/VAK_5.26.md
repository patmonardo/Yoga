# VAK 5.26

## Sanskrit

ते भावलक्षणावस्थान्यथान्यथिकसंज्ञिताः ।
तृतीयः शोभनोऽध्वानः कारित्रेण व्यवस्थिताः ॥ ५.२६ ॥

## IAST

te bhāvalakṣaṇāvasthānyathānyathikasaṃjñitāḥ |
tṛtīyaḥ śobhano 'dhvānaḥ kāritreṇa vyavasthitāḥ || 5.26 ||

## Padaccheda

```text
te
bhāva-anyathika
lakṣaṇa-anyathika
avasthā-anyathika
anyathā-anyathika
saṃjñitāḥ
tṛtīyaḥ
śobhanaḥ
adhvānaḥ
kāritreṇa
vyavasthitāḥ
```

Normalized:

```text
te bhāvānyathika-lakṣaṇānyathika-avasthānyathika-anyathānyathika-saṃjñitāḥ |
tṛtīyaḥ śobhanaḥ; adhvānaḥ kāritreṇa vyavasthitāḥ ||
```

## Grammar

- `te` — nominative masculine plural: those; referring to the four Sarvāstivāda positions announced in 5.25.
- `bhāva-anyathika` — one who posits difference or alteration in mode of being.
- `lakṣaṇa-anyathika` — one who posits difference in characteristic.
- `avasthā-anyathika` — one who posits difference in state or condition.
- `anyathā-anyathika` — one who posits difference through relative otherness, that is, difference according to relation.
- `saṃjñitāḥ` — named, designated, termed.
- `tṛtīyaḥ` — the third.
- `śobhanaḥ` — good, excellent, preferable.
- `adhvānaḥ` — nominative plural from `adhvan`: temporal courses or periods, namely past, present, and future.
- `kāritreṇa` — instrumental singular: by operative activity, function, or causal efficacy.
- `vyavasthitāḥ` — determined, established, fixed in distinction.

## Literal translation

They are designated as the proponents of alteration in mode of being, alteration in characteristic, alteration in state, and alteration through relative otherness. The third is good: the temporal courses are determined by operative activity.

## Philosophical translation

The four Sarvāstivāda accounts distinguish temporal difference respectively through change of mode, characteristic, state, and relation. Of these, the third account is preferable, because past, present, and future are established through the functional condition of a dharma—whether its operative efficacy has not yet occurred, is occurring, or has ceased.

## Analysis

Verse 5.25 established the common Sarvāstivāda commitment:

```text
all dharmas exist across the three times
```

Verse 5.26 asks how temporal difference is possible if the dharma remains existent.

The four answers are:

```text
bhāvānyathika
    difference in mode of being

lakṣaṇānyathika
    difference in characteristic

avasthānyathika
    difference in state

anyathānyathika
    difference through relation to what is before and after
```

The kārikā does not yet unfold the examples or attribute the theories to individual masters. It does, however, make a judgment:

```text
tṛtīyaḥ śobhanaḥ
    the third is preferable
```

The preferred account is `avasthānyathatva`, difference of state.

Its criterion is `kāritra`, operative function:

```text
future
    kāritra has not yet been exercised

present
    kāritra is being exercised

past
    kāritra has already been exercised
```

The dharma is therefore distinguished temporally not by losing its identity, but by entering a different functional state.

## Technical vocabulary

```text
bhāva
    mode of being
    manner in which a dharma exists

lakṣaṇa
    characteristic
    mark through which a temporal determination is identified

avasthā
    state
    determinate functional condition

anyathānyathatva
    relative otherness
    temporal designation through relation to preceding and succeeding moments

adhvan
    temporal course
    past, present, or future

kāritra
    operative activity
    function or causal efficacy exercised by a dharma
```

## Doctrinal determination

The verse preserves two claims together:

```text
identity across time
    the dharma remains the same dharma

difference across time
    its temporal state differs
```

The third theory is preferred because it locates difference in operation rather than in substance:

```text
dravya or svabhāva
    remains identifiable

avasthā
    changes according to kāritra
```

This gives a functional account of temporality:

```text
time is known through the status of efficacy
```

The verse does not merely assign dates to dharmas. It defines temporal determination through what a dharma can presently do.

## Logical determination

Verse 5.26 moves from temporal existence to temporal specification:

```text
5.25
    dharmas exist across all times

5.26
    temporal difference must still be determined
```

The four positions propose four possible loci of difference:

```text
mode
mark
state
relation
```

The chosen solution places the difference in `avasthā`, and determines that state through `kāritra`.

Thus:

```text
existence
    ≠
operation
```

and:

```text
same determination
    can possess different functional states
```

The decisive structure is:

```text
Dharma
    retains identity
        while
    Kāritra-status changes
        thereby
    TemporalState is determined
```

This is a movement from ontology to executable state.

## Organon note

The verse gives the Platform a direct rule:

```text
TemporalState
    must be inferred from
OperationalStatus
```

A determination should not be classified as past, present, or future solely from an external timestamp. Its temporal mode is tied to its efficacy:

```text
NotYetOperative
    → Future

CurrentlyOperative
    → Present

NoLongerOperative
    → Past
```

This sharply separates:

```text
hasExistenceStatus
hasOperationalStatus
hasTemporalState
```

The same dharma may remain ontologically available while changing its operational state. This is exactly the distinction needed for latent powers, deferred effects, persistent traces, and previously exercised functions.

## OWL++ seed

```text
Class: TemporalTheory

Class: BhavanyathikaTheory
    SubClassOf: TemporalTheory

Class: LaksananyathikaTheory
    SubClassOf: TemporalTheory

Class: AvasthanyathikaTheory
    SubClassOf: TemporalTheory

Class: AnyathanyathikaTheory
    SubClassOf: TemporalTheory

Class: OperationalStatus

Individual: NotYetOperative
    Types: OperationalStatus

Individual: CurrentlyOperative
    Types: OperationalStatus

Individual: NoLongerOperative
    Types: OperationalStatus

ObjectProperty: hasOperationalStatus
    Domain: Dharma
    Range: OperationalStatus

ObjectProperty: hasTemporalState
    Domain: Dharma
    Range: TemporalState

Rule:
    Dharma(?x)
    hasOperationalStatus(?x, NotYetOperative)
    -> hasTemporalState(?x, Future)

Rule:
    Dharma(?x)
    hasOperationalStatus(?x, CurrentlyOperative)
    -> hasTemporalState(?x, Present)

Rule:
    Dharma(?x)
    hasOperationalStatus(?x, NoLongerOperative)
    -> hasTemporalState(?x, Past)
```

## Bhāṣya questions

1. Which four masters are associated with the four theories, and how exactly are their positions formulated?
2. What examples are used to explain `bhāvānyathatva`, `lakṣaṇānyathatva`, `avasthānyathatva`, and `anyathānyathatva`?
3. Why is the third theory judged `śobhana` rather than simply true?
4. Does `kāritra` mean causal efficacy generally, the production of a result, or a more specific present operation?
5. How does the Bhāṣya preserve dharma-identity while preventing the three temporal states from collapsing into one another?

## Commit

```text
Add VAK 5.26 analysis
```
