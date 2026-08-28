# VAK_2.42

## 1. Sanskrit (Devanāgarī)

> तथासंज्ञिसमापत्तिर्ध्यानेऽन्त्ये निःसृतीच्छया ।
>
> शुभा उपपद्यवेद्यैव नार्यस्यैकाध्विकाप्यते ॥ २.४२ ॥

## 2. Sanskrit (IAST)

> tathāsaṃjñisamāpattir dhyāne 'ntye niḥsṛtīcchayā /
>
> śubhā upapadyavedyaiva nāryasyaikādhvikāpyate // 2.42 //

## 3. Padaccheda

```text
tathāsaṃjñisamāpattiḥ
                    → tathā asaṃjñi-samāpattiḥ
dhyāne 'ntye         → dhyāne antye
niḥsṛtīcchayā       → niḥsṛti-icchayā
śubhā               → śubhā
upapadyavedyaiva    → upapadya-vedyā eva
nāryasya            → na āryasya
ekādhvikāpyate      → eka-adhvikā āpyate
```

| Form | Morphology | Lexical force here |
|---|---|---|
| tathā | indeclinable | likewise; carries forward the preceding citta-caitta cessation definition |
| asaṃjñi-samāpattiḥ | nominative feminine singular | non-reflective attainment |
| dhyāne antye | locative masculine singular phrase | in the final, fourth dhyāna |
| niḥsṛti-icchayā | instrumental feminine singular compound | through the wish for escape / release |
| śubhā | nominative feminine singular | wholesome |
| upapadya-vedyā | nominative feminine singular | having a result to be experienced in the immediately following rebirth |
| eva | restrictive particle | only / precisely |
| na āryasya | negation with genitive singular | not belonging to a noble person |
| eka-adhvikā | nominative feminine singular | belonging to one temporal mode |
| āpyate | present passive third-person singular | is obtained / acquired |

`Upapadya-vedya` is a technical karmic timing term. It does not mean that
the attainment itself is merely “experienced at rebirth”; its maturation is
fixed for the immediately following existence.

## 4. Grammar

The feminine subject `asaṃjñi-samāpattiḥ` receives a sequence of
predications:

```text
tathā
    → it too is cessation of citta and caittas,
      according to the Bhāṣya

dhyāne antye
    → it belongs to the final dhyāna

niḥsṛti-icchayā
    → it is entered through a wish for release

śubhā
    → it is wholesome

upapadya-vedyā eva
    → its result is fixed for the next rebirth only

na āryasya
    → it does not belong to a noble person

eka-adhvikā āpyate
    → it is acquired in one temporal mode
```

The Bhāṣya identifies the one temporal mode as present acquisition. From
the second moment onward, the practitioner may also possess the past instance
while it remains unrelinquished, but no future instance is cultivated.

## 5. Translation

### Close syntactic construe

> Likewise, the non-reflective attainment occurs in the final dhyāna through the wish for release. It is wholesome, has a result to be experienced only in the immediately following rebirth, does not belong to a noble person, and is acquired in one temporal mode.

### Bhāṣya-informed translation

> Like the non-reflective maturation-state, the non-reflective attainment is a cultivated cessation of consciousness and associated mental factors. It is produced through powerful preparation in the fourth dhyāna by an ordinary practitioner who takes that cessation to be escape. The attainment is wholesome, but its fixed maturation is rebirth among the non-reflective Bṛhatphala beings. Noble persons do not cultivate it because they recognize that state as a place of downfall rather than liberation. Only its present instance is initially acquired.

## 6. Philosophical Translation

> A disciplined attainment may be wholesome, powerful, and non-reflective without being liberating. The decisive question is whether reflection has been fulfilled in Knowledge or merely suppressed. In this Kośa account, the practitioner mistakes the cessation of cognitive operation for release; the result is an exalted but conditioned rebirth rather than entry into the noble Path.

The verse therefore distinguishes ethical quality from rational adequacy:

```text
wholesome cultivation
    ⇏ noble liberation

cessation of reflective operation
    ⇏ possession of the Concept
```

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| asaṃjñi-samāpatti | non-reflective attainment | cultivated state that the Bhāṣya identifies as cessation of citta and caittas |
| āsaṃjñika | non-reflective maturation-state | indeterminate result produced by the wholesome attainment; distinguished from its cause |
| antya-dhyāna | final dhyāna | fourth dhyāna, the only level including this attainment |
| niḥsṛti-icchā | wish for release | motive of practitioners who conceive the state as liberation |
| śubha | wholesome | ethical quality of the intentional attainment, not of its indeterminate maturation-result |
| vipāka | maturation-result | five-aggregate existence among the non-reflective beings |
| upapadya-vedanīya | to be experienced in the immediately following rebirth | fixed timing of the karmic result |
| ārya | noble person | one who does not enter this attainment because its limitation is understood |
| eka-adhvika | belonging to one temporal mode | initially only present acquisition |
| prayogaviśeṣa | powerful special preparation | Bhāṣya condition required to produce the attainment |

