# VAK_1.06 — The Two Cessations

## 1. Sanskrit (Devanāgarī)

> प्रतिसंख्यानिरोधो यो विसंयोगः पृथक् पृथक् ।
>
> उत्पादात्यन्तविघ्नोऽन्यो निरोधोऽप्रतिसंख्यया ॥ १.०६ ॥

## 2. Sanskrit (IAST)

> pratisaṃkhyānirodho yo visaṃyogaḥ pṛthak pṛthak /
>
> utpādātyantavighno 'nyo nirodho 'pratisaṃkhyayā // 1.06 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| pratisaṃkhyā-nirodhaḥ | tatpuruṣa; nominative singular | cessation through discrimination; the first named in 1.05 |
| yaḥ | relative pronoun | which |
| visaṃyogaḥ | nominative singular | disjunction; the definition |
| pṛthak pṛthak | iterated indeclinable | separately, and separately |
| utpāda-atyanta-vighnaḥ | compound; nominative singular | absolute obstruction of arising |
| anyaḥ | nominative singular | the other |
| nirodhaḥ | nominative singular | cessation |
| apratisaṃkhyayā | instrumental | not through discrimination |

## 4. Grammar

The two cessations named in 1.05 are defined.

```text
pratisaṃkhyā-nirodhaḥ
    = yaḥ visaṃyogaḥ
    = pṛthak pṛthak

anyaḥ nirodhaḥ
    = utpāda-atyanta-vighnaḥ
    = apratisaṃkhyayā
```

The first is attained through discrimination. The second is not. Neither is a conditioned event.

## 5. Translation

### Literal Translation

Cessation through discrimination is disjunction, separately and separately. The other cessation, not through discrimination, is the absolute obstruction of arising.

### Bhāṣya-informed study translation

Cessation through discrimination is disjunction from Impure dharmas, attained
separately in each case through the prajñā that discerns the Noble Truths:
there are as many disjunctions as conjunctions. The other cessation, not
attained through that discrimination, is the absolute obstruction of a future
dharma's arising when its conditions are lacking.

## 6. Philosophical Translation

Two cessations, two attainments. They are not the same unconditioned.

The first is disjunction. It is item by item. One seeing does not end every conjunction. If it did, the rest of the Path would be useless.

The second is not that Path. A future arising is absolutely blocked because the conditions fail. What has passed cannot be taken. Liberation and mere non-production are not one cessation.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| pratisaṃkhyā | discrimination | a particular prajñā of the Noble Truths |
| nirodha | cessation | unconditioned here; the two are not one |
| visaṃyoga | disjunction | from impure dharmas |
| pṛthak pṛthak | separately | as many disjunctions as conjunctions |
| sāsrava | impure | the field of the first cessation |
| anāsrava | pure | no disjunction required where it can arise |
| apratisaṃkhyā | not through discrimination | not attained by that prajñā |
| utpāda-atyanta-vighna | absolute obstruction of arising | the second definition |
| pratyaya-vaikalya | deficiency of conditions | how the second is got |

## 8. Logical Determination

```text
cessation through discrimination
    = disjunction from impure dharmas
    = one per conjunction
    = attained by discrimination

cessation not through discrimination
    = absolute obstruction of arising
    = deficiency of conditions
    = not attained by discrimination
```

```text
impure, able to arise                 first only
pure and conditioned, unable          second only
impure, unable to arise               both
pure, able to arise                   neither
```

## 9. Interpretive Note

The first cessation is not nothing. It is disjunction, separately. The second is not that disjunction. A future dharma is blocked because its conditions are gone. The eye and the mind occupied with one form cannot later take what has already passed.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_06 a vak:Karika ;
    vak:hasTopic vak:TwoCessations ;
    vak:belongsTo vak:Dhatunirdesa .

vak:PratisamkhyaNirodha a vak:UnconditionedDharma, vak:PureDharma ;
    vak:definedAs vak:Disjunction ;
    vak:attainedBy vak:Discrimination .

vak:ApratisamkhyaNirodha a vak:UnconditionedDharma, vak:PureDharma ;
    vak:definedAs vak:AbsoluteObstructionOfArising ;
    vak:attainedBy vak:DeficiencyOfConditions .
```
