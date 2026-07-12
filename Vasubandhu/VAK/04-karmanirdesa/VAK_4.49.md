# VAkK 4.49

## Sanskrit

### Devanāgarī

> स्वभावसंप्रयोगाभ्यामालम्बनविपाकतः ।  
> संमुखीभावतश्चेति पञ्चधा वेदनीयता ॥ ४.४९ ॥

### IAST

> **svabhāva-saṃprayogābhyām ālambana-vipākataḥ |**  
> **saṃmukhībhāvataś ceti pañcadhā vedanīyatā || 4.49 ||**

## Padaccheda

```text
svabhāva-saṃprayogābhyām
ālambana-vipākataḥ
saṃmukhī-bhāvataḥ
ca iti
pañcadhā vedanīyatā
```

Expanded into five grounds:

```text
svabhāvataḥ
saṃprayogataḥ
ālambanataḥ
vipākataḥ
saṃmukhībhāvataḥ
```

## Literal translation

> **The condition of being “to be experienced” is fivefold: by intrinsic nature, by association, by object-support, by maturation, and by becoming immediately present.**

## Doctrinal determination

The verse distinguishes five grounds for experiential designation:

```text
1. identity
   the dharma is itself feeling

2. association
   the dharma is conjoined with feeling

3. object-support
   the dharma is that upon which feeling takes hold

4. maturation
   the dharma produces feeling through karmic maturation

5. immediate presence
   feeling has become presently manifest
```

Karma is called **vedanīya** chiefly in the fourth sense. It is not itself the later feeling; rather, it matures into an experience characterized as pleasant, painful, or neither.

## Technical vocabulary

```text
svabhāva
    intrinsic nature

saṃprayoga
    association or conjunction

ālambana
    object-support

vipāka
    maturation

saṃmukhībhāva
    becoming immediately present

vedanīyatā
    the condition or mode of being experienced
```

## Logical determination

One predicate is licensed through several distinct relational structures:

```text
VEDANIYA(X)
    because X is feeling

VEDANIYA(X)
    because X is associated with feeling

VEDANIYA(X)
    because X is the object-support of feeling

VEDANIYA(X)
    because X produces feeling through maturation

VEDANIYA(X)
    because X is presently manifest as feeling
```

The shared predicate must not obscure the typed relation grounding its application.

## Logic of Experience

```text
[ VEDANIYA-STATUS
  MODE
    intrinsic
    | associated
    | object-supported
    | maturation-produced
    | presently-manifest ]
```

This prevents a reasoner from collapsing:

```text
is feeling
causes feeling
is associated with feeling
is the object-support of feeling
is presently felt
```

## Organon interpretation

The verse gives a compact theory of predication through relation:

```text
one predicate
    does not imply
one mode of determination
```

A semantic attribution must therefore preserve the relation that licenses it. “Karma is experienced” means that karma produces experience through maturation, not that karma is identical with feeling.

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix karma: <http://127.0.0.1:3000/karma#> .
@prefix cognition: <http://127.0.0.1:3000/cognition#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_49
    a vak:Karika ;
    rdfs:label "VAK 4.49" ;
    vak:continues vak:VAK_4_48 ;
    vak:hasTopic cognition:FiveModesOfExperientialDesignation .

cognition:ExperientialDesignation
    cognition:hasMode cognition:ByIntrinsicNature ;
    cognition:hasMode cognition:ByAssociation ;
    cognition:hasMode cognition:ByObjectSupport ;
    cognition:hasMode cognition:ByMaturation ;
    cognition:hasMode cognition:ByImmediatePresence .

cognition:Feeling
    cognition:isExperientiallyDesignatedBy cognition:ByIntrinsicNature .

karma:Karma
    cognition:isExperientiallyDesignatedBy cognition:ByMaturation ;
    karma:mayProduce cognition:Feeling .
```

## Determinate result

VAkK 4.49 establishes five meanings of experiential designation:

```text
by intrinsic nature
by association
by object-support
by maturation
by immediate presence
```

Its decisive clarification is:

```text
karma is called “to be experienced”
not because karma is itself feeling
but because karma produces feeling
through maturation
```
