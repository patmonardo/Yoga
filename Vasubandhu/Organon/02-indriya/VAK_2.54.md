# VAK_2.54

## 1. Sanskrit (Devanāgarī)

> सर्वत्रगाख्यः क्लिष्टानां स्वभूमौ पूर्वसर्वगाः ।
>
> विपाकहेतुरशुभाः कुशलाश्चैव सास्रवाः ॥ २.५४ ॥

## 2. Sanskrit (IAST)

> sarvatragākhyaḥ kliṣṭānāṃ svabhūmau pūrvasarvagāḥ /
>
> vipākahetur aśubhāḥ kuśalāś caiva sāsravāḥ // 2.54 //

## 3. Padaccheda

```text
sarvatragākhyaḥ       → sarvatraga-ākhyaḥ
kliṣṭānām             → kliṣṭānām
svabhūmau             → sva-bhūmau
pūrvasarvagāḥ         → pūrva-sarvagāḥ
vipākahetur           → vipāka-hetuḥ
aśubhāḥ               → aśubhāḥ
kuśalāś               → kuśalāḥ
caiva                 → ca eva
sāsravāḥ              → sa-āsravāḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| sarvatraga-ākhyaḥ | nominative masculine singular compound | called pervasive [cause] |
| kliṣṭānām | genitive masculine plural | of later afflicted dharmas |
| sva-bhūmau | locative feminine singular | within their own level |
| pūrva-sarvagāḥ | nominative masculine plural compound | previously arisen pervasive dharmas |
| vipāka-hetuḥ | nominative masculine singular compound | maturation cause |
| aśubhāḥ | nominative masculine plural | unwholesome dharmas |
| kuśalāḥ | nominative masculine plural | wholesome dharmas |
| ca eva | conjunction plus emphatic particle | and indeed |
| sa-āsravāḥ | nominative masculine plural compound | accompanied by contaminating outflows |

`Sāsrava` qualifies the wholesome dharmas: only contaminated, realm-bound
wholesome dharmas are maturation causes. It does not qualify the unwholesome
members through the immediate syntax, although those are likewise within the
contaminated causal field.

## 4. Grammar

The first half defines pervasive cause through an understood causal relation:

```text
sva-bhūmau pūrva-sarvagāḥ
    → kliṣṭānāṃ sarvatraga-ākhyaḥ [hetuḥ]

previously arisen pervasive dharmas on their own level
    → are the cause called pervasive for later afflicted dharmas
```

The genitive `kliṣṭānām` marks the affected field. The Bhāṣya clarifies that
pervasive cause can produce afflicted dharmas of another class while
remaining restricted to its own level.

The second half is another classificatory nominal definition:

```text
aśubhāḥ
kuśalāḥ ca eva sāsravāḥ
    → vipāka-hetuḥ

unwholesome dharmas
and contaminated wholesome dharmas
    → are maturation cause
```

The singular predicates name causal types under which plural dharmas are
classified.

## 5. Translation

### Close syntactic construe

> Previously arisen pervasive [dharmas] are the cause called pervasive for afflicted dharmas on their own level. Unwholesome dharmas and wholesome dharmas accompanied by outflows are maturation cause.

### Bhāṣya-informed translation

> Earlier pervasive afflictions become common causes of later afflicted dharmas within the same level, including afflictions of a different class. Maturation causes are unwholesome dharmas and contaminated wholesome dharmas: they possess causal potency and are appropriated by craving, enabling a conditioned continuum to transform toward a later, dissimilar, terminal maturation-result.

## 6. Philosophical Translation

> Affliction can condition an entire field rather than reproduce only its exact likeness. Karma operates differently: an efficacious determination appropriated by craving enters a continuum, undergoes transformation, and culminates in a result unlike its originating cause. Pervasion propagates a causal atmosphere; maturation completes a delayed genetic process.

The distinction is:

```text
sarvatraga:
    prior affliction → diverse later affliction within one level

vipāka:
    appropriated karmic cause
        → transformation of a continuum
        → dissimilar terminal result
```

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| sarvatraga-hetu | pervasive cause | prior pervasive affliction functioning as common cause of later afflicted dharmas |
| kliṣṭa | afflicted | defiled determination conditioned by afflictive causes |
| sva-bhūmi | own level | level within which pervasive causality operates |
| nikāyāntarīya | belonging to another class | afflicted result reachable beyond exact homogeneous similarity |
| vipāka-hetu | maturation cause | karmically potent cause of a matured result |
| aśubha | unwholesome | ethically negative determination capable of karmic maturation |
| kuśala sāsrava | contaminated wholesome | wholesome but still accompanied by outflows and connected to a realm |
| avyākṛta | indeterminate | ethically neutral and too weak to generate maturation in this account |
| anāsrava | uncontaminated | not moistened by craving and not connected with a realm-bound maturation |
| vipāka-dharmatva | nature or capacity of producing maturation | positive causal qualification of a maturation cause |
| tṛṣṇābhiṣyandita | moistened by craving | Bhāṣya image for appropriation into a realm-bound karmic series |
| santati-pariṇāma-viśeṣaja | born from a specific transformation of a continuum | genetic definition of the matured result |
| phala-paryanta | reaching a terminal result | completion distinguishing maturation from indefinite continuation |

`Sāsrava` is not the same as `niḥṣyanda`. The former marks contamination;
the latter names homogeneous causal continuation. Translating both with
English “outflow” requires explicit control of the Sanskrit term.

## 8. Logical Determination

Pervasive cause is:

```text
PervasiveAffliction(x)
AND Afflicted(y)
AND PriorTo(x, y)
AND SameLevel(x, y)
    → SarvatragaHetu(x, y)
