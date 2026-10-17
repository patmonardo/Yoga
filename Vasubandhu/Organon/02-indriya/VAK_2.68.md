# VAK_2.68 — Unobscured and Form Wholesome

## 1. Sanskrit (Devanāgarī)

> अनिवृतं पञ्चभ्यः तदनन्तरं सप्त चित्तनि /
> रूपे दशैकं च शुभात् नवभ्यस्तदनन्तरम् // २.६८ //

## 2. Sanskrit (IAST)

> anivṛtaṃ pañcabhyaḥ tadanantaraṃ sapta cittāni /
>
> rūpe daśaikaṃ ca śubhāt navabhyas tadanantaram // 2.68 //

## 3. Lexical Analysis

| Pada | Morphology | Force |
|---|---|---|
| anivṛtam | adj. | Unobscured. |
| pañcabhyaḥ | abl. pl. | From five. |
| tadanantaram | adv. | Immediately after that. |
| sapta | num. | Seven. |
| cittāni | n. pl. | Minds. |
| rūpe | loc. sg. | In the form realm. |
| daśa | num. | Ten. |
| ekam | num. | One. |
| ca | pcl. | And. |
| śubhāt | abl. sg. | From wholesome. |
| navabhyaḥ | abl. pl. | From nine. |

## 4. Grammar

```text
% start S
S[SUCCESSION=desire-unobscured] -> Follows[FIVE=true] | FollowedBy[SEVEN=true]
S[SUCCESSION=form-wholesome] -> FollowedBy[ELEVEN=true] | Follows[NINE=true]
```

Desire unobscured follows five, followed by seven.  
Form wholesome followed by eleven, follows nine.  
Excludes formless unobscured.

## 5. Translation

### Literal Translation

Unobscured from five. Immediately after it, seven minds. In the form realm, eleven from wholesome. That, immediately after nine.

### Bhāṣya-informed study translation

> The desire-realm unobscured-indeterminate follows five: the four of its own level and form wholesome, from which the mind of supernormal creation arises. Seven follow it: the four of its own level; form wholesome, after the creation-mind; form obscured, at rebirth-linking; and formless obscured, at rebirth-linking. In the form realm, eleven follow the wholesome, all but the formless unobscured-indeterminate; and it follows nine, excluding the two afflicted desire kinds and the formless unobscured-indeterminate.

## 6. Philosophical Translation

> Desire unobscured follows five, followed by seven. Form wholesome followed by eleven, follows nine. Excludes formless unobscured.

## 7. Technical Vocabulary

| Term | Rendering |
|---|---|
| anivṛta | Unobscured. |
| nirmāṇa | Creation. Supernormal. |
| upapatti | Rebirth-linking. |

## 8. Logical Determination

Desire unobscured follows five, followed by seven. Form wholesome followed by eleven, follows nine.

## 9. Interpretive Note

Desire unobscured follows five, followed by seven. Form wholesome followed by eleven, follows nine. Excludes formless unobscured.

## 10. OWL++ Seed

```turtle
:DesireUnobscured :follows 5 ; :followedBy 7 .
:FormWholesome :followedBy 11 ; :follows 9 .
:FormlessUnobscured :excluded true .
```
