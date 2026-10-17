# VAK_3.22 — From Name-and-Form to Contact

## 1. Sanskrit (Devanāgarī)

```sanskrit
प्राक् षडायतनोत्पादात् तत्पूर्वं त्रिकसंगमात् ।
स्पर्शः प्राक्सुखदुःखादिकारणज्ञानशक्तितः ॥ ३.२२ ॥
```

## 2. Sanskrit (IAST)

```text
prāk ṣaḍāyatanotpādāt tatpūrvaṃ trikasaṃgamāt /
sparśaḥ prāk sukhaduḥkhādikāraṇajñānaśaktitaḥ // 3.22 //
```

The first phrase completes the definition of Name-and-Form begun in VAK
3.21.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| prāk | indeclinable governing an ablative | before; marks the stage's terminal boundary |
| ṣaṭ-āyatana-utpādāt | ablative singular compound | before the arising of the six Essences |
| tat-pūrvam | adverbial expression | before that; marks the preceding boundary of the six-Essence stage |
| trika-saṃgamāt | ablative singular compound | before the conjunction of the triad |
| sparśaḥ | nominative masculine singular | Contact, the stage arising from the triad's conjunction |
| sukhaduḥkha-ādi | compound members | pleasure, pain, and the other kind of Feeling |
| kāraṇa-jñāna-śaktitaḥ | ablative singular compound | before the capacity to know the causes |

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
> Contact extends until before the capacity to know the causes of
> pleasure, pain, and the other Feeling.

The stage subjects in the first two constructions are supplied from the
preceding verse and the Bhāṣya. The Bhāṣya specifies the triad and clarifies
the final capacity as discrimination of the causes of three Feelings.

## 5. Translation

### Literal Translation
> [Name-and-Form extends] until before the arising of the six Essences;
> [the six-Essence stage extends] until before the conjunction of the triad.
> Contact [extends] until before the capacity to know the causes
> of pleasure, pain, and the other Feeling.

### Bhāṣya-informed study translation

> Name-and-Form lasts until the six Essences arise; the six-Essence stage
> lasts until the triad converges. Contact lasts until the capacity to know
> the causes of pleasant, painful, and other Feeling arises.

## 6. Philosophical Translation

> Name-and-Form extends until the six Essences arise. The six-Essence stage
> extends until Faculty, Condition, and Discriminative Cognition come
> together. From that conjunction Contact arises; the Contact-stage extends
> until there is capacity to know the causes of pleasure, pain, and
> the other Feelings.

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this passage |
|---|---|---|
| `prāk` | before / up to before | marks the boundary of a stage |
| `ṣaḍāyatana` | six Essences | the full sixfold organization used to designate the stage |
| `trika` | triad | Faculty, Condition, and Discriminative Cognition, as specified by the Bhāṣya |
| `saṃgama` | conjunction | the meeting from which Contact arises |
| `sparśa` | Contact | the relation arising from conjunction, and the stage before cause-discrimination capacity |
| `sukha-duḥkha-ādi` | pleasure, pain, and the other Feelings | the objects of the relevant cause-discrimination |
| `jñāna-śakti` | capacity for knowledge | here, capacity to know the causes of the three Feelings |

## 8. Logical Determination

```text
rebirth-junction
    → Name-and-Form
    → sixfold Essence organization established
    → six-Essence stage
    → Faculty + Condition + Discriminative Cognition meet
    → Contact arises
    → capacity to know causes of the three Feelings
    → end of the Contact-stage
```

The first two stage-boundaries continue the sequence begun in VAK 3.21.
The Bhāṣya says the six-Essence designation names the established whole;
it does not identify the four Essences that could mark immediate emergence.
Contact is not one of the triad's members.

## 9. Interpretive Note

**Translation note.** Here *viṣaya* is **Condition**, a specific moment of the Seen and the
playground of the Faculties—not Object, the comprehended truth of Vastu.
The local triad also keeps Discriminative Cognition distinct from
consciousness (*citta*) and Mind (*manas*).

## 10. OWL++ Seed

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
    vak:endsBefore vak:CauseKnowledgeCapacity .

vak:CauseKnowledgeCapacity
    a organon:DiscriminativeCapacity ;
    vak:concerns vak:ThreeFeelingsCauses .
```
