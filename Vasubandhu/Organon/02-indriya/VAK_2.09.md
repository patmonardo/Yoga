# VAK_2.09 — Nine as Three, and the Partition

## 1. Sanskrit (Devanāgarī)

> दृग्भावनाशैक्षपथे नव त्रीणि अमलं त्रयम् ।
>
> रूपीणि जीवितं दुःखे सास्रवाणि द्विधा नव ॥ २.९ ॥

## 2. Sanskrit (IAST)

> dṛgbhāvanāśaikṣapathe nava trīṇi amalaṃ trayam /
>
> rūpīṇi jīvitaṃ duḥkhe sāsravāṇi dvidhā nava // 2.9 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| dṛk-bhāvanā-aśaikṣa-pathe | locative | on the paths of seeing, cultivation, and no-more-training |
| nava | nominative | nine |
| trīṇi | nominative | three |
| amalam trayam | nominative | the triad is stainless |
| rūpīṇi | nominative | those possessing form |
| jīvitam | nominative | life |
| duḥkhe | nominative dual | the two painful faculties |
| sāsravāṇi | nominative | with outflows |
| dvidhā nava | nominative | nine are twofold |

Duḥkhe is dual, not locative. Pain and distress.

## 4. Grammar

```text
% start S
S[NAME=?n, PATH=?p] -> Nine[PATH=?p]
Nine[PATH=seeing] -> 'I shall know'
Nine[PATH=cultivation] -> 'knowledge-faculty'
Nine[PATH=no-more-training] -> 'one who has known'
S[OUTFLOW=without] -> Triad
S[OUTFLOW=with] -> Form | Life | Painful
```

Path names the nine. Outflow status is a separate feature.

## 5. Translation

### Literal Translation

On the paths of seeing, cultivation, and no-more-training, the nine are the three. The triad is stainless. Those possessing form, life, and the two painful faculties are with outflows. Nine are twofold.

### Bhāṣya-informed study translation

> The three are not three further items. They are the same nine, named by the path-task. The triad is stainless. Those possessing form, life, and the two painful faculties are with outflows. Nine, as types, can be either.

## 6. Philosophical Translation

> A name does not settle the instance. The nine remain twofold.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| darśana-mārga | path of seeing | knowing what had not been known |
| bhāvanā-mārga | path of cultivation | the same knowing, against remaining anuśaya |
| aśaikṣa-mārga | path of no-more-training | it has been known |
| amala | stainless | glossed anāsrava; not Pure |
| sāsrava | with outflows | the ten, and the nine in one way |
| anāsrava | without outflows | the triad; not causally inert |
| dvidhā | twofold | either, not both at once |
| rūpin | possessing form | seven, in the form aggregate |
| duḥkhe | pain and distress | dual |
| kṣaya-jñāna | knowledge of exhaustion | |
| anutpāda-jñāna | knowledge of non-arising | |

## 8. Logical Determination

```text
nine
    = mind, pleasure, gladness, neutral feeling,
      faith, vigor, mindfulness, concentration, Discrimination

seeing
    → I shall know
cultivation
    → knowledge-faculty
no-more-training
    → one who has known

triad
    → exclusively without outflows
seven of form, life, pain, distress
    → exclusively with outflows
nine
    → either

3 + 10 + 9 = 22

nine twofold
    ↛ triad partly with outflows
five beginning with faith
    ↛ exclusively without outflows
```

Nine types are not nine factors co-present in every path-event.

## 9. Interpretive Note

The chapter has named the twenty-two and defined the feelings. This verse qualifies them by path and by outflow.

Nothing unprecedented to know is the path-task, not omniscience. Suffering fully known is not the loss of the power to cognize it again.

Twofold is either status across instances, not both in one instance. With outflows is not unwholesome, and not the arhat's bodily feeling denied. Conditioned and unconditioned are not this classification.

Some restrict the five. The first reply limits the citation to the faculties without outflows. The alternative limits it to the outsider whose wholesome roots are severed. Or marks an alternative, not a second step that must be joined. The Wheel not yet turned, and the fivefold examination, are the positive grounds. The last quotation is abbreviated in the Sanskrit. It is not completed from elsewhere.

Organon reading: nine jewels, three names, one stainless configuration. The principles remain deposited. Pure is not amala. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_09
    a vak:Karika ;
    rdfs:label "VAK 2.09" ;
    vak:hasTopic vak:NineAsThree ;
    vak:belongsTo vak:Indriyanirdesa .

vak:NineFaculties vak:namedOn vak:PathOfSeeing, vak:PathOfCultivation, vak:PathOfNoMoreTraining .
vak:Triad vak:stainless true .
vak:SevenOfForm vak:withOutflows true .
vak:NineFaculties vak:twofold true .

organon:PathConfiguration
    organon:notPure true ;
    organon:notTheVerseEnglish true .
```
