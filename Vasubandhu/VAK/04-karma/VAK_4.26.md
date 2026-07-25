# VAK_4.26

## Sanskrit — Devanāgarī

```sanskrit
ध्यानजो ध्यानभूम्यैव लभ्यतेऽनास्रवस्तया ।
आर्यया प्रातिमोक्षाख्यः परविज्ञापनादिभिः ॥
```

## Sanskrit — IAST

```iast
dhyānajo dhyānabhūmyaiva labhyate 'nāsravas tayā |
āryayā prātimokṣākhyaḥ paravijñāpanādibhiḥ ||
```

## Source reference and caution

Source: `VAkK_4.26`.

The verse begins the account of how the three restraints are acquired:

```text
dhyānaja-saṃvara
anāsrava-saṃvara
prātimokṣa-saṃvara
```

## Padaccheda

```text
dhyāna-jaḥ
dhyāna-bhūmyā
eva
labhyate

anāsravaḥ
tayā
āryayā

prātimokṣa-ākhyaḥ
para-vijñāpana-ādibhiḥ
```

| Form | Analysis | Working meaning |
|---|---|---|
| `dhyānajaḥ` | nominative singular masculine | born from dhyāna |
| `dhyānabhūmyā` | instrumental singular feminine | through a dhyāna level |
| `eva` | restrictive particle | only |
| `labhyate` | present passive | is obtained |
| `anāsravaḥ` | nominative singular masculine | uncontaminated |
| `tayā āryayā` | instrumental singular feminine | through that noble level |
| `prātimokṣākhyaḥ` | nominative singular masculine | called prātimokṣa |
| `paravijñāpanādibhiḥ` | instrumental plural | through notification by another and related procedures |

## Literal translation

> The restraint born from dhyāna is obtained only through a dhyāna level; the uncontaminated restraint is obtained through that level insofar as it is noble; the restraint called prātimokṣa is obtained through notification by another and related procedures.

## Philosophical translation

> Meditative restraint arises intrinsically from attainment of a meditative ground, while uncontaminated restraint arises from that ground when it has become noble path-attainment. Prātimokṣa restraint, by contrast, is acquired through a determinate interpersonal and declarative procedure.

## Technical analysis

### `dhyānaja`

`dhyāna + ja` means “born from dhyāna.” The `-ja` preserves genesis: this restraint is produced by actual meditative attainment, not merely by verbal undertaking.

```text
dhyāna-bhūmi attainment
    → dhyānaja-saṃvara
```

### `anāsrava`

The uncontaminated restraint belongs to the noble path. The compressed construction is:

```text
anāsravaḥ [saṃvaraḥ]
tayā āryayā [bhūmyā labhyate]
```

Thus:

```text
ārya-bhūmi / ārya-mārga
    → anāsrava-saṃvara
```

### `prātimokṣākhya`

The restraint called prātimokṣa is acquired neither by mere meditative state nor by noble path-attainment, but through an interpersonal undertaking.

### `paravijñāpana`

`para-vijñāpana` means notification, declaration, or formal communication by another person. The plural `-ādibhiḥ` indicates a range of accepted procedures, not only one ordination form.

## Three modes of acquisition

| Restraint | Ground | Mode |
|---|---|---|
| `dhyānaja` | dhyāna level | meditative attainment |
| `anāsrava` | noble level/path | supramundane attainment |
| `prātimokṣa` | another person and formal procedure | communicative undertaking |

```text
state-generated restraint
path-generated restraint
declaration-generated restraint
```

## Logical determination

Each restraint is acquired through a ground adequate to its nature:

```text
dhyānaja restraint
    requires dhyāna

anāsrava restraint
    requires noble path-attainment

prātimokṣa restraint
    requires formal interpersonal declaration
```

The first two are immanently generated through transformation of the continuum. The third is socially mediated, yet becomes a real persistent karmic form.

```text
formal communication
    → undertaking
    → prātimokṣa-avijñapti
```

Thus convention can become karmically efficacious when properly enacted.

## Relation to VAK_4.25

```text
VAK_4.25
    vijñapti and avijñapti can occur separately

VAK_4.26
    each persistent restraint has its own genesis
```

## Light Organon interpretation

The verse distinguishes three ways in which ethical form becomes actual:

```text
immediate state-form
    dhyānaja

rational path-form
    anāsrava

mediated institutional form
    prātimokṣa
```

The speech act does not merely report the vow. It participates in producing the standing form.

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_26
    a vak:Karika ;
    rdfs:label "VAK 4.26" ;
    vak:continues vak:VAK_4_25 ;
    vak:hasTopic vak:AcquisitionOfRestraint .

vak:DhyanaBornRestraint
    rdfs:subClassOf vak:Restraint ;
    vak:acquiredThrough vak:DhyanaAttainment .

vak:UncontaminatedRestraint
    rdfs:subClassOf vak:Restraint ;
    vak:acquiredThrough vak:NoblePathAttainment .

vak:PratimokshaRestraint
    rdfs:subClassOf vak:Restraint ;
    vak:acquiredThrough vak:FormalNotification .
```

## Verse summary

```text
VAK_4.26

Meditative restraint
is born from meditative attainment.

Uncontaminated restraint
is born from noble path-attainment.

Prātimokṣa restraint
is born from formal interpersonal undertaking.

The mode of acquisition
corresponds to the nature
of the restraint acquired.
```
