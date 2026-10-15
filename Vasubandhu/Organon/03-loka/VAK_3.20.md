# VAK_3.20 — Samutpāda Across Three Births

## 1. Sanskrit (Devanāgarī)

> स प्रतीत्यसमुत्पादो द्वादशाङ्गस्त्रिकाण्डकः ।
>
> पूर्वापरान्तयोर्द्वे द्वे मध्येऽष्टौ परिपूरिणः ॥ ३.२० ॥

## 2. Sanskrit (IAST)

> sa pratītyasamutpādo dvādaśāṅgas trikāṇḍakaḥ /
>
> pūrvāparāntayor dve dve madhye 'ṣṭau paripūriṇaḥ // 3.20 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| saḥ | nominative masculine singular pronoun | that; the Bhāṣya supplies the previously described Base-continuum as its antecedent |
| pratītya-samutpādaḥ | nominative masculine singular compound | the named samutpāda, specified by relation and articulated below |
| dvādaśa-aṅgaḥ | nominative masculine singular compound | twelve-membered |
| tri-kāṇḍakaḥ | nominative masculine singular compound | three-sectioned |
| pūrva-apara-antayoḥ | locative dual compound | at the prior and subsequent limits |
| dve dve | distributive numeral | two at each of the two limits |
| madhye | locative singular | in the middle section |
| aṣṭau | cardinal numeral | eight members |
| paripūriṇaḥ | genitive singular of *paripūrin* | for one who completes all the successive states, as the Bhāṣya explains |

## 4. Grammar

The first line predicates the structure of *samutpāda*:

```text
saḥ pratītyasamutpādaḥ
    dvādaśāṅgaḥ
    trikāṇḍakaḥ [asti]
```

> That samutpāda is twelve-membered and three-sectioned.

The second line distributes the members:

```text
pūrvāparāntayoḥ dve dve
madhye aṣṭau paripūriṇaḥ
```

> Two at each of the prior and subsequent limits; eight in the middle for
> one who completes the course.

The kārikā gives the twelve-member, three-section architecture and its
2/8/2 distribution. The Bhāṣya identifies the members and specifies the
three sections as past, future, and present births.

## 5. Translation

### Close syntactic rendering

> That conditioned arising is twelve-membered and three-sectioned: two at
> each of the prior and subsequent limits, and eight in the middle for one
> who completes the course.

### Bhāṣya-informed study translation

> The Base-continuum already described across three births is the
> conditioned arising, articulated in twelve members and three sections:
> two at each of the past and future limits, and eight in the present course
> of one who completes all successive states.

## 6. Philosophical Translation

> The Base-continuum already described across three births is conditioned
> arising, articulated into twelve members and three temporal sections. Two
> members mark the prior limit, eight occupy the present middle of a
> complete course, and two mark the subsequent limit.

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this passage |
|---|---|---|
| `pratītya-samutpāda` | conditioned arising | the twelve-member course under its conditions |
| `dvādaśāṅga` | twelve-membered | the count of members in the arrangement |
| `trikāṇḍaka` | three-sectioned | past, present, and future births, as specified by the Bhāṣya |
| `pūrvāparāntayoḥ` | at the prior and subsequent limits | two members at each temporal boundary |
| `paripūriṇaḥ` | for one who completes the course | limits the complete eight-member middle; the Bhāṣya excludes one who dies in the interval and those in the Form or Formless Realms |
| `vijñāna` | Discriminative Cognition | one of the eight members in the present middle |

## 8. Logical Determination

```text
Past birth — prior limit
    Ignorance
    Formations

Present birth — middle
    Discriminative Cognition
    Name-and-Form
    six Essences
    Contact
    Feeling
    Craving
    Appropriation
    Becoming

Future birth — subsequent limit
    Birth
    Aging-and-Death
```

The kārikā fixes the distribution at 2 / 8 / 2. The Bhāṣya assigns the
three sections and their members, and restricts the complete middle course
to one who encounters all its successive states.

## 9. Interpretive Note

The past, present, and future sections are temporal divisions, not the
three BEP projections. The Bhāṣya's “person” marks the scope of the complete
course, not a separate traveler. It excludes one who dies in the interval
and those in the Form or Formless Realms. The verse names Discriminative
Cognition as one member; the Kośa's wider account of Vijñāna joining and
governing Perception and Conception is not expanded here. Keep it distinct
from consciousness (*citta*) and Mind (*manas*).

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix loka: <http://127.0.0.1:3000/loka#> .

vak:VAK_3_20
    a vak:Karika ;
    vak:hasTopic vak:Samutpada ;
    vak:hasMemberCount 12 ;
    vak:hasSectionCount 3 ;
    vak:hasDistribution "2/8/2" ;
    vak:hasPriorSection vak:PastBirth ;
    vak:hasMiddleSection vak:PresentBirth ;
    vak:hasSubsequentSection vak:FutureBirth ;
    vak:hasScope vak:CompletedMiddleCourse .

vak:Samutpada
    a loka:ThreeSectionArticulation ;
    vak:articulates vak:ThreeBirthBaseContinuum .

vak:PastBirth
    a vak:TemporalSection ;
    vak:hasMemberCount 2 ;
    vak:hasMember vak:Avidya, vak:Samskara .

vak:PresentBirth
    a vak:TemporalSection ;
    vak:hasMemberCount 8 ;
    vak:hasMember vak:Vijnana, vak:Namarupa, vak:SixEssences,
        vak:Sparsa, vak:Vedana, vak:Trsna, vak:Upadana, vak:Bhava .

vak:FutureBirth
    a vak:TemporalSection ;
    vak:hasMemberCount 2 ;
    vak:hasMember vak:Jati, vak:Jaramarana .

vak:CompletedMiddleCourse
    a vak:ScopeCondition ;
    vak:qualifies vak:PresentBirth .
```
