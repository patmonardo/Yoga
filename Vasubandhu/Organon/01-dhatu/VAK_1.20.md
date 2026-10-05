# VAK_1.20 — Collection, Door, Source

## 1. Sanskrit (Devanāgarī)

> राश्यायद्वारगोत्रार्थाः स्कन्धायतनधातवः ।
>
> मोहेन्द्रियरुचित्रैधात्तिस्रः स्कन्धादिदेशनाः ॥ १.२० ॥॥

## 2. Sanskrit (IAST)

> rāśyāyadvāragotrārthāḥ skandhāyatanadhātavaḥ /
>
> mohendriyarucitraidhāt tisraḥ skandhādideśanāḥ // 1.20 //

## 3. Lexical Analysis

```text
rāśyāyadvāragotrārthāḥ → rāśi-āya-dvāra-gotra-arthāḥ
skandhāyatanadhātavaḥ   → skandha-āyatana-dhātavaḥ
mohendriyarucitraidhāt  → moha-indriya-ruci-traidhāt
skandhādideśanāḥ        → skandha-ādi-deśanāḥ
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| rāśi | compound member | collection; a heap gathered into one |
| āya | compound member | arrival |
| dvāra | compound member | door |
| gotra | compound member | source-kind; the mine |
| arthāḥ | nominative plural | having these meanings, distributed |
| skandha-āyatana-dhātavaḥ | nominative plural | bases, essences, principles |
| moha | compound member | confusion |
| indriya | compound member | the learner's faculty |
| ruci | compound member | inclination |
| traidhāt | ablatival | because of the threefold |
| tisraḥ | nominative feminine plural | three; agrees with the teachings |
| deśanāḥ | nominative feminine plural | teachings |

The first compound distributes. It does not pile four meanings on one word.

```text
base     → collection
essence  → door of arrival
principle → source-kind
```

## 4. Grammar

```text
skandha-āyatana-dhātavaḥ
    = rāśi-āya-dvāra-gotra-arthāḥ

moha-indriya-ruci-traidhāt
    → tisraḥ skandha-ādi-deśanāḥ
```

The first line is a distributive predication. The second is an ablative of
cause. *Tisraḥ* agrees with *deśanāḥ*.

The Bhāṣya unfolds each meaning, then assigns the three teachings in order.

## 5. Translation

### Literal Translation

Bases, essences, and principles have the meanings of collection, door of
arrival, and source-kind. Because confusion, faculty, and inclination are
threefold, there are three teachings, beginning with the bases.

### Bhāṣya-informed study translation

A base is a collection: whatever form is past, future, or present, gathered
into one, is reckoned the form-base. An essence is the door through which
consciousness and the mental factors arrive and extend. A principle is a
source-kind, as the mines in one mountain. For the conditioned, that source
is a homogeneous cause of its own kind. The unconditioned are principles as
kind and own-nature, not as that cause. The three teachings answer three
confusions, three faculties, and three inclinations.

## 6. Philosophical Translation

Again, two lines. The first is the science. The second is why it is taught
three ways.

The system rolls because the three are not synonyms. A base collects. The
sūtra is the warrant: all of it gathered into one. The collection is a
designation, as a heap is. It is not a further substance over the gathered,
and it is not the burden-bearing or the portion that others propose. Those
depart from the sūtra.

An essence is a door. Consciousness and the mental factors arrive through
it, and are extended. That is the derivation: they extend the arrival. Not
a place on a map.

A principle is a source-kind. One mountain, many mines: iron, copper,
silver, gold. One support, or one continuum, eighteen sources. The eye and
the rest are sources of their own kind, because they are homogeneous
causes. The objection is exact. Then the unconditioned would not be a
principle. Others therefore take the word as kind and own-nature: the
eighteen dharmas, eighteen principles. Source where there is a series.
Kind where there is not. The word is not reduced to the cause.

The second line does not rank the teachings. Some are confused about the
mental factors, grasping a self as a lump. Some about form alone. Some
about form and consciousness. Faculties are sharp, middling, weak.
Inclination wants the brief, the intermediate, or the extensive. In that
order: bases, essences, principles. The field is one. The exposition
follows the one to be trained.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| skandha | base | the collection; not a further substance |
| rāśi | collection | the sūtra's meaning; a heap |
| prajñapti | designation | how a base exists |
| āyatana | essence | the door |
| āya | arrival | of consciousness and the mental factors |
| dvāra | door | they extend the arrival |
| dhātu | principle | source-kind |
| gotra | source-kind | glossed as mine |
| ākara | mine | the mountain image |
| sabhāga-hetu | homogeneous cause | of its own kind; the conditioned |
| svabhāva | own-nature | the general account, with the unconditioned |
| citta | consciousness | what arrives through the door |
| moha | confusion | lump-self; form; form and consciousness |
| indriya | faculty | here the learner's: sharp, middling, weak |
| ruci | inclination | brief, intermediate, extensive |
| vineya | one to be trained | why three teachings |
| deśanā | teaching | not three rival systems |

## 8. Logical Determination

```text
base      → collection
          → gathered into one
          → designation, as a heap
          not burden, not portion

essence   → door of arrival
          → consciousness and mental factors extend

principle → source-kind
          conditioned → homogeneous cause of its own kind
          unconditioned → kind, own-nature
          not the cause alone

teachings, in order
    confusion about mental factors, sharp, brief        → bases
    confusion about form, middling, intermediate        → essences
    confusion about form and consciousness, weak, long  → principles

one field
three expositions
1.21 not opened
```

## 9. Interpretive Note

The hinge is the distributed compound, then *traidhāt*. Interpretation of
the mine, the unconditioned, and the designation is in the Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_20 a vak:Karika ;
    vak:hasTopic vak:ThreeMeaningsThreeTeachings ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Base vak:means vak:Collection ;
    vak:existsAs vak:Designation .
vak:Essence vak:means vak:DoorOfArrival .
vak:Principle vak:means vak:SourceKind ;
    vak:whenConditioned vak:HomogeneousCause ;
    vak:whenUnconditioned vak:OwnNature .

vak:ThreeTeachings vak:because vak:ThreefoldConfusion,
    vak:ThreefoldFaculty, vak:ThreefoldInclination ;
    vak:order vak:Bases, vak:Essences, vak:Principles ;
    vak:oneField true .
```
