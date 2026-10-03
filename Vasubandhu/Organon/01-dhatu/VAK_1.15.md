# VAK_1.15

## 1. Sanskrit (Devanāgarī)

> चतुर्भ्योऽन्ये तु संस्कारस्कन्धः एते पुनस्त्रयः ।
>
> धर्मायतनधात्वाख्याः सहाविज्ञप्त्यसंस्कृतैः ॥ १.१५ ॥॥

## 2. Sanskrit (IAST)

> caturbhyo 'nye tu saṃskāraskandhaḥ ete punas trayaḥ /
>
> dharmāyatanadhātvākhyāḥ sahāvijñaptyasaṃskṛtaiḥ // 1.15 //

## 3. Padaccheda

caturbhyaḥ | anye | tu | saṃskāra-skandhaḥ |
ete | punaḥ | trayaḥ |
dharma-āyatana-dhātu-ākhyāḥ | saha | avijñapti-asaṃskṛtaiḥ

| Form | Analysis | Force |
|---|---|---|
| caturbhyaḥ | ablative plural | apart from the four |
| anye | nominative masculine plural | the others |
| tu | contrastive | marks the remainder |
| saṃskāra-skandhaḥ | nominative masculine singular | one formations-base |
| ete | nominative masculine plural | these |
| punaḥ | indeclinable | resumes under the further naming. Not “again” as a new item |
| trayaḥ | nominative masculine plural | the three |
| dharma-āyatana-dhātu-ākhyāḥ | bahuvrīhi | called dharma-essence and dharma-principle |
| saha | governs the instrumental | together with |
| avijñapti-asaṃskṛtaiḥ | instrumental plural | *avijñapti* and the unconditioned |

## 4. Grammar

```text
caturbhyaḥ anye
    = saṃskāra-skandhaḥ

ete trayaḥ
    saha avijñapti-asaṃskṛtaiḥ
    = dharma-āyatana-dhātu-ākhyāḥ
```

`Caturbhyaḥ` is an ablative of separation. `Anye` is plural. `Saṃskāra-skandhaḥ` is a singular predicate. Many formations, one base.

The four are form, feeling, reflection, and the vijñāna-base. The Bhāṣya names them. The verse does not.

`Ete trayaḥ` is feeling, reflection, and the formations-base. `Punaḥ` resumes them under the essence-and-principle naming. It does not add a fourth base.

`Saha` takes the instrumental. *Avijñapti* and the unconditioned accompany the three. They are not members of the formations-base by this verse.

## 5. Translation

### Literal

The others apart from the four are the formations-base. These three again, together with *avijñapti* and the unconditioned, are called dharma-essence and dharma-principle.

“Sphere” and “domain” are withdrawn. They are not called for.

### Bhāṣya-informed

The Bhāṣya names the four: form, feeling, reflection, and the vijñāna-base. The others are the formations-base. It says a sūtra speaks of six groups of volition because of predominance. Volition is principal in active formation because it has the nature of karma. It does not exhaust the base.

It says that if the remaining mental factors and the dissociated formations were left out of a base, they would not be suffering and origin, and full comprehension and abandonment would not apply. Their inclusion must be accepted.

It resolves the three as the feeling-base, the reflection-base, and the formations-base. Together with *avijñapti* and the unconditioned, these seven counted constituents are called dharma-essence and dharma-principle.

Those are the prose. They are not a second verse.

## 6. Philosophical Translation

Remainder. Not a drawer. The formations-base is what the four do not already name.

The three are the useful dharma-skandha. This verse names that skandha twice: dharma-essence, and dharma-principle. Feeling, reflection, formations.

Form sits in that essence. *Avijñapti* is included, and it stays form. The vijñāna-base is the one left out of the three. It is not a member of this naming. It controls the show from outside it.

The encyclopedia of dharmas is not this verse. A Dharma-skandha, in the Organon, is a Science: reflection and formation, a Thinking and an Intuiting. That formula is not the verse line.

## 7. Technical Vocabulary

| Sanskrit | Do not use as the reading | Determination |
|---|---|---|
| saṃskāra-skandha | a leftover bin; volition alone | formations-base |
| caturbhyaḥ | an unnamed four | form, feeling, reflection, vijñāna-base |
| trayaḥ | three loose factors | feeling-base, reflection-base, formations-base |
| āyatana | sphere; sense-base | essence |
| dhātu | domain; element | principle |
| saṃjñā | recognition; perception | reflection |
| avijñapti | a mental item | form, included in the essence |
| asaṃskṛta | a fourth base | unconditioned, accompanying |
| dharma-skandha | the encyclopedia, in this verse | the three. Organon only |

## 8. Logical Determination

```text
FormationsBase
    = Conditioned
    − form
    − feeling
    − reflection
    − vijñāna-base

DharmaEssence = DharmaPrinciple, in this naming
    = feeling-base
    + reflection-base
    + formations-base
    + avijñapti
    + unconditioned

Avijñapti → Form
Avijñapti → included in the essence
VijñānaBase → ¬ member of the three
```

Volition is principal. Principal does not exhaust the base.

This verse names essence and principle. It does not yet seat the vijñāna-base. That seating is 1.16.

## 9. Interpretive Note

The kārikā is the naming. The Bhāṣya supplies the four, the predominance of volition, the path-inclusion argument, and the count of seven. Those stay in the Bhāṣya-informed line. They are not pasted into the literal.

Sphere and domain are the stain of the older page. Withdrawn.

The Bhāṣya file is not synced. Pure stays off the verse line.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_15 a vak:Karika ;
    vak:hasTopic vak:FormationsBaseAndDharmaEssence ;
    vak:belongsTo vak:Dhatunirdesa .

vak:FormationsBase vak:definedByRemainder true .
vak:DharmaEssence vak:names vak:ThreeBases .
vak:DharmaPrinciple vak:names vak:ThreeBases .
vak:Avijnapti vak:remainsForm true .
vak:VijnanaBase vak:memberOfThree false .
vak:SphereGloss vak:isNotTheReading true .
vak:DomainGloss vak:isNotTheReading true .
```
