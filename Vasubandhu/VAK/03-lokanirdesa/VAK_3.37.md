# VAK_3b — VAkK_3.37

## Sanskrit — Devanāgarī

तुषितण्डुलवत् कर्म तथैवौषधिपुष्पवत् ।
सिद्धान्नपानवद्वस्तु तस्मिन् भवचतुष्टये ॥ VAkK_3.37 ॥

## Sanskrit — IAST

tuṣitaṇḍulavat karma tathaivauṣadhi puṣpavat /
siddhānnapānavad vastu tasmin bhavacatuṣṭaye // VAkK_3.37 //

## Source Caution

The source reads:

```text
tuṣitaṇḍulavat karma tathaivauṣadhi puṣpavat /
siddhānnapānavadvastu tasmin bhavacatuṣṭaye // VAkK_3.37 //
```

This continues the simile-series begun in VAkK_3.36. The exact force of each simile should be checked against the Bhāṣya.

## Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| tuṣitaṇḍulavat | tuṣa-taṇḍula-vat | like husk and grain |
| karma | karma | action / karma |
| tathā eva | tathā eva | just so / likewise |
| auṣadhi | auṣadhi | herb / medicine / plant |
| puṣpavat | puṣpa-vat | like flower |
| siddhānnapānavat | siddha-anna-pāna-vat | like prepared food and drink |
| vastu | vastu | real thing / factual basis / concrete existence |
| tasmin | tasmin | in that |
| bhavacatuṣṭaye | bhava-catuṣṭaye | in the fourfold becoming / four modes of existence |

## Grammar

```text
tuṣa-taṇḍula-vat karma
    = karma is like husk and grain

tathā eva auṣadhi puṣpa-vat
    = likewise like herb/medicine and flower

siddha-anna-pāna-vat vastu
    = vastu is like prepared food and drink

tasmin bhava-catuṣṭaye
    = in that fourfold becoming
```

## Literal Translation

Karma is like husk and grain, and likewise like herb and flower. Vastu is like prepared food and drink within that fourfold becoming.

## Philosophical Translation

Within the fourfold becoming, karma is illustrated by generative and maturing similes such as husk-and-grain, herb, and flower. Vastu, the resultant factual basis, is compared to prepared food and drink. The wheel is thus explained not merely by listing factors, but by showing their essential functions: affliction roots, karma matures, and vastu is the consumable result.

## Technical Vocabulary

| Sanskrit | Working translation | Note |
|---|---|---|
| karma | action / karma | The productive action-factor in the wheel |
| tuṣa | husk / chaff | Protective or enclosing grain-simile |
| taṇḍula | grain / rice-grain | Maturing karmic seed-result image |
| auṣadhi | herb / plant / medicine | Growth or efficacy simile |
| puṣpa | flower | Maturation / blossoming simile |
| vastu | factual basis / concrete existence | Resultant concrete thinghood |
| siddhānna | prepared food | Consumable or completed result |
| pāna | drink | Consumable support |
| bhava-catuṣṭaya | fourfold becoming | Four modes of becoming; requires Bhāṣya control |

## Doctrinal Determination

VAkK_3.36 began with kleśa as generative root-condition.

VAkK_3.37 now extends the simile-analysis to karma and vastu.

```text
kleśa
    = seed / root / generative condition

karma
    = husk-grain / herb / flower
    = productive and maturing action

vastu
    = prepared food and drink
    = resultant concrete basis
```

This returns to the compression stated in VAkK_3.26:

```text
kleśa
karma
vastu / phala
```

## Logical Determination

This does look like a movement from listed being to essential being.

```text
listed being:
    kleśa, karma, vastu

essential being:
    kleśa as generative root
    karma as maturing productivity
    vastu as consumable result / concrete basis
```

The verse does not merely say what the items are. It says how they function in the wheel.

```text
affliction roots
karma matures
vastu appears as concrete result
```

## Interpretive Note

This is a protocol for passing from the factor as named to the factor as functional essence.

The twelve limbs are not isolated items. Through simile they become intelligible as roles in a reproductive process.

```text
factor
    → functional role
        → essential determination in the wheel
```

This remains Sanskrit-first and Bhāṣya-dependent, but the contact point is strong.

## Organon Interpretation

Light contact point:

```text
Being as item
    becomes essence as function.
```

The wheel is not only an inventory. It is a system of roles:

```text
rooting
maturing
resulting
consuming / sustaining
```

This supports the larger project claim that the first part of Lokanirdeśa is the world of conditioned human experience as a self-reproducing system.

## OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_37
    a vak:Karika ;
    rdfs:label "VAkK 3.37" ;
    vak:continues vak:VAK_3_36 ;
    vak:hasTopic vak:Karma ;
    vak:hasTopic vak:Vastu ;
    vak:usesSimile vak:HuskGrainSimile ;
    vak:usesSimile vak:HerbFlowerSimile ;
    vak:usesSimile vak:FoodDrinkSimile .

vak:HuskGrainSimile
    a logic:FunctionalSimile ;
    rdfs:label "husk-grain simile" .

vak:FoodDrinkSimile
    a logic:ResultSimile ;
    rdfs:label "prepared food and drink simile" .
```

## Commit Note

Committed VAK_3b / VAkK_3.37.

Established:
- karma and vastu are added to the simile-analysis begun with kleśa.
- karma is explained through productive and maturing similes.
- vastu is explained through prepared food and drink as concrete result.
- the verse supports reading the wheel as functional essence, not merely listed being.
