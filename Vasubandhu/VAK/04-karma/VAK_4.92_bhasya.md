# VAK_4.92 — Bhāṣya

## Kārikā

> dharmāḥ śaikṣādikā ekaṃ phalaṃ trīṇy api ca dvayam |
> tābhyām anyasya śaikṣādyā dve dve pañca phalāni ca || 4.92 ||

**Best translation:**  
For the karma of one beyond training, the dharmas beginning with the trainee class constitute respectively one result, three results, and two. For karma other than those two, the classes beginning with the trainee constitute respectively two, two, and five results.

**Kārikā analysis:** [`VAK_4.92.md`](./VAK_4.92.md)

## Bhāṣya Source

Working e-text, Pradhan/Shastri-based reference source, around [257|11–257|16].

```text
aśaikṣasya karmaṇaḥ śaikṣā dharmāḥ ekamadhipatiphalam /
aśaikṣāstrīṇi vipākavisaṃyogaphale hitvā /
naivaśaikṣānāśaikṣā dve puruṣakārādhipatiphale /

tābhyāmanyasya śaikṣādyā dve dve pañca phalāni ca // VAkK_4.92 //

śaikṣāśaikṣābhyāmanyasya karmaṇo naivaśaikṣānāśaikṣasya śaikṣā dharmā dve puruṣakārādhipatiphale /
aśaikṣā apyevam /
naivaśaikṣānāśaikṣāḥ pañca phalāni /
```

The prose completes the path-status matrix begun in VAK 4.91.

## Natural Segmentation

### 1. Aśaikṣa karma → śaikṣa dharmas

```text
ekaṃ phalam
```

Only one fruit-relation applies:

```text
adhipati-phala
```

### 2. Aśaikṣa karma → aśaikṣa dharmas

Three fruit-relations apply, excluding:

```text
vipāka-phala
visaṃyoga-phala
```

Therefore:

```text
niḥṣyanda-phala
puruṣakāra-phala
adhipati-phala
```

### 3. Aśaikṣa karma → neither-status dharmas

Two fruit-relations apply:

```text
puruṣakāra-phala
adhipati-phala
```

### 4. Neither-status karma → śaikṣa dharmas

Two fruit-relations:

```text
puruṣakāra-phala
adhipati-phala
```

### 5. Neither-status karma → aśaikṣa dharmas

The same two:

```text
puruṣakāra-phala
adhipati-phala
```

### 6. Neither-status karma → neither-status dharmas

All five fruit-relations apply:

```text
vipāka-phala
niḥṣyanda-phala
visaṃyoga-phala
puruṣakāra-phala
adhipati-phala
```

## Literal Prose Translation

For the karma of one beyond training, trainee dharmas are one fruit, namely the dominant fruit. Beyond-training dharmas are three fruits, excluding maturation and disconnection. Dharmas that are neither trainee nor beyond-training are two fruits, the activity-produced fruit and the dominant fruit.

For karma other than trainee and beyond-training—that is, karma that is neither trainee nor beyond-training—trainee dharmas are two fruits, the activity-produced and dominant fruits. Beyond-training dharmas are likewise two. Dharmas that are neither trainee nor beyond-training are all five fruits.

## Argument Reconstruction

VAK 4.91–4.92 does not classify karma by intrinsic labels alone. It asks how a source karma of one path-status may stand in fruit-relations to dharmas of another path-status.

The completed matrix is:

| Source karma | śaikṣa result | aśaikṣa result | neither result |
|---|---|---|---|
| śaikṣa | niḥṣyanda, puruṣakāra, adhipati | niḥṣyanda, puruṣakāra, adhipati | visaṃyoga, puruṣakāra, adhipati |
| aśaikṣa | adhipati | niḥṣyanda, puruṣakāra, adhipati | puruṣakāra, adhipati |
| neither | puruṣakāra, adhipati | puruṣakāra, adhipati | all five |

Numerically:

```text
              target
source     śaikṣa  aśaikṣa  neither
śaikṣa        3       3        3
aśaikṣa       1       3        2
neither       2       2        5
```

The table is directed:

```text
C(source, target) ≠ C(target, source)
```

For example:

```text
śaikṣa → aśaikṣa = 3

aśaikṣa → śaikṣa = 1
```

