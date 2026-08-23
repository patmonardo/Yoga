# VAK_1.08

## 1. Sanskrit (Devanāgarī)

> ये सास्रवा उपादानस्कन्धास्ते सरणा अपि ।
>
> दुःखं समुदयो लोको दृष्टिस्थानं भवश्च ते ॥ १.०८ ॥

## 2. Sanskrit (IAST)

> ye sāsravā upādānaskandhās te saraṇā api /
>
> duḥkhaṃ samudayo loko dṛṣṭisthānaṃ bhavaś ca te // 1.08 //


## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| ye | ye | whichever / those which |
| sāsravāḥ | sāsravāḥ | with outflows |
| upādāna-skandhāḥ | upādāna-skandhāḥ | aggregates of appropriation/clinging |
| te | te | they |
| saraṇāḥ api | saraṇāḥ api | also with conflict / vulnerable course; term to review |
| duḥkham | duḥkham | suffering |
| samudayaḥ | samudayaḥ | origin / arising-source |
| lokaḥ | lokaḥ | world |
| dṛṣṭi-sthānam | dṛṣṭi-sthānam | seat/place of view |
| bhavaḥ ca | bhavaḥ ca | and becoming |
| te | te | they |

## 4. Grammar

The verse identifies the **sāsrava aggregates** as **upādāna-skandhas**:

```text
sāsrava skandhas
    = consequential aggregates
    = aggregates of clinging
```

The same sāsrava aggregate-field is then named under several doctrinal determinations:

```text
duḥkha
samudaya
loka
dṛṣṭisthāna
bhava
```

These are not separate substances. They are different determinations of the appropriated aggregate-field.

## 5. Literal Translation

> Those which are with outflows are the aggregates of appropriation; they are also saraṇa. They are suffering, origin, world, place of view, and becoming.

## 6. Philosophical Translation

> The consequential aggregates are the aggregates of clinging. The same field is suffering, origin, world, the seat of views, and becoming.

Organon rendering:

> When outflow settles in the aggregate-field, the aggregates become consequential: each determination passes into a further determination. Clinging is this fixation of the consequential field as independently subsistent. The field is suffering as unresolved contradiction, origin as the generation of consequence, world as the field of appearance, view-place as fixed cognition, and becoming as the continuation of the series.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| sāsrava | consequential (lit. with outflows) | field from which a further consequential series proceeds |
| upādāna | clinging / appropriation | fixation of a determination as independently subsistent |
| upādānaskandha | aggregate of clinging | consequential aggregate-field |
| duḥkha | suffering | unresolved contradiction in the consequential field |
| samudaya | origin | source of further becoming |
| loka | world | appearance-field of sāsrava aggregates |
| dṛṣṭisthāna | place of view | support of false or fixed views |
| bhava | becoming | ongoing conditioned existence |

## 8. Logical Determination

VAK_1.07 identified conditioned dharmas with the five aggregates. VAK_1.08 adds the bondage determination:

```text
conditioned aggregates
    when sāsrava
        = upādānaskandhas
```

The appropriated aggregate-field is:

```text
duḥkha
samudaya
loka
dṛṣṭisthāna
bhava
```

## 9. Interpretive Note

This verse is the first explicit transformation of neutral analysis into consequential Science. The aggregate-field becomes suffering and world when it is consequential and held in clinging. `Āsrava` is therefore rendered rationally as consequence: the outflow by which a principle develops into a series of determinations.

The point is not that aggregates as such are evil. Rather:

```text
aggregate + consequence + clinging
    = unresolved world-series
```

Seeing does not destroy the consequential field. It dissolves the clinging and fixed view-structure that prevent consequence from being comprehended as the necessary development of its principle. `Anāsrava`, the unconsequential, is consequently not an empty absence: it is the completion of the series without a further unresolved outflow.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_08
    a vak:Karika ;
    rdfs:label "VAK 1.08" ;
    vak:hasTopic vak:AppropriatedAggregates ;
    vak:belongsTo vak:Dhatunirdesa .

vak:UpadanaSkandha
    a vak:AggregateStatus ;
    rdfs:label "aggregate of clinging" ;
    vak:hasDetermination vak:Duhkha , vak:Samudaya , vak:Loka , vak:Drstisthana , vak:Bhava .
```
