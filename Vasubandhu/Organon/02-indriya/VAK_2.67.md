# VAK_2.67 — Desire Realm Succession

## 1. Sanskrit (Devanāgarī)

> कामे नव शुभात् तच्च अष्टाभ्यः दशभिः अकुशलात् /
> तस्मात् चतुर्भिः निवृतं तथा // २.६७ //

## 2. Sanskrit (IAST)

> kāme nava śubhāt tac ca aṣṭābhyaḥ daśabhir akuśalāt /
>
> tasmāt caturbhiḥ nivṛtaṃ tathā // 2.67 //

## 3. Lexical Analysis

| Pada | Morphology | Force |
|---|---|---|
| kāme | loc. sg. | In the desire realm. |
| nava | num. | Nine. |
| śubhāt | abl. sg. | From wholesome. |
| tat | n. sg. | That. |
| ca | pcl. | And. |
| aṣṭābhyaḥ | abl. pl. | From eight. |
| daśabhiḥ | inst. pl. | By ten. |
| akuśalāt | abl. sg. | From unwholesome. |
| tasmāt | abl. sg. | From that. |
| caturbhiḥ | inst. pl. | By four. |
| nivṛtam | adj. | Obscured. |
| tathā | adv. | Likewise. |

## 4. Grammar

```text
% start S
S[SUCCESSION=desire-wholesome] -> FollowedBy[NINE=true] | Follows[EIGHT=true]
S[SUCCESSION=unwholesome] -> FollowedBy[FOUR=true] | Follows[TEN=true]
S[SUCCESSION=obscured] -> FollowedBy[FOUR=true] | Follows[TEN=true]
```

Desire wholesome followed by nine, follows eight.  
Asymmetry is formless obscured.  
Formless wholesome excluded by four remotenesses.  
Unwholesome and obscured follow ten, followed by four.

## 5. Translation

### Literal Translation

In the desire realm, nine minds from a wholesome mind. That, only from eight. Unwholesome from ten. From it, four. Obscured, likewise.

### Bhāṣya-informed study translation

> In the desire realm, nine minds follow a wholesome mind: the four of its own level; two of the form realm, wholesome at entry into attainment and obscured at rebirth-linking; formless obscured, at rebirth-linking; and trainee and beyond-training. Formless wholesome does not follow it, being too remote by the four remotenesses of support, aspect, object, and counteragent. That wholesome mind itself follows only eight: the four of its own level; form wholesome, at emergence; form obscured, when one pressed by an afflicted attainment resorts to the wholesome supporting level; and trainee and beyond-training, at emergence. Unwholesome mind follows ten, excluding trainee and beyond-training, by rebirth-linking after all form and formless minds; four follow it, of its own level only. The obscured is likewise: it follows ten, and four follow it.

## 6. Philosophical Translation

> Desire wholesome followed by nine, follows eight. Asymmetry is formless obscured. Formless wholesome excluded by four remotenesses. Unwholesome and obscured follow ten, followed by four.

## 7. Technical Vocabulary

| Term | Rendering |
|---|---|
| dūratā | Remoteness. Four: support, aspect, object, counteragent. |
| upapatti | Rebirth-linking. |
| samāpatti | Attainment. |

## 8. Logical Determination

Desire wholesome followed by nine, follows eight. Asymmetry is formless obscured. Four remotenesses exclude formless wholesome.

## 9. Interpretive Note

Desire wholesome followed by nine, follows eight. Asymmetry is formless obscured. Formless wholesome excluded by four remotenesses. Unwholesome and obscured follow ten, followed by four.

## 10. OWL++ Seed

```turtle
:DesireWholesome :followedBy 9 ; :follows 8 .
:Asymmetry :isFormlessObscured true .
:FormlessWholesome :excludedBy :FourRemotenesses .
:Unwholesome :follows 10 ; :followedBy 4 .
:Obscured :follows 10 ; :followedBy 4 .
```
