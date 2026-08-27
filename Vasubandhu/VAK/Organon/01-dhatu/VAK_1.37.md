# VAK_1.37

## 1. Sanskrit (Devanāgarī)

> विपाकजौपचयिकाः पञ्चाध्यात्मं विपाकजः ।
>
> न शब्दोऽप्रतिघा अष्टौ नैःष्यन्दिकविपाकजाः ॥ १.३७ ॥

## 2. Sanskrit (IAST)

> vipākajaupacayikāḥ pañcādhyātmaṃ vipākajaḥ /
>
> na śabdo 'pratighā aṣṭau naiḥṣyandika-vipākajāḥ // 1.37 //

## 3. Padaccheda

```text
vipākajaupacayikāḥ      → vipākajāḥ aupacayikāḥ
pañcādhyātmam           → pañca adhyātmam
vipākajaḥ na śabdaḥ     → vipākajaḥ na śabdaḥ
'pratighāḥ              → apratighāḥ
naiḥṣyandika-vipākajāḥ  → naiḥṣyandikāḥ vipākajāḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| vipākajāḥ | nominative masculine plural compound | born from a maturation-ground |
| aupacayikāḥ | nominative masculine plural adjective | produced or reinforced through organic accumulation |
| pañca | numeral | the five sensory faculty-Domains |
| adhyātmam | adverbial accusative | internally; on the internal side |
| na | negative particle | not |
| śabdaḥ | nominative masculine singular | sound-domain |
| a-pratighāḥ | nominative masculine plural adjective | non-resistant, non-obstructive |
| aṣṭau | numeral | seven cognitive Domains plus the Dharma-domain |
| naiḥṣyandikāḥ | nominative masculine plural adjective | born through homogeneous causal continuity |
| vipākajāḥ | nominative masculine plural adjective | born through karmic maturation |

`Naiḥṣyandika` should not be confused with `sāsrava`, “with outflows.” Here
it names production through a corresponding causal flow or homogeneous
continuity, specified in the Bhāṣya through `sabhāgahetu` and
`sarvatragahetu`.

## 4. Grammar

The first clause assigns two possible origins to the five internal
faculty-Domains:

```text
pañca adhyātmam
    eye, ear, nose, tongue, and body faculties

vipākajāḥ
    born from karmic maturation

aupacayikāḥ
    produced or reinforced through organic accumulation
```

The Bhāṣya analyzes `vipākaja` as an abbreviated
`vipāka-hetu-ja`: born from a maturation-ground. `Aupacayika` is explained
through buildup by nourishment, conditioning, sleep, and distinctions of
concentration. Some add celibate discipline, but Vasubandhu notes that this
may merely prevent injury rather than produce positive increase.

The next clause is singular:

```text
śabdaḥ na vipākajaḥ
    sound is not maturation-born
```

The Bhāṣya does not deny every causal mode to sound. Sound may be
accumulation-produced or continuity-born. It is excluded specifically from
direct maturation because its present occurrence proceeds from effort
(`īhātaḥ pravṛtti`).

The final clause concerns the eight non-resistant Domains:

```text
seven citta-Domains
+ Dharma-domain
    → continuity-born or maturation-born
```

They are not accumulation-produced because non-resistant Domains do not
consist in material accumulation.

## 5. Translation

### Close syntactic construe

> The five internal [faculty-Domains] are maturation-born and accumulation-produced. Sound is not maturation-born. The eight non-resistant Domains are continuity-born or maturation-born.

### Bhāṣya-informed translation

> The five sensory faculties may arise as results of karmic maturation and may also be organically reinforced through nourishment, conditioning, sleep, and concentration. Sound is not itself a maturation-result because its immediate production proceeds from effort, although it can arise through accumulation or causal continuity. The seven cognitive Domains together with the Dharma-domain may arise through homogeneous continuity or karmic maturation, but not through material accumulation.

The disjunctions express permitted genetic modes. They do not imply that
every individual instance is produced simultaneously by every listed cause.

## 6. Philosophical Translation

> A Domain is determined not only by its present properties but by the manner in which its continuity is generated. The faculties possess a karmically matured constitution that can be organically maintained and strengthened. Sound is an event initiated through present effort rather than a passive maturation-result. Non-resistant cognitive and Dharma Domains lack material accumulation yet remain fully subject to causal continuity and maturation.

Organon rendering:

> The Principle of the Agent now receives a genesis protocol. Its faculties are inherited capacities whose maturation-continuity is protected and reinforced by living conditions. Cognitive Domains are non-spatial without being causally ungrounded. The Agent is therefore neither assembled from inert parts nor posited outside causality; it is a differentiated system of generated and maintained capacities.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| vipākaja | maturation-born | generated from karma that has reached the time of fruition |
| vipākahetu | maturation-ground | causal basis expanded from the abbreviated compound |
| vipākasantāna | maturation-continuity | karmically generated organic continuum |
| aupacayika | organically accumulated / reinforced | built up through nourishment and other living conditions |
| upacayasantāna | reinforcement-continuity | continuity protecting and strengthening maturation like a surrounding wall |
| anupaghāta | non-injury / preservation | absence of damage, distinguished from positive growth |
| naiḥṣyandika | continuity-born | generated through homogeneous or universally operative causal grounds |
| sabhāgahetu | homogeneous ground | produces corresponding factors in a causal series |
| sarvatragahetu | universally operative ground | continuity-ground especially relevant to afflicted dharmas |
| īhā | effort / exertion | immediate initiating condition excluding sound from maturation-status |
| paramparā | mediated causal succession | explains how karma can indirectly condition voice without making sound itself vipākaja |
| apratigha | non-resistant | non-spatially obstructive, not causally unconditioned |

## 8. Logical Determination

The faculty genesis types are:

```text
FiveInternalFacultyDomains
    → MayBeGeneratedBy(VipakaHetu)
    ∧ MayBeReinforcedBy(OrganicAccumulation)

