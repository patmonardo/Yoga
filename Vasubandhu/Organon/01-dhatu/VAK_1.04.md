# VAK_1.04 — Impure and Pure

## 1. Sanskrit (Devanāgarī)

> सास्रवानास्रवा धर्माः संस्कृता मार्गवर्जिताः ।
>
> सास्रवाः आस्रवास्तेषु यस्मात्समनुशेरते ॥ १.०४ ॥

## 2. Sanskrit (IAST)

> sāsravānāsravā dharmāḥ saṃskṛtā mārgavarjitāḥ /
>
> sāsravāḥ āsravās teṣu yasmāt samanuśerate // 1.04 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sāsravānāsravāḥ | sāsravāḥ + anāsravāḥ; nominative plural | impure and pure; the first division of the dharmas |
| dharmāḥ | nominative masculine plural | the dharmas so divided |
| saṃskṛtāḥ | participial adjective; nominative plural | conditioned |
| mārgavarjitāḥ | mārga-varjitāḥ; nominative plural | excluding the Path |
| sāsravāḥ | nominative plural | impure; the predicate resumed |
| āsravāḥ | nominative plural | the *āsravas* |
| teṣu | locative plural | in those |
| yasmāt | causal indeclinable | because |
| samanuśerate | 3rd plural middle, present | persist |

## 4. Grammar

```text
dharmāḥ
    = sāsravāḥ
    + anāsravāḥ

sāsravāḥ
    = saṃskṛtāḥ
    = mārga-varjitāḥ
    because āsravāḥ teṣu samanuśerate
```

The first quarter divides. The second names the impure member. The third and fourth give the reason. The pure member is not enumerated here.

## 5. Translation

### Literal Translation

Dharmas are impure and pure. Conditioned, excluding the Path, are impure, because the *āsravas* persist in them.

### Bhāṣya-informed study translation

The dharmas are impure or pure. The impure are the conditioned dharmas apart from the Truth of the Path, because the āsravas persist in them; the Path, though conditioned, is pure.

## 6. Philosophical Translation

Two predicates, not one. Impure and pure divide the dharmas. Conditioned and unconditioned do not.

The impure side is stated. Conditioned, and not the Path. The reason is persistence. The *āsravas* persist in those dharmas. Taking a dharma as *ālambana* is a different relation. Cessation and the Path can be taken, and remain pure.

The Path is the exception inside the conditioned. It is conditioned, and it is pure. Purity is not the absence of conditions. The unconditioned pure is the next verse. It is not this one.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| dharma | dharma | not a second word for the division |
| sāsrava | impure | conditioned, excluding the Path |
| anāsrava | pure | the Path, and the unconditioned of the next verse |
| saṃskṛta | conditioned | produced through conditions |
| mārga | Path | the commentary: the Truth of the Path |
| āsrava | *āsrava* | what persists; not the name of the division |
| samanuśerate | persist | the criterion of the impure |
| ālambana | *ālambana* | taking; not persistence |

## 8. Logical Determination

```text
dharmas
    = impure or pure

impure
    = conditioned
    = not the Truth of the Path
    = the āsravas persist there

Truth of the Path
    = conditioned
    = pure
    = taking is not persistence

unconditioned
    = pure
    = not this verse
```

Conditioned does not entail impure. Pure does not entail unconditioned.

## 9. Interpretive Note

The verse gives the impure member and the reason. The pure member is named in the first quarter and left for the next verse. Persistence is the test. *Ālambana* is the qualification, and it does not decide the division.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_04 a vak:Karika ;
    vak:hasTopic vak:PureImpureDivision ;
    vak:belongsTo vak:Dhatunirdesa .

vak:ImpureDharma a vak:ConditionedDharma ;
    vak:excludes vak:PathTruth ;
    vak:criterion vak:Persistence .

vak:PathTruth a vak:ConditionedDharma, vak:PureDharma .

vak:Alambana owl:differentFrom vak:Persistence .
```
