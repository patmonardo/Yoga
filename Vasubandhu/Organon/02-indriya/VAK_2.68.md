# VAK_2.68 — Unobscured and Form Wholesome

## 1. Sanskrit (Devanāgarī)

```sanskrit
अनिवृतं पञ्चभ्यः तदनन्तरं सप्त चित्तनि /
रूपे दशैकं च शुभात् नवभ्यस्तदनन्तरम् // २.६८ //
```

## 2. Sanskrit (IAST)

```text
anivṛtaṃ pañcabhyaḥ tadanantaraṃ sapta cittāni /
rūpe daśaikaṃ ca śubhāt navabhyas tadanantaram // 2.68 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| anivṛtam | adj. | Unobscured. |
| pañcabhyaḥ | abl. pl. | From five. |
| tadanantaram | adv. | Immediately after that. |
| sapta | num. | Seven. |
| cittāni | n. pl. | Consciousnesses. |
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

> Unobscured [consciousness] follows five, and seven follow it. In the
> Form realm, eleven follow the wholesome, which follows nine.
### Bhāṣya-informed study translation

> Desire-realm unobscured-indeterminate follows five, and seven follow it.
> In the Form realm, eleven follow wholesome consciousness, which itself
> follows nine.
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

**Translation note.** The five predecessors are the four desire-level kinds
and Form wholesome, from which supernormal-creation consciousness arises.
Seven successors include the four desire-level kinds, Form wholesome after
creation-consciousness, and Form and formless obscured at rebirth-linking.
Eleven follow Form wholesome except formless unobscured-indeterminate; its
nine predecessors exclude the two afflicted desire kinds and formless
unobscured-indeterminate.

Desire unobscured follows five, followed by seven. Form wholesome followed by eleven, follows nine. Excludes formless unobscured.

## 10. OWL++ Seed

```turtle
:DesireUnobscured :follows 5 ; :followedBy 7 .
:FormWholesome :followedBy 11 ; :follows 9 .
:FormlessUnobscured :excluded true .
```
