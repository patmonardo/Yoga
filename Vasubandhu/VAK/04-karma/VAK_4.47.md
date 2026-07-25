# VAkK 4.47

## Sanskrit

### Devanāgarī

> सुखवेद्यं शुभं ध्यानादातृतीयादतः परम् ।  
> अदुःखासुखवेद्यं तु दुःखवेद्यमिहाशुभम् ॥ ४.४७ ॥

### IAST

> **sukhavedyaṃ śubhaṃ dhyānād ā tṛtīyād ataḥ param |**  
> **aduḥkhāsukhavedyaṃ tu duḥkhavedyam ihāśubham || 4.47 ||**

## Padaccheda

```text
sukha-vedyam
śubham
dhyānāt
ā
tṛtīyāt |

ataḥ
param
aduḥkha-asukha-vedyam
tu |

duḥkha-vedyam
iha
aśubham ||
```

## Literal translation

> **Wholesome karma from the first through the third dhyāna is to be experienced as pleasure. Beyond this, it is to be experienced as neither pain nor pleasure. Here, unwholesome karma is to be experienced as pain.**

## Doctrinal determination

VAkK 4.47 distributes the three classes announced in VAkK 4.45 according to ethical quality and meditative level:

```text
wholesome karma
    first through third dhyāna
        → pleasant maturation

wholesome karma
    beyond the third dhyāna
        → neither-painful-nor-pleasant maturation

unwholesome karma
    desire-domain
        → painful maturation
```

The verse concerns the feeling belonging to karmic maturation, not necessarily the feeling present while the action is being performed.

```text
feeling at the time of action
    ≠ necessarily
feeling belonging to maturation
```

The first three dhyānas retain pleasant or joyful feeling. Beyond the third, the fourth dhyāna and formless levels are correlated with neither-painful-nor-pleasant feeling. Unwholesome karma is restricted by **iha**, “here,” to the desire-domain.

## Philosophical translation

> **Wholesome action associated with the first three meditative absorptions matures as pleasant experience. Action belonging to levels beyond the third absorption matures as experience that is neither painful nor pleasant. Unwholesome action in the desire-domain matures as painful experience.**

## Technical vocabulary

```text
sukha-vedya
    to be experienced as pleasure

duḥkha-vedya
    to be experienced as pain

aduḥkha-asukha-vedya
    to be experienced as neither pain nor pleasure

vedya
    to be experienced
    referring here to the feeling-character of maturation
```

## Logical determination

The verse defines felt maturation as a joint function of ethical quality and level of production:

```text
FELT-MATURATION
    = function(
        ETHICAL-QUALITY,
        MEDITATIVE-LEVEL
      )
```

```text
[ KARMA
  ETHICAL-QUALITY wholesome
  PRODUCTION-LEVEL dhyāna-1-to-3
  FELT-MATURATION pleasant ]
```

```text
[ KARMA
  ETHICAL-QUALITY wholesome
  PRODUCTION-LEVEL above-dhyāna-3
  FELT-MATURATION neither-painful-nor-pleasant ]
```

```text
[ KARMA
  ETHICAL-QUALITY unwholesome
  PRODUCTION-DOMAIN desire
  FELT-MATURATION painful ]
```

## Logic of Experience

VAkK 4.46 established:

```text
production-domain
    → maturation-domain
```

VAkK 4.47 adds:

```text
production-level
    → feeling-form of maturation
```

Thus:

```text
cognitive level of action
        ↓
determinate karmic function
        ↓
domain and feeling of result
```

The higher levels do not simply yield more pleasure. Beyond the third dhyāna, the pleasure/pain opposition is surpassed in neither-painful-nor-pleasant feeling.

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix karma: <http://127.0.0.1:3000/karma#> .
@prefix dhyana: <http://127.0.0.1:3000/dhyana#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_47
    a vak:Karika ;
    rdfs:label "VAK 4.47" ;
    vak:continues vak:VAK_4_46 ;
    vak:determines karma:FeltMaturation .

karma:PleasantlyExperiencedKarma
    a karma:FeltMaturationClass ;
    karma:hasEthicalQuality karma:Wholesome ;
    karma:hasProductionLevel dhyana:FirstThroughThird .

karma:NeitherPainfulNorPleasantlyExperiencedKarma
    a karma:FeltMaturationClass ;
    karma:hasEthicalQuality karma:Wholesome ;
    karma:hasProductionLevel dhyana:AboveThird .

karma:PainfullyExperiencedKarma
    a karma:FeltMaturationClass ;
    karma:hasEthicalQuality karma:Unwholesome ;
    karma:hasProductionDomain loka:DesireDomain .
```

## Determinate result

```text
wholesome karma of dhyānas one through three
    → pleasure as maturation

wholesome karma beyond the third dhyāna
    → neither pain nor pleasure as maturation

unwholesome desire-domain karma
    → pain as maturation
```

Central principle:

```text
the feeling-form of karmic maturation
is determined jointly by
ethical quality and meditative level
```
