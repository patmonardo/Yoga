# VAK_1.10 — Counts Within the Five Meanings

## 1. Sanskrit (Devanāgarī)

> रूपं द्विधा विंशतिधा शब्दस्त्वष्टविधः रसः ।
>
> षोढा चतुर्विधो गन्धः स्पृश्यमेकादशात्मकम् ॥ १.१० ॥

## 2. Sanskrit (IAST)

> rūpaṃ dvidhā viṃśatidhā śabdas tv aṣṭavidhaḥ rasaḥ /
>
> ṣoḍhā caturvidho gandhaḥ spṛśyam ekādaśātmakam // 1.10 //

## 3. Lexical Analysis

```text
rūpam | dvidhā | viṃśati-dhā | śabdaḥ | tu | aṣṭa-vidhaḥ | rasaḥ |
ṣoḍhā | catur-vidhaḥ | gandhaḥ | spṛśyam | ekādaśa-ātmakam
```

| Form | Morphology | Force in this passage |
|---|---|---|
| rūpam | nominative neuter singular | visible Form, one of the five meanings |
| dvidhā | adverb | twofold |
| viṃśatidhā | adverb | twentyfold |
| śabdaḥ | nominative masculine singular | sound |
| tu | particle | contrastive transition |
| aṣṭavidhaḥ | nominative masculine singular | eightfold; agrees with sound |
| rasaḥ | nominative masculine singular | taste |
| ṣoḍhā | adverb | sixfold |
| gandhaḥ | nominative masculine singular | odor |
| caturvidhaḥ | nominative masculine singular | fourfold; agrees with odor |
| spṛśyam | nominative neuter singular | the tangible |
| ekādaśātmakam | nominative neuter singular compound | having eleven as its nature |

Here *rūpa* means visible Form, one meaning named in 1.09, not the Form
Base (*rūpa-skandha*). The verse counts within the five meanings.

## 4. Grammar

```text
visible Form     twofold and twentyfold
sound            eightfold
taste            sixfold
odor             fourfold
tangible         eleven in nature
```

The twentyfold count further enumerates the same visible-Form meaning; it
does not add another meaning or Form Base. The Bhāṣya explains the relation
between the twofold and twentyfold descriptions.

## 5. Translation

### Close syntactic construe

> Visible Form is twofold and twentyfold. Sound, however, is eightfold.
> Taste is sixfold. Odor is fourfold. The tangible has eleven as its nature.

### Bhāṣya-informed translation

> Visible Form is twofold as color and configuration, and that same meaning
> is enumerated as twentyfold. Sound is eightfold. Taste is sixfold. Odor
> is fourfold. The tangible has eleven as its nature: the four Great
> Elements and seven further tangibles.

The verse gives the counts. The Bhāṣya goes on to examine whether sensory
Principles arise from one or many substances and how their Conditions
retain particular character.

## 6. Philosophical Translation

Verse 1.09 named five meanings within the Form Base; 1.10 determines the
counts within those meanings. Visible Form remains one meaning under two
determinations—color and configuration—and the twentyfold enumeration
further specifies it. These numbers do not form a second Base.

This is the meaning-side of the Form Base, not the whole Dharma System.
The Kārikā does not name Essence (*āyatana*) or Principle (*dhātu*). The
Bhāṣya calls visible Form *rūpāyatana*, bringing in its Essence
determination, and later discusses the Conditions for the sensory
Principles. These relations enrich the analysis without changing the
Kārikā's count.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| rūpa | visible Form | one of the five meanings, not the Form Base |
| dvidhā | twofold | color and configuration |
| viṃśatidhā | twentyfold | enumeration of that same visible-Form meaning |
| varṇa | color | the four color determinations given in the Bhāṣya |
| saṃsthāna | configuration | the eight configurations given in the Bhāṣya |
| śabda | sound | eightfold in the verse |
| rasa | taste | sixfold |
| gandha | odor | fourfold in the verse; the treatise gives three |
| spṛśya | tangible | eleven in nature |
| viṣaya | Condition | the Bhāṣya's term for the sensory determinations |
| ālambana | object | term used in the Bhāṣya's objection about one or many |
| vid | know / be known | in the Bhāṣya, knowing rather than existence |
| vijñāna | Principle | the sensory Principle discussed in the prose |
| āyatana | Essence | named in the Bhāṣya as *rūpāyatana* |
| dhātu | Principle | not named in the Kārikā |

## 8. Logical Determination

```text
1.09  five meanings named within the Form Base
1.10  counts determined within those meanings

visible Form
    = color + configuration
    = twofold
    → enumerated as twentyfold

sound      eight
taste      six
odor       four in the verse; three in the treatise
tangible   eleven in nature

counts within meanings
    ↛ a second Form Base
```

## 9. Interpretive Note

The hinge is the Bhāṣya's distinction between being and being known:
one substance may be known under both color and configuration without
becoming two substances. A Kantian-transcendental framing asks what makes
that one appearance determinable in both ways. This is a project-level
comparison, not a claim that Vasubandhu is using Kant's framework.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_10 a vak:Karika ;
    vak:hasTopic vak:CountsWithinMeanings ;
    vak:belongsTo vak:Dhatunirdesa .

vak:VisibleFormMeaning
    vak:hasDetermination vak:Color, vak:Configuration ;
    vak:hasEnumerationCount 20 .

vak:Sound vak:hasEnumerationCount 8 .
vak:Taste vak:hasEnumerationCount 6 .
vak:Odor vak:hasVerseCount 4 ;
    vak:hasTreatiseCount 3 .
vak:Tangible vak:hasNatureCount 11 .
```
