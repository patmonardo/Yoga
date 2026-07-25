# VAK_4d — VAkK_4.68

## 1. Sanskrit — Devanāgarī

सामन्तकास्तु विज्ञप्तिरविज्ञप्तिर्भवेन्न वा ।
विपर्ययेण पृष्ठानि प्रयोगस्तु त्रिमूलजः ॥ VAkK_4.68 ॥

## 2. Sanskrit — IAST

sāmantakās tu vijñaptir avijñaptir bhaven na vā /
viparyayeṇa pṛṣṭhāni prayogas tu trimūlajaḥ // VAkK_4.68 //

## 3. Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| sāmantakāḥ | sāmantakāḥ | proximate or preliminary actions |
| tu | tu | but; now |
| vijñaptiḥ | vijñaptiḥ | manifest action |
| avijñaptiḥ | avijñaptiḥ | non-manifest determination |
| bhavet | bhavet | may be; may occur |
| na vā | na vā | or may not |
| viparyayeṇa | viparyayeṇa | conversely; in reverse manner |
| pṛṣṭhāni | pṛṣṭhāni | subsequent actions; aftermath |
| prayogaḥ | prayogaḥ | preparatory undertaking |
| tri-mūla-jaḥ | tri-mūla-jaḥ | born from the three roots |

Provisional syntax:

```text
sāmantakāḥ tu
    vijñaptiḥ

avijñaptiḥ
    bhavet vā
    na vā

pṛṣṭhāni
    viparyayeṇa

prayogaḥ tu
    tri-mūla-jaḥ
```

## 4. Grammar

- `sāmantakāḥ`: masculine nominative plural, adjoining or proximate actions.
- `vijñaptiḥ`: feminine nominative singular, manifest action.
- `avijñaptiḥ`: feminine nominative singular, non-manifest karmic determination.
- `bhavet`: optative third-person singular of `bhū`, “may be.”
- `viparyayeṇa`: instrumental singular, “conversely.”
- `pṛṣṭhāni`: neuter nominative plural, subsequent actions.
- `prayogaḥ`: masculine nominative singular, preparatory application or undertaking.
- `trimūlajaḥ`: masculine nominative singular, born from the three roots.

The proximate actions are manifest; avijñapti may or may not accompany them. The subsequent actions are treated conversely. The preparatory undertaking arises from any of the three unwholesome roots.

## 5. Literal Translation

The proximate actions are manifest action; non-manifest action may or may not occur. Subsequent actions are the reverse. The preparatory undertaking arises from the three roots.

## 6. Philosophical Translation

A completed karmic course is surrounded by preparatory and subsequent phases. Its preparation is outwardly enacted, though it need not always establish a persistent non-manifest determination. The aftermath has the converse modal structure. The preparatory undertaking may be driven by greed, hatred, or delusion.

```text
preparation
    ↓
principal act
    ↓
aftermath
```

## 7. Technical Vocabulary

### sāmantaka

A proximate or adjoining action near the principal karmic course.

### vijñapti

Manifest action: an outwardly expressive bodily or verbal act.

### avijñapti

A persistent non-manifest karmic determination. The verse states that it may or may not arise from the preliminary phase.

### pṛṣṭha

Literally what is behind or follows. Here: subsequent action, posterior phase, or aftermath.

### viparyayeṇa

Conversely or in reverse manner. The exact modal reversal remains for Bhāṣya confirmation.

### prayoga

Preparatory undertaking, intentional engagement, or application leading toward the principal act.

### trimūlaja

Born from the three unwholesome roots:

```text
lobha    greed
dveṣa   hatred
moha    delusion
```

## 8. Doctrinal Determination

The karmic course has three moments:

```text
1. prayoga / sāmantaka
    preparation or proximate action

2. maula
    principal act

3. pṛṣṭha
    subsequent action
```

The preliminary phase is necessarily manifest and may additionally establish avijñapti. The posterior phase is distributed conversely; the precise distribution remains open pending the Bhāṣya.

The preparation may arise from greed, hatred, or delusion. The motive governing preparation need not be identical with the root characteristically governing completion.

## 9. Logical Determination

The verse converts karma from a punctual event into a temporally structured process.

```text
before
    preparation

during
    principal completion

after
    posterior continuation
```

Each phase may have a distinct manifestation mode, causal root, ethical force, and relation to completion.

```text
visible preparation
    does not necessarily imply
stable karmic persistence
```

The same outward preparation may arise from different motivational grounds. Moral evaluation must therefore distinguish event morphology from motivational genesis.

## 10. Light Organon Interpretation

```text
Orientation
    ↓
Preparation
    ↓
Execution
    ↓
Completion
    ↓
Aftermath
    ↓
Persistent state
```

A moral processor must inspect what prepared the act, what completed it, what followed it, what persisted from it, and which root generated each phase.

```text
MoralProcess
    hasPreparation
    hasPrincipalAct
    hasAftermath
    hasMotivationalRoot
    hasManifestEvent
    hasPersistentDisposition
```

The main insight is that moral identity belongs to a process, not merely to a terminal event.

## 11. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_68
    a vak:Karika ;
    rdfs:label "VAkK 4.68" ;
    vak:continues vak:VAK_4_67 ;
    vak:hasTopic vak:KarmicProcessPhases,
                 vak:PreparatoryRoots .

vak:KarmicProcess
    a logic:Process ;
    vak:hasPhase vak:PreparatoryPhase,
                 vak:PrincipalPhase,
                 vak:SubsequentPhase .

vak:PreparatoryPhase
    rdfs:label "prayoga / sāmantaka" ;
    vak:necessarilyHasMode vak:ManifestRealization ;
    vak:optionallyHasMode vak:NonManifestRealization .

vak:PrincipalPhase
    rdfs:label "maula" .

vak:SubsequentPhase
    rdfs:label "pṛṣṭha" ;
    vak:hasModalRelation vak:ConverseDistribution .

vak:Greed rdfs:subClassOf vak:UnwholesomeRoot ; rdfs:label "lobha" .
vak:Hatred rdfs:subClassOf vak:UnwholesomeRoot ; rdfs:label "dveṣa" .
vak:Delusion rdfs:subClassOf vak:UnwholesomeRoot ; rdfs:label "moha" .

vak:PreparatoryPhase
    vak:mayAriseFrom vak:Greed,
                     vak:Hatred,
                     vak:Delusion .
```

## 12. Commit Note

Committed VAK_4d / VAkK_4.68.

Established:
- preparatory, principal, and subsequent phases
- preparation as manifest and optionally non-manifest
- converse distribution for posterior actions, pending Bhāṣya clarification
- preparatory undertaking from greed, hatred, or delusion
- separation of temporal phase, manifestation mode, and motivational root

```text
karma
    is not an isolated event

karma
    is a temporally articulated process
```
