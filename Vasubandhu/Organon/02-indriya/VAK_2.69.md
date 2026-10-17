# VAK_2.69 — Form Obscured and Unobscured

## 1. Sanskrit (Devanāgarī)

> निवृतात् अष्टाभ्यः तस्मात् षट् /
> अनिवृतं तु त्रिभ्यः तस्मात् षट् /
> तस्य नियमः तथा अरूप्ये /
> शुभात् पुनः // २.६९ //

## 2. Sanskrit (IAST)

> nivṛtād aṣṭābhyaḥ tasmāt ṣaṭ /
>
> anivṛtaṃ tu tribhyaḥ tasmāt ṣaṭ /
>
> tasya niyamaḥ tathā ārūpye /
>
> śubhāt punaḥ // 2.69 //

## 3. Lexical Analysis

| Pada | Morphology | Force |
|---|---|---|
| nivṛtāt | abl. sg. | From obscured. |
| aṣṭābhyaḥ | abl. pl. | From eight. |
| tasmāt | abl. sg. | From that. |
| ṣaṭ | num. | Six. |
| anivṛtam | adj. | Unobscured. |
| tu | pcl. | However. |
| tribhyaḥ | abl. pl. | From three. |
| niyamaḥ | m. sg. | Rule. |
| tathā | adv. | Thus. |
| ārūpye | loc. sg. | In the formless. |
| śubhāt | abl. sg. | From wholesome. |
| punaḥ | adv. | However. |

## 4. Grammar

```text
% start S
S[SUCCESSION=form-obscured] -> Follows[EIGHT=true] | FollowedBy[SIX=true]
S[SUCCESSION=form-unobscured] -> Follows[THREE=true] | FollowedBy[SIX=true]
S[SUCCESSION=formless] -> SamePattern
```

Form obscured follows eight, followed by six.  
Form unobscured follows three, followed by six.  
Same pattern in formless.  
From wholesome, however—

## 5. Translation

### Literal Translation

Obscured from eight. From it, six. Unobscured, in turn, from three. From it, six. Its rule, thus, in the formless. From wholesome, however—

### Bhāṣya-informed study translation

> Form obscured follows eight, setting aside the two afflicted desire kinds and trainee and beyond-training; six follow it: the three of its own level and the desire kinds other than unobscured-indeterminate. Form unobscured follows only the three of its own level; six follow it: those three, the two afflicted desire kinds, and formless obscured. The same rule holds in the formless: three of its own level come before it, and six after, its own three and the afflicted of the lower realms. From wholesome, however—

## 6. Philosophical Translation

> Form obscured follows eight, followed by six. Form unobscured follows three, followed by six. Same pattern in formless. From wholesome, however—

## 7. Technical Vocabulary

| Term | Rendering |
|---|---|
| nivṛta | Obscured. |
| anivṛta | Unobscured. |
| niyama | Rule. |

## 8. Logical Determination

Form obscured follows eight, followed by six. Form unobscured follows three, followed by six. Same pattern in formless.

## 9. Interpretive Note

Form obscured follows eight, followed by six. Form unobscured follows three, followed by six. Same pattern in formless. From wholesome, however—

## 10. OWL++ Seed

```turtle
:FormObscured :follows 8 ; :followedBy 6 .
:FormUnobscured :follows 3 ; :followedBy 6 .
:Formless :samePattern true .
```
