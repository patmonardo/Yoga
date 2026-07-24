# VAK_7.49 — The Constructed Field of Rūpa

## Sanskrit

```text
kāmāptaṃ nirmitaṃ bāhyaṃ caturāyatanaṃ dvidhā /
rūpāptaṃ dve tu nirmāṇacittaistāni caturdaśa // VAK_7.49 //
```

## Padaccheda

```text
kāma-āptam
nirmitam
bāhyam
catur-āyatanam
dvidhā

rūpa-āptam
dve
tu

nirmāṇa-cittaiḥ
tāni
caturdaśa
```

| Term | Working sense |
|---|---|
| kāmāptam | belonging to or obtained in the desire realm |
| nirmitam | constructed, projected, produced |
| bāhyam | external |
| caturāyatanam | consisting of four sense-fields |
| dvidhā | twofold |
| rūpāptam | belonging to or obtained in the form realm |
| dve | two |
| nirmāṇacittaiḥ | by construction-minds, minds of projection |
| caturdaśa | fourteen |

## Literal Translation

What is constructed in the desire realm is external and consists of four sense-fields, in two modes. What belongs to the form realm consists of two. The minds of construction by which these are produced are fourteen.

## Philosophical Translation

Constructive cognition does not create an indeterminate apparition. In the desire realm it projects an external sensible complex structured through four objective sense-fields; in the form realm the projection is reduced to two. These constructions are generated through fourteen determinate types of construction-consciousness.

# 1. From Power to Product

VAK 7.48 gave the operative powers:

```text
gamana
    movement

nirmāṇa
    formation
```

VAK 7.49 turns from the act of construction to the constitution of the constructed object.

```text
7.48
    What does power do?

7.49
    What sort of objective field
    does constructive power produce?
```

Nirmāṇa is not left as a vague magical capacity. Its output is classified according to realm, externality, sensory composition, and cognitive cause.

# 2. Nirmitam Bāhyam — The Constructed Is External

```text
nirmitam bāhyam
    the constructed is external
```

The projection is not merely a private inner image. It appears as an objective sensible formation.

```text
mental image
    representation within cognition

nirmita
    projected form
    established in an external field
```

The verse therefore distinguishes construction from imagination. A projected object has objective placement within the relevant world-system.

# 3. The Four External Āyatanas

In the desire realm, the constructed object consists of four sense-fields:

```text
rūpa
    visible form

gandha
    smell

rasa
    taste

spraṣṭavya
    tangible quality
```

Sound is excluded because sound is more event-like and depends upon further activity. Thus the projected object is not merely visual; it has a richer sensible constitution.

# 4. State-Features and Event-Features

The omission of sound suggests a primitive distinction:

```text
form, smell, taste, touch
    state-features
    what the constructed object is

sound
    event-feature
    what the constructed object does
```

This belongs directly in the Organon Dataset.

# 5. Dvidhā — Typed Construction

The twofold division indicates that nirmāṇa is not one homogeneous operation. The constructed object is instantiated under a determinate mode.

```text
nirmāṇa
    is typed

not merely:
    construct form

but:
    construct form under a determinate mode
```

# 6. The Form-Realm Reduction

```text
rūpāptaṃ dve
    in the form realm, two
```

The constructed object in the rūpa-dhātu possesses only visible form and tangibility.

```text
Kāma-dhātu construction
    visible
    tangible
    odorous
    gustatory

Rūpa-dhātu construction
    visible
    tangible
```

The form realm is therefore a world with a narrower sensory ontology, not merely vague subtle matter.

# 7. Rūpa-Dhātu as Restricted Feature Space

The higher world is scientifically expressible as a reduced feature-space. Certain empirical determinations are absent, while externality and sensible structure remain.

This fits the account of rūpa-dhātu devas as gods of sensibility inhabiting worlds structured by a refined subset of sensible predicates.

# 8. Object-Side Feature Architecture

A constructed object is defined by a set of active sensible features:

```text
ConstructedObject {
    visibleForm
    smell
    taste
    tangibility
}
```

or, in the form realm:

```text
ConstructedObject {
    visibleForm
    tangibility
}
```

This is the object-side analogue of citta-caitta:

```text
citta-caitta
    cognition analyzed through co-operative features

nirmita-rūpa
    object analyzed through co-present sensible features
```

