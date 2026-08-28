# VAK_2.25

## 1. Sanskrit (Devanāgarī)

> श्रद्धाप्रमादः प्रश्रब्धिरुपेक्षा ह्रीरपत्रपा ।
>
> मूलद्वयमहिंसा च वीर्यं च कुशले सदा ॥ २.२५ ॥

## 2. Sanskrit (IAST)

> śraddhāpramādaḥ praśrabdhir upekṣā hrīr apatrapā /
>
> mūladvayam ahiṃsā ca vīryaṃ ca kuśale sadā // 2.25 //

The transmitted sandhi `śraddhāpramādaḥ` is resolved by the Bhāṣya as two
factors: `śraddhā` and `apramāda`. It must not be parsed as confidence joined
to negligence (`pramāda`).

## 3. Padaccheda

```text
śraddhāpramādaḥ      → śraddhā apramādaḥ
praśrabdhir          → praśrabdhiḥ
upekṣā               → upekṣā
hrīr                 → hrīḥ
apatrapā             → apatrapā
mūladvayam           → mūla-dvayam
ahiṃsā ca            → ahiṃsā ca
vīryaṃ ca            → vīryam ca
kuśale               → kuśale
sadā                 → sadā
```

| Form | Morphology | Lexical force here |
|---|---|---|
| śraddhā | nominative feminine singular | confidence / clarity |
| a-pramādaḥ | nominative masculine singular privative formation | heedfulness / non-negligence |
| praśrabdhiḥ | nominative feminine singular | pliancy / workability |
| upekṣā | nominative feminine singular | equanimity |
| hrīḥ | nominative feminine singular | moral shame / inward ethical restraint |
| apatrapā | nominative feminine singular | moral caution / regard for blame |
| mūla-dvayam | nominative neuter singular compound | the pair of wholesome roots |
| ahiṃsā | nominative feminine singular | non-harming |
| vīryam | nominative neuter singular | energy |
| kuśale | locative neuter singular | in wholesome consciousness |
| sadā | indeclinable | always |

The dual content compressed into `mūla-dvayam` is supplied by the Bhāṣya:
non-greed and non-hatred. Counting those separately yields ten factors.

## 4. Grammar

The verse coordinates ten nominative subjects under one locative and one
universal adverb:

```text
śraddhā ... vīryam
    → ten wholesome great-ground factors

kuśale sadā
    → always in wholesome [consciousness]
```

The governing rule is conditional universality:

```text
whenever a citta is wholesome,
all ten factors are present
```

The ten are counted as:

```text
confidence             1
heedfulness            2
pliancy                3
equanimity             4
moral shame            5
moral caution          6
non-greed              7
non-hatred             8
non-harming            9
energy                10
```

Non-delusion is not absent. The Bhāṣya identifies it in nature with `prajñā`,
already counted as `mati` among the universal factors of VAK 2.24, so it is
not counted again in this class.

## 5. Translation

### Close syntactic construe

> Confidence, heedfulness, pliancy, equanimity, moral shame, moral caution, the two [wholesome] roots, non-harming, and energy are always present in the wholesome.

### Bhāṣya-informed translation

> Every wholesome consciousness necessarily includes ten factors: confidence, heedful maintenance of wholesome dharmas, mental workability, evenness and non-exertion of consciousness, inward moral restraint, moral caution, non-greed, non-hatred, non-injury, and energetic arousal.

Here `upekṣā` is a wholesome mental factor defined as evenness and
non-exertion of consciousness. It is not the neutral-feeling faculty that
bears the same Sanskrit name.

## 6. Philosophical Translation

> Wholesomeness is not an external value assigned to an otherwise unchanged consciousness. It is an internally articulated mode: consciousness becomes clear, heedful, workable, balanced, ethically restrained, non-appropriative, non-hostile, non-injurious, and energetically capable. To call a consciousness wholesome is to assert this coordinated functional structure.

Restrained Organon rendering:

> `Kuśala` is a state constraint rather than a label. A state validates as wholesome only when its required factors are present; related names must still preserve distinct functions, and factors already inherited from the universal ground must not be counted twice.

