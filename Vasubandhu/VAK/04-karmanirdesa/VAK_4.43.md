# VAkK 4.43

## Sanskrit

### Devanāgarī

> नॄणामसंवरो हित्वा षण्ढपण्डद्विधाकृतीन् ।  
> कुरूंश्च संवरोऽप्येवं देवानां च नॄणां त्रयः ॥ ४.४३ ॥

### IAST

> **nṛṇām asaṃvaro hitvā śaṇḍha-paṇḍa-dvidhākṛtīn |**  
> **kurūṃś ca saṃvaro ’py evaṃ devānāṃ ca nṛṇāṃ trayaḥ || 4.43 ||**

## Padaccheda

```text
nṛṇām
asaṃvaraḥ
hitvā
śaṇḍha-paṇḍa-dvidhākṛtīn
kurūn
ca |

saṃvaraḥ
api
evam |

devānām
ca
nṛṇām
trayaḥ ||
```

Syntactically expanded:

```text
nṛṇām asaṃvaraḥ,
śaṇḍha-paṇḍa-dvidhākṛtīn kurūṃś ca hitvā;

saṃvaraḥ api evam;

devānāṃ ca nṛṇāṃ trayaḥ.
```

## Grammar

- **nṛṇām** — genitive plural of *nṛ*: among human beings.
- **asaṃvaraḥ** — nominative singular: non-restraint.
- **hitvā** — absolutive of √*hā*: having left aside, excepting.
- **śaṇḍha-paṇḍa-dvidhākṛtīn** — accusative plural enumeration governed by *hitvā*.
- **kurūn** — accusative plural: the Kurus, here the inhabitants of Uttarakuru.
- **saṃvaraḥ api evam** — restraint also in the same way.
- **devānāṃ ca nṛṇāṃ trayaḥ** — the three among gods and humans; the exact distribution continues in VAkK 4.44.

The existential relation is elliptical:

```text
asaṃvaraḥ asti
saṃvaraḥ api asti
```

## Literal translation

> **Among human beings there is non-restraint, excluding the śaṇḍhas, paṇḍakas, those of twofold constitution, and the Kurus. Restraint is likewise. Among gods and human beings are the three.**

The final phrase is deliberately compressed. Its distribution is completed by VAkK 4.44.

## Technical vocabulary

### asaṃvara

```text
a-saṃvara
    non-restraint
```

Here **asaṃvara** is not merely the absence of restraint. It is a positively acquired unwholesome continuity supported by avijñapti.

```text
asaṃvara
    ≠ simple lack of discipline

asaṃvara
    = acquired continuity of non-restraint
```

### saṃvara

```text
sam-√vṛ
    to enclose
    to restrain
    to hold together
```

A **saṃvara** is a determinate restraint regulating the continuum of action. The three already established are:

```text
prātimokṣa-saṃvara
    restraint grounded in undertaken discipline

dhyānaja-saṃvara
    restraint born from meditative absorption

anāsrava-saṃvara
    uncontaminated restraint belonging to the noble path
```

### dvidhākṛti

```text
dvidhā
    twofold

kṛti
    formation or constitution
```

Thus **dvidhākṛti** designates one whose bodily constitution is twofold. The inherited doctrinal category should be preserved rather than forced into a modern identity category.

### Kuru

Here **Kurus** means the inhabitants of Uttarakuru. Within Kośa cosmology, their mode of life does not support the specific acquisition of restraint or non-restraint classified here.

## Doctrinal determination

VAkK 4.43 concerns eligibility for acquisition:

```text
In which kinds of embodied continuum
can these karmic determinations occur?
```

The answer begins:

```text
asaṃvara
    belongs to the human domain,
    but not universally to every human embodiment
```

The same restriction applies to the relevant restraint, most immediately prātimokṣa restraint, since this is acquired through conventional undertaking and communicative reception.

The verse does not claim that the excluded beings cannot perform wholesome or unwholesome acts. It claims that they do not acquire these specific enduring structures of restraint or non-restraint.

```text
isolated action
    ≠
acquired standing karmic form
```

The final **trayaḥ** points to the three restraints, but their complete realm-distribution belongs to VAkK 4.44.

## Philosophical translation

> **Non-restraint occurs within the human domain, except among the śaṇḍhas, paṇḍakas, persons of twofold bodily constitution, and the inhabitants of Uttarakuru. The corresponding restriction applies to restraint. The three forms of restraint are distributed among gods and humans, as specified in the following verse.**

The verse concerns the domains in which determinate ethical dispositions can be acquired, not merely the attribution of moral predicates to classes of beings.

## Logic of Experience

The verse determines the subject-domain of a karmic form:

```text
determination
    asaṃvara / saṃvara

domain
    human continuum

restriction
    excluded configurations and Uttarakuru

further distribution
    gods and humans in relation to the three restraints
```

A karmic determination does not exist abstractly. It requires:

```text
an appropriate bearer
an appropriate domain
conditions of acquisition
```

Thus the verse moves from the internal definition of restraint to its concrete distribution.

## Organon interpretation

Ethical form requires a suitable field of actualization. Restraint and non-restraint are acquired, sustained, and lost only under determinate existential conditions.

```text
universal determination
    saṃvara / asaṃvara

particular eligibility
    a specified class of living continuum

singular actuality
    acquired avijñapti in that continuum
```

The Triple here is not transcendental. It is the concrete distribution of a higher karmic determination through eligible forms of existence.

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix karma: <http://127.0.0.1:3000/karma#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_43
    a vak:Karika ;
    rdfs:label "VAK 4.43" ;
    vak:continues vak:VAK_4_42 ;
    vak:continuedBy vak:VAK_4_44 ;
    vak:hasTopic karma:EligibilityForRestraint ;
    vak:hasTopic karma:EligibilityForNonRestraint .

karma:Asamvara
    a karma:AcquiredKarmicContinuity ;
    karma:possibleIn loka:HumanDomain ;
    karma:excludesBearer loka:Shandha ;
    karma:excludesBearer loka:Pandaka ;
    karma:excludesBearer loka:Dvidhakriti ;
    karma:excludesBearer loka:UttarakuruBeing .

karma:Samvara
    a karma:KarmicRestraint .

karma:PratimokshaSamvara
    rdfs:subClassOf karma:Samvara .

karma:DhyanaBornSamvara
    rdfs:subClassOf karma:Samvara .

karma:UncontaminatedSamvara
    rdfs:subClassOf karma:Samvara .
```

## Determinate result

VAkK 4.43 establishes:

```text
restraint and non-restraint
    are not abstractly attributable

rather
    they require an eligible embodied continuum
```

The verse opens the distribution problem whose full determination continues in VAkK 4.44.
