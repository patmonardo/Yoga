# VAK_2.70 — Formless and Uncontaminated

## 1. Sanskrit (Devanāgarī)

> नव चित्तनि तस्मात् षड्भिः /
> निवृतात् सप्त तद् एव /
> शैक्षं चतुर्भ्यः तस्मात् पञ्च /
> अशैक्षं तु पञ्चकात् // २.७० //

## 2. Sanskrit (IAST)

> nava cittāni tasmāt ṣaḍbhiḥ /
>
> nivṛtāt sapta tad eva /
>
> śaikṣaṃ caturbhyo 'smāt pañca /
>
> aśaikṣaṃ tu pañcakāt // 2.70 //

## 3. Lexical Analysis

| Pada | Morphology | Force |
|---|---|---|
| nava | num. | Nine. |
| cittāni | n. pl. | Minds. |
| tasmāt | abl. sg. | From that. |
| ṣaḍbhiḥ | inst. pl. | By six. |
| nivṛtāt | abl. sg. | From obscured. |
| sapta | num. | Seven. |
| tad | n. sg. | That. |
| eva | pcl. | Indeed. |
| śaikṣam | adj. | Trainee. |
| caturbhyaḥ | abl. pl. | From four. |
| asmāt | abl. sg. | From this. |
| pañca | num. | Five. |
| aśaikṣam | adj. | Beyond-training. |
| tu | pcl. | However. |
| pañcakāt | abl. sg. | From the group of five. |

## 4. Grammar

```text
% start S
S[SUCCESSION=formless-wholesome] -> FollowedBy[NINE=true] | Follows[SIX=true]
S[SUCCESSION=formless-obscured] -> FollowedBy[SEVEN=true] | Follows[SEVEN=true]
S[SUCCESSION=trainee] -> Follows[FOUR=true] | FollowedBy[FIVE=true]
S[SUCCESSION=beyond-training] -> Follows[FIVE=true] | FollowedBy[FOUR=true]
```

Formless wholesome followed by nine, follows six.  
Formless obscured followed by seven, follows seven.  
Trainee follows four, followed by five.  
Beyond-training follows five, followed by four.  
Twelve complete.

## 5. Translation

### Literal Translation

Nine minds. That, from six. From obscured, seven. That, likewise. Trainee from four. From this, five. Beyond-training from the group of five.

### Bhāṣya-informed study translation

> Formless wholesome followed by nine, follows six. Formless obscured followed by seven, follows seven. Trainee follows four, followed by five. Beyond-training follows five, followed by four. Twelve complete.

## 6. Philosophical Translation

> Formless wholesome followed by nine, follows six. Formless obscured followed by seven, follows seven. Trainee follows four, followed by five. Beyond-training follows five, followed by four. Twelve complete.

## 7. Technical Vocabulary

| Term | Rendering |
|---|---|
| śaikṣa | Trainee. |
| aśaikṣa | Beyond-training. |
| pañcaka | Group of five. |

## 8. Logical Determination

Formless wholesome followed by nine, follows six. Formless obscured followed by seven, follows seven. Trainee follows four, followed by five. Beyond-training follows five, followed by four. Twelve complete.

## 9. Interpretive Note

Formless wholesome followed by nine, follows six. Formless obscured followed by seven, follows seven. Trainee follows four, followed by five. Beyond-training follows five, followed by four. Twelve complete.

## 10. OWL++ Seed

```turtle
:FormlessWholesome :followedBy 9 ; :follows 6 .
:FormlessObscured :followedBy 7 ; :follows 7 .
:Trainee :follows 4 ; :followedBy 5 .
:BeyondTraining :follows 5 ; :followedBy 4 .
:Twelve :complete true .
```
