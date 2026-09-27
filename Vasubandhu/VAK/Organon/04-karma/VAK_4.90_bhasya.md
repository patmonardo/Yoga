# VAK 4.90 Bhāṣya — The Temporal Result Matrix

## 1. Kārikā Anchor

```iast
sarve 'tītasya catvāri madhyamasyāpy anāgatāḥ /
madhyamā dve 'jātasya phalāni trīṇy anāgatāḥ // 4.90 //
```

> For past action, dharmas of all three times are four results. For present
> action, future dharmas are also four; present dharmas are two. For future
> action, future dharmas are three results.

The verse rotates the causal matrix again. After classifying action and result
by ethical quality, it now indexes both sides of the result relation by time.

## 2. Continuous Sanskrit

```iast
sarve 'tītasya catvāri

sarva iti traiyadhvikāḥ. atītasya karmaṇas traiyadhvikā dharmāś catvāri
phalāni, visaṃyogaphalaṃ hitvā.

madhyamasyāpy anāgatāḥ /

pratyutpannasyāpi karmaṇo 'nāgatā dharmāś catvāri phalāny etāny eva.

madhyamā dve

pratyutpannā dharmāḥ pratyutpannasya dve, puruṣakārādhipatiphale.

ajātasya phalāni trīṇy anāgatāḥ // 4.90 //

anāgatasyānāgatāni trīṇi phalāni, niṣyandavisaṃyogaphale hitvā.
```

The witness reads `phalaṃ` at `[256|20]`, `catvāti` at `[256|22]`,
`pratyupannasya` at `[256|24]`, and `triṇy` at `[256|25]`. These are
normalized above according to the immediately explicit syntax.

## 3. Continuous Conventional Translation

For past action, dharmas of all three times stand as four results. “All” means
belonging to the three times. Past, present, and future dharmas can be results
of past action under four result relations, with the disconnection result
excluded.

For present action, future dharmas also stand as these same four results.

Present dharmas stand as two results of present action: the activity-produced
and dominant results.

For future action, future dharmas stand as three results, with the
corresponding and disconnection results excluded.

## 4. Resolution of the Compressed Syntax

The research kārikā alone permits a misleading reading:

```text
sarve 'tītasya
    “all five results belong to past action”
```

The Bhāṣya rules this out. `Sarve` refers to the temporal classes of the
result-dharmas:

```text
past dharmas
present dharmas
future dharmas
```

Each class can stand as a result of past action through four relations. The
excluded fifth is disconnection.

Likewise, `madhyamā dve` does not mean “the middle two members” of the
five-result list. It means that **present dharmas** stand as two results of
**present action**.

## 5. The Completed Temporal Matrix

The verse establishes the following nonempty cells:

| Time of action | Time of result-dharma | Number | Result relations |
|---|---|---:|---|
| past | past | 4 | maturation, correspondence, activity-produced, dominant |
| past | present | 4 | maturation, correspondence, activity-produced, dominant |
| past | future | 4 | maturation, correspondence, activity-produced, dominant |
| present | present | 2 | activity-produced, dominant |
| present | future | 4 | maturation, correspondence, activity-produced, dominant |
| future | future | 3 | maturation, activity-produced, dominant |

The unstated reverse-time cells remain empty:

```text
present action → past result
future action  → present or past result
```

An action cannot produce as its result a dharma whose occurrence is already
behind that action.

## 6. Why Disconnection Is Absent

Every cell in this verse excludes `visaṃyogaphala`. Disconnection is an
unconditioned result and therefore is not classified as past, present, or
future in the manner of conditioned dharmas.

The temporal matrix ranges over `traiyadhvika` dharmas, dharmas belonging to
the three times. Disconnection does not enter those temporal columns. Its
absence follows from the coordinate system of the question, rather than from
a claim that no action ever produces disconnection.

## 7. Why the Present Has Only Two Present Results

A presently arising action and presently arising result coexist only under
two relations:

```text
puruṣakāraphala — result directly produced by the activity
adhipatiphala   — result conditioned through dominance
```

Maturation and correspondence require temporal succession; the result cannot
already be present as the maturation or later similar outflow of the action
that is itself presently arising.

The present therefore has immediate efficacy without completed karmic return:

```text
present action
    → concurrent production and conditioning
    → future maturation and correspondence
```

## 8. Why Future Action Has Three Future Results

Future action and future result-dharmas can be related through maturation,
activity-production, and dominance. Correspondence is excluded because an
outflow result must follow an already arisen similar cause. Disconnection is
excluded for the nontemporal reason already given.

The future cell represents causal capacity, not a completed occurrence:

```text
future action + future result
    = admissible future causal relation
    ≠ presently executed causation
```

This is specifically intelligible within the Sarvāstivāda temporal framework,
where future dharmas can be classified by causal function without being
presently active.

## 9. Organon Contact Point

The Causal Algebra for Agency now requires temporal typing on both ends of
every result edge:

```text
ActionResultEdge {
    action
    actionTime
    resultDharma
    resultTime
    resultType
}
```

The validity rule depends on the entire triple:

```text
Allowed(actionTime, resultTime, resultType)
```

It cannot be reduced to `actionTime ≤ resultTime`, because present-to-present
relations admit only two result types, while present-to-future admits four.
Temporal order is necessary, but the causal modality supplies the fuller
constraint.

This is the Organon reconstruction. The three-time ontology and exact temporal
memberships remain the Abhidharma doctrine of the source.

## 10. Review Status

The complete 4.90 unit `[256|18]–[257|01]` is included. It resolves `sarve`
and `madhyamā`, constructs the complete nonempty temporal matrix, and records
the precise omitted result types. It stops before 4.91 changes the coordinate
from time to domain and training status at `[257|02]`. Witness irregularities
are marked explicitly.
