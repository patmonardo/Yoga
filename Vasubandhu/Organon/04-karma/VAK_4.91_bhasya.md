# VAK 4.91 Bhāṣya — Ground and Training-status Result Matrices

## 1. Kārikā Anchor

```iast
svabhūmidharmāś catvāri trīṇi dve vānyabhūmikāḥ /
śaikṣasya trīṇi śaikṣādyā aśaikṣasya tu karmaṇaḥ // 4.91 //
```

> Dharmas of the same ground are four results; those of another ground are
> three or two. For trainee action, dharmas beginning with the trainee class
> are three; but for the action of an adept—

The final construction is intentionally incomplete. The first row of the
training-status matrix is explained here; the verse then opens the adept row,
whose numbers occur in 4.92.

## 2. Continuous Sanskrit

```iast
svabhūmidharmāś catvāri

svabhūmikasya karmaṇaḥ svabhūmikā dharmāś catvāri phalāni,
visaṃyogaphalaṃ hitvā.

trīṇi dve vānyabhūmikāḥ /

anyabhūmikā dharmā anāsravāś cet trīṇi phalāni,
vipākavisaṃyogaphale hitvā, dhātvapatitatvāt; sāsravāś cet dve,
puruṣakārādhipatiphale.

śaikṣasya trīṇi śaikṣādyāḥ

śaikṣasya karmaṇaḥ śaikṣā dharmās trīṇi phalāni,
vipākavisaṃyogaphale hitvā. aśaikṣā apy evam.
naivaśaikṣānāśaikṣā api vipākaniṣyandaphale hitvā.

aśaikṣasya tu karmaṇaḥ // 4.91 //
```

The running witness presents no major lacuna in this unit. Compounds and
sandhi have been opened, and the phrase `dhātvapatitatvāt` has been retained
without reducing `dhātu` and `bhūmi` to one undifferentiated spatial notion.

## 3. Continuous Conventional Translation

Dharmas belonging to the same ground as the action stand as four results,
with the disconnection result excluded.

Dharmas belonging to another ground stand as three or two results. If those
other-ground dharmas are uncontaminated, they stand as three results, with
maturation and disconnection excluded, because uncontaminated dharmas do not
fall within a realm. If they are contaminated, they stand as two results:
the activity-produced and dominant results.

For the action of a trainee, dharmas belonging to a trainee stand as three
results, with maturation and disconnection excluded. Dharmas belonging to an
adept are related in the same way. Dharmas belonging to neither trainee nor
adept also stand as three results, but here maturation and correspondence are
excluded.

As for the action of an adept—the classification continues in the next verse.

## 4. The Same-ground Profile

When action and result-dharma belong to the same `bhūmi`, four result
relations are available:

```text
same ground:
    maturation
    correspondence
    activity-production
    dominance

excluded:
    disconnection
```

Disconnection is not a ground-bound conditioned dharma. The same-ground
comparison therefore ranges over the remaining four causal modes.

`Bhūmi` here means a classified causal and contemplative ground. It should not
be reduced to physical location, nor identified without qualification with
the broader `dhātu` classification.

## 5. Other-ground Results

The other-ground cell divides according to contamination:

| Other-ground result | Number | Included relations |
|---|---:|---|
| uncontaminated | 3 | correspondence, activity-produced, dominant |
| contaminated | 2 | activity-produced, dominant |

Uncontaminated dharmas cannot be maturation results and do not supply the
disconnection result in this comparison. The stated reason is
`dhātvapatitatva`: they are not assigned to a conditioned realm in the manner
required for realm-bound maturation.

Contaminated dharmas of another ground also lack correspondence. A
corresponding result continues a similar causal series within the relevant
ground; cross-ground contaminated dharmas can instead be produced or
conditioned through the broader activity and dominance relations.

## 6. The Trainee-action Row

The ordered result-status classes are:

```text
śaikṣa                      trainee
aśaikṣa                     adept; beyond training
naivaśaikṣa-nāśaikṣa       neither trainee nor adept
```

For action belonging to a trainee, all three columns contain three result
relations, but the memberships differ:

| Result status | Number | Included relations | Excluded relations |
|---|---:|---|---|
| trainee | 3 | correspondence, activity-produced, dominant | maturation, disconnection |
| adept | 3 | correspondence, activity-produced, dominant | maturation, disconnection |
| neither | 3 | disconnection, activity-produced, dominant | maturation, correspondence |

The equal numerical row `3–3–3` conceals the decisive shift. Trainee action
can continue into trainee or adept Path dharmas by correspondence. Relative
to neither-status dharmas, disconnection replaces correspondence.

## 7. Training Is a Directional Relation

`Śaikṣa` means someone or something belonging to the Path while training
remains to be completed. `Aśaikṣa` means the training has been completed; it
does not mean untrained. The third category includes dharmas carrying neither
Path status.

The matrix is directional:

```text
status of action → status of result-dharma
```

The action of a trainee can produce an adept result because the Path is
genetically ordered toward completion. The reverse relation cannot be assumed
from symmetry; it requires the separate adept row opened at the end of this
verse.

## 8. Two Matrices in One Verse

VAK 4.91 should not be flattened into a single table. It performs two related
classifications:

```text
Matrix A:
    action ground × result ground × contamination → result types

Matrix B:
    action training status × result training status → result types
```

Ground determines causal continuity across classified fields. Training
status determines causal direction within the architecture of the Path. Both
constrain the same five result relations, but they answer different questions.

## 9. Organon Contact Point

The Causal Algebra for Agency now needs ground and developmental status as
first-class types:

```text
ActionResultEdge {
    actionGround
    resultGround
    resultContamination
    actionTrainingStatus
    resultTrainingStatus
    resultType
}
```

The same numerical signature can encode different operations:

```text
3 results for trainee → trainee
    = correspondence + production + dominance

3 results for trainee → neither
    = disconnection + production + dominance
```

Counts are therefore only compressed checksums. The executable meaning lies
in exact typed membership.

These architecture terms are the Organon reconstruction. The ground theory,
realm status of uncontaminated dharmas, and trainee classifications remain
the doctrine of the Bhāṣya.

## 10. Review Status

The complete 4.91 unit `[257|02]–[257|10]` is included. It gives the full
same-ground/other-ground classification and the full trainee-action row. It
preserves the final phrase opening the adept-action row without importing the
4.92 commentary that completes it. Source and reconstruction remain distinct.
