# VAK_1.47

## 1. Sanskrit (Devanāgarī)

> तथा श्रोत्रं त्रयाणां तु सर्वमेव स्वभूमिकम् ।
>
> कायविज्ञानमधरसवभूमि अनियतं मनः ॥ १.४७ ॥

## 2. Sanskrit (IAST)

> tathā śrotraṃ trayāṇāṃ tu sarvam eva svabhūmikam /
>
> kāyavijñānam adharasvabhūmi aniyataṃ manaḥ // VAkK_1.47 //

Source saṃhitā form:

> tathā śrotraṃ trayāṇāṃ tu sarvameva svabhūmikam /
>
> kāyavijñānamadharasvabhūmi aniyataṃ manaḥ // VAkK_1.47 //

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| tathā | tathā | likewise |
| śrotram | śrotram | ear-domain |
| trayāṇām tu | trayāṇām tu | but of the three |
| sarvam eva | sarvam eva | all indeed |
| svabhūmikam | sva-bhūmikam | belonging to its own plane |
| kāyavijñānam | kāya-vijñānam | body-knowledge |
| adhara-svabhūmi | adhara-svabhūmi | lower or own plane |
| aniyatam | aniyatam | indeterminate, not fixed |
| manaḥ | manaḥ | mind |

## 4. Grammar

This verse continues the plane-analysis from VAK_1.46.

The ear-domain is treated similarly to the eye-domain. For the three remaining sensory domains, the relation is said to be **svabhūmika**, belonging to their own plane.

```text
ghrāṇa
jihvā
kāya
    = own-plane object relation
```

Body-knowledge is said to be related to lower or own plane:

```text
kāyavijñāna
    = lower-plane or own-plane
```

Mind is **aniyata**, indeterminate or not fixed. Manas is not restricted in the same way as the bodily sensory domains.

## 5. Literal Translation

> Likewise the ear. But for the three, everything indeed belongs to its own plane. Body-knowledge is of lower or own plane. Mind is indeterminate.

## 6. Philosophical Translation

> The ear-domain follows the same plane-logic as the eye. For smell, taste, and touch, the object-relation belongs to the same plane. Body-knowledge may relate to a lower or its own plane, while mind is not fixed by these plane restrictions.

Organon rendering:

> Sensory domains are bound to plane-law in different degrees. Eye and ear have one mode; smell, taste, and touch are own-plane contact domains; bodily knowledge can reach lower or own level; mind is not fixed. Manas exceeds the rigid plane-constraint of the bodily senses.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| śrotra | ear-domain | follows eye-like plane logic |
| trayāṇām | of the three | smell, taste, touch |
| svabhūmika | own-plane | belonging to the same level |
| kāyavijñāna | body-knowledge | tactile/body knowledge-domain |
| adhara | lower | lower plane |
| aniyata | indeterminate / not fixed | applies to mind |
| manas | mind-domain | not restricted like bodily senses |

## 8. Logical Determination

VAK_1.46 gave visual plane-relation. VAK_1.47 completes the sensory and mental plane-structure.

```text
eye / ear
    = distance faculties with special plane relation

smell / taste / touch
    = own-plane contact domains

body-knowledge
    = lower or own plane

mind
    = indeterminate
```

The decisive distinction:

```text
bodily senses
    are plane-bound

manas
    is plane-indeterminate
```

## 9. Interpretive Note

This verse marks the exceptional status of mind. The bodily senses are constrained by the planes of their faculties and objects. Manas is not fixed in the same way.

This is not yet liberation. It is structural openness. Mind can range across determinations in a way that bodily contact faculties cannot.

Organon note:

```text
sense-domain
    = plane-conditioned disclosure

mind-domain
    = plane-indeterminate disclosure
```

This prepares the closing verse, where knowability, permanence, and faculty-status are gathered.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_47
    a vak:Karika ;
    rdfs:label "VAK 1.47" ;
    vak:hasIAST "tathā śrotraṃ trayāṇāṃ tu sarvam eva svabhūmikam / kāyavijñānam adharasvabhūmi aniyataṃ manaḥ" ;
    vak:hasTopic vak:PlaneRelationOfSenseAndMind ;
    vak:belongsTo vak:Dhatunirdesa .

vak:ContactSenseTriad
    vak:hasPlaneRelation vak:OwnPlane .

vak:KayaVijnanaDhatu
    vak:hasPlaneRelation vak:LowerOrOwnPlane .

vak:ManoDhatu
    vak:hasPlaneRelation vak:IndeterminatePlane .
```

## 11. Commit History

- Added Organon analysis for VAK_1.47.
- Extends plane-analysis from eye to ear and the remaining sensory domains.
- Establishes smell, taste, and touch as own-plane domains.
- Marks body-knowledge as lower-or-own-plane.
- Establishes mind as indeterminate with respect to plane.
