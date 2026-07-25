# VAK_7.15 — The Supports of the Knowledges

## Sanskrit

### Devanāgarī

```text
ध्यानेष्वन्यमनोज्ञानं कामरूपाश्रयं च तत् ।
कामाश्रयं तु धर्माख्यमन्यत्त्रैधातुकाश्रयम् ॥ ७.१५ ॥
```

### IAST

```text
dhyāneṣv anya-mano-jñānaṃ kāma-rūpāśrayaṃ ca tat /
kāmāśrayaṃ tu dharmākhyam anyat traidhātukāśrayam // VAK_7.15 //
```

## Source Caution

The verse continues the specification of the ten knowledges through their `āśraya`, their supporting or originating sphere. The compact syntax distinguishes:

```text
where a knowledge is supported or produced
    from
what that knowledge may take as its object
```

The first pāda states that knowledge of another mind is based in the meditative absorptions. The following phrase states that the minds apprehended by it belong to the desire and form realms. The exact commentarial distribution should be revisited in a deeper pass, but the primary structural distinction is clear.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| dhyāneṣu | locative plural | in the meditative absorptions |
| anya-mano-jñānam | nominative singular neuter | knowledge of another mind |
| kāma-rūpa-āśrayam | nominative singular neuter | having the desire and form realms as its support or range |
| ca | indeclinable | and |
| tat | nominative singular neuter | that |
| kāma-āśrayam | nominative singular neuter | supported in the desire realm |
| tu | indeclinable | but; whereas |
| dharma-ākhyam | nominative singular neuter | that called dharma-knowledge |
| anyat | nominative singular neuter | the rest; the other |
| trai-dhātuka-āśrayam | nominative singular neuter | supported throughout the three realms |

## Grammar

The verse distributes the knowledges according to their support:

```text
paracittajñāna
    based in the dhyānas
    concerned with minds of kāma and rūpa

dharmajñāna
    based in kāmadhātu

remaining knowledges
    based throughout the three realms
```

`āśraya` is the governing technical term. It indicates the basis, sphere, or locus upon which a cognition depends. The same word must not automatically be flattened into a single English equivalent in every clause; its function is determined by the relation being specified.

## Literal Translation

Knowledge of another mind is in the meditative absorptions, and it has the desire and form realms as its support. That called dharma-knowledge has the desire realm as its support; the rest have the three realms as their support.

## Philosophical Translation

Knowledge is further differentiated by the sphere upon which it depends. Knowledge of another mind arises through the absorptions and reaches minds belonging to the desire and form realms. Dharma-knowledge is rooted in the desire realm, whereas the remaining knowledges may be supported across all three realms.

## Technical Vocabulary

### āśraya

```text
āśraya
    = support
    = basis of occurrence
    = sphere upon which cognition depends
```

The verse does not treat cognition as an unconditioned faculty. Every knowledge has a determinate support.

### dhyāna

```text
dhyāna
    = meditative absorption
    = cultivated cognitive support
```

Knowledge of another mind is not presented as spontaneous omniscience. It depends upon a specific meditative basis.

### traidhātuka

```text
traidhātuka
    = belonging to the three realms
    = desire, form, and formless spheres
```

The term states the maximum cosmological range of support for the remaining knowledges.

## Doctrinal Determination

The verse distinguishes three support-structures.

| Knowledge | Supporting sphere |
|---|---|
| knowledge of another mind | the meditative absorptions; directed toward minds of desire and form |
| dharma-knowledge | desire realm |
| the remaining knowledges | all three realms |

The crucial point is dependence:

```text
knowledge
    is not merely named by its object

knowledge
    is also determined by the basis
    from which it can arise
```

This continues the grounding program announced in VAK 7.08. The knowledges are differentiated by determinate conditions rather than by a flat list of names.

## Logical Determination

VAK 7.15 specifies cognition through an Essential Relation:

```text
knowledge
    / supported-by /
realm or meditative basis
```

A cognition does not act as a bare one over an undifferentiated many. Its efficacy requires a determinate support through which its range becomes possible.

The verse therefore separates:

```text
originating support
    where cognition is established

object-range
    what cognition can reach
```

That distinction is particularly important for knowledge of another mind. Its meditative basis and its object-domain are related but not identical.

## Organon Light

The verse remains entirely within disciplined Reflection. It asks of each knowledge:

```text
There—upon what does it rest?
```

The answer is given through `āśraya`:

```text
paracittajñāna
    rests upon dhyāna

dharmajñāna
    rests upon kāmadhātu

other knowledges
    may rest upon the three realms
```

This supports the provisional project insight that an impure or conditioned dharma cannot function as bare immediacy. It must pass through determinate relations of support, sphere, and range before it can act.

But no genetic derivation is imposed here. The Kośa is still specifying the reflected architecture of knowledge by identifying the determinate `there` of each cognition.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix realm: <http://127.0.0.1:3000/realm#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_15
    a vak:Karika ;
    rdfs:label "VAK 7.15" ;
    vak:determines jna:KnowledgeSupport,
                   jna:OtherMindKnowledgeSupport,
                   jna:DharmaKnowledgeSupport,
                   jna:ThreeRealmKnowledgeSupport .

jna:OtherMindKnowledge
    jna:isSupportedBy jna:Dhyana ;
    jna:hasObjectRealm realm:DesireRealm,
                       realm:FormRealm .

jna:DharmaKnowledge
    jna:isSupportedBy realm:DesireRealm .

jna:RemainingKnowledges
    jna:isSupportedBy realm:ThreeRealms .
```

## Commit History

```text
2026-07-23 — Initial kārikā-pass analysis.
```
