# VAK_2.07

## 1. Sanskrit (Devanāgarī)

> दुःखेन्द्रियमशाता या कायिकी वेदना सुखम् ।
>
> शाता ध्याने तृतीये तु चैतसी सा सुखेन्द्रियम् ॥ २.७ ॥

## 2. Sanskrit (IAST)

> duḥkhendriyam aśātā yā kāyikī vedanā sukham /
>
> śātā dhyāne tṛtīye tu caitasī sā sukhendriyam // 2.7 //

## 3. Padaccheda

```text
duḥkhendriyam     → duḥkha-indriyam
aśātā yā          → aśātā yā
kāyikī vedanā     → kāyikī vedanā
sukham śātā       → sukham śātā
dhyāne tṛtīye     → dhyāne tṛtīye
tu caitasī sā     → tu caitasī sā
sukhendriyam      → sukha-indriyam
```

| Form | Morphology | Lexical force here |
|---|---|---|
| duḥkha-indriyam | nominative neuter singular compound | pain-faculty |
| aśātā | nominative feminine singular | disagreeable or unpleasant; modifies `vedanā` |
| yā | nominative feminine singular relative pronoun | whichever / that which |
| kāyikī | nominative feminine singular adjective | bodily |
| vedanā | nominative feminine singular | feeling |
| sukham | nominative neuter singular | pleasure; predicative designation |
| śātā | nominative feminine singular | agreeable or pleasant; understood with bodily `vedanā` |
| dhyāne | locative neuter singular | in dhyāna |
| tṛtīye | locative neuter singular ordinal | in the third |
| tu | contrastive particle | but / however |
| caitasī | nominative feminine singular adjective | mental; understood with `vedanā` |
| sā | nominative feminine singular pronoun | that same [feeling] |
| sukha-indriyam | nominative neuter singular compound | pleasure-faculty |

The feminine descriptions agree with `vedanā`; the neuter compounds are
predicate designations. The difference in gender does not imply a different
referent:

```text
yā kāyikī vedanā aśātā
    sā duḥkha-indriyam
```

## 4. Grammar

The opening relative construction identifies the pain-faculty:

```text
aśātā yā kāyikī vedanā
    → whichever bodily feeling is disagreeable

[sā] duḥkha-indriyam
    → [that] is the pain-faculty
```

The definition of ordinary pleasure is compressed across the pāda boundary:

```text
sukham śātā [kāyikī vedanā]
    → pleasure is agreeable [bodily feeling]
```

The Bhāṣya supplies the ellipsis explicitly:

```text
sukhendriyaṃ kāyikī śātā vedanā
    → the pleasure-faculty is agreeable bodily feeling
```

The final pāda introduces a locative exception:

```text
dhyāne tṛtīye tu
    → but in the third dhyāna

caitasī sā [vedanā] sukha-indriyam
    → that same [agreeable] feeling, when mental,
      is the pleasure-faculty
```

`Sā` carries forward the agreeable feeling already designated by `śātā`.
The contrast is between its ordinary bodily mode and its mental mode in the
third dhyāna.

## 5. Translation

### Close syntactic construe

> Whichever bodily feeling is disagreeable is the pain-faculty; pleasure is agreeable [bodily feeling]. But in the third dhyāna, that [agreeable feeling], when mental, is the pleasure-faculty.

### Bhāṣya-informed translation

> The pain-faculty is disagreeable bodily feeling—that is, feeling which is injurious. The pleasure-faculty is ordinarily agreeable bodily feeling—that is, feeling which is supportive. In the third dhyāna, however, agreeable mental feeling is classified as the pleasure-faculty, because the five sensory cognition-groups, and therefore bodily feeling, are absent there.

The explanatory terms `upaghātikā` and `anugrāhikā`, together with the reason
from the absence of the five sensory cognition-groups, belong to the Bhāṣya.
They are not additional words in the Kārikā.

## 6. Philosophical Translation

> The Kośa first distinguishes pain and pleasure by affective character and bodily mode: bodily feeling that works against the continuum is pain, while bodily feeling that supports it is pleasure. Yet the pleasure-faculty is not inseparably bound to bodily feeling. At the third dhyāna, where the five sensory cognition-groups are absent, agreeable mental feeling occupies the functional position of pleasure.

Organon rendering:

> A faculty is classified through an organized relation among affective character, mode of feeling, and level of experience. The ordinary rule assigns agreeable bodily feeling to pleasure; the third-dhyāna rule preserves pleasure-faculty identity under a determinate change from bodily to mental mode. The governing function is stable, while its admissible realization varies with the architecture of the experiential level.

This rendering concerns a specific Kośa classification. It does not establish
a general independence of function from embodiment.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| duḥkha-indriya | pain-faculty | disagreeable bodily feeling |
| sukha-indriya | pleasure-faculty | agreeable bodily feeling, with agreeable mental feeling in the third dhyāna as the stated exception |
| vedanā | feeling | affective mode classified here by agreeableness and bodily or mental locus |
| aśātā | disagreeable / unpleasant | Kārikā characterization of bodily feeling counted as pain |
| upaghātikā | injurious / working against | Bhāṣya gloss on `aśātā`; functional rather than moral description |
| śātā | agreeable / pleasant | Kārikā characterization of feeling counted as pleasure |
| anugrāhikā | supportive / beneficial | Bhāṣya gloss on `śātā`; favoring or supporting the continuum |
| kāyikī vedanā | bodily feeling | ordinary mode of both pain-faculty and pleasure-faculty in this verse |
| caitasī vedanā | mental feeling | mode of the pleasure-faculty in the third dhyāna |
| tṛtīya-dhyāna | third dhyāna | meditative level in which the stated mental exception applies |
| pañca-vijñāna-kāya | five sensory cognition-groups | absent in the third dhyāna according to the Bhāṣya |

