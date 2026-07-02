# VAK_1.3

## 1. Sanskrit (Devanāgarī)

> धर्माणां प्रविचयमन्तरेण नास्ति क्लेशानां यत उपशान्तयेऽभ्युपायः ।
>
> क्लेशैश्च भ्रमति भवार्णवेऽत्र लोकस्तद्धेतोरत उदितः किलैष शास्त्रः ॥ १.३ ॥

## 2. Sanskrit (IAST)

> dharmāṇāṃ pravicayam antareṇa nāsti kleśānāṃ yata upaśāntaye 'bhyupāyaḥ /
>
> kleśaiś ca bhramati bhavārṇave 'tra lokas taddhetor ata uditaḥ kilaiṣa śāstraḥ // VAkK_1.3 //

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| dharmāṇām | dharmāṇām | of dharmas |
| pravicayam | pravicayam | discriminative analysis, investigation |
| antareṇa | antareṇa | without |
| nāsti | na asti | there is not |
| kleśānām | kleśānām | of the defilements |
| upaśāntaye | upaśāntaye | for pacification |
| abhyupāyaḥ | abhyupāyaḥ | adequate means, method |
| kleśaiḥ ca | kleśaiḥ ca | and by defilements |
| bhramati | bhramati | wanders |
| bhava-arṇave | bhava-arṇave | in the ocean of becoming |
| lokaḥ | lokaḥ | the world |
| tad-hetoḥ | tad-hetoḥ | for that reason |
| ataḥ | ataḥ | therefore |
| uditaḥ | uditaḥ | spoken, taught, arisen |
| eṣaḥ śāstraḥ | eṣaḥ śāstraḥ | this treatise |

## 4. Grammar

The argument is explicit:

```text
without pravicaya of dharmas
    there is no method for pacifying kleśas

because of kleśas
    the world wanders in the ocean of becoming

therefore
    this śāstra has been taught
```

The key term is **pravicaya**: discriminative investigation of dharmas. This is the operational form of prajñā introduced in VAK_1.2.

## 5. Literal Translation

> Without discriminative analysis of dharmas, there is no adequate means for the pacification of the defilements. And by the defilements the world wanders here in the ocean of becoming. For that reason, therefore, this treatise has been taught.

## 6. Philosophical Translation

> The pacification of affliction requires discriminative analysis of dharmas. Because beings wander in the ocean of becoming under the power of kleśa, the Abhidharma śāstra is taught as the method of Dharma-discrimination.

Organon rendering:

> Liberation requires the analysis of determinations. Kleśa persists where Dharma is not discriminated. The world wanders in becoming because its determinations are confused. Abhidharma is therefore the śāstric means by which Dharma becomes knowable and affliction is pacified.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| dharma | determination / law | object of pravicaya |
| pravicaya | discriminative analysis | analytic operation of prajñā |
| kleśa | defilement / affliction | what obscures and agitates |
| upaśānti | pacification | stilling of kleśa |
| abhyupāya | adequate means | effective method |
| bhava-arṇava | ocean of becoming | saṃsāric field of wandering |
| śāstra | treatise | taught because pravicaya is necessary |

## 8. Logical Determination

The verse establishes the necessity of Abhidharma:

```text
kleśa
    ↓
wandering in becoming
    ↓
need for pacification
    ↓
pravicaya of dharmas
    ↓
śāstra
```

Thus Dharma-analysis is not optional. It is the adequate means to pacify affliction.

## 9. Interpretive Note

This verse gives the methodological core of the chapter. The reason for enumerating dharmas is not taxonomy. It is pacification through discriminative knowing.

This is why the project rendering **dharma = determination / law** matters. The world wanders because determinations are not known as determinations. Kleśa is confusion in the field of appearance. Pravicaya restores lawful discrimination.

Organon note:

```text
pravicaya
    = analysis of determinate Dharma

kleśa
    = confused projection

upaśānti
    = pacification through principle
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_3
    a vak:Karika ;
    rdfs:label "VAK 1.3" ;
    vak:hasIAST "dharmāṇāṃ pravicayam antareṇa nāsti kleśānāṃ yata upaśāntaye 'bhyupāyaḥ / kleśaiś ca bhramati bhavārṇave 'tra lokas taddhetor ata uditaḥ kilaiṣa śāstraḥ" ;
    vak:hasTopic vak:NecessityOfPravicaya ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Pravicaya
    a vak:Method ;
    rdfs:label "discriminative analysis of dharmas" ;
    vak:pacifies vak:Klesa .
```

## 11. Commit History

- Added first-pass expanded Organon analysis for VAK_1.3.
- Establishes pravicaya of dharmas as necessary for pacifying kleśa.
- Frames Abhidharma as method for ending wandering in the ocean of becoming.
