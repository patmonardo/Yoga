# VAK_1.21 — Feeling and Reflection as Distinct Bases

## 1. Sanskrit (Devanāgarī)

> विवादमूलसंसारहेतुत्वात् क्रमकारणात् ।
>
> चैत्तेभ्यो वेदनासंज्ञे पृथक्स्कन्धौ निवेशितौ ॥ १.२१ ॥॥

## 2. Sanskrit (IAST)

> vivādamūlasaṃsārahetutvāt kramakāraṇāt /
>
> caittebhyo vedanāsaṃjñe pṛthakskandhau niveśitau // 1.21 //

## 3. Lexical Analysis

```text
vivāda-mūla-saṃsāra-hetutvāt → because they are causes of the roots of dispute and of saṃsāra
krama-kāraṇāt                → because of the reason of order
caittebhyaḥ                  → apart from the other mental factors
vedanā-saṃjñe                → feeling and reflection
pṛthak-skandhau              → two distinct bases
niveśitau                   → placed, established
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| vivāda-mūla | compound | roots of dispute |
| saṃsāra-hetutvāt | ablative abstract | because they are causes of saṃsāra |
| krama-kāraṇāt | ablative | because of the reason of order |
| caittebhyaḥ | ablative plural | from the other mental factors |
| vedanā-saṃjñe | feminine dual | feeling and reflection |
| pṛthak-skandhau | masculine dual | two distinct bases |
| niveśitau | past participle dual | established |

The commentary supplies *pradhāna-hetu*: principal cause. Feeling and reflection are not the only causes. The local Devanāgarī sometimes reads *cittebhyaḥ*. The prose and the IAST support *caittebhyaḥ*.

## 4. Grammar

```text
vivāda-mūla-hetutvāt
    + saṃsāra-hetutvāt
    + krama-kāraṇāt
        → vedanā-saṃjñe
           caittebhyaḥ pṛthak-skandhau niveśitau
```

*Caittebhyaḥ* is an ablative of separation. Feeling and reflection remain mental factors. They are placed apart from the rest, which stay in the formations-base. The masculine dual follows *skandha*.

The commentary distributes the first reasons in order. Feeling is the principal cause of fixation upon sensual desire. Reflection is the principal cause of fixation upon views. The reason of order is announced and deferred.

## 5. Translation

### Literal Translation

Because they are causes of the roots of dispute and of saṃsāra, and because of the reason of order, feeling and reflection are established as two distinct bases apart from the other mental factors.

### Bhāṣya-informed study translation

Feeling and reflection receive distinct bases because they are principal causes of the two roots of dispute. Savoring feeling leads to fixation upon sensual desire. Inverted reflection leads to fixation upon views. Both are also principal causes of saṃsāra. The order of the bases is a further reason, and it is explained next.

## 6. Philosophical Translation

Again, two lines. The first names the reasons. The second names the placement.

The question is why two mental factors leave the formations-base. Not because they cease to be mental factors. Because their operations are the principal hinges of the two roots of dispute, and of continued wandering.

Feeling is undergoing. The hinge is the savor of that undergoing. Under that savor, one clings to sensual desire. Reflection takes up the mark. The hinge is the inverted mark. Under that inversion, one clings to views. Principal, not sole.

The one who wanders is greedy for the savor of feeling and inverted in reflection. The two determinations join in one subject. They are not two independent inventories.

The last reason is the order of the bases. It is promised in three ways. It is not given here.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| caitta | mental factor | the class they leave, as bases |
| vedanā | feeling | undergoing; not the fixation |
| saṃjñā | reflection | takes up the mark |
| saṃskāra-skandha | formations-base | where the other mental factors remain |
| vivāda-mūla | root of dispute | the two fixations |
| kāmādhyavasāna | fixation upon sensual desire | principal cause: feeling |
| dṛṣṭyadhyavasāna | fixation upon views | principal cause: reflection |
| vedanā-svāda | savor of feeling | the mediation |
| viparīta-saṃjñā | inverted reflection | not every reflection |
| pradhāna-hetu | principal cause | not sole |
| krama | order | deferred |

## 8. Logical Determination

```text
why not both only in the formations-base?

feeling
    → savor
    → fixation upon sensual desire
    → a root of dispute

reflection
    → inverted mark
    → fixation upon views
    → a root of dispute

greed for the savor
    and inverted reflection
    → the one who wanders

principal ≠ sole
order of the bases → 1.22
1.22 not opened
```

## 9. Interpretive Note

The hinge is *pṛthak*: apart, and still mental factors. Interpretation of the two roots is in the Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_21 a vak:Karika ;
    vak:hasTopic vak:FeelingAndReflectionAsBases ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Feeling vak:remains vak:MentalFactor ;
    vak:hasSeparateBase true ;
    vak:isPrincipalCauseOf vak:SensualFixation .
vak:Reflection vak:remains vak:MentalFactor ;
    vak:hasSeparateBase true ;
    vak:isPrincipalCauseOf vak:ViewFixation .
vak:BaseOrder vak:deferredTo vak:VAK_1_22 .
```
