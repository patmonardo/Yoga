# VAK_2.60 — Citta Status and Hetu Exclusions

## 1. Sanskrit — Devanāgarī

```text
क्लिष्टा विपाकजाः शेषाः प्रथमाऱ्या यथाक्रमम् ।
विपाकं सर्वगं हित्वा तौ सभागं च शेषजाः ॥ VAkK_2.60 ॥
```

## 2. Sanskrit — IAST

```text
kliṣṭā vipākajāḥ śeṣāḥ prathamāryā yathākramam /
vipākaṃ sarvagaṃ hitvā tau sabhāgaṃ ca śeṣajāḥ // VAkK_2.60 //
```

## 3. Padaccheda

| Text | Padaccheda | Basic Sense |
|---|---|---|
| kliṣṭāḥ | kliṣṭāḥ | afflicted |
| vipākajāḥ | vipāka-jāḥ | maturation-born |
| śeṣāḥ | śeṣāḥ | remaining, residual |
| prathamāryāḥ | prathamā-āryāḥ | first noble ones |
| yathākramam | yathākramam | in order |
| vipākaṃ | vipākaṃ | maturation |
| sarvagam | sarva-gam | pervasive |
| hitvā | hitvā | having excluded |
| tau | tau | those two |
| sabhāgaṃ | sabhāgam | homogeneous |
| ca | ca | and |
| śeṣajāḥ | śeṣa-jāḥ | remaining-born |

## 4. Literal Translation

```text
Afflicted, maturation-born, the remaining, and the first noble states, in order:
excluding vipāka and sarvaga, those two; and for the remaining-born, also sabhāga.
```

## 5. Philosophical Translation

```text
The hetu-phala rules are applied to classes of citta: afflicted, maturation-born, remaining, and first noble states.
Different ground-types are included or excluded according to the status of the arising citta.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| kliṣṭa | afflicted | Distorted/defiled citta-status |
| vipākaja | maturation-born | Arisen as maturation-result |
| śeṣa | remaining | Residual/other classes; technical review needed |
| prathamārya | first noble | First noble/path moment; review with Bhāṣya |
| yathākramam | in order | Ordered application marker |
| hitvā | having excluded | Exclusion rule |
| vipāka | maturation ground/result | Excluded in specified cases |
| sarvaga / sarvatraga | pervasive ground | Source gives `sarvaga`; likely sarvatraga sense |
| sabhāga | homogeneous ground | Also excluded in certain cases |

## 7. Logical Determination

VAK_2.60 applies the HetuEngine to citta-status classes.

```text
CittaStatus:
    kliṣṭa
    vipākaja
    śeṣa
    prathamārya
```

Rule-form:

```text
if citta has status X,
then include/exclude specified hetus.
```

This is the transition from general ground-result theory to profile-specific arising rules.

## 8. Organon Interpretation

```text
CittaArisingRule:
    cittaStatus
    allowedHetus
    excludedHetus
```

This prepares the next block:

```text
2.61–2.64
    PratyayaFeatureSet
    condition system
```

## 9. Commit History

```text
VAK_2.60 opened.
Method: kārikā-first speculative seed.
Theme: citta-status-specific inclusion/exclusion of hetus.
Technical count and exclusion details marked for Bhāṣya review.
```
