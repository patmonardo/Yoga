# VAK_1.33

## 1. Sanskrit (Devanāgarī)

> निरूपणानुस्मरणविकल्पेनाविकल्पकाः ।
>
> तौ प्रज्ञा मानसी व्यग्रा स्मृतिः सर्वैव मानसी ॥ १.३३ ॥

## 2. Sanskrit (IAST)

> nirūpaṇānusmaraṇavikalpenāvikalpakāḥ /
>
> tau prajñā mānasī vyagrā smṛtiḥ sarvaiva mānasī // 1.33 //

## 3. Padaccheda

```text
nirūpaṇānusmaraṇavikalpena
    → nirūpaṇa-anusmaraṇa-vikalpena

avikalpakāḥ        → a-vikalpakāḥ
tau                → tau
prajñā mānasī      → prajñā mānasī
vyagrā             → vyagrā
sarvaiva           → sarvā eva
```

| Form | Morphology | Lexical force here |
|---|---|---|
| nirūpaṇa | compound member | examination, determination, discriminative specification |
| anusmaraṇa | compound member | recollection, renewed or reproductive remembering |
| vikalpena | instrumental masculine singular | with respect to discrimination; by the discriminative operation |
| a-vikalpakāḥ | nominative masculine plural adjective | conventionally called non-discriminative in the restricted sense specified |
| tau | nominative masculine dual pronoun | those two: determining and recollective discrimination |
| prajñā | nominative feminine singular | discernment or discriminative understanding |
| mānasī | nominative feminine singular adjective | mental; associated with mental knowledge |
| vyagrā | nominative feminine singular adjective | dispersed, distracted, unconcentrated |
| smṛtiḥ | nominative feminine singular | memory, recollection |
| sarvā eva | emphatic nominative feminine singular | all of it without exception |

The Kārikā has `nirūpaṇa`; the Bhāṣya names the corresponding full category
`abhinirūpaṇa-vikalpa`. The two should be related without silently replacing
the transmitted verse.

## 4. Grammar

The understood subject of `avikalpakāḥ` is the five sensory knowledge-Domains
from VAK 1.32. The instrumental compound restricts the negation:

```text
nirūpaṇa-anusmaraṇa-vikalpena
    with respect to determining and recollective discrimination

avikalpakāḥ
    they are non-discriminative
```

The verse does not say that sensory knowledge lacks every form of
discrimination. The Bhāṣya resolves the apparent contradiction by reporting
three kinds of `vikalpa`:

```text
svabhāva-vikalpa
    intrinsic or elementary discrimination
    = vitarka

abhinirūpaṇa-vikalpa
    examining or determining discrimination
    = unconcentrated mental prajñā

anusmaraṇa-vikalpa
    recollective discrimination
    = all mental smṛti
```

Sensory knowledge possesses the first and lacks the latter two. It is called
`avikalpaka` by conventional abbreviation, just as the Bhāṣya says that a
horse with only one foot may be called “footless.”

The dual `tau` refers to determining and recollective discrimination. Their
definitions are distributed across the second line:

```text
[nirūpaṇa-vikalpa]
    = prajñā that is mental and unconcentrated

[anusmaraṇa-vikalpa]
    = smṛti, all of which is mental
```

The Bhāṣya glosses `vyagrā` with `asamāhitā`, “unconcentrated.” Hence the
first definition does not include every possible instance of prajñā.

## 5. Translation

### Close syntactic construe

> [The five sensory knowledge-Domains] are non-discriminative with respect to determining and recollective discrimination. Those two are, respectively, unconcentrated mental discernment and memory, all of which is mental.

### Bhāṣya-informed translation

> Sensory knowledge is called non-discriminative only because it lacks the developed discriminations of mental examination and recollection; it still possesses intrinsic discrimination, identified with vitarka. Determining discrimination is unconcentrated discernment associated with mental knowledge, while recollective discrimination is memory, which belongs entirely to the mental sphere whether concentrated or unconcentrated.

This translation preserves the relative force of `avikalpaka` and prevents
“nonconceptual” from being mistaken for cognitively blank sensation.

## 6. Philosophical Translation

> Sensory knowing already differentiates, but it does not yet determine through mental examination or reproduce through memory. Determination arises when discernment operates in unconcentrated mental activity; reproduction arises through memory, which is wholly mental. Cognition therefore develops through distinct and irreducible powers rather than leaping directly from sensation to a finished concept.

Organon rendering:

> The Seed unfolds a graded synthesis. Immediate sensory knowledge carries intrinsic discrimination; manas adds determinate examination and the reproduction of what is no longer immediately present. Only by distinguishing these operations can the later Vārttika ask how recognition, conceptual unity, and rational agency emerge from their cooperation.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| vikalpa | discrimination / differentiating construction | genus with three forms in the Bhāṣya; not mere fantasy and not automatically a finished concept |
| svabhāva-vikalpa | intrinsic discrimination | minimal discrimination present in sensory knowledge; identified with vitarka |
| abhinirūpaṇa-vikalpa | determining or examining discrimination | unconcentrated mental prajñā |
| anusmaraṇa-vikalpa | recollective discrimination | all mental memory, concentrated or unconcentrated |
| avikalpaka | relatively non-discriminative | lacking the two developed mental forms, not all differentiation |
| nirūpaṇa | determination / examination | discriminative specification performed mentally |
| anusmaraṇa | reproductive recollection | renewed presentation through memory |
| prajñā | discernment | here specifically mental and unconcentrated, not prajñā without qualification |
| vyagra | dispersed / unconcentrated | explicitly glossed as `asamāhita` |
| smṛti | memory / recollection | wholly mental in this classification |
| mānasī | mental | requiring the mental sphere rather than sensory knowledge alone |

