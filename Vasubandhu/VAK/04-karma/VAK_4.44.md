# VAkK 4.44

## Sanskrit

### Devanāgarī

> कामरूपजदेवानां ध्यानजः अनास्रवः पुनः ।  
> ध्यानान्तरासंज्ञिसत्त्ववर्ज्यानामप्यरूपिणाम् ॥ ४.४४ ॥

### IAST

> **kāmarūpajadevānāṃ dhyānajaḥ anāsravaḥ punaḥ |**  
> **dhyānāntarāsaṃjñisattvavarjyānām apy arūpiṇām || 4.44 ||**

## Padaccheda

```text
kāma-rūpa-ja-devānām
dhyāna-jaḥ |

anāsravaḥ
punaḥ |

dhyāna-antara-asaṃjñi-sattva-varjyānām
api
arūpiṇām ||
```

The understood substantive is **saṃvaraḥ**, carried forward from VAkK 4.43:

```text
dhyānajaḥ saṃvaraḥ
anāsravaḥ saṃvaraḥ
```

## Literal translation

> **Restraint born from dhyāna belongs to gods born in the desire and form domains. Uncontaminated restraint, in turn, belongs also to formless beings, excluding the intermediate-dhyāna and non-percipient beings.**

The syntax is compressed, and the precise attachment of the exclusions should be checked against the Bhāṣya.

## Doctrinal determination

VAkK 4.43 established the eligible bearer. VAkK 4.44 determines the generating ground and corresponding distribution of the higher restraints.

### Dhyāna-born restraint

```text
dhyāna
    → purified meditative activity
    → dhyānaja-saṃvara
```

This restraint is not acquired through verbal undertaking. It arises from the meditative state itself. Its range therefore follows the range of beings capable of actualizing dhyāna.

A being born in the desire domain may nevertheless produce a cognition associated with a higher meditative level. Thus:

```text
domain of birth
    ≠ necessarily
level of presently actualized cognition
```

### Uncontaminated restraint

**Anāsrava-saṃvara** arises with the uncontaminated noble path:

```text
noble path
    → anāsrava-saṃvara
```

It does not arise merely because a being inhabits a higher world. Its decisive condition is the actualization of path-cognition. Hence it can extend even into formless existence where the required cognitive conditions are available.

### Functional exclusions

The excluded modes are not morally condemned. They lack the determinate cognitive basis required to produce the corresponding restraint.

```text
absence of generative cognition
    → absence of generated restraint
```

## Philosophical translation

> **Meditative restraint occurs among divine beings of the desire and form domains wherever the corresponding dhyāna can be actualized. Uncontaminated restraint has a still wider domain: it can occur even within formless existence, though not in modes of existence that lack the cognitive and path-conditions required for its production.**

## Relation to VAkK 4.43

The three restraints are not distributed uniformly:

```text
prātimokṣa-saṃvara
    conventional undertaking

dhyānaja-saṃvara
    meditative production

anāsrava-saṃvara
    noble-path production
```

The final **trayaḥ** of VAkK 4.43 therefore announces a distribution that VAkK 4.44 differentiates according to generating condition.

## Logic of Experience

```text
RESTRAINT-TYPE
    has GENERATING-CONDITION

GENERATING-CONDITION
    requires ELIGIBLE-BEARER

ELIGIBLE-BEARER
    exists within DETERMINATE-DOMAIN
```

For dhyāna-born restraint:

```text
DHYANA-BORN-RESTRAINT
    GENERATED-BY dhyāna
    REQUIRES capacity-for-dhyāna
    OCCURS-IN eligible human-or-divine continuum
```

For uncontaminated restraint:

```text
UNCONTAMINATED-RESTRAINT
    GENERATED-BY noble-path
    REQUIRES path-capable cognition
    OCCURS-IN eligible continuums across the domains
```

The governing principle is:

```text
the range of a karmic form
is determined by the range of its generative ground
```

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix karma: <http://127.0.0.1:3000/karma#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix path: <http://127.0.0.1:3000/path#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_44
    a vak:Karika ;
    rdfs:label "VAK 4.44" ;
    vak:continues vak:VAK_4_43 ;
    vak:hasTopic karma:DistributionOfMeditativeRestraint ;
    vak:hasTopic karma:DistributionOfUncontaminatedRestraint .

karma:DhyanaBornRestraint
    a karma:Restraint ;
    karma:generatedBy karma:Dhyana ;
    karma:possibleFor loka:EligibleHuman ;
    karma:possibleFor loka:EligibleDesireDomainDeity ;
    karma:possibleFor loka:EligibleFormDomainDeity .

karma:UncontaminatedRestraint
    a karma:Restraint ;
    karma:generatedBy path:NoblePath ;
    karma:possibleFor loka:EligibleHuman ;
    karma:possibleFor loka:EligibleDeity ;
    karma:possibleFor loka:EligibleFormlessBeing .

loka:NonPercipientBeing
    karma:ineligibleFor karma:UncontaminatedRestraint .
```

## Determinate result

VAkK 4.44 establishes:

```text
dhyāna-born restraint
    follows the possibility of dhyāna

uncontaminated restraint
    follows the possibility of the noble path
```

Realm alone does not generate restraint. The decisive factor is the cognition or path capable of producing it.
