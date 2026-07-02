# VAK_1.09

## 1. Sanskrit (Devanāgarī)

> रूपं पञ्चेन्द्रियाण्यर्थाः पञ्चाविज्ञप्तिरेव च ।
>
> तद्विज्ञानाश्रया रूपप्रसादाश्चक्षुरादयः ॥ १.०९ ॥

## 2. Sanskrit (IAST)

> rūpaṃ pañcendriyāṇy arthāḥ pañcāvijñaptir eva ca /
>
> tadvijñānāśrayā rūpaprasādāś cakṣurādayaḥ // VAkK_1.09 //

Source label in GRETIL: `VAkK_1.9`. Project-normalized label: `VAkK_1.09`.

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| rūpam | rūpam | form / form-bearing materiality |
| pañca-indriyāṇi | pañca indriyāṇi | five faculties |
| arthāḥ pañca | arthāḥ pañca | five objects / meanings |
| avijñaptiḥ eva ca | avijñaptiḥ eva ca | and avijñapti also |
| tad-vijñāna-āśrayāḥ | tad-vijñāna-āśrayāḥ | supports of their knowledge |
| rūpa-prasādāḥ | rūpa-prasādāḥ | clear/refined material forms |
| cakṣus-ādayaḥ | cakṣus-ādayaḥ | eye and the others |

## 4. Grammar

The first half defines **rūpa** as:

```text
five faculties
five objects
avijñapti
```

The second half defines the faculties beginning with eye as **rūpa-prasāda**, clear material supports for their corresponding knowledges.

## 5. Literal Translation

> Rūpa is the five faculties, the five objects, and avijñapti also. Eye and the others are clear material forms, supports of the corresponding knowledge.

## 6. Philosophical Translation

> Form includes the five sensory faculties, the five object-domains, and avijñapti. The faculties beginning with the eye are refined material supports for their respective knowledge-domains.

Organon rendering:

> Rūpa is not merely visible shape. It is the material side of disclosure: faculty, object, and subtle form. The sensory faculty is a clear material support through which knowledge becomes possible.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| rūpa | form / form-bearing materiality | broader than visible form |
| indriya | faculty | sensory power/support |
| artha | meaning / object-domain | object side of sensory disclosure |
| avijñapti | avijñapti / non-disclosive form | subtle form; developed at VAK_1.11 |
| vijñāna | knowledge | project rendering, not consciousness |
| āśraya | support | basis for knowledge |
| rūpa-prasāda | clear material form | subtle faculty-basis |

## 8. Logical Determination

```text
rūpa
    = five faculties
    + five object-domains
    + avijñapti
```

The faculties are:

```text
rūpa-prasāda
    → āśraya of vijñāna
```

Thus rūpa includes both the support-side and object-side of sensory knowing.

## 9. Interpretive Note

This verse is a first theory of embodied knowing. The faculty is not merely a gross organ. It is refined material support. The object is not merely external stuff. It is artha, the object/meaning side of disclosure. Avijñapti introduces a subtle form that does not appear in the ordinary way.

Organon note:

```text
faculty
    = material support of knowing

object-domain
    = artha of sensory disclosure

avijñapti
    = subtle form reserved for deeper analysis
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_09
    a vak:Karika ;
    rdfs:label "VAK 1.09" ;
    vak:hasSourceLabel "VAkK_1.9" ;
    vak:hasProjectLabel "VAkK_1.09" ;
    vak:hasTopic vak:DefinitionOfRupa ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Rupa
    rdfs:label "rūpa" ;
    vak:includes vak:FiveFaculties , vak:FiveObjectDomains , vak:Avijnapti .
```

## 11. Commit History

- Added expanded Organon analysis for VAK_1.09.
- Normalized project verse numbering to padded lexical form.
- Defines rūpa as five faculties, five object-domains, and avijñapti.
- Defines eye and the other faculties as refined material supports of knowledge.
