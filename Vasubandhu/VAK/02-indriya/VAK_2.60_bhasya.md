# VAK 2.60 — Four Dharma Classes and Their Admissible Causes

## Kārikā

```text
kliṣṭā vipākajāḥ śeṣāḥ prathamāryā yathākramam /
vipākaṃ sarvagaṃ hitvā tau sabhāgaṃ ca śeṣajāḥ // VAkK_2.60 //
```

> The afflicted, the maturation-born, the residual, and the first noble
> [dharmas] arise, respectively, from the remaining causes after excluding the
> maturation cause, the pervasive cause, those two, and those two together with
> the homogeneous cause.

## Continuous Bhāṣya Translation

**Voice: Vasubandhu presenting the six-cause classification**

Which dharmas arise from how many causes?

In summary, dharmas are fourfold: afflicted dharmas, maturation-born dharmas,
the first uncontaminated dharmas, and those remaining after these.

What are the remaining dharmas? They are indeterminate dharmas other than the
maturation-born and wholesome dharmas other than the first uncontaminated
moment. These are the four classes of dharmas.

Afflicted dharmas arise from the five remaining causes after the maturation
cause has been excluded.

Maturation-born dharmas arise from the five remaining causes after the
pervasive cause has been excluded.

The residual dharmas arise from the four remaining causes after both the
maturation and pervasive causes have been excluded.

The first uncontaminated dharmas arise from the three remaining causes after
the maturation, pervasive, and homogeneous causes have been excluded.

The commentary then asks to which domain this fourfold classification first
applies. The next kārikā answers: citta and caitta. It will subsequently apply
the same pattern to material dharmas and formations dissociated from citta,
with associated cause additionally removed. That continuation belongs to VAK
2.61.

## Structural Reconstruction

The Bhāṣya begins with the whole inventory of six causes and derives each
genetic profile by exclusion:

```text
H = {
    conditioning,
    co-arisen,
    associated,
    homogeneous,
    pervasive,
    maturation
}

afflicted
    = H − {maturation}
    = five causes

maturation-born
    = H − {pervasive}
    = five causes

residual
    = H − {maturation, pervasive}
    = four causes

first uncontaminated
    = H − {maturation, pervasive, homogeneous}
    = three causes
```

The order is not a simple numerical descent. The first two classes each have
five causes, but their excluded causes differ. A count alone therefore loses
the logical profile.

The residual class is positively delimited by two exclusions:

```text
residual indeterminate
    = indeterminate − maturation-born

residual wholesome
    = wholesome − first uncontaminated moment
```

The first uncontaminated occurrence is not causeless. Homogeneous cause is
absent because there has been no earlier uncontaminated dharma of the same
class in that continuum. Three other causal relations remain operative.

## Voices

- **Vasubandhu** — frames the question, defines the four classes, and explicates
  the ordered exclusions.
- **Vaibhāṣika six-cause system** — supplies the cause inventory within which
  the exclusion rules operate.
- **Organon reconstruction** — treats the ordered exclusions as typed genetic
  profiles; this formalization is not wording from the kārikā or Bhāṣya.

No competing school position is introduced in this unit.

## New Technical Terms

- **kliṣṭa-dharma** — afflicted dharma.
  - **Status:** Bhāṣya-explicit class.
  - **Function:** arises from five causes, excluding maturation cause.

- **vipākaja** — maturation-born.
  - **Status:** kārikā and Bhāṣya class.
  - **Function:** arises from five causes, excluding pervasive cause.

- **śeṣa** — residual / remaining.
  - **Status:** explicitly defined by the Bhāṣya.
  - **Function:** gathers non-maturation-born indeterminate dharmas and wholesome
    dharmas other than the first uncontaminated moment.

- **prathamānāsrava** — first uncontaminated dharma or moment.
  - **Status:** Bhāṣya specification of kārikā `prathamārya`.
  - **Function:** marks the initial noble breakthrough, arising from three
    causes and lacking any prior homogeneous uncontaminated cause.

- **sarvaga** — pervasive.
  - **Status:** metrical kārikā form for the pervasive cause previously called
    `sarvatraga-hetu`.
  - **Function:** excluded from maturation-born, residual, and first
    uncontaminated profiles.

- **śeṣaja** — born from the remaining causes.
  - **Status:** common predicate of all four kārikā classes.
  - **Function:** makes each genetic profile the complement of its stated
    exclusions within the six-cause inventory.

## Translation Consequences

1. **`Yathākramam` must be made visible.** It maps four classes to four ordered
   exclusion expressions. Without “respectively,” the verse is nearly
   unintelligible.
2. **`Śeṣa` and `śeṣaja` must not be conflated.** The former names the third
   dharma class; the latter predicates birth from the causes left after
   exclusion.
3. **`Prathamārya` is narrow.** The Bhāṣya identifies it as the first
   uncontaminated occurrence, not every noble dharma.
4. **The two five-cause profiles are not equivalent.** Afflicted and
   maturation-born dharmas exclude different causes.
5. **“Born from” expresses causal classification, not substantial production.**
   The verse specifies admissible relations in the six-hetu system.

## Doctrinal and Logical Determination

This unit answers a second-order causal question:

```text
not merely:
    What is a cause?

but:
    Given the status of an arising dharma,
    which already-defined causal relations can ground it?
```

The result is a constraint table:

| Dharma class | Excluded cause | Number remaining |
|---|---|---:|
| afflicted | maturation | 5 |
| maturation-born | pervasive | 5 |
| residual | maturation and pervasive | 4 |
| first uncontaminated | maturation, pervasive, and homogeneous | 3 |

The causes excluded from the first uncontaminated occurrence show three
different kinds of incompatibility:

```text
maturation cause
    → cannot generate the noble breakthrough as karmic maturation

pervasive cause
    → belongs to the afflicted causal order

homogeneous cause
    → would require an earlier uncontaminated occurrence of the same class
```

Accordingly, novelty on the Path is neither self-generation nor absence of
ground. It is a newly available causal profile whose very first occurrence
cannot presuppose its own prior homogeneous instance.

## Limited Organon Interpretation

VAK 2.60 turns the six causes into a typed validation engine:

```text
HetuProfile {
    dharmaClass,
    candidateCauseInventory,
    excludedCauseTypes,
    admissibleCauseTypes,
    exclusionGround
}
```

The decisive database lesson is that identical counts do not establish
identical schemas:

```text
count(afflicted causes) = 5
count(maturation-born causes) = 5

but

excluded(afflicted) = maturation
excluded(maturation-born) = pervasive
```

An Ocular representation must retain the named relations and the grounds for
their exclusion, not only the cardinality of a cause set.

The first uncontaminated occurrence also provides a precise form for a Path
transition. Its novelty consists in the absence of a prior homogeneous noble
determination, while its remaining causal structure prevents the transition
from becoming an inexplicable leap.

This completes the profile-level analysis of `hetu`. VAK 2.61 will qualify the
profile by dharma domain before opening the four `pratyaya`.
