# VAK_2.60 — Four Classes by Exclusion

## 1. Sanskrit (Devanāgarī)

> क्लिष्टा विपाकजाः शेषाः प्रथमं चानास्रवम् /
> विपाकं सर्वगं हित्वा तौ सभागं च शेषजाः // २.६० //

## 2. Sanskrit (IAST)

> kliṣṭā vipākajāḥ śeṣāḥ prathamaṃ cānāsravam /
>
> vipākaṃ sarvagaṃ hitvā tau sabhāgaṃ ca śeṣajāḥ // 2.60 //

## 3. Lexical Analysis

| Pada | Morphology | Force |
|---|---|---|
| kliṣṭā | adj. pl. | Afflicted. |
| vipākajāḥ | adj. pl. | Maturation-born. |
| śeṣāḥ | adj. pl. | Remaining. |
| prathamam | adj. | First. |
| anāsravam | adj. | Uncontaminated. |
| vipākam | m. sg. | Maturation. |
| sarvagam | adj. | Pervasive. |
| hitvā | ger. | Excluding. |
| tau | dual | Those two. |
| sabhāgam | adj. | Homogeneous. |
| śeṣajāḥ | adj. pl. | Born from the rest. |

## 4. Grammar

```text
% start S
S[CLASS=afflicted] -> Omit[CAUSE=maturation]
S[CLASS=maturation-born] -> Omit[CAUSE=pervasive]
S[CLASS=remaining] -> Omit[CAUSE=maturation, CAUSE=pervasive]
S[CLASS=first-uncontaminated] -> Omit[CAUSE=maturation, CAUSE=pervasive, CAUSE=homogeneous]
```

Four classes by exclusion.  
Afflicted omit maturation.  
Maturation-born omit pervasive.  
Remaining omit both.  
First uncontaminated also omits homogeneous, and is not causeless.  
None from one cause.

## 5. Translation

### Literal Translation

Afflicted, maturation-born, remaining, and first noble, respectively, excluding maturation, the pervasive, those two, and those two with the homogeneous: born from the rest.

### Bhāṣya-informed study translation

> Four classes are distinguished: the afflicted, the maturation-born, the first uncontaminated, and the remaining. The afflicted arise from five causes, excluding maturation. The maturation-born arise from five, excluding the pervasive. The remaining arise from four, excluding those two. The first uncontaminated arises from three, excluding those two and the homogeneous. These counts are of mind and the mental factors; form, and what is dissociated from mind, are likewise, but without the associated cause. No dharma arises from one cause alone.

## 6. Philosophical Translation

> Four classes by exclusion. Afflicted omit maturation. Maturation-born omit pervasive. Remaining omit both. First uncontaminated also omits homogeneous, and is not causeless. Form and dissociated also omit associated. None from one cause.

## 7. Technical Vocabulary

| Term | Rendering |
|---|---|
| kliṣṭa | Afflicted. |
| vipākaja | Maturation-born. |
| śeṣa | Remaining. |
| anāsrava | Uncontaminated. |

## 8. Logical Determination

Four classes by exclusion. None from one cause.

## 9. Interpretive Note

Four classes by exclusion. Afflicted omit maturation. Maturation-born omit pervasive. Remaining omit both. First uncontaminated also omits homogeneous, and is not causeless. None from one cause.

## 10. OWL++ Seed

```turtle
:Afflicted :omitsCause :Maturation .
:MaturationBorn :omitsCause :Pervasive .
:Remaining :omitsCause :Maturation ; :omitsCause :Pervasive .
:FirstUncontaminated :omitsCause :Maturation ; :omitsCause :Pervasive ; :omitsCause :Homogeneous .
:NoDharma :arisesFromOneCause false .
```
