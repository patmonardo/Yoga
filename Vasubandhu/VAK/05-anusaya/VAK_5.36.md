# VAK 5.36

## Sanskrit

अव्याकृतान्तर्मुखा हि ते समाहितभूमिकाः ।
अत एकीकृताः मूलमविद्येत्यास्रवः पृथक् ॥ ५.३६ ॥

## IAST

avyākṛtāntarmukhā hi te samāhitabhūmikāḥ |
ata ekīkṛtāḥ mūlam avidyety āsravaḥ pṛthak || 5.36 ||

## Padaccheda

avyākṛtāḥ | antarmukhāḥ | hi | te | samāhita-bhūmikāḥ |
ataḥ | ekīkṛtāḥ | mūlam | avidyā | iti | āsravaḥ | pṛthak |

## Grammar

- **avyākṛtāḥ** — nominative plural masculine; ethically indeterminate or neutral.
- **antarmukhāḥ** — nominative plural masculine; inward-facing, turned inward.
- **te** — nominative plural masculine; those afflictions of the form and formless domains discussed in 5.35.
- **samāhita-bhūmikāḥ** — nominative plural masculine compound; belonging to concentrated or meditative planes.
- **ataḥ** — therefore, for this reason.
- **ekīkṛtāḥ** — nominative plural masculine past passive participle; unified, collected into one class.
- **mūlam** — nominative/accusative singular neuter; root.
- **avidyā** — nominative singular feminine; ignorance.
- **iti** — thus, on the ground that.
- **āsravaḥ pṛthak** — a distinct influx, classified separately.

## Literal Translation

For those [higher-domain afflictions] are neutral, inward-facing, and situated in meditative planes. Therefore they are unified. Ignorance, because it is the root, is a separate influx.

## Philosophical Translation

The afflictive tendencies of the form and formless domains are gathered into a single current because their mode is subtle: ethically neutral, inwardly directed, and rooted in concentrated states. Ignorance, however, is not merely one current among others; as their root-condition, it must be distinguished as an influx in its own right.

## Analysis

Verse 5.35 introduced the distinction between **kāmāsrava**, **bhavāsrava**, and the separate influx of ignorance. Verse 5.36 now explains the logic of that classification.

The form- and formless-domain afflictions are grouped together as **bhavāsrava** because they share three structural features:

1. **avyākṛta** — they are ethically indeterminate rather than directly unwholesome;
2. **antarmukha** — their movement is inward rather than outwardly dispersed among coarse sense-objects;
3. **samāhita-bhūmika** — they belong to concentrated meditative planes.

The classification is therefore not based merely on location. It is based on a common **mode of operation**.

The verse then distinguishes ignorance:

> **mūlam avidyā** — ignorance is the root.

Ignorance is classified separately because it does not merely occur within the afflictive stream. It conditions the possibility that the other streams can arise and continue.

Thus:

```text
member of a stream
    ≠
root-condition of the stream
```

The root must be modeled at a different level from the events it grounds.

## Technical Vocabulary

- **āsrava** — influx, outflow, afflictive current.
- **bhavāsrava** — the influx of continued existence, especially through higher-domain latent affliction.
- **avyākṛta** — ethically indeterminate.
- **antarmukha** — inward-facing.
- **samāhita-bhūmi** — a concentrated or meditative plane.
- **mūla** — root, generative principle.
- **avidyā** — ignorance, the fundamental misapprehension conditioning the afflictive system.

## Doctrinal Determination

The verse makes two determinations.

First, a plurality may be legitimately unified when its members share one operative form:

```text
common ethical status
+ common directionality
+ common cognitive plane
    → one influx-class
```

Second, ignorance is separated because roothood is not one property among others. A root occupies a distinct causal level.

The Kośa therefore refuses a flat taxonomy. It distinguishes:

```text
stream-components
stream-organization
stream-root
```

## Logical Determination

The logical form is a double classification:

```text
shared mode
    → unification

generative priority
    → separation
```

The first gathers differences under one universal. The second prevents the universal from swallowing its own ground.

This is important for the Dialectical Copula. A relation engine must be able both to unify determinations by common function and to preserve the asymmetry between a generated state and the ground that generates it.

```text
hasSameModeAs
    supports class formation

isGroundOf
    blocks flat equivalence
```

## Organon Note

For the Platform, 5.36 suggests at least two distinct operations:

```text
clusterByOperationalMode(...)
identifyGenerativeRoot(...)
```

A system should not classify only by surface type or domain. It should also detect whether several states share:

- ethical status,
- direction of attention,
- cognitive plane,
- and mode of manifestation.

But once a root-condition is found, it must not be treated as simply another member of the cluster.

```text
RootCause
    ≠
ClusterMember
```

This is a practical requirement for **making analysis actual**. Otherwise diagnosis collapses the enabling condition into the events it enables.

## OWL++ Seed

```text
Class: Asrava
Class: Bhavasrava SubClassOf: Asrava
Class: Avidyasrava SubClassOf: Asrava
Class: HigherDomainAffliction
Class: GenerativeRoot

ObjectProperty: groupedInto
ObjectProperty: hasOperationalMode
ObjectProperty: hasRoot
ObjectProperty: grounds

DataProperty: hasEthicalStatus
DataProperty: hasDirectionality
DataProperty: hasCognitivePlane

HigherDomainAffliction
    hasEthicalStatus "avyakrta"
    hasDirectionality "antarmukha"
    hasCognitivePlane "samahita"
    groupedInto Bhavasrava

Avidya
    Type GenerativeRoot
    grounds Asrava
```

## Bhāṣya Questions

1. Does the Bhāṣya treat **antarmukha** primarily as freedom from coarse sensory dispersion, or more specifically as inward absorption?
2. Is **samāhitabhūmika** here meant to cover all form- and formless-domain afflictions without exception?
3. How strongly should **mūlam avidyā** be read causally: as universal root, proximate condition, or classificatory ground?
4. Does Vasubandhu accept this separation of ignorance without reservation, or preserve a critique for the following verses?
