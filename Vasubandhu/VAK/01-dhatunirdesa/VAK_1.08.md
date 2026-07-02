# VAK_1.08

## 1. Sanskrit (Devanāgarī)

> ये सास्रवा उपादानस्कन्धास्ते सरणा अपि ।
>
> दुःखं समुदयो लोको दृष्टिस्थानं भवश्च ते ॥ १.०८ ॥

## 2. Sanskrit (IAST)

> ye sāsravā upādānaskandhās te saraṇā api /
>
> duḥkhaṃ samudayo loko dṛṣṭisthānaṃ bhavaś ca te // VAkK_1.08 //

Source label in GRETIL: `VAkK_1.8`. Project-normalized label: `VAkK_1.08`.

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
    = aggregates of appropriation
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

> The aggregates that are permeated by outflows are the appropriated aggregates. The same field is designated as suffering, origin, world, the seat of views, and becoming.

Organon rendering:

> When the aggregate-field is taken up by outflow and appropriation, it becomes the world of bondage. It is suffering because it is unstable and appropriated; origin because it generates further becoming; world because it is the field of appearance; view-place because false seeing fixes itself there; becoming because it continues the cycle.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| sāsrava | with outflows | field in which āsrava adheres |
| upādāna | appropriation / clinging | taking-up as mine/for self |
| upādānaskandha | aggregate of appropriation | sāsrava aggregate-field |
| duḥkha | suffering | conditioned appropriation as instability |
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

This verse is the first explicit transformation of neutral analysis into path-analysis. The same aggregate-field becomes suffering and world when it is sāsrava and appropriated.

The point is not that aggregates as such are evil. Rather:

```text
aggregate + outflow + appropriation
    = world of bondage
```

This prepares the later doctrine that seeing does not destroy the real. It removes the false appropriation and view-structure that make the aggregate-field into saṃsāric becoming.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_08
    a vak:Karika ;
    rdfs:label "VAK 1.08" ;
    vak:hasSourceLabel "VAkK_1.8" ;
    vak:hasProjectLabel "VAkK_1.08" ;
    vak:hasTopic vak:AppropriatedAggregates ;
    vak:belongsTo vak:Dhatunirdesa .

vak:UpadanaSkandha
    a vak:AggregateStatus ;
    rdfs:label "aggregate of appropriation" ;
    vak:hasDetermination vak:Duhkha , vak:Samudaya , vak:Loka , vak:Drstisthana , vak:Bhava .
```

## 11. Commit History

- Added expanded Organon analysis for VAK_1.08.
- Normalized project verse numbering to padded lexical form.
- Identifies sāsrava aggregates as upādānaskandhas.
- Establishes the appropriated aggregate-field as suffering, origin, world, view-place, and becoming.
