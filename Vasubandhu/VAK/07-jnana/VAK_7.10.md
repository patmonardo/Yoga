# VAK_7.10 — The Aspects of the Knowledges

## Sanskrit

### Devanāgarī

```text
धर्मज्ञानान्वयज्ञानं षोडशाकारमन्यथा ।
तथा च सांवृतं स्वैः स्वैः सत्याकारैश्चतुष्टयम् ॥ ७.१० ॥
```

### IAST

```text
dharmajñānānvayajñānaṃ ṣoḍaśākāram anyathā /
tathā ca sāṃvṛtaṃ svaiḥ svaiḥ satyākāraiś catuṣṭayam // VAK_7.10 //
```

## Source Caution

The verse is compressed and distributes the ground of `ākāra` introduced in VAK 7.08. The most natural first-pass reading is:

```text
dharmajñāna and anvayajñāna
    possess the sixteen truth-aspects

saṃvṛtijñāna
    may likewise possess those sixteen
    and may also operate under other aspects

the four truth-knowledges
    each possess the four aspects proper to their own truth
```

The exact scope of `anyathā` is therefore preserved cautiously as indicating that conventional knowledge is not restricted to the sixteen truth-aspects.

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| dharma-jñāna-anvaya-jñānam | compound, nominative singular neuter | dharma-knowledge and subsequent/concordant knowledge |
| ṣoḍaśa-ākāram | nominative singular neuter | having sixteen aspects |
| anyathā | indeclinable | otherwise; in another manner |
| tathā | indeclinable | likewise; in that manner |
| ca | indeclinable | and |
| sāṃvṛtam | nominative singular neuter | conventional knowledge |
| svaiḥ svaiḥ | instrumental plural, distributive | by their own respective |
| satya-ākāraiḥ | instrumental plural | truth-aspects |
| catuṣṭayam | nominative singular neuter | the group of four |

## Grammar

The first pāda identifies a shared aspect-structure:

```text
dharmajñāna
    sixteen-aspected

anvayajñāna
    sixteen-aspected
```

`anyathā tathā ca sāṃvṛtam` indicates that conventional knowledge may operate in the same sixteenfold manner and also otherwise.

`svaiḥ svaiḥ satyākāraiś catuṣṭayam` refers to the four truth-knowledges:

```text
duḥkhajñāna
samudayajñāna
nirodhajñāna
mārgajñāna
```

Each is limited to the four aspects proper to its respective truth.

## Literal Translation

Dharma-knowledge and anvaya-knowledge have sixteen aspects. Conventional knowledge is likewise so and also otherwise. The group of four possesses the respective aspects of its own truths.

## Philosophical Translation

Dharma-knowledge and anvaya-knowledge can apprehend the complete sixteenfold articulation of the Four Noble Truths. Conventional knowledge may also take up those same aspects, but it is not confined to them. The four truth-knowledges are more determinate: each knows only through the four aspects belonging to its own truth.

## Technical Vocabulary

### ṣoḍaśākāra

```text
sixteen aspects
    = four truths
        ×
      four aspects proper to each truth
```

A standard arrangement is:

| Truth | Four aspects |
|---|---|
| suffering | impermanent, suffering, empty, non-self |
| origin | cause, arising, production, condition |
| cessation | cessation, peace, excellence, escape |
| path | path, method, practice, leading out |

The present verse does not enumerate these terms, but presupposes this sixteenfold truth-structure.

### anyathā

```text
anyathā
    = otherwise
    = under aspects beyond the sixteen truth-aspects
```

This marks the relative breadth of conventional knowledge. Its object-field and modes of apprehension are not exhausted by the path-specific truth-aspects.

### svaiḥ svaiḥ satyākāraiḥ

```text
by their own respective truth-aspects
```

The distributive repetition `svaiḥ svaiḥ` is important. It prevents the four truth-knowledges from collapsing into one undifferentiated sixteen-aspected cognition.

## Doctrinal Determination

The verse distinguishes breadth from restriction.

```text
dharmajñāna
    all sixteen truth-aspects

anvayajñāna
    all sixteen truth-aspects

saṃvṛtijñāna
    the sixteen truth-aspects
    plus other conventional aspects

four truth-knowledges
    four aspects each
    restricted to their respective truth
```

Thus identity of aspect does not erase difference of knowledge. Several knowledges may employ the same aspect while differing through object-domain, purity, function, preparation, or path-position.

## Logical Determination

VAK 7.10 applies the `ākāra` ground announced in VAK 7.08.

The division is not grounded merely by counting objects. It is grounded by the range and distribution of determinate modes of apprehension.

```text
universal aspect-range
    dharmajñāna
    anvayajñāna

open aspect-range
    saṃvṛtijñāna

restricted aspect-range
    each of the four truth-knowledges
```

The four truth-knowledges are distinguished distributively:

```text
one truth
    four proper aspects
```

The two broader knowledges can traverse the full truth-system:

```text
four truths
    sixteen aspects
```

This remains grounded Reflection. The verse states where each cognition stands and under which aspects it operates; it does not yet derive these forms genetically from a single Concept.

## Organon Light

The main scientific point is simple:

> A knowledge is determined not only by its object, but by the range of aspects under which it can know.

This gives the Organon Dataset a sharper requirement. A knowledge-entry cannot be represented merely as:

```text
knowledge
    → object
```

It must also include:

```text
knowledge
    → permitted aspects
    → aspect-range
    → relation to truth-domain
```

VAK 7.10 therefore continues the grounding program without leaving the Kośa's own reflective level.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_10
    a vak:Karika ;
    rdfs:label "VAK 7.10" ;
    vak:determines jna:SixteenTruthAspects,
                   jna:UniversalAspectRange,
                   jna:OpenAspectRange,
                   jna:RestrictedTruthAspectRange .

jna:DharmaKnowledge
    jna:hasAspectRange jna:SixteenTruthAspects .

jna:AnvayaKnowledge
    jna:hasAspectRange jna:SixteenTruthAspects .

jna:ConventionalKnowledge
    jna:hasAspectRange jna:SixteenTruthAspects,
                       jna:OtherConventionalAspects .

jna:FourTruthKnowledges
    jna:hasAspectRange jna:RespectiveFourTruthAspects .
```

## Commit History

```text
2026-07-23 — Initial kārikā-pass analysis.
```
