# VAK_2.69 — Form Obscured and Unobscured

## 1. Sanskrit (Devanāgarī)

```sanskrit
निवृतात् अष्टाभ्यः तस्मात् षट् / अनिवृतं तु त्रिभ्यः तस्मात् षट् /
तस्य नियमः तथा अरूप्ये / शुभात् पुनः // २.६९ //
```

## 2. Sanskrit (IAST)

```text
nivṛtād aṣṭābhyaḥ tasmāt ṣaṭ / anivṛtaṃ tu tribhyaḥ tasmāt ṣaṭ /
tasya niyamaḥ tathā ārūpye / śubhāt punaḥ // 2.69 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
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

> Obscured follows eight, and six follow it. Unobscured follows three, and
> six follow it. The same rule holds in the formless; from wholesome,
> however—
### Bhāṣya-informed study translation

> Form obscured follows eight and is followed by six. Form unobscured
> follows three and is followed by six. The same rule holds in the
> formless. From wholesome, however—
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

**Translation note.** The Bhāṣya excludes the two afflicted desire kinds and
the two uncontaminated kinds from the eight predecessors of Form obscured;
its six successors comprise the three of its level and desire kinds other
than unobscured-indeterminate. Form unobscured has three same-level
predecessors and six successors, including the two afflicted desire kinds
and formless obscured. The same pattern holds in the formless: three of its
level before it, and six after, including the lower realms' afflicted kinds.

Form obscured follows eight, followed by six. Form unobscured follows three, followed by six. Same pattern in formless. From wholesome, however—

## 10. OWL++ Seed

```turtle
:FormObscured :follows 8 ; :followedBy 6 .
:FormUnobscured :follows 3 ; :followedBy 6 .
:Formless :samePattern true .
```
