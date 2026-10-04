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

> The attainment is wholesome, but its result is an indeterminate maturation
> in the immediately following rebirth. Practitioners enter it with a wish
> for release and regard it as an escape; noble persons instead see it as
> a place of downfall. The Bhāṣya keeps their motive and the result distinct from the
> attainment's ethical quality.

**Organon reading (limited):** Do not infer liberation from cessation alone.
Here the Bhāṣya distinguishes the practitioners' intended escape from the
conditioned result it describes.

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
| ārya | noble person | does not enter the attainment, seeing it as a place of downfall |
| eka-adhvika | belonging to one temporal mode | initially only present acquisition |
| mahābhisaṃskāra | great formative effort | required for producing the attainment |

The project's controlled term “non-reflective attainment” does not replace
the Bhāṣya's explicit description: cessation of consciousness and mental
factors, produced through great effort and understood by its practitioners
as release.

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

FutureInstanceCultivation(A)
    = false
```

## 9. Interpretive Note

The Bhāṣya distinguishes the practitioners' wish for release from the
attainment's result and from the noble persons' assessment of it as a place
of downfall. It also distinguishes present acquisition, subsequent possession
of the past instance, and the non-cultivation of a future instance.

**Organon note (limited):** Keep these distinctions within the existing
*Prāpti:Aprāpti* vocabulary. The passage does not equate this conditioned
attainment with liberation or generalize its account to the attainment of
cessation discussed next.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
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
    vak:hasMaturationTiming vak:NextRebirthOnly ;
    vak:isNotCultivatedBy vak:NoblePractitioner ;
    vak:hasInitialPraptiTime vak:Present .

vak:AsamjnikaMaturation
    a vak:Vipaka ;
    vak:isProducedBy vak:AsamjniSamapatti ;
    vak:hasEthicalClass vak:Indeterminate ;
    vak:hasBirthLocation vak:NonReflectiveBrhatphalaRegion .

```

## 11. Review Status

Provisional paired study. The kārikā and Bhāṣya are reviewed against the
printed passage at 68.28–69.23. VAK 2.43 begins at 69.24.
