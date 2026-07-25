# VAK 5.44

## Sanskrit

अगन्तुकामता मार्गविभ्रमो मार्गसंशयः ।
इत्यन्तराया मोक्षस्य गमनेऽतस्त्रिदेशना ॥ ५.४४ ॥

## IAST

agantukāmatā mārgavibhramo mārgasaṃśayaḥ /
ity antarāyā mokṣasya gamane 'tas trideśanā // 5.44 //

## Padaccheda

agantukāmatā | mārga-vibhramaḥ | mārga-saṃśayaḥ | iti | antarāyāḥ | mokṣasya | gamane | ataḥ | tri-deśanā

## Grammar

- **agantukāmatā** — feminine nominative singular abstract noun: **a-gantu-kāmatā**, “not wanting to go,” “unwillingness to proceed.” The negative prefix qualifies the desiderative sense attached to √gam.
- **mārga-vibhramaḥ** — masculine nominative singular, “deviation from the path,” “confusion regarding the path,” or “wandering onto another path.”
- **mārga-saṃśayaḥ** — masculine nominative singular, “doubt concerning the path.”
- **iti** — closes the enumeration: “thus.”
- **antarāyāḥ** — masculine nominative plural, “obstacles,” “impediments,” “intervening hindrances.”
- **mokṣasya gamane** — locative construction, “in the going toward liberation,” “with respect to progress to liberation.”
- **ataḥ** — “therefore,” marking the reason for the threefold teaching.
- **tri-deśanā** — feminine nominative singular, “the threefold teaching,” or “the teaching of three.”

## Literal Translation

Unwillingness to go, deviation from the path, and doubt concerning the path—these are obstacles in going toward liberation; therefore there is the teaching of three.

## Philosophical Translation

The three lower fetters are taught separately because they obstruct liberation in three distinct ways: one refuses the movement, one mistakes another route for the path, and one remains undecided about the path itself.

## Structural Analysis

VAK 5.43 distinguished the five lower fetters into:

```text
2 fetters
    preventing transcendence of the desire-domain

3 fetters
    producing return to the lower position
```

VAK 5.44 now explains why the latter three are especially singled out. They do not merely produce suffering within a domain. They interfere with the movement of liberation itself.

The Bhāṣya maps them as follows:

| Obstacle | Fetter | Operation |
|---|---|---|
| **agantukāmatā** | **satkāyadṛṣṭi** | fear of liberation produces unwillingness to go |
| **mārga-vibhrama** | **śīlavrataparāmarśa** | grasping another discipline or observance produces deviation from the path |
| **mārga-saṃśaya** | **vicikitsā** | doubt leaves the path undecided |

The three are therefore not interchangeable defects. They obstruct three successive conditions of purposive movement:

```text
willingness to depart
    ↓
correct orientation
    ↓
decisive continuation
```

## Technical Vocabulary

### Agantukāmatā

The unwillingness to go. The affliction does not merely block an external action; it prevents the very adoption of liberation as one’s direction. According to the Bhāṣya, **satkāyadṛṣṭi** makes liberation appear threatening because the imagined self fears its own dissolution.

### Mārga-vibhrama

Deviation, confusion, or wandering with respect to the path. This is not simple ignorance of the destination. A route is positively adopted, but it is the wrong route. **Śīlavrataparāmarśa** turns a conditioned practice, vow, or observance into an absolute means of liberation.

### Mārga-saṃśaya

Doubt regarding the path. The path may have been presented, but cognition does not determinately assent to it. **Vicikitsā** suspends practical movement by withholding decision.

### Antarāya

An obstacle that intervenes between an agent and an end. Here the obstacle is defined dynamically: it obstructs **gamana**, the going toward liberation.

### Gamana

Going, proceeding, directed movement. Liberation is not treated here merely as a static object but as the end of a structured path.

## Doctrinal Determination

The verse explains the special doctrinal prominence of three fetters:

```text
satkāyadṛṣṭi
śīlavrataparāmarśa
vicikitsā
```

They are singled out because each attacks one indispensable condition of liberation:

