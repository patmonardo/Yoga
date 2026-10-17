# VAK_2.70 — Formless and Uncontaminated

## 1. Sanskrit (Devanāgarī)

```sanskrit
नव चित्तनि तस्मात् षड्भिः / निवृतात् सप्त तद् एव /
शैक्षं चतुर्भ्यः तस्मात् पञ्च / अशैक्षं तु पञ्चकात् // २.७० //
```

## 2. Sanskrit (IAST)

```text
nava cittāni tasmāt ṣaḍbhiḥ / nivṛtāt sapta tad eva /
śaikṣaṃ caturbhyo 'smāt pañca / aśaikṣaṃ tu pañcakāt // 2.70 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| nava | num. | Nine. |
| cittāni | n. pl. | Consciousnesses. |
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

> —nine consciousnesses; six from that [wholesome consciousness]. Seven
> from the obscured, and the same number from it. The trainee follows
> four; five follow it. The beyond-training follows five.
### Bhāṣya-informed study translation

> —nine consciousnesses follow formless wholesome, and six follow it.
> Seven follow formless obscured, and seven follow it. Trainee follows
> four and is followed by five; beyond-training follows five.
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

**Translation note.** The Bhāṣya lists the nine successors of formless
wholesome and its six predecessors: its own three kinds, Form wholesome,
trainee, and beyond-training. Seven follow formless obscured—its own three,
Form wholesome and Form obscured, and the two afflicted desire kinds—and
seven precede it, excluding the afflicted kinds of desire and Form and the
two uncontaminated kinds. Trainee follows the three realm-wholesome kinds
and itself; five follow it, those four plus beyond-training. Beyond-training
follows that group of five. The twelve-kind succession count is complete.

Formless wholesome followed by nine, follows six. Formless obscured followed by seven, follows seven. Trainee follows four, followed by five. Beyond-training follows five, followed by four. Twelve complete.

## 10. OWL++ Seed

```turtle
:FormlessWholesome :followedBy 9 ; :follows 6 .
:FormlessObscured :followedBy 7 ; :follows 7 .
:Trainee :follows 4 ; :followedBy 5 .
:BeyondTraining :follows 5 ; :followedBy 4 .
:Twelve :complete true .
```
