# VAK_1.08

## 1. Sanskrit (Devanāgarī)

> ये सास्रवा उपादानस्कन्धास्ते सरणा अपि ।
>
> दुःखं समुदयो लोको दृष्टिस्थानं भवश्च ते ॥ १.०८ ॥

## 2. Sanskrit (IAST)

> ye sāsravā upādānaskandhās te saraṇā api /
>
> duḥkhaṃ samudayo loko dṛṣṭisthānaṃ bhavaś ca te // 1.08 //


## 3. Lexical Analysis

| Form | Padaccheda | Meaning |
|---|---|---|
| ye | ye | whichever / those which |
| sāsravāḥ | sāsravāḥ | with outflows |
| upādāna-skandhāḥ | upādāna-skandhāḥ | aggregates of appropriation/clinging |
| te | te | they |
| saraṇāḥ api | saraṇāḥ api | also accompanied by conflict, as explained by the Bhāṣya |
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

> Those aggregates which are with outflows are the aggregates of appropriation; they are also accompanied by conflict. They are suffering, origin, world, the station of views, and becoming.

## 6. Philosophical Translation

> Aggregates with outflows are aggregates of appropriation and are accompanied by conflict. The Bhāṣya relates them to afflictions in three ways: they arise from appropriation, are governed by it, and give rise to more of it. This same field is suffering because it is adverse to the noble ones, origin because suffering arises from it, world because it breaks down, the station of views because views lie latent there, and becoming because it comes to be.

Organon rendering (project reconstruction):

> The three relations between appropriation and the aggregates form a reciprocal pattern: affliction shapes a conditioned field that can generate further affliction. “Consequential” may name this pattern in the Organon, but it is not a translation of `sāsrava`. Seeing or manifestation alone does not entail appropriation; the Bhāṣya here concerns the aggregate-field in which afflictions can lie latent.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| sāsrava | with outflows | the relevant afflictions can lie latent in this field |
| upādāna | appropriation | identified here with afflictions; cause, governor, and product in three derivations |
| upādānaskandha | aggregate of appropriation | sāsrava aggregate; not every aggregate is one |
| saraṇa | accompanied by conflict | afflictions injure self and others and lie latent here |
| duḥkha | suffering | adverse to the noble ones in this derivation |
| samudaya | origin | suffering arises from this field |
| loka | world | explained by breaking down, following the marked `lujyata` reading |
| dṛṣṭisthāna | station of views | views stand here through latency |
| bhava | becoming | that which comes to be |

## 8. Logical Determination

VAK_1.07 identified conditioned dharmas with the five aggregates. VAK_1.08 adds the bondage determination:

```text
conditioned aggregates
    when sāsrava
        = upādānaskandhas
```

The appropriated aggregate-field is:

```text
saraṇa
duḥkha
samudaya
loka
dṛṣṭisthāna
bhava
```

## 9. Interpretive Note

The Bhāṣya restricts appropriation-aggregates to aggregates with outflows; it
does not make every conditioned aggregate an aggregate of appropriation.
Its three derivations give a reciprocal pattern:

```text
appropriation → sāsrava aggregates → further appropriation
                 ↑ governed by appropriation
```

The Organon may study this as a reproductive structure of affliction. That is
a project interpretation, not a claim that manifestation or seeing itself
produces clinging. The source still distinguishes conditioned aggregates
without outflows from this appropriated field.

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
    vak:hasDetermination vak:Sarana , vak:Duhkha , vak:Samudaya , vak:Loka , vak:Drstisthana , vak:Bhava .
```
