# VAK_3b — VAkK_3.30

## Sanskrit — Devanāgarī

नाम त्वरूपिणः स्कन्धाः स्पर्शाः षट् संनिपातजाः ।
पञ्चप्रतिघसंस्पर्शः षष्ठोऽधिवचनाह्वयः ॥ VAkK_3.30 ॥

## Sanskrit — IAST

nāma tv arūpiṇaḥ skandhāḥ sparśāḥ ṣaṭ saṃnipātajāḥ /
pañcapratighasaṃsparśaḥ ṣaṣṭho 'dhivacanāhvayaḥ // VAkK_3.30 //

## Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| nāma | nāma | name |
| tu | tu | but; now |
| arūpiṇaḥ | arūpiṇaḥ | non-material / formless |
| skandhāḥ | skandhāḥ | aggregates |
| sparśāḥ | sparśāḥ | contacts |
| ṣaṭ | ṣaṭ | six |
| saṃnipātajāḥ | saṃnipāta-jāḥ | born from conjunction / concurrence |
| pañca | pañca | five |
| pratighasaṃsparśaḥ | pratigha-saṃsparśaḥ | contact involving resistance / impact |
| ṣaṣṭhaḥ | ṣaṣṭhaḥ | the sixth |
| adhivacanāhvayaḥ | adhivacana-āhvayaḥ | called designation / name-expression |

## Grammar

```text
nāma tu arūpiṇaḥ skandhāḥ
    = name, however, is the non-material aggregates

sparśāḥ ṣaṭ saṃnipāta-jāḥ
    = the six contacts are born from conjunction

pañca pratigha-saṃsparśaḥ
    = five are resistant/contact-with-impact contacts

ṣaṣṭhaḥ adhivacana-āhvayaḥ
    = the sixth is called designation-contact / name-expression-contact
```

## Literal Translation

Name, however, consists of the non-material aggregates. The contacts are six, born from conjunction. The five are contacts involving resistance; the sixth is called designation-contact.

## Philosophical Translation

Here `name` is not mere verbal naming. It denotes the non-material aggregates. Contact is sixfold and arises from conjunction. The first five forms of contact involve resistance or impact, while the sixth, mental contact, is called contact through designation.

## Technical Vocabulary

| Sanskrit | Working translation | Note |
|---|---|---|
| nāma | name | Here the non-material aggregates, not mere linguistic label |
| arūpiṇaḥ skandhāḥ | non-material aggregates | Feeling, saṃjñā, saṃskāra, vijñāna in relation to rūpa |
| skandha | aggregate | Functional aggregate of conditioned existence |
| sparśa | contact | Arises through conjunction |
| ṣaṭ | six | Six contacts corresponding to six spheres/knowledges |
| saṃnipāta | conjunction / concurrence | Coming-together of factors |
| pratigha | resistance / impact | Pertains to five sense contacts involving material resistance |
| saṃsparśa | contact / touch | Contact-event |
| adhivacana | designation / name-expression | Marks the sixth, mental contact |
| āhvaya | called / named | Denomination |

## Doctrinal Determination

VAkK_3.30 defines two earlier terms from the twelvefold sequence:

```text
nāma
sparśa
```

First:

```text
nāma
    = arūpiṇaḥ skandhāḥ
    = the non-material aggregates
```

So `nāma` is not just linguistic naming. It is the non-material side of the psycho-physical complex.

Second:

```text
sparśa
    = sixfold
    = born from conjunction
```

The contacts divide into:

```text
five contacts involving resistance / impact
    = eye, ear, nose, tongue, body contacts

sixth contact through designation
    = mental contact
```

Thus contact is not one simple thing. It is sixfold according to the spheres of access and their corresponding conjunctions.

## Logical Determination

The verse refines the middle as concrete existence.

```text
nāma
    = non-material aggregate structure

sparśa
    = conjunction-born contact-event
```

The logical movement is:

```text
non-material aggregate organization
    enters conjunction
        produces sixfold contact
```

The split between the first five and the sixth is important:

```text
five contacts
    = resistant / impact-based contact

sixth contact
    = designation-based contact
```

So the concrete middle is not merely material. It contains both:

```text
resistant contact
and
semantic/designative contact
```

## Interpretive Note

This verse corrects any too-simple reading of nāma as merely language. In this context, nāma is the non-material aggregate side of the life-series.

At the same time, the sixth contact is explicitly connected with `adhivacana`, designation. This gives a legitimate textual basis for saying that mental contact has a semantic or name-bearing structure. But this should be kept local to the sixth contact, not generalized too quickly to all of nāmarūpa.

## Organon Interpretation

Speculatively, VAkK_3.30 distinguishes two modes of contact within the concrete middle.

```text
pratigha-saṃsparśa
    = contact through resistance / impact

adhivacana-saṃsparśa
    = contact through designation / name-expression
```

In Organon terms:

```text
concrete existence
    contains resistant interface-events
    and designative interface-events
```

This helps refine the earlier interface hypothesis:

```text
ṣaḍāyatana
    = sixfold sphere-structure

sparśa
    = contact born from conjunction

five contacts
    = impact-based

sixth contact
    = designation-based
```

Thus the system does not reduce experience to either matter or meaning. It articulates both resistant contact and designative contact inside the same wheel.

## OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_30
    a vak:Karika ;
    rdfs:label "VAkK 3.30" ;
    vak:continues vak:VAK_3_29 ;
    vak:hasTopic vak:DependentCoArising ;
    vak:defines vak:Nama ;
    vak:defines vak:Sparsa ;
    vak:distinguishes vak:PratighaSamsparsa ;
    vak:distinguishes vak:AdhivacanaSamsparsa .

vak:Nama
    a vak:DharmaTerm ;
    rdfs:label "nāma" ;
    vak:hasCanonicalTranslation "name" ;
    rdfs:comment "In VAkK 3.30, nāma is defined as the non-material aggregates." .

vak:ArupinahSkandhah
    a logic:AggregateClass ;
    rdfs:label "arūpiṇaḥ skandhāḥ" ;
    vak:hasCanonicalTranslation "non-material aggregates" .

vak:Nama
    logic:definedAs vak:ArupinahSkandhah .

vak:Sparsa
    a vak:DharmaTerm ;
    rdfs:label "sparśa" ;
    vak:hasCanonicalTranslation "contact" ;
    logic:arisesFrom vak:Samnipata ;
    vak:hasMemberCount 6 .

vak:Samnipata
    a logic:Conjunction ;
    rdfs:label "saṃnipāta" ;
    vak:hasCanonicalTranslation "conjunction" .

vak:PratighaSamsparsa
    a logic:ContactType ;
    rdfs:label "pratigha-saṃsparśa" ;
    vak:hasCanonicalTranslation "resistant contact" ;
    vak:hasMemberCount 5 .

vak:AdhivacanaSamsparsa
    a logic:ContactType ;
    rdfs:label "adhivacana-saṃsparśa" ;
    vak:hasCanonicalTranslation "designation-contact" ;
    vak:hasMemberCount 1 .
```

## Commit Note

Committed VAK_3b / VAkK_3.30.

Established:
- nāma is defined as the non-material aggregates.
- sparśa is sixfold and born from conjunction.
- the first five contacts are pratigha-saṃsparśa, contacts involving resistance or impact.
- the sixth is adhivacana-āhvaya, called designation-contact.

Logical determination:
VAkK_3.30 refines the concrete middle by distinguishing non-material aggregate structure from sixfold contact, and by distinguishing impact-based contact from designation-based mental contact.
