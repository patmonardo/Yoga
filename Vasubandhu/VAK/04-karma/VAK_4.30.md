# VAK_4.30

## Sanskrit — Devanāgarī

```sanskrit
अन्यस्याप्युपवासोऽस्ति शरणं त्वगतस्य न ।
उपासकत्वोपगमात्संवृत् उक्तिस्तु भिक्षुवत् ॥
```

## Sanskrit — IAST

```iast
anyasyāpy upavāso 'sti śaraṇaṃ tv agatasya na |
upāsakatvopagamāt saṃvṛt uktis tu bhikṣuvat ||
```

## Source reference and caution

Source: `VAkK_4.30`.

The second half is compressed, and the source reads `saṃvṛt uktiḥ`. Its exact construction should be checked against the Bhāṣya. The secure topic is the relation among upavāsa, refuge, upāsaka status, and the verbal undertaking of restraint.

## Padaccheda

```text
anyasya api
upavāsaḥ asti

śaraṇam tu
agatasya na

upāsakatva-upagamāt
saṃvṛt uktiḥ tu
bhikṣu-vat
```

## Literal translation

> Even another person may possess the upavāsa, but not one who has not gone for refuge. From undertaking upāsaka status comes the declaration of restraint, as in the case of a monk.

The second sentence remains provisional pending the Bhāṣya.

## Philosophical translation

> The temporary observance is not confined to someone already established as an upāsaka, but it presupposes orientation through refuge. Becoming an upāsaka is itself an acquired normative status: through undertaking and declaration, the person becomes a bearer of lay restraint, in a structure analogous to monastic admission.

## Technical analysis

### `anyasyāpy upavāso 'sti`

The one-day observance is available even to a person who is not already established in full lay status.

```text
prior upāsaka status
    not necessarily required
```

### `śaraṇaṃ tv agatasya na`

The openness of the observance is qualified: it is not available to one who has not gone for refuge.

```text
refuge
    supplies Path-orientation

upavāsa
    supplies determinate temporary discipline
```

### `upāsakatvopagama`

`upāsakatva` is the acquired status of being an upāsaka. `upagama` indicates entering, accepting, or undertaking that condition.

```text
ordinary person
    → undertaking
    → bearer of lay restraint
    → upāsaka
```

### `saṃvṛt uktiḥ`

The phrase likely concerns the declaration or verbal formula of restraint. It should not be normalized more narrowly until the Bhāṣya is consulted.

### `bhikṣuvat`

The analogy concerns formal status-acquisition, not equality of vow-content:

```text
lay undertaking
    → upāsaka status

monastic undertaking
    → bhikṣu status
```

## Refuge, vow, and practical identity

```text
refuge
    universal Path-orientation

vow
    particular discipline

upāsaka
    singular bearer of the discipline
```

The vow does not merely modify an already complete person. A transient act of undertaking establishes a persistent practical identity.

## Doctrinal determination

1. Upavāsa is not restricted to one already established as an upāsaka.
2. Going for refuge is nevertheless required.
3. Upāsaka status is entered through a formal undertaking.
4. The acquired restraint determines a continuing practical identity.

## Relation to VAK_4.26–4.29

```text
VAK_4.26
    prātimokṣa is acquired through interpersonal procedure

VAK_4.27
    restraint may be lifelong or one day and night

VAK_4.28
    concrete procedure of upavāsa undertaking

VAK_4.29
    functional classification of its eight limbs

VAK_4.30
    eligibility, refuge, and lay status
```

## Light Organon interpretation

A normative status arises through orientation, recognition, undertaking, and continuing obligation. Speech institutes a form that reorganizes future activity.

```text
speech-act
    → acquired restraint
    → persistent karmic form
    → practical status
```

## OWL++ seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_30
    a vak:Karika ;
    rdfs:label "VAK 4.30" ;
    vak:continues vak:VAK_4_29 ;
    vak:hasTopic vak:EligibilityRefugeAndLayStatus .

vak:UpavasaCandidate
    vak:needNotAlreadyPossess vak:UpasakaStatus ;
    vak:requires vak:GoingForRefuge .

vak:UpasakaStatus
    vak:isAcquiredThrough vak:LayStatusUndertaking ;
    vak:includesPossessionOf vak:LayRestraint .
```

## Verse summary

```text
Upavāsa is open beyond already established lay followers,
but not apart from refuge.

Refuge supplies orientation.
Undertaking supplies restraint.
Restraint establishes upāsaka status.
```
