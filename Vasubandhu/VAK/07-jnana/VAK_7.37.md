# VAK 7.37 — Knowledge of Resolve and the Four Discriminating Knowledges

## Sanskrit

### Devanāgarī

तथैव प्रणिधिज्ञानं सर्वालम्बं तु तत् तथा ।
धर्मार्थयोर्निरुक्तौ च प्रतिभाने च संविदः ॥ ७.३७ ॥

### IAST

tathaiva praṇidhijñānaṃ sarvālambaṃ tu tat tathā /
dharmārthayor niruktau ca pratibhāne ca saṃvidaḥ // VAK_7.37 //

## Padaccheda

tathā eva | praṇidhi-jñānam | sarva-ālambam | tu | tat | tathā | dharma-arthayoḥ | niruktau | ca | pratibhāne | ca | saṃvidaḥ

## Literal Translation

Knowledge arising from resolve is likewise of the same kind, but it has all things as its object-support. The discriminating knowledges concern dharma, meaning, linguistic explanation, and ready articulation.

## Philosophical Translation

Knowledge governed by resolve shares the general contemplative basis of freedom from conflict, but its possible object-field is unrestricted: according to the practitioner’s deliberate determination, any knowable object may become its support. The four discriminating knowledges are mastery concerning determinations, their meanings, their linguistic expression, and their unobstructed communicative articulation.

## Technical Vocabulary

- **praṇidhi** — deliberate resolve; directed determination.
- **praṇidhi-jñāna** — knowledge arising in conformity with such resolve.
- **sarvālamba** — having all knowable things as possible object-support.
- **saṃvid / pratisaṃvid** — discriminating mastery of a determinate cognitive field.
- **dharma** — determination, classified doctrinal item.
- **artha** — meaning, intended content.
- **nirukti** — exact linguistic explanation and derivation.
- **pratibhāna** — ready, unobstructed, context-sensitive articulation.

## Doctrinal Determination

The verse establishes two architectures of knowledge.

First:

```text
resolve
    ↓
selected object-support
    ↓
knowledge
```

Praṇidhi-jñāna is potentially universal in range, though this does not mean simultaneous omniscience.

Second:

```text
dharma
    determination

artha
    meaning

nirukti
    linguistic expression

pratibhāna
    living articulation
```

The four discriminating knowledges form a movement from intelligible content to successful teaching.

## Logical Determination

Praṇidhi-jñāna answers:

```text
What is to be known?
```

The four pratisaṃvids answer:

```text
How is the known content
determined,
understood,
expressed,
and communicated?
```

The decisive distinction is:

```text
dharma
    articulated determination

artha
    the meaning borne by that determination
```

Dharma without artha becomes empty classification; artha without dharma remains indeterminate content. Their unity is determinate meaning.

## Organon Interpretation

The verse presents a miniature architecture of science:

```text
Object
    ↓
Determination
    ↓
Meaning
    ↓
Language
    ↓
Teaching
```

Knowledge does not automatically contain adequate exposition. The Kośa distinguishes knowing an object from mastering the determinations, meanings, linguistic forms, and communicative acts through which that knowledge becomes available to another rational being.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix lang: <http://127.0.0.1:3000/language#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_37
    a vak:Karika ;
    rdfs:label "VAK 7.37" ;
    vak:determines jna:ResolutionKnowledge,
                   jna:FourDiscriminatingKnowledges .

jna:ResolutionKnowledge
    a jna:ConventionalKnowledge ;
    jna:conditionedBy jna:DeliberateResolve ;
    jna:hasPossibleObjectSupport jna:AllKnowableObjects .

jna:FourDiscriminatingKnowledges
    jna:hasMember jna:DharmaPratisamvid,
                  jna:ArthaPratisamvid,
                  jna:NiruktiPratisamvid,
                  jna:PratibhanaPratisamvid .

jna:DharmaPratisamvid jna:hasDomain jna:Determination .
jna:ArthaPratisamvid jna:hasDomain jna:Meaning .
jna:NiruktiPratisamvid jna:hasDomain lang:LinguisticExplanation .
jna:PratibhanaPratisamvid jna:hasDomain lang:UnobstructedArticulation .
```

## Kārikā-Pass Determination

Knowledge arising from resolve can take any knowable object as its support. The discriminating knowledges then master the determination, its meaning, its linguistic expression, and its living articulation.
