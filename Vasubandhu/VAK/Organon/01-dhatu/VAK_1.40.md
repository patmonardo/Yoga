# VAK_1.40

## 1. Sanskrit (Devanāgarī)

> दश भावनया हेयाः पञ्च चान्त्यास्त्रयस्त्रिधा ।
>
> न दृष्टिहेयमक्लिष्टं न रूपं नाप्यषष्ठजम् ॥ १.४० ॥

## 2. Sanskrit (IAST)

> daśa bhāvanayā heyāḥ pañca cāntyās trayas tridhā /
>
> na dṛṣṭiheyam akliṣṭaṃ na rūpaṃ nāpy aṣaṣṭhajam // 1.40 //

## 3. Padaccheda

```text
bhāvanayā heyāḥ       → bhāvanayā heyāḥ
pañca cāntyāḥ         → pañca ca antyāḥ
trayas tridhā         → trayaḥ tridhā
dṛṣṭiheyam            → dṛṣṭi-heyam
akliṣṭam              → a-kliṣṭam
nāpy aṣaṣṭhajam       → na api a-ṣaṣṭha-jam
```

| Form | Morphology | Lexical force here |
|---|---|---|
| daśa | numeral | the ten material Domains |
| bhāvanayā | instrumental feminine singular | through cultivation or repeated development |
| heyāḥ | nominative masculine plural gerundive | to be abandoned or relinquished in their contaminated mode |
| pañca | numeral | the five sensory knowledge-Domains |
| antyāḥ trayaḥ | nominative masculine plural | mind-, Dharma-, and mental-knowledge Domains |
| tridhā | adverb | in three modes of abandonability |
| dṛṣṭi-heya | neuter singular predicate | to be abandoned by seeing |
| a-kliṣṭam | nominative/accusative neuter singular | undefiled, unafflicted |
| rūpam | nominative/accusative neuter singular | material form |
| a-ṣaṣṭha-jam | nominative/accusative neuter singular compound | not born from the sixth Sphere, the mental Sphere |

The Bhāṣya commonly uses `darśanaheya` for the Kārikā's `dṛṣṭiheya`.
Both designate the technical category abandoned through seeing the truths.

## 4. Grammar

The first line supplies three path-statuses across the eighteen Domains.
The ten material Domains and five sensory knowledge-Domains are assigned to
`bhāvanāheya`:

```text
ten material Domains
+ five sensory knowledge-Domains
    → to be abandoned through cultivation
```

This does not mean that matter, faculty, or sensory knowledge is annihilated
as a Domain-kind. The Bhāṣya concerns their contaminated occurrences and
operation.

The final three are threefold:

```text
mind-domain
Dharma-domain
mental-knowledge Domain
    → dṛṣṭiheya
    ∨ bhāvanāheya
    ∨ aheya
```

The Bhāṣya identifies the three groups precisely:

```text
eighty-eight latent afflictions,
their co-arisen factors,
their acquisitions,
and their attendants
    → abandoned by seeing

remaining outflow-bound dharmas
    → abandoned by cultivation

outflow-free dharmas
    → not to be abandoned
```

The second line gives necessary exclusions from seeing-abandonment. Nothing
undefiled, nothing material, and nothing generated outside the sixth or
mental Sphere is abandoned by seeing.

## 5. Translation

### Close syntactic construe

> Ten are to be abandoned through cultivation, and five also. The final three are threefold. Nothing undefiled is to be abandoned by seeing, nor material form, nor what is not born from the sixth.

### Bhāṣya-informed translation

> The contaminated modes of the ten material Domains and five sensory knowledge-Domains are relinquished through cultivation. Mind, Dharma, and mental knowledge contain three classes: afflictive factors abandoned through seeing, remaining outflow-bound factors abandoned through cultivation, and outflow-free factors that are not abandoned. Direct seeing abandons nothing undefiled, nothing material, and nothing not generated from the mental Sphere.

The qualification “contaminated modes” prevents the path-classification from
being mistaken for destruction of the fifteen Domain lineages themselves.

## 6. Philosophical Translation

> The Path differentiates its corrective operations according to the nature of their object. Seeing directly removes a delimited field of afflicted mental determination. Cultivation gradually relinquishes the remaining contaminated operation of embodied and sensory life. Outflow-free determination is not an object of correction. Abandonment is therefore typed transformation, not universal negation.

Organon rendering:

