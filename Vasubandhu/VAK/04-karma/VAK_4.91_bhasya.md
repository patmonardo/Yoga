# VAK 4.91 — Bhāṣya Study

## Kārikā

**svabhūmi-dharmāś catvāri trīṇi dve vānya-bhūmikāḥ |**  
**śaikṣasya trīṇi śaikṣādyā aśaikṣasya tu karmaṇaḥ || 4.91 ||**

See: [VAK_4.91.md](./VAK_4.91.md)

## Bhāṣya Source

```text
svabhūmikasya karmaṇaḥ svabhūmikā dharmāś catvāri phalāni visaṃyogaphalaṃ hitvā /

anyabhūmikā dharmā anāsravāś cet trīṇi phalāni /
vipākavisaṃyogaphale hitvā /
dhātvapatitatvāt /
sāsravāś cet dve puruṣakārādhipatiphale /

śaikṣasya karmaṇaḥ śaikṣā dharmās trīṇi phalāni vipākavisaṃyogaphale hitvā /
aśaikṣā apy evam /
naivaśaikṣānāśaikṣā api vipākaniḥṣyandaphale hitvā /
```

The sentence then continues into VAK 4.92 with the karma of the `aśaikṣa`.

## Literal Prose Translation

For karma belonging to its own level, dharmas belonging to that same level are four fruits, with the disconnection-fruit excluded.

If dharmas belonging to another level are uncontaminated, they are three fruits, with maturation and disconnection excluded, because they do not fall within a domain. If they are contaminated, they are two fruits: the activity-produced fruit and the dominant fruit.

For the karma of a trainee, trainee dharmas are three fruits, with maturation and disconnection excluded. Dharmas of one beyond training are likewise three. Dharmas that are neither trainee nor beyond-training are also three fruits, but here maturation and outflow are excluded.

## Argument Reconstruction

The verse adds two new relational axes to the fruit system developed in 4.87–4.90.

### 1. Bhūmi relation

The first distinction is relational:

```text
same bhūmi
    versus
other bhūmi
```

For same-level karma and result-dharmas:

```text
vipāka
niḥṣyanda
puruṣakāra
adhipati
```

are available.

`visaṃyoga` is excluded.

For result-dharmas belonging to another bhūmi, the count divides again according to contamination-status.

If the other-bhūmi dharmas are **uncontaminated**:

```text
niḥṣyanda
puruṣakāra
adhipati
```

are available.

Both `vipāka` and `visaṃyoga` are excluded.

The Bhāṣya gives a specific reason for the absence of maturation:

```text
dhātvapatitatvāt
because they do not fall within a domain
```

If the other-bhūmi dharmas are **contaminated**:

```text
puruṣakāra
adhipati
```

alone remain.

So `anya-bhūmika` by itself does not determine one result-count. The decisive further condition is whether the result-dharmas are contaminated or uncontaminated.

### 2. Training-status relation

The second half begins a new matrix based on:

```text
śaikṣa
    trainee

aśaikṣa
    beyond training

naivaśaikṣa-nāśaikṣa
    neither trainee nor beyond-training
```

For **trainee karma** the Bhāṣya already gives the whole row:

```text
trainee results:
    3
    niḥṣyanda
    puruṣakāra
    adhipati

beyond-training results:
    3
    niḥṣyanda
    puruṣakāra
    adhipati

neither results:
    3
    visaṃyoga
    puruṣakāra
    adhipati
```

The third cell is especially important: it has the same cardinality as the first two, but **different membership**.

The predicate `aśaikṣasya tu karmaṇaḥ` deliberately carries the matrix into VAK 4.92.

## Voice

**Voice:** Vaibhāṣika Abhidharma classification, transmitted and explained by Vasubandhu.

No explicit objection appears in this unit; the prose is systematic exposition.

## New Technical Terms

- **svabhūmika** — belonging to the same `bhūmi` as the source karma.  
  **Status:** already implicit in prior realm/domain classifications, now technicalized relationally.  
  **Function:** determines admissible fruit-relations.

- **anyabhūmika** — belonging to another `bhūmi`.  
  **Status:** newly explicit in this fruit matrix.  
  **Function:** introduces cross-level causal restriction.

