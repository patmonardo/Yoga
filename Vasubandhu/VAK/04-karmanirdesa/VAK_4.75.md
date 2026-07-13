# VAK_4.75

## 1. Sanskrit — Devanāgarī

चक्षुःश्रोत्रमनश्चित्तैरनुभूतं त्रिभिश्च यत् ।  
तद्दृष्टश्रुतविज्ञातं मतं चोक्तं यथाक्रमम् ॥ ४.७५ ॥

## 2. Sanskrit — IAST

**cakṣuḥ-śrotra-manaś-cittair anubhūtaṃ tribhiś ca yat |**  
**tad dṛṣṭa-śruta-vijñātaṃ mataṃ coktaṃ yathākramam || 4.75 ||**

Source text:

```text
cakṣuḥ śrotamanaścittairanubhūtaṃ tribhiśca yat /
taddaṣṭaśrutavijñātaṃ mataṃ coktaṃ yathākramam //
```

The source form `taddaṣṭa-` is normalized as `tad dṛṣṭa-`.

## 3. Padaccheda

```text
cakṣuḥ
śrotram
manaḥ
cittaiḥ
anubhūtam
tribhiḥ
ca
yat
tat
dṛṣṭam
śrutam
vijñātam
matam
ca
uktam
yathākramam
```

The verse establishes a technical correspondence among modes of acquisition and the predicates **seen**, **heard**, **known**, and **thought**. The exact internal distribution of `manas`, `citta`, and `tribhiḥ` remains for the Bhāṣya pass.

## 4. Grammar

- **cakṣuḥ** — eye.
- **śrotram** — ear.
- **manaḥ** — mind.
- **cittaiḥ** — instrumental plural: by moments or series of knowledge.
- **anubhūtam** — experienced; encountered through a determinate route.
- **tribhiḥ** — by the three; compressed technical reference requiring Bhāṣya confirmation.
- **dṛṣṭam** — seen.
- **śrutam** — heard.
- **vijñātam** — known.
- **matam** — thought or mentally considered.
- **uktam** — called or designated.
- **yathākramam** — respectively, in the stated order.

The verse is not merely listing private states. It fixes the correct predicates for distinct epistemic relations.

## 5. Literal Translation

> Whatever has been experienced through the eye, ear, mind, and through the relevant three modes of knowledge is called, respectively, seen, heard, known, and thought.

Because the compact syntax remains partly dependent on the Bhāṣya, the exact one-to-one allocation is provisional.

## 6. Philosophical Translation

> The predicates “seen,” “heard,” “known,” and “thought” designate distinct practical relations through which an object has been acquired. A truthful assertion must represent not only its content but also the actual mode by which the speaker stands in relation to that content.

The verse therefore gives a taxonomy of claims:

```text
I saw it
I heard it
I know it
I thought it
```

Each claim is licensed only by the corresponding acquisition route.

## 7. Technical Vocabulary

### anubhūta

Experienced or actually encountered through a determinate route.

### dṛṣṭa

Seen: acquired through visual relation.

### śruta

Heard: acquired through auditory relation.

### vijñāta

Known. Following the project rule, `vijñāna` is knowledge, never consciousness.

### mata

Thought, considered, or mentally apprehended. It need not possess the force of established knowledge.

### yathākramam

Respectively. The mode of acquisition governs the permissible epistemic predicate.

## 8. Doctrinal Determination

VAK_4.74 defined false speech through a contradiction between the speaker’s recognition and the statement understood by another. VAK_4.75 specifies the possible standing of that recognition:

```text
seen
heard
known
thought
```

Falsehood can therefore concern not only the object asserted, but also:

```text
the acquisition route
the certainty-status
the speaker’s actual relation to the matter
```

Thus a speaker may falsely claim direct perception for hearsay, knowledge for mere consideration, or observation for inference.

## 9. Logical Determination

The central rule is:

```text
AcquisitionMode(x)
    determines
AssertibleStatus(x)
```

A semantic violation occurs when:

```text
actual acquisition-mode
    ≠
asserted acquisition-mode
```

A proposition may be materially true while the speaker’s claim remains deceptive. If `P` is true, but the speaker says “I saw P” without having seen it, the proposition and the speaker’s asserted epistemic relation must be evaluated separately.

Truthfulness therefore requires both:

```text
object accuracy
self-location within the epistemic relation
```

## 10. Light Organon Interpretation

The verse provides an epistemic-provenance model for a Rational Agent:

```text
Claim
    hasContent
    hasAcquisitionMode
    hasSource
    hasConfidenceStatus
    hasAssertedStatus
```

The practical rule is:

```text
assert only the status
licensed by the acquisition path
```

This is not Rational Psychology. It does not ask which hidden faculty contains a representation. It asks what entitlement the agent possesses to assert a content under a given description.

```text
object
    ↓
mode of acquisition
    ↓
licensed description
    ↓
communicable claim
```

False speech breaks faith with that provenance chain.

## 11. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_75
    a vak:Karika ;
    rdfs:label "VAkK 4.75" ;
    vak:continues vak:VAK_4_74 ;
    vak:hasTopic vak:EpistemicProvenance,
                 vak:TruthfulAssertion .

vak:VisualAcquisition
    rdfs:subClassOf vak:AcquisitionMode ;
    vak:licensesStatus vak:Seen .

vak:AuditoryAcquisition
    rdfs:subClassOf vak:AcquisitionMode ;
    vak:licensesStatus vak:Heard .

vak:KnowledgeAcquisition
    rdfs:subClassOf vak:AcquisitionMode ;
    vak:licensesStatus vak:Known .

vak:MentalConsideration
    rdfs:subClassOf vak:AcquisitionMode ;
    vak:licensesStatus vak:Thought .

vak:TruthfulAssertion
    vak:requiresMatchBetween
        vak:ActualAcquisitionMode,
        vak:AssertedEpistemicStatus .

vak:FalseEpistemicClaim
    rdfs:subClassOf vak:FalseSpeech ;
    vak:hasCondition vak:ProvenanceStatusMismatch .
```

Rule seed:

```text
ActualStatus(agent, P, S1)
and AssertedStatus(agent, P, S2)
and S1 != S2
and RecipientUnderstands(P)
    -> FalseEpistemicClaim(agent, P)
```

## 12. Commit Note

```text
VAK_4.75 — Define epistemic provenance for truthful assertion

- distinguish seen, heard, known, and thought
- correlate each predicate with a determinate acquisition route
- treat these as practical claim-statuses rather than faculties
  of a rational psychology
- extend false speech to misrepresentation of epistemic standing
- distinguish propositional truth from truthful provenance
- establish semantic integrity as correspondence between
  actual acquisition and asserted status
```

### First-pass determination

```text
object acquired through a determinate route
    ↓
licensed epistemic predicate
```

```text
actual route
    ≠
asserted route
        ↓
false speech
```

Truthfulness requires not only saying what is the case, but honestly representing how one stands in relation to what is said.
