# VAK_1.06

## 1. Sanskrit (Devanāgarī)

> प्रतिसंख्यानिरोधो यो विसंयोगः पृथक् पृथक् ।
>
> उत्पादात्यन्तविघ्नोऽन्यो निरोधोऽप्रतिसंख्यया ॥ १.०६ ॥॥

## 2. Sanskrit (IAST)

> pratisaṃkhyānirodho yo visaṃyogaḥ pṛthak pṛthak /
>
> utpādātyantavighno 'nyo nirodho 'pratisaṃkhyayā // 1.06 //

## 3. Lexical Analysis

| Form | Padaccheda | Meaning |
|---|---|---|
| pratisaṃkhyā-nirodhaḥ | pratisaṃkhyā-nirodhaḥ | cessation through discrimination |
| yaḥ | yaḥ | which |
| visaṃyogaḥ | visaṃyogaḥ | disjunction |
| pṛthak pṛthak | pṛthak pṛthak | separately, one by one |
| utpāda-atyanta-vighnaḥ | utpāda-atyanta-vighnaḥ | absolute obstruction of arising |
| anyaḥ | anyaḥ | the other |
| nirodhaḥ | nirodhaḥ | cessation |
| apratisaṃkhyayā | a-pratisaṃkhyayā | not through discrimination |

## 4. Grammar

The two cessations from 1.05 are now defined:

```text
pratisaṃkhyā-nirodha
    = visaṃyogaḥ pṛthak pṛthak
    = disjunction, separately and separately

apratisaṃkhyā-nirodha
    = utpāda-atyanta-vighnaḥ
    = absolute obstruction of arising
```

The first is attained through discrimination. The second is not. It is the absolute block on a future arising when conditions fail. Neither is produced as a conditioned event.

## 5. Translation

### Literal Translation

> Cessation through discrimination is disjunction, separately and separately. The other cessation, not through discrimination, is the absolute obstruction of arising.

### Bhāṣya-informed translation

> Cessation through discrimination is disjunction from Impure dharmas, separately for each conjunction. Discrimination here is a particular prajñā directed to the Noble Truths, beginning with suffering. The other cessation is not attained by that prajñā. It is the absolute obstruction of a future arising, got by deficiency of conditions.

## 6. Philosophical Translation

> One cessation is disjunction by discrimination, one conjunction at a time. The other is non-arising: a future dharma is blocked because its conditions fail. Liberation and mere non-production are not the same.

Organon note: samādhi read as deep sleep is the second cessation, not this discrimination. Not conventional English.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| pratisaṃkhyā | discrimination | Bhāṣya: a particular prajñā directed to the Noble Truths |
| nirodha | cessation | unconditioned cessation here |
| visaṃyoga | disjunction | from Impure dharmas |
| pṛthak pṛthak | separately | as many disjunctions as conjunctions |
| sāsrava | Impure | the field of disjunction |
| anāsrava | Pure | no disjunction required |
| apratisaṃkhyā | not through discrimination | attained by deficient conditions |
| utpāda | arising | of a future dharma |
| atyanta-vighna | absolute obstruction | complete prevention of arising |
| pratyayavaikalya | deficiency of conditions | how the second cessation is got |

## 8. Logical Determination

```text
ākāśa
    = non-obstruction

pratisaṃkhyā-nirodha
    = disjunction by discrimination
    = separately, one conjunction at a time

apratisaṃkhyā-nirodha
    = obstruction of arising
    = deficiency of conditions
```

```text
Impure, able to arise          first only
Pure and conditioned, unable   second only
Impure, unable to arise        both
Pure, able to arise            neither
```

## 9. Interpretive Note

Cessation through discrimination is not nothing. It is disjunction, item by item. If one seeing ended every affliction, the rest of the Path would be useless.

The other cessation is not that Path. A future arising is absolutely blocked because the conditions are gone. The eye taken by one form cannot later take what has already passed.

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
