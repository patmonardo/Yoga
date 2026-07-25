# VAK_3b — VAkK_3.22

## Sanskrit — Devanāgarī

प्राक् षडायतनोत्पादात् तत्पूर्वं त्रिकसंगमात् ।
स्पर्शः प्राक्सुखदुःखादिकारणज्ञानशक्तितः ॥ VAkK_3.22 ॥

## Sanskrit — IAST

prāk ṣaḍāyatanotpādāt tatpūrvaṃ trikasaṃgamāt /
sparśaḥ prāk sukhaduḥkhādikāraṇajñānaśaktitaḥ // VAkK_3.22 //

## Working Clarification

Here `āyatana` is translated as **sphere**. It should be read as a sphere of access or interface, not as the subject itself.

The triadic contact structure is primarily:

```text
sphere
    +
object-support
    +
knowledge
        =
contact
```

This may be interpreted secondarily through the Organon as a Subject–Object–Idea style interface event. But the primary Abhidharma structure should remain sphere / object-support / knowledge.

## Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| prāk | prāk | before; prior to |
| ṣaḍāyatanotpādāt | ṣaṭ-āyatana-utpādāt | before the arising of the six spheres |
| tatpūrvam | tat-pūrvam | prior to that |
| trikasaṃgamāt | trika-saṃgamāt | before / from the conjunction of the triad |
| sparśaḥ | sparśaḥ | contact |
| prāk | prāk | before |
| sukhaduḥkhādi | sukha-duḥkha-ādi | pleasure, pain, and so forth |
| kāraṇa | kāraṇa | cause |
| jñāna | jñāna | knowing |
| śaktitaḥ | śaktitaḥ | from / before the capacity |

## Grammar

```text
prāk + ablative
    = prior to / before

ṣaḍāyatana-utpādāt
    = ablative singular
    = before the arising of the six spheres

tat-pūrvam
    = prior to that

trika-saṃgamāt
    = ablative singular
    = before the conjunction of the triad

sparśaḥ
    = nominative singular masculine
    = contact

sukha-duḥkha-ādi-kāraṇa-jñāna-śaktitaḥ
    = ablative singular compound
    = before the capacity for knowing the causes of pleasure, pain, etc.
```

The verse is elliptical and continues the sequence from 3.21:

```text
vijñāna
    ↓
nāmarūpa
    ↓
ṣaḍāyatana
    ↓
sparśa
```

## Literal Translation

Name-and-form lasts until before the arising of the six spheres; that, in turn, lasts before the conjunction of the triad. Contact lasts until before the capacity for knowing the causes of pleasure, pain, and so forth.

## Philosophical Translation

After junctional knowledge, name-and-form unfolds until the six spheres arise. The six spheres then stand prior to the conjunction of the threefold relation. Contact begins with that triadic conjunction and continues until the being has the capacity to know the causes of pleasure, pain, and related experience.

## Technical Vocabulary

| Sanskrit | Working translation | Note |
|---|---|---|
| nāmarūpa | name-and-form | Psycho-physical determinacy after junctional knowledge |
| ṣaḍāyatana | six spheres | Sixfold sphere-structure or interface structure |
| āyatana | sphere | Sphere of access; not the subject itself |
| utpāda | arising | Coming forth of a determinate structure |
| trika | triad | The threefold conjunction required for contact |
| saṃgama | conjunction | A relational event |
| sparśa | contact | A triadic cognitive-affective event |
| sukha | pleasure | Positive affective tone |
| duḥkha | pain | Negative affective tone |
| kāraṇa | cause | Cause of pleasure or pain; not hetu as ground |
| jñāna | knowing | Capacity to know causes |
| śakti | capacity / power | Developmental capacity |

## Doctrinal Determination

VAkK_3.22 gives the next three limbs of the twelvefold wheel:

```text
4. nāmarūpa
5. ṣaḍāyatana
6. sparśa
```

The verse defines them developmentally:

```text
nāmarūpa
    lasts before the arising of ṣaḍāyatana

ṣaḍāyatana
    lasts before the conjunction of the triad

sparśa
    lasts before the capacity to know the causes of pleasure and pain
```

The important phrase is **trika-saṃgama**, conjunction of the triad.

For the project vocabulary:

```text
sphere
    +
object-support
    +
knowledge
        =
contact
```

## Logical Determination

Each limb is determined by what it is prior to.

```text
nāmarūpa
    = threshold toward articulated spheres

ṣaḍāyatana
    = threshold toward triadic conjunction

sparśa
    = threshold toward affective-causal knowing
```

In Hegel-clean terms:

```text
immediate psycho-physical determinacy
    becomes differentiated sphere-structure
    becomes triadic relation
    becomes contact
    becomes capacity to know affective causality
```

The middle eight are therefore not merely events. They are successive concretions of embodiment.

## Organon Interpretation

VAkK_3.22 expands semantic embodiment into interface architecture:

```text
Nāmarūpa
    = embodied schema

Ṣaḍāyatana
    = sixfold interface layer / sphere-structure

Trika-saṃgama
    = runtime conjunction of sphere, object-support, knowledge

Sparśa
    = contact event

Sukha-duḥkha-kāraṇa-jñāna-śakti
    = capacity for affective causal recognition
```

This should not be flattened into a simple subject-object relation. The safer formulation is:

```text
A junctional knowledge-event
    unfolds into name-and-form,
    differentiates into spheres,
    enters triadic conjunction,
    produces contact,
    and only then develops the capacity to know pleasure/pain causality.
```

Thus the world is generated as interface-contact, not as substance.

## OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_22
    a vak:Karika ;
    rdfs:label "VAkK 3.22" ;
    vak:continues vak:VAK_3_21 ;
    vak:hasTopic vak:DependentCoArising ;
    vak:explicatesLimb vak:Namarupa ;
    vak:explicatesLimb vak:SadAyatana ;
    vak:explicatesLimb vak:Sparsa .

vak:SadAyatana
    a vak:DependentCoArisingLimb ;
    rdfs:label "ṣaḍāyatana" ;
    vak:hasCanonicalTranslation "six spheres" ;
    vak:belongsToSection vak:MadhyaSection ;
    vak:definedByLimit vak:TrikaSamgama .

vak:TrikaSamgama
    a logic:TriadicConjunction ;
    rdfs:label "trika-saṃgama" ;
    vak:hasCanonicalTranslation "conjunction of the triad" .

vak:Sparsa
    a vak:DependentCoArisingLimb ;
    rdfs:label "sparśa" ;
    vak:hasCanonicalTranslation "contact" ;
    vak:arisesFrom vak:TrikaSamgama .
```

## Commit Note

Committed VAK_3b / VAkK_3.22.

Established:
- nāmarūpa is defined as prior to the arising of ṣaḍāyatana.
- ṣaḍāyatana is defined as prior to trika-saṃgama.
- āyatana is treated as a sphere of access/interface, not the subject itself.
- sparśa arises through triadic conjunction.
- sparśa lasts prior to the capacity to know the causes of pleasure and pain.