OrganicAccumulation
    ← Nourishment
    ∨ Conditioning
    ∨ Sleep
    ∨ ConcentrationDifference
```

Preservation and increase are non-equivalent:

```text
PreventsInjury(x)
    ↛ PositivelyIncreases(x)
```

The two faculty continuities cooperate:

```text
VipakaContinuity
    → supplies matured organic capacity

UpacayaContinuity
    → protects and reinforces VipakaContinuity
```

Sound is typed by immediate production:

```text
ProducedThroughPresentEffort(Sound)
    → ¬Vipakaja(Sound)

IndirectlyConditionedByKarma(Sound)
    ↛ DirectlyVipakaja(Sound)
```

The eight non-resistant Domains have causal but non-accumulative genesis:

```text
EightApratighaDomains
    → MayBe(Naisyandika)
    ∨ MayBe(Vipakaja)
    ∧ ¬Aupacayika
```

The Smart-Domain rule is:

```text
GenesisType(x)
    determinedBy ImmediateCausalMode(x)
    not merely RemoteCausalAncestry(x)
```

## 9. Interpretive Note

VAK 1.37 adds causal lineage to the Smart Domain. The question is no longer
only what a Domain is capable of doing; it is how that capability came to be
present and how its continuity is maintained.

The Indriya receives an especially powerful determination:

```text
karma reaching fruition
    → matured faculty-continuity

nourishment, sleep, conditioning, concentration
    → reinforced faculty-continuity

faculty-operation
    → actual apprehensive capacity
```

Thus the faculty is not the gross organ, not an independent Seer, and not a
merely abstract function. It is an internal organic capacity with a causal
history and a maintainable continuum. This is part of the constitution of
the Agent, not an incidental biological note.

Sound reveals the difference between remote ancestry and immediate genesis.
A disciplined karmic history may condition the bodily basis of a beautiful
voice, yet the actual sound proceeds through present effort. The Logic must
therefore type an event by its operative mode of production rather than
assigning the same causal label to everything downstream from karma.

The eight non-resistant Domains make the complementary point. Absence of
material obstruction or accumulation does not imply absence of causal
lineage:

```text
non-material accumulation
    ≠ non-causal
```

Mind and Dharma flow through homogeneous causal continuities and may also
arise as maturation-results. This is precisely the sort of constraint the
eventual Agent requires: inwardness does not exempt a state from genesis.

The Principle of the Agent has consequently acquired a genetic architecture:

```text
Agent capacity
    = inherited causal lineage
    + living reinforcement
    + present operation
```

Later Yoga will work upon this constituted Agent. It will not create its
faculties ex nihilo; it will regulate, reinforce, transform, and eventually
purify modes whose causal structures the Kośa has already made explicit.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_37
    a vak:Karika ;
    rdfs:label "VAK 1.37" ;
    vak:hasTopic vak:CausalGenesisOfDomains ;
    vak:belongsTo vak:Dhatunirdesa .

vak:FiveInternalFacultyDomains
    a vak:DomainSet ;
    vak:permitsGenesis vak:Vipakaja,
        vak:Aupacayika .

vak:SoundDhatu
    vak:notGenesis vak:Vipakaja ;
    vak:immediatelyProducedBy vak:Effort .

vak:EightApratighaDomains
    a vak:DomainSet ;
    vak:permitsGenesis vak:Naisyandika,
        vak:Vipakaja ;
    vak:notGenesis vak:Aupacayika .

vak:FacultyCapacity
    vak:generatedAs vak:VipakaContinuity ;
    vak:reinforcedBy vak:UpacayaContinuity ;
    vak:actualizedThrough vak:FacultyOperation .

organon:GeneticSmartDomain
    a vak:SmartDomainCapability ;
    organon:requiresParameter vak:ImmediateCausalMode,
        vak:CausalContinuity,
        vak:ReinforcementMode .
```
