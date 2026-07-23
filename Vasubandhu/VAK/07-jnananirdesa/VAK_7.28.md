# VAK_7.28 — The Buddha’s Distinctive Qualities and the First Two Powers

## Sanskrit

### Devanāgarī

```text
अष्टादशावेणिकास्तु बुद्धधर्मा बलादयः ।
स्थानास्थाने दश ज्ञानानि अष्टौ कर्मफले नव ॥ ७.२८ ॥
```

### IAST

```text
aṣṭādaśāveṇikāstu buddhadharmā balādayaḥ /
sthānāsthāne daśa jñānāni aṣṭau karmaphale nava // VAK_7.28 //
```

## Source Caution

This verse opens a new sub-block. The subject is no longer cultivation in general but the Buddha’s distinctive qualities as constituted by knowledges.

The final word *nava* carries forward into VAK 7.29. Thus VAK 7.28 itself gives two completed counts:

```text
power concerning what is possible and impossible
    ten knowledges

power concerning karmic result
    eight knowledges
```

The number nine begins the next set of powers explained in VAK 7.29.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| aṣṭādaśa | numeral | eighteen |
| āveṇikāḥ | nominative plural | distinctive, unshared |
| tu | particle | now, however |
| buddha-dharmāḥ | nominative plural compound | qualities or dharmas of a Buddha |
| bala-ādayaḥ | nominative plural | the powers and the remaining groups |
| sthāna-asthāne | locative singular compound | in knowledge of the possible and impossible |
| daśa jñānāni | nominative plural | ten knowledges |
| aṣṭau | numeral | eight |
| karma-phale | locative singular | in karmic result |
| nava | numeral | nine; carried into the next verse |

## Literal Translation

The qualities distinctive to a Buddha are eighteen, beginning with the powers. In the power concerning what is possible and impossible there are ten knowledges; in the power concerning karmic result there are eight. Nine [in the powers taken up next].

## Philosophical Translation

The Buddha’s distinctive capacities are not presented as mysterious additions to knowledge. They are highly organized powers constituted by definite ranges of knowing. The first power employs all ten knowledges to determine what can and cannot occur. The second employs eight knowledges to determine the lawful results of action.

## Technical Vocabulary

### āveṇika-buddha-dharma

```text
āveṇika
    distinctive
    unshared

buddha-dharma
    quality belonging specifically to a Buddha
```

The traditional eighteen are:

```text
ten powers
four fearlessnesses
three establishments of mindfulness
great compassion
```

### bala

```text
bala
    power
    strength
    unobstructed cognitive capacity
```

Here a power is not mere force. It is a stable and unobstructed competence to know a definite field.

### sthāna-asthāna

```text
sthāna
    what is possible
    what can stand under the conditions

asthāna
    what is impossible
    what cannot occur under those conditions
```

This first power determines lawful possibility and impossibility.

### karma-phala

```text
karma
    action

phala
    result
    maturation
```

This second power determines the results of actions according to their conditions.

## Doctrinal Determination

### The eighteen distinctive qualities

The verse introduces a new architecture:

```text
Buddha’s distinctive qualities
    ten powers
    four fearlessnesses
    three mindfulness establishments
    great compassion
```

The immediate focus is the ten powers.

### First power: possible and impossible

```text
sthāna-asthāna-bala
    constituted by all ten knowledges
```

Because this power concerns the complete determination of what can and cannot occur, no one of the ten knowledges is excluded.

### Second power: karmic result

```text
karma-phala-bala
    constituted by eight knowledges
```

The knowledges of extinction and of the Path are excluded because this power concerns the maturation of action rather than liberation as such.

## Logical Determination

The verse defines power as a structured range of cognition.

```text
power
    not an extra faculty added to knowledge

power
    knowledge rendered complete
    stable
    unobstructed
    and domain-specific
```

The first two domains are:

```text
modal domain
    what is possible or impossible

causal domain
    what result follows from action
```

The Buddha’s power is therefore not arbitrary omnipotence. It is exact knowledge of lawful possibility and lawful consequence.

## Organon Light

```text
cultivation
    organizes the dialectical copula

power
    is that organization made stable
    unobstructed
    and fully available
```

The first power knows whether a determination can stand.

The second knows what follows when it does.

That is the basic movement:

```text
possibility
    → consequence
```

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix buddha: <http://127.0.0.1:3000/buddha#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_28
    a vak:Karika ;
    rdfs:label "VAK 7.28" ;
    vak:determines buddha:EighteenDistinctiveQualities,
                   buddha:PossibleImpossiblePower,
                   buddha:KarmicResultPower .

buddha:EighteenDistinctiveQualities
    a buddha:BuddhaQualitySet ;
    buddha:includes buddha:TenPowers,
                    buddha:FourFearlessnesses,
                    buddha:ThreeMindfulnessEstablishments,
                    buddha:GreatCompassion .

buddha:PossibleImpossiblePower
    a buddha:KnowledgePower ;
    jna:constitutedBy jna:TenKnowledges .

buddha:KarmicResultPower
    a buddha:KnowledgePower ;
    jna:constitutedBy jna:EightKnowledges .
```

## Commit History

```text
2026-07-23 — Initial kārikā-pass analysis for VAK_7b.
```
