# VAK_3.22 — Name-and-Form, Six Essences, and Contact

## 1. Sanskrit (Devanāgarī)

> प्राक् षडायतनोत्पादात् तत्पूर्वं त्रिकसंगमात् ।
>
> स्पर्शः प्राक्सुखदुःखादिकारणज्ञानशक्तितः ॥ ३.२२ ॥

## 2. Sanskrit (IAST)

> prāk ṣaḍāyatanotpādāt tatpūrvaṃ trikasaṃgamāt /
>
> sparśaḥ prāk sukhaduḥkhādikāraṇajñānaśaktitaḥ // 3.22 //

The first phrase completes the definition of Name-and-Form begun in VAK
3.21.

## 3. Lexical Analysis

```text
prāk                              → prāk
ṣaṭ-āyatana-utpādāt              → ṣaḍāyatanotpādāt
tat-pūrvam                       → tatpūrvam
trika-saṃgamāt                   → trikasaṃgamāt
sparśaḥ                          → sparśaḥ
prāk                             → prāk
sukha-duḥkha-ādi-kāraṇa-jñāna-śaktitaḥ
                                 → sukhaduḥkhādikāraṇajñānaśaktitaḥ
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| prāk | indeclinable governing an ablative | before; marks the stage's terminal boundary |
| ṣaṭ-āyatana-utpādāt | ablative singular compound | before the arising of the six Essences |
| tat-pūrvam | adverbial expression | before that; marks the preceding boundary of the six-Essence stage |
| trika-saṃgamāt | ablative singular compound | before the conjunction of the triad |
| sparśaḥ | nominative masculine singular | Contact, the stage arising from the triad's conjunction |
| sukhaduḥkha-ādi | compound members | pleasure, pain, and the other kind of Feeling |
| kāraṇa-jñāna-śaktitaḥ | ablative singular compound | before the capacity to discriminate the causes |

The Bhāṣya identifies the triad as Faculty, Condition, and Discriminative
Cognition. It explains the final compound through the capacity to
discriminate the causes of the three Feelings.

## 4. Grammar

The verse continues the stage definitions:

```text
[nāmarūpam]
    prāk ṣaḍāyatana-utpādāt

[ṣaḍāyatanam]
    tat-pūrvam trika-saṃgamāt

sparśaḥ
    prāk sukha-duḥkha-ādi-kāraṇa-jñāna-śaktitaḥ
```

> Name-and-Form extends until before the arising of the six Essences; the
> six-Essence stage extends until before the conjunction of the triad.
> Contact extends until before the capacity to discriminate the causes of
> pleasure, pain, and the other Feeling.

The stage subjects in the first two constructions are supplied from the
preceding verse and the Bhāṣya. The Bhāṣya specifies the triad and clarifies
the final capacity as discrimination of the causes of three Feelings.

## 5. Translation

### Close syntactic rendering

> [Name-and-Form extends] until before the arising of the six Essences;
> [the six-Essence stage extends] until before the conjunction of the triad.
> Contact [extends] until before the capacity to discriminate the causes
> of pleasure, pain, and the other Feeling.

### Bhāṣya-informed study translation

> Name-and-Form names the interval after junction consciousness and before
> the arising of the six Essences. The succeeding interval is called the
> six-Essence stage, even though its boundary could be stated as the arising
> of four Essences, because the full sixfold organization is established
> then. That stage continues until Faculty, Condition, and Discriminative
> Cognition meet. From their conjunction, Contact arises; the Contact-stage
> lasts until the capacity to discriminate the causes of pleasant, painful,
> and neutral Feeling is established.

## 6. Scope Note

The Bhāṣya does not name which four Essences mark the immediate emergence.
It explains why the stage is designated through the full six-Essence
organization. The arising of Contact and the limit of the Contact-stage are
also Bhāṣya determinations.

Here *viṣaya* is rendered **Condition**: a specific moment of the Seen and
the playground of the Faculties. Keep it distinct from Object, the
comprehended truth of Vastu, and keep Discriminative Cognition distinct from
consciousness and Mind.

## 7. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:VAK_3_22
    a vak:Karika ;
    vak:continues vak:VAK_3_21 ;
    vak:definesStage vak:NameAndFormStage, vak:SixEssenceStage,
        vak:ContactStage ;
    vak:definesRelation vak:CognitiveTriad .

vak:NameAndFormStage
    a vak:TemporalStage ;
    vak:endsBefore vak:SixEssencesArise .

vak:SixEssenceStage
    a vak:TemporalStage ;
    vak:endsBefore vak:CognitiveTriadConjunction .

vak:CognitiveTriad
    a organon:CognitiveRelation ;
    vak:hasMember vak:Faculty, vak:Condition, vak:Vijnana ;
    vak:conjunctionProduces vak:Contact .

vak:ContactStage
    a vak:TemporalStage ;
    vak:beginsAt vak:CognitiveTriadConjunction ;
    vak:endsBefore vak:CauseDiscriminationCapacity .

vak:CauseDiscriminationCapacity
    a organon:DiscriminativeCapacity ;
    vak:concerns vak:ThreeFeelingsCauses .
```