The Kośa is constructing a general feature ontology of actuality.

# 9. Fourteen Construction-Minds

```text
nirmāṇacittais tāni caturdaśa
    these are produced by fourteen construction-minds
```

There is no single undifferentiated creative mind. Construction is governed by a finite architecture of cognitive operators.

```text
different construction
    requires
    different cognitive ground
```

# 10. Nirmāṇa-Citta Is Not Citta in General

```text
citta
    cognitive occurrence

nirmāṇa-citta
    cognitive occurrence
    whose operative form is construction
```

This marks the transition from transcendental idealism to systematic science:

```text
consciousness conditions appearance
```

becomes:

```text
this determinate type of consciousness
produces this determinate type of appearance
under these determinate conditions
```

# 11. Construction as Typed Kriyā

```text
Samādhi
    power-ground

Nirmāṇa-citta
    operation-specific cognitive state

Nirmāṇa
    formative act

Nirmita
    constructed product

Āyatana-profile
    sensible feature structure
```

The complete pipeline is:

```text
Ground
    → Operator
    → Operation
    → Product
    → Feature profile
```

# 12. Rationalist–Empirical Conjunction

Pure Reason gives the universal operation of formation. The empirical-systematic analysis determines the actual product:

```text
which realm?
which sensory fields?
which construction-mind?
which mode?
```

The universal is not abandoned. It becomes exact.

# 13. Nature–Spirit Conjunction

```text
Spirit
    nirmāṇa-citta
    formative cognition

Nature
    external object
    articulated into sensible fields

Conjunction
    constructive cognition
    produces determinate sensible externality
```

This is already beyond the Science of Logic taken in isolation and belongs to the larger System of Science.

# 14. The World Speaks Through Its Āyatanas

Sabīja cognition allows the World to speak through determinate channels:

```text
visibility
tangibility
smell
taste
```

An āyatana is a domain in which subject and object can enter relation. A constructed object is therefore a relation-ready world-fragment.

# 15. A Scientific Theory of Projection

The verse blocks both naïve realism and subjective fantasy.

```text
cognitively generated
    and
objectively articulated
```

The cognitive principle and phenomenal field are neither collapsed nor absolutely separated.

# 16. GDSL Model

```text
ConstructionOperation {
    sourceAgent
    sourceRealm
    samadhiGround
    constructionMindType
    constructionMode
    targetRealm
    outputFeatureProfile
}
```

Possible profiles:

```text
KamaRealmProfile {
    visible = true
    smell = true
    taste = true
    tangible = true
}

RupaRealmProfile {
    visible = true
    tangible = true
    smell = false
    taste = false
}
```

Rule:

```text
construction is valid only when
operator,
realm,
and output feature-profile
are compatible
```

# 17. Agentic Interpretation

The verse distinguishes internal representation from externally instantiated artifact.

```text
internal form
    plan, image, concept

external construction
    artifact with usable features
```

The scientific question is not merely whether something was generated, but what affordances the generated object possesses and in which world it is valid.

# 18. Hegel-Clean Interpretation

```text
Subjective Concept
    nirmāṇa-citta

Purpose
    determinate projected form

Means
    samādhi-grounded operation

Realized End
    external nirmita object
```

Objectivity becomes actual only as a structured field of possible relations.

# 19. Fichtean Interpretation

Productive cognition determines a field of appearance. The object is neither an alien thing wholly outside Knowing nor a fiction with no objective force. It is a determinate appearance produced according to lawful cognitive conditions.

# 20. Beginning–End Relation

At the End we encounter constructed worlds, typed operators, and realm-specific feature profiles. This points back to the Beginning:

```text
Samāpatti
    immediate conjunction
    of cognition and object

Nirmāṇa
    that conjunction
    made productively operative

Nirmita
    the conjunction externalized
    as a determinate world-fragment
```

# Condensed Principle

> Nirmāṇa is not arbitrary creation. It is a samādhi-grounded cognitive operation that produces an external object with a realm-specific and scientifically enumerable feature structure.

```text
Pure Reason gives the form of construction.

Nirmāṇa-citta supplies the operator.

Kriyā produces the object.

The āyatanas certify its empirical actuality.
```
