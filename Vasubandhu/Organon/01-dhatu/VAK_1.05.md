# VAK_1.05 — The Pure

## 1. Sanskrit (Devanāgarī)

> अनास्रवा मार्गसत्यं त्रिविधं चाप्यसंस्कृतम् ।
>
> आकाशं द्वौ निरोधौ च तत्राकाशमनावृतिः ॥ १.०५ ॥

## 2. Sanskrit (IAST)

> anāsravā mārgasatyaṃ trividhaṃ cāpy asaṃskṛtam /
>
> ākāśaṃ dvau nirodhau ca tatrākāśam anāvṛtiḥ // 1.05 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| anāsravāḥ | adjective; nominative plural | pure; the subject supplied from 1.04 |
| mārgasatyam | mārga-satyam; nominative neuter singular | the Truth of the Path |
| trividham | nominative neuter singular | threefold |
| ca api | particles | and also |
| asaṃskṛtam | nominative neuter singular | the unconditioned |
| ākāśam | nominative neuter singular | space |
| dvau nirodhau | masculine dual nominative | the two cessations |
| tatra | indeclinable | among these |
| anāvṛtiḥ | an-āvṛtiḥ; nominative feminine singular | non-obstruction; the predicate of space |

## 4. Grammar

The subject is recovered from 1.04.

```text
anāsravāḥ
    = mārga-satyam
    + trividham asaṃskṛtam
        = ākāśam
        + dvau nirodhau

tatrākāśam anāvṛtiḥ
```

*Ākāśam anāvṛtiḥ* is a cross-gender nominal definition. Space is non-obstruction. The names of the two cessations are supplied by the commentary and defined in the next verse.

## 5. Translation

### Literal

The pure are the Truth of the Path and also the threefold unconditioned: space and the two cessations. Among these, space is non-obstruction.

### Bhāṣya-informed

Which dharmas are pure? The Truth of the Path, and the threefold unconditioned. The three are space and the two cessations: cessation through discrimination, and cessation not through discrimination. These, together with the Truth of the Path, are the pure dharmas, because the *āsravas* do not persist in them. Space is non-obstruction. Its nature is non-obstruction. It is where form can move.

## 6. Philosophical Translation

The pure member named in the previous verse is enumerated here. It is not the unconditioned as such.

The Truth of the Path is conditioned, and pure. Space and the two cessations are unconditioned, and pure. The reason is the same failure: the *āsravas* do not persist in them. Persistence was the test of the impure. Its absence is the test of the pure.

Space is defined. The two cessations are named. Their definitions are the next verse.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| anāsrava | pure | the *āsravas* do not persist |
| mārga-satya | Truth of the Path | conditioned and pure |
| asaṃskṛta | unconditioned | space and the two cessations |
| ākāśa | space | non-obstruction |
| anāvṛti | non-obstruction | where form can move |
| pratisaṃkhyā-nirodha | cessation through discrimination | named here; defined in 1.06 |
| apratisaṃkhyā-nirodha | cessation not through discrimination | named here; defined in 1.06 |
| anuśerate | persist | the verb that fails in the pure |

## 8. Logical Determination

```text
pure
    = Truth of the Path
    + threefold unconditioned
        = space
        + cessation through discrimination
        + cessation not through discrimination

conditioned does not entail impure
pure does not entail unconditioned

space
    = non-obstruction
    = where form can move
```

| Dharma class | Conditioned? | Pure? |
|---|---:|---:|
| conditioned, other than the Path | yes | no |
| Truth of the Path | yes | yes |
| space and the two cessations | no | yes |

## 9. Interpretive Note

The verse completes the division opened in 1.04. Four dharmas are pure. One of them is conditioned. Space receives its definition. The two cessations do not.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_05 a vak:Karika ;
    vak:hasTopic vak:PureDharmas ;
    vak:belongsTo vak:Dhatunirdesa .

vak:PathTruth a vak:ConditionedDharma, vak:PureDharma .
vak:Akasha a vak:UnconditionedDharma, vak:PureDharma ;
    vak:definedAs vak:NonObstruction .
vak:PratisamkhyaNirodha a vak:UnconditionedDharma, vak:PureDharma .
vak:ApratisamkhyaNirodha a vak:UnconditionedDharma, vak:PureDharma .
```
