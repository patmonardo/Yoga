# VAK_2.25 — The Wholesome Great-Ground Factors

## 1. Sanskrit (Devanāgarī)

> श्रद्धाप्रमादः प्रश्रब्धिरुपेक्षा ह्रीरपत्रपा ।
>
> मूलद्वयमहिंसा च वीर्यं च कुशले सदा ॥ २.२५ ॥

## 2. Sanskrit (IAST)

> śraddhāpramādaḥ praśrabdhir upekṣā hrīr apatrapā /
>
> mūladvayam ahiṃsā ca vīryaṃ ca kuśale sadā // 2.25 //

The Bhāṣya resolves the first sandhi as *śraddhā apramādaḥ*: confidence
and heedfulness. It is not parsed as *śraddhā-pramādaḥ*, “confidence and
negligence.”

## 3. Lexical Analysis

```text
śraddhāpramādaḥ → śraddhā apramādaḥ
praśrabdhir     → praśrabdhiḥ
upekṣā          → upekṣā
hrīr            → hrīḥ
apatrapā        → apatrapā
mūladvayam      → mūla-dvayam
ahiṃsā ca       → ahiṃsā ca
vīryaṃ ca       → vīryam ca
kuśale          → kuśale
sadā            → sadā
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| śraddhā | nominative feminine singular | confidence |
| a-pramādaḥ | nominative masculine singular privative formation | heedfulness |
| praśrabdhiḥ | nominative feminine singular | pliancy or workability |
| upekṣā | nominative feminine singular | equanimity |
| hrīḥ | nominative feminine singular | moral shame |
| apatrapā | nominative feminine singular | moral caution |
| mūla-dvayam | nominative neuter singular compound | the pair of wholesome roots |
| ahiṃsā | nominative feminine singular | non-harming |
| vīryam | nominative neuter singular | energy |
| kuśale | locative neuter singular | in wholesome consciousness |
| sadā | indeclinable | always |

The Bhāṣya identifies the two roots as non-greed and non-hatred. Counted
separately, they make ten factors.

## 4. Grammar

The ten coordinated factors share the locative condition *kuśale* and the
adverb *sadā*:

```text
śraddhā ... vīryam
    → ten wholesome great-ground factors

kuśale sadā
    → always in wholesome [consciousness]
```

The rule is universal within a qualified range: whenever a consciousness
is wholesome, the ten factors occur. The Bhāṣya says non-delusion is also
present, but identifies its nature with *prajñā*, already included among
the universal factors in VAK 2.24; it is not counted again here.

## 5. Scientific English Rendering

### Kārikā

> Confidence, heedfulness, pliancy, equanimity, moral shame, moral caution,
> the two [wholesome] roots, non-harming, and energy are always present in
> wholesome consciousness.

### Bhāṣya-informed rendering

> Every wholesome consciousness necessarily includes ten factors:
> confidence, heedful cultivation of wholesome Dharmas, mental workability,
> evenness and non-application of consciousness, moral shame, moral caution,
> non-greed, non-hatred, non-harming, and energetic arousal.

Here *upekṣā* is a wholesome mental factor defined as evenness and
non-application of consciousness. It is distinct from the neutral-feeling
Faculty discussed earlier.

## 6. Interpretation

VAK 2.25 narrows the operating range from factors occurring in every
consciousness to those occurring in every wholesome consciousness. The
Bhāṣya supplies ten members, counting the two wholesome roots separately,
and explains why non-delusion is not an additional member: its nature is
*prajñā*, already present in the universal great-ground.

The discussion also distinguishes a factor's nature from relations of
support and naming. The Bhāṣya says bodily workability supports mental
workability and that factors favorable to an awakening factor may receive
its designation without having the same nature. The equanimity exchange
remains unresolved: “in one respect … in another” is proposed, but the
objection about associated factors sharing one object-support is deferred
to the treatment of similar questions. An Organon reconstruction must
preserve that open issue rather than depict aspect-differentiation as a
settled solution.

In Kant-informed Techne, the wholesome class is a conditional
determination of consciousness, specified by its ten associated factors;
it is not a new Faculty or a succession of stages. The ten Samyama-bhūmis
describe Path-related operation of mental factors in the Organon
framework, with Buddha Dharma as the 11th Bhūmi. This verse neither
identifies every wholesome consciousness with a Path stage nor asserts
that each wholesome occurrence is perfected.

The Kośa's governing synthesis: Vijñāna is Discriminative Cognition joining
and governing Perception and Conception. Their unity is Inconceivable as a
homogeneous operation; its Idea is disclosed in the Cognition Base. Vijñāna
governs Mind and guides the reading of Dharma Base. Form Base and Dharma
Base both include the same *avijñapti* in distinct classifications, and
Vijñāna bears a *prati* relation to *avijñapti*. The factors named here
remain distinct from Faculties and from Vijñāna.

## 7. Logical Determination

```text
WholesomeFactors = {
    Confidence,
    Heedfulness,
    Pliancy,
    Equanimity,
    MoralShame,
    MoralCaution,
    NonGreed,
    NonHatred,
    NonHarming,
    Energy
}

For every consciousness-event e:
    Wholesome(e)
        → For every factor f in WholesomeFactors:
              PresentTogether(f, e)
```

Non-delusion is present through *prajñā* but is not counted as an
additional member of this ten-factor class. This schema does not resolve
the Bhāṣya's common-object question about attention and equanimity.

## 8. Interpretive Note

The commentary's alternative definitions remain attributed rather than
fused. Confidence is first explained as clarity of consciousness; “others”
explain it as conviction concerning truth, the Three Jewels, action, and
its result. Heedfulness is cultivation of wholesome Dharmas, specified as
attentive care; an unnamed other community uses the wording “guarding of
consciousness.”

The account of pliancy preserves the distinction between bodily
workability, its support of mental workability, and the designation
“awakening factor” received through favorability. Likewise, the prajñā
example distinguishes being prajñā by nature from being favorable to
prajñā. The source's apparent duplicated wording in that example is
recorded in the Bhāṣya study and is not treated as a settled emendation.

## 9. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_25
    a vak:Karika ;
    rdfs:label "VAK 2.25" ;
    vak:hasTopic vak:WholesomeGreatGroundFactors ;
    vak:belongsTo vak:Indriyanirdesa .

vak:WholesomeGreatGroundFactors
    vak:hasMember vak:Confidence,
        vak:Heedfulness,
        vak:Pliancy,
        vak:Equanimity,
        vak:MoralShame,
        vak:MoralCaution,
        vak:NonGreed,
        vak:NonHatred,
        vak:NonHarming,
        vak:Energy ;
    vak:occursIn vak:EveryWholesomeCittaEvent .

vak:Equanimity
    vak:definedAs vak:EvennessOfCitta,
        vak:NonApplicationOfCitta ;
    vak:distinctFrom vak:NeutralFeelingFaculty .

vak:NonDelusion
    vak:hasNature vak:Prajna ;
    vak:classifiedUnder vak:UniversalGreatGroundFactors .

organon:FactorDesignation
    organon:distinguishes organon:FactorNature,
        organon:SupportRelation,
        organon:TransferredDesignation .
```
