# VAK_1.20

## 1. Sanskrit (Devanāgarī)

> राश्यायद्वारगोत्रार्थाः स्कन्धायतनधातवः ।
>
> मोहेन्द्रियरुचित्रैधात्तिस्रः स्कन्धादिदेशनाः ॥ १.२० ॥

## 2. Sanskrit (IAST)

> rāśyāyadvāragotrārthāḥ skandhāyatanadhātavaḥ /
>
> mohendriyarucitraidhāt tisraḥ skandhādideśanāḥ // VAkK_1.20 //

Source label in GRETIL: `VAkK_1.20`. Project-normalized label: `VAkK_1.20`.

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| rāśi-arthaḥ | rāśi-arthaḥ | aggregate has the meaning of heap/collection |
| āya-dvāra-arthaḥ | āya-dvāra-arthaḥ | sphere has the meaning of entrance/gateway |
| gotra-arthaḥ | gotra-arthaḥ | domain has the meaning of lineage/source-kind |
| skandha-āyatana-dhātavaḥ | skandha-āyatana-dhātavaḥ | aggregates, spheres, domains |
| moha-indriya-ruci-traidhāt | moha-indriya-ruci-traidhāt | because of threefold delusion, faculty, and inclination |
| tisraḥ | tisraḥ | three |
| skandha-ādi-deśanāḥ | skandha-ādi-deśanāḥ | teachings beginning with aggregates |

## 4. Grammar

The verse defines the three analytic schemes by their meanings:

```text
skandha
    = rāśi, collection/aggregate

āyatana
    = āya-dvāra, entrance/gateway

dhātu
    = gotra, lineage/source-kind/domain-family
```

It also gives the pedagogical reason for three teachings: beings differ by delusion, faculty, and inclination.

## 5. Literal Translation

> Aggregates, spheres, and domains have the meanings of collection, entrance-gateway, and lineage. Because of the threefold difference in delusion, faculties, and inclinations, there are three teachings beginning with aggregates.

## 6. Philosophical Translation

> The aggregates analyze dharmas as collections; the spheres analyze them as gateways of relation; the domains analyze them as source-kinds or domain-families. The Buddha teaches these three schemes because beings differ in confusion, capacity, and disposition.

Organon rendering:

> The three systems are not redundant lists. They are three lawful pedagogical forms: aggregate for collection, sphere for access, domain for generative kind. The teaching adapts to the structure of the learner while preserving the one Dharma-field.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| skandha | aggregate | rāśi: collection/aggregate structure |
| āyatana | sphere | āya-dvāra: gateway or access-field |
| dhātu | domain | gotra: lineage/source-kind |
| deśanā | teaching | pedagogical exposition |
| moha | delusion | confusion-type of learner |
| indriya | faculty | capacity of learner |
| ruci | inclination | disposition/preference |

## 8. Logical Determination

```text
skandha
    = collection-form

āyatana
    = access-form

dhātu
    = domain/source-form
```

The three teachings are grounded in:

```text
threefold learner-condition:
    moha
    indriya
    ruci
```

## 9. Interpretive Note

This verse explains why the chapter uses three schemes. They are not merely different taxonomies. Each reveals the same Dharma-field under a distinct logical form.

Organon note:

```text
aggregate
    = determination as collection

sphere
    = determination as gateway of relation

domain
    = determination as source-kind / generative family
```

This is a profound pedagogical principle: doctrine is shaped to the capacities and confusions of the learner without sacrificing truth.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_20
    a vak:Karika ;
    rdfs:label "VAK 1.20" ;
    vak:hasSourceLabel "VAkK_1.20" ;
    vak:hasProjectLabel "VAkK_1.20" ;
    vak:hasTopic vak:ThreeAnalyticTeachings ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Skandha vak:hasMeaning vak:Rasi .
vak:Ayatana vak:hasMeaning vak:AyaDvara .
vak:Dhatu vak:hasMeaning vak:Gotra .
```

## 11. Commit History

- Upgraded VAK_1.20 with expanded Organon analysis.
- Defines skandha, āyatana, and dhātu through rāśi, āya-dvāra, and gotra.
- Explains the three teaching schemes by differences in delusion, faculties, and inclinations.
