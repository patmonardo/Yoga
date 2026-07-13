# VAK_4d — VAkK_4.74

## 1. Sanskrit — Devanāgarī

अगम्यगमनं काममिथ्याचारश्चतुर्विधः ।
अन्यथासंज्ञिनो वाक्यमर्थाभिज्ञे मृषावचः ॥ ४.७४ ॥

## 2. Sanskrit — IAST

agamyagamanaṃ kāmamithyācāraś caturvidhaḥ /
anyathāsaṃjñino vākyam arthābhijñe mṛṣāvacaḥ // VAkK_4.74 //

## 3. Padaccheda

- a-gamya-gamanam — going to one who should not be approached
- kāma-mithyā-ācāraḥ — wrong conduct in the sexual domain
- catur-vidhaḥ — fourfold
- anyathā-saṃjñinaḥ — of one whose recognition is otherwise
- vākyam — statement
- artha-abhijñe — to one understanding the meaning
- mṛṣā-vacaḥ — false speech

Expanded syntax:

```text
agamya-gamanam
    kāma-mithyācāraḥ

saḥ
    caturvidhaḥ

anyathā-saṃjñinaḥ vākyam
    arthābhijñe
    mṛṣāvacaḥ
```

## 4. Grammar

`agamya-gamanam` is neuter nominative singular and predicates the principal form of sexual misconduct. `kāma-mithyācāraḥ` is masculine nominative singular; `caturvidhaḥ` agrees with it. `anyathā-saṃjñinaḥ` is genitive singular, qualifying `vākyam`: the utterance of one whose inward recognition differs from what is said. `arthābhijñe` is locative singular, used relationally for the hearer who understands the meaning. `mṛṣāvacaḥ` is neuter nominative singular.

## 5. Literal Translation

Going to one who should not be approached is sexual misconduct, and it is fourfold. The statement of one whose recognition is otherwise, addressed to one who understands its meaning, is false speech.

## 6. Philosophical Translation

Sexual misconduct is activity that violates the determinate conditions under which a sexual relation is permissible; the text classifies this violation as fourfold. False speech occurs when an agent knowingly expresses something contrary to their own recognition and successfully communicates that contrary meaning to another.

```text
sexual misconduct
    = corruption of embodied interpersonal relation

false speech
    = corruption of semantic relation
```

## 7. Technical Vocabulary

### agamya

Relationally impermissible as an object of sexual approach; not an assertion of intrinsic impurity.

### kāma-mithyācāra

Wrongly conducted sexual activity. The defect is not sexuality as such, but violation of the law governing the relation.

### caturvidha

Fourfold. The exact fourfold classification is deferred to the Bhāṣya; a provisional grouping concerns person, bodily mode, place, and time.

### saṃjñā

Recognition or designation. Here it is the speaker’s inward apprehension of the matter.

### vākya

A meaning-bearing statement, not sound alone.

### artha

Meaning.

### mṛṣāvacas

False speech: semantic expression contrary to the speaker’s own recognition.

## 8. Doctrinal Determination

Sexual misconduct is determined through violation of the constitutive conditions of a permissible sexual relation. False speech requires:

```text
speaker recognizes P
speaker states contrary-to-P
hearer understands the stated meaning
```

The principal verbal course is therefore not completed merely by producing false sounds. It requires successful semantic transmission.

This gives a sequence:

```text
contrary recognition
    ↓
deceptive utterance
    ↓
meaning understood by hearer
    ↓
completed false speech
```

## 9. Logical Determination

Sexual misconduct is relational misapplication: an activity is performed under conditions that invalidate its practical determination.

False speech is a doubled representation:

```text
inward recognition
    ≠
outward statement
```

and becomes practically effective through the hearer’s comprehension. The completed act therefore relates three poles:

```text
speaker’s recognition
statement
hearer’s understanding
```

Verbal karma is semantic action.

## 10. Light Organon Interpretation

A practical processor must distinguish factual error from deception.

```text
speaker believes false content and states it
    = error, not necessarily lying

speaker recognizes one content but states another
    = deceptive contradiction
```

False speech requires comparison among:

```text
BeliefState
MessageContent
RecipientComprehension
```

The reusable practical form is:

```text
recognized governing relation
    deliberately violated
through enacted expression
```

This should be treated as Pure Practical Reason: recognition, statement, and reception are functional moments in the determination of an act, not entities in a rational psychology.

## 11. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_74
    a vak:Karika ;
    rdfs:label "VAkK 4.74" ;
    vak:defines vak:SexualMisconduct, vak:FalseSpeech .

vak:SexualMisconduct
    rdfs:subClassOf vak:BodilyUnwholesomeKarmicCourse ;
    vak:hasModeCount 4 ;
    vak:requiresViolationOf vak:SexualRelationConstraint ;
    vak:hasCompletionRoot vak:Greed .

vak:FalseSpeech
    rdfs:subClassOf vak:VerbalUnwholesomeKarmicCourse ;
    vak:requiresSpeakerState vak:RecognitionContraryToStatement ;
    vak:requiresRecipientState vak:UnderstandingOfMeaning .

vak:RecognitionContraryToStatement
    a logic:SemanticContradiction .
```

Rule seed:

```text
Recognizes(speaker, P)
and Expresses(speaker, Q)
and ContraryMeaning(P, Q)
and Understands(hearer, Q)
    -> CompletedFalseSpeech(speaker, hearer)
```

## 12. Commit Note

VAK_4.74 — Define sexual misconduct and false speech.

Established:
- sexual misconduct as violation of governing relational conditions
- fourfoldness preserved for Bhāṣya determination
- false speech as contradiction between recognition and statement
- hearer comprehension as a completion condition
- distinction between factual error and intentional deception
- verbal karma as semantic practical action