This asymmetry is doctrinally substantive, not an artifact of enumeration.

## Voice

**Voice:** Vasubandhu, presenting the Abhidharma fruit-classification without a marked objection in this unit.

## New Technical Terms

- **tābhyām anya** — “other than those two,” here the class that is neither śaikṣa nor aśaikṣa.  
  **Status:** already structurally implied in 4.91; explicit here.  
  **Function:** completes the third path-status required for the matrix.

- **naivaśaikṣānāśaikṣa** — neither trainee nor beyond-training.  
  **Status:** technical path-status class.  
  **Function:** marks dharmas outside the two noble training statuses.

- **ekam adhipatiphalam** — a single result, specifically dominant result.  
  **Status:** exact Bhāṣya clarification absent from the Kārikā alone.  
  **Function:** identifies the sole admissible relation from aśaikṣa karma to śaikṣa dharmas.

## Doctrinal Determination

The completed table shows that path-status is a genuine causal qualifier.

A dharma being śaikṣa, aśaikṣa, or neither does not by itself determine its fruit-status. The relevant determination is relational:

```text
source-status
    ×
target-status
    ×
fruit-type
```

The strongest asymmetries are:

```text
aśaikṣa karma → śaikṣa dharmas
    only adhipati

neither karma → neither dharmas
    all five fruits
```

Thus the broadest fruit-range occurs not in the noble statuses but in the neither-status relation to itself.

This does not imply superiority. It means only that all five technical causal relations are available in that ordered cell.

## Logical Determination

Define:

```text
F(S, T)
    = set of admissible fruit-types
      from source status S
      to target status T
```

Then:

```text
F(Śaikṣa, Śaikṣa)
    = {Niḥṣyanda, Puruṣakāra, Adhipati}

F(Śaikṣa, Aśaikṣa)
    = {Niḥṣyanda, Puruṣakāra, Adhipati}

F(Śaikṣa, Neither)
    = {Visaṃyoga, Puruṣakāra, Adhipati}

F(Aśaikṣa, Śaikṣa)
    = {Adhipati}

F(Aśaikṣa, Aśaikṣa)
    = {Niḥṣyanda, Puruṣakāra, Adhipati}

F(Aśaikṣa, Neither)
    = {Puruṣakāra, Adhipati}

F(Neither, Śaikṣa)
    = {Puruṣakāra, Adhipati}

F(Neither, Aśaikṣa)
    = {Puruṣakāra, Adhipati}

F(Neither, Neither)
    = {Vipāka, Niḥṣyanda, Visaṃyoga, Puruṣakāra, Adhipati}
```

The matrix therefore demonstrates again:

```text
same count
    ≠
same membership
```

and:

```text
same two statuses
    ≠
symmetric relation
```

## Translation Consequences

The first-pass translation is basically correct. The Bhāṣya allows us to sharpen it by making clear that the numerals count technical fruit-relations, not concrete individual effects.

The phrase `ekaṃ phalam` in the first pāda should be understood specifically as:

```text
one fruit-relation: adhipati-phala
```

Likewise `pañca phalāni` in the final cell means the complete fivefold fruit taxonomy is admissible.

## Light Organon Contact

The fruit matrix is now complete as a directed relation-table.

The useful structural lesson is restrained but exact:

```text
classification(source)
classification(target)
    ↓
do not determine causality independently

ordered relation(source, target)
    ↓
determines admissible causal predicates
```

The visible 3×3 table is therefore a projection of the deeper relation:

```text
SourceStatus × FruitType × TargetStatus
```

This is a good example of why the Kośa repeatedly resists unary classification. Its logic is relational and context-sensitive.

## Completion of the Fruit Matrix

VAK 4.87–4.92 has now successively indexed the five fruits by:

```text
contamination/path status
ethical quality
source/result quality
time
bhūmi
training status
```

The recurring principle is:

```text
phala is not a single output relation

it is a family of technically distinct causal relations
whose admissibility depends on the determinations
of both source and result
```

VAK 4.92 closes the śaikṣa/aśaikṣa/neither matrix. VAK 4.93 begins a new indexing by what is abandoned through seeing, cultivation, or is not to be abandoned.
