# VAK_1.05

## 1. Sanskrit (Devanāgarī)

> अनास्रवा मार्गसत्यं त्रिविधं चाप्यसंस्कृतम् ।
>
> आकाशं द्वौ निरोधौ च तत्राकाशमनावृतिः ॥ १.०५ ॥

## 2. Sanskrit (IAST)

> anāsravā mārgasatyaṃ trividhaṃ cāpy asaṃskṛtam /
>
> ākāśaṃ dvau nirodhau ca tatrākāśam anāvṛtiḥ // 1.05 //

## 3. Lexical Analysis

```text
cāpy → ca api                  tatrākāśam → tatra ākāśam
mārgasatyam → mārga-satyam    anāvṛtiḥ → an-āvṛtiḥ
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| anāsravāḥ | adjective, nominative plural | qualifies supplied `dharmāḥ` |
| mārga-satyam | neuter nominative singular | conditioned anāsrava member |
| trividham asaṃskṛtam | neuter nominative singular | threefold unconditioned class |
| ākāśam | neuter nominative singular | first unconditioned dharma |
| dvau nirodhau | masculine dual nominative | two cessations |
| tatra | indeclinable | among these |
| anāvṛtiḥ | feminine nominative singular | predicate definition: non-obstruction |

## 4. Grammar

The supplied `dharmāḥ` is recovered from 1.04:

```text
anāsrava dharmas
├── mārga-satya             conditioned
└── threefold asaṃskṛta     unconditioned
    ├── ākāśa
    ├── pratisaṃkhyā-nirodha
    └── apratisaṃkhyā-nirodha
```

The names of the two cessations are supplied by the Bhāṣya and defined in 1.06. `ākāśam anāvṛtiḥ` is a cross-gender nominal definition: space is non-obstruction.

## 5. Translation

### Close syntactic construe

> The Pure dharmas are the Truth of the Path and also the threefold unconditioned: space and the two cessations. Among these, space is non-obstruction.

### Bhāṣya-informed translation

> The Pure dharmas comprise the conditioned Truth of the Path and three unconditioned dharmas—space, cessation through discrimination, and cessation not through discrimination—because the *āsravas* do not persist in them. Space is non-obstruction: that in which form can move.

## 6. Philosophical Translation and Techne Reading

> Being Pure and being unconditioned are distinct determinations. The Truth of the Path is conditioned yet Pure; space and the two cessations are unconditioned and Pure. Space is non-obstruction, explained by the Bhāṣya as allowing form to move.

Techne reading:

> The Science of Principles must distinguish two independent questions: whether a dharma is produced by conditions, and whether the *āsravas* can persist in it. The Pure Path is conditioned activity; the other three Pure dharmas are unconditioned. Space first appears as non-obstruction, a determinate account of where form can move. The two cessations are named here and explained in 1.06.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Determination |
|---|---|---|
| anāsrava | Pure | the *āsravas* do not persist in these dharmas |
| mārga-satya | Truth of the Path | conditioned and anāsrava |
| asaṃskṛta | unconditioned | space and the two cessations |
| ākāśa | space | non-obstruction |
| anāvṛti | non-obstruction | explained through movement of Form (*rūpa*) |
| pratisaṃkhyā-nirodha | cessation through discrimination | named here; defined in 1.06 |
| apratisaṃkhyā-nirodha | cessation not through discrimination | named here; defined in 1.06 |

## 8. Logical Determination

Two axes must remain independent:

| Dharma class | Conditioned? | Pure? |
|---|---:|---:|
| conditioned dharmas other than the Path | yes | no |
| Truth of the Path | yes | yes |
| space and the two cessations | no | yes |

```text
ākāśa = non-obstruction where Form can move
```

## 9. Interpretive Note

VAK 1.05 completes the Pure side of the summary division begun in 1.04.
The Truth of the Path and the unconditioned three belong together under
Purity, while remaining different in whether they are conditioned. The
Bhāṣya gives one criterion for their shared placement: the *āsravas* do
not persist in them.

For our Techne, this is a lesson in scientific definition. One predicate
cannot silently stand in for another: Pure does not mean unconditioned.
The Path makes that difference actual within conditioned activity. Space
then receives a positive use through its negative definition,
non-obstruction, because it is where Form can move. The passage does not
yet tell us what the two cessations do; that belongs to 1.06.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
vak:VAK_1_05 a vak:Karika ; vak:hasTopic vak:AnasravaDharmas ; vak:belongsTo vak:Dhatunirdesa .
vak:PathTruth a vak:ConditionedDharma, vak:AnasravaDharma .
vak:Akasha a vak:UnconditionedDharma, vak:AnasravaDharma ; vak:definedAs vak:NonObstruction .
vak:PratisamkhyaNirodha a vak:UnconditionedDharma .
vak:ApratisamkhyaNirodha a vak:UnconditionedDharma .
```
