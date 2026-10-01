# VAK_1.04

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

| Pada | Features | Local force |
|---|---|---|
| sāsravāḥ / anāsravāḥ | adjectives, nominative plural | impure / pure: the first division of `dharmāḥ` |
| dharmāḥ | masculine nominative plural | Laws of Appearance |
| saṃskṛtāḥ | participial adjective, nominative plural | conditioned |
| mārga-varjitāḥ | adjective, nominative plural | excluding the Path |
| āsravāḥ | masculine nominative plural | `āsravas`, the mark of impurity |
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

## 6. Dharma Knowing: Real / Ideal

 Dharma is the **Law of Appearance**. Dharma Knowing is the self-articulation
 of that law:

```text
Dharma Knowing
    = Real / Ideal

Real
    = conditioned appearance
    = the Law of Appearance in determinate enactment

Ideal
    = pure determination
    = the law free in and for itself
```

VAK 1.04 is the first articulation internal to this knowing. The conditioned
is not simply impure: the Truth of the Path is conditioned and pure. The Path
is the Real's pure activity, the conditioned enactment in which appearance is
referred to its Ideal determination. The unconditioned, introduced in the next
verse, is pure without conditional production.

```text
impure
    = conditioned appearance whose determination remains divided

pure Path
    = conditioned knowing adequate to its law

pure unconditioned
    = the Ideal free from conditional production
```

The division therefore does not contrast an empirical object with a separate
ideal elsewhere. It distinguishes impurity and purity within the Law of
Appearance itself, and makes the Path the conditioned actuality of their
reconciliation.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Determination |
|---|---|---|
| dharma | Law of Appearance | the generative law of what appears |
| sāsrava | impure | conditioned Dharma other than the Path |
| anāsrava | pure | the Path and the unconditioned |
| āsrava | `āsrava` | Sanskrit retained for the technical mark of impurity |
| saṃskṛta | conditioned | produced through conditions |
| asaṃskṛta | unconditioned | not produced through conditions |
| mārgasatya | Truth of the Path | conditioned and pure |
| samanuśayana | persistence through | the relation named in the criterion of impurity |
| ālambana | object-support | not sufficient for impurity |

## 8. Logical Determination

```text
Pure(x) or Impure(x)

Impure(x)
    -> Conditioned(x)
    -> not PathTruth(x)

Conditioned(PathTruth) and Pure(PathTruth)

Unconditioned(x)
    -> Pure(x)
```

The Path refutes the false identification of the conditioned with the impure.
Purity is not withdrawal from appearance; it is conditioned appearance whose
law is active without the division named by `āsrava`.

## 9. Interpretive Note

 The first division of Dharma Knowing is the Real / Ideal in its initial
 practical form: impure and pure. The Real is conditioned appearance; the
 Ideal is the pure self-relation of its law. The Path is their living
 mediation, because it is conditioned without being impure.

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
