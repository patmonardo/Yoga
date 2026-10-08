# VAK_1.24 — Why One Essence Is Named Form and One Dharma

## 1. Sanskrit (Devanāgarī)

> विशेषणार्थं प्राधान्याद्बहुधर्माग्रसंग्रहात् ।
>
> एकमायतनं रूपमेकं धर्माख्यमुच्यते ॥ १.२४ ॥

## 2. Sanskrit (IAST)

> viśeṣaṇārthaṃ prādhānyād bahudharmāgrasaṃgrahāt /
>
> ekam āyatanaṃ rūpam ekaṃ dharmākhyam ucyate // 1.24 //

## 3. Lexical Analysis

```text
viśeṣaṇārthaṃ prādhānyād bahudharmāgrasaṃgrahāt
    → viśeṣaṇa-artham + prādhānyāt + bahu-dharma-agra-saṃgrahāt

ekam āyatanaṃ rūpam ekam dharmākhyam ucyate
    → ekam + āyatanam + rūpam + ekam + dharma-ākhyam + ucyate
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| viśeṣaṇārtham | accusative neuter singular, used adverbially | for distinction |
| prādhānyāt | ablative singular | because of primacy |
| bahu-dharma-agra-saṃgrahāt | ablative singular compound | because many dharmas and the highest Dharma are gathered |
| ekam | nominative neuter singular | one |
| āyatanam | nominative neuter singular | Essence |
| rūpam | nominative neuter singular | Form |
| dharmākhyam | nominative neuter singular compound | named Dharma |
| ucyate | third-person singular present passive | is called |

## 4. Grammar

```text
one Essence = Form
one Essence = named Dharma

reasons:
distinction + primacy + gathering many dharmas and the highest Dharma
```

The Bhāṣya applies distinction to both names, primacy to Form, and the
gathering of many dharmas and nirvāṇa to Dharma.

## 5. Translation

### Literal Translation

For distinction, because of primacy, and because many dharmas and the
highest Dharma are gathered, one Essence is called Form and one is called
Dharma.

### Bhāṣya-informed study translation

Among the ten Essences included in the Form Base, one is named Form because
it is prominent in ordinary experience: it is resistant, visible, and can
be pointed out as “this, here, there.” One Essence is named Dharma because
it gathers many dharmas, including nirvāṇa, the highest Dharma.

## 6. Systematic Placement

The Form Essence is one of the ten Essences in the Form Base. The Dharma
Essence gathers many dharmas, including nirvāṇa. Their names follow
different reasons in the Bhāṣya. Within the Dhātu-machine sequence
(1.24–1.28), this verse establishes the naming distinction that later
classification and assignment preserve.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| viśeṣaṇa | distinction | preserves the individual Essence positions |
| prādhānya | primacy; prominence | the reason associated with Form |
| saṃgraha | gathering | the reason associated with Dharma |
| rūpāyatana | Form Essence | named through primacy |
| dharmāyatana | Dharma Essence | gathers many dharmas and nirvāṇa |
| agra-dharma | highest Dharma | identified as nirvāṇa in the Bhāṣya |

## 8. Logical Determination

```text
Form Essence
    → one of the ten Essences in the Form Base
    → named through primacy

Dharma Essence
    → gathers many dharmas, including nirvāṇa
    → named Dharma
```

## 9. Interpretive Note

The Bhāṣya reports an alternative explanation from other teachers: the
Form Essence is gross in its twenty varieties and is the field of the
fleshly, divine, and noble wisdom-eyes.

The Kośa presents Vijñāna as Discriminative Cognition joining and
governing Perception and Conception. Their unity is Inconceivable as a
homogeneous operation; its Idea is disclosed in the Cognition Base.
Vijñāna governs Manas and guides the reading of Dharma Base. Form Base and
Dharma Base classify the same *avijñapti* distinctly; Vijñāna bears a
*prati* relation to it and remains distinct from *citta* and *manas*.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_24
    a vak:Karika ;
    rdfs:label "VAK 1.24" ;
    vak:hasTopic vak:FormAndDharmaEssenceNaming ;
    vak:belongsTo vak:Dhatunirdesa .

vak:FormEssence
    a vak:Essence ;
    vak:memberOf vak:FormBase ;
    vak:namedThrough vak:Primacy .

vak:DharmaEssence
    a vak:Essence ;
    vak:namedThrough vak:InclusiveGathering ;
    vak:gathers vak:ManyDharmas, vak:Nirvana .

vak:Nirvana
    a vak:HighestDharma ;
    vak:gatheredIn vak:DharmaEssence .
```
