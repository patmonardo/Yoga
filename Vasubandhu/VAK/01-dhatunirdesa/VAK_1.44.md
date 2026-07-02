# VAK_1.44

## 1. Sanskrit (Devanāgarī)

> त्रिभिर्घ्राणादिभिस्तुल्यविषयग्रहणं मतम् ।
>
> चरमस्याश्रयोऽतीतः पञ्चानां सहजश्च तैः ॥ १.४४ ॥

## 2. Sanskrit (IAST)

> tribhir ghrāṇādibhis tulyaviṣayagrahaṇaṃ matam /
>
> caramasyāśrayo 'tītaḥ pañcānāṃ sahajaś ca taiḥ // VAkK_1.44 //

Source saṃhitā form:

> tribhirghrāṇādibhistulyaviṣayagrahaṇaṃ matam /
>
> caramasyāśrayo 'tītaḥ pañcānāṃ sahajaśca taiḥ // VAkK_1.44 //

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| tribhiḥ | tribhiḥ | by three |
| ghrāṇa-ādibhiḥ | ghrāṇa-ādibhiḥ | by nose and the others |
| tulya-viṣaya-grahaṇam | tulya-viṣaya-grahaṇam | apprehension of an equal object |
| matam | matam | is held / accepted |
| caramasya | caramasya | of the last |
| āśrayaḥ | āśrayaḥ | support / basis |
| atītaḥ | atītaḥ | past |
| pañcānām | pañcānām | of the five |
| sahajaḥ | sahajaḥ | co-born, simultaneous |
| ca taiḥ | ca taiḥ | and with them |

## 4. Grammar

The first half completes VAK_1.43. Nose, tongue, and body apprehend an object equal to themselves in contact-relation.

```text
ghrāṇa
jihvā
kāya
    = contact faculties
    = apprehend a tulyaviṣaya, an object equal/present in contact
```

The second half concerns support-time.

```text
caramasya āśrayaḥ atītaḥ
    the support of the last is past
```

The last knowledge-domain is **manovijñāna**. Its support is the immediately past **manodhātu**.

For the five sensory knowledge-domains:

```text
pañcānām sahajaḥ ca taiḥ
    the support is co-born with them
```

The five sensory knowledges arise together with their respective sense-faculty supports.

## 5. Literal Translation

> By the three beginning with smell, apprehension of an equal object is accepted. The support of the last is past; for the five, the support is co-born with them.

## 6. Philosophical Translation

> Nose, tongue, and body apprehend objects in contact, through an equal object-field. Mental knowledge, the last knowledge-domain, depends on a past support; the five sensory knowledge-domains depend on supports simultaneous with them.

Organon rendering:

> Object-relation is also time-relation. Contact faculties require equality with their object-field. Mental knowledge is supported by the past, while sensory knowledge is supported by the co-born faculty. The system now distinguishes contact-mode and temporal support.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| ghrāṇādi | nose and the others | smell, taste, touch faculties |
| tulyaviṣaya | equal object | object equal/present in contact-relation |
| grahaṇa | apprehension | object-taking |
| āśraya | support / basis | support of knowledge |
| carama | last | manovijñāna, mental knowledge-domain |
| atīta | past | past support for mental knowledge |
| sahaja | co-born | simultaneous support for sensory knowledge |

## 8. Logical Determination

VAK_1.43 distinguished non-contact and contact object-domains. VAK_1.44 adds temporal support:

```text
contact faculties
    = apprehend equal/contact object

mental knowledge
    = supported by the past

five sensory knowledges
    = supported by co-born faculties
```

This gives a new axis:

```text
object-contact
    +
support-time
```

## 9. Interpretive Note

The verse is subtle because it binds object-relation to temporality.

Mental knowledge is not supported in the same way as sensory knowledge. Manovijñāna depends on the immediately past manodhātu. Sensory knowledges arise together with their living faculty-bases.

Thus the system distinguishes:

```text
co-born support
    sensory knowledge

past support
    mental knowledge
```

Organon note:

```text
sensation
    = simultaneity of faculty and knowledge

mental knowledge
    = mediation through the past
```

This prepares the higher logic of recollection, representation, and mental determination.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_44
    a vak:Karika ;
    rdfs:label "VAK 1.44" ;
    vak:hasIAST "tribhir ghrāṇādibhis tulyaviṣayagrahaṇaṃ matam / caramasyāśrayo 'tītaḥ pañcānāṃ sahajaś ca taiḥ" ;
    vak:hasTopic vak:ObjectContactAndSupportTime ;
    vak:belongsTo vak:Dhatunirdesa .

vak:ContactTriad
    vak:hasObjectRelation vak:TulyaVisayaGrahana .

vak:ManoVijnanaDhatu
    vak:hasSupportTime vak:PastSupport .

vak:FiveSensoryKnowledgeDomains
    vak:hasSupportTime vak:CobornSupport .
```

## 11. Commit History

- Added Organon analysis for VAK_1.44.
- Establishes smell, taste, and touch as apprehending equal/contact objects.
- Distinguishes past support for mental knowledge from co-born support for five sensory knowledges.
- Adds temporal support to the chapter sequence.
