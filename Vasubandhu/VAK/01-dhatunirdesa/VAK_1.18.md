# VAK_1.18

## 1. Sanskrit (Devanāgarī)

> सर्वसंग्रह एकेन स्कन्धेनायतनेन च ।
>
> धातुना च स्वभावेन परभाववियोगतः ॥ १.१८ ॥

## 2. Sanskrit (IAST)

> sarvasaṃgraha ekena skandhenāyatanena ca /
>
> dhātunā ca svabhāvena parabhāvaviyogataḥ // VAkK_1.18 //

Source label in GRETIL: `VAkK_1.18`. Project-normalized label: `VAkK_1.18`.

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| sarva-saṃgrahaḥ | sarva-saṃgrahaḥ | inclusion of all |
| ekena | ekena | by one |
| skandhena | skandhena | aggregate |
| āyatanena ca | āyatanena ca | and sphere |
| dhātunā ca | dhātunā ca | and domain |
| svabhāvena | svabhāvena | by own-nature |
| para-bhāva-viyogataḥ | para-bhāva-viyogataḥ | because of separation from other-nature |

## 4. Grammar

The verse gives the rule of inclusion:

```text
all dharmas are included
    by one aggregate
    by one sphere
    by one domain
```

The ground is **svabhāva**: each dharma is included by its own-nature because it is distinct from what is other than itself.

## 5. Literal Translation

> The inclusion of all is by one aggregate, by one sphere, and by one domain, according to own-nature, because of separation from other-nature.

## 6. Philosophical Translation

> Every dharma is included in its proper aggregate, sphere, and domain according to its own-nature. Its inclusion is determined by what it is, and by its separation from what it is not.

Organon rendering:

> Classification is grounded in self-determination. A dharma belongs where its own-nature places it. Inclusion is therefore not arbitrary grouping but the logical result of difference from other-nature.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| saṃgraha | inclusion / collection | systematic gathering |
| skandha | aggregate | aggregate-form of inclusion |
| āyatana | sphere | relational inclusion |
| dhātu | domain | domain inclusion |
| svabhāva | own-nature | self-determination |
| parabhāva | other-nature | what the dharma is not |
| viyoga | separation | distinction from other |

## 8. Logical Determination

```text
inclusion
    = by own-nature
    = through exclusion of other-nature
```

Thus:

```text
classification
    rests on self-determination
```

## 9. Interpretive Note

This is the logical heart of the taxonomy. The systems of aggregate, sphere, and domain are not competing lists. They are modes of including dharmas according to svabhāva.

Organon note:

```text
svabhāva
    = own determination

classification
    = placing each dharma according to that determination
```

This becomes the foundation for the entire Dhātunirdeśa.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_18
    a vak:Karika ;
    rdfs:label "VAK 1.18" ;
    vak:hasSourceLabel "VAkK_1.18" ;
    vak:hasProjectLabel "VAkK_1.18" ;
    vak:hasTopic vak:InclusionByOwnNature ;
    vak:belongsTo vak:Dhatunirdesa .

vak:InclusionByOwnNature
    vak:groundedIn vak:Svabhava ;
    vak:requiresSeparationFrom vak:Parabhava .
```

## 11. Commit History

- Upgraded VAK_1.18 with expanded Organon analysis.
- Establishes inclusion by aggregate, sphere, and domain according to svabhāva.
- Reads classification as self-determination through distinction from other-nature.