```

It is broader than homogeneous cause with respect to class:

```text
SarvatragaHetu(x, y)
    ⇏ SameClass(x, y)

SabhagaHetu(x, y)
    → RelevantSimilarity(x, y)
```

Maturation eligibility is:

```text
Unwholesome(x)
    → EligibleVipakaHetu(x)

Wholesome(x)
AND Contaminated(x)
    → EligibleVipakaHetu(x)
```

The Bhāṣya's exclusions expose two necessary dimensions:

```text
Indeterminate(x)
    → InsufficientPotency(x)
    → NOT VipakaHetu(x)

Uncontaminated(x)
    → NOT AppropriatedByCraving(x)
    AND NOT RealmBound(x)
    → NOT VipakaHetu(x)
```

The seed analogy yields the eligibility matrix:

| Cause profile | Potent seed | Moistened by craving | Maturation |
|---|---:|---:|---:|
| indeterminate | no | not decisive | no |
| uncontaminated | yes | no | no |
| unwholesome or contaminated wholesome | yes | yes | yes |

Maturation itself is:

```text
VipakaResult(r, c) :=
    DissimilarInKind(r, c)
    AND SpecificContinuumTransformation(c, r)
    AND TerminalResult(r)
```

This excludes the other causal forms from strict ripening:

```text
SahabhuHetu OR SamprayuktakaHetu
    → no result born from terminal continuum-transformation

SabhagaHetu
    → potentially recurrent homogeneous continuation
    → no necessary terminal completion
```

The Bhāṣya also treats karmic maturation as producing organized result
complexes rather than isolated atoms. Depending on the karma, the maturation
may comprise from one through eleven sense-spheres.

## 9. Interpretive Note

VAK 2.54 completes the sixfold `hetu` system by distinguishing field-like
contamination from terminal karmic transformation.

`Sarvatraga-hetu` explains how an affliction can reproduce a wider afflicted
field than its own exact class. It is therefore not another homogeneous edge:

```text
homogeneous cause
    → typed continuity through similarity

pervasive cause
    → contamination propagated across afflicted classes
```

`Vipāka-hetu` introduces a different temporal architecture. Its result need
not resemble the cause. The intelligible identity lies instead in the
transformation of the continuum connecting them:

```text
cause ≠ result in manifest form

but:

cause → appropriated continuum → transformation → result
```

This makes provenance indispensable. One cannot infer the causal type from
surface similarity alone; the Ocular Schema must retain the intervening
continuum and its terminal completion.

The software analogy can now distinguish two causal control forms:

```python
def homogeneous_series(state):
    while state.can_continue:
        state = state.next_of_same_causal_kind()
        yield state

def maturation_process(continuum):
    while not continuum.is_terminal:
        continuum = continuum.transform()
    return continuum.dissimilar_matured_result()
```

`Niḥṣyanda` resembles repeated `yield` because it continues a causal kind.
`Vipāka` resembles a terminal `return` after internal transformation. These
are Organon analogies, not translations of the Sanskrit or claims that karma
is literally software execution.

The result classifications also return us to the āyatana architecture. Karma
can mature not merely as one property but as a structured complex of
faculties and fields—for example life alone, mind with Dharma-sphere, or a
sensory faculty together with body, tangible, and Dharma spheres. The Kośa
therefore models a maturation as an Ocular result-schema of variable breadth.

The six causes are now distinguishable as:

```text
kāraṇa       permissive or productive conditioning
sahabhū      co-arisen causal participation
sabhāga      prior homogeneous continuation
saṃprayukta  fivefold associated Citta-complex
sarvatraga   pervasive afflicted propagation
vipāka       terminal maturation through continuum-transformation
```

This is the Kośa as Technē: not one occult Cause, but an exposed causal schema
whose relations preserve their own scope, direction, and result-form.

The textual layers are:

```text
kārikā
    → defines pervasive and maturation causes

Bhāṣya
    → explains cross-class affliction, causal eligibility,
      craving-appropriation, continuum-transformation,
      terminality, and variable result-complexes

Organon reconstruction
    → contrasts field propagation, homogeneous yielding,
      and terminal maturation in an Ocular causal schema
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:SarvatragaHetu a organon:FieldPropagationCause .
vak:VipakaHetu a organon:TerminalTransformationCause .

vak:ContaminatedWholesome a organon:EthicalCausalProfile .
vak:Unwholesome a organon:EthicalCausalProfile .
vak:Indeterminate a organon:EthicalCausalProfile .
vak:Uncontaminated a organon:EthicalCausalProfile .

organon:CausalPotency a organon:EligibilityCondition .
organon:CravingAppropriation a organon:EligibilityCondition .
organon:RealmConnection a organon:EligibilityCondition .
organon:ContinuumTransformation a organon:CausalProcess .
organon:TerminalResult a organon:ResultProfile .
organon:DissimilarResult a organon:ResultProfile .

vak:VipakaHetu organon:requires organon:CausalPotency,
        organon:CravingAppropriation,
        organon:RealmConnection .

vak:VipakaResult organon:requires organon:ContinuumTransformation,
        organon:TerminalResult,
        organon:DissimilarResult .

organon:OcularMaturationSchema a organon:OcularSchema ;
    organon:requires organon:CausalProvenance,
        organon:ContinuumIdentity,
        organon:TransformationHistory,
        organon:TerminalResult,
        organon:ResultSphereComplex .

vak:HomogeneousOutflow organon:projectAnalogy organon:YieldContinuation .
vak:VipakaResult organon:projectAnalogy organon:TerminalReturn .
```
