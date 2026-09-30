# VAK_2.26

## 1. Sanskrit (Devanāgarī)

> मोहः प्रमादः कौशीद्यमाश्रद्ध्यं स्त्यानमौद्धत्यम् ।
>
> क्लिष्टे सदैवाकुशले त्वाह्रीक्यमनपत्रपा ॥ २.२६ ॥

The research witness reads `आश्रद्धयं` and `उद्धवः`. The Bhāṣya preserves
the doctrinally and morphologically expected forms `आश्रद्ध्यम्`
(`āśraddhyam`) and `औद्धत्यम्` (`auddhatyam`), which are adopted in the
official text above while the research witness remains unchanged.

## 2. Sanskrit (IAST)

> mohaḥ pramādaḥ kauśīdyam āśraddhyaṃ styānam auddhatyam /
>
> kliṣṭe sadaivākuśale tv āhrīkyam anapatrapā // 2.26 //

## 3. Padaccheda

```text
mohaḥ               → mohaḥ
pramādaḥ            → pramādaḥ
kauśīdyam           → kauśīdyam
āśraddhyaṃ          → ā-śraddhyam
styānam             → styānam
auddhatyam          → auddhatyam
kliṣṭe              → kliṣṭe
sadaivākuśale       → sadā eva akuśale
tv                  → tu
āhrīkyam            → āhrīkyam
anapatrapā          → an-apatrapā
```

| Form | Morphology | Lexical force here |
|---|---|---|
| mohaḥ | nominative masculine singular | delusion / ignorance |
| pramādaḥ | nominative masculine singular | negligence |
| kauśīdyam | nominative neuter singular | laziness |
| āśraddhyam | nominative neuter singular | lack of confidence or clarity |
| styānam | nominative neuter singular | sluggishness / unworkability |
| auddhatyam | nominative neuter singular | agitation / non-pacification |
| kliṣṭe | locative neuter singular | in afflicted consciousness |
| sadā eva | indeclinables | always indeed |
| akuśale | locative neuter singular | in unwholesome consciousness |
| tu | contrastive particle | but / further, in the more specific case |
| āhrīkyam | nominative neuter singular | shamelessness / absence of moral restraint |
| an-apatrapā | nominative feminine singular | absence of moral caution |

## 4. Grammar

The first line lists six subjects governed by the locative and universal
adverb at the beginning of the second line:

```text
mohaḥ ... auddhatyam
    → six afflicted great-ground factors

kliṣṭe sadā eva
    → always in afflicted [consciousness]
```

The latter half adds a narrower conditioned rule:

```text
akuśale tu
    → but in unwholesome [consciousness]

āhrīkyam anapatrapā
    → shamelessness and absence of moral caution [are also always present]
```

The Bhāṣya treats these as two different class predicates. `Kliṣṭa` and
`akuśala` are not interchangeable here. The unwholesome state bears the
afflicted factors and additionally the two specifically unwholesome
great-ground factors.

## 5. Translation

### Close syntactic construe

> Delusion, negligence, laziness, lack of confidence, sluggishness, and agitation are always indeed present in the afflicted; but in the unwholesome [there are also] shamelessness and absence of moral caution.

### Bhāṣya-informed translation

> Every afflicted consciousness contains six factors proper to the extensive afflicted ground: ignorance, failure to cultivate the wholesome, absence of energetic exertion, absence of confidence or clarity, bodily and mental heaviness and unworkability, and non-pacification of consciousness. Every specifically unwholesome consciousness additionally contains shamelessness and lack of moral concern.

The Bhāṣya also reports a longer Abhidharma enumeration of ten. Its resolution
does not replace the Kārikā's six; it distinguishes corrupted forms of
universal factors from factors classified specifically under the afflicted
great ground.

## 6. Philosophical Translation

> Affliction is not the disappearance of the universal mental functions. It is their operation within a field necessarily pervaded by ignorance, negligence, depleted energy, loss of confidence, unworkability, and agitation. Memory, concentration, discernment, attention, and resolution can remain structurally present while functioning in corrupted forms. Unwholesomeness adds the collapse of the two ethical restraints.

Restrained Organon rendering:

> A diagnostic model must separate capability from mode and class-membership. The same universal operation may execute wholesomely or afflictedly; a specifically afflicted factor is not identical with an afflicted mode of a universal factor. State labels based on predominance must also preserve co-present factors hidden by the label.

This diagnostic language is project-level. The textual analysis concerns
operating grounds, afflicted modes, and the intention of competing
Abhidharma enumerations.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Bhāṣya determination |
|---|---|---|
| kleśa-mahābhūmika | afflicted great-ground factor | factor always found only in afflicted consciousness |
| moha | delusion / ignorance | not knowing and not clearly comprehending |
| pramāda | negligence | non-cultivation of wholesome dharmas; opposed to heedfulness |
| kauśīdya | laziness | absence of energetic exertion in consciousness; opposed to energy |
| āśraddhya | lack of confidence | absence of clarity or confidence; opposed to `śraddhā` |
| styāna | sluggishness / unworkability | heaviness and unworkability of body and consciousness |
| auddhatya | agitation | non-pacification of consciousness |
| akuśala-mahābhūmika | unwholesome great-ground factor | factor always present in specifically unwholesome consciousness |
| āhrīkya | shamelessness | absence of inward moral restraint |
| anapatrāpya | absence of moral caution | absence of concern regarding misconduct and others |
| muṣita-smṛtitā | lost recollection | afflicted mode of the universal recollection factor |
| vikṣepa | distraction | afflicted concentration; some treat it as distinct from wrong concentration |
| asaṃprajanya | lack of clear comprehension | afflicted discernment |
| ayoniśo-manaskāra | improper attention | afflicted mode of the universal attention factor |
| mithyādhimokṣa | false resolution | afflicted mode of the universal resolution factor |
| catuṣkoṭika | fourfold alternatives | analysis of two class predicates without collapsing their extensions |

