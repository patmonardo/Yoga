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
% start S
S[ABANDON=?a] -> Mind | ThreeFeelings
S[ABANDON=seeing|cultivation] -> Distress
S[ABANDON=cultivation] -> Nine
S[ABANDON=cultivation|none] -> Five[OUTFLOW=?o]
S[ABANDON=none] -> Triad[FAULTLESS=true]
```

Abandonment is a feature of the qualified instance.

## 5. Translation

### Literal Translation

Mind and the triad of feelings are threefold. Distress is to be abandoned in two ways. Nine by cultivation. The five, however, also not to be abandoned. Not the triad.

### Bhāṣya-informed study translation

> Mind and the three feelings, pleasure, gladness, and neutral feeling, are threefold: to be abandoned by seeing, by cultivation, or not at all. Distress is to be abandoned in two ways, by seeing and by cultivation. Nine, the eye and the rest with life as the eighth, together with pain, are to be abandoned by cultivation alone. The five beginning with faith are both to be abandoned by cultivation and not to be abandoned, according as they are with or without outflows. The triad is not to be abandoned at all, for what is faultless is not fit to be abandoned.

## 6. Philosophical Translation

> Abandonment falls on the qualified instance, not on the faculty. The five can be either. The triad is faultless and is not abandoned.

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
