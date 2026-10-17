# VAK_1.08 — The Impure Division of the Bases

## 1. Sanskrit (Devanāgarī)

```sanskrit
ये सास्रवा उपादानस्कन्धास्ते सरणा अपि ।
दुःखं समुदयो लोको दृष्टिस्थानं भवश्च ते ॥ १.०८ ॥
```

## 2. Sanskrit (IAST)

```text
ye sāsravā upādānaskandhās te saraṇā api /
duḥkhaṃ samudayo loko dṛṣṭisthānaṃ bhavaś ca te // 1.08 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| ye | nominative masculine plural | those which. Restricts the five Bases of 1.07 |
| sāsravāḥ | sa-āsrava; nominative masculine plural | Impure. The summary division |
| upādānaskandhāḥ | upādāna-skandha; nominative masculine plural | Bases of appropriation. Not every Base |
| te | nominative masculine plural | they. Same field |
| saraṇāḥ | sa-raṇa; nominative masculine plural | with conflict. Coextensive with the Impure field |
| api | particle | also. Not a second inventory |
| duḥkham | nominative neuter singular | suffering |
| samudayaḥ | nominative masculine singular | origin |
| lokaḥ | nominative masculine singular | world. Here, what dissolves |
| dṛṣṭisthānam | dṛṣṭi-sthāna; nominative neuter singular | station of views. Not the station of prajñā |
| bhavaḥ | nominative masculine singular | becoming |
| ca | particle | and. The five names are one field |
| te | nominative masculine plural | they, resumed |

## 4. Grammar

```text
ye sāsravāḥ
    = upādānaskandhāḥ
    = saraṇāḥ api
    = duḥkha, samudaya, loka, dṛṣṭisthāna, bhava
```

One field under a summary division. The second line names that same Impure field. It is not a second inventory. The Path is Conditioned and Pure, and is outside the restriction.

## 5. Translation

### Literal Translation

> Those which are Impure are the Bases of appropriation. They are also with
> conflict. They are suffering, origin, world, the station of views, and
> becoming.

### Bhāṣya-informed study translation

> Those conditioned dharmas that are with outflows are Bases of
> appropriation; they too are with conflict. These same dharmas are
> suffering, origin, the world, the station of views, and becoming.

## 6. Philosophical Translation

The five Bases are divided. The Impure are the Bases of appropriation, and they are also the field of conflict. That same field is suffering, origin, world, the station of views, and becoming.

```text
Five Bases       the gathered field of 1.07

Impure           Bases of appropriation
                 the summary division

Path             Conditioned and Pure
                 not within this division
```

## 7. Technical Vocabulary

| Sanskrit | Do not use as the reading | Determination |
|---|---|---|
| sāsrava | with outflows; lodging | Impure. Summary division |
| anāsrava | outflow-free | Pure. The Path is Conditioned and Pure |
| upādānaskandha | Base of clinging as a stain-word | Base of appropriation |
| saraṇa | with defilement, unspecified | with conflict |
| loka | a place | here, what dissolves |
| dṛṣṭisthāna | a viewpoint | station of views |
| bhava | existence as a realm-name | becoming |

## 8. Logical Determination

```text
Impure(x) ↔ AppropriationBase(x)
AppropriationBase(x) → Base(x)
Base(x) ↛ Impure(x)
Path is Conditioned and Pure

saraṇa ↔ Impure
duḥkha, samudaya, loka, dṛṣṭisthāna, bhava
    coextensive
    not synonyms
```

## 9. Interpretive Note

**Translation note.** The Bhāṣya explains the three relations behind the name Base of appropriation: the afflictions arise from these Bases, govern them, or arise from them. It also explains that afflictions are called conflicts because they injure oneself and others.

Impure is the top-level division within the five-Base field. Once the division is made, the word can drop. The sheath is later. The first two names are the first two Truths of what persists. The station of views is not the station of prajñā. A Rational Dharma does not Persist.

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