# VAK_2.13 — To Be Abandoned, and Not

## 1. Sanskrit (Devanāgarī)

> मनोवित्तित्रयं त्रेधा द्विहेया दुर्मनस्कता ।
>
> नव भावनया पञ्च त्वहेयान्यपि न त्रयम् ॥ २.१३ ॥

## 2. Sanskrit (IAST)

> manovittitrayaṃ tredhā dviheyā durmanaskatā /
>
> nava bhāvanayā pañca tv aheyāny api na trayam // 2.13 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| manaḥ-vitti-trayam | nominative | mind and a triad of feelings |
| tredhā | indeclinable | in three ways |
| dvi-heyā | nominative | to be abandoned in two ways |
| durmanaskatā | nominative | distress |
| nava | nominative | nine |
| bhāvanayā | instrumental | by cultivation |
| pañca tu | nominative | the five, however |
| aheyāni api | nominative | also not to be abandoned |
| na trayam | nominative | the triad is not |

Manovittitrayam is four faculties. The three feelings are pleasure, gladness, and neutral feeling. Pain is not in that triad.

## 4. Grammar

```text
mind, pleasure, gladness, neutral feeling
    → by seeing, by cultivation, or not to be abandoned

distress
    → by seeing or by cultivation
    never not-to-be-abandoned

nine, to be abandoned continues
    → by cultivation only
    seven of form, life, pain

five
    → by cultivation, and also not to be abandoned
    with outflows, or without

triad
    → not to be abandoned
    faultless is not fit
```

Api adds a class. It does not put both statuses on one instance.

## 5. Translation

### Literal Translation

Mind and the triad of feelings are threefold. Distress is to be abandoned in two ways. Nine by cultivation. The five, however, also not to be abandoned. Not the triad.

### Bhāṣya-informed study translation

How many are to be abandoned by seeing, how many by cultivation, how many not to be abandoned? Mind and the three feelings are threefold. Which three? Pleasure, gladness, and neutral feeling. Distress is to be abandoned in two ways, by seeing and by cultivation. Nine by cultivation: to be abandoned continues. Those beginning with the eye, life as the eighth, and the pain-faculty, are to be abandoned only by cultivation. The five beginning with faith are to be abandoned by cultivation, and also not to be abandoned, because they can be with outflows or without. The three beginning with “I shall know” are not to be abandoned at all, because they are without outflows. What is faultless is not fit to be abandoned. The distinctions of kind have been explained.

## 6. Philosophical Translation

Abandonment falls on the qualified instance, not on the faculty-name. Mind and three feelings can be abandoned by seeing, by cultivation, or kept. Distress has no faultless remainder. The seven of form, life, and pain are cultivation only. Seeing does not erase them. The five split by outflow. The triad is never abandoned. Faultless is not fit.

Organon rendering:

Citta supports. The caitta-instance is what the path abandons or keeps. A faulted faith is not the faculty deleted. A faultless realization is not discarded after use. The agent traverses by this rule. Not the verse English.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| darśana-prahātavya | to be abandoned by seeing | |
| bhāvanā-prahātavya | to be abandoned by cultivation | |
| aheya | not to be abandoned | not inert, not permanent |
| vitti-traya | three feelings | pleasure, gladness, neutral feeling |
| durmanaskatā | distress | both ways; never kept |
| jīvitāṣṭama | life as eighth | with pain, the nine |
| nirdoṣa | faultless | the reason the triad is not fit |
| prakāra-bheda | distinctions of kind | closed here |

## 8. Logical Determination

```text
mind, pleasure, gladness, neutral feeling
    = seeing, cultivation, or not
    = 4

distress
    = seeing or cultivation
    = 1

seven of form, life, pain
    = cultivation only
    = 9

five
    = cultivation if with outflows
    = not abandoned if without
    = 5

triad
    = not abandoned
    = 3

4 + 1 + 9 + 5 + 3 = 22

faultless
    → not fit to be abandoned

same type, different outflow
    → may differ in abandonment
```

Threefold here is not the ethical threefold of 2.11. Pain has moved.

## 9. Interpretive Note

This closes the distinctions of kind opened at 2.09: outflow, maturation, ethical quality, realm-connection, abandonment. Acquisition is the next question. It is not another name for this.

Both ways, for distress, distributes instances. One instance is not abandoned twice. Cultivation-abandonable is not unwholesome. The nine include indeterminate faculties. The five are wholesome and still abandonable when with outflows.

The paragraph does not say how the nine are abandoned. It is not an instruction to destroy the body or end life. Ordinary cessation is not this category. Not to be abandoned is not permanence, and not uninterrupted operation.

Organon reading: the path-rule is typed. Keep the faculty. Inspect the instance. Abandon only what is fit. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_13
    a vak:Karika ;
    rdfs:label "VAK 2.13" ;
    vak:hasTopic vak:Abandonment ;
    vak:belongsTo vak:Indriyanirdesa .

vak:DistressFaculty vak:notAbandoned false .
vak:Triad vak:notAbandoned true ;
    vak:because vak:Faultless .
vak:Five vak:splitsBy vak:Outflow .

organon:InstanceNotType
    organon:notTheVerseEnglish true .
```
