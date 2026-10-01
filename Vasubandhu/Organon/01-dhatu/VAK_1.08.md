# VAK_1.08

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

`Ye … te` restricts 1.07. Not every aggregate is this. The Path is Conditioned and not Impure.

## 4. Grammar

```text
ye sāsravāḥ
    = upādānaskandhāḥ
    = saraṇāḥ api
    = duḥkha, samudaya, loka, dṛṣṭisthāna, bhava
```

One field under a summary division. The second line names that same Impure field. It is not a second inventory.

## 5. Translation

### Literal

Those which are Impure are the *upādānaskandhas*. They are also *saraṇa*. They are suffering, origin, world, the station of views, and becoming.

### Bhāṣya-informed

The Impure aggregates are the *upādānaskandhas*. Not every aggregate is one: the Path is Conditioned and Pure. The five names are coextensive with this Impure field. Each has its own ground. Those grounds wait on the Bhāṣya.

## 6. Philosophical Translation

1.07 was the wheel. 1.08 divides it.

```text
Impure          what persists
                the summary division
                the sheath is not this verse

Path            Conditioned
                Pure
                not this field
```

Suffering, origin, world, station of views, becoming: names of that division. Not synonyms. Not a second list.

## 7. Vocabulary

| Sanskrit | Determination |
|---|---|
| sāsrava | Impure. Summary division |
| upādānaskandha | the Impure subset of the aggregates |
| anāsrava | Pure. The Path |
| saraṇa | with conflict. Coextensive with the Impure field |
| loka | here, what dissolves |
| dṛṣṭisthāna | station of views |
| bhava | becoming |

## 8. Logical Determination

```text
Impure(x) ↔ Upādānaskandha(x)
Being(x) ↛ Impure(x)
Path is Conditioned and Pure
```

## 9. Interpretive Note

Impure is the top-level division. The sheath is later. The Bhāṣya is not synced.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_08 a vak:Karika ;
    vak:hasTopic vak:ImpureDivision ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Impure vak:summaryDivision true .
vak:Path vak:not vak:Impure .
```
