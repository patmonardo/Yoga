# VAK_1.15 — Formations and the Dharma Classifications

## 1. Sanskrit (Devanāgarī)

> चतुर्भ्योऽन्ये तु संस्कारस्कन्धः एते पुनस्त्रयः ।
>
> धर्मायतनधात्वाख्याः सहाविज्ञप्त्यसंस्कृतैः ॥ १.१५ ॥

## 2. Sanskrit (IAST)

> caturbhyo 'nye tu saṃskāraskandhaḥ ete punas trayaḥ /
>
> dharmāyatanadhātvākhyāḥ sahāvijñaptyasaṃskṛtaiḥ // 1.15 //

## 3. Lexical Analysis

```text
caturbhyo 'nye tu saṃskāraskandhaḥ
    → caturbhyaḥ + anye + tu + saṃskāraskandhaḥ
ete punas trayaḥ
    → ete + punaḥ + trayaḥ
dharmāyatanadhātvākhyāḥ
    → dharma-āyatana-dhātu-ākhyāḥ
sahāvijñaptyasaṃskṛtaiḥ
    → saha + avijñapti + asaṃskṛtaiḥ
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| caturbhyaḥ | ablative plural | apart from the four |
| anye | nominative masculine plural | the others |
| saṃskāraskandhaḥ | nominative masculine singular | Formations Base |
| ete | nominative masculine plural | these |
| punaḥ | indeclinable | further; resumes the prior group |
| trayaḥ | nominative masculine plural numeral | three |
| dharmāyatanadhātvākhyāḥ | nominative masculine plural compound | named as Dharma Essence and Dharma Principle |
| saha | indeclinable | together with; governs the instrumental |
| avijñaptyasaṃskṛtaiḥ | instrumental plural compound | with *avijñapti* and the unconditioned |

## 4. Grammar

```text
the others apart from the four
    = Formations Base

these three
    together with avijñapti and the unconditioned
    = Dharma Essence and Dharma Principle
```

The Bhāṣya identifies the four as Form, Feeling, Reflection, and Cognition
Bases. “These three” are Feeling, Reflection, and Formations Bases.

## 5. Translation

### Literal Translation

The others, apart from the four, are the Formations Base. These three,
together with *avijñapti* and the unconditioned, are named Dharma Essence
and Dharma Principle.

### Bhāṣya-informed study translation

The remaining conditioned formations constitute the Formations Base. The
Feeling, Reflection, and Formations Bases, together with *avijñapti* and
the three unconditioned dharmas, are classified as Dharma Essence and
Dharma Principle.

## 6. Systematic Placement

The Formations Base completes the five-Base classification. The Bhāṣya
counts seven constituents under the Dharma classifications: the three Bases
just named, *avijñapti*, and the three unconditioned dharmas. *Avijñapti*
retains its Form Base classification; the unconditioned have no Base.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| saṃskāra-skandha | Formations Base | the remaining conditioned formations |
| dharmāyatana | Dharma Essence | one of the two designations |
| dharmadhātu | Dharma Principle | the other designation |
| ākhyā | designation | naming |
| avijñapti | Form Controller | retains its Form Base classification |
| asaṃskṛta | unconditioned | three unconditioned dharmas are included |

## 8. Logical Determination

```text
other conditioned formations
    → Formations Base

Feeling Base + Reflection Base + Formations Base
    with avijñapti and three unconditioned dharmas
    → Dharma Essence + Dharma Principle
```

## 9. Interpretive Note

The verse gives the remainder and the two Dharma designations. The Bhāṣya
identifies the three Bases and specifies the seven constituents.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_15 a vak:Karika ;
    vak:hasTopic vak:FormationsAndDharmaDesignations ;
    vak:belongsTo vak:Dhatunirdesa .

vak:FormationsBase vak:definedByRemainder true .
vak:DharmaEssence vak:names vak:SevenConstituents .
vak:DharmaPrinciple vak:names vak:SevenConstituents .
vak:Avijnapti vak:remainsForm true ;
    vak:alsoIncludedIn vak:DharmaEssence, vak:DharmaPrinciple .
vak:UnconditionedDharmas vak:hasBase false ;
    vak:includedIn vak:DharmaEssence, vak:DharmaPrinciple .
```
