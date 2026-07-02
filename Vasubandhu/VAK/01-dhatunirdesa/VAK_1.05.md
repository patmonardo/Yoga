# VAK_1.05

## 1. Sanskrit (Devanāgarī)

> अनास्रवा मार्गसत्यं त्रिविधं चाप्यसंस्कृतम् ।
>
> आकाशं द्वौ निरोधौ च तत्राकाशमनावृतिः ॥ १.०५ ॥

## 2. Sanskrit (IAST)

> anāsravā mārgasatyaṃ trividhaṃ cāpy asaṃskṛtam /
>
> ākāśaṃ dvau nirodhau ca tatrākāśam anāvṛtiḥ // VAkK_1.05 //

Source label in GRETIL: `VAkK_1.5`. Project-normalized label: `VAkK_1.05`.

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| anāsravā | anāsravāḥ | without outflows |
| mārga-satyam | mārga-satyam | the truth of the path |
| trividham | tri-vidham | threefold |
| ca api | ca api | and also |
| asaṃskṛtam | asaṃskṛtam | unconditioned |
| ākāśam | ākāśam | space |
| dvau nirodhau | dvau nirodhau | two cessations |
| ca | ca | and |
| tatra | tatra | there, among these |
| ākāśam | ākāśam | space |
| anāvṛtiḥ | anāvṛtiḥ | non-obstruction, non-covering |

## 4. Grammar

The verse identifies the anāsrava field:

```text
anāsrava
    = mārga-satya
    + threefold asaṃskṛta
```

The three unconditioned dharmas are:

```text
ākāśa
pratisaṃkhyā-nirodha
apratisaṃkhyā-nirodha
```

This verse defines the first of these:

```text
ākāśa = anāvṛti
    space = non-obstruction
```

## 5. Literal Translation

> The anāsrava is the truth of the path and also the threefold unconditioned: space and the two cessations. Among these, space is non-obstruction.

## 6. Philosophical Translation

> The domain free of outflows consists of the path-truth and the three unconditioned dharmas. These unconditioned dharmas are space and two forms of cessation. Space is defined not as a substance but as non-obstruction.

Organon rendering:

> The uncontaminated field is not empty negation. It contains the path as conditioned release and the unconditioned as the non-produced real. Space is not a thing among things; it is non-obstruction, the opened field in which determinations are not blocked.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| anāsrava | without outflows | free from taint-field |
| mārga-satya | truth of the path | conditioned but undefiled |
| asaṃskṛta | unconditioned | not constructed by conditions |
| ākāśa | space | defined as non-obstruction |
| nirodha | cessation | two forms in VAK_1.06 |
| anāvṛti | non-obstruction | absence of covering or blockage |

## 8. Logical Determination

VAK_1.04 distinguished sāsrava and anāsrava. VAK_1.05 now specifies the anāsrava side:

```text
anāsrava
    ↓
path-truth
    +
unconditioned threefold
```

The first unconditioned is not a material container:

```text
ākāśa
    = anāvṛti
    = non-obstruction
```

## 9. Interpretive Note

The verse prevents a crude opposition between conditioned and liberating. The path is conditioned, but it belongs to the anāsrava field. The unconditioned is threefold, and the first member, space, is defined negatively as non-obstruction.

This matters for the whole chapter because the dhātu-system will include both conditioned and unconditioned determinations. The unconditioned is not outside Dharma-analysis; it is part of the Dharma-field.

Organon note:

```text
Path
    = conditioned release-function

Unconditioned
    = non-produced truth-status

Space
    = openness / non-obstruction
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_05
    a vak:Karika ;
    rdfs:label "VAK 1.05" ;
    vak:hasSourceLabel "VAkK_1.5" ;
    vak:hasProjectLabel "VAkK_1.05" ;
    vak:hasTopic vak:AnasravaAndUnconditioned ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Akasha
    a vak:UnconditionedDharma ;
    rdfs:label "space as non-obstruction" ;
    vak:sanskrit "ākāśa" ;
    vak:definedAs vak:Anavrti .
```

## 11. Commit History

- Added expanded Organon analysis for VAK_1.05.
- Normalized project verse numbering to padded lexical form.
- Establishes anāsrava as path-truth plus the three unconditioned dharmas.
- Defines ākāśa as non-obstruction rather than inert spatial substance.
