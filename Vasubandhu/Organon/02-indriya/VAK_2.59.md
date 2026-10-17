# VAK_2.59 — Taking and Giving

## 1. Sanskrit (Devanāgarī)

> वर्तमानाः फलं पञ्च गृह्णन्ति द्वौ प्रयच्छतः /
> वर्तमानातीतौ द्वौ एकोऽतीतः प्रयच्छति // २.५९ //

## 2. Sanskrit (IAST)

> vartamānāḥ phalaṃ pañca gṛhṇanti dvau prayacchataḥ /
>
> vartamānātītau dvau eko 'tītaḥ prayacchati // 2.59 //

## 3. Lexical Analysis

| Pada | Morphology | Force |
|---|---|---|
| vartamānāḥ | adj. pl. | Present. |
| phalam | n. sg. | Fruit. |
| pañca | num. | Five. |
| gṛhṇanti | 3 pl. | Take. |
| dvau | num. | Two. |
| prayacchataḥ | 3 dual | Give. |
| vartamānātītau | adj. dual | Present and past. |
| ekaḥ | num. | One. |
| atītaḥ | adj. | Past. |
| prayacchati | 3 sg. | Gives. |

## 4. Grammar

```text
% start S
S[TAKE=present] -> Five
S[GIVE=present] -> Two
S[GIVE=present-or-past] -> Two
S[GIVE=past-only] -> Maturation
```

Five take while present.  
Two give present.  
Two give present or past.  
Maturation gives past only.  
Taking is seed-status, not a store. Taking does not imply giving.

## 5. Translation

### Literal Translation

Five, present, take the fruit. Two give. Two, present and past. One, past, gives.

### Bhāṣya-informed study translation

> Five take while present. Two give present. Two give present or past. Maturation gives past only. Taking is seed-status, not a store. Taking does not imply giving.

## 6. Philosophical Translation

> Five take while present. Two give present. Two give present or past. Maturation gives past only. Taking is seed-status, not a store. Taking does not imply giving.

## 7. Technical Vocabulary

| Term | Rendering |
|---|---|
| gṛhṇanti | Take. Seed-status, not a store. |
| prayacchanti | Give. |
| bīja-bhāva | Seed-status. |

## 8. Logical Determination

Taking is seed-status. Taking does not imply giving. Maturation gives past only.

## 9. Interpretive Note

Five take while present. Two give present. Two give present or past. Maturation gives past only. Taking is seed-status, not a store. Taking does not imply giving.

## 10. OWL++ Seed

```turtle
:FiveCauses :takeWhilePresent true .
:TwoCauses :giveWhilePresent true .
:TwoCauses :givePresentOrPast true .
:MaturationCause :givesPastOnly true .
:Taking :isSeedStatus true ; :impliesGiving false .
```
