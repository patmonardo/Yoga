# VAK_1.30 — Threefold, and Fourteen

## 1. Sanskrit (Devanāgarī)

> त्रिधान्ये कामधात्वाप्ताः सर्वे रूपे चतुर्दश ।
>
> विना गन्धरसघ्राणजिह्वाविज्ञानधातुभिः ॥ १.३० ॥

## 2. Sanskrit (IAST)

> tridhānye kāmadhātvāptāḥ sarve rūpe caturdaśa /
>
> vinā gandharasaghrāṇajihvāvijñānadhātubhiḥ // 1.30 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| tridhā | indeclinable | in three ways |
| anye | nominative masculine plural | the others; the ten remaining after 1.29 |
| kāmadhātvāptāḥ | kāma-dhātu-āptāḥ | connected with the desire realm |
| sarve | nominative masculine plural | all eighteen |
| rūpe | locative; rūpa-dhātau | in the form realm |
| caturdaśa | numeral | fourteen |
| vinā | indeclinable, with instrumental | excluding |
| gandha-rasa-ghrāṇa-jihvā-vijñāna-dhātubhiḥ | instrumental plural | smell, taste, nose-cognition, tongue-cognition |

The closing compound excludes four principles, not six. Nose and tongue, the organs, are not in the exclusion.

## 4. Grammar

```text
anye tridhā
    the other ten
    wholesome, unwholesome, indeterminate

sarve kāma-dhātu-āptāḥ
    all eighteen
    connected with the desire realm

rūpe caturdaśa
    vinā gandha-rasa-ghrāṇa-vijñāna-jihvā-vijñāna-dhātubhiḥ
        fourteen in the form realm
```

*Tridhā* does not mean three realms. The realm question begins at *kāmadhātvāptāḥ*.

## 5. Translation

### Literal Translation

The others are threefold. All are connected with the desire realm. In the form realm, fourteen, excluding the smell, taste, nose-cognition, and tongue-cognition principles.

### Bhāṣya-informed study translation

The other ten principles can be wholesome, unwholesome, or indeterminate. All eighteen occur in the desire realm. In the form realm there are fourteen, excluding smell and taste and the corresponding nose-cognition and tongue-cognition principles.

## 6. Philosophical Translation

The ethical cut finishes the ten. The realm cut begins a new question. Threefold is not three realms.

The form realm drops four principles: two meanings, and the two cognitions that take them. It does not drop the two organs. Absence of the support removes the cognition. Absence of a use does not, by itself, remove the organ.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| anye | the others | the ten after the eight |
| tridhā | threefold | wholesome, unwholesome, indeterminate |
| kuśala | wholesome | not the Pure |
| akuśala | unwholesome | not the Impure |
| avyākṛta | indeterminate | not declared either |
| kāmadhātu | desire realm | not one of the eighteen |
| rūpadhātu | form realm | not the visible-form principle |
| āpta | connected | not separated from |
| gandha-dhātu | smell-principle | excluded from the fourteen |
| rasa-dhātu | taste-principle | excluded from the fourteen |
| ghrāṇa-vijñāna-dhātu | nose-cognition principle | cognition, not a second principle |
| jihvā-vijñāna-dhātu | tongue-cognition principle | likewise |
| vijñāna | cognition | not principle |
| dhātu | principle | the eighteen, except the realm names |

## 8. Logical Determination

```text
the other ten
    threefold
    the Cognition Principle, the seven, by association
    dharma-principle by nature, association, arising
    visible form and sound by vijñapti

all eighteen
    connected with the desire realm

form realm
    fourteen
    excluding smell, taste
    excluding nose-cognition, tongue-cognition
    not excluding nose and tongue

1.31 not opened
```

## 9. Interpretive Note

The hinge is the verse boundary. *Tridhā anye* closes the ethical question. *Kāmadhātvāptāḥ* opens the realms. The exclusion is four principles.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_30 a vak:Karika ;
    vak:hasTopic vak:ThreefoldAndFourteen ;
    vak:belongsTo vak:Dhatunirdesa .

vak:OtherTen vak:ethicalStatus vak:Wholesome, vak:Unwholesome, vak:Indeterminate .
vak:EighteenPrinciples vak:connectedWith vak:DesireRealm .
vak:FormRealm vak:includesCount 14 ;
    vak:excludes vak:SmellPrinciple, vak:TastePrinciple,
        vak:NoseCognitionPrinciple, vak:TongueCognitionPrinciple .
```
