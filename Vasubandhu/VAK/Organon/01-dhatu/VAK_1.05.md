# VAK_1.05

## 1. Sanskrit (Devanāgarī)

> अनास्रवा मार्गसत्यं त्रिविधं चाप्यसंस्कृतम् ।
>
> आकाशं द्वौ निरोधौ च तत्राकाशमनावृतिः ॥ १.०५ ॥

## 2. Sanskrit (IAST)

> anāsravā mārgasatyaṃ trividhaṃ cāpy asaṃskṛtam /
>
> ākāśaṃ dvau nirodhau ca tatrākāśam anāvṛtiḥ // 1.05 //

## 3. Padaccheda

```text
cāpy → ca api                  tatrākāśam → tatra ākāśam
mārgasatyam → mārga-satyam    anāvṛtiḥ → an-āvṛtiḥ
```

| Pada | Features | Local force |
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

## 5. Literal Translation

### Close syntactic construe

> The dharmas without outflows are the Truth of the Path and also the threefold unconditioned: space and the two cessations. Among these, space is non-obstruction.

### Bhāṣya-informed translation

> The anāsrava dharmas comprise the conditioned Truth of the Path and three unconditioned dharmas—space, cessation through discrimination, and cessation not through discrimination—because outflows do not settle in them. Space is non-obstruction: that in which material form can move.

## 6. Philosophical Translation

> Freedom from outflows and freedom from conditioning are distinct determinations. The Path is produced through conditions yet does not lodge outflows; the three unconditioned dharmas are likewise anāsrava. Space is defined exactly by non-obstruction of material movement.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Determination |
|---|---|---|
| anāsrava | without outflows | outflows do not settle within it |
| mārga-satya | Truth of the Path | conditioned and anāsrava |
| asaṃskṛta | unconditioned | space and the two cessations |
| ākāśa | space | non-obstruction |
| anāvṛti | non-obstruction | explained through movement of rūpa |
| pratisaṃkhyā-nirodha | cessation through discrimination | named here; defined in 1.06 |
| apratisaṃkhyā-nirodha | cessation not through discrimination | named here; defined in 1.06 |

## 8. Logical Determination

Two axes must remain independent:

| Dharma class | Conditioned? | With outflows? |
|---|---:|---:|
| ordinary conditioned dharmas | yes | yes |
| Path-truth | yes | no |
| three unconditioned dharmas | no | no |

```text
ākāśa = non-obstruction in which material form can move
```

## 9. Interpretive Note

The Kośa begins comprehension through intersecting predicates rather than a single metaphysical division. “Conditioned” does not entail “contaminated,” and `anāsrava` does not mean “unconditioned.” The earlier seed's language of an unlimited “opened field” is therefore restricted here to the Bhāṣya's concrete determination of space.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
vak:VAK_1_05 a vak:Karika ; vak:hasTopic vak:AnasravaDharmas ; vak:belongsTo vak:Dhatunirdesa .
vak:PathTruth a vak:ConditionedDharma, vak:AnasravaDharma .
vak:Akasha a vak:UnconditionedDharma, vak:AnasravaDharma ; vak:definedAs vak:NonObstruction .
vak:PratisamkhyaNirodha a vak:UnconditionedDharma .
vak:ApratisamkhyaNirodha a vak:UnconditionedDharma .
```
