# VAK_1.15

## 1. Sanskrit (Devanāgarī)

> चतुर्भ्योऽन्ये तु संस्कारस्कन्धः एते पुनस्त्रयः ।
>
> धर्मायतनधात्वाख्याः सहाविज्ञप्त्यसंस्कृतैः ॥ १.१५ ॥

## 2. Sanskrit (IAST)

> caturbhyo 'nye tu saṃskāraskandhaḥ ete punas trayaḥ /
>
> dharmāyatanadhātvākhyāḥ sahāvijñaptyasaṃskṛtaiḥ // VAkK_1.15 //

Source label in GRETIL: `VAkK_1.15`. Project-normalized label: `VAkK_1.15`.

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| caturbhyaḥ anye | caturbhyaḥ anye | others than the four |
| tu | tu | but |
| saṃskāra-skandhaḥ | saṃskāra-skandhaḥ | aggregate of formations |
| ete | ete | these |
| punaḥ | punaḥ | again |
| trayaḥ | trayaḥ | three |
| dharma-āyatana-dhātu-ākhyāḥ | dharma-āyatana-dhātu-ākhyāḥ | called dharma-sphere and dharma-domain |
| saha | saha | together with |
| avijñapti-asaṃskṛtaiḥ | avijñapti-asaṃskṛtaiḥ | avijñapti and the unconditioned |

## 4. Grammar

The formations aggregate is defined negatively:

```text
saṃskāraskandha
    = conditioned factors other than the four aggregates
```

The verse then gathers the three non-material/non-sensory categories as **dharmāyatana** and **dharmadhātu**:

```text
vedanā
saṃjñā
saṃskāra
+ avijñapti
+ asaṃskṛta dharmas
    = dharmāyatana / dharmadhātu
```

## 5. Literal Translation

> The others than the four are the aggregate of formations. These three again, together with avijñapti and the unconditioned, are called the dharma-sphere and dharma-domain.

## 6. Philosophical Translation

> All conditioned factors not included in the other four aggregates belong to the aggregate of formations. Feeling, saṃjñā, and formations, together with avijñapti and the unconditioned, are gathered under the dharma-sphere and dharma-domain.

Organon rendering:

> The dharma-domain begins to emerge as the gathering place of determinations not reducible to visible materiality or sensory objecthood. It includes mental factors, subtle form, and the unconditioned.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| saṃskāra | formation | conditioned formative factor |
| skandha | aggregate | structured aggregate-field |
| dharmāyatana | dharma-sphere | sixth object-sphere for manas |
| dharmadhātu | dharma-domain | domain of dharmas/determinations |
| avijñapti | non-disclosive form | included in dharma-domain |
| asaṃskṛta | unconditioned | included in dharma-domain |

## 8. Logical Determination

```text
other conditioned factors
    = saṃskāraskandha
```

and:

```text
vedanā + saṃjñā + saṃskāra
+ avijñapti
+ asaṃskṛta
    = dharmāyatana / dharmadhātu
```

## 9. Interpretive Note

This is one of the crucial early dharmadhātu verses. Dharmadhātu is not merely a leftover bin. It is the domain in which mental factors, subtle form, and the unconditioned are gathered as dharmas.

Organon note:

```text
dharmadhātu
    = domain of determinations
    = mental factors + subtle form + unconditioned
```

This prepares the later insight that dharmadhātu alone has real-domain status.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_15
    a vak:Karika ;
    rdfs:label "VAK 1.15" ;
    vak:hasSourceLabel "VAkK_1.15" ;
    vak:hasProjectLabel "VAkK_1.15" ;
    vak:hasTopic vak:FormationsAndDharmaDomain ;
    vak:belongsTo vak:Dhatunirdesa .

vak:DharmaDhatu
    vak:includes vak:Vedana , vak:Samjna , vak:Samskara , vak:Avijnapti , vak:AsamskrtaDharmas .
```

## 11. Commit History

- Added expanded Organon analysis for VAK_1.15.
- Defines saṃskāraskandha by exclusion from the other four aggregates.
- Establishes dharmāyatana/dharmadhātu as including mental factors, avijñapti, and the unconditioned.
