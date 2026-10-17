# VAK_8.26 — Objects and Aspects of the Further Samādhis

## 1. Sanskrit (Devanāgarī)

```sanskrit
आलम्बेते अशैक्षं द्वौ शून्यतश्चाप्यनित्यतः ।
आनिमित्तानिमित्तस्तु शान्ततोऽसंख्यया क्षयम् ॥ ८.२६ ॥
```

## 2. Sanskrit (IAST)

```text
ālambete aśaikṣaṃ dvau śūnyataś cāpy anityataḥ |
ānimittānimittas tu śāntato 'saṃkhyayā kṣayam || 8.26 ||
```

The Sanskrit follows the local kārikā witness. The
running verse has `akṣaikṣaṃ`, but the repeated
aśaikṣa in the explanatory prose supports the local
reading. The last clause's compressed cessation expression
is resolved explicitly as apratisaṃkhyānirodha.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `ālambete` | third-person dual present middle of ā-√lamb | the two take as object |
| `aśaikṣam` | accusative singular masculine, qualifying understood samādhim | an adept's [samādhi], belonging to one beyond training |
| `dvau` | nominative dual masculine | the two further samādhis |
| `śūnyataḥ` | adverbial form with -tas | under the aspect of emptiness |
| `anityataḥ` | adverbial form with -tas | under the aspect of impermanence |
| `ānimittānimittaḥ` | nominative singular masculine | signlessness-of-signlessness |
| `tu` | contrast particle | however |
| `śāntataḥ` | adverbial form with -tas | under the aspect of peace |
| `asaṃkhyayā` | instrumental singular feminine, compressed expression | without discriminative analysis, as resolved in prose |
| `kṣayam` | accusative singular masculine | cessation, here the specified non-analytical cessation |

`Śūnyataḥ + ca` yields `śūnyataś ca`;
`ca + api` yields `cāpi`; `ānimitta + ānimitta`
yields `ānimittānimitta`; `śāntataḥ + asaṃkhyayā`
yields `śāntato 'saṃkhyayā`.

## 4. Grammar

The dual subject selects the first two further samādhis and one shared adept-object; emptiness and impermanence are distributed to them. `Tu` marks a different object construction for signlessness-of-signlessness, whose cessation type is supplied by the Bhāṣya.

```nltk-fcfg
% start S
# tokens: ∅-aparasamādhī dvau ∅-samādhi aśaikṣam ālambete śūnyataḥ ca api anityataḥ ānimittānimittaḥ tu śāntataḥ asaṃkhyayā kṣayam
S -> CL[K=first_two] CL[K=third]
CL[K=first_two] -> N[CASE=nom,NUM=du,GEN=m,SUPPLIED=prose] NUMR[CASE=nom,NUM=du,GEN=m] N[CASE=?c,NUM=?n,GEN=?g,SUPPLIED=prose] ADJ[CASE=?c,NUM=?n,GEN=?g] V[PERS=3,NUM=du,TENSE=pres,VOICE=mid] ADV[ASPECT=emptiness] PTCL[ADD=yes] PTCL[EMPH=yes] ADV[ASPECT=impermanence]
CL[K=third] -> N[CASE=nom,NUM=sg,GEN=m] PTCL[CONTRAST=yes] ADV[ASPECT=peace] ABL[CASE=ins,NUM=sg,GEN=f,TYPE=cessation] N[CASE=acc,NUM=sg,GEN=m,TYPE=cessation]
N[CASE=nom,NUM=du,GEN=m,SUPPLIED=prose] -> '∅-aparasamādhī'
NUMR[CASE=nom,NUM=du,GEN=m] -> 'dvau'
N[CASE=acc,NUM=sg,GEN=m,SUPPLIED=prose] -> '∅-samādhi'
ADJ[CASE=acc,NUM=sg,GEN=m] -> 'aśaikṣam'
V[CASE=none,NUM=du,GEN=none,PERS=3,TENSE=pres,VOICE=mid] -> 'ālambete'
ADV[CASE=none,NUM=none,GEN=none,ASPECT=emptiness] -> 'śūnyataḥ'
PTCL[CASE=none,NUM=none,GEN=none,ADD=yes] -> 'ca'
PTCL[CASE=none,NUM=none,GEN=none,EMPH=yes] -> 'api'
ADV[CASE=none,NUM=none,GEN=none,ASPECT=impermanence] -> 'anityataḥ'
N[CASE=nom,NUM=sg,GEN=m] -> 'ānimittānimittaḥ'
PTCL[CASE=none,NUM=none,GEN=none,CONTRAST=yes] -> 'tu'
ADV[CASE=none,NUM=none,GEN=none,ASPECT=peace] -> 'śāntataḥ'
ABL[CASE=ins,NUM=sg,GEN=f,TYPE=cessation] -> 'asaṃkhyayā'
N[CASE=acc,NUM=sg,GEN=m,TYPE=cessation] -> 'kṣayam'
```

