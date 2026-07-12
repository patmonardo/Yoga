# VAkK 4.52

## Sanskrit

### Devanāgarī

> यद्विरक्तः स्थिरो बालस्तत्र नोत्पद्यवेद्यकृत् ।  
> नान्यवेद्यकृदप्यार्यः कामेऽग्रे वा स्थिरोऽपि न ॥ ४.५२ ॥

### IAST

> **yadviraktaḥ sthiro bālas tatra notpadyavedyakṛt |**  
> **nānyavedyakṛd apy āryaḥ kāme ’gre vā sthiro ’pi na || 4.52 ||**

## Padaccheda

```text
yat-viraktaḥ
sthiraḥ
bālaḥ

tatra
na
utpadya-vedya-kṛt

na
anya-vedya-kṛt
api
āryaḥ

kāme
agre
vā

sthiraḥ
api
na
```

## Literal translation

> **A stable ordinary person, when detached from a given level, does not produce there karma to be experienced in the next rebirth. Nor does a noble person produce karma to be experienced in another existence; nor does a stable person in the desire-domain or at the summit.**

The exact scope of **anya-vedya** and the final pāda remains to be fixed in the Bhāṣya pass.

## Doctrinal determination

The verse restricts the production of temporally fixed karma according to the spiritual condition of the agent.

```text
stable detachment from level X
    → no new next-birth-projecting karma for X
```

The claim concerns newly produced karma, not necessarily every previously accumulated karmic determination.

```text
cannot newly produce X
    ≠
old X has already been destroyed
```

A stable ordinary person has lost the practical capacity to project immediate rebirth into the level from which they are detached. The noble person has a still narrower future rebirth-range and therefore cannot produce certain remote-maturation karmas whose result would require an existential sequence already closed by the path.

The verse also names the two boundary positions:

```text
kāma
    desire-domain

agra
    summit of conditioned existence, bhavāgra
```

These carry special restrictions because they are the lower and upper limits of the conditioned domain-structure.

## Technical vocabulary

```text
virakta
    detached from a domain or level

sthira
    stable, firm, non-retrogressing in that detachment

bāla
    ordinary, non-noble person

ārya
    noble person who has entered the path

utpadya-vedya
    karma to be experienced in the immediately following rebirth

anya-vedya
    another or later temporally experienced karma
```

## Logical determination

```text
KARMA-PRODUCTION
    depends upon
        agent-status
        detachment-level
        stability
        target-domain
        maturation-time
```

```text
IF
    agent = ordinary
    detachment-from(X) = stable
THEN
    produce(next-birth-karma-for-X) = false
```

The causal capacity of an agent is therefore not invariant. Advancement on the path changes the range of karmas the continuum can newly produce.

## Logic of Experience

```text
[ AGENT
  PATH-STATUS ordinary
  DETACHED-FROM level-X
  DETACHMENT-STABILITY stable
  KARMA-PRODUCTION
      [ NEXT-BIRTH-FOR level-X prohibited ] ]
```

```text
[ AGENT
  PATH-STATUS noble
  FUTURE-REBIRTH-RANGE contracted
  KARMA-PRODUCTION
      [ REMOTE-MATURATION restricted ] ]
```

## Organon interpretation

A transformed ground changes the range of possible functions.

```text
before detachment
    future rebirth X is projectible

after stable detachment
    future rebirth X is no longer projectible
```

Thus:

```text
AGENT-STATE
    determines
AVAILABLE-KARMIC-OPERATIONS
    determines
POSSIBLE-FUTURE-WORLDS
```

The path progressively contracts the samsaric projection-space.

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix karma: <http://127.0.0.1:3000/karma#> .
@prefix path: <http://127.0.0.1:3000/path#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix doctrine: <http://127.0.0.1:3000/doctrine#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_52
    a vak:Karika ;
    rdfs:label "VAK 4.52" ;
    vak:continues vak:VAK_4_51 ;
    vak:hasTopic karma:AgentRelativeKarmaProduction ;
    vak:hasTopic path:DetachmentConstraint .

path:StableDetachment
    karma:prohibitsProductionOf
        karma:NextBirthKarmaForDetachedLevel .

path:NoblePerson
    karma:hasRestrictedProductionOf
        karma:LaterLifeMaturationKarma .

loka:DesireDomain
    a loka:BoundaryDomain .

loka:SummitOfExistence
    a loka:BoundaryDomain ;
    rdfs:label "bhavāgra" .

doctrine:VAK_4_52_AnyaVedya
    doctrine:status doctrine:RequiresBhashyaReview .
```

## Determinate result

VAkK 4.52 establishes that stable detachment and noble path-status contract the range of karmas—and therefore the range of future rebirth-worlds—that the continuum can still project.