The validation language is project-level. The textual doctrine is that these
ten mental factors are invariably present in wholesome consciousness.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Bhāṣya determination |
|---|---|---|
| kuśala-mahābhūmika | wholesome great-ground factor | factor whose operating range includes every wholesome consciousness |
| śraddhā | confidence / clarity | serenity of consciousness; alternatively, conviction concerning truth, the Three Jewels, karma, and karmic result |
| apramāda | heedfulness | careful attentiveness to wholesome dharmas; another school calls it guarding consciousness |
| praśrabdhi | pliancy / workability | workability of consciousness (`citta-karmaṇyatā`) |
| upekṣā | equanimity | evenness and non-exertion of consciousness; distinct from neutral feeling |
| hrī | moral shame / inward restraint | named here and deferred for later explanation |
| apatrapā | moral caution / regard | named here and deferred for later explanation |
| alobha | non-greed | first of the two wholesome roots counted here |
| adveṣa | non-hatred | second of the two wholesome roots counted here |
| amoha | non-delusion | present through `prajñā`; not counted again because it belongs to the universal ground |
| ahiṃsā | non-harming | non-injury |
| vīrya | energy | energetic arousal of consciousness |
| bodhyaṅgānukūlya | favorability to an awakening factor | relation explaining transferred designation of bodily pliancy |

The alternative accounts of confidence and heedfulness are attributed views,
not definitions silently fused into a single Kārikā meaning.

## 8. Logical Determination

Let:

```text
WholesomeTen = {
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
```

Then:

```text
ForEvery cittaEvent e:
    Wholesome(e)
        → ForEvery f in WholesomeTen:
              CoarisesIn(f, e)
```

Because universal great-ground factors already occur in every consciousness:

```text
WholesomeMentalEvent(e)
    → UniversalTen ⊆ Factors(e)
    → WholesomeTen ⊆ Factors(e)
```

Non-delusion illustrates classification without duplication:

```text
Nature(NonDelusion) = Prajñā
Prajñā ∈ UniversalTen

therefore
NonDelusion is operative in wholesome consciousness
but is not a second member of WholesomeTen
```

The attention-equanimity problem requires aspect-indexing:

```text
Attention(e, aspectA) = Exertion
Equanimity(e, aspectB) = NonExertion

aspectA ≠ aspectB
    → CompatibleInSameEvent(Attention, Equanimity)
```

This does not identify exertion with non-exertion. It preserves their
functional opposition while allowing co-presence under different aspects.

The bodily-pliancy discussion supplies a semantic relation:

```text
DirectlySupports(x, AwakeningFactor(y))
    → x may receive y's designation by transferred naming

NameTransfer(x, y)
    ⇏ Nature(x) = Nature(y)
```

## 9. Interpretive Note

VAK 2.25 moves from the factors distributed through every consciousness to
the factors distributed through every wholesome consciousness. Its `bhūmi`
is therefore narrower than the great ground but still universal within its
condition:

```text
GreatGround
    = all consciousness-events

WholesomeGreatGround
    = all wholesome consciousness-events
```

The definitions show that wholesomeness is operational. Confidence clarifies;
heedfulness sustains and guards; pliancy makes consciousness workable;
equanimity gives evenness without forced exertion; the ethical factors inhibit
appropriation, hostility, and injury; energy actively arouses the wholesome
continuum.

The equanimity discussion is especially important for discrimination. The
same event contains attention, previously defined through application or
exertion, and equanimity, defined through non-exertion. Vasubandhu does not
erase the opposition. He resolves it by differentiating the aspects under
which the two functions operate. Necessary co-arising therefore requires a
relational model fine-grained enough to preserve opposition without declaring
contradiction.

The discussion of bodily pliancy adds an equally important semantic rule. A
supporting condition may receive the name of an awakening factor because it
is favorable to that factor, without sharing its nature. Provenance matters:

```text
same designation
    may arise from
identity of nature
    or
functional support
```

This protects the Kośa study from flattening relational attribution into
ontological identity. It also keeps the factor taxonomy economical:
non-delusion is fully present through universal `prajñā`, but is not duplicated
in the wholesome count.

For the Kośa Technē, the restrained consequence is that a mental-state model
must track factor identity, operating ground, aspect, and reason for
designation. A name or Boolean wholesome flag cannot substitute for that
structure.

## 10. OWL++ Seed

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
    vak:operatesIn vak:EveryWholesomeCittaEvent .

vak:Equanimity
    vak:definedAs vak:EvennessOfCitta,
        vak:NonExertionOfCitta ;
    vak:distinctFrom vak:NeutralFeelingFaculty .

vak:NonDelusion
    vak:hasNature vak:Prajna ;
    vak:classifiedUnder vak:UniversalGreatGroundFactors .

organon:FactorAttribution
    a organon:InterpretiveReconstruction ;
    organon:requires organon:FactorIdentity,
        organon:OperatingGround,
        organon:Aspect,
        organon:DesignationGround ;
    organon:inferredFrom vak:WholesomeGreatGroundFactors .
```
