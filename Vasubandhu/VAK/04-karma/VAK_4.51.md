# VAkK 4.51

## Sanskrit

### Devanāgarī

> चतुष्कोटिकमित्यन्ये निकायाक्षेपणं त्रिभिः ।  
> सर्वत्र चतुराक्षेपः शुभस्य नरके त्रिधा ॥ ४.५१ ॥

### IAST

> **catuṣkoṭikam ity anye nikāyākṣepaṇaṃ tribhiḥ |**  
> **sarvatra catur ākṣepaḥ śubhasya narake tridhā || 4.51 ||**

## Padaccheda

```text
catuḥ-koṭikam
iti
anye

nikāya-ākṣepaṇam
tribhiḥ

sarvatra
catuḥ-ākṣepaḥ

śubhasya
narake
tridhā
```

## Literal translation

> Others hold that it is four-cornered. The projection of a new continuum is accomplished by three. Everywhere there is a fourfold projection; with regard to wholesome karma in hell, it is threefold.

The final two pādas are highly compressed and require the Bhāṣya for exact distribution.

## Doctrinal determination

The verse moves through three levels:

```text
logical classification
    catuṣkoṭika

causal function
    nikāyākṣepaṇa

cosmological distribution
    sarvatra / narake
```

### Catuṣkoṭika

The four alternatives likely distinguish two questions:

```text
Is maturation fixed?
Is its temporal position fixed?
```

This yields:

```text
maturation fixed / time fixed
maturation fixed / time unfixed
maturation unfixed / time fixed
maturation unfixed / time unfixed
```

The exact doctrinal formulation remains for the Bhāṣya pass.

### Nikāyākṣepaṇa

```text
nikāya
    aggregate-series
    rebirth-continuum

ākṣepaṇa
    projection
    casting forth
```

Karma may project not merely a single result but a new aggregate-continuum of rebirth.

```text
present continuum
    performs karma

karmic determination persists

rebirth
    → a new nikāya is projected
```

This preserves causal continuity without introducing a permanent self.

### Projection and completion

The verse opens the distinction between:

```text
ākṣepaka-karma
    projecting karma

paripūraka-karma
    completing karma
```

Projecting karma establishes the basic rebirth-continuum. Completing karma determines features within that field.

### Hell and wholesome karma

Hell-birth is projected by unwholesome karma. Wholesome karma may nevertheless mature within a hell-continuum in subordinate respects.

```text
unwholesome projecting karma
    → hell rebirth

wholesome karma
    → limited results within that existence
```

The exact threefold structure of **śubhasya narake tridhā** remains commentary-dependent.

## Logical determination

The verse adds distinct dimensions:

```text
[ KARMA
  MATURATION-FIXITY fixed | unfixed
  TEMPORAL-FIXITY fixed | unfixed
  REBIRTH-FUNCTION projecting | non-projecting
  DOMAIN-OF-OPERATION determinate ]
```

The classification of karma is not identical with the function performed by karma.

## Logic of Experience

```text
[ REBIRTH-CONTINUUM
  PROJECTED-BY dominant-karma
  COMPLETED-BY additional-karmas
  DOMAIN specific-destination
  INTERNAL-RESULTS multiple ]
```

One karma may establish the field; other karmas determine events and qualities within that field.

## Organon interpretation

The phrase **nikāyākṣepaṇa** reveals karma as a projective function:

```text
KARMA
    may project an entire field
    in which subsequent results appear
```

The structural relation is:

```text
Ground
    projecting karma

Appearance
    rebirth-continuum

Determinations within Appearance
    completing karmic results
```

This directly interlocks the Karma and World chapters:

```text
karma
    as determinate relation

world
    as projected field
    in which that relation appears
```

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix karma: <http://127.0.0.1:3000/karma#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix doctrine: <http://127.0.0.1:3000/doctrine#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_51
    a vak:Karika ;
    rdfs:label "VAK 4.51" ;
    vak:continues vak:VAK_4_50 ;
    vak:hasTopic karma:FourCorneredClassification ;
    vak:hasTopic karma:RebirthProjection .

karma:FourCorneredClassification
    a logic:Catuskoti ;
    logic:hasDimension karma:MaturationFixity ;
    logic:hasDimension karma:TemporalFixity .

karma:ProjectingKarma
    a karma:KarmicFunction ;
    karma:projects karma:RebirthContinuum .

karma:RebirthContinuum
    a karma:Nikaya ;
    karma:hasDomain loka:RebirthDomain ;
    karma:mayBeCompletedBy karma:CompletingKarma .

loka:HellContinuum
    rdfs:subClassOf karma:RebirthContinuum ;
    karma:requiresProjectingKarma karma:UnwholesomeProjectingKarma .

karma:WholesomeKarma
    karma:cannotPrincipallyProject loka:HellContinuum ;
    karma:mayProduceResultWithin loka:HellContinuum .

doctrine:VAK_4_51_FinalHalf
    doctrine:status doctrine:RequiresBhashyaReview .
```

## Determinate result

VAkK 4.51 establishes:

```text
some authorities analyze karmic fixity
through four logical alternatives

three karmic modes are involved
in projecting a new aggregate-continuum

projection must be distinguished
from subordinate karmic completion
```

Its deepest result is:

```text
karma may project
not merely a particular result

but the existential field
within which results are experienced
```
