# VAK_2.60 — Four Classes by Exclusion

## 1. Sanskrit (Devanāgarī)

```sanskrit
क्लिष्टा विपाकजाः शेषाः प्रथमं चानास्रवम् /
विपाकं सर्वगं हित्वा तौ सभागं च शेषजाः // २.६० //
```

## 2. Sanskrit (IAST)

```text
kliṣṭā vipākajāḥ śeṣāḥ prathamaṃ cānāsravam /
vipākaṃ sarvagaṃ hitvā tau sabhāgaṃ ca śeṣajāḥ // 2.60 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
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

> Afflicted, maturation-born, remaining, and first uncontaminated
> [dharmas] arise from the causes left after excluding maturation, the
> pervasive, those two, and those two plus the homogeneous, respectively.
### Bhāṣya-informed study translation

> Afflicted, maturation-born, remaining, and first uncontaminated dharmas
> arise from the causes left after excluding maturation, the pervasive,
> both, and both plus the homogeneous, respectively.
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

**Translation note.** The Bhāṣya counts five causes for the afflicted, five
for maturation-born, four for the remaining, and three for the first
uncontaminated. These counts concern consciousness and mental factors; Form
and dharmas dissociated from consciousness follow likewise but without the
associated cause. The remaining class includes indeterminate dharmas apart
from maturation-born and wholesome dharmas apart from the first
uncontaminated moment. No dharma arises from a single cause.

Four classes by exclusion. Afflicted omit maturation. Maturation-born omit pervasive. Remaining omit both. First uncontaminated also omits homogeneous, and is not causeless. None from one cause.

## 10. OWL++ Seed

```turtle
:Afflicted :omitsCause :Maturation .
:MaturationBorn :omitsCause :Pervasive .
:Remaining :omitsCause :Maturation ; :omitsCause :Pervasive .
:FirstUncontaminated :omitsCause :Maturation ; :omitsCause :Pervasive ; :omitsCause :Homogeneous .
:NoDharma :arisesFromOneCause false .
```
