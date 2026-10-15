# VAK_1.26 — The Measure of a Dharma-Collection

## 1. Sanskrit (Devanāgarī)

> शास्त्रप्रमाण इत्येके स्कन्धादीनां कथैकशः ।
>
> चरितप्रतिपक्षस्तु धर्मस्कन्धोऽनुवर्णितः ॥ १.२६ ॥

## 2. Sanskrit (IAST)

> śāstrapramāṇa ity eke skandhādīnāṃ kathaikaśaḥ /
>
> caritapratipakṣas tu dharmaskandho 'nuvarṇitaḥ // 1.26 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| śāstrapramāṇaḥ | śāstra-pramāṇa; nominative masculine singular | a treatise is the measure; said of the dharma-collection |
| iti | quotative | the reported account |
| eke | nominative masculine plural | some |
| skandhādīnām | skandha-ādīnām; genitive plural | of the bases and the rest |
| kathā | nominative feminine singular | exposition |
| ekaśaḥ | distributive | each separately |
| caritapratipakṣaḥ | carita-pratipakṣa; nominative masculine singular | a counteragent to a disposition |
| tu | particle | but; the account that is described |
| dharmaskandhaḥ | dharma-skandha; nominative masculine singular | a dharma-collection; not a sixth base |
| anuvarṇitaḥ | past passive participle | has been described |

The research verse has `śāstrapramāṇā`. The running verse and the commentary read `śāstrapramāṇa`. That reading is kept. The long vowel is recorded, not adopted.

## 4. Grammar

```text
śāstra-pramāṇaḥ iti eke
    some: the measure is a treatise

skandha-ādīnām kathā ekaśaḥ
    an exposition of each of the bases and the rest

carita-pratipakṣaḥ tu dharmaskandhaḥ anuvarṇitaḥ
    but a dharma-collection is described as a counteragent to a disposition
```

The first clause is elliptical. The commentary supplies the dharma-collection as what is measured. The second clause has an understood “others say,” and an understood predicate: each exposition is one collection. The third clause is complete. `Tu` contrasts. It does not say the first two are false.

## 5. Translation

### Literal Translation

Some say the measure is a treatise; an exposition of each of the bases and the rest. But a dharma-collection is described as a counteragent to a disposition.

### Bhāṣya-informed study translation

What is the measure of a dharma-collection? Some say a treatise is its measure. They mean the Abhidharma treatise named Dharmaskandha. That is six thousand. The unit is not stated.

Others say: an exposition of each of the bases and the rest. An exposition of each of the bases, the essences, the principles, dependent arising, the truths, the nutriments, the concentrations, the immeasurables, the formless attainments, the liberations, the masteries, the totalities, the factors of awakening, the higher knowledges, the discriminations, knowledge through resolve, freedom from conflict, and the rest, is a dharma-collection.

But a dharma-collection is described as a counteragent to a disposition. They explain it thus. Beings have eighty thousand dispositions, differentiated by attachment, hatred, delusion, pride, and the other dispositions. As counteragents to these, the Blessed One taught eighty thousand dharma-collections.

## 6. Philosophical Translation

Three measures. The verse does not choose by erasing.

Some measure the collection by a treatise. The treatise named Dharmaskandha is six thousand. The unit is not given.

Others measure it by exposition. Each topic, separately. The bases and the rest are the topics. A topic is not a further base.

But the collection that is described is a counteragent to a disposition. Eighty thousand dispositions. Eighty thousand collections. The count is the correspondence. The pairings are not listed.

The word is a teaching-collection. It is not a member of the five bases. It does not reopen the essence called form, or the essence called dharma.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| dharmaskandha | dharma-collection | a teaching-unit; not a sixth base |
| pramāṇa | measure | extent; not a means of knowledge |
| śāstra | treatise | the work named Dharmaskandha |
| ṣaṭsahasrāṇi | six thousand | unit unstated |
| kathā | exposition | the second measure |
| ekaśaḥ | each separately | not one collective topic |
| skandha | base | in the topic list; the five |
| āyatana | essence | in the topic list; the twelve |
| dhātu | principle | in the topic list; the eighteen |
| carita | disposition | attachment, hatred, delusion, pride, and the rest |
| pratipakṣa | counteragent | the third measure |
| aśītisahasra | eighty thousand | dispositions, and collections |

## 8. Logical Determination

```text
what is the measure of one dharma-collection

some
    treatise
    the work named Dharmaskandha
    six thousand
    unit unstated

others
    exposition of each topic
    bases, essences, principles, and the rest
    each exposition is one collection

but, described
    counteragent to a disposition
    eighty thousand dispositions
    eighty thousand collections
    correspondence, not a listing

tu
    contrasts
    does not refute the first two

not a base
not the essence called form
not the essence called dharma

1.27 not opened
```

## 9. Interpretive Note

The hinge is `tu`. The form system has already named its positions. This verse meets the word that looks like a further base. The word is a collection of teaching, and the collection that is described is the counteragent. Assignment of other scriptural names is the next verse.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_26 a vak:Karika ;
    vak:hasTopic vak:DharmaCollectionMeasure ;
    vak:belongsTo vak:Dhatunirdesa .

vak:DharmaCollection vak:notA vak:Base ;
    vak:measuredBy vak:Treatise, vak:Exposition, vak:Counteragent .

vak:Counteragent vak:correspondsTo vak:Disposition ;
    vak:count 80000 .
vak:DharmaskandhaTreatise vak:count 6000 ;
    vak:unitUnstated true .
```