- **dhātvapatitatva** — not falling within a domain.  
  **Status:** Bhāṣya-only explanatory phrase in this unit.  
  **Function:** explains why uncontaminated other-bhūmi dharmas cannot be `vipāka-phala`.

- **śaikṣa** — trainee, one for whom training remains.  
  **Status:** previously encountered in the Kośa.  
  **Function:** path-status axis of the result matrix.

- **aśaikṣa** — beyond training, one whose training is complete.  
  **Status:** previously encountered.  
  **Function:** second path-status class; its karma is treated in 4.92.

- **naivaśaikṣa-nāśaikṣa** — neither trainee nor beyond-training.  
  **Status:** technical third class.  
  **Function:** completes the threefold path-status matrix.

## Doctrinal Determination

VAK 4.91 demonstrates that `bhūmi` is not merely a location-label. It becomes an active constraint on causal relation.

The first matrix is:

```text
same bhūmi:
    4 fruits
    minus visaṃyoga

other bhūmi + uncontaminated:
    3 fruits
    minus vipāka, visaṃyoga

other bhūmi + contaminated:
    2 fruits
    puruṣakāra, adhipati
```

The second matrix begins:

```text
source karma = trainee

result status:
    trainee          → 3
    beyond-training  → 3
    neither          → 3
```

but equal counts conceal different sets.

Thus the causal system must track not only the class of source and result, but the **relation between their classifications**.

## Logical Determination

The important predicates are relational:

```text
SameBhumi(K, R)
DifferentBhumi(K, R)
```

not unary properties of an isolated dharma.

A clean rule structure is:

```text
SameBhumi(K, R)
    → Results(K,R) = {
        vipāka,
        niḥṣyanda,
        puruṣakāra,
        adhipati
      }
```

```text
DifferentBhumi(K, R)
and Uncontaminated(R)
    → Results(K,R) = {
        niḥṣyanda,
        puruṣakāra,
        adhipati
      }
```

```text
DifferentBhumi(K, R)
and Contaminated(R)
    → Results(K,R) = {
        puruṣakāra,
        adhipati
      }
```

The trainee row adds:

```text
TraineeKarma(K)
and TraineeResult(R)
    → {niḥṣyanda, puruṣakāra, adhipati}

TraineeKarma(K)
and BeyondTrainingResult(R)
    → {niḥṣyanda, puruṣakāra, adhipati}

TraineeKarma(K)
and NeitherResult(R)
    → {visaṃyoga, puruṣakāra, adhipati}
```

The lesson is the same one already emerging in 4.87–4.90:

```text
same result-count
    does not imply
same causal membership
```

## Translation Consequences

The first-pass rendering of `bhūmi` as “domain-level” remains useful, but the Bhāṣya shows that the category is more general than the three `dhātu`s. Here it functions as a classified level relative to source and result.

The line `trīṇi dve vānyabhūmikāḥ` should therefore not be translated as if all other-level dharmas were simply either three or two without condition. The Bhāṣya supplies the missing distinction:

```text
uncontaminated other-level dharmas → 3
contaminated other-level dharmas   → 2
```

The second half should likewise be allowed to remain syntactically open into 4.92.

## Light Organon Contact

The Bhāṣya is now effectively constructing a typed relation system.

A result relation is not determined by either endpoint alone:

```text
source class
result class
source-result level relation
contamination status
path status
```

all participate in determining the admissible fruit-set.

The clean abstraction is therefore:

```text
QualifiedFruitRelation(
    source,
    result,
    sourceLevel,
    resultLevel,
    contaminationStatus,
    trainingStatus,
    fruitType
)
```

This is not an external analogy imposed on the text; it is simply the logical form of Vasubandhu's increasingly explicit matrix.

## Summary

VAK 4.91 adds two more dimensions to the five-fruit system.

```text
same bhūmi
    → 4 fruits
    → no visaṃyoga

other bhūmi + uncontaminated
    → 3 fruits
    → no vipāka, no visaṃyoga

other bhūmi + contaminated
    → 2 fruits
    → puruṣakāra, adhipati
```

For trainee karma:

```text
trainee results         → 3
beyond-training results → 3
neither results         → 3
```

but the third set differs in membership.

VAK 4.92 continues from `aśaikṣasya tu karmaṇaḥ` and completes the path-status matrix.