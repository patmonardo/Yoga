# VAK_2.48 — Result-Sort

## 1. Sanskrit (Devanāgarī)

```sanskrit
सभागता सा तु पुनर्विपाकोऽप्याप्तयो द्विधा ।
लक्षणानि च निःष्यन्दाः समापत्त्यसमन्वयाः ॥ २.४८ ॥
```

## 2. Sanskrit (IAST)

```text
sabhāgatā sā tu punar vipāko 'py āptayo dvidhā /
lakṣaṇāni ca niḥṣyandāḥ samāpatty-asamanvayāḥ // 2.48 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sabhāgatā | nom. sg. f. | same-class |
| sā tu punaḥ | nom. sg. f. + particles | that, however, further |
| vipākaḥ api | nom. sg. m. + particle | also maturation |
| āptayaḥ dvidhā | nom. pl. f. + adverb | acquisitions, twofold |
| lakṣaṇāni ca | nom. pl. n. + particle | and the marks |
| niḥṣyandāḥ | nom. pl. m. | homogeneous outflows |
| samāpatti-asamanvaya | nom. pl. f.; compound | the attainments and non-acquisition |
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

> Same-class shares those classifications and is also maturation.
> Acquisitions are twofold, and the marks are also twofold: homogeneous
> outflows or maturation. The attainments and non-acquisition are
> homogeneous outflows.
### Bhāṣya-informed study translation

> Same-class shares the classifications of the groups of names and the rest,
> and is also maturation. Acquisitions are twofold, as are the marks:
> homogeneous outflows or maturation. The attainments and non-acquisition
> are homogeneous outflows.
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

**Translation note.** The commentary carries forward the classifications of the groups of names from 2.47, states that same-class is also maturation, and divides acquisition and marks into two kinds. The two attainments and non-acquisition are classified as homogeneous outflows only. This closes the dissociated formations; the next inquiry turns to causes and conditions.

The pronoun carries 2.47. The sort closes the dissociated formations. Stopping here, as asked.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_48 a vak:Karika ; vak:hasTopic vak:ResultSort .
vak:CausesAndConditions vak:opened false .
```