## 8. Logical Determination

The apparent contradiction is:

```text
VAK 1.32:
    SensoryKnowledge
        → AssociatedWith(Vitarka, Vicara)

VAK 1.33:
    SensoryKnowledge
        → Avikalpaka
```

The threefold analysis resolves it:

```text
Vikalpa
    = {SvabhavaVikalpa,
       AbhinirupanaVikalpa,
       AnusmaranaVikalpa}

SensoryKnowledge
    → Has(SvabhavaVikalpa)
    ∧ Lacks(AbhinirupanaVikalpa)
    ∧ Lacks(AnusmaranaVikalpa)
    → ConventionallyCalled(Avikalpaka)
```

The mental operations are typed separately:

```text
AbhinirupanaVikalpa(x)
    ↔ Prajna(x)
    ∧ AssociatedWith(x, MentalKnowledge)
    ∧ Unconcentrated(x)

AnusmaranaVikalpa(x)
    ↔ Smrti(x)
    ∧ Mental(x)
```

Concentration restricts the first but not the second:

```text
ConcentratedPrajna(x)
    ↛ AbhinirupanaVikalpa(x)

Smrti(x)
    → AnusmaranaVikalpa(x)
      whether Concentrated(x) or Unconcentrated(x)
```

The resulting cognitive capability stack is:

```text
intrinsic sensory discrimination
    → determining mental discrimination
    → recollective mental discrimination
```

This is a differentiation of functions, not yet a claim that they form one
Kantian transcendental synthesis.

## 9. Interpretive Note

VAK 1.33 is one of the decisive cognitive verses of the Dhātu chapter. It
refuses the crude binary in which sensory cognition is either an
undifferentiated given or already a fully conceptual judgment. Sensory
knowledge has `svabhāva-vikalpa`; it differentiates through `vitarka`. What
it lacks is the mental power to examine and determine, together with the
power to reproduce through recollection.

The Kantian comparison is therefore compelling but must remain structurally
exact:

| Kośa operation | Provisional Kantian bridge |
|---|---|
| sensory knowledge with intrinsic discrimination | synthesis of apprehension |
| `anusmaraṇa-vikalpa` as mental `smṛti` | reproduction in imagination |
| `abhinirūpaṇa-vikalpa` as mental `prajñā` | determination oriented toward recognition |

The ordering in the Kārikā is not itself Kant's transcendental deduction,
and `nirūpaṇa` is not simply identical with recognition in a concept.
Recognition requires a unity under which the reproduced manifold is known
as the same. The present verse supplies determination and reproduction as
typed cognitive powers; the Organon Vārttika must still demonstrate their
unity.

That restraint makes the comparison more powerful. We are not importing a
ready-made Kantian triad. We have found a Kośa Seed whose native articulation
makes such a triad constructible:

```text
present sensory differentiation
    + mental reproduction
    + determinate examination
        → possible recognition
```

The order also matters for Buddha Mind. The sensory level is not rejected
as darkness, and the mental level is not automatically pure. Rather, the
Basis specifies the functions that a rational cognitive agent must integrate
and the precise Domain in which each function operates. Their translation
into the Organon Vārttika will be a later systematic construction, grounded
in this analysis rather than substituted for it.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_33
    a vak:Karika ;
    rdfs:label "VAK 1.33" ;
    vak:hasTopic vak:ThreefoldVikalpa ;
    vak:belongsTo vak:Dhatunirdesa .

vak:SensoryKnowledge
    vak:hasDiscrimination vak:SvabhavaVikalpa ;
    vak:lacksDiscrimination vak:AbhinirupanaVikalpa,
        vak:AnusmaranaVikalpa ;
    vak:conventionallyCalled vak:Avikalpaka .

vak:SvabhavaVikalpa
    a vak:DiscriminationMode ;
    vak:identifiedWith vak:Vitarka .

vak:AbhinirupanaVikalpa
    a vak:DiscriminationMode ;
    vak:realizedBy vak:UnconcentratedMentalPrajna .

vak:AnusmaranaVikalpa
    a vak:DiscriminationMode ;
    vak:realizedBy vak:MentalSmrti .

organon:ApprehensionBridge
    organon:provisionallyGroundedIn vak:SensoryKnowledge .

organon:ReproductionBridge
    organon:provisionallyGroundedIn vak:AnusmaranaVikalpa .

organon:RecognitionBridge
    organon:provisionallyGroundedIn vak:AbhinirupanaVikalpa ;
    organon:requiresFurtherDerivation true .
```
