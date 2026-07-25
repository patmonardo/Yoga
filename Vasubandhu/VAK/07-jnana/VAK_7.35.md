# VAK_7.35 — Qualities Shared with Disciples and Ordinary Persons

## Sanskrit

### Devanāgarī

```text
शिष्यसाधारणा अन्ये धर्माः केचित् पृथग्जनैः ।
अरणाप्रणिधिज्ञानप्रतिसंविद्गुणादयः ॥ ७.३५ ॥
```

### IAST

```text
śiṣya-sādhāraṇā anye dharmāḥ kecit pṛthagjanaiḥ /
araṇā-praṇidhi-jñāna-pratisaṃvid-guṇādayaḥ // VAK_7.35 //
```

## Padaccheda

```text
śiṣya-sādhāraṇāḥ
anye
dharmāḥ
kecit
pṛthagjanaiḥ
araṇā
praṇidhi-jñāna
pratisaṃvid
guṇa-ādayaḥ
```

| Pada | Grammar | Working sense |
|---|---|---|
| śiṣya-sādhāraṇāḥ | nominative plural masculine | shared with disciples |
| anye | nominative plural masculine | other |
| dharmāḥ | nominative plural masculine | qualities, determinations |
| kecit | nominative plural masculine | certain, some |
| pṛthagjanaiḥ | instrumental plural | with ordinary persons |
| araṇā | compound member | freedom from conflict |
| praṇidhi-jñāna | compound member | knowledge arising from resolve |
| pratisaṃvid | compound member | discriminating knowledge, analytical mastery |
| guṇa-ādayaḥ | nominative plural | qualities beginning with these |

## Grammar

The first line gives two levels of commonality:

```text
anye dharmāḥ
    other qualities

śiṣya-sādhāraṇāḥ
    are shared with disciples

kecit pṛthagjanaiḥ
    and some are shared with ordinary persons
```

The second line begins the enumeration:

```text
araṇā
praṇidhi-jñāna
pratisaṃvid
guṇa-ādayaḥ
```

The final `-ādayaḥ` indicates qualities beginning with freedom from conflict, knowledge of resolve, and discriminating knowledges.

## Literal Translation

Other qualities are shared with disciples, and some with ordinary persons—qualities beginning with freedom from conflict, knowledge arising from resolve, and the discriminating knowledges.

## Philosophical Translation

Beyond the qualities exclusive to Buddhas, there are further excellences that may also be attained by disciples, while some are accessible even to ordinary persons. These include freedom from producing conflict, knowledge governed by a deliberate resolve, the discriminating knowledges, and related capacities.

## Technical Vocabulary

### śiṣya

```text
śiṣya
    disciple
    one instructed within the Buddha’s path
```

### sādhāraṇa

```text
sādhāraṇa
    common
    shared
    belonging to more than one bearer
```

A quality may be extremely refined while still being non-exclusive.

### pṛthagjana

```text
pṛthag-jana
    ordinary person
    one not established in the noble path
```

### araṇā

```text
a-raṇa
    absence of conflict
    absence of contention
```

Here it indicates a cultivated capacity by which an accomplished practitioner avoids becoming an occasion for the afflictions of others.

### praṇidhi-jñāna

```text
praṇidhi
    resolve
    deliberate determination
    directed aspiration

jñāna
    knowledge
```

Thus `praṇidhi-jñāna` is knowledge arising according to a resolve.

### pratisaṃvid

```text
pratisaṃvid
    discriminating mastery
    precise and unobstructed knowledge
    of a determinate domain
```

The following verses specify four forms concerning dharma, artha, nirukti, and pratibhāna.

## Doctrinal Determination

The previous verses established qualities exclusive to Buddhas. VAK 7.35 opens a new class: excellent qualities that do not define Buddhahood exclusively.

```text
ordinary person
    may possess certain cultivated capacities

disciple
    may possess more advanced qualities

Buddha
    possesses shared qualities
    and qualities uniquely perfected or exclusive
```

The distinction is therefore one of range, degree, purity, completeness, and exclusivity rather than wholly different kinds of rational being.

## Logical Determination

The verse distinguishes possession from exclusive possession.

```text
X possesses quality Q
```

does not entail:

```text
only X can possess quality Q
```

The same determination may occur in Buddha, disciple, and ordinary person in different degrees of actualization.

## Organon Interpretation

The verse establishes continuity across levels of rational development.

```text
7.34
    equality within Buddhahood

7.35
    continuity across levels of rational development
```

The difference between human and Buddha is not an absolute difference of rational kind, but a difference in range, purity, completion, and actualized power.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix path: <http://127.0.0.1:3000/path#> .
@prefix agent: <http://127.0.0.1:3000/agent#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_35
    a vak:Karika ;
    rdfs:label "VAK 7.35" ;
    vak:determines path:SharedExcellentQualities ;
    vak:introduces path:Arana,
                   jna:ResolutionKnowledge,
                   jna:DiscriminatingMastery .

path:SharedExcellentQualities
    path:mayBePossessedBy agent:Buddha,
                          agent:Disciple ;
    path:someMayBePossessedBy agent:OrdinaryPerson .

path:Arana
    a path:CultivatedQuality ;
    rdfs:label "Freedom from conflict" .

jna:ResolutionKnowledge
    a jna:Knowledge ;
    jna:conditionedBy jna:DeterminateResolve .

jna:DiscriminatingMastery
    a jna:KnowledgeCapacity ;
    path:hasBearer agent:Buddha,
                   agent:Disciple .
```

## Commit History

```text
2026-07-24 — Initial kārikā-pass analysis for VAK_7c.
```