The controlled term `non-reflective attainment` must be held together with
the source's doctrinal evaluation. Non-reflective can name either fulfilled
Knowing or suppressed reflection at the project level; the Kośa identifies
this particular attainment by its cause, result, and exclusion from the noble
Path as the latter.

## 8. Logical Determination

The attainment and its result must be typed separately:

```text
AsamjniSamapatti(A) {
    cause: PowerfulPreparation,
    dhyana: Fourth,
    motive: WishForRelease,
    ethicalClass: Wholesome,
    practitionerClass: Ordinary,
    initialAcquisitionTime: Present
}

AsamjnikaResult(R) {
    cause: A,
    resultClass: Maturation,
    ethicalClass: Indeterminate,
    birthLocation: NonReflectiveBrhatphalaRegion
}
```

The causal rule is:

```text
Produces(S, AsamjniSamapatti)
    → NextLifeMaturation(S, AsamjnikaExistence)
```

The Path exclusion is:

```text
NoblePractitioner(S)
    → NOT Cultivates(S, AsamjniSamapatti)

ConceivesAsRelease(S, CittaCaittaCessation)
    ∧ OrdinaryPractitioner(S)
    → MayCultivate(S, AsamjniSamapatti)
```

The temporal acquisition rule is:

```text
InitialPrapti(S, A)
    → PraptiTime = Present

FromSecondMoment(S, A)
    → MayPossess(PastInstance(A))

FuturePrapti(S, A)
    = false
```

The diagnostic rule for the Organon reconstruction is:

```text
NonReflective(State)
    is insufficient to classify liberation.

LiberativeNonReflection(State)
    requires ConceptPossession
       + PathKnowledge
       + FreedomFromConditionedResult
```

The last rule is project-level and does not purport to translate the kārikā.

## 9. Interpretive Note

VAK 2.42 prevents a disastrous inference:

```text
mental cessation → liberation
```

The attainment is disciplined and wholesome. It arises through powerful
preparation at the fourth dhyāna. Nevertheless, its practitioner mistakes a
conditioned suspension for release, and its unavoidable result is another
conditioned existence. Ethical purity of intention does not guarantee that
the intended end has been conceptually understood.

This gives us the precise test for the two senses of non-reflection.

```text
suppressed reflection:
    the operation is stopped
    the Concept is not possessed
    conditioned causality remains

fulfilled reflection:
    mediation has completed itself
    Dharma and its Path are possessed
    Jñāna is immediately available
```

The Kośa passage describes the first. Our discovery that Knowing is
non-reflective describes the second. The shared negative form—reflection is
not presently operating—must not conceal their opposite genesis and result.

The ABC example makes the distinction exact:

```text
forgetting or suppressing the alphabet
    ≠
possessing the alphabet so completely
that renewed reflection is unnecessary
```

This also clarifies `nirodha`. In the present Kośa attainment, `nirodha` is
causal prevention of citta-caitta arising and leads to a maturation-result.
In the transcendental-rational reconstruction, the right `nirodha` is the
completion of reflection in the possessed Concept. The latter interpretation
must not be attributed to Vasubandhu's description of `asaṃjñi-samāpatti`.

For the Kośa Technē, the operational lesson is severe:

```text
disabled process
    ≠ acquired capability

no reflection event
    ≠ Jñāna
```

An Agent must be tested positively for Concept-possession and Path-knowledge,
not classified as knowing merely because reflective search has ceased.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_42
    a vak:Karika ;
    rdfs:label "VAK 2.42" ;
    vak:hasTopic vak:AsamjniSamapatti ;
    vak:belongsTo vak:Indriyanirdesa .

vak:AsamjniSamapatti
    a vak:CittaViprayuktaSamskara ;
    vak:hasControlledRendering "non-reflective attainment" ;
    vak:belongsTo vak:FourthDhyana ;
    vak:hasMotive vak:WishForRelease ;
    vak:hasEthicalClass vak:Wholesome ;
    vak:hasResultTiming vak:NextRebirthOnly ;
    vak:isNotCultivatedBy vak:NoblePractitioner ;
    vak:hasInitialPraptiTime vak:Present .

vak:AsamjnikaMaturation
    a vak:Vipaka ;
    vak:isProducedBy vak:AsamjniSamapatti ;
    vak:hasEthicalClass vak:Indeterminate ;
    vak:hasBirthLocation vak:NonReflectiveBrhatphalaRegion .

organon:LiberativeNonReflection
    a organon:InterpretiveReconstruction ;
    organon:requires organon:ConceptPossession,
        organon:PathKnowledge,
        organon:FreedomFromConditionedResult ;
    organon:isDistinctFrom vak:AsamjniSamapatti .
```
