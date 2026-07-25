# VAkK 4.35

## Sanskrit

### Devanāgarī

> सर्वोभयेभ्यः कामाप्तो वर्तमानेभ्य आप्यते ।  
> मौलेभ्यः सर्वकालेभ्यो ध्यानानास्रवसंवरौ ॥ ४.३५ ॥

### IAST

> **sarvobhayebhyaḥ kāmāpto vartamānebhya āpyate |**  
> **maulebhyaḥ sarvakālebhyo dhyānānāsravasaṃvarau || 4.35 ||**

## Source caution

The verse begins a new determination: the range of beings, offenses, and times with respect to which the different restraints are acquired. The scope of **ubhaya** is compressed and should be fixed only with the Bhāṣya.

## Padaccheda

```text
sarva-ubhayebhyaḥ
kāma-āptaḥ
vartamānebhyaḥ
āpyate |

maulebhyaḥ
sarva-kālebhyaḥ
dhyāna-anāsrava-saṃvarau ||
```

Expanded syntax:

```text
kāmāptaḥ saṃvaraḥ
    sarva-ubhayebhyaḥ
    vartamānebhyaḥ
    āpyate

dhyānasaṃvaraḥ
anāsravasaṃvaraḥ
    maulebhyaḥ
    sarvakālebhyaḥ
    āpyete
```

## Grammar

| Form | Analysis | Working meaning |
|---|---|---|
| **sarvobhayebhyaḥ** | ablative plural compound | with respect to all and both relevant classes |
| **kāmāptaḥ** | nominative singular masculine | belonging to the desire realm |
| **vartamānebhyaḥ** | ablative plural | with respect to present beings |
| **āpyate** | passive present of *āp* | is acquired |
| **maulebhyaḥ** | ablative plural of *maula* | with respect to fundamental offenses |
| **sarvakālebhyaḥ** | ablative plural | with respect to all times |
| **dhyānānāsravasaṃvarau** | nominative dual | meditation-born and uncontaminated restraints |

## Literal translation

> The restraint belonging to the desire realm is acquired with respect to all relevant classes and to presently existing beings. The meditation-born and uncontaminated restraints are acquired with respect to the fundamental offenses and throughout all times.

## Philosophical translation

> Ordinary prātimokṣa restraint is instituted within the present embodied world and determines conduct toward the current field of living beings. Meditation-born and noble restraint penetrate more deeply: they concern the fundamental forms of misconduct as discriminated across past, present, and future.

## Doctrinal determination

The verse distinguishes three restraints by origin and scope:

```text
prātimokṣa-saṃvara
    desire-realm
    present field of beings

dhyānaja-saṃvara
    meditation-born
    fundamental offenses
    all three times

anāsrava-saṃvara
    noble-Path-born
    fundamental offenses
    all three times
```

The ordinary vow reorganizes present bodily and verbal relations. The higher restraints are not limited to an immediate empirical occasion; they concern the root structure of misconduct.

## Relation to kleśa and Path

```text
ordinary vow
    governs determinate present conduct
    while latent kleśa may remain

meditation-born restraint
    suppresses coarse kleśa-expression
    through a transformed meditative ground

uncontaminated restraint
    belongs to the noble Path
    and addresses the root relation
    between kleśa and action
```

This supports the distinction between restraining manifestation and transforming the causal ground of manifestation.

## Logical determination

The verse distinguishes two modes of universality:

```text
practical universality
    all relevant present beings

cognitive universality
    fundamental misconduct across all times
```

Thus the depth and origin of a restraint determine its objective and temporal range.

## Light Organon interpretation

A restraint is not merely a prohibition. It is a structured record with fields such as:

```text
origin
realm
object-field
offense-scope
temporal range
mode of acquisition
```

The ordinary vow constitutes an ethical world of present relations. The higher restraints constitute a more universal cognitive relation to the fundamental activity itself.

## Typed feature structure

```text
[ PRATIMOKSHA-RESTRAINT
  REALM           desire
  BEING-SCOPE     all-relevant-present-beings
  TEMPORAL-SCOPE  present
  ACQUISITION     formal-undertaking ]

[ DHYANA-RESTRAINT
  OFFENSE-SCOPE   fundamental
  TEMPORAL-SCOPE  past-present-future
  ACQUISITION     dhyana-attainment ]

[ UNCONTAMINATED-RESTRAINT
  OFFENSE-SCOPE   fundamental
  TEMPORAL-SCOPE  past-present-future
  ACQUISITION     noble-path ]
```

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_35
    a vak:Karika ;
    rdfs:label "VAK 4.35" ;
    vak:continues vak:VAK_4_34 ;
    vak:hasTopic vak:ScopeOfRestraintAcquisition .

vak:PratimokshaRestraint
    vak:belongsToRealm vak:DesireRealm ;
    vak:hasTemporalScope vak:Present ;
    vak:hasBeingScope vak:AllRelevantPresentBeings .

vak:DhyanaBornRestraint
    vak:hasOffenseScope vak:FundamentalOffenses ;
    vak:hasTemporalScope vak:AllThreeTimes .

vak:UncontaminatedRestraint
    vak:hasOffenseScope vak:FundamentalOffenses ;
    vak:hasTemporalScope vak:AllThreeTimes .
```

## Determinate result

VAkK 4.35 establishes:

```text
desire-realm prātimokṣa restraint
    is acquired within the present field
    of embodied relations

dhyāna-born and uncontaminated restraint
    are acquired with respect to
    fundamental misconduct throughout all times
```

Its central principle is:

```text
the depth and origin of a restraint
determine the objective and temporal range
over which it operates
```