The alternative view that distraction differs from wrong concentration is
reported as such. It prevents a single inherited taxonomy from being
presented as uncontested.

## 8. Logical Determination

Let the six specifically afflicted factors be:

```text
AfflictedSix = {
    Delusion,
    Negligence,
    Laziness,
    LackOfConfidence,
    Sluggishness,
    Agitation
}
```

Then:

```text
ForEvery cittaEvent e:
    Afflicted(e)
        → AfflictedSix ⊆ Factors(e)
```

The specifically unwholesome extension is:

```text
UnwholesomeTwo = {
    Shamelessness,
    AbsenceOfMoralCaution
}

Unwholesome(e)
    → Afflicted(e)
    → UnwholesomeTwo ⊆ Factors(e)
```

The longer list of ten uses a different classification relation:

```text
AfflictedUniversalModes = {
    LostRecollection,
    Distraction,
    LackOfClearComprehension,
    ImproperAttention,
    FalseResolution
}

ForEvery m in AfflictedUniversalModes:
    BaseFunction(m) ∈ UniversalGreatGroundFactors
    ∧ Mode(m) = Afflicted
```

Therefore:

```text
OccursInAfflictedMode(f)
    ⇏ ClassifiedExclusivelyAsAfflictedGroundFactor(f)
```

The Bhāṣya's fourfold analysis discriminates two predicates:

```text
U(f) = f belongs to the universal great ground
A(f) = f belongs to the afflicted great ground or occurs in afflicted form

U ∧ ¬A
¬U ∧ A
U ∧ A
¬U ∧ ¬A
```

The exact membership shifts under the disputed account of distraction, so
the fourfold form is stable while one boundary remains school-dependent.

Sluggishness and agitation establish predominance without exclusion:

```text
Afflicted(e)
    → CoarisesIn(Sluggishness, e)
    ∧ CoarisesIn(Agitation, e)

Label(e) = SluggishType
    iff Strength(Sluggishness, e) > Strength(Agitation, e)

Label(e) = AgitatedType
    iff Strength(Agitation, e) > Strength(Sluggishness, e)
```

## 9. Interpretive Note

VAK 2.26 prevents the bhūmi taxonomy from becoming a partition of simple,
mutually exclusive items. The universal factors of VAK 2.24 remain in every
consciousness, including afflicted consciousness. What changes is their mode:
recollection becomes lost recollection, concentration becomes distraction,
discernment becomes lack of clear comprehension, attention becomes improper
attention, and resolution becomes false resolution.

This explains the apparent conflict between six and ten afflicted factors.
The longer recitation names factors found in afflicted consciousness. The
Kārikā's list identifies factors whose classificatory identity belongs
specifically to the afflicted great ground. Vasubandhu preserves the
recitation by reconstructing its intention rather than treating its extension
as identical with the sixfold class.

The result is a three-axis analysis:

```text
Factor
    = universal function
    + present qualitative mode
    + classificatory operating ground
```

The sluggishness-agitation discussion adds a fourth axis: relative strength.
The two never abandon co-presence, yet a continuum is designated by whichever
predominates. A type-name therefore records dominance, not exclusive
membership.

The traditional claim that sluggishness may be favorable to concentration is
not praise of sluggishness. It shows that causal or supportive relations do
not always align neatly with ethical classification. Vasubandhu's question
then refuses the fantasy of pure sluggish and pure agitated types: both
factors remain present, and only their strength differs.

For the Kośa Technē, this yields a restrained diagnostic requirement:

```text
MentalFactorState
    = baseFunction
    + mode
    + groundClass
    + strength

diagnosticLabel
    = derived from predominance
    ≠ complete state description
```

No factor should be replaced by its label, and no corrupted mode should be
mistaken for the absence of the underlying universal function.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_26
    a vak:Karika ;
    rdfs:label "VAK 2.26" ;
    vak:hasTopic vak:AfflictedGreatGroundFactors,
        vak:UnwholesomeGreatGroundFactors ;
    vak:belongsTo vak:Indriyanirdesa .

vak:AfflictedGreatGroundFactors
    vak:hasMember vak:Delusion,
        vak:Negligence,
        vak:Laziness,
        vak:LackOfConfidence,
        vak:Sluggishness,
        vak:Agitation ;
    vak:operatesIn vak:EveryAfflictedCittaEvent .

vak:UnwholesomeGreatGroundFactors
    vak:hasMember vak:Shamelessness,
        vak:AbsenceOfMoralCaution ;
    vak:operatesIn vak:EveryUnwholesomeCittaEvent .

vak:LostRecollection
    vak:hasBaseFunction vak:Recollection ;
    vak:hasMode vak:AfflictedMode .

vak:Distraction
    vak:hasBaseFunction vak:Concentration ;
    vak:hasMode vak:AfflictedMode ;
    vak:hasDisputedIdentity true .

organon:MentalFactorState
    a organon:InterpretiveReconstruction ;
    organon:requires organon:BaseFunction,
        organon:QualitativeMode,
        organon:OperatingGround,
        organon:RelativeStrength ;
    organon:distinguishes organon:PredominanceLabel,
        organon:CompleteStateDescription .
```
