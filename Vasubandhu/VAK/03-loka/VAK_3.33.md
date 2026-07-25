# VAK_3b — VAkK_3.33

## Sanskrit — Devanāgarī

कामे स्वालम्बनाः सर्वे रूपी द्वादशगोचरः ।
त्रयाणामुत्तरः ध्यानद्वये द्वादश कामगाः ॥ VAkK_3.33 ॥

## Sanskrit — IAST

kāme svālambanāḥ sarve rūpī dvādaśagocaraḥ /
trayāṇām uttaraḥ dhyānadvaye dvādaśa kāmagāḥ // VAkK_3.33 //

## Source Caution

The source reads:

```text
kāme svālambanāḥ sarve rūpī dvādaśagocaraḥ /
trayāṇāmuttaraḥ dhyānadvaye dvādaśa kāmagāḥ // VAkK_3.33 //
```

This verse begins the distribution of the eighteen mental approaches across realms and meditation-levels. The interpretation should remain provisional until the Bhāṣya controls the exact mapping.

## Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| kāme | kāme | in the desire realm |
| svālambanāḥ | sva-ālambanāḥ | having their own object-supports |
| sarve | sarve | all |
| rūpī | rūpī | one belonging to form / form-realm |
| dvādaśagocaraḥ | dvādaśa-gocaraḥ | having twelve as field / range |
| trayāṇām | trayāṇām | of the three |
| uttaraḥ | uttaraḥ | the higher / later / superior |
| dhyānadvaye | dhyāna-dvaye | in the two dhyānas |
| dvādaśa | dvādaśa | twelve |
| kāmagāḥ | kāma-gāḥ | going to / belonging to desire |

## Grammar

```text
kāme
    locative singular
    = in the desire realm

sva-ālambanāḥ sarve
    nominative plural
    = all having their own object-supports

rūpī dvādaśa-gocaraḥ
    nominative singular masculine
    = the form-realm one has twelve as its field/range

trayāṇām uttaraḥ
    = the higher of the three / the later among the three

dhyāna-dvaye
    locative singular
    = in the pair of dhyānas

dvādaśa kāma-gāḥ
    = twelve going to / belonging to desire
```

## Literal Translation

In the desire realm, all have their own object-supports. The form-realm one has twelve as its field. The higher of the three — in the two dhyānas, twelve are desire-going.

## Philosophical Translation

Within the desire realm, all eighteen mental approaches operate with their own object-supports. In the form-realm context, the field is restricted to twelve. In the two dhyānas under consideration, twelve mental approaches are directed toward or belong to the desire realm. The exact distribution is to be checked against the Bhāṣya.

## Technical Vocabulary

| Sanskrit | Working translation | Note |
|---|---|---|
| kāma | desire realm | One of the three dhātus; sphere of sensual desire |
| sva-ālambana | own object-support | Each mental approach has its corresponding support |
| ālambana | object-support | Project term; not merely object |
| sarve | all | Here all eighteen mental approaches in the desire realm |
| rūpī | belonging to form | Refers to form-realm classification |
| gocara | field / range | Range of operation or domain of support |
| dvādaśa | twelve | Restricted range in this classification |
| dhyāna | meditative absorption | Here dhyāna-level as cosmological/experiential field |
| kāma-ga | desire-going / desire-directed | Directed toward or belonging to the desire realm |

## Doctrinal Determination

VAkK_3.32 stated that feeling is eighteenfold by `manopavicāra`.

VAkK_3.33 begins to distribute these eighteen mental approaches by realm and meditative level.

The basic movement is:

```text
manopavicāra
    = eighteenfold

in kāma-dhātu
    all operate with their own ālambanas

in rūpa-related context
    the field is restricted to twelve

in the relevant dhyāna-pair
    twelve are kāma-going / desire-directed
```

The verse is not defining feeling in general. It is mapping the field of mental approaches according to realm and object-support.

## Logical Determination

The logical point is that mental approach is not free-floating.

```text
manopavicāra
    depends on ālambana
    and is distributed by dhātu / dhyāna-field
```

So the eighteenfold feeling-system is bounded by its field of operation.

```text
mental approach
    rises and falls with its object-support field
```

This should be kept doctrinally sober:

```text
not yet:
    Concept in the full Organon sense

but:
    a structured mental operation conditioned by its support-domain
```

## Interpretive Note

This verse supports the working principle that mental operation must be read with its container or field.

The important terms are:

```text
ālambana
    object-support

gocara
    field / range

dhātu / dhyāna
    larger operating domain
```

So `manopavicāra` is not merely an internal subjective act. It is field-bound and support-bound.

This is a contact point for later Organon interpretation, but for now the primary Abhidharma claim is simply that the eighteen mental approaches are distributed by realm and object-support.

## Organon Interpretation

Speculatively, VAkK_3.33 gives a light contact point for the relation of mental approach and container.

```text
mental approach
    has object-support
    has field/range
    belongs to a realm-level
```

This resonates with the idea that a concept rises and falls with its container, but we should not overcommit.

The safe Organon marker is:

```text
manopavicāra
    = field-bound mental ranging
```

The full concept-mapping must wait until the entire wheel and Bhāṣya are in view.

## OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_33
    a vak:Karika ;
    rdfs:label "VAkK 3.33" ;
    vak:continues vak:VAK_3_32 ;
    vak:hasTopic vak:Manopavicara ;
    vak:distributes vak:EighteenfoldManopavicara ;
    vak:hasContext vak:KamaDhatu ;
    vak:hasContext vak:RupaDhatu ;
    vak:hasContext vak:DhyanaField .

vak:EighteenfoldManopavicara
    a logic:Classification ;
    rdfs:label "eighteenfold mental approach" ;
    vak:hasMemberCount 18 .

vak:KamaDhatuManopavicara
    a logic:Distribution ;
    rdfs:label "desire-realm mental approaches" ;
    logic:inField vak:KamaDhatu ;
    logic:hasSupport vak:OwnAlambana .

vak:OwnAlambana
    a logic:ObjectSupport ;
    rdfs:label "own object-support" ;
    vak:hasSanskrit "svālambana" .

vak:RupaFieldRestriction
    a logic:Distribution ;
    rdfs:label "form-field restriction to twelve" ;
    vak:hasMemberCount 12 ;
    logic:inField vak:RupaDhatu .

vak:Gocara
    a logic:FieldOrRange ;
    rdfs:label "gocara" ;
    vak:hasCanonicalTranslation "field / range" .
```

## Commit Note

Committed VAK_3b / VAkK_3.33.

Established:
- the eighteenfold manopavicāra is distributed by realm and field.
- in the desire realm, the approaches have their own object-supports.
- in the form-related context, the field is restricted to twelve.
- the verse must remain provisional pending Bhāṣya control for the exact mapping.

Logical determination:
VAkK_3.33 shows that mental approach is field-bound and object-support-bound. It does not float freely; it operates within a dhātu/dhyāna field and according to its ālambana/gocara.