```nltk-dep
'ālambete' -> '∅-aparasamādhī' | 'dvau' | '∅-samādhi' | 'śūnyataḥ' | 'anityataḥ'
'ānimittānimittaḥ' -> 'tu' | 'kṣayam' | 'śāntataḥ' | 'asaṃkhyayā'
'kṣayam' -> 'aśaikṣam'
```

The first two objects are corresponding adept samādhis, not one undifferentiated object
relation; `asaṃkhyayā` is resolved as non-analytical cessation. The third clause must not
inherit either aspect/object pairing.


**Close construe.** The first two take corresponding
adept samādhis as objects under emptiness and impermanence,
respectively. The third takes the non-analytical cessation
of an adept's signless samādhi under peace.

## 5. Translation

### Literal Translation

> The two take an adept's [samādhi] as object,
> under emptiness and under impermanence. Signlessness-of-signlessness,
> however, [takes] cessation without analysis under
> the aspect of peace.

### Bhāṣya-informed study translation

> The two [further samādhis] take an adept's samādhi as object, under emptiness
> and under impermanence respectively; but signlessness-of-signlessness takes
> non-analytical cessation as its object, under the aspect of peace.

## 6. Philosophical Translation

> The further samādhis do not simply repeat the
> first triad's aspects. Each selects an aspect
> appropriate to its specified object. The first
> two take adept samādhis directly; the third takes
> a particular cessation associated with the adept's
> signless samādhi. That difference prevents a uniform
> formula of direct self-observation.

An uncontaminated samādhi can be considered impermanent
without thereby being reclassified as contaminated.
Likewise, the non-analytical cessation associated with
it must not be equated with liberating disjunction
from a contaminated dharma.

## 7. Technical Vocabulary

**`Aśaikṣa`.** Belonging to an adept, one beyond
training. It qualifies the samādhi taken as object
or specified in the cessation relation. It does
not, merely by grammatical transfer, establish that
the further samādhi itself is uncontaminated.

**`Dūṣaṇīyatva`.** Being approached as something to
be depreciated or criticized. This supplies the
reason for excluding the affirmative path-aspects in
the second case. It does not assert that the
uncontaminated path has become an unwholesome dharma.

**`Atallakṣaṇatva`.** Not having those characteristics.
The uncontaminated object does not bear suffering
and origin characteristics in the relevant truth-aspect
classification, so those aspects are excluded.

**`Apratisaṃkhyānirodha`.** Non-analytical cessation, the
established unconditioned category of non-arising without
analytical disjunction. It is not simply the momentary
perishing of a conditioned event or a technique
of stopping thought.

**`Pratisaṃkhyānirodha`.** Analytical cessation, disjunction
attained through discriminative knowing. The prose
excludes it for the uncontaminated samādhi concerned;
the object is not a contaminant from which liberating
disjunction must be achieved.

**`Śānta`.** Peaceful. This is the selected aspect
for the third further samādhi. Selecting it does
not license importing all four cessation aspects
from first-order signless samādhi.

**`Avyākṛta / avisaṃyoga`.** Ethically indeterminate /
not disjunction. These qualify the non-analytical cessation
in the explanation of the excluded aspects. Ethical
indeterminacy here is not neutral feeling.

## 8. Logical Determination

The first two further samādhis have corresponding adept samādhis as objects, with emptiness and impermanence respectively; signlessness-of-signlessness instead takes non-analytical cessation under peace. The prose supplies the object identities and resolves `asaṃkhyayā kṣayam` as *apratisaṃkhyānirodha*. `[verse]` / `[prose]`.

**Signature.** `Takes(s,o)`; `AspectOf(s,a)`; `AdeptSamadhi(o)`; `NonAnalyticalCessation(o)`; `Aspect(a)`.

