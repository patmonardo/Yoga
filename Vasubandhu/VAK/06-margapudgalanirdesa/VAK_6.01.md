# VAK 6.01

## Sanskrit

### Devanāgarī

क्लेशप्रहाणमाख्यातं सत्यदर्शनभावनात् ।
द्विविधो भावनामार्गो दर्शनाख्यस्त्वनास्रवः ॥ ६.१ ॥

### IAST

kleśa-prahāṇam ākhyātaṃ satya-darśana-bhāvanāt |
dvividho bhāvanā-mārgo darśanākhyas tv anāsravaḥ || 6.1 ||

## Padaccheda

| Pada | Form | Determination |
|---|---|---|
| kleśa-prahāṇam | nominative singular neuter compound | abandonment of the afflictive determinations |
| ākhyātam | nominative singular neuter past passive participle of ā-√khyā | has been declared or explained |
| satya-darśana-bhāvanāt | ablative singular compound | through seeing the truths and through cultivation |
| dvi-vidhaḥ | nominative singular masculine | twofold |
| bhāvanā-mārgaḥ | nominative singular masculine | Path of Cultivation |
| darśana-ākhyaḥ | nominative singular masculine | that which is called the Path of Seeing |
| tu | adversative particle | but; whereas |
| anāsravaḥ | nominative singular masculine | without influx; uncontaminated |

## Grammar

The opening statement is complete and retrospective:

```text
kleśa-prahāṇam ākhyātam
    the abandonment of the kleśas has been explained
```

It points back to the Anuśayanirdeśa, where the classes of affliction and their modes of abandonment were determined.

The ablative compound **satya-darśana-bhāvanāt** gives the means through which abandonment occurs:

```text
satya-darśana
    seeing of the truths

bhāvanā
    cultivation
```

The second half establishes an asymmetry:

```text
bhāvanā-mārga
    twofold

darśana-mārga
    necessarily anāsrava
```

The verse therefore does not merely divide the Path into seeing and practice. It distinguishes originary seeing from the continued cultivation that follows and extends it.

## Literal Translation

The abandonment of the afflictions has been explained as occurring through seeing the truths and through cultivation. The Path of Cultivation is twofold, whereas that called the Path of Seeing is uncontaminated.

## Philosophical Translation

The abandonment of afflictive determinations has already been established as proceeding through the seeing of truth and through cultivated realization. Cultivation may take two forms; the Path named Seeing, however, is intrinsically free from influx.

## Technical Vocabulary

### kleśa

**Kleśa** is an afflictive determination. It is not merely an emotion or psychological disturbance, but a determination that conditions appropriation, action, and continued becoming.

### prahāṇa

**Prahāṇa** is abandonment: the accomplished separation from an afflictive determination. It is not merely temporary suppression.

### satya-darśana

**Satya-darśana** is the seeing of the truths. Here **darśana** is not passive reception of doctrine. It is direct discriminative seeing of what had not previously been seen.

### bhāvanā

**Bhāvanā** is cultivation, development, or repeated actualization. It is not restricted to meditation in a narrow modern sense. It is the bringing into actuality and continued formation of the Path after truth has been seen.

### mārga

**Mārga** is Path: a determinate sequence of knowing and transformation capable of functioning as the counterforce to kleśa.

### anāsrava

**Anāsrava** means without influx. The conventional translation **uncontaminated** may be retained, but the literal force remains important:

```text
that into which the āsravas do not flow
```

## Analysis

Chapter 5 established the afflictive field. Chapter 6 now asks by what Path that field is abandoned.

```text
Chapter 5
    determination of kleśa and abandonment

Chapter 6
    determination of the Path and the person of the Path
```

The first result is that not every cultivation is automatically uncontaminated. Bhāvanā is twofold, while the Path of Seeing is necessarily anāsrava.

This gives the foundational sequence:

```text
kleśa
    ↓
truth is seen
    ↓
the seen truth is cultivated
    ↓
abandonment is completed
```

Darśana concerns the first direct discrimination of truth. Bhāvanā concerns the continued actualization of what has been seen throughout the field of practice.

The verse therefore distinguishes:

```text
originary discrimination
    from
continued actualization
```

Knowing becomes Path only when its determinate form has the power to abandon a determinate obstruction.

## Logical Determination

The Path is first divided as:

```text
Mārga
├── Darśana-mārga
└── Bhāvanā-mārga
```

But the division is not symmetrical:

```text
Darśana-mārga
    necessarily anāsrava

Bhāvanā-mārga
    twofold
```

The higher Idea incarnated by this division is **kleśa-prahāṇa**:

```text
Kleśa-prahāṇa
    ↓
Darśana
    ↔
Bhāvanā
```

Darśana and bhāvanā are not two independent paths externally combined. They are two differentiated functions through which abandonment becomes actual.

## Interpretive Note

The architecture here differs from any account in which knowledge is exhausted by scriptural testimony concerning an absolute object.

The Kośa asks a functional question:

```text
What kind of knowing
abandons which determinate kleśa?
```

A determinate Path of Knowing requires:

```text
specific cognition
+ specific object
+ specific counteraction
+ specific abandonment
+ specific resulting person
```

This is why the chapter is Mārgapudgalanirdeśa. The Path cannot remain an abstract means; it becomes the determination of the person who embodies it.

## Organon Note

```text
Kleśa
    conditioned obstruction

Darśana
    discriminative breakthrough

Bhāvanā
    concrete actualization

Prahāṇa
    accomplished separation
```

The verse supplies the first architecture for the Path as a transformation of knowing into actuality.

## OWL++ Seed

```text
Class: Klesa
Class: KlesaPrahanam
Class: Marga
Class: DarsanaMarga
Class: BhavanaMarga
Class: AnasravaMarga

DarsanaMarga SubClassOf Marga
BhavanaMarga SubClassOf Marga
AnasravaMarga SubClassOf Marga
DarsanaMarga SubClassOf AnasravaMarga

ObjectProperty: abandonsKlesa
    Domain: Marga
    Range: Klesa

ObjectProperty: actualizesPrahanam
    Domain: Marga
    Range: KlesaPrahanam

Individual: VAK_6_01
    Types: Karika
    Facts:
        establishes DarsanaMarga
        establishes BhavanaMarga
        establishes KlesaPrahanam
```

## Commit Note

```text
Add VAK 6.01 path analysis
```
