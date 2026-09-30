# VAK_1.06

## 1. Sanskrit (Devanāgarī)

> प्रतिसंख्यानिरोधो यो विसंयोगः पृथक् पृथक् ।
>
> उत्पादात्यन्तविघ्नोऽन्यो निरोधोऽप्रतिसंख्यया ॥ १.०६ ॥

## 2. Sanskrit (IAST)

> pratisaṃkhyānirodho yo visaṃyogaḥ pṛthak pṛthak /
>
> utpādātyantavighno 'nyo nirodho 'pratisaṃkhyayā // 1.06 //


## 3. Lexical Analysis

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

The first is cessation attained through discriminative knowing. The second is attained without that discrimination, when deficiency of conditions absolutely prevents a future dharma from arising. Neither unconditioned cessation is produced as a conditioned event.

## 5. Literal Translation

> Cessation through discrimination is disjunction, separately and separately. The other cessation, not through discrimination, is the absolute obstruction of arising.

## 6. Philosophical Translation

> Pratisaṃkhyā-nirodha is attained through a specific prajñā directed to the Noble Truths: it is disjunction from dharmas with outflows, separately for each conjunction. Apratisaṃkhyā-nirodha is attained through deficiency of conditions: it is the absolute obstruction of a future arising, without discriminative insight being its means.

Organon rendering:

> Cessation is twofold. One is principled release: Dharma is discriminated, and bondage is severed one determination at a time. The other is non-arising: a determination is blocked from manifestation. Thus the unconditioned includes both liberating disjunction and absolute non-production.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| pratisaṃkhyā | discriminative consideration | a specific prajñā directed to the Noble Truths in the Bhāṣya |
| nirodha | cessation | unconditioned cessation here |
| visaṃyoga | disjunction / separation | specifically from dharmas with outflows in the Bhāṣya |
| pṛthak pṛthak | separately | each defilement/determination severed distinctly |
| apratisaṃkhyā | not through discriminative consideration | cessation is attained through deficient conditions rather than through that prajñā |
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
