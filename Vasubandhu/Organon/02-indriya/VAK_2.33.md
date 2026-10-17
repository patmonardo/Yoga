# VAK_2.33 — Coarse and Subtle

## 1. Sanskrit (Devanāgarī)

```sanskrit
वितर्कचारावौदार्यसूक्ष्मते मान उन्नतिः ।
मदः स्वधर्मे रक्तस्य पर्यादानं तु चेतसः ॥ २.३३ ॥
```

## 2. Sanskrit (IAST)

```text
vitarkacārāv audāryasūkṣmate māna unnatiḥ /
madaḥ svadharme raktasya paryādānaṃ tu cetasaḥ // 2.33 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| vitarka-cārau | nom. dual m. | vitarka and vicāra |
| audārya-sūkṣmate | nom. dual n. | coarseness and subtlety |
| mānaḥ | nom. sg. m. | conceit |
| unnatiḥ | nom. sg. f. | elevation |
| madaḥ | nom. sg. m. | intoxication |
| sva-dharme raktasya | loc. sg. n. + gen. sg. m. participle | of one attached to one's own qualities |
| paryādānam | nom. sg. n. | taking-over |
| cetasaḥ | gen. sg. n. | of consciousness |

Of consciousness is supplied later. It covers the three definitions.
## 4. Grammar

```text
% start S
S[NAME=vitarka] -> Coarseness[OF=consciousness]
S[NAME=vicara] -> Subtlety[OF=consciousness]
S[NAME=conceit] -> Elevation[RELATIVE=other]
S[NAME=intoxication] -> TakingOver[ATTACHMENT=own-qualities]
```

Coexistence of vitarka and vicāra is not settled by the dual.  
Conceit compares; intoxication takes over one's own.

## 5. Translation

### Literal Translation

> Vitarka and vicāra are coarseness and subtlety. Conceit is elevation.
> Intoxication is the taking-over of the consciousness of one attached to
> one's own qualities.
### Bhāṣya-informed study translation

> Vitarka and vicāra are coarseness and subtlety of consciousness. Conceit
> is elevation of consciousness; intoxication is the taking-over of
> consciousness in one attached to one's own qualities.
## 6. Philosophical Translation

> Coarseness and subtlety do not by themselves settle co-presence. Conceit compares. Intoxication takes over one's own. Level-attribution is not moment-co-presence.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| vitarka | vitarka | proposed coarseness; not settled |
| vicāra | vicāra | proposed subtlety; not settled |
| vāk-saṃskāra | formation of speech | the sūtra account |
| jāti-bheda | difference of kind | demanded, not stated |
| bhūmitaḥ | by level | the five-factor attribution |
| kṣaṇataḥ | by moment | not thereby co-present |
| māna | conceit | elevation by comparison |
| mada | intoxication | taking-over; not conceit |
| saṃpraharṣaṇa | exhilaration | others |

## 8. Logical Determination

```python
from nltk.sem.logic import LogicParser
lp = LogicParser()

vitarka = lp.parse(r'Vitarka(x) <-> Coarseness(x,consciousness)')
vicara = lp.parse(r'Vicara(x) <-> Subtlety(x,consciousness)')
conceit = lp.parse(r'Conceit(x) <-> Elevation(x,relative-to-other)')
intox = lp.parse(r'Intoxication(x) <-> TakingOver(x,own-qualities)')
```

The dual does not settle co-presence.  
Level is not moment.  
Conceit compares; intoxication takes over. another
intoxication
    = taking-over of one's own
liquor
    ≠ the factor
```

## 9. Interpretive Note

**Translation note.** The commentary supplies consciousness as the locus and says conceit involves constructed distinction relative to another. It presents three positions on the relation of vitarka and vicāra—balancing, speech-formation, or denial of co-presence—without harmonizing them. The butter example and a quoted reply are damaged; the summit objection concerns the exclusions of 2.31.

Three positions: balancing, speech-formation, denial of co-presence. No harmonization is appended. The butter example is damaged. Cast into water follows the reply's water and heat. Not a restored reading. The speech quotation is damaged. Its sense is kept.

The summit objection uses the exclusions of 2.31. A satisfactory account would name the factors and keep that range.

Interpretation: what each proposal explains, and what it leaves, is the account. Not a smooth definition the passage does not give. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_33
    a vak:Karika ;
    rdfs:label "VAK 2.33" ;
    vak:hasTopic vak:VitarkaVicara ;
    vak:belongsTo vak:Indriyanirdesa .

vak:VitarkaVicara vak:disputeOpen true .
vak:Conceit vak:comparesWithAnother true .
vak:Intoxication vak:takesOverOwnQualities true .

organon:LevelNotMoment
    organon:notTheVerseEnglish true .
```
