# VAK_2.07 — Pain and Pleasure Faculties

## 1. Sanskrit — Devanāgarī

```text
दुःखेन्द्रियमशाता या कायिकी वेदना सुखम् ।
शाता ध्याने तृतीये तु चैतसी सा सुखेन्द्रियम् ॥ VAkK_2.7 ॥
```

## 2. Sanskrit — IAST

```text
duḥkhendriyam aśātā yā kāyikī vedanā sukham /
śātā dhyāne tṛtīye tu caitasī sā sukhendriyam // VAkK_2.7 //
```

Source form:

```text
duḥkhendriyamaśātā yā kāyikī vedanā sukham /
śātā dhyāne tṛtīye tu caitasī sā sukhendriyam // VAkK_2.7 //
```

## 3. Padaccheda

| Text | Padaccheda | Basic Sense |
|---|---|---|
| duḥkhendriyam | duḥkha-indriyam | the pain faculty |
| aśātā | aśātā | disagreeable / unpleasant |
| yā | yā | which |
| kāyikī | kāyikī | bodily |
| vedanā | vedanā | feeling |
| sukham | sukham | pleasure / ease |
| śātā | śātā | agreeable / pleasant |
| dhyāne tṛtīye | dhyāne tṛtīye | in the third dhyāna |
| tu | tu | but / moreover |
| caitasī | caitasī | mental |
| sā | sā | that |
| sukhendriyam | sukha-indriyam | the pleasure faculty |

## 4. Grammar

```text
aśātā yā kāyikī vedanā
    relative construction
    “that bodily feeling which is disagreeable”

duḥkha-indriyam
    nominative / accusative singular neuter
    “the pain faculty”

śātā ... caitasī
    feminine singular
    “agreeable mental [feeling]”

dhyāne tṛtīye
    locative singular
    “in the third dhyāna”

sā sukha-indriyam
    predicative construction
    “that is the pleasure faculty”
```

## 5. Literal Translation

```text
The pain faculty is that bodily feeling which is disagreeable.
Pleasure is agreeable bodily feeling; but in the third dhyāna,
that agreeable mental feeling is the pleasure faculty.
```

## 6. Philosophical Translation

```text
The pain faculty is defined as unpleasant bodily feeling. The pleasure faculty is
pleasant bodily feeling, except that in the third dhyāna the relevant pleasant feeling
is mental and is still counted as the pleasure faculty.
```

## 7. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| duḥkha-indriya | pain faculty | Unpleasant bodily feeling |
| sukha-indriya | pleasure faculty | Pleasant bodily feeling; special mental case in third dhyāna |
| aśātā | disagreeable / unpleasant | Negative hedonic tone |
| śātā | agreeable / pleasant | Positive hedonic tone |
| kāyikī vedanā | bodily feeling | Feeling associated with the body |
| caitasī vedanā | mental feeling | Feeling associated with mind |
| dhyāna | dhyāna | Meditative absorption; here third dhyāna |
| tṛtīya | third | Marks the special third-dhyāna case |

## 8. Classification Note

VAK_2.07 begins the definition of the five feeling faculties introduced in VAK_2.03.

```text
Five feeling faculties:
    sukha
    duḥkha
    saumanasya
    daurmanasya
    upekṣā
```

This verse defines the first two:

```text
duḥkha-indriya
    =
unpleasant bodily feeling

sukha-indriya
    =
pleasant bodily feeling
    plus the special case of pleasant mental feeling in the third dhyāna
```

The important technical point is that **sukha** and **duḥkha** are not generic happiness and suffering here. They are classified as bodily feeling-faculties, with a meditative exception for the third dhyāna.

## 9. Logical Determination

The feeling faculties are defined by hedonic tone and locus.

```text
hedonic tone:
    pleasant / unpleasant

locus:
    bodily / mental
```

VAK_2.07 gives:

```text
unpleasant + bodily
    -> duḥkha-indriya

pleasant + bodily
    -> sukha-indriya

pleasant + mental + third dhyāna
    -> sukha-indriya
```

The verse therefore begins a subtle classification of affective governing efficacy.

## 10. Transcendental Placement

Feeling is not treated as passive decoration. It is an *indriya*, a governing efficacy.

```text
vedanā
    =
affective registration
    =
valuation of the experiential field
```

The body is not merely empirical matter here. It is the locus of determinate affective registration. The pain and pleasure faculties govern how the lived series is affected as agreeable or disagreeable.

The third-dhyāna exception shows that meditative transformation changes the locus of pleasure without removing its governing efficacy.

## 11. Organon Interpretation

Organon reading:

```text
duḥkha-indriya
    =
unpleasant bodily valuation-driver

sukha-indriya
    =
pleasant bodily valuation-driver
    with a third-dhyāna mental valuation mode
```

This continues the `VAK_2.03` insight:

```text
vedanā governs saṃkleśa
```

But it now refines the structure of feeling:

```text
bodily unpleasantness
bodily pleasantness
meditative mental pleasantness
```

The feeling faculties are therefore affective model-drivers within the Logic of Experience.

## 12. Compact Formula

```text
VAK_2.07 defines duḥkha as unpleasant bodily feeling and sukha as pleasant bodily feeling,
while preserving the special case that pleasant mental feeling in the third dhyāna is also sukha-indriya.
```

## 13. OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_07 a vak:Karika ;
    rdfs:label "VAK 2.07" ;
    vak:sourceVerse "VAkK_2.7" ;
    vak:chapter vak:Indriyanirdesa ;
    vak:hasTopic vak:DuhkhaIndriya, vak:SukhaIndriya ;
    vak:hasKeyTerm vak:KayikiVedana, vak:CaitasiVedana, vak:ThirdDhyana ;
    vak:hasLiteralTranslation
        "The pain faculty is that bodily feeling which is disagreeable. Pleasure is agreeable bodily feeling; but in the third dhyāna, that agreeable mental feeling is the pleasure faculty." ;
    vak:hasPhilosophicalTranslation
        "The pain faculty is defined as unpleasant bodily feeling. The pleasure faculty is pleasant bodily feeling, except that in the third dhyāna the relevant pleasant feeling is mental and is still counted as the pleasure faculty." .

vak:DuhkhaIndriya a vak:Indriya ;
    rdfs:label "duḥkha-indriya" ;
    vak:canonicalTranslation "pain faculty" ;
    vak:logicalFunction "Unpleasant bodily feeling as affective governing efficacy." .

vak:SukhaIndriya a vak:Indriya ;
    rdfs:label "sukha-indriya" ;
    vak:canonicalTranslation "pleasure faculty" ;
    vak:logicalFunction "Pleasant bodily feeling, with third-dhyāna pleasant mental feeling as special case." .
```

## 14. Commit History

```text
VAK_2.07 opened.
Chapter: Indriyanirdeśa.
Method: kārikā-first.
Pain faculty defined as unpleasant bodily feeling.
Pleasure faculty defined as pleasant bodily feeling, with third-dhyāna mental exception.
Technical distinction established: hedonic tone plus bodily/mental locus.
Organon note added: feeling faculties as affective valuation-drivers.
Zero-padded file naming maintained: VAK_2.07.
```
