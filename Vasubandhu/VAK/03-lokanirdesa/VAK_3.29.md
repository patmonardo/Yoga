# VAK_3b — VAkK_3.29

## Sanskrit — Devanāgarī

संयोजनादिवचनात् कुप्रज्ञा चेन्न दर्शनात् ।
दृष्टेस्तत्संप्रयुक्तत्वात् प्रज्ञोपक्लेशदेशनात् ॥ VAkK_3.29 ॥

## Sanskrit — IAST

saṃyojanādivacanāt kuprajñā cenna darśanāt /
dṛṣṭes tatsaṃprayuktatvāt prajñopakleśadeśanāt // VAkK_3.29 //

## Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| saṃyojanādivacanāt | saṃyojana-ādi-vacanāt | because of the statement of fetter, etc. |
| kuprajñā | ku-prajñā | bad / false / faulty principle-knowing |
| cet | cet | if |
| na | na | not |
| darśanāt | darśanāt | because of seeing / view / doctrinal seeing |
| dṛṣṭeḥ | dṛṣṭeḥ | of view |
| tatsaṃprayuktatvāt | tat-saṃprayuktatvāt | because of being associated with that |
| prajñopakleśadeśanāt | prajñā-upakleśa-deśanāt | because of the teaching of defilement of prajñā |

## Grammar

```text
saṃyojana-ādi-vacanāt
    ablative singular
    = because of the statement of saṃyojana and so forth

ku-prajñā cet
    = if it is faulty prajñā

na darśanāt
    = no, because of darśana / seeing / view

dṛṣṭeḥ tat-saṃprayuktatvāt
    = because view is associated with that

prajñā-upakleśa-deśanāt
    = because there is a teaching of the defilement of prajñā
```

## Literal Translation

Because of the statement of fetter and so forth — if it is faulty prajñā, no, because of seeing. Because view is associated with that, and because of the teaching of defilement of prajñā.

## Philosophical Translation

One might object that ignorance is simply faulty prajñā, since it is spoken of among fetters and related afflictions. But this is not adequate. It is distinguished by reference to view: views are associated with it, and the tradition teaches the defilement of prajñā. Therefore avidyā is not reducible to prajñā itself, even as faulty prajñā; it is a distinct defiling condition related to prajñā.

## Technical Vocabulary

| Sanskrit | Working translation | Note |
|---|---|---|
| saṃyojana | fetter | Bondage-factor; one of the afflictive classifications |
| vacana | statement / teaching | Doctrinal statement or scriptural usage |
| ku-prajñā | faulty prajñā | The rejected reduction of avidyā to bad prajñā |
| prajñā | principle-knowing / discriminative knowing | Kept as project term; not simply intellect |
| darśana | seeing / view | Can mean vision, view, or doctrinal seeing |
| dṛṣṭi | view | A cognitive-afflictive position associated with avidyā |
| saṃprayukta | associated / conjoined | Technical relation of accompanying mental factors |
| upakleśa | secondary defilement / contamination | Defilement affecting prajñā |
| deśanā | teaching | Doctrinal teaching / exposition |

## Doctrinal Determination

VAkK_3.28 established that avidyā is a dharma opposed to vidyā, not a mere absence.

VAkK_3.29 now rejects a second reduction:

```text
avidyā
    is not merely ku-prajñā
    not merely bad prajñā
```

The reasoning is technical:

```text
If avidyā were simply bad prajñā,
    then it would collapse into prajñā under a negative quality.

But dṛṣṭi / view is associated with it,
    and prajñā itself can be defiled.

Therefore avidyā must be treated as a distinct associated defiling dharma.
```

## Logical Determination

This verse continues the logic of systemic meaning.

In a dictionary, avidyā may appear as:

```text
avidyā = non-knowledge / ignorance
```

But in the system, that is insufficient.

VAkK_3.28 rejected:

```text
avidyā = mere absence of knowledge
```

VAkK_3.29 rejects:

```text
avidyā = bad prajñā
```

The proper determination is relational and systemic:

```text
avidyā
    = distinct opposed dharma
    = associated with view
    = condition of defilement in relation to prajñā
```

So meaning emerges only in the doctrinal system:

```text
vidyā
    gives the positive pole

avidyā
    is not mere lack of that pole
    and not simply defective prajñā

avidyā
    is a determinate opposing condition
    whose role appears through its relations
```

## Interpretive Note

This verse is exactly where dictionary meaning gives way to encyclopedic or systematic meaning.

The word `avidyā` cannot be understood by prefix-analysis alone. Nor can it be understood by translating it as bad knowledge. Its meaning emerges through its position in the Abhidharma system:

```text
relation to vidyā
relation to prajñā
relation to dṛṣṭi
relation to saṃyojana
relation to upakleśa
```

Thus avidyā is a node in a doctrinal network, not a lexical item alone.

## Organon Interpretation

Speculatively, VAkK_3.29 gives a rule for semantic modeling.

```text
Dictionary meaning
    = isolated lexical gloss

Systematic meaning
    = role in a structured field of relations
```

In Organon terms:

```text
Term
    becomes concept
        only inside a system of determinate relations
```

Avidyā is not a raw token. It is a determinate functional node:

```text
opposes vidyā
is not reducible to prajñā
is associated with dṛṣṭi
conditions defilement
functions as first limb of dependent co-arising
```

This is why the wheel reproduces itself: the first condition is not a lexical negative, but a systematic operative determination.

## OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_29
    a vak:Karika ;
    rdfs:label "VAkK 3.29" ;
    vak:continues vak:VAK_3_28 ;
    vak:hasTopic vak:Avidya ;
    vak:rejectsReduction vak:AvidyaAsMereKuPrajna ;
    vak:statesRelation vak:AvidyaViewAssociation ;
    vak:statesRelation vak:PrajnaDefilementTeaching .

vak:AvidyaAsMereKuPrajna
    a logic:RejectedReduction ;
    rdfs:label "avidyā as merely faulty prajñā" ;
    rdfs:comment "VAkK 3.29 rejects reducing avidyā to ku-prajñā." .

vak:AvidyaViewAssociation
    a logic:AssociationRelation ;
    rdfs:label "association of avidyā with dṛṣṭi" ;
    vak:hasSanskrit "dṛṣṭes tatsaṃprayuktatvāt" .

vak:PrajnaDefilementTeaching
    a logic:DoctrinalStatement ;
    rdfs:label "teaching of defilement of prajñā" ;
    vak:hasSanskrit "prajñopakleśadeśanāt" .

vak:Avidya
    logic:opposes vak:Vidya ;
    logic:notIdenticalTo vak:Prajna ;
    logic:associatedWith vak:Drsti .
```

## Commit Note

Committed VAK_3b / VAkK_3.29.

Established:
- avidyā is not mere absence of vidyā.
- avidyā is also not reducible to ku-prajñā, faulty prajñā.
- avidyā is related to dṛṣṭi and to the defilement of prajñā.
- its meaning emerges systematically through relation to vidyā, prajñā, dṛṣṭi, saṃyojana, and upakleśa.

Logical determination:
VAkK_3.29 continues the systemic analysis of avidyā. It rejects a reduction to faulty prajñā and shows that avidyā is a distinct opposing dharma whose meaning arises only in the doctrinal network.
