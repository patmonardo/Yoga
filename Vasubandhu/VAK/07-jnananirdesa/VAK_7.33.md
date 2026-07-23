# VAK_7.33 — Great Compassion and Its Eight Distinctions

## Sanskrit

### Devanāgarī

```text
महाकृपा संवृतिधीः संभाराकारगोचरैः ।
समत्वादाधिमात्र्याच्च नानाकरणमष्टधा ॥ ७.३३ ॥
```

### IAST

```text
mahākṛpā saṃvṛtidhīḥ saṃbhārākāragocaraiḥ /
samatvād ādhimātryāc ca nānākaraṇam aṣṭadhā // VAK_7.33 //
```

## Source Caution

The verse defines great compassion and states that it differs in eight respects.

The transmitted compound sequence is highly compressed. On a first kārikā pass, the safest reading is:

```text
great compassion
    is conventional cognition

it is distinguished eightfold
    by accumulation
    mode
    object-field
    equality
    superiority
    and the remaining correlated factors supplied by the bhāṣya
```

The full eightfold list belongs to the bhāṣya’s exposition. The kārikā itself gives the governing categories rather than a fully expanded inventory.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| mahā-kṛpā | nominative singular feminine | great compassion |
| saṃvṛti-dhīḥ | nominative singular feminine | conventional cognition |
| saṃbhāra | instrumental within compound | accumulation, preparatory equipment |
| ākāra | instrumental within compound | mode, cognitive form |
| gocara | instrumental within compound | object-field, range |
| samatvāt | ablative singular | because of equality, by equality |
| ādhimātryāt | ablative singular | because of superiority, greater intensity |
| ca | conjunction | and |
| nānā-karaṇam | nominative/accusative singular neuter | differentiation, making distinct |
| aṣṭadhā | adverb | in eight ways |

## Grammar

The opening identification is direct:

```text
mahākṛpā
    great compassion

saṃvṛtidhīḥ
    is conventional cognition
```

The remainder states the grounds of distinction:

```text
saṃbhāra-ākāra-gocaraiḥ
    by accumulation, mode, and object-field

samatvāt
    by equality

ādhimātryāt ca
    and by superiority or greater intensity

nānākaraṇam aṣṭadhā
    the differentiation is eightfold
```

The verse compresses several paired contrasts into a compact scholastic formula.

## Literal Translation

Great compassion is conventional cognition. Its differentiation is eightfold, according to accumulation, mode, object-field, equality, and superiority.

## Philosophical Translation

The Buddha’s great compassion is classified as a conventional form of knowing because it takes suffering beings and their conditions as its object-field. Yet it is not ordinary sympathy. It differs from lesser compassion through a determinate eightfold structure involving the depth of its preparation, the form in which it apprehends suffering, the range of beings it addresses, its equality toward all, and its unsurpassed intensity.

## Technical Vocabulary

### mahā-kṛpā

```text
mahā-kṛpā
    great compassion
    the Buddha’s unrestricted orientation toward the suffering of beings
```

Its greatness does not mean mere emotional magnitude. It is great because its preparation, range, equality, and power exceed ordinary compassion.

### saṃvṛti-dhī

```text
saṃvṛti-dhī
    conventional cognition
    cognition directed toward dependently designated beings and suffering situations
```

This does not make compassion false. It identifies its analytical level: compassion operates toward beings as encountered within the conventional field.

### saṃbhāra

```text
saṃbhāra
    accumulation
    preparatory equipment
    cultivated resources supporting a perfected function
```

Great compassion presupposes a vast prior cultivation rather than arising as an isolated affect.

### ākāra

```text
ākāra
    mode
    cognitive presentation
    the form under which an object is known
```

Compassion is distinguished not only by what it knows but by how suffering appears within the cognition.

### gocara

```text
gocara
    object-field
    operational range
```

The field of great compassion is universal rather than selective.

## Doctrinal Determination

### Conventional cognition

The verse’s first determination is important:

```text
great compassion
    is not direct cognition of the unconditioned

it is cognition of beings
    suffering
    causes
    and situations
    within the conventional field
```

Compassion therefore belongs to the Buddha’s engagement with the world rather than to withdrawal from it.

### Eightfold differentiation

The bhāṣya expands the difference between ordinary compassion and great compassion through eight factors. The kārikā groups them under several headings:

```text
preparation
    the accumulation from which compassion arises

mode
    how suffering is cognitively presented

object-field
    the extent of beings and suffering taken as object

equality
    impartiality toward beings

superiority
    greater force, continuity, and effectiveness
```

For the first pass, the exact sub-enumeration can remain attached to the bhāṣya. The verse’s main function is to establish that great compassion is a structured cognitive capacity.

### Compassion as knowledge-function

VAK 7.28–7.32 analyzed powers, fearlessnesses, and establishments of mindfulness. VAK 7.33 now shows that compassion also has a determinate cognitive architecture:

```text
compassion
    is not opposed to knowledge

compassion
    is knowledge organized toward the suffering of beings
```

## Logical Determination

The verse distinguishes classification from value:

```text
conventional
    does not mean insignificant

conventional cognition
    may possess universal range
    equality
    and unsurpassed intensity
```

It also gives a light rule for analytical scope:

```text
one function
    can be analyzed by
    source
    form
    object
    range
    and degree
```

This is the Kośa’s knowledge combinatorics applied to compassion.

## Organon Light

The basic determination is:

> Great compassion is conventional cognition made universal, equal, and unsurpassed in its operation.

The Buddha does not leave the conventional field behind. He masters it as an object-field of liberative activity.

```text
truth of suffering
    is known

beings who suffer
    become the field of compassion

knowledge
    becomes universally directed action
```

Compassion is therefore not an ornament added to knowledge. It is knowledge turned without obstruction toward the world.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix path: <http://127.0.0.1:3000/path#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_33
    a vak:Karika ;
    rdfs:label "VAK 7.33" ;
    vak:determines path:GreatCompassion,
                   jna:ConventionalCognition,
                   path:EightfoldCompassionDifference .

path:GreatCompassion
    a jna:ConventionalCognition ;
    path:hasDifferentiation path:EightfoldCompassionDifference ;
    path:hasObjectField path:AllSufferingBeings ;
    path:hasQuality path:Equality,
                    path:UnsurpassedIntensity .

path:EightfoldCompassionDifference
    path:analyzedBy path:Accumulation,
                    jna:CognitiveMode,
                    jna:ObjectField,
                    path:Equality,
                    path:Superiority .
```

## Commit History

```text
2026-07-23 — Initial kārikā-pass analysis for VAK_7b.
```
