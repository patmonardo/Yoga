# VAkK 4.46

## Sanskrit

### Devanāgarī

> कामधातौ शुभं कर्म पुण्यमानेञ्जमूर्ध्वजम् ।  
> तद्भूमिषु यतः कर्मविपाकं प्रति नेञ्जति ॥ ४.४६ ॥

### IAST

> **kāmadhātau śubhaṃ karma puṇyam āneñjam ūrdhvajam |**  
> **tadbhūmiṣu yataḥ karma vipākaṃ prati neñjati || 4.46 ||**

## Padaccheda

```text
kāma-dhātau
śubham
karma
puṇyam |

āneñjam
ūrdhva-jam |

tad-bhūmiṣu
yataḥ
karma
vipākam
prati
na
iñjati ||
```

## Literal translation

> **Wholesome karma in the desire-domain is meritorious. That which is produced above is immovable, because in those levels karma does not move with respect to maturation.**

## Doctrinal determination

VAkK 4.46 defines two members of the triad announced in 4.45:

```text
puṇya
    wholesome karma in the desire-domain

āneñja
    karma produced in the higher domains
```

The unstated middle member is **apuṇya**, unwholesome karma.

The higher karma is called **immovable** because its maturation does not shift away from the level corresponding to its production:

```text
higher meditative level
    → determinate karma
    → maturation in the corresponding level
```

This immovability is relative, not absolute:

```text
āneñja
    ≠ unconditioned

āneñja
    = fixed with respect to maturation-domain
```

## Philosophical translation

> **Wholesome action belonging to the desire-domain is classified as meritorious. Action generated in the higher meditative domains is called immovable because its maturation remains fixed to its corresponding level and does not shift to another plane.**

## Logic of Experience

```text
[ KARMA
  ETHICAL-QUALITY wholesome
  PRODUCTION-DOMAIN desire
  DOMAIN-EFFICACY puṇya ]
```

```text
[ KARMA
  ETHICAL-QUALITY wholesome
  PRODUCTION-DOMAIN higher
  MATURATION-DOMAIN corresponding-higher-level
  DOMAIN-EFFICACY āneñja
  MATURATION-MOBILITY fixed ]
```

The classification depends on both quality and domain:

```text
wholesome karma
    in desire-domain
        → meritorious

wholesome karma
    in higher domains
        → immovable
```

## Organon interpretation

The term **āneñja** expresses a functional invariance:

```text
originating cognitive level
        ↓
determinate action
        ↓
corresponding maturation-level
```

The karma does not move relative to this mapping. The domain in which karma is generated determines the domain-structure of its maturation.

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix karma: <http://127.0.0.1:3000/karma#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_46
    a vak:Karika ;
    rdfs:label "VAK 4.46" ;
    vak:continues vak:VAK_4_45 ;
    vak:determines karma:Punya ;
    vak:determines karma:Anenja ;
    vak:hasTopic karma:DomainIndexedMaturation .

karma:Punya
    a karma:DomainEfficacyClassification ;
    karma:hasEthicalQuality karma:Wholesome ;
    karma:hasProductionDomain loka:DesireDomain .

karma:Anenja
    a karma:DomainEfficacyClassification ;
    karma:hasProductionDomain loka:HigherDomain ;
    karma:hasMaturationMobility karma:Fixed ;
    karma:maturesInCorrespondingDomain true .
```

## Determinate result

```text
wholesome desire-domain karma
    = puṇya

higher-domain karma
    = āneñja
```

Its central principle is:

```text
the domain in which karma is generated
determines the domain-structure
of its maturation
```
