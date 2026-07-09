# VAK_3.96 — Kalpa Machinery: Cakravartin Territory and Modes of Conquest

## 1. Sanskrit — Devanāgarī

```sanskrit
एकद्वित्रिचतुर्द्वीपा न च द्वौ सह बुद्धवत् ।
प्रत्युद्यानस्वयंयानकलहास्त्रजितोऽवधाः ॥ VAkK_3.96 ॥
```

## 2. Sanskrit — IAST

```iast
ekadvitricaturdvīpāḥ na ca dvau saha buddhavat /
pratyudyāna-svayaṃyāna-kalahāstrajitā avadhāḥ // VAkK_3.96 //
```

## 3. Source Caution

The source reading is:

```iast
ekadvitricaturdvīpāḥ na ca dvau saha buddhavat /
pratyudyānasvayaṃyāna kalahāstrajitaḥ avadhāḥ // VAkK_3.96 //
```

Sandhi and compounds have been lightly normalized:

```iast
eka-dvi-tri-catur-dvīpāḥ na ca dvau saha buddha-vat /
pratyudyāna-svayaṃ-yāna-kalaha-astra-jitāḥ avadhāḥ //
```

The verse continues the four cakravartin types from VAkK_3.95. Their scope extends respectively over one, two, three, or four continents, and two do not arise together, just as two Buddhas do not arise together in the same world-system. The second pāda gives graded modes of conquest, from peaceful reception through weapon-conquest. The exact matching of each conquest-mode to each wheel-type should be checked against the bhāṣya.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| ekadvitricaturdvīpāḥ | eka-dvi-tri-catur-dvīpāḥ | having one, two, three, or four continents as scope |
| na ca | na ca | and not |
| dvau | dvau | two |
| saha | saha | together, simultaneously |
| buddhavat | buddha-vat | like Buddhas |
| pratyudyāna | pratyudyāna | coming forth to meet, reception |
| svayaṃyāna | svayaṃ-yāna | going by oneself / self-approach |
| kalaha | kalaha | conflict, quarrel |
| astra | astra | weapon |
| jitāḥ | jitāḥ | conquered, won |
| avadhāḥ | avadhāḥ | boundaries, limits, extents |

## 5. Grammar

| Term | Form | Function |
|---|---|---|
| eka-dvi-tri-catur-dvīpāḥ | nominative plural masculine | the four cakravartins have one-, two-, three-, and four-continent scope |
| na ca dvau saha | negative phrase | two do not occur together |
| buddha-vat | adverbial comparison | like Buddhas |
| pratyudyāna-svayaṃ-yāna-kalaha-astra-jitāḥ | nominative plural masculine compound | conquered by reception, self-going, conflict, or weapons |
| avadhāḥ | nominative plural masculine/feminine | limits / territorial extents; or those whose limits are thus won |

## 6. Literal Translation

They have one, two, three, or four continents; and two do not [arise] together, as with Buddhas. Their limits are won by coming forth to meet, by self-going, by conflict, and by weapons.

## 7. Philosophical Translation

The four wheel-turning kings differ by territorial scope: one continent, two continents, three continents, or all four continents. Like Buddhas, two cakravartins do not arise simultaneously in the same world-field. Their conquest is also graded: some are accepted by subjects coming out to meet them, some by their own approach, some through conflict, and some through weapons.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| eka-dvīpa | one-continent | lowest territorial scope |
| dvi-dvīpa | two-continent | second territorial scope |
| tri-dvīpa | three-continent | third territorial scope |
| catur-dvīpa | four-continent | complete four-continent scope |
| buddha-vat | like Buddhas | non-co-presence rule |
| pratyudyāna | reception / coming forth to meet | peaceful submission mode |
| svayaṃ-yāna | self-going / personal approach | conquest by the king’s own movement |
| kalaha | conflict | conquest through struggle |
| astra | weapon | conquest through arms |
| jita | conquered / won | achieved dominion |
| avadhi | boundary / limit | territorial extent |

## 9. Doctrinal Determination

VAkK_3.95 gave the four wheel-materials:

```text
gold
    → silver
        → copper
            → iron
```

VAkK_3.96 adds their territorial and political determination:

```text
cakravartin types
    → one-continent
    → two-continent
    → three-continent
    → four-continent
```

And their conquest modes:

```text
reception
    → self-going
        → conflict
            → weapons
```

The royal wheel is therefore graded both spatially and politically.

## 10. Logical Determination

This verse gives sovereignty as territorial scope plus mode of establishment.

```text
cakravartin
    → wheel-type
        → territorial range
            → conquest-mode
```

The political wheel is a lawful differentiation within the kalpa-wheel.

## 11. Interpretive Note

The comparison `buddha-vat` is important:

```text
Buddha
    → no two together

Cakravartin
    → no two together
```

Both are world-historical singularities. But their function differs:

```text
Buddha
    → Dharma sovereignty

Cakravartin
    → worldly sovereignty
```

This keeps the wheel-language precise without collapsing Dharma-wheel and royal wheel.

## 12. Organon Interpretation

Light contact point:

```text
The world-wheel admits singular world-rulers, but not duplication of the singular function.
```

For this pass, we stay close to the Kośa. The cakravartin is not merely a powerful king; he is a temporally conditioned singular appearance whose sovereignty is measured by continent-scope and mode of conquest.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_96
    a vak:Karika ;
    rdfs:label "VAK 3.96" ;
    vak:sourceReference "VAkK_3.96" ;
    vak:continues vak:VAK_3_95 ;
    vak:hasTopic vak:CakravartinTerritorialScope ;
    vak:hasTopic vak:CakravartinConquestModes ;
    vak:belongsTo vak:KalpaMachineryBlock .

vak:CakravartinTerritorialScope
    a logic:TerritorialClassification ;
    rdfs:label "cakravartin territorial scope" ;
    vak:hasScope vak:OneContinentScope ;
    vak:hasScope vak:TwoContinentScope ;
    vak:hasScope vak:ThreeContinentScope ;
    vak:hasScope vak:FourContinentScope .

vak:CakravartinConquestModes
    a logic:PoliticalModeSeries ;
    rdfs:label "cakravartin conquest modes" ;
    vak:hasMode vak:ReceptionConquest ;
    vak:hasMode vak:SelfGoingConquest ;
    vak:hasMode vak:ConflictConquest ;
    vak:hasMode vak:WeaponConquest .

vak:NoCoPresenceRule
    a logic:SingularityRule ;
    rdfs:label "no two together, like Buddhas" .
```

## 14. Commit Note

Committed VAK_3.96 / VAkK_3.96.

Established:
- cakravartins rule one, two, three, or four continents.
- two cakravartins do not arise together, like Buddhas.
- their conquest modes are reception, self-going, conflict, and weapons.
- cakravartin sovereignty is graded by territorial scope and mode of establishment.
