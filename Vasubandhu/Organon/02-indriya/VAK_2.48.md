# VAK_2.48 — Result-Sort

## 1. Sanskrit (Devanāgarī)

> सभागता सा तु पुनर्विपाकोऽप्याप्तयो द्विधा ।
>
> लक्षणानि च निःष्यन्दाः समापत्त्यसमन्वयाः ॥ २.४८ ॥

## 2. Sanskrit (IAST)

> sabhāgatā sā tu punar vipāko 'py āptayo dvidhā /
>
> lakṣaṇāni ca niḥṣyandāḥ samāpatty-asamanvayāḥ // 2.48 //

## 3. Lexical Analysis

| Pada | Force |
|---|---|
| sabhāgatā | same-class |
| sā tu punaḥ | that, however, further |
| vipākaḥ api | also maturation |
| āptayaḥ dvidhā | acquisitions, twofold |
| lakṣaṇāni ca | and the marks |
| niḥṣyandāḥ | homogeneous outflows |
| samāpatti-asamanvaya | the attainments and non-acquisition |

## 4. Grammar

```text
% start S
S[NAME=same-class] -> Classification[LIKE=name-groups, ALSO=maturation]
S[NAME=acquisition|marks] -> Twofold[OUTFLOW=homogeneous | MATURATION=true]
S[NAME=attainment|non-acquisition] -> Outflow[HOMOGENEOUS=true]
```

Same-class shares the name-group classifications and is also maturation.  
Acquisition and marks are twofold.  
The two attainments and non-acquisition are homogeneous outflow only.

## 5. Translation

### Literal Translation

Same-class, that however is further also maturation. Acquisitions are twofold, and the marks. Homogeneous outflows: the attainments and non-acquisition.

### Bhāṣya-informed study translation

> Same-class shares the classifications of the groups of names, and is also maturation. Acquisition is twofold, homogeneous outflow or maturation. The marks likewise. The two attainments and non-acquisition are homogeneous outflows only. The dissociated formations have been explained. Causes and conditions are the next question.

## 6. Philosophical Translation

> Same-class is also maturation. Acquisition and marks are twofold. The two attainments and non-acquisition are homogeneous outflow only. The dissociated formations close. Causes and conditions are the next question.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| sabhāgatā | same-class | also maturation |
| niḥṣyanda | homogeneous outflow | continuity in kind |
| vipāka | maturation | karmic |
| asamanvāgama | non-acquisition | outflow only |

## 8. Logical Determination

```text
same-class, acquisition, marks
    → outflow or maturation
two attainments, non-acquisition
    → outflow only
    not maturation
same catalogue class
    ≠ same result-type
causes and conditions
    asked
    not answered
```

## 9. Interpretive Note

The pronoun carries 2.47. The sort closes the dissociated formations. Stopping here, as asked.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_48 a vak:Karika ; vak:hasTopic vak:ResultSort .
vak:CausesAndConditions vak:opened false .
```
