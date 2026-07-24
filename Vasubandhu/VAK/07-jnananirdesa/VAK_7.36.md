# VAK_7.36 — Freedom from Conflict

## Sanskrit

### Devanāgarī

```text
संवृतिज्ञानमरणा ध्यानेऽन्त्येऽकोप्यधर्मणः ।
नृजा अनुत्पन्नकामाप्तसवस्तुक्लेशगोचराः ॥ ७.३६ ॥
```

### IAST

```text
saṃvṛtijñānam araṇā dhyāne 'ntye 'kopyadharmaṇaḥ /
nṛjā anutpanna-kāmāpta-savastuka-kleśa-gocarāḥ // VAK_7.36 //
```

## Source Caution

The second line is highly compressed. On the first kārikā pass, the safest reading is that araṇā is conventional knowledge, belongs to an immovable arhat, is based on the final dhyāna, arises in a human continuum, and takes as its field unarisen desire-domain afflictions connected with determinate objects.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| saṃvṛti-jñānam | nominative singular neuter | conventional knowledge |
| araṇā | nominative singular feminine | freedom from conflict |
| dhyāne antye | locative singular | in the final dhyāna |
| akopya-dharmaṇaḥ | genitive singular | belonging to one of immovable disposition |
| nṛ-jā | nominative singular feminine | produced in a human continuum |
| anutpanna | compound member | not yet arisen |
| kāma-āpta | compound member | belonging to the desire domain |
| sa-vastuka | compound member | possessing a determinate object-basis |
| kleśa-gocarā | nominative singular feminine | having afflictions as its object-field |

## Literal Translation

Freedom from conflict is conventional knowledge. It belongs to one of immovable disposition, is based on the final dhyāna, is produced among humans, and has as its object-field unarisen, object-based afflictions belonging to the desire domain.

## Philosophical Translation

Freedom from conflict is a conventional mode of knowing cultivated by an immovable arhat on the basis of the highest dhyāna. It anticipates the desire-domain afflictions that might arise in others in relation to particular objects, enabling the practitioner to avoid becoming the occasion for their arising.

## Technical Vocabulary

### araṇā

```text
araṇā
    freedom from conflict
    absence of contention
    knowledge preventing afflictive reaction
```

Araṇā is not merely the absence of hostility in oneself. It is a cultivated cognitive capacity by which one knows which words, appearances, situations, or actions might provoke affliction in another and avoids supplying that condition.

### saṃvṛti-jñāna

Araṇā is conventional knowledge because it concerns persons, situations, objects, and possible conditioned reactions. Conventional does not mean false; it identifies the level at which the knowledge operates.

### akopya-dharman

```text
akopya-dharman
    one whose liberation is immovable
    one not liable to regression
```

### antya-dhyāna

```text
antya-dhyāna
    final dhyāna
    fourth dhyāna
```

The fourth dhyāna supplies the stability required for precise anticipatory knowledge.

### anutpanna-kleśa

```text
anutpanna-kleśa
    an affliction not yet arisen
```

Araṇā is therefore preventive rather than merely corrective.

### savastuka

```text
sa-vastuka
    possessing a determinate object-basis
```

The affliction is anticipated as arising in dependence upon a concrete object or circumstance.

## Doctrinal Determination

Araṇā is a specialized knowledge with strict limits:

```text
type
    conventional knowledge

bearer
    immovable arhat

basis
    fourth dhyāna

place of production
    human continuum

object-field
    unarisen desire-domain afflictions
    connected with determinate objects
```

## Logical Determination

Araṇā knows a grounded possibility rather than an already actual conflict:

```text
determinate disposition
    +
determinate object
    +
determinate encounter
        ↓
possible kleśa
```

The practitioner alters conduct before the affliction becomes actual.

```text
Ground
    dispositions and conditions

Possibility
    unarisen affliction

Preventive determination
    transformed conduct

Result
    non-arising of conflict
```

## Organon Interpretation

Freedom from conflict is knowledge becoming ethical activity without ceasing to be knowledge:

```text
cognition
    anticipates another's possible reaction

judgment
    determines the relevant conditions

action
    refuses to produce the conflict
```

> Freedom from conflict is knowledge of the conditions under which harm would arise, joined to the power not to actualize them.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix path: <http://127.0.0.1:3000/path#> .
@prefix agent: <http://127.0.0.1:3000/agent#> .
@prefix dharma: <http://127.0.0.1:3000/dharma#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_36
    a vak:Karika ;
    rdfs:label "VAK 7.36" ;
    vak:determines path:Arana .

path:Arana
    a jna:ConventionalKnowledge ;
    rdfs:label "Freedom from conflict" ;
    path:hasBearer agent:ImmovableArhat ;
    path:hasBasis path:FourthDhyana ;
    path:isProducedIn agent:HumanContinuum ;
    jna:hasObjectField dharma:UnarisenDesireDomainAffliction ;
    path:hasFunction path:PreventAfflictionArising .
```

## Commit History

```text
2026-07-24 — Initial kārikā-pass analysis for VAK_7c.
```