```text
satkāyadṛṣṭi
    attacks the will to leave

śīlavrataparāmarśa
    attacks correct means

vicikitsā
    attacks determination
```

Thus the teaching is path-indexed. The severity of an affliction is measured not only by the distress it causes, but by the exact way it blocks liberative movement.

The structure is:

```text
end
    liberation

movement
    going toward liberation

obstacles
    refusal
    misdirection
    indecision
```

## Logical Determination

VAK 5.44 gives a compact logic of failed purposive action.

A successful path requires at least three determinations:

```text
1. the end is accepted
2. the means is correctly identified
3. the judgment is practically resolved
```

The corresponding failures are:

```text
rejection of the end
misidentification of the means
suspension of decision
```

These are not three degrees of one generic negation. They are three locations at which purposive mediation can break down.

Formally:

```text
acceptsEnd(agent, liberation)
selectsCorrectPath(agent, path)
resolvesToProceed(agent, path)
```

The obstacles negate different predicates:

```text
not acceptsEnd
wrong selectsPath
not resolvesToProceed
```

The verse therefore moves beyond classification by substance. It classifies affliction according to its position within a teleological sequence.

## Organon Note

This verse is highly important for a future Kośa Speculative Reason action model.

A path-capable agent must discriminate at least:

```text
End
Route
Commitment
```

The three afflictions corrupt these as:

```text
EndConflict
RouteError
CommitmentSuspension
```

Possible action-planning pattern:

```text
if liberation is rejected:
    resolve identity-fear

if the route is wrong:
    discriminate valid path from substitute path

if the route is doubted:
    establish sufficient ground for decision
```

This supports an important distinction:

```text
error of desire
    ≠
error of representation
    ≠
error of judgment
```

Pure Prajñā need not itself enter into conflict with the dharmas. Rather, it discriminates the exact point at which the path-process is deformed. The conflict belongs to the determinate path-structure; Prajñā reveals its location and type.

The verse therefore suggests that liberative intelligence is not an undifferentiated intuition of the world. It is a discriminative cognition of:

```text
whether to go
where to go
whether the ground is sufficient to proceed
```

## OWL++ Seed

```ttl
vak:LiberativeObstacle a owl:Class .
vak:UnwillingnessToProceed a owl:Class ;
  rdfs:subClassOf vak:LiberativeObstacle .
vak:PathDeviation a owl:Class ;
  rdfs:subClassOf vak:LiberativeObstacle .
vak:PathDoubt a owl:Class ;
  rdfs:subClassOf vak:LiberativeObstacle .

vak:obstructsEndAcceptance a owl:ObjectProperty .
vak:obstructsCorrectPathSelection a owl:ObjectProperty .
vak:obstructsPracticalResolution a owl:ObjectProperty .

vak:Satkayadrsti
  vak:obstructsEndAcceptance vak:Liberation .

vak:Silavrataparamarsa
  vak:obstructsCorrectPathSelection vak:LiberativePath .

vak:Vicikitsa
  vak:obstructsPracticalResolution vak:LiberativePath .
```

Possible SHACL structure:

```text
LiberativeActionPlan
    requires exactly one accepted End
    requires at least one discriminated Route
    requires one resolved Commitment state
```

A reasoning rule may infer the obstacle-class from the failed planning relation rather than merely from a lexical label.

## Bhāṣya Questions

1. How strongly does **satkāyadṛṣṭi** produce fear of liberation specifically through fear of personal extinction?
2. Does **mārga-vibhrama** primarily mean choosing an entirely different path, or misidentifying a subordinate practice as the complete path?
3. Is **vicikitsā** doubt about the existence of the path, its efficacy, or one’s capacity to follow it?
4. Why are desire and resistance not included among these three immediate obstacles to “going,” although they prevent transcendence of the desire-domain?
5. Does the travel analogy define a general Buddhist theory of action: destination, route, and decision?
6. Can these three failures be mapped cleanly onto desire, representation, and judgment without distorting Vasubandhu’s sequence?

## Commit Note

VAK 5.44 analyzed as the threefold obstruction of liberative movement: unwillingness to depart, deviation from the path, and doubt concerning the path.