# VAK_1.10

## 1. Sanskrit (Devanāgarī)

> रूपं द्विधा विंशतिधा शब्दस्त्वष्टविधः रसः ।
>
> षोढा चतुर्विधो गन्धः स्पृश्यमेकादशात्मकम् ॥ १.१० ॥

## 2. Sanskrit (IAST)

> rūpaṃ dvidhā viṃśatidhā śabdas tv aṣṭavidhaḥ rasaḥ /
>
> ṣoḍhā caturvidho gandhaḥ spṛśyam ekādaśātmakam // VAkK_1.10 //

Source label in GRETIL: `VAkK_1.10`. Project-normalized label: `VAkK_1.10`.

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| rūpam | rūpam | visible form / form-object |
| dvidhā | dvidhā | twofold |
| viṃśati-dhā | viṃśati-dhā | twentyfold |
| śabdaḥ tu | śabdaḥ tu | sound, however |
| aṣṭa-vidhaḥ | aṣṭa-vidhaḥ | eightfold |
| rasaḥ | rasaḥ | taste |
| ṣoḍhā | ṣoḍhā | sixfold |
| catur-vidhaḥ | catur-vidhaḥ | fourfold |
| gandhaḥ | gandhaḥ | smell |
| spṛśyam | spṛśyam | tangible / touchable |
| ekādaśa-ātmakam | ekādaśa-ātmakam | elevenfold in nature |

## 4. Grammar

The verse subdivides the five material object-domains:

```text
rūpa
    = twofold / twentyfold

śabda
    = eightfold

rasa
    = sixfold

gandha
    = fourfold

spṛśya
    = elevenfold
```

Here **rūpa** means visible form as object-domain, not the whole rūpa aggregate defined in VAK_1.09.

## 5. Literal Translation

> Visible form is twofold and twentyfold. Sound is eightfold; taste is sixfold; smell is fourfold; the tangible is elevenfold in nature.

## 6. Philosophical Translation

> The object-domain of form is internally differentiated into two and then twenty modes. Sound, taste, smell, and tangibility are likewise subdivided into their proper modal structures.

Organon rendering:

> The object-field is not immediate uniform matter. Each sensory object-domain has an internal articulation. Form, sound, taste, smell, and tangibility are differentiated domains, each with its own count and structure.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| rūpa | visible form | here object-domain, not the whole rūpa aggregate |
| dvidhā | twofold | primary division of visible form |
| viṃśatidhā | twentyfold | extended modal subdivision |
| śabda | sound | eightfold |
| rasa | taste | sixfold |
| gandha | smell | fourfold |
| spṛśya | tangible / touchable | elevenfold; later linked to mahābhūtas |

## 8. Logical Determination

VAK_1.09 defined rūpa broadly. VAK_1.10 now begins the inner analysis of the five object-domains:

```text
object-domain
    ↓
internal modal differentiation
```

The important distinction is:

```text
rūpa as aggregate category
    ≠
rūpa as visible object-domain
```

## 9. Interpretive Note

The verse begins the granular analysis of the sensory field. This is not empirical listing for its own sake. It shows that every object-domain is already internally articulated.

The tangible will become especially important because VAK_1.35 later says **spraṣṭavyaṃ dvividham**: the tangible contains both the great elements and derivative tangible qualities.

Organon note:

```text
object-domain
    is not flat objecthood

object-domain
    is articulated modal structure
```

This prepares the later movement from object-domain to material constitution.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_10
    a vak:Karika ;
    rdfs:label "VAK 1.10" ;
    vak:hasSourceLabel "VAkK_1.10" ;
    vak:hasProjectLabel "VAkK_1.10" ;
    vak:hasTopic vak:ObjectDomainDifferentiation ;
    vak:belongsTo vak:Dhatunirdesa .

vak:VisibleFormDomain vak:hasModeCount 20 .
vak:SoundDomain vak:hasModeCount 8 .
vak:TasteDomain vak:hasModeCount 6 .
vak:SmellDomain vak:hasModeCount 4 .
vak:TangibleDomain vak:hasModeCount 11 .
```

## 11. Commit History

- Added expanded Organon analysis for VAK_1.10.
- Preserves padded lexical filename; verse label remains `1.10`, already two-digit.
- Distinguishes rūpa as visible object-domain from rūpa as aggregate category.
- Establishes the modal differentiation of the five material object-domains.