> The Principle of the Agent now receives a correction protocol. False mental determination, conditioned operational habit, and outflow-free knowing cannot be treated by one undifferentiated act. The Agent must discriminate what insight can terminate, what development must transform, and what must remain untouched. This is Kośa path-technē available for later appropriation by Yoga, not a rule imposed upon Yoga itself.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| heya | to be abandoned / relinquished | path-status of a contaminated factor, not destruction of its Domain-kind |
| dṛṣṭiheya / darśanaheya | to be abandoned by seeing | directly removed through seeing the truths |
| bhāvanāheya | to be abandoned through cultivation | relinquished through repeated path-development |
| aheya | not to be abandoned | status of outflow-free dharmas |
| bhāvanā | cultivation / development | repeated transformation rather than one cognitive cut |
| anuśaya | latent affliction | eighty-eight are assigned to seeing-abandonment |
| sahabhū | co-arisen factor | factor arising with a latent affliction |
| prāpti | acquisition / possession-factor | maintains possession of the relevant afflictive dharma |
| sānucara | accompanied by attendants | extends the complex abandoned with the affliction |
| akliṣṭa | undefiled / unafflicted | excluded from seeing-abandonment |
| pṛthagjanatva | ordinary-person status | undefiled-indeterminate test case, though incompatible with the noble Path |
| āryamārgavirodhitva | opposition to the noble Path | insufficient by itself to determine seeing-abandonment |
| aṣaṣṭhaja | not born from the sixth | generated outside the mental Sphere and therefore not seeing-abandonable |
| mana-āyatana | mental Sphere | the sixth Sphere intended by the Kārikā |

## 8. Logical Determination

The path-status partition is:

```text
ContaminatedInstanceOf(TenMaterialDomains)
    → Bhavanaheya

ContaminatedInstanceOf(FiveSensoryKnowledgeDomains)
    → Bhavanaheya

InstanceOf(FinalMentalDharmaTriad)
    → Drstiheya
    ∨ Bhavanaheya
    ∨ Aheya
```

The exact classes are:

```text
EightyEightAnusayas
∪ CoarisenFactors
∪ Acquisitions
∪ Attendants
    → Drstiheya

RemainingSasravaDharmas
    → Bhavanaheya

AnasravaDharmas
    → Aheya
```

The negative rule is:

```text
Aklishta(x)
∨ Material(x)
∨ NotBornFromMentalSphere(x)
    → ¬Drstiheya(x)
```

Mere opposition is insufficient:

```text
OpposesNoblePath(x)
    ↛ Drstiheya(x)
```

The operations must not be collapsed:

```text
SeeingAbandonment
    ≠ CultivationAbandonment
    ≠ NonAbandonment
```

Nor may the status of an occurrence be transferred to the entire lineage:

```text
Bhavanaheya(ContaminatedInstanceOfDomain)
    ↛ Abolish(DomainKind)
```

## 9. Interpretive Note

VAK 1.40 is the threshold at which the descriptive science of Domains
becomes explicitly path-directed. The established Domains are now queried
according to the mode by which their contaminated determinations cease.

The principal safeguard is that seeing is selective. It does not abolish
embodiment, sensory capacity, ordinary-person status merely because it is
incompatible with the noble Path, or everything opposed to liberation. Its
direct field is the afflicted mental complex rooted in the sixth Sphere.

Cultivation performs different work. Material and sensory operations are
conditioned capacities and habits. Their contaminated modes are relinquished
through development rather than destroyed by insight:

```text
seeing
    → direct termination of afflicted mental determination

cultivation
    → developmental transformation of remaining contamination

outflow-free status
    → no abandonment
```

This extends the distinction between Domain lineage and functional status
from 1.39. The path does not delete the lineage because one of its modes is
contaminated. It transforms or terminates the relevant occurrence according
to its type.

For the Principle of the Agent, this yields a precise correction science:

```text
Agent determination
    → classify its path-status
    → apply the corresponding mode of correction
```

The future Organon Vārttika may find this highly useful, but we should not
overlay Kośa technē upon Yoga. The positive textual result is Abhidharma's
own: different kinds of contamination require different kinds of
abandonment, and outflow-free dharmas are not abandoned.

This also keeps the comparison with Yoga answerable. Yoga may appropriate,
translate, or reject aspects of this correction schema from its own higher
principles. The Kośa supplies a potent Agent-side technē; it does not decide
the metaphysics or final method of our Yoga.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_40
    a vak:Karika ;
    rdfs:label "VAK 1.40" ;
    vak:hasTopic vak:PathStatusOfDomains ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Drstiheya
    a vak:PathStatus ;
    vak:appliesTo vak:EightyEightAnusayas,
        vak:AfflictionAssociatedComplex .

vak:Bhavanaheya
    a vak:PathStatus ;
    vak:appliesTo vak:RemainingSasravaDharmas .

vak:Aheya
    a vak:PathStatus ;
    vak:appliesTo vak:AnasravaDharmas .

vak:SeeingAbandonment
    vak:distinctFrom vak:CultivationAbandonment .

vak:DomainLineage
    vak:notAbolishedBy vak:AbandonmentOfContaminatedInstance .

organon:AgentCorrectionScience
    a vak:AgentSideModel ;
    organon:distinguishes vak:DirectSeeingCorrection,
        vak:CultivationalTransformation,
        vak:NonAbandonment .
```
