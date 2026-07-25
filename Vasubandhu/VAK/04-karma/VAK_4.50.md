# VAkK 4.50

## Sanskrit

### Devanāgarī

> नियतामनियतं तच्च नियतं त्रिविधं पुनः ।  
> दृष्टधर्मादिवेद्यत्वात् पञ्चधा कर्म केचन ॥ ४.५० ॥

### IAST

> **niyatāniyataṃ tac ca niyataṃ trividhaṃ punaḥ |**  
> **dṛṣṭadharmādi-vedyatvāt pañcadhā karma kecana || 4.50 ||**

## Padaccheda

```text
niyata-aniyatam
tat ca
niyatam trividham punaḥ
dṛṣṭa-dharma-ādi-vedyatvāt
pañcadhā karma kecana
```

## Literal translation

> That karma is determinate or indeterminate. The determinate is again threefold because it is to be experienced beginning in the present life. Some hold karma to be fivefold.

## Doctrinal determination

The first division concerns the fixity of maturation:

```text
niyata
    determinate or fixed maturation

aniyata
    indeterminate or unfixed maturation
```

Determinate karma is threefold according to when its maturation is experienced:

```text
dṛṣṭadharma-vedanīya
    in the present life

upapadya-vedanīya
    in the immediately following rebirth

aparaparyāya-vedanīya
    in a later existence
```

This temporal indeterminacy must not be confused with **avyākṛta**, ethical indeterminacy.

## Logical determination

```text
KARMA
    MATURATION-FIXITY
        fixed | unfixed

FIXED-KARMA
    MATURATION-TIME
        present-life
        next-life
        later-life
```

Karma is therefore a temporally indexed causal relation. It may determine not only the character of maturation but also its temporal position.

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix karma: <http://127.0.0.1:3000/karma#> .
@prefix time: <http://127.0.0.1:3000/time#> .
@prefix doctrine: <http://127.0.0.1:3000/doctrine#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_50
    a vak:Karika ;
    rdfs:label "VAK 4.50" ;
    vak:continues vak:VAK_4_49 ;
    vak:hasTopic karma:MaturationFixity ;
    vak:hasTopic karma:TemporalMaturation .

karma:DeterminateKarma
    rdfs:subClassOf karma:Karma ;
    karma:hasMaturationFixity karma:Fixed ;
    karma:hasTemporalMaturation
        karma:PresentLifeMaturation,
        karma:NextLifeMaturation,
        karma:LaterLifeMaturation .

karma:IndeterminateKarma
    rdfs:subClassOf karma:Karma ;
    karma:hasMaturationFixity karma:Unfixed .

doctrine:FivefoldKarmaClassification
    a doctrine:AlternativeClassification ;
    doctrine:attributedTo doctrine:SomeAuthorities ;
    doctrine:status doctrine:RequiresBhashyaReview .
```

## Determinate result

VAkK 4.50 establishes determinate and indeterminate karma. Determinate karma is to be experienced in the present life, the next life, or a later life; some authorities instead formulate a fivefold classification.
