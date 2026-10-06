# VAK_1.08 — The Impure Division of the Bases

## 1. Sanskrit (Devanāgarī)

> ये सास्रवा उपादानस्कन्धास्ते सरणा अपि ।
>
> दुःखं समुदयो लोको दृष्टिस्थानं भवश्च ते ॥ १.०८ ॥॥

## 2. Sanskrit (IAST)

> ye sāsravā upādānaskandhās te saraṇā api /
>
> duḥkhaṃ samudayo loko dṛṣṭisthānaṃ bhavaś ca te // 1.08 //

## 3. Lexical Analysis

```text
ye | sāsravāḥ | upādāna-skandhāḥ | te | saraṇāḥ | api |
duḥkham | samudayaḥ | lokaḥ | dṛṣṭi-sthānam | bhavaḥ | ca | te
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| ye | masculine nominative plural relative pronoun | those among the conditioned Bases which are Impure |
| sāsravāḥ | masculine nominative plural adjective | Impure |
| upādāna-skandhāḥ | masculine nominative plural compound | aggregates of appropriation; Techne: Bases of appropriation |
| te | masculine nominative plural demonstrative | those same Impure dharmas |
| saraṇāḥ | masculine nominative plural adjective | with conflict; Bhāṣya relates conflict to affliction |
| api | particle | also |
| duḥkham | neuter singular noun | suffering, a further designation |
| samudayaḥ | masculine singular noun | origin |
| lokaḥ | masculine singular noun | world |
| dṛṣṭi-sthānam | neuter singular compound | station of views |
| bhavaḥ | masculine singular noun | becoming |
| ca | particle | and |

`Ye … te` restricts the five Bases of 1.07. Not every Base is Impure:
the Path is Conditioned and Pure.

## 4. Grammar

```text
ye sāsravāḥ
    = upādānaskandhāḥ
    = saraṇāḥ api
    = duḥkha, samudaya, loka, dṛṣṭisthāna, bhava
```

One field under a summary division. The second line names that same Impure
field. It is not a second inventory.

## 5. Translation

### Literal

Those which are Impure are the Bases of appropriation
(*upādānaskandhas*). They are also *saraṇa*. They are suffering, origin,
world, the station of views, and becoming.

### Bhāṣya-informed

The Impure aggregates are Bases of appropriation. Every such Base is an
aggregate, but some aggregates are Pure and therefore are not Bases of
appropriation. Appropriation here means the afflictions: these Bases can
arise from them, be governed by them, or give rise to them. They are also
with conflict because afflictions persist latently in them and injure self
and others. Suffering, Origin, World, Station of Views, and Becoming are
further designations of this same Impure field, each with its own reason.

## 6. Philosophical Translation and Techne Reading

1.07 gathers the Conditioned dharmas as five Bases. 1.08 divides that
field by Impure and Pure.

```text
Five Bases      the gathered Being-grade field of 1.07

Impure          Bases of appropriation
                the summary division

Path            Conditioned and Pure
                not within this Impure division
```

Suffering, origin, world, station of views, becoming: names of that division. Not synonyms. Not a second list.

In our Techne, the Science of Principles is the First Dharma that can see
the appropriated field without being captured by its persistence. 1.08
shows what comes second as a determinate, Impure configuration of the
conditioned Bases. The Absolute holds that configuration as eternally
sublated: its origin, dependence, and limit are intelligible within the
whole, while its suffering and causal force remain real for those caught
in it. This is our logical reading of the Bhāṣya's distinct relations,
not a translation of *upādāna* or *sāsrava*.

The Form Base is Form Theory, not a material substrate: it is the empirical
determination of appearance, as established in 1.07. This verse marks the
Impure subset while preserving the Path as Conditioned and Pure.

## 7. Vocabulary

| Sanskrit | Conventional force | Techne determination |
|---|---|---|
| sāsrava | Impure | the summary predicate restricting the Bases |
| upādānaskandha | aggregate of appropriation | Base of appropriation; Impure subset |
| anāsrava | Pure | the conditioned Path remains outside this subset |
| saraṇa | with conflict | conflict persists latently in this field |
| duḥkha | suffering | what is contrary to the Āryas |
| samudaya | origin | suffering arises from it |
| loka | world | what dissolves |
| dṛṣṭisthāna | station of views | views persist here |
| bhava | becoming | what comes to be |

## 8. Logical Determination

```text
Impure(x) ↔ AppropriationBase(x)
AppropriationBase(x) → Base(x)
Base(x) ↛ Impure(x)
Path is Conditioned and Pure
```

## 9. Interpretive Note

The Bhāṣya makes the restriction exact: every Base of appropriation is a
Base, but not every Base is a Base of appropriation. It gives three
different relations between affliction and the appropriated Bases:
production from affliction, governance by it, and production of further
affliction from the Bases. The five subsequent names are coextensive
designations, each grounded differently. A reader should be able to
follow these relations before adopting the Techne's First Dharma reading.

Together, 1.07 and 1.08 begin the division beneath the Concept: one
conditioned field, then its Impure subset. The Pure Path prevents the
second determination from exhausting the first. The Base grade has been
opened; the later Essence and Principle grades require their own textual
work.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_08 a vak:Karika ;
    vak:hasTopic vak:ImpureDivision ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Impure vak:summaryDivision true ;
    vak:selects vak:AppropriationBase .
vak:AppropriationBase vak:subsetOf vak:Base .
vak:Path vak:isConditioned true ;
    vak:isPure true ;
    vak:not vak:Impure .
```
