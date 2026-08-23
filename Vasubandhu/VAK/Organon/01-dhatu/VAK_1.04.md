# VAK_1.04

## 1. Sanskrit (Devanāgarī)

> सास्रवानास्रवा धर्माः संस्कृता मार्गवर्जिताः ।
>
> सास्रवाः आस्रवास्तेषु यस्मात्समनुशेरते ॥ १.०४ ॥

## 2. Sanskrit (IAST)

> sāsravānāsravā dharmāḥ saṃskṛtā mārgavarjitāḥ /
>
> sāsravāḥ āsravās teṣu yasmāt samanuśerate // 1.04 //

## 3. Padaccheda

```text
sāsravānāsravāḥ → sāsravāḥ anāsravāḥ
mārgavarjitāḥ → mārga-varjitāḥ
āsravās teṣu → āsravāḥ teṣu
```

| Pada | Features | Local force |
|---|---|---|
| sāsravāḥ / anāsravāḥ | adjectives, nominative plural | exhaustive first division of `dharmāḥ` |
| dharmāḥ | masculine nominative plural | classified field |
| saṃskṛtāḥ | participial adjective, nominative plural | conditioned dharmas |
| mārga-varjitāḥ | adjective, nominative plural | excluding the Path |
| āsravāḥ | masculine nominative plural | outflows, subject |
| teṣu | locative plural | in those dharmas |
| yasmāt | causal relative adverb | because |
| samanuśerate | 3rd plural middle | settle and continue within |

## 4. Grammar

```text
all dharmas = sāsrava ∪ anāsrava
sāsrava = conditioned dharmas − Path-truth
```

The Bhāṣya identifies `mārga` as `mārgasatya`. The decisive locative relation is expressed by `teṣu samanuśerate`: the outflows settle within these dharmas.

The Bhāṣya then blocks a false inference:

```text
outflow takes X as object (ālambana)  ≠  outflow settles in X (anuśayana)
```

An outflow may arise with cessation or Path as its object without either becoming sāsrava. The full mechanism is explicitly deferred to the Anuśayanirdeśa.

## 5. Literal Translation

### Close syntactic construe

> Dharmas are with outflows and without outflows. Conditioned dharmas, excluding the Path, are with outflows, because the outflows settle and continue within them.

### Bhāṣya-informed translation

> All dharmas are comprehensively divided into those with and those without outflows. Conditioned dharmas other than the Truth of the Path are with outflows because they can serve as the field in which outflows settle; merely being taken as an outflow's object does not meet this condition.

## 6. Philosophical Translation

> The first universal division of dharmas concerns their relation to afflictive persistence. A dharma is sāsrava not because affliction can refer to it, but because affliction can lodge and continue within it. The conditioned Path is exceptional because it does not sustain that recurrence.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Determination |
|---|---|---|
| sāsrava | with outflows | capable of sustaining their settlement |
| anāsrava | without outflows | not a lodging of outflows |
| saṃskṛta | conditioned | distinct axis from outflow-status |
| mārgasatya | Truth of the Path | conditioned yet anāsrava |
| samanuśayana | settling and continuing within | criterion of sāsravatva |
| ālambana | object-support | not equivalent to lodging |

## 8. Logical Determination

```text
Sāsrava(x) ↔ outflows can settle in x
ObjectOfOutflow(x) ↛ Sāsrava(x)
Conditioned(Path) ∧ Anāsrava(Path)
```

## 9. Interpretive Note

Contamination is not mere objectification by an afflicted cognition. It is a reproductive relation: a field sustains latent affliction. The Path occurs conditionally while countering, rather than housing, that recurrence.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
vak:VAK_1_04 a vak:Karika ; vak:hasTopic vak:SasravaAnasravaDivision ; vak:belongsTo vak:Dhatunirdesa .
vak:SasravaDharma vak:lodges vak:Asrava .
vak:PathTruth a vak:ConditionedDharma, vak:AnasravaDharma .
vak:ObjectRelation vak:distinctFrom vak:LodgingRelation .
```
