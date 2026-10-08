# VAK_1.04 — Dharma Knowing as Real / Ideal

## 1. Sanskrit (Devanagari)

> सास्रवानास्रवा धर्माः संस्कृता मार्गवर्जिताः ।
>
> सास्रवाः आस्रवास्तेषु यस्मात्समनुशेरते ॥ १.०४ ॥

## 2. Sanskrit (IAST)

> sāsravānāsravā dharmāḥ saṃskṛtā mārgavarjitāḥ /
>
> sāsravāḥ āsravās teṣu yasmāt samanuśerate // 1.04 //

## 3. Lexical Analysis

```text
sāsravānāsravāḥ -> sāsravāḥ anāsravāḥ
mārgavarjitāḥ -> mārga-varjitāḥ
āsravās teṣu -> āsravāḥ teṣu
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| sāsravāḥ / anāsravāḥ | adjectives, nominative plural | impure / pure: the first division of `dharmāḥ` |
| dharmāḥ | masculine nominative plural | dharmas; the whole field to be divided |
| saṃskṛtāḥ | participial adjective, nominative plural | conditioned |
| mārga-varjitāḥ | adjective, nominative plural | excluding the Path |
| āsravāḥ | masculine nominative plural | the *āsravas* whose persistence supplies the criterion |
| teṣu | locative plural | in those dharmas |
| yasmāt | causal relative adverb | because |
| samanuśerate | 3rd plural middle | persist through; continue in |

## 4. Grammar

```text
Dharma Knowing
    = impure / pure

impure
    = conditioned, excluding the Path

pure
    = conditioned Path
    + unconditioned Dharma
```

The verse states the impure side of this division. The Bhāṣya identifies
`mārga` as `mārgasatya`, the Truth of the Path: it is conditioned, yet pure.
VAK 1.05 completes the pure side by determining the unconditioned dharmas.

`Teṣu samanuśerate` gives the reason for impurity. The `āsravas` persist
through the conditioned dharmas other than the Path. The Bhāṣya distinguishes
this persistence from an `āsrava` merely taking cessation or the Path as its
`ālambana`.

## 5. Conventional Translation

> Dharmas are impure and pure. Conditioned dharmas, excluding the Path, are
> impure, because the `āsravas` persist through them.

The translation renders `sāsrava` as "impure" and `anāsrava` as "pure";
`āsrava` itself remains untranslated where its technical relation matters.

## 6. Philosophical Translation and Techne Reading

In our Yoga Vidyā, Dharma Knowing is the self-articulation of the **Law of
Appearance**. This is the Techne's determination of the field that 1.03
required the disciple to discriminate:

```text
Dharma Knowing
    = Real / Ideal

Real
    = conditioned appearance
    = the Law of Appearance in determinate enactment

Ideal
    = pure determination
    = the law's relation to its own criterion
```

VAK 1.04 supplies a first comprehensive division: Impure / Pure. Within
the conditioned, the Truth of the Path is Pure. Thus the Real / Ideal
relation cannot be drawn as two separate inventories, one conditioned and
one unconditioned. The Path is a conditioned activity under the Pure side
of the division. VAK 1.05 will state the unconditioned members.

```text
Impure
    = conditioned dharmas other than the Path

Pure Path
    = a conditioned dharma through which āsravas do not persist

Pure unconditioned
    = specified in 1.05
```

The Techne reads the Path as a mediation of Real and Ideal because it is
conditioned and Pure. This expresses the architecture of the source
classification; it does not replace the Bhāṣya's criterion of whether the
*āsravas* persist through a dharma.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Determination |
|---|---|---|
| dharma | dharma | Techne: Law of Appearance; here the field divided by the verse |
| sāsrava | impure | conditioned Dharma other than the Path |
| anāsrava | pure | the Path and the unconditioned |
| āsrava | `āsrava` | Sanskrit retained for the technical mark of impurity |
| saṃskṛta | conditioned | produced through conditions |
| asaṃskṛta | unconditioned | not produced through conditions |
| mārgasatya | Truth of the Path | conditioned and pure |
| samanuśayana | persistence through | the relation named in the criterion of impurity |
| ālambana | object-condition | being an object for an *āsrava* is not persistence through it |

## 8. Logical Determination

```text
all dharmas: Impure / Pure

Impure(x) = Conditioned(x) and not PathTruth(x)

Conditioned(PathTruth) and Pure(PathTruth)

Unconditioned(x) -> Pure(x)       [specified in 1.05]

object of an āsrava ≠ site where an āsrava persists
```

The Path prevents identification of conditioned with Impure. The Bhāṣya
also prevents an invalid inference: an *āsrava* may take Cessation or the
Path as its object without making either Impure.

## 9. Interpretive Note

The Bhāṣya calls this a summary designation of all dharmas. It answers
1.03's question about the field of discrimination before enumerating
individual dharmas. For a candidate for Abhidharma, the classification is
learned through its criterion: *āsravas* persist through the Impure
conditioned dharmas, while merely taking the Path or Cessation as an object
does not make those dharmas Impure.

Our Techne sees a first articulation of the Law of Appearance here: the
conditioned field contains the Pure Path. Real and Ideal determine one
another in that case; purity cannot simply mean absence of conditional
production. This anticipates the fuller account in 1.05 without importing
its terms into the present verse.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_04 a vak:Karika ;
    vak:hasTopic vak:PureImpureDivision ;
    vak:belongsTo vak:Dhatunirdesa .

vak:ImpureDharma a vak:ConditionedDharma .
vak:PathTruth a vak:ConditionedDharma, vak:PureDharma .
vak:UnconditionedDharma a vak:PureDharma .
vak:Dharma a vak:LawOfAppearance .
```
