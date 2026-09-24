# VAK_1.07

## 1. Sanskrit (Devanāgarī)

> ते पुनः संस्कृता धर्मा रूपादिस्कन्धपञ्चकम् ।
>
> स एवाध्वा कथावस्तु सनिःसाराः सवस्तुकाः ॥ १.०७ ॥

## 2. Sanskrit (IAST)

> te punaḥ saṃskṛtā dharmā rūpādiskandhapañcakam /
>
> sa evādhvā kathāvastu saniḥsārāḥ savastukāḥ // 1.07 //


## 3. Lexical Analysis

| Form | Padaccheda | Meaning |
|---|---|---|
| te punaḥ | te punaḥ | these again |
| saṃskṛtāḥ dharmāḥ | saṃskṛtāḥ dharmāḥ | conditioned dharmas |
| rūpādi-skandha-pañcakam | rūpa-ādi-skandha-pañcakam | five aggregates beginning with form |
| saḥ eva | saḥ eva | that very same |
| adhvā | adhvā | temporal course |
| kathā-vastu | kathā-vastu | basis of discourse |
| sa-niḥsārāḥ | sa-niḥsārāḥ | possessed of an exit; the Bhāṣya identifies it as nirvāṇa |
| sa-vastukāḥ | sa-vastukāḥ | possessed of causes, under the local Vaibhāṣika gloss of `vastu` |

## 4. Grammar

The verse identifies the conditioned dharmas:

```text
saṃskṛtā dharmāḥ
    = rūpādi-skandha-pañcakam
    = the five aggregates beginning with form
```

The same conditioned field is then described as the temporal courses, basis of
discourse, possessed of an exit, and possessed of causes. The last rendering
follows the Vaibhāṣika gloss reported by the Bhāṣya; it does not set a
universal meaning for `vastu`.

## 5. Literal Translation

> Those conditioned dharmas, again, are the five aggregates beginning with form. Those very same dharmas are the temporal courses, the basis of discourse, possessed of an exit, and possessed of a basis (`vastu`).

## 6. Philosophical Translation

> Conditioned dharmas are the five aggregates beginning with material form. The same dharmas are the temporal courses and the basis of meaningful discourse; they possess nirvāṇa as their exit and, under the Vaibhāṣika explanation reported here, causes as their `vastu`.

Organon rendering:

> The conditioned field is not an abstract list. It is aggregate structure, temporal course, and basis of discourse; it is produced through causes and stands in relation to nirvāṇa as its exit. The five aggregates are the first articulated body of conditioned determination.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| saṃskṛta | conditioned | constructed by grounds and conditions |
| skandha | aggregate | structured aggregate-field |
| rūpa | form / material form-bearing domain | first aggregate |
| adhvā | temporal course | conditioned dharmas across time |
| kathāvastu | basis of discourse | what doctrinal speech concerns |
| niḥsāra | exit | nirvāṇa is the exit from everything conditioned in the Bhāṣya |
| saniḥsāra | possessed of an exit | the conditioned has nirvāṇa as its exit |
| vastu | cause in this local gloss | Vaibhāṣika explanation reported by the Bhāṣya; other uses remain open |
| savastuka | possessed of a basis; locally, with causes | causal rendering follows that attributed gloss |

## 8. Logical Determination

VAK_1.07 gives the conditioned side of the architecture:

```text
saṃskṛta dharmas
    = five aggregates
```

The same field is determined under several aspects:

```text
aggregate
    temporal course
    discourse-basis
    possessed of an exit in nirvāṇa
    possessed of causes (Vaibhāṣika gloss)
```

## 9. Interpretive Note

This verse bridges the pure division of dharmas into the analytic apparatus of aggregates. The five aggregates are not merely psychological categories. They are the whole conditioned field under aggregate-form.

Organon note:

```text
conditioned dharma
    = aggregate-structure
    = temporal course
    = basis for discourse
    = possessed of nirvāṇa as an exit
    = causally grounded under the attributed Vaibhāṣika gloss
```

The system gives several determinations of the same conditioned field.
`Savastuka` is rendered causally here because the Bhāṣya attributes that
explanation to the Vaibhāṣikas; it is not a general equation of `vastu` and
cause.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_07
    a vak:Karika ;
    rdfs:label "VAK 1.07" ;
    vak:hasTopic vak:ConditionedDharmasAsAggregates ;
    vak:belongsTo vak:Dhatunirdesa .

vak:ConditionedDharmas
    vak:identifiedWith vak:FiveAggregates ;
    vak:hasAspect vak:TemporalCourse , vak:DiscourseBasis , vak:ExitInNirvana , vak:PossessedOfCauses .
```
