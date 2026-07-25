# VAkK 4.37

## Sanskrit

### Devanāgarī

> असंवरस्य क्रियया लाभोऽभ्युपगमेन वा ।  
> शेषाविज्ञप्तिलाभस्तु क्षेत्रादानादरेहनात् ॥ ४.३७ ॥

### IAST

> **asaṃvarasya kriyayā lābho ’bhyupagamena vā |**  
> **śeṣāvijñaptilābhas tu kṣetrādānādarehanāt || 4.37 ||**

The final compound is densely compressed. A cautious segmentation is:

```text
kṣetra-ādāna-ādara-īhanāt
```

with four conditioning factors: field, taking up, earnestness, and effort.

## Padaccheda

```text
asaṃvarasya
kriyayā
lābhaḥ
abhyupagamena
vā |

śeṣa-avijñapti-lābhaḥ
tu
kṣetra-ādāna-ādara-īhanāt ||
```

Expanded syntax:

```text
asaṃvarasya lābhaḥ
    kriyayā
    abhyupagamena vā

śeṣasya avijñapteḥ lābhaḥ tu
    kṣetrāt
    ādānāt
    ādarāt
    īhanāt
```

## Grammar

| Form | Analysis | Meaning |
|---|---|---|
| **asaṃvarasya** | genitive singular | of non-restraint |
| **kriyayā** | instrumental singular | through action or performance |
| **lābhaḥ** | nominative singular | acquisition |
| **abhyupagamena** | instrumental singular | through undertaking or acceptance |
| **vā** | disjunctive particle | or |
| **śeṣāvijñaptilābhaḥ** | nominative singular compound | acquisition of the remaining avijñapti |
| **kṣetrāt** | ablative singular | from a field |
| **ādānāt** | ablative singular | from taking up |
| **ādarāt** | ablative singular | from earnestness or intensity |
| **īhanāt** | ablative singular | from effort or striving |

## Literal translation

> **Non-restraint is acquired through performing the action or through undertaking it. The remaining avijñapti, however, is acquired through the field, taking up, earnestness, and active effort.**

## Philosophical translation

> **A durable harmful form may arise either from enacted practice or from the deliberate assumption of a harmful practical identity. Beyond complete restraint and non-restraint, particular actions also generate persistent unmanifest determinations. Their acquisition depends upon the field involved, the undertaking through which the act is assumed, the seriousness with which it is embraced, and the effort through which it is actualized.**

## Doctrinal determination

Non-restraint has two principal acquisition modes:

```text
kriyā
    performance of the harmful action

abhyupagama
    deliberate adoption of the harmful practice
```

Thus asaṃvara may arise either from deed to standing disposition or from adopted standing disposition toward future deed.

The “remaining avijñapti” refers to persistent karmic forms belonging neither to complete restraint nor to complete non-restraint. This preserves the intermediate category of determinate durable action-form.

The four factors are:

```text
kṣetra
    the recipient-field or object-field

ādāna
    taking up or assuming the act

ādara
    earnestness, regard, intensity

īhana
    effort, striving, active performance
```

A transient visible action can therefore become a persistent karmic record through a relational and intentional complex rather than through bare motion alone.

## Logical determination

The verse distinguishes:

```text
actuality generating form:
    kriyā → asaṃvara

form anticipating actuality:
    abhyupagama → asaṃvara
```

It then adds the mediated structure of other avijñapti:

```text
field
undertaking
earnestness
effort
    → persistent determination
```

The avijñapti is the unity of ground, relation, execution, and persistence.

## Light Organon interpretation

VAkK 4.37 shows Karma as the logic of how activity becomes form. Activity is not lost when the visible event ceases; it returns into the continuum as a standing determination. But the determination is generated through the complete structure of the act: its field, acceptance, intensity, and effort.

This supports a non-substantialist account of agency. There is no permanent agent behind action, but there is a fully determinate organization of undertaking, direction, intensity, effort, field, and result.

## Typed feature structure

```text
[ NON-RESTRAINT-ACQUISITION
  MODE
    action-performance
    | deliberate-undertaking
  RESULT
    persistent-non-restraint ]
```

```text
[ REMAINING-AVIJNAPTI-ACQUISITION
  FIELD          kṣetra
  ASSUMPTION     ādāna
  EARNESTNESS    ādara
  EFFORT         īhana
  RESULT         persistent-particular-form ]
```

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_37
    a vak:Karika ;
    rdfs:label "VAK 4.37" ;
    vak:continues vak:VAK_4_36 ;
    vak:hasTopic vak:ModesOfAvijnaptiAcquisition .

vak:NonRestraint
    vak:mayBeAcquiredThrough vak:HarmfulActionPerformance ;
    vak:mayBeAcquiredThrough vak:HarmfulPracticeUndertaking .

vak:RemainingAvijnapti
    vak:acquisitionCondition vak:Field ;
    vak:acquisitionCondition vak:TakingUp ;
    vak:acquisitionCondition vak:Earnestness ;
    vak:acquisitionCondition vak:Effort .
```

## Determinate result

VAkK 4.37 establishes:

```text
asaṃvara:
    acquired through performing
    or deliberately undertaking
    the harmful activity

remaining avijñapti:
    acquired through field,
    assumption, earnestness, and effort
```

Its central principle is:

```text
a transient action becomes
a persistent karmic determination
through the complete relational structure
of how it is undertaken,
toward what field,
with what intensity,
and through what effort
```
