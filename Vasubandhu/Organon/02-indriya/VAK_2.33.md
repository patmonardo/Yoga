# VAK_2.33

## 1. Sanskrit (Devanāgarī)

> वितर्कचारावौदार्यसूक्ष्मते मान उन्नतिः ।
>
> मदः स्वधर्मे रक्तस्य पर्यादानं तु चेतसः ॥ २.३३ ॥

The source assigns the preceding verse the same number. The repository
retains this second source instance as VAK 2.33.

## 2. Sanskrit (IAST)

> vitarkacārāv audāryasūkṣmate māna unnatiḥ /
>
> madaḥ svadharme raktasya paryādānaṃ tu cetasaḥ // 2.33 //

The kārikā's *cāra* is read as *vicāra* in the Bhāṣya, which pairs it with
*vitarka*. The displayed source form is retained.

## 3. Lexical Analysis

```text
vitarkacārāv      → vitarka-cārau [Bhāṣya: vitarka-vicāra]
audāryasūkṣmate   → audārya-sūkṣmate
māna              → mānaḥ
unnatiḥ           → unnatiḥ
madaḥ             → madaḥ
svadharme         → sva-dharme
raktasya          → raktasya
paryādānaṃ        → paryādānam
tu                → tu
cetasaḥ           → cetasaḥ
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| vitarka-cārau | nominative masculine dual | initial and sustained examination; the Bhāṣya reads *vicāra* for *cāra* |
| audārya-sūkṣmate | nominative feminine dual | coarseness and subtlety, respectively |
| mānaḥ | nominative masculine singular | conceit |
| unnatiḥ | nominative feminine singular | elevation of consciousness |
| madaḥ | nominative masculine singular | intoxication |
| sva-dharme | locative singular | with regard to one's own qualities |
| raktasya | genitive singular participial form | of one attached |
| paryādānam | nominative neuter singular | taking-over or complete occupation |
| tu | contrastive particle | however |
| cetasaḥ | genitive neuter singular | of consciousness |

## 4. Scientific English Rendering

> Initial and sustained examination are coarseness and subtlety [of
> consciousness]. Conceit is elevation. Intoxication, however, is the
> taking-over of the consciousness of one attached to one's own qualities.

The Bhāṣya specifies conceit as elevation through a constructed distinction
relative to another. It explains intoxication as the taking-over of
consciousness through attachment to one's own qualities; other teachers
give a distinct alternative definition.

## 5. Interpretation

VAK 2.33 places the proposed distinction between initial and sustained
examination under pressure. Coarseness and subtlety might name the factors
themselves, their effects, or degrees within a kind. The Bhāṣya records
accounts based on joint modulation and speech-formation, objections about
causation and kind, and an alternative that denies momentary coexistence.
It does not resolve these accounts into one uncontested definition.

The closing definitions are more determinate in their relational
distinction. Conceit elevates consciousness through comparison with another;
intoxication takes over consciousness through attachment to one's own
qualities. The alternative definition of intoxication as a particular
exhilaration remains attributed to other teachers.

The Kośa's governing synthesis: Vijñāna is Discriminative Cognition joining
and governing Perception and Conception. Their unity is Inconceivable as a
homogeneous operation; its Idea is disclosed in the Cognition Base. Vijñāna
governs Mind and guides the reading of Dharma Base. Form Base and Dharma
Base both include the same *avijñapti* in distinct classifications, and
Vijñāna bears a *prati* relation to *avijñapti*. This system-level synthesis
does not resolve the local Bhāṣya debate about these factors.

## 6. Logical Determination

The proposed definition:

```text
vitarka = coarseness of consciousness
vicāra  = subtlety of consciousness
```

The balancing analogy proposes joint operation that keeps consciousness
neither excessively coarse nor excessively subtle. The objection distinguishes
conditioning from identity:

```text
Conditions(x, state) does not entail x = state
```

The speech-formation account treats initial and sustained examination as
coarse and subtle formations of speech. Its critics require a difference of
kind, not merely greater or lesser intensity. The separately attributed
non-coexistence account distinguishes attribution by level from occurrence
in one moment:

```text
FirstDhyana has five factors at the level (*bhūmi*)
    does not entail
all five co-occur in every moment (*kṣaṇa*)
```

These are reported positions and objections, not a final adjudication.

## 7. Interpretive Note

The source compares butter under the sun's rays with the proposed
co-operation of initial and sustained examination. The opening wording is
damaged; “cast into water” is a contextual construal supported by the
reply's reference to water and heat. The speech quotation is also defective,
and its negative clause is rendered by its contextual sense.

The first debate moves through distinct tests: whether the factors are
conditions or states, whether relative coarseness and subtlety can define
them across levels, whether speech-formation supplies a common genus, and
whether degree alone establishes a difference of kind. The final
non-coexistence position answers the five-factor objection by applying the
count to the level rather than to each moment. Keep the scope and attribution
of that answer explicit.

## 8. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_33
    a vak:Karika ;
    rdfs:label "VAK 2.33" ;
    vak:hasTopic vak:SelectedMentalFactorDefinitions ;
    vak:belongsTo vak:Indriyanirdesa ;
    vak:hasSourceNumberingIssue vak:DuplicatedSourceVerseNumber .

vak:InitialExamination
    vak:hasProposedCharacter vak:CoarsenessOfConsciousness ;
    vak:isDebatedWith vak:SustainedExamination .

vak:SustainedExamination
    vak:hasProposedCharacter vak:SubtletyOfConsciousness .

vak:Conceit
    vak:elevates vak:Consciousness ;
    vak:usesComparisonWith vak:Other .

vak:Intoxication
    vak:mayCompletelyOccupy vak:Consciousness ;
    vak:hasAlternativeDefinition vak:ParticularExhilaration .
```
