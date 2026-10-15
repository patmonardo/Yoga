# VAK_2.21 — The Greatest Number

## 1. Sanskrit (Devanāgarī)

> बहुभिर्युक्त एकान्नविंशत्यामलवर्जितैः ।
>
> द्विलिङ्ग आर्यो रागी एकलिङ्गद्वयामलवर्जितैः ॥ २.२१ ॥

## 2. Sanskrit (IAST)

> bahubhir yukta ekānnaviṃśatyāmalavarjitaiḥ /
>
> dviliṅga āryo rāgī ekaliṅgadvayāmalavarjitaiḥ // 2.21 //

Dviliṅga completes the first case. It does not qualify ārya. The second case begins at āryo rāgī.

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
both sex faculties, otherwise complete
    → exclude the three
    = 19

noble trainee, not free from attachment
    → exclude one sex faculty
    → exclude one who has known, and one of the other two
    = 19
```

Same count. Different exclusions. Complete does not mean all twenty-two.

## 5. Translation

### Literal Translation

Endowed with the greatest number, nineteen, excluding the stainless: one possessing both sex faculties. A noble person still possessing attachment, excluding one sex faculty and two stainless faculties.

### Bhāṣya-informed study translation

With how many is one endowed who possesses the greatest number? Nineteen, excluding the stainless: excluding the three uncontaminated faculties. Who? One possessing both sex faculties, whose faculties are complete.

Who else? A noble person still possessing attachment. A trainee not yet free from attachment is also endowed with nineteen, excluding one sex characteristic and two uncontaminated faculties: the faculty of one who has known, and either one of the other two. The detailed differentiation of the faculties, entered in connection with the differentiation of the principles, has been stated.

## 6. Philosophical Translation

Nineteen is the upper bound, and it is two subjects. The worldly maximum has both sex faculties and no realization-faculty. The trainee has one sex faculty and one realization-faculty, the one appropriate to the stage. One who has known is excluded in either trainee case. Equal count is not equal path-status. The maximum is not the completion of training.

Organon rendering:

The floor was two eights. The ceiling is two nineteens. Neither is the telos. Prāpti is still the look-ahead, the entry the count does not make. Not the verse English.

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
