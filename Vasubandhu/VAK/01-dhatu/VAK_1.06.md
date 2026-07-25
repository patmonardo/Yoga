# VAK_1.06

## 1. Sanskrit (Devanāgarī)

> प्रतिसंख्यानिरोधो यो विसंयोगः पृथक् पृथक् ।
>
> उत्पादात्यन्तविघ्नोऽन्यो निरोधोऽप्रतिसंख्यया ॥ १.०६ ॥

## 2. Sanskrit (IAST)

> pratisaṃkhyānirodho yo visaṃyogaḥ pṛthak pṛthak /
>
> utpādātyantavighno 'nyo nirodho 'pratisaṃkhyayā // VAkK_1.06 //

Source label in GRETIL: `VAkK_1.6`. Project-normalized label: `VAkK_1.06`.

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| pratisaṃkhyā-nirodhaḥ | pratisaṃkhyā-nirodhaḥ | cessation through discriminative insight |
| yaḥ | yaḥ | which |
| visaṃyogaḥ | visaṃyogaḥ | disjunction, separation, release |
| pṛthak pṛthak | pṛthak pṛthak | separately, one by one |
| utpāda-atyanta-vighnaḥ | utpāda-atyanta-vighnaḥ | absolute obstruction of arising |
| anyaḥ | anyaḥ | the other |
| nirodhaḥ | nirodhaḥ | cessation |
| apratisaṃkhyayā | a-pratisaṃkhyayā | not through discriminative insight |

## 4. Grammar

The two cessations from VAK_1.05 are now defined:

```text
pratisaṃkhyā-nirodha
    = visaṃyogaḥ pṛthak pṛthak
    = disjunction separately, item by item

apratisaṃkhyā-nirodha
    = utpāda-atyanta-vighnaḥ
    = absolute obstruction of arising
```

The first is cessation through discriminative knowing. The second is cessation not produced by such analysis, but by the definitive non-arising of a dharma due to the absence or blockage of its conditions.

## 5. Literal Translation

> Cessation through discrimination is disjunction, separately and separately. The other cessation, not through discrimination, is the absolute obstruction of arising.

## 6. Philosophical Translation

> Pratisaṃkhyā-nirodha is the cessation that occurs through discriminative insight, the separate disjunction from each object of bondage. Apratisaṃkhyā-nirodha is another cessation: the complete prevention of arising, not produced by discriminative analysis.

Organon rendering:

> Cessation is twofold. One is principled release: Dharma is discriminated, and bondage is severed one determination at a time. The other is non-arising: a determination is blocked from manifestation. Thus the unconditioned includes both liberating disjunction and absolute non-production.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| pratisaṃkhyā | discrimination / analytic insight | principled discrimination of dharmas |
| nirodha | cessation | unconditioned cessation here |
| visaṃyoga | disjunction / separation | release from bondage |
| pṛthak pṛthak | separately | each defilement/determination severed distinctly |
| apratisaṃkhyā | not through discrimination | not produced by insight |
| utpāda | arising | production/manifestation of a dharma |
| atyanta-vighna | absolute obstruction | complete prevention of arising |

## 8. Logical Determination

VAK_1.06 completes the threefold unconditioned:

```text
ākāśa
    = non-obstruction

pratisaṃkhyā-nirodha
    = discriminative disjunction

apratisaṃkhyā-nirodha
    = obstruction of arising
```

The two cessations are not identical:

```text
release by insight
    ≠
non-arising by obstruction
```

## 9. Interpretive Note

This verse is crucial for the project because it separates liberation from mere absence. Pratisaṃkhyā-nirodha is not nothingness. It is disjunction through prajñā: the analytic cutting of bondage.

Apratisaṃkhyā-nirodha is also not ordinary absence. It is the absolute non-arising of a dharma due to the blocking of its conditions. The unconditioned therefore has a rich structure:

```text
openness
release
non-arising
```

Organon note:

```text
ākāśa
    = open field

pratisaṃkhyā-nirodha
    = liberation by principle

apratisaṃkhyā-nirodha
    = non-manifestation by blocked arising
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_06
    a vak:Karika ;
    rdfs:label "VAK 1.06" ;
    vak:hasSourceLabel "VAkK_1.6" ;
    vak:hasProjectLabel "VAkK_1.06" ;
    vak:hasTopic vak:TwoCessations ;
    vak:belongsTo vak:Dhatunirdesa .

vak:PratisamkhyaNirodha
    a vak:UnconditionedDharma ;
    rdfs:label "cessation through discrimination" ;
    vak:definedAs vak:Visamyoga .

vak:ApratisamkhyaNirodha
    a vak:UnconditionedDharma ;
    rdfs:label "cessation not through discrimination" ;
    vak:definedAs vak:AbsoluteObstructionOfArising .
```

## 11. Commit History

- Added expanded Organon analysis for VAK_1.06.
- Normalized project verse numbering to padded lexical form.
- Defines **pratisaṃkhyā-nirodha** as discriminative disjunction.
- Defines **apratisaṃkhyā-nirodha** as absolute obstruction of arising.
- Completes the initial account of the three unconditioned dharmas.
