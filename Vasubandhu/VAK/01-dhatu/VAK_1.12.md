# VAK_1.12

## 1. Sanskrit (Devanāgarī)

> भूतानि पृथिवीधातुरप्तेजोवायुधातवः ।
>
> धृत्यादिकर्मसंसिद्धाः खरस्नेहोष्णतेरणाः ॥ १.१२ ॥

## 2. Sanskrit (IAST)

> bhūtāni pṛthivīdhātur aptejovāyudhātavaḥ /
>
> dhṛtyādikarmasaṃsiddhāḥ kharasnehoṣṇateraṇāḥ // VAkK_1.12 //

Source label in GRETIL: `VAkK_1.12`. Project-normalized label: `VAkK_1.12`.

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| bhūtāni | bhūtāni | the elements / become-bases |
| pṛthivī-dhātuḥ | pṛthivī-dhātuḥ | earth-domain |
| ap-tejo-vāyu-dhātavaḥ | ap-tejas-vāyu-dhātavaḥ | water, fire, and wind domains |
| dhṛti-ādi-karma-saṃsiddhāḥ | dhṛti-ādi-karma-saṃsiddhāḥ | established by functions beginning with support |
| khara | khara | hard, resistant |
| sneha | sneha | cohesion, moistness |
| uṣṇatā | uṣṇatā | heat |
| īraṇā | īraṇā | motion, impulsion |

## 4. Grammar

The four **mahābhūtas** are named as domains:

```text
pṛthivī-dhātu
ap-dhātu
tejo-dhātu
vāyu-dhātu
```

They are established through function and characteristic:

```text
earth  = hardness / support
water  = cohesion
fire   = heat / maturation
wind   = motion / impulsion
```

## 5. Literal Translation

> The elements are the earth-domain, and the water-, fire-, and wind-domains. They are established by functions beginning with support: hardness, cohesion, heat, and motion.

## 6. Philosophical Translation

> The great elements are not inert stuffs but functional domains. Earth supports through hardness, water coheres, fire heats and matures, and wind moves or impels.

Organon rendering:

> Materiality begins from four functional determinations. Earth, water, fire, and wind are not substances lying under qualities; they are elemental domains whose reality is known through support, cohesion, transformation, and motion.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| bhūta | element / become-basis | elemental basis of derivative form |
| dhātu | domain | never merely element in this project layer |
| pṛthivī | earth | hardness/support function |
| ap | water | cohesion |
| tejas | fire | heat, maturation |
| vāyu | wind | motion, impulsion |
| karma | function | element known through operation |

## 8. Logical Determination

```text
mahābhūta
    = elemental domain
    = functionally established
```

The four functions are:

```text
support
cohesion
heating / maturation
motion
```

## 9. Interpretive Note

This is not naive physics. The so-called elements are functional conditions of material manifestation. They are dhātus because they are domains of operation.

Organon note:

```text
element
    = functional domain

materiality
    = support + cohesion + heat + motion
```

This prepares VAK_1.35, where derivative materiality is grounded on the great elements.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_12
    a vak:Karika ;
    rdfs:label "VAK 1.12" ;
    vak:hasSourceLabel "VAkK_1.12" ;
    vak:hasProjectLabel "VAkK_1.12" ;
    vak:hasTopic vak:FourGreatElements ;
    vak:belongsTo vak:Dhatunirdesa .

vak:EarthDomain vak:hasFunction vak:Support .
vak:WaterDomain vak:hasFunction vak:Cohesion .
vak:FireDomain vak:hasFunction vak:Heat .
vak:WindDomain vak:hasFunction vak:Motion .
```

## 11. Commit History

- Added expanded Organon analysis for VAK_1.12.
- Interprets the four great elements as functional domains.
- Establishes materiality through support, cohesion, heat, and motion.