`Sukha` and `duḥkha` are not unrestricted synonyms for every happiness and
suffering in this passage. They name two of the five feeling-faculties and
are technically distinguished from `saumanasya` and `daurmanasya`, which
VAK 2.08 will define.

## 8. Logical Determination

The ordinary classification uses two coordinates:

```text
AffectiveCharacter
    = {Agreeable, Disagreeable}

FeelingMode
    = {Bodily, Mental}
```

VAK 2.07 gives the following rules:

```text
Feeling(x)
∧ Bodily(x)
∧ Disagreeable(x)
    → FacultyClass(x, DuhkhaIndriya)

Feeling(x)
∧ Bodily(x)
∧ Agreeable(x)
    → FacultyClass(x, SukhaIndriya)
```

The third-dhyāna rule is context-sensitive:

```text
Feeling(x)
∧ Mental(x)
∧ Agreeable(x)
∧ OccursAt(x, ThirdDhyana)
    → FacultyClass(x, SukhaIndriya)
```

The Bhāṣya supplies its ground:

```text
OccursAt(x, ThirdDhyana)
    → Absent(FiveSensoryCognitionGroups)
    → Absent(BodilyFeeling)
```

Therefore bodily mode is an ordinary condition of `sukha-indriya`, not an
exceptionless definition across every meditative level:

```text
SukhaIndriya(x)
    ↛ NecessarilyBodily(x)

Mental(x)
    ↛ SukhaIndriya(x)

Mental(x)
∧ Agreeable(x)
∧ ThirdDhyanaContext(x)
    → SukhaIndriya(x)
```

The exception is narrow. It does not erase the bodily/mental distinction or
license every agreeable mental feeling to be called `sukha-indriya`.

## 9. Interpretive Note

VAK 2.07 begins the detailed definition of the five feeling-faculties that
VAK 2.03 assigned a governing role in defilement and VAK 2.06 assigned to the
experience of `pravṛtti`. The verse now shows how that experiential function
is internally differentiated.

Pain and pleasure are not introduced as free-standing substances or abstract
qualities. Each is a determinate feeling classified by affective character
and mode. The Bhāṣya further interprets disagreeableness as `upaghātikā`,
working against the continuum, and agreeableness as `anugrāhikā`, supporting
it. These glosses give the hedonic distinction a functional force without
turning it into a moral judgment.

The third-dhyāna clause prevents a rigid anatomical definition of pleasure.
Ordinarily, agreeable bodily feeling is `sukha`, while agreeable mental
feeling will be classified as `saumanasya`. At the third dhyāna, however, the
five sensory cognition-groups do not occur, so no bodily feeling is available.
The agreeable mental feeling of that level is nevertheless `sukha-indriya`.

For the Organon, this discloses a context-governed Agent classification:

```text
faculty determination
    = affective character
    + mode of realization
    + experiential level
```

The third-dhyāna result is not an arbitrary exception patched onto the rule.
It is licensed by a change in the available cognitive architecture. The
Kośa Agent must therefore preserve both the default determination and the
ground under which a different realization satisfies the same faculty-role.

This is a project-level inference from the verse and Bhāṣya. The textual
claim remains the narrower one: pleasant mental feeling in the third dhyāna
is the pleasure-faculty because bodily feeling is absent there.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_07
    a vak:Karika ;
    rdfs:label "VAK 2.07" ;
    vak:hasTopic vak:DuhkhaIndriya,
        vak:SukhaIndriya ;
    vak:belongsTo vak:Indriyanirdesa .

vak:DuhkhaIndriya
    a vak:FeelingFaculty ;
    vak:hasAffectiveCharacter vak:Disagreeable ;
    vak:hasFeelingMode vak:Bodily .

vak:SukhaIndriya
    a vak:FeelingFaculty ;
    vak:hasDefaultAffectiveCharacter vak:Agreeable ;
    vak:hasDefaultFeelingMode vak:Bodily ;
    vak:hasContextualRealization vak:ThirdDhyanaSukha .

vak:ThirdDhyanaSukha
    a vak:ContextualFacultyRealization ;
    vak:hasAffectiveCharacter vak:Agreeable ;
    vak:hasFeelingMode vak:Mental ;
    vak:occursAt vak:ThirdDhyana ;
    vak:groundedBy vak:AbsenceOfFiveSensoryCognitionGroups .

vak:Asata
    vak:explainedBy vak:Upaghatika .

vak:Sata
    vak:explainedBy vak:Anugrahika .

organon:ContextGovernedFacultyClassification
    a organon:InterpretiveReconstruction ;
    organon:preserves vak:FacultyIdentity ;
    organon:variesBy vak:FeelingMode,
        vak:ExperientialLevel ;
    organon:inferredFrom vak:ThirdDhyanaSukha .
```
