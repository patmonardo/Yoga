# VAK 6.63

## Sanskrit

प्रयोगाक्षसमापत्तिविमुक्त्युभयतः कृताः ।
पुद्गलाः सप्त षट् त्वेते द्वौ द्वौ मार्गत्रये यतः ॥

*prayogākṣasamāpattivimuktyubhayataḥ kṛtāḥ /  
pudgalāḥ sapta ṣaṭ tv ete dvau dvau mārgatraye yataḥ //*

## Source Caution

This verse gives a compact derivation of the seven pudgalas through several differentiating principles:

```text
prayoga
akṣa / indriya
samāpatti
vimukti
ubhaya
```

The second half explains why six of these are arranged as pairs across three Paths. The exact identification of every member should be verified against the Bhāṣya, but the classificatory architecture is already visible.

## Padaccheda

- *prayoga* — application, practice, preparatory effort
- *akṣa* — faculty; here equivalent to `indriya`
- *samāpatti* — contemplative attainment
- *vimukti* — liberation
- *ubhayataḥ* — through both; from the conjunction of two factors
- *kṛtāḥ* — constituted, established, distinguished
- *pudgalāḥ* — persons
- *sapta* — seven
- *ṣaṭ* — six
- *tu* — but
- *ete* — these
- *dvau dvau* — two by two
- *mārga-traye* — in the three Paths
- *yataḥ* — because, insofar as

## Literal Translation

Seven persons are constituted according to application, faculty, contemplative attainment, liberation, and both. Six of these occur two by two in the three Paths.

## Philosophical Translation

Seven principal Path-persons are distinguished according to their mode of practice, strength of faculty, possession of contemplative attainment, mode of liberation, or conjunction of the latter determinations. Six form three corresponding pairs distributed across the three principal stages of the Path.

## Five Grounds of Classification

The first half does not merely enumerate seven names. It states the principles by which they are generated.

### `Prayoga`

```text
prayoga
    mode of application
    manner of undertaking the Path
```

This concerns how the practitioner enters or applies themselves to realization.

A person can be distinguished through the character of the practice by which progress is made.

### `Akṣa`

```text
akṣa
    faculty
    operative capacity
```

This is the mild or sharp faculty distinction already encountered:

```text
śraddhānusārin
    confidence-following

dharmānusārin
    Dharma-following
```

and later:

```text
śraddhādhimukta
    confidence-resolved

dṛṣṭiprāpta
    seeing-attained
```

The same Path-stage can therefore be occupied through different operative powers.

### `Samāpatti`

```text
samāpatti
    contemplative attainment
```

This distinguishes the person according to possession of the meditative attainments, especially the cessation attainment relevant to the `kāyasākṣin` and the doubly liberated Arhat.

### `Vimukti`

```text
vimukti
    mode of liberation
```

Liberation itself differentiates persons, particularly where liberation through principle is contrasted with liberation supported by contemplative mastery.

### `Ubhayataḥ`

```text
ubhaya
    both
```

A further person is constituted through the conjunction of contemplative attainment and liberating principle.

This yields the category later named:

```text
ubhayatovimukta
    liberated in both respects
```

## Six Persons as Three Pairs

The second half gives the formal arrangement:

```text
ṣaṭ tv ete
    six of these

dvau dvau
    two by two

mārgatraye
    across three Paths
```

The likely architecture is:

```text
Path of Seeing
    two persons

Path of Cultivation
    two persons

Path beyond Training
    two persons
```

More concretely:

```text
darśanamārga
    śraddhānusārin
    dharmānusārin

bhāvanāmārga
    śraddhādhimukta
    dṛṣṭiprāpta

aśaikṣamārga
    prajñāvimukta
    ubhayatovimukta
```

The seventh person is then distinguished through contemplative attainment:

```text
kāyasākṣin
    bodily witness
```

This reconstruction is strongly suggested by the surrounding verses, but the Bhāṣya should confirm the exact enumeration.

## Provisional Sevenfold Architecture

```text
1. śraddhānusārin
2. dharmānusārin

3. śraddhādhimukta
4. dṛṣṭiprāpta

5. kāyasākṣin

6. prajñāvimukta
7. ubhayatovimukta
```

The structure is not a simple linear ladder.

It combines:

```text
Path-stage
faculty
contemplative attainment
mode of liberation
```

## Doctrinal Determination

The verse shows that `pudgala` classifications are generated intersectionally.

A Path-person is not defined by only one question:

```text
Where are they on the Path?
```

The full determination asks:

```text
By what application do they proceed?
With what faculty?
What attainment do they possess?
How are they liberated?
Do they unite contemplative and discriminative liberation?
```

Thus:

```text
pudgala
    =
Path-stage
    + operative faculty
    + contemplative capacity
    + mode of liberation
```

## Logical Determination

The seven persons are not seven independent substances.

They are determinate combinations produced by several axes of differentiation.

```text
one Path
    ↓
three stages
    ↓
paired faculty or liberation modes
    ↓
additional contemplative determination
```

The sixfold paired structure expresses symmetry:

```text
two persons
    at seeing

two persons
    in cultivation

two persons
    beyond training
```

The seventh introduces a crossing determination that cannot be reduced simply to one pair:

```text
samāpatti
    generates an additional personal form
```

This makes the pudgala architecture a structured matrix rather than a flat list.

## Basic Organon Light

This verse makes especially clear that the Kośa’s persons are functional Path-forms.

```text
pudgala
    not an independent self

pudgala class
    a determinate configuration
    of Path-operation
```

The classification arises from the conjunction of:

```text
practice
faculty
attainment
liberation
```

The knowing subject is therefore generated as a determinate position within the Path-field.

At the same time, each position possesses a correspondingly different knowable and actionable field:

```text
different faculty
    different mode of Path-access

different samāpatti
    different contemplative field

different liberation
    different completed relation to the field
```

The Path as Mega Uni Principle is one, but its personal actuality differentiates itself through these functional configurations.

## OWL++ Seed

```text
Class: PathPerson
Class: ApplicationMode
Class: SpiritualFaculty
Class: ContemplativeAttainment
Class: LiberationMode

Class: FaithFollower
Class: DharmaFollower
Class: FaithResolved
Class: SeeingAttained
Class: BodyWitness
Class: PrincipleLiberated
Class: DoublyLiberated

FaithFollower SubClassOf PathPerson
DharmaFollower SubClassOf PathPerson
FaithResolved SubClassOf PathPerson
SeeingAttained SubClassOf PathPerson
BodyWitness SubClassOf PathPerson
PrincipleLiberated SubClassOf PathPerson
DoublyLiberated SubClassOf PathPerson

PathPerson SubClassOf
    hasApplication some ApplicationMode

PathPerson SubClassOf
    hasFaculty some SpiritualFaculty

BodyWitness SubClassOf
    hasAttainment some ContemplativeAttainment

PrincipleLiberated SubClassOf
    hasLiberation some LiberationMode

DoublyLiberated SubClassOf
    hasAttainment some ContemplativeAttainment
    and hasLiberation some LiberationMode
```

## Determinate Summary

VAK 6.63 derives seven Path-persons through differences of application, faculty, contemplative attainment, liberation, and their conjunction. Six are organized as three pairs corresponding to the Paths of Seeing, Cultivation, and Beyond Training, while the seventh introduces the distinct determination of contemplative attainment. The pudgala taxonomy is therefore a matrix of operative Path-configurations rather than a collection of substantial selves.
