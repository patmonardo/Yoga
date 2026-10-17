# VAK_2.21 — The Greatest Number

## 1. Sanskrit (Devanāgarī)

```sanskrit
बहुभिर्युक्त एकान्नविंशत्यामलवर्जितैः ।
द्विलिङ्ग आर्यो रागी एकलिङ्गद्वयामलवर्जितैः ॥ २.२१ ॥
```

## 2. Sanskrit (IAST)

```text
bahubhir yukta ekānnaviṃśatyāmalavarjitaiḥ /
dviliṅga āryo rāgī ekaliṅgadvayāmalavarjitaiḥ // 2.21 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| bahubhiḥ | instrumental | with the greatest number |
| yuktaḥ | nominative | endowed with |
| ekānna-viṃśatyā | instrumental | with nineteen |
| amala-varjitaiḥ | instrumental | excluding the stainless |
| dvi-liṅgaḥ | nominative | possessing both sex faculties |
| āryaḥ rāgī | nominative | a noble person still with attachment |
| eka-liṅga-dvaya-amala-varjitaiḥ | instrumental | excluding one sex faculty and two stainless |

Stainless is the three. The running text has a short vowel in the second compound. The prose secures two uncontaminated faculties.

## 4. Grammar

```text
% start S
S[MAX=19, SEX=both] -> Faculty[STAINLESS=false]
S[MAX=19, NOBLE=true, ATTACHMENT=true] -> Faculty[SEX=one, STAINLESS=two-excluded]
```

Nineteen is the maximum that still carries attachment or both sex faculties.
## 5. Translation

### Literal Translation

> Endowed with the greatest number, nineteen, excluding the stainless: one
> possessing both sex faculties. A noble person still possessing attachment,
> excluding one sex faculty and two stainless faculties.

### Bhāṣya-informed study translation

> One is endowed with the greatest number, nineteen, excluding the
> stainless; one possessing both sex faculties. A noble person still
> possessing attachment has nineteen, excluding one sex faculty and two
> stainless faculties.

## 6. Philosophical Translation

> Nineteen is the maximum that still includes attachment or both sexual characteristics. The stainless triad is never co-present with that maximum.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| bahubhiḥ | the greatest number | nineteen |
| amala | stainless | the three; not every wholesome |
| dvi-liṅga | both sex faculties | dvivyañjana; the first case |
| samagra-indriya | complete in faculties | relative to the nineteen |
| ārya rāgin | noble, still with attachment | avītarāga śaikṣa |
| dvayoś cānyatarat | and either of the other two | with one who has known; two exclusions |

## 8. Logical Determination

```text
worldly maximum
    = 22 - 3
    = 19
    stainless intersection empty

trainee maximum
    = 22 - 1 sex - 2 stainless
    = 19
    one stainless possessed
    one who has known excluded

same count
    ≠ same set
complete
    ≠ all twenty-two
greatest number
    ↛ every trainee has exactly nineteen
```

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): The greatest number is nineteen. One possessing both
sex faculties is endowed with nineteen, excluding the stainless triad. A
trainee still possessing attachment is also endowed with nineteen,
excluding one sex faculty and two of the stainless. The maximum is not the
full twenty-two. It is the complete ordinary or still-attached noble
continuum.

The first case reaches nineteen by lacking every realization-faculty. Abundance and absence of noble realization coincide. Both sex characteristics do not by themselves supply the nineteen. Complete is the qualification.

The trainee exclusions are compatibility with a stage, not a deficit measured against the worldly case. Continuing attachment is kept. Noble is not the end of training. Possession is not nineteen faculties in one moment, and not a measure of strength.

Dviliṅga does not join ārya. Who else introduces the second subject. Stainless is uncontaminated, all three in the first case, two named in the second. The conjunction is one who has known and either of the other two, not either completed knowledge or one other.

The close is the differentiation entered with the principles. It does not close the chapter. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_21
    a vak:Karika ;
    rdfs:label "VAK 2.21" ;
    vak:hasTopic vak:MaximumPossession ;
    vak:belongsTo vak:Indriyanirdesa .

vak:WorldlyMaximum vak:hasCount 19 ;
    vak:excludes vak:ThreeStainless .
vak:TraineeMaximum vak:hasCount 19 ;
    vak:hasStainlessCount 1 .

organon:MaximumNotTelos
    organon:notTheVerseEnglish true .
```
