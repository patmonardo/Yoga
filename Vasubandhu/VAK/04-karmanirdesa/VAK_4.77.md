# VAK_4.77

## 1. Sanskrit — Devanāgarī

अतोऽन्यत् क्लिष्टमित्यन्ये लपनागीतनाट्यवत् ।
कुशास्त्रवच्चाभिध्या तु परस्वविषमा स्पृहा ॥ ४.७७ ॥

## 2. Sanskrit — IAST

**ato ’nyat kliṣṭam ity anye lapanā-gīta-nāṭyavat |**  
**kuśāstravac cābhidhyā tu para-sva-viṣamā spṛhā || 4.77 ||**

Local source:

```text
ato 'nyat kliṣṭamityanye lapanāgītanāṭyavat /
kuśāstavacca abhidhyā tu parasvaviṣamaspṛhā // VAkK_4.77 //
```

The source form `kuśāsta-` is provisionally normalized as `kuśāstra-`, pending Bhāṣya and critical-edition confirmation.

## 3. Padaccheda

```text
ataḥ
anyat
kliṣṭam
iti
anye

lapanā-gīta-nāṭya-vat

ku-śāstra-vat
ca

abhidhyā
tu

para-sva
viṣamā
spṛhā
```

Expanded sense:

```text
anye iti āhuḥ:
ataḥ anyat kliṣṭam vacanam
    bhinna-pralāpaḥ

lapanā-gīta-nāṭya-vat
kuśāstravat ca
```

and:

```text
parasve viṣamā spṛhā
    = abhidhyā
```

## 4. Grammar

- **ataḥ anyat** — other than these; the remainder after the specifically defined verbal courses.
- **kliṣṭam** — afflicted, governed by an unwholesome root.
- **iti anye** — “so say others”; an attributed doctrinal opinion.
- **lapanā-gīta-nāṭya-vat** — like chatter, song, or drama.
- **kuśāstravat** — like a bad, corrupt, or defective treatise.
- **abhidhyā** — covetousness.
- **para-sva** — another’s property.
- **viṣamā spṛhā** — improper or distorted longing.

The first half treats disconnected speech as a residual class of afflicted verbal production. The second half defines covetousness through the practical distortion of another’s ownership relation.

## 5. Literal Translation

> Others say that any afflicted speech other than these is disconnected speech, as in chatter, song, drama, and corrupt treatises. Covetousness, however, is an improper longing for another’s property.

## 6. Philosophical Translation

> According to one view, disconnected speech is the residual field of afflicted linguistic production: discourse that may possess grammar, rhythm, narrative, or even systematic form, yet lacks a valid practical orientation toward truth, benefit, or liberation. Covetousness is the distorted practical desire that another’s possession should become one’s own.

The first half establishes:

```text
formal coherence
    ≠
practical-semantic validity
```

The second half distinguishes:

```text
abhidhyā
    prospective appropriation

adattādāna
    completed bodily appropriation
```

## 7. Technical Vocabulary

### lapanā

Conversation, chatter, or purposeless talk. The practical defect depends on afflicted orientation, not mere informality.

### gīta

Song or singing. The qualification `kliṣṭa` prevents an indiscriminate condemnation of all musical form.

### nāṭya

Drama or theatrical presentation. Narrative organization does not by itself establish practical validity.

### kuśāstra

A defective treatise, corrupt doctrine, or invalid systematic discourse. It is especially important because it shows that semantic disorder may acquire highly organized form.

### abhidhyā

Covetousness or acquisitive fixation; one of the three mental unwholesome karmapathas.

### para-sva

What belongs to another.

### viṣama

Uneven, improper, distorted, contrary to proper order.

### spṛhā

Longing or aspiration. Desire becomes covetousness only when directed improperly toward another’s possession.

## 8. Doctrinal Determination

The first half gives a residual classification:

```text
Afflicted verbal activity
    minus false speech
    minus divisive speech
    minus harsh speech
    = disconnected speech
```

This class may include afflicted chatter, song, drama, and even systematic teaching. Therefore `bhinna-pralāpa` is broader than random noise: a discourse can be internally organized yet disconnected from a valid governing end.

Covetousness has the structure:

```text
another possesses O
agent practically desires:
    may O become mine
```

It is not yet bodily theft, but the practical orientation toward wrongful transfer. Both covetousness and theft are characteristically completed through greed.

## 9. Logical Determination

Disconnected speech may contain local coherence without adequate universal integration:

```text
grammar
rhythm
narrative
argument
    without
valid governing practical unity
```

Covetousness is a practical counter-claim against an existing ownership relation:

```text
belongsTo(O, Other)
    ↓ improper positing
oughtToBelongTo(O, Me)
```

The mental course is therefore not a hidden psychological object. It is an incipient practical relation.

## 10. Light Organon Interpretation

A Rational Agent must distinguish surface coherence from semantic grounding, provenance, inferential validity, practical purpose, and relational consequence.

```text
Discourse {
    formalCoherence
    semanticGrounding
    provenance
    practicalPurpose
    inferentialValidity
    relationalEffect
}
```

A fluent and systematic artifact may still be a `kuśāstra`: coherent hallucination, organized semantic drift, or false explanatory closure.

Covetousness can be modeled as an unauthorized projected state transition:

```text
currentOwner = Other
desiredOwner = Self
transferAuthorization = None
appropriationIntent = Active
    → Covetousness
```

Pure Practical Reason asks not what private faculty contains desire, but what practical transition the agent is positing.

## 11. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_77
    a vak:Karika ;
    rdfs:label "VAkK 4.77" ;
    vak:continues vak:VAK_4_76 ;
    vak:hasTopic vak:DisconnectedSpeech,
                 vak:Covetousness .

vak:CorruptTreatise
    rdfs:subClassOf vak:DisconnectedSpeech ;
    rdfs:label "kuśāstra" ;
    vak:mayHaveCondition vak:FormalCoherence ;
    vak:lacksCondition vak:ValidPracticalSemanticOrder .

vak:Covetousness
    rdfs:subClassOf vak:MentalUnwholesomeKarmicCourse ;
    rdfs:label "abhidhyā" ;
    vak:hasObject vak:AnotherPersonsProperty ;
    vak:hasActionForm vak:ImproperAcquisitiveLonging ;
    vak:hasCompletionRoot vak:Greed .
```

Rule seeds:

```text
AfflictedSpeech(?u)
and not FalseSpeech(?u)
and not DivisiveSpeech(?u)
and not HarshSpeech(?u)
    → DisconnectedSpeech(?u)
```

```text
PropertyOf(?object, ?other)
and DesiresAsOwn(?agent, ?object)
and not AuthorizedTransfer(?object, ?agent)
and ImproperAppropriationOrientation(?agent, ?object)
    → Covetousness(?agent, ?object)
```

## 12. Commit Note

```text
VAK_4.77 — Extend disconnected speech and define covetousness

- record the residual definition of disconnected speech
- include afflicted chatter, song, drama, and corrupt treatises
- distinguish formal coherence from practical-semantic validity
- define covetousness as improper longing for another’s property
- distinguish covetous orientation from completed physical theft
- model covetousness as an unauthorized projected transfer
- preserve the mental karmapatha as a practical determination
```

### First-pass determination

```text
disconnected speech
    may be formally coherent

yet disconnected from
a valid governing practical end
```

```text
abhidhyā
    =
improper acquisitive longing
for what belongs to another
```

The central Rational Agent result is:

```text
semantic form is not enough

a fluent, ordered, systematic artifact
may still be practically irrational
if its production lacks:
    grounding
    valid purpose
    truthful relation
    and governed consequence
```