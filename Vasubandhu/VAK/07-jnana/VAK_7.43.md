# VAK_7.43 — The Cognitive Composition and Dhyānic Ground of the Abhijñās

## Sanskrit

### IAST

```text
catasraḥ saṃvṛtijñānaṃ cetasi jñānapañcakam /
kṣayābhijñā balaṃ yadvat pañca dhyānacatuṣṭaye // VAK_7.43 //
```

## Padaccheda

```text
catasraḥ
saṃvṛti-jñānam
cetasi
jñāna-pañcakam
kṣaya-abhijñā
balam
yadvat
pañca
dhyāna-catuṣṭaye
```

## Literal Translation

Four are conventional knowledge. Regarding mind there is a group of five knowledges. The direct knowledge of exhaustion is as with the corresponding Buddha-power. Five are grounded in the four dhyānas.

## Philosophical Translation

The first four direct knowledges remain conventional because their objects belong to the conditioned field. Direct knowledge of another mind is one unified capacity constituted through five kinds of knowing. Knowledge of the exhaustion of the influxes has the same cognitive composition as the corresponding Buddha-power. The first five abhijñās depend upon the four dhyānas as their contemplative ground.

## Analysis

### 1. Four are conventional knowledge

The first four abhijñās concern extraordinary efficacy, purified hearing, another mind, and former lives. Their range may exceed ordinary cognition, yet their objects remain conditioned.

```text
extraordinary cognition
    ≠
ultimate cognition
```

`saṃvṛti-jñāna` does not mean false cognition. It marks the level of the object: conditioned appearance may be known exactly as conditioned appearance.

### 2. Other-mind knowledge contains five knowledges

`cetasi jñāna-pañcakam` shows that a single named capacity may have an internally plural epistemic composition.

```text
unity of developed capacity
    does not imply
simplicity of cognitive constitution
```

Adequate knowledge of another mind requires determination of its present condition, afflictive quality, contemplative level, degree of concentration, and relation to liberation. Direct presence does not abolish discrimination; it makes discrimination adequate to the living object.

### 3. Knowledge of exhaustion corresponds to the Buddha-power

`kṣayābhijñā balaṃ yadvat` links the sixth abhijñā with the corresponding Buddha-power concerning the exhaustion of the influxes. The identity concerns cognitive form, not equality of range, universality, spontaneity, or completeness.

```text
same essential object and knowledge-form
    ≠
same manifest measure
```

The sixth abhijñā is not merely another enlargement of conditioned cognition. It directly knows that the afflictive ground of bondage has been exhausted.

### 4. Five depend upon the four dhyānas

The first five abhijñās arise on the basis of the four rūpa-dhyānas. Dhyāna here is not private repose but the power-plant of transformed cognition.

```text
withdrawal from ordinary dispersion
    ↓
unification of cognitive power
    ↓
expanded knowledge and efficacy
```

The sixth is governed instead by liberative wisdom: concentration expands and stabilizes cognition, while prajñā penetrates and terminates bondage.

### 5. Pure Practical Reason

VAK 7.42 displayed raw practical power. VAK 7.43 subjects that power to critical determination according to object, knowledge-type, internal composition, contemplative ground, and liberative status.

```text
practical efficacy
    +
critical classification
    =
rational power
```

The Kośa refuses both abstract reason without power and power without rational determination.

## Logical Architecture

```text
Cognitive level
    four are conventional

Internal plurality
    other-mind knowledge contains five knowledges

Formal correspondence
    exhaustion-knowledge resembles the Buddha-power

Ground
    the first five depend upon the four dhyānas
```

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix path: <http://127.0.0.1:3000/path#> .
@prefix dhyana: <http://127.0.0.1:3000/dhyana#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_43
    a vak:Karika ;
    rdfs:label "VAK 7.43" ;
    vak:determines jna:CognitiveCompositionOfAbhijnas .

jna:FirstFourAbhijnas
    a jna:ConventionalKnowledgeGroup .

jna:OtherMindAbhijna
    jna:isComposedOf jna:FiveKnowledges .

jna:InfluxExhaustionAbhijna
    jna:hasCognitiveComposition jna:InfluxExhaustionBuddhaPowerComposition ;
    path:certifies path:ExhaustionOfInfluxes .

jna:FirstFiveAbhijnas
    path:hasGround dhyana:FirstDhyana,
                   dhyana:SecondDhyana,
                   dhyana:ThirdDhyana,
                   dhyana:FourthDhyana .
```

## Kārikā-Pass Determination

```text
The first four direct knowledges
are conventional because they know conditioned fields.

Knowledge of another mind
is one developed capacity
composed through five kinds of knowledge.

Knowledge of exhaustion
has the cognitive structure
of the corresponding Buddha-power.

The first five depend upon the four dhyānas:
contemplative unification becomes expanded practical cognition.

The sixth exceeds mere expansion.
It directly knows that the work of liberation is complete.
```
