# VAK 4.92 Bhāṣya — Completion of the Training-status Matrix

## 1. Kārikā Anchor

```iast
dharmāḥ śaikṣādikā ekaṃ phalaṃ trīṇy api ca dvayam /
tābhyām anyasya śaikṣādyā dve dve pañca phalāni ca // 4.92 //
```

> For adept action, dharmas beginning with the trainee class are respectively
> one result, three, and two. For action belonging to neither of those two,
> dharmas beginning with the trainee class are respectively two, two, and all
> five results.

The opening words complete the `aśaikṣa` construction left suspended at the
end of 4.91. The second half then supplies the final row of the matrix.

## 2. Continuous Sanskrit

```iast
dharmāḥ śaikṣādikā ekaṃ phalaṃ trīṇy api ca dvayam /

aśaikṣasya karmaṇaḥ śaikṣā dharmā ekam adhipatiphalam; aśaikṣās trīṇi,
vipākavisaṃyogaphale hitvā; naivaśaikṣānāśaikṣā dve,
puruṣakārādhipatiphale.

tābhyām anyasya śaikṣādyā dve dve pañca phalāni ca // 4.92 //

śaikṣāśaikṣābhyām anyasya karmaṇo naivaśaikṣānāśaikṣasya śaikṣā
dharmā dve, puruṣakārādhipatiphale. aśaikṣā apy evam.
naivaśaikṣānāśaikṣāḥ pañca phalāni.
```

The unit is textually stable. The continuous Sanskrit opens compounds and
sandhi while preserving the source's ordered classes: trainee, adept, and
neither trainee nor adept.

## 3. Continuous Conventional Translation

For action belonging to an adept, trainee dharmas stand as one result: the
dominant result. Adept dharmas stand as three results, with maturation and
disconnection excluded. Dharmas belonging to neither trainee nor adept stand
as two results: the activity-produced and dominant results.

For action belonging to neither trainee nor adept, trainee dharmas stand as
two results: the activity-produced and dominant results. Adept dharmas are
related in the same way. Dharmas belonging to neither status stand as all
five results.

## 4. The Adept-action Row

The action of one beyond training has the profile:

| Result-dharma status | Number | Included relations |
|---|---:|---|
| trainee | 1 | dominant |
| adept | 3 | corresponding, activity-produced, dominant |
| neither | 2 | activity-produced, dominant |

The first cell is striking. Adept action does not produce trainee dharmas as
its corresponding continuation, because completion of training does not
regress genetically into the trainee Path. It can nevertheless stand as a
dominant condition for trainee dharmas.

The adept-to-adept cell retains correspondence: completed training can
continue through dharmas of its own status. The neither-status cell lacks
that same-status Path correspondence but remains open to direct production
and dominance.

## 5. The Neither-status Row

Action belonging to neither trainee nor adept yields:

| Result-dharma status | Number | Included relations |
|---|---:|---|
| trainee | 2 | activity-produced, dominant |
| adept | 2 | activity-produced, dominant |
| neither | 5 | maturation, correspondence, disconnection, activity-produced, dominant |

The two cross-status cells show that ordinary action can support or produce
Path dharmas without itself possessing a Path status. Its relation to Path
results is limited to production and dominance.

Within its own neither-status field, however, the complete fivefold result
range is available. This broad class includes the contaminated and ordinary
processes capable of maturation and correspondence, while also admitting an
action that produces disconnection.

## 6. The Complete Directed Matrix

Combining 4.91 and 4.92 gives:

| Action status ↓ / Result status → | Trainee | Adept | Neither |
|---|---|---|---|
| trainee | N, P, A | N, P, A | V, P, A |
| adept | A | N, P, A | P, A |
| neither | P, A | P, A | M, N, V, P, A |

where:

```text
M = maturation       (vipāka)
N = correspondence   (niṣyanda)
V = disconnection    (visaṃyoga)
P = activity-produced (puruṣakāra)
A = dominant         (adhipati)
```

This table displays the exact membership concealed by the count matrix:

```text
trainee: 3, 3, 3
adept:   1, 3, 2
neither: 2, 2, 5
```

## 7. Path Directionality

The matrix is not symmetric:

```text
trainee action → adept result
    correspondence + production + dominance

adept action → trainee result
    dominance only
```

This is the causal signature of an irreversible developmental order. The
trainee can generate a continuation culminating in adept dharmas. Adept
action does not generate a corresponding return to training, although it can
support trainees as a dominant condition.

The Path is therefore represented as directed transformation rather than a
mere partition into social or psychological classes.

## 8. Why Neither-status Action Can Have Disconnection

“Neither” does not mean incapable of entering the Path's causal field. It is
a classification of the action itself, not a blanket denial of liberating
effect. The all-five cell shows that a neither-status action can stand in the
disconnection relation to a neither-status result under the relevant cases.

Similarly, the trainee-to-neither cell includes disconnection even though
correspondence is absent. The result ontology classifies the precise causal
aspect; training status alone does not dictate it without the ordered source
and target relation.

## 9. Organon Contact Point

The completed table is an executable transition policy:

```text
AllowedResultTypes(
    action.trainingStatus,
    result.trainingStatus
) -> Set<ResultType>
```

It also gives the Agent architecture a nonregression rule:

```text
Correspondence(Adept, Trainee) = false
Correspondence(Trainee, Adept) = true
```

An adept process may govern, enable, or condition training processes without
becoming their developmental predecessor. Conversely, a trainee process can
have an adept successor as its genetic continuation.

The executable framing is the Organon reconstruction. The training statuses
and exact result memberships belong to the source.

## 10. Review Status

The complete 4.92 unit `[257|11]–[257|16]` is included. It completes the
adept row, supplies the neither-status row, and reconstructs the entire
directed three-by-three training-status matrix from 4.91–4.92. It stops
before 4.93 changes the coordinate to mode of abandonment at `[257|17]`.
