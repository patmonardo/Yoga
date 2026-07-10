# VAK_4.02 — Manifest and Non-Manifest Karma

## 1. Sanskrit — Devanāgarī

```sanskrit
ते तु विज्ञप्त्यविज्ञप्ती कायविज्ञप्तिरिष्यते ।
संस्थानं न गतिर्यस्मात् संस्कृतं क्षणिकं व्ययात् ॥
```

## 2. Sanskrit — IAST

```iast
te tu vijñapty-avijñaptī kāya-vijñaptir iṣyate |
saṃsthānaṃ na gatir yasmāt saṃskṛtaṃ kṣaṇikaṃ vyayāt ||
```

## 3. Source Caution

```iast
te tu vijñaptyavijñaptī kāyavijñaptiriṣyate /
saṃsthānaṃ na gatiryasmātsaṃskṛtaṃ kṣaṇikaṃ vyayāt // VAkK_4.2 //
```

Light separation:

```iast
te tu vijñapti-avijñaptī |
kāya-vijñaptiḥ iṣyate saṃsthānam, na gatiḥ |
yasmāt saṃskṛtaṃ kṣaṇikaṃ vyayāt ||
```

The verse first distinguishes manifest and non-manifest modes of bodily and verbal karma, then determines bodily manifestation as configuration rather than enduring motion.

## 4. Padaccheda

| Sandhi / Compound | Padaccheda | Notes |
|---|---|---|
| vijñaptyavijñaptī | vijñapti-avijñaptī | manifestation and non-manifestation |
| kāyavijñaptiḥ | kāya-vijñaptiḥ | bodily manifestation |
| saṃsthānam | saṃsthānam | configuration / spatial articulation |
| gatir | gatiḥ | motion / going |
| yasmāt | yasmāt | because |
| saṃskṛtam | saṃskṛtam | the conditioned |
| kṣaṇikam | kṣaṇikam | momentary |
| vyayāt | vyayāt | because of perishing |

## 5. Grammar

`te` is neuter nominative dual and refers back to verbal and bodily karma in VAK_4.01. `vijñapty-avijñaptī` names two modes of produced action rather than assigning speech and body one-to-one to the two terms.

```text
verbal and bodily karma
    → vijñapti
    → avijñapti
```

`kāya-vijñaptir iṣyate saṃsthānam` means that bodily manifestation is held to be configuration. `iṣyate` marks a doctrinally maintained position.

`na gatiḥ` rejects motion understood as one enduring conditioned entity traversing successive positions.

`yasmāt saṃskṛtaṃ kṣaṇikaṃ vyayāt` gives the ground: whatever is conditioned is momentary because it perishes.

## 6. Literal Translation

Those two are manifestation and non-manifestation. Bodily manifestation is held to be configuration, not motion, because the conditioned is momentary owing to its perishing.

## 7. Philosophical Translation

Verbal and bodily action are differentiated into manifest and non-manifest action. Bodily manifestation is doctrinally determined as a spatial configuration rather than as an enduring movement, since every conditioned determination perishes within the moment.

## 8. Technical Vocabulary

| Sanskrit | Working Translation | Determination |
|---|---|---|
| vijñapti | manifestation / making-known | expressive mode of action |
| avijñapti | non-manifest action | effective action-determination without present expression |
| kāya-vijñapti | bodily manifestation | bodily expressive action |
| saṃsthāna | configuration | determinate bodily arrangement |
| gati | motion / going | continuous transit of an identical mover |
| saṃskṛta | conditioned | dependently produced determination |
| kṣaṇika | momentary | existing for one moment |
| vyaya | perishing | dissolution of the present conditioned determination |

`vijñapti` derives from the semantic field of making distinctly known. It must not be collapsed into `vijñāna`:

```text
vijñāna
    knowledge

vijñapti
    making-known / manifestation
```

`avijñapti` does not mean mere absence. It names a karmically effective determination that does not presently manifest itself perceptibly.

## 9. Doctrinal Determination

VAK_4.01 classified action by domain:

```text
mental
verbal
bodily
```

VAK_4.02 introduces a second axis, the mode of karmic existence:

```text
manifest
non-manifest
```

Thus the chapter moves from where action occurs to how action exists and remains effective.

## 10. Logical Determination

The compact inference is:

```text
all conditioned determinations are momentary

motion would require
    one and the same mover
    to persist through successive locations

but the conditioned determination at the first location perishes

therefore bodily manifestation
    is not one enduring motion
    but a succession of momentary configurations
```

Conventionally:

```text
A → B → C
```

Ontologically:

```text
A | B | C
```

## 11. Interpretive Note

The verse does not deny phenomenal change. It denies that movement is a single enduring conditioned entity. What is real at each moment is a determinate configuration.

This creates the central problem of karmic continuity:

```text
vijñapti
    is momentary and perishes

karma
    remains effective after the manifestation has ceased
```

The doctrine of `avijñapti` is introduced within this pressure, although its exact status must be determined by the following verses.

## 12. Organon Interpretation

The text currently supports only a light determination:

```text
cetanā
    inward action-determination

vijñapti
    momentary expressive configuration

avijñapti
    non-manifest karmic mode
```

A stronger account of persistence should wait for the succeeding verses.

## 13. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_02
    a vak:Karika ;
    rdfs:label "VAK 4.02" ;
    vak:sourceReference "VAkK_4.2" ;
    vak:continues vak:VAK_4_01 ;
    vak:hasTopic vak:Vijnapti ;
    vak:hasTopic vak:Avijnapti ;
    vak:hasTopic vak:MomentaryBodilyManifestation .

vak:ProducedKarma
    a logic:ActionDetermination ;
    vak:hasMode vak:Vijnapti ;
    vak:hasMode vak:Avijnapti .

vak:KayaVijnapti
    a vak:Vijnapti ;
    vak:hasDeterminateForm vak:Samsthana ;
    vak:notIdenticalWith vak:Gati .

vak:Samsthana
    a logic:MomentaryConfiguration ;
    rdfs:label "bodily configuration" .
```

## 14. Commit Note

Committed VAK_4.02.

Established:
- verbal and bodily karma have manifest and non-manifest modes.
- bodily manifestation is held to be configuration rather than enduring motion.
- conditioned determinations are momentary because they perish.
- the precise continuity-function of non-manifest karma remains open for the following verses.
