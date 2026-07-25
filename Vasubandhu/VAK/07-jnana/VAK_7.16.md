# VAK_7.16 — Knowledges and the Four Applications of Mindfulness

## Sanskrit

### Devanāgarī

```text
स्मृत्युपस्थानमेकं धीर्निरोधे परचित्तधीः ।
त्रीणि चत्वारि शेषाणि धर्मधीर्गोचरो नव ॥ ७.१६ ॥
```

### IAST

```text
smṛtyupasthānam ekaṃ dhīr nirodhe paracittadhīḥ /
trīṇi catvāri śeṣāṇi dharmadhīgocaro nava // VAK_7.16 //
```

## Source Caution

This verse contains two linked classifications:

1. the relation of the knowledges to the four applications of mindfulness (`smṛtyupasthāna`), and
2. the number of knowledges that can become the object of knowledge of dharmas.

The second half begins a sequence continued in VAK 7.17. The present verse therefore states only the first member of a larger object-range table.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| smṛtyupasthānam | nominative singular neuter | application or foundation of mindfulness |
| ekam | nominative singular neuter | one |
| dhīḥ nirodhe | nominative singular feminine with locative | cognition concerning cessation |
| paracitta-dhīḥ | nominative singular feminine | knowledge of another mind |
| trīṇi | nominative plural neuter | three |
| catvāri | nominative plural neuter | four |
| śeṣāṇi | nominative plural neuter | the remaining ones |
| dharma-dhī-gocaraḥ | nominative singular masculine | object-range of knowledge of dharmas |
| nava | nominative plural neuter | nine |

## Grammar

The first three pādas distribute the knowledges across the four applications of mindfulness:

```text
knowledge of cessation
    one application of mindfulness

knowledge of another mind
    three applications of mindfulness

the remaining knowledges
    four applications of mindfulness
```

The omitted nouns are supplied from context. `dhīr nirodhe` means the cognition or knowledge whose object is cessation. Since cessation is apprehended only under the application of mindfulness to dharmas, this knowledge is onefold.

Knowledge of another mind takes another's mental event together with its associated feeling, recognition, and formations. It is therefore threefold with respect to the applications of mindfulness to feeling, mind, and dharmas.

The remaining knowledges can function through all four applications of mindfulness: body, feeling, mind, and dharmas.

The final pāda begins a new classification:

```text
nine knowledges
    can be objects of knowledge of dharmas
```

Inferential knowledge is excluded because knowledge of dharmas concerns the truth-structure of the desire realm.

## Literal Translation

Knowledge concerning cessation is one application of mindfulness. Knowledge of another mind is three. The remaining knowledges are four. Nine knowledges are the object-range of knowledge of dharmas.

## Philosophical Translation

The knowledges are further determined by the reflective standpoint through which their objects are attended to. Knowledge of cessation can occur only as mindfulness of dharmas; knowledge of another mind operates through three applications of mindfulness; the other knowledges may operate through all four. Knowledge of dharmas, in turn, can take nine of the ten knowledges as its objects.

## Technical Vocabulary

### smṛtyupasthāna

```text
smṛtyupasthāna
    = application or establishment of mindfulness
    = determinate standpoint of reflective attention
```

The four are:

| Application | Object-field |
|---|---|
| kāya-smṛtyupasthāna | body |
| vedanā-smṛtyupasthāna | feeling |
| citta-smṛtyupasthāna | mind |
| dharma-smṛtyupasthāna | dharmas |

These are not four separate substances. They are four determinate ways in which conditioned facticity is attended to and discriminated.

### nirodhajñāna

```text
nirodhajñāna
    = knowledge of cessation
    = dharma-smṛtyupasthāna only
```

Cessation is not body, feeling, or mind. It is therefore apprehended only within the dharma-application of mindfulness.

### paracittajñāna

```text
paracittajñāna
    = knowledge of another mind
    = three applications of mindfulness
```

It concerns:

```text
feeling
mind
associated mental dharmas
```

It does not function as mindfulness of body.

### gocara

```text
gocara
    = object-range
    = the field within which cognition can operate
```

The verse now turns from the constitution of each knowledge to the relations among the knowledges themselves.

## Doctrinal Determination

The first division is:

| Knowledge | Number of applications of mindfulness |
|---|---:|
| knowledge of cessation | 1 |
| knowledge of another mind | 3 |
| remaining knowledges | 4 |

This is grounded by object-constitution:

```text
what the knowledge can attend to
    determines
which application of mindfulness can carry it
```

The second division begins the analysis of knowledges as objects of other knowledges:

```text
knowledge of dharmas
    takes nine knowledges as object
    excludes inferential knowledge
```

VAK 7.17 completes the table for the remaining knowledges.

## Logical Determination

This verse is a precise presentation of Reflection as facticity.

The knowledge is not treated in abstraction from the conditions under which it appears. It is marked by:

```text
object-field
standpoint of attention
range of possible reflection
relation to other knowledges
```

The four applications of mindfulness therefore function as reflective indices. They state where and under what determination a cognition occurs.

```text
conditioned genesis
    leaves determinate marks

Reflection
    records those marks

scientific classification
    follows their actual distribution
```

The verse does not yet derive the knowledges genetically. It sets down the complete factual relations by which they are distinguishable.

## Organon Light

VAK 7.16 supports the project description of Reflection as **Facticity**:

> Reflection sets down the marks of conditional genesis.

Here those marks are not merely causes or supports. They include the reflective standpoint from which the object is attended to.

```text
fact
    is given under a determinate application of mindfulness

knowledge
    is bounded by the applications compatible with its object
```

This gives a useful Organon Dataset requirement:

```text
KNOWLEDGE
    object
    aspect
    support
    moral nature
    application of mindfulness
    possible knowledge-objects
```

A knowledge-entry is incomplete unless these conditioned relations are preserved.

No stronger mapping to Absolute Reflection is imposed in this first pass.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_16
    a vak:Karika ;
    rdfs:label "VAK 7.16" ;
    vak:determines jna:MindfulnessApplicationDistribution,
                   jna:KnowledgeObjectRange .

jna:CessationKnowledge
    jna:usesMindfulnessApplication jna:DharmaMindfulness .

jna:OtherMindKnowledge
    jna:usesMindfulnessApplication jna:FeelingMindfulness,
                                   jna:MindMindfulness,
                                   jna:DharmaMindfulness .

jna:DharmaKnowledge
    jna:hasKnowledgeObjectCount 9 .
```

## Commit History

```text
2026-07-23 — Initial kārikā-pass analysis.
```
