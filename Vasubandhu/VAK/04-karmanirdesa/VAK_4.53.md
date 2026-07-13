# VAkK 4.53

## Sanskrit — Devanāgarī

द्वाविंशतिविधं कामेष्वाक्षिपत्यन्तराभवः ।
दृष्टधर्मफलं तच्च निकायो ह्येक एव सः ॥ ४.५३ ॥

## Sanskrit — IAST

dvāviṃśatividhaṃ kāmeṣv ākṣipaty antarābhavaḥ /
dṛṣṭadharmaphalaṃ tac ca nikāyo hy eka eva saḥ // VAkK_4.53 //

## Padaccheda

dvāviṃśati-vidham
kāmeṣu
ākṣipati
antarābhavaḥ

dṛṣṭa-dharma-phalam
tat
ca

nikāyaḥ
hi
ekaḥ
eva
saḥ

## Literal translation

> In the desire-domain, the intermediate existence projects a twenty-twofold determination. That also has its result in the present existence, for that aggregate-continuum is one and the same.

## Philosophical translation

> Within the desire-domain, the intermediate continuum possesses a twenty-twofold range of projective karmic determination. An action performed during this intermediate phase may mature after rebirth and yet still count as producing its result in the same life, because intermediate existence and rebirth existence are successive phases of one causal aggregate-series.

## Doctrinal determination

The **antarābhava** is not a merely passive transit state. The verse attributes to it the active verb **ākṣipati**, “it projects.” It therefore retains karmic activity and projective efficacy.

The number twenty-two is doctrinally exact, although the kārikā does not enumerate its members. The internal derivation belongs to the Bhāṣya pass.

The decisive proposition is:

```text
nikāyo hy eka eva saḥ
    for that aggregate-continuum is one and the same
```

This does not assert a permanent subject. Intermediate aggregates cease, rebirth aggregates arise in immediate causal succession, and the series is treated as one **nikāya**.

Accordingly, karma produced in intermediate existence and maturing after entry into rebirth existence can still be classified as **dṛṣṭadharmaphala**, a result in the present existence. The criterion is continuity of the karmic series, not visible bodily identity.

## Logical determination

```text
IF
    action-time = intermediate phase
    result-time = rebirth phase
    continuum(intermediate) = continuum(rebirth)

THEN
    result-class = present-life
```

Thus temporal distance alone does not determine the karmic time-class. Continuum identity is also required.

## Organon interpretation

The projected field unfolds through phases:

```text
projective transition
    antarābhava

embodied actualization
    upapattibhava
```

Yet these remain one functional continuum. Projection is not the transport of a substance but the continuation of a causal organization into a new field of appearance.

```text
nikāya identity
    = continuity of causal organization
      across phase transformation
```

This is identity of process through difference of appearance.

## OWL++ seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix karma: <http://127.0.0.1:3000/karma#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_53
    a vak:Karika ;
    rdfs:label "VAK 4.53" ;
    vak:continues vak:VAK_4_52 ;
    vak:hasTopic karma:IntermediateExistenceProjection ;
    vak:hasTopic karma:ContinuumRelativeTemporalResult .

loka:IntermediateExistence
    a loka:ConditionedContinuum ;
    loka:occursIn loka:DesireDomain ;
    karma:hasProjectiveRange karma:TwentyTwofoldRange ;
    loka:hasNikayaIdentity loka:NikayaN1 .

loka:RebirthExistence
    a loka:ConditionedContinuum ;
    loka:immediatelySucceeds loka:IntermediateExistence ;
    loka:hasNikayaIdentity loka:NikayaN1 .

karma:IntermediateExistenceKarma
    karma:producedIn loka:IntermediateExistence ;
    karma:mayMatureIn loka:RebirthExistence ;
    karma:hasTemporalResultClass karma:PresentLifeResult .
```

## Determinate result

VAkK 4.53 establishes that the desire-domain intermediate existence has a twenty-twofold projective range, and that karma produced in the intermediate phase may mature after rebirth while still counting as present-life-result karma because the two phases constitute one aggregate-continuum.
