# VAK_2.05 — As Far As That

## 1. Sanskrit (Devanāgarī)

```sanskrit
चित्ताश्रयस्तद्विकल्पः स्थितिः संक्लेश एव च ।
संभारो व्यवदानं च यावता तावदिन्द्रियम् ॥ २.५ ॥
```

## 2. Sanskrit (IAST)

```text
cittāśrayas tadvikalpaḥ sthitiḥ saṃkleśa eva ca /
saṃbhāro vyavadānaṃ ca yāvatā tāvad indriyam // 2.5 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| citta-āśrayaḥ | nominative | support of mind |
| tad-vikalpaḥ | nominative | its differentiation |
| sthitiḥ | nominative | persistence |
| saṃkleśaḥ eva | nominative | defilement |
| saṃbhāraḥ | nominative | equipment |
| vyavadānam | nominative | purification |
| yāvatā tāvat | correlative | as far as that, so far |
| indriyam | nominative | faculty |

Vikalpa here is female and male differentiation of the living basis. It is not concept, and it is not imagination.

## 4. Grammar

```text
% start S
S[TYPE=faculty] -> Function[SIX=true]
Function[SIX=true] -> Support | Differentiation | Persistence | Defilement | Equipment | Purification
```

Only the six functions carry `SIX=true`. Anything outside fails to unify.

## 5. Translation

### Literal Translation

> Support of mind, its differentiation, persistence, and defilement;
> equipment and purification: as far as that, so far faculty.

### Bhāṣya-informed study translation

> The support of consciousness, its differentiation and persistence, its
> defilement, equipment, and purification: as far as these extend, so far
> extends Faculty.

## 6. Philosophical Translation

> The six functions define the membership. Nothing outside them is faculty.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| citta-āśraya | support of mind | the six |
| ṣaḍāyatana | sixfold āyatana | fundamental constitution of a living being |
| maulaṃ sattva-dravya | fundamental constitution | the commentary's phrase; not a substance thesis |
| tad-vikalpa | its differentiation | female and male; not concept |
| saṃbhāra | equipment | the five; provision, not inert |
| vyavadāna | purification | the three |
| yāvatā tāvat | as far as that, so far | the membership limit |
| upasaṃkhyāna | supplementary inclusion | what is refused |
| avidyā | ignorance | governs; not a faculty here |
| vāk, pāṇi, pāda, pāyu, upastha | speech, hand, foot, anus, genital organ | proposed; excluded |

## 8. Logical Determination

```text
governing efficacy
    ↛ faculty in this enumeration

faculty here
    ↔ assigned to one of the six

six
    → support of mind
female, male
    → differentiation
life
    → persistence
five feelings
    → defilement
five beginning with faith
    → provision for purification
three
    → purification

ignorance, speech, hand, foot, anus, genital organ
    → govern
    ↛ counted
```

Six plus two plus one plus five plus five plus three. The genital organ proposed for pleasure is not the female and male faculties of 2.02. The relation differs.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): Faculty is the support of mind, its differentiation,
its persistence, and its defilement, together with its equipment and its
purification: as far as these extend, so far is faculty. The six faculties
are the support of mind; their differentiation is through the female and
male faculties, their persistence through life, their defilement through
the feelings, the provision for purification through the five, and
purification through the three. Ignorance and the rest, and speech and the
other action-organs, are therefore not counted.

2.01 gave the predicate. 2.02 narrowed it to apprehension. 2.03 and 2.04 filled defilement and purification. This verse stops the count.

The objector is right that ignorance governs formations, and that speech and the four govern their acts. The reply does not deny that. Iha bounds the enumeration. Sāṃkhya counts action-faculties of this kind. This passage does not name Sāṃkhya. The designs differ. The twenty-two are not a fuller list of those faculties.

The five are provision. They are not inert: 2.03 already has them check and draw the path. The three are purification itself. 2.04 already split them into seeing, cultivation, and one who has known. No chronology in which the five stop before the three begin.

Organon reading: membership is the discriminator. The six rules define the path. The victim traverses that path and not the powers left outside it. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_05
    a vak:Karika ;
    rdfs:label "VAK 2.05" ;
    vak:hasTopic vak:MembershipLimit ;
    vak:belongsTo vak:Indriyanirdesa .

vak:Indriya vak:requires vak:AssignedFunction .
vak:AssignedFunction vak:hasMembers vak:MindSupport,
    vak:Differentiation, vak:Persistence, vak:Defilement,
    vak:Provision, vak:Purification .
vak:Ignorance vak:notIncludedIn vak:TwentyTwoIndriyas .
vak:Speech vak:notIncludedIn vak:TwentyTwoIndriyas .

organon:MembershipDiscriminator
    organon:bounds vak:TwentyTwoIndriyas ;
    organon:notTheVerseEnglish true .
```
