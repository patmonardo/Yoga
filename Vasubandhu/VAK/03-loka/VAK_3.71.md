# VAK_3.71 — Deva-World Classification: Desire-Births and Pleasure-Births

## 1. Sanskrit — Devanāgarī

```sanskrit
कामोपपत्तयस्तिस्रः कामदेवाः समानुषाः ।
सुखोपपत्तयस्तिस्रो नव त्रिध्यानभूमयः ॥ VAkK_3.71 ॥
```

## 2. Sanskrit — IAST

```iast
kāmopapattayas tisraḥ kāmadevāḥ samānuṣāḥ /
sukhopapattayas tisro nava tridhyānabhūmayaḥ // VAkK_3.71 //
```

## 3. Source Caution

The source reading is:

```iast
kāmopapattayastistraḥ kāmadevāḥ samānuṣāḥ /
sukhopapattayastistro navatridhyānabhūmayaḥ // VAkK_3.71 //
```

Sandhi has been lightly separated:

```iast
kāma-upapattayaḥ tisraḥ kāma-devāḥ sa-mānuṣāḥ /
sukha-upapattayaḥ tisraḥ nava tri-dhyāna-bhūmayaḥ //
```

`sa-mānuṣāḥ` is provisionally read as “together with humans,” linking human beings with the desire-realm gods in the classification of kāma-births. The exact taxonomy of the three `kāmopapatti` classes and the three `sukhopapatti` classes should be checked against the bhāṣya.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| kāmopapattayaḥ | kāma-upapattayaḥ | births / modes of arising in desire |
| tisraḥ | tisraḥ | three |
| kāmadevāḥ | kāma-devāḥ | desire-realm gods |
| samānuṣāḥ | sa-mānuṣāḥ | together with humans; including humans |
| sukhopapattayaḥ | sukha-upapattayaḥ | births / modes of arising in happiness or pleasure |
| tisraḥ | tisraḥ | three |
| nava | nava | nine |
| tridhyānabhūmayaḥ | tri-dhyāna-bhūmayaḥ | grounds of the three dhyānas |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| kāma-upapattayaḥ | nominative plural feminine | subject: desire-births |
| tisraḥ | nominative plural feminine | number: three |
| kāma-devāḥ | nominative plural masculine | included class: desire gods |
| sa-mānuṣāḥ | nominative plural masculine | together with humans; included class |
| sukha-upapattayaḥ | nominative plural feminine | subject: pleasure/happiness births |
| tisraḥ | nominative plural feminine | number: three |
| nava | numeral | nine |
| tri-dhyāna-bhūmayaḥ | nominative plural feminine | the grounds belonging to the three dhyānas |

## 6. Literal Translation

There are three desire-births: the desire-gods together with humans. There are three pleasure-births: the nine grounds of the three dhyānas.

## 7. Philosophical Translation

The text now classifies births by their dominant mode of experience. In the desire-field there are three desire-births, including humans and the desire-realm gods. In the happiness-field there are three pleasure-births, corresponding to the nine grounds of the three dhyānas.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| kāma | desire | defining register of the desire realm |
| upapatti | birth / arising / mode of rebirth | mode of appearance into a world-field |
| kāmopapatti | desire-birth | rebirth structured by desire-enjoyment |
| kāma-deva | desire-realm god | deva remaining within kāmadhātu |
| mānuṣa | human | human birth included in the desire-field classification |
| sukha | happiness / pleasure | refined experiential register beyond ordinary desire-contact |
| sukhopapatti | pleasure-birth / happiness-birth | rebirth structured by pleasure or happiness |
| dhyāna | dhyāna | meditative absorption and corresponding world-ground |
| bhūmi | ground | level, basis, or world-ground |
| tri-dhyāna-bhūmi | ground of the three dhyānas | the nine grounds distributed across three dhyānas |

## 9. Doctrinal Determination

VAkK_3.69–3.70 described the six desire-enjoying gods and their formed mode of birth. VAkK_3.71 abstracts that material into a classification of births.

```text
kāma-upapatti
    → desire-births
    → humans and desire-realm gods

sukha-upapatti
    → pleasure/happiness-births
    → nine grounds of the three dhyānas
```

This verse is a hinge between kāmadhātu refinement and dhyāna-world classification.

## 10. Logical Determination

The verse introduces birth as a classified mode of world-entry.

```text
upapatti
    = arising into a determinate experiential field

kāma-upapatti
    = arising into desire-field

sukha-upapatti
    = arising into happiness/dhyāna-field
```

The deva-world is therefore not just a place. It is a structured birth-mode determined by the dominant quality of experience.

## 11. Interpretive Note

This is an especially useful verse for the devic Dhyāna Path. The ascent is not merely spatial. It becomes modal: beings arise into different territories according to whether their field is structured by kāma or by sukha.

```text
draṣṭṛ
    observes a territory

upapatti
    determines the territory into which a being arises
```

The movement from `kāma` to `sukha` is higher, but it is still world-entry. It is not yet kaivalya, and still less the return beyond isolated Purusha to Brahman.

## 12. Organon Interpretation

Light contact point:

```text
Birth is the assignment of a being to an experiential territory.
```

This gives a strong Organon reading. The field is not merely populated by beings; beings are sorted by the mode of arising that places them into a determinate territory: desire-field or happiness/dhyāna-field.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_71
    a vak:Karika ;
    rdfs:label "VAK 3.71" ;
    vak:sourceReference "VAkK_3.71" ;
    vak:continues vak:VAK_3_70 ;
    vak:hasTopic vak:KamaUpapatti ;
    vak:hasTopic vak:SukhaUpapatti ;
    vak:belongsTo vak:DevaWorldAscentBlock .

vak:KamaUpapatti
    a logic:BirthMode ;
    rdfs:label "kāma-upapatti" ;
    vak:hasCanonicalTranslation "desire-birth" ;
    vak:includes vak:Humans ;
    vak:includes vak:KamaDevas .

vak:SukhaUpapatti
    a logic:BirthMode ;
    rdfs:label "sukha-upapatti" ;
    vak:hasCanonicalTranslation "pleasure-birth / happiness-birth" ;
    vak:hasGroundCount 9 ;
    vak:associatedWith vak:ThreeDhyanas .

vak:Upapatti
    a logic:WorldEntryMode ;
    rdfs:label "upapatti" ;
    vak:hasCanonicalTranslation "birth / arising into a world-field" .
```

## 14. Commit Note

Committed VAK_3.71 / VAkK_3.71.

Established:
- three desire-births are associated with humans and desire-realm gods.
- three pleasure-births are associated with the nine grounds of the three dhyānas.
- `upapatti` is treated as birth / arising into a determinate experiential territory.
- the verse bridges kāmadhātu deva classification into the dhyāna-world classification.
