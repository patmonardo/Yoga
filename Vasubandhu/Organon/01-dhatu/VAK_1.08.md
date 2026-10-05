# VAK_1.08 — The Impure Division of the Bases

## 1. Sanskrit (Devanāgarī)

> ये सास्रवा उपादानस्कन्धास्ते सरणा अपि ।
>
> दुःखं समुदयो लोको दृष्टिस्थानं भवश्च ते ॥ १.०८ ॥॥

## 2. Sanskrit (IAST)

> ye sāsravā upādānaskandhās te saraṇā api /
>
> duḥkhaṃ samudayo loko dṛṣṭisthānaṃ bhavaś ca te // 1.08 //

## 3. Padaccheda

ye | sāsravāḥ | upādāna-skandhāḥ | te | saraṇāḥ | api |
duḥkham | samudayaḥ | lokaḥ | dṛṣṭi-sthānam | bhavaḥ | ca | te

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

The Impure Bases are the Bases of appropriation
(*upādānaskandhas*). Not every Base is one: the Path is Conditioned and
Pure. The five names are coextensive with this Impure field. Each has its
own ground. Those grounds wait on the Bhāṣya.

## 6. Philosophical Translation

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

The Form Base is Form Theory, not a material substrate: it is the empirical
determination of appearance, as established in 1.07. This verse marks the
Impure subset while preserving the Path as Conditioned and Pure.

## 7. Vocabulary

| Sanskrit | Determination |
|---|---|
| sāsrava | Impure. Summary division |
| upādānaskandha | Base of appropriation; the Impure subset of the five Bases |
| anāsrava | Pure; the Path is Conditioned and Pure |
| saraṇa | with conflict. Coextensive with the Impure field |
| loka | here, what dissolves |
| dṛṣṭisthāna | station of views |
| bhava | becoming |

## 8. Logical Determination

```text
Impure(x) ↔ AppropriationBase(x)
AppropriationBase(x) → Base(x)
Base(x) ↛ Impure(x)
Path is Conditioned and Pure
```

## 9. Interpretive Note

Impure is the top-level division within the five-Base field. The sheath is
later. The Bhāṣya is not synced. This verse refines the Base/Being
determination; it does not itself complete the Essence Base and Principle
movement. The machine continues through 1.28.

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
