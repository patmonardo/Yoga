# VAK_4.14

## 1. Sanskrit — Devanāgarī

```sanskrit
अष्टधा प्रातिमोक्षाख्यो द्रव्यतस्तु चतुर्विधः ।
लिङ्गतो नामसंचारात् पृथक् ते चाविरोधिनः ॥
```

## 2. Sanskrit — IAST

```iast
aṣṭadhā prātimokṣākhyo dravyatas tu caturvidhaḥ |
liṅgato nāmasaṃcārāt pṛthak te cāvirodhinaḥ ||
```

## 3. Source reference and caution

Source: `VAkK_4.14`.

The first half is secure: prātimokṣa restraint is eightfold by classification, but fourfold in terms of real type. The compressed second half explains the role of gender or distinguishing mark, transfer of designation, and non-conflict. Its exact syntactic attachment should be checked against the Bhāṣya.

## 4. Padaccheda

```text
aṣṭadhā
prātimokṣa-ākhyaḥ
dravyataḥ
tu
caturvidhaḥ
liṅgataḥ
nāma-saṃcārāt
pṛthak
te
ca
avirodhinaḥ
```

| Form | Analysis | Working meaning |
|---|---|---|
| `aṣṭadhā` | adverb | eightfold |
| `prātimokṣākhyaḥ` | `prātimokṣa-ākhyaḥ` | called prātimokṣa |
| `dravyataḥ` | ablatival adverb | substantially; by real entity |
| `tu` | particle | but |
| `caturvidhaḥ` | adjective | fourfold |
| `liṅgataḥ` | ablatival adverb | according to gender or distinguishing mark |
| `nāmasaṃcārāt` | ablative compound | because of transfer or change of designation |
| `pṛthak` | adverb | separately |
| `te` | nominative plural | those |
| `ca` | particle | and |
| `avirodhinaḥ` | nominative plural | non-conflicting; compatible |

## 5. Grammar

The understood subject is `saṃvaraḥ`: the restraint called prātimokṣa is eightfold. `Dravyatas tu caturvidhaḥ` contrasts named or disciplinary enumeration with substantial differentiation: in terms of real restraint-types, it is fourfold.

`Liṅgato nāmasaṃcārāt` gives the reason for the broader enumeration: distinctions of gender or formal mark and corresponding changes of designation. `Pṛthak te cāvirodhinaḥ` indicates that the separately named forms are not thereby opposed as distinct restraint-substances. The precise referent of `te` remains to be confirmed from the commentary.

## 6. Literal translation

> The restraint called prātimokṣa is eightfold, but substantially it is fourfold. Owing to gender and the transfer of designation, those are separate and non-conflicting.

## 7. Philosophical translation

> Prātimokṣa restraint is divided into eight disciplinary forms, yet these amount to only four distinct kinds of restraint in substance. The broader enumeration results from differences of gender and corresponding changes of designation; separate names do not establish mutually opposed restraint-substances.

## 8. Technical vocabulary

### `dravya`

Here `dravyataḥ` asks how many genuinely distinct restraint-types there are, rather than how many names or statuses are counted. It should not be read through an imported Aristotelian notion of substance.

### `liṅga`

Possible senses include gender, sex, distinguishing sign, or formal characteristic. Gender is likely central in the present disciplinary classification.

### `nāmasaṃcāra`

`Nāman` is name or designation; `saṃcāra` is passage, transfer, or change. A change of disciplinary name does not necessarily imply production of a wholly new restraint-substance.

### `avirodhin`

`A-virodhin` means non-opposed, non-conflicting, or compatible. The exact practical implication should await the Bhāṣya.

## 9. Doctrinal determination

VAK_4.13 identified prātimokṣa as one kind of restraint. VAK_4.14 now analyzes it internally:

```text
prātimokṣa restraint
├── eightfold by disciplinary designation
└── fourfold by substantial type
```

The Kośa therefore distinguishes nominal classification from real dharma classification. A distinct institutional name does not by itself prove a distinct restraint-dharma.

## 10. Logical determination

The verse introduces two levels of division:

```text
external or nominal division
    eightfold

internal or substantial division
    fourfold
```

Thus:

```text
difference of designation
    does not necessarily entail
difference of substance
```

## 11. Relation to the sequence

```text
VAK_4.13
    identifies prātimokṣa restraint

VAK_4.14
    distinguishes its named forms
    from its substantial forms

VAK_4.15
    supplies the rule of the four substantial types
```

## 12. Light Organon interpretation

The restrained result is simply that a multiplicity of names may express a smaller number of real determinations. Stronger speculative reconstruction should remain bracketed until the Bhāṣya pass.

## 13. OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_14
    a vak:Karika ;
    rdfs:label "VAK 4.14" ;
    vak:continues vak:VAK_4_13 ;
    vak:hasTopic vak:PratimoksaClassification ;
    vak:hasTopic vak:NominalAndSubstantialDivision .

vak:PratimoksaSamvara
    vak:hasNominalDivision vak:Eightfold ;
    vak:hasSubstantialDivision vak:Fourfold .

vak:NominalPratimoksaClass
    vak:distinguishedBy vak:Gender ;
    vak:distinguishedBy vak:TransferOfDesignation .

vak:PratimoksaClasses
    vak:haveRelation vak:NonConflict .
```

## 14. Verse summary

```text
VAK_4.14

Prātimokṣa restraint is:

    eightfold by disciplinary designation

but:

    fourfold in substantial type

Different names do not necessarily establish different restraint-substances.
```