```nltk-valuation
emptyFurther => emptyFurther
nonDirectedFurther => nonDirectedFurther
signlessFurther => signlessFurther
adeptEmpty => adeptEmpty
adeptNonDirected => adeptNonDirected
cessationOfAdeptSignless => cessationOfAdeptSignless
emptinessAspect => emptinessAspect
impermanence => impermanence
peace => peace
Takes => {(emptyFurther,adeptEmpty),(nonDirectedFurther,adeptNonDirected),(signlessFurther,cessationOfAdeptSignless)}
AspectOf => {(emptyFurther,emptinessAspect),(nonDirectedFurther,impermanence),(signlessFurther,peace)}
AdeptSamadhi => {adeptEmpty, adeptNonDirected}
NonAnalyticalCessation => {cessationOfAdeptSignless}
Aspect => {emptinessAspect, impermanence, peace}
```

```nltk-fol
# THEORY shared
# [verse, prose] first further samādhi: adept emptiness samādhi under emptiness
Takes(emptyFurther,adeptEmpty)
AspectOf(emptyFurther,emptinessAspect)
# [verse, prose] second: adept non-directed samādhi under impermanence
Takes(nonDirectedFurther,adeptNonDirected)
AspectOf(nonDirectedFurther,impermanence)
# [verse, prose] tu marks the distinct third object construction
Takes(signlessFurther,cessationOfAdeptSignless)
AspectOf(signlessFurther,peace)
all x.(AdeptSamadhi(x) -> -NonAnalyticalCessation(x))
all x.(NonAnalyticalCessation(x) -> -AdeptSamadhi(x))
```

**Results (NLTK).** The checker reports `shared: T` in the supplied finite model. The six ground object/aspect assertions and the stated object-kind distinction are satisfied there.

**Scope cautions.** The third object is cessation associated with an adept's signless samādhi, not that samādhi itself. These assignments do not copy the earlier four/two/ten distribution; the absence of analytical cessation is not a denial of impermanence.

## 9. Interpretive Note

**Correction of the cessation rendering.**
“Cessation through non-discrimination” is too open-ended
without the technical identification. The Bhāṣya
expressly names apratisaṃkhyānirodha and attaches it
to an adept's signless samādhi. That complete
object relation belongs in the study translation.

**Witness cautions.** The running verse's akṣaikṣaṃ
is controlled by the repeated aśaikṣa in prose.
The source also prints pratisaṃkhayānirodha and splits
the final causal compound across a line. The
technical contrast and three ordered reasons remain
intelligible. The local study's readings are used
with these differences disclosed; originals remain untouched.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
The project's “reflexive Recognition” vocabulary can
express the further relation to an attained samādhi,
provided the third member's cessation object remains
explicit. Yoga Vidyā articulates object status and
admissible aspect; Yoga Technē, its kriyā–karma companion,
concerns the operative orientation described in the
commentary, including the second case's depreciation.

The research comparison with Yoga's artha-mātra-nirbhāsa
and the determinate Concept belongs to comparative
interpretation. This Kośa passage supplies object–aspect
constraints; it does not itself rank Yoga above
the further samādhis. For Organon representation,
retain those constraints rather than treating reflection
as unrestricted application of any predicate to any
prior attainment.

**Review status.** Provisional, Bhāṣya-controlled study.
The two direct objects, third cessation object,
three selected aspects, exclusions and their reasons,
and aśaikṣa witness correction have been checked
against the local research and running source.

## 10. OWL++ Seed

```text
Class: FurtherSamadhi
Class: AdeptSamadhi
Class: NonAnalyticalCessation
Class: SelectedAspect

ObjectProperty: takesAsObject
ObjectProperty: apprehendsUnderAspect
ObjectProperty: cessationAssociatedWith

SunyataSunyata:
    object: AdeptSunyataSamadhi
    aspect: Emptiness

ApranihitaApranihita:
    object: AdeptApranihitaSamadhi
    aspect: Impermanence
    excludedAspects: Suffering, OriginAspects, PathAspects

AnimittaAnimitta:
    object: ApratisamkhyaNirodhaOfAdeptAnimittaSamadhi
    aspect: Peace
    excludedAspects: Cessation, Excellence, Emergence

ProjectConstraint: Preserve the third member's cessation object.
ProjectConstraint: Non-analytical cessation is not momentary conditioned perishing.
ProjectConstraint: Uncontaminated samadhi remains impermanent.
ProjectConstraint: Path-aspect exclusion does not deny the object's path status.
ProjectConstraint: Object mode does not automatically transfer to the further samadhi.
ProjectConstraint: Keep the three cessation-aspect exclusions and reasons distinct.
ProjectConstraint: Further-samadhi mode and practitioner rules continue in VAK 8.27.
```

This is a declarative project seed, not executable OWL.
VAK 8.27 next specifies the further samādhis' mode,
human occurrence, practitioner, and levels.
