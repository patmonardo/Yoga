# VAK_3b — VAkK_3.40

## Sanskrit — Devanāgarī

स्पर्शंचेतनाविज्ञा आहाराः सास्रवास्त्रिषु ।
मनोमयः संभवैषी गन्धर्वश्चान्तराभवः ॥ VAkK_3.40 ॥

## Sanskrit — IAST

sparśaṃcetanāvijñā āhārāḥ sāsravās triṣu /
manomayaḥ saṃbhavaiṣī gandharvaścāntarābhavaḥ // VAkK_3.40 //

## Source Caution

The source reads:

```text
sparśaṃcetanāvijñā āhārāḥ sāsravāstriṣu /
manomayaḥ saṃbhavaiṣī gandharvaścāntarābhavaḥ // VAkK_3.40 //
```

The first pāda is compact. It is resolved as naming three further nutriments: sparśa, cetanā, and vijñāna. The second pāda introduces names for the intermediate existence.

## Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| sparśam | sparśam | contact |
| cetanā | cetanā | intention / volition |
| vijñā | vijñā / vijñāna | knowledge / consciousness-series term; here nutriment name |
| āhārāḥ | āhārāḥ | nutriments |
| sāsravāḥ | sa-āsravāḥ | with outflows / contaminated |
| triṣu | triṣu | in the three |
| manomayaḥ | mano-mayaḥ | mind-made |
| saṃbhavaiṣī | saṃbhava-eṣī | seeking birth / seeking coming-into-being |
| gandharvaḥ | gandharvaḥ | gandharva; intermediate being-name |
| ca | ca | and |
| antarābhavaḥ | antarā-bhavaḥ | intermediate existence |

## Grammar

```text
sparśaṃ cetanā vijñā āhārāḥ
    = contact, intention, and vijñāna are nutriments

sāsravāḥ triṣu
    = they are with outflows in the three realms

manomayaḥ saṃbhavaiṣī gandharvaḥ ca antarābhavaḥ
    = the intermediate existence is mind-made, seeking birth, and called gandharva
```

## Literal Translation

Contact, intention, and vijñāna are nutriments, with outflows in the three realms. The intermediate existence is mind-made, seeking birth, and also called gandharva.

## Philosophical Translation

Beyond morsel nutriment, contact, volition, and vijñāna also function as nutriments. In the three realms they are contaminated. The verse then names the intermediate existence as mind-made, birth-seeking, and gandharva.

## Technical Vocabulary

| Sanskrit | Working translation | Note |
|---|---|---|
| sparśa | contact | Here as nutriment |
| cetanā | intention / volition | Volitional nutriment |
| vijñāna / vijñā | knowledge / consciousness-series term | Here as nutriment; keep source form cautious |
| āhāra | nutriment | Sustaining condition |
| sāsrava | with outflows | Still within contaminated conditioned experience |
| triṣu | in the three | The three realms |
| manomaya | mind-made | Name of intermediate existence |
| saṃbhavaiṣī | seeking birth | Or seeking coming-to-be |
| gandharva | gandharva | Name for the intermediate being |
| antarābhava | intermediate existence | Existence between death and rebirth |

## Doctrinal Determination

VAkK_3.39 defined morsel nutriment.

VAkK_3.40 completes the four nutriments:

```text
kavaḍīkāra āhāra
sparśa āhāra
cetanā āhāra
vijñāna āhāra
```

The verse also states:

```text
sāsravāḥ triṣu
```

These nutriments are with outflows in the three realms. Nutriment belongs to the sustaining structure of conditioned experience.

The second half introduces `antarābhava`:

```text
antarābhava
    = manomaya
    = saṃbhavaiṣī
    = gandharva
```

This prepares the following discussion of birth, continuity, and intermediate existence.

## Logical Determination

The sustaining feature of the world is not only material food.

```text
āhāra
    includes contact
    includes intention
    includes vijñāna
```

So nutriment is a general sustaining function:

```text
material support
contact support
volitional support
vijñāna support
```

This is a powerful refinement of the active-modeling vocabulary:

```text
nutriment
    = that by which the conditioned series is maintained
```

## Interpretive Note

The Vedānta food-sheath echo remains useful, but this verse shows why the Abhidharma analysis is broader than material food.

`Āhāra` names the sustaining condition of the world. That sustaining condition includes contact, volition, and vijñāna. The world is fed not only by morsels but by contact, intention, and the continuity of knowing.

## Organon Interpretation

Light contact point:

```text
A system reproduces itself by what feeds it.
```

Here, feeding is not only physical. The wheel is sustained by:

```text
matter
contact
intention
vijñāna
```

This remains Abhidharma-first, but it gives a clear active-modeling feature: nutriment is the sustaining input of the conditioned process.

## OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_40
    a vak:Karika ;
    rdfs:label "VAkK 3.40" ;
    vak:continues vak:VAK_3_39 ;
    vak:hasTopic vak:Ahara ;
    vak:hasTopic vak:Antarabhava ;
    vak:defines vak:FourNutriments .

vak:FourNutriments
    a logic:Classification ;
    rdfs:label "four nutriments" ;
    vak:hasMember vak:KavadikaraAhara ;
    vak:hasMember vak:SparsaAhara ;
    vak:hasMember vak:CetanaAhara ;
    vak:hasMember vak:VijnanaAhara .

vak:Antarabhava
    a logic:IntermediateExistence ;
    rdfs:label "antarābhava" ;
    vak:hasName vak:Manomaya ;
    vak:hasName vak:Sambhavaisin ;
    vak:hasName vak:Gandharva .
```

## Commit Note

Committed VAK_3b / VAkK_3.40.

Established:
- the four nutriments are morsel nutriment, contact, intention, and vijñāna.
- the nutriments are sāsrava in the three realms.
- antarābhava is introduced as manomaya, saṃbhavaiṣī, and gandharva.
