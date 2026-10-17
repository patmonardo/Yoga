# VAK_8.24 — Three Samādhis and the Sixteen Truth-Aspects

## 1. Sanskrit (Devanāgarī)

```sanskrit
आनिमित्तः शमाकारैः शून्यतानात्मशून्यतः ।
प्रवर्ततेऽप्रणिहितः सत्याकारैरतः परैः ॥ ८.२४ ॥
```

## 2. Sanskrit (IAST)

```text
ānimittaḥ śamākāraiḥ śūnyatānātmaśūnyataḥ |
pravartate 'praṇihitaḥ satyākārair ataḥ paraiḥ || 8.24 ||
```

The verse follows the local kārikā study's provisional
śamākāraiḥ, “through the aspects of peace.” The
running witness reads samākāraiḥ. The commentary
securely identifies the four cessation-truth aspects,
but this semantic control does not itself establish
a critical correction of the consonant. The adopted
reading remains explicitly provisional.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `ānimittaḥ` | nominative singular masculine | signless [samādhi] |
| `śamākāraiḥ` | instrumental plural masculine; provisional reading | through the aspects of peace, resolved as cessation aspects |
| `śūnyatā` | nominative singular feminine | emptiness [samādhi designation] |
| `anātmaśūnyataḥ` | compressed adverbial expression with -tas | through non-self and emptiness |
| `pravartate` | third-person singular present middle of pra-√vṛt | proceeds, operates |
| `apraṇihitaḥ` | nominative singular masculine | non-directed or wishless [samādhi] |
| `satyākāraiḥ` | instrumental plural masculine | through aspects of the truths |
| `ataḥ` | pronominal adverb | other than these, in the present comparison |
| `paraiḥ` | instrumental plural masculine adjective | other, remaining |

`Śama + ākāraiḥ` yields `śamākāraiḥ`;
`śūnyatā + anātma-` yields `śūnyatānātma-`;
`pravartate + apraṇihitaḥ` yields `pravartate
'praṇihitaḥ`. The prose expands the second expression
as association with the two aspects anātman and śūnyatā.

## 4. Grammar

The clauses name three samādhis and assign their aspects; the verb is shared by ellipsis. Instrumental agreement links each aspect phrase to its samādhi, while `paraiḥ` is restricted to the remainder of the truth-aspects.

```nltk-fcfg
% start S
# tokens: ānimittaḥ śamākāraiḥ śūnyatā ∅-samādhi anātmaśūnyataḥ apraṇihitaḥ satyākāraiḥ ataḥ paraiḥ pravartate
S -> CL[K=signless] CL[K=emptiness] CL[K=non_directed] V[PERS=3,NUM=sg,TENSE=pres,VOICE=mid]
CL[K=signless] -> N[CASE=?c,NUM=?n,GEN=?g] N[CASE=ins,NUM=pl,GEN=?g,ROLE=aspect]
CL[K=emptiness] -> N[CASE=nom,NUM=sg,GEN=f] N[CASE=nom,NUM=sg,GEN=m,SUPPLIED=prose] ADV[ASPECT=two]
CL[K=non_directed] -> N[CASE=nom,NUM=sg,GEN=m] N[CASE=ins,NUM=pl,GEN=m,ROLE=aspect] ADV[ORDER=other] ADJ[CASE=ins,NUM=pl,GEN=m,ROLE=remainder]
N[CASE=nom,NUM=sg,GEN=m] -> 'ānimittaḥ'
N[CASE=ins,NUM=pl,GEN=m,ROLE=aspect] -> 'śamākāraiḥ' | 'satyākāraiḥ'
N[CASE=nom,NUM=sg,GEN=f] -> 'śūnyatā'
N[CASE=nom,NUM=sg,GEN=m,SUPPLIED=prose] -> '∅-samādhi'
ADV[CASE=none,NUM=none,GEN=none,ASPECT=two] -> 'anātmaśūnyataḥ'
N[CASE=nom,NUM=sg,GEN=m] -> 'apraṇihitaḥ'
ADV[CASE=none,NUM=none,GEN=none,ORDER=other] -> 'ataḥ'
ADJ[CASE=ins,NUM=pl,GEN=m,ROLE=remainder] -> 'paraiḥ'
V[CASE=none,NUM=sg,GEN=none,PERS=3,TENSE=pres,VOICE=mid] -> 'pravartate'
```

```nltk-dep
'ānimittaḥ' -> 'śamākāraiḥ'
'śūnyatā' -> '∅-samādhi' | 'anātmaśūnyataḥ'
'apraṇihitaḥ' -> 'satyākāraiḥ' | 'ataḥ'
'satyākāraiḥ' -> 'paraiḥ'
'pravartate' -> 'ānimittaḥ' | 'śūnyatā' | 'apraṇihitaḥ'
```

The supplied head makes the feminine designation local; it does not
change the masculine subjects ānimitta and apraṇihita. The commentary
resolves the first group as four cessation aspects and `ataḥ paraiḥ` as
the other ten, while the object relation to nirvāṇa remains separate.


**Close construe.** Signless samādhi proceeds through
the cessation aspects; emptiness samādhi through non-self
and emptiness; non-directed samādhi through the remaining
truth-aspects.

## 5. Translation

### Literal Translation

> Signless [samādhi proceeds] through the aspects of
> peace; [samādhi of] emptiness [proceeds] through non-self and emptiness.
> Non-directed [samādhi proceeds] through the other
> aspects of the truths.

### Bhāṣya-informed study translation

> Signless samādhi proceeds through the four aspects of cessation;
> emptiness samādhi through the two aspects, non-self and emptiness;
> and non-directed samādhi through the remaining aspects of the truths.

## 6. Philosophical Translation

> The three samādhis are distinguished through their
> determinate relation to truth-aspects. Signlessness
> takes cessation as its object under four aspects;
> emptiness proceeds under its two specified aspects;
> non-direction concerns the remaining aspects, including
> the path as something serving passage beyond itself.

The names therefore do not indicate an absence
of all cognitive content. Nor does non-direction
mean abandoning the work of the path before its
purpose is accomplished: the raft comparison concerns
its eventual relinquishment.

## 7. Technical Vocabulary

**`Ākāra`.** Aspect, the determinate mode under which
a truth is apprehended. The count in this verse
partitions the established sixteen aspects; it does
not introduce sixteen new objects or techniques.

**`Ānimitta / animitta`.** Signless samādhi / signless
nirvāṇa. The prose explains the former by its
object, the latter by absence of the ten signs.
The two grammatical forms should not obscure that
object-based explanation.

**`Daśanimitta`.** Ten signs: five sensory object
fields, female and male signs, and the three
marks of the conditioned. The local prose names
these groups without separately spelling out every
conditioned mark; their group-count is sufficient
for the present explanation.

**`Śūnyatā-samādhi`.** Emptiness samādhi, associated
with the non-self and emptiness aspects. The twofold
specification should remain explicit rather than being
replaced with an unrestricted philosophical theory of emptiness.

**`Apraṇihita`.** Non-directed or wishless. The prose
explains its name through recoil from impermanence,
suffering, and their causes, together with the
path's eventual relinquishment. It does not equate
this orientation with apathy or inability to act.

**`Udvega`.** Recoil, alarm, or disquiet in relation
to the specified conditioned determinations. The
passage distinguishes its application from the treatment
of emptiness and non-self.

**`Kolopamatā`.** Being like a raft. The analogy
supports the path's instrumental role and eventual
relinquishment; it is part of the commentary's
explanation of non-directed samādhi.

**`Nirvāṇasāmānya`.** Commonality with nirvāṇa. This
is the stated reason why emptiness and non-self
do not occasion the same recoil. It does not
identify every empty or non-self conditioned dharma
with nirvāṇa.

## 8. Logical Determination

The verse partitions sixteen truth-aspects among three samādhis: four for signless, two for emptiness, and the remainder for non-directed. `[verse]` supplies the partition; `[prose]` resolves the first instrumental as cessation-aspects and explains signlessness through its object, nirvāṇa.

**Signature.** `Samadhi(x)`; `Aspect(x)`; `Assign(s,a)` (samādhi `s` is assigned aspect `a`).

**Dataset (the sixteen assignments).** The extension records the prose's four/two/ten split; cessation and peace are individual aspects, while nirvāṇa is not treated as one of the sixteen aspect labels.

```nltk-valuation
signless => signless
emptiness => emptiness
nondirected => nondirected
cessation1 => cessation1
cessation2 => cessation2
cessation3 => cessation3
cessation4 => cessation4
nonself => nonself
emptinessAspect => emptinessAspect
impermanence1 => impermanence1
suffering1 => suffering1
origin1 => origin1
origin2 => origin2
origin3 => origin3
origin4 => origin4
path1 => path1
path2 => path2
path3 => path3
path4 => path4
Samadhi => {signless, emptiness, nondirected}
Aspect => {cessation1, cessation2, cessation3, cessation4, nonself, emptinessAspect, impermanence1, suffering1, origin1, origin2, origin3, origin4, path1, path2, path3, path4}
Assign => {(signless,cessation1),(signless,cessation2),(signless,cessation3),(signless,cessation4),(emptiness,nonself),(emptiness,emptinessAspect),(nondirected,impermanence1),(nondirected,suffering1),(nondirected,origin1),(nondirected,origin2),(nondirected,origin3),(nondirected,origin4),(nondirected,path1),(nondirected,path2),(nondirected,path3),(nondirected,path4)}
```

```nltk-fol
# THEORY shared
# [verse] first group; [prose] resolved as four cessation aspects
all a.(Assign(signless,a) -> Aspect(a))
# [verse] emptiness and non-self
all a.(Assign(emptiness,a) -> Aspect(a))
# [verse] ataḥ paraiḥ; [prose] the ten remaining aspects
all a.(Assign(nondirected,a) -> Aspect(a))
# [prose] every represented aspect belongs to one of the three groups
all a.(Aspect(a) -> (Assign(signless,a) | Assign(emptiness,a) | Assign(nondirected,a)))
```

**Results (NLTK).** `check_logic.py` parses the blocks and reports `shared: T` for this finite model.

**Scope cautions.** The ten signs explaining the name ānimitta are a separate classification, not these ten remaining aspects. The model does not make nirvāṇa one of the sixteen, and the path's eventual relinquishment does not negate its present assignment to non-directed samādhi.

## 9. Interpretive Note

**The provisional consonant reading is not a new doctrine.**
The local study adopts śamākāraiḥ where the running
source reads samākāraiḥ. The commentary securely
determines cessation's four aspects, but the exact
verse reading remains a textual question. The
translation follows that secure meaning and discloses
the adopted form.

**Other witness cautions.** The running source has
`śunyataḥ`, a damaged `samādhidvarcyākāraḥ`, and
`samādhipraṇihito`. The local extract regularizes
the two-aspected emptiness statement and the apraṇihita
name. The explicit dual aspect expression and
subsequent daśākāra statement secure the counts.
Original witnesses remain unchanged.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
The research study uses “Recognition” for samādhi
and interprets it as the determinate Concept. This
project vocabulary can articulate how an already
specified field of meaning is comprehended without
reducing samādhi to a bare list of features.
It remains distinguished from the source's own
explanation through aspects, objects, and the named samādhis.

Yoga Vidyā articulates the sixteen-aspect field and
its threefold distribution. Yoga Technē, its kriyā–karma
companion, concerns the operation and relinquishment
described in the commentary. The raft analogy
links the means to its purpose without erasing
the work performed by the means.

For Organon representation, preserve aspect membership,
object relation, and explanatory rationale separately.
No external logical triad is needed to supply
the three names: the Bhāṣya provides their local
determinations. This is a controlled project reconstruction,
not an attribution of the Organon Concept to Vasubandhu.

**Review status.** Provisional, Bhāṣya-controlled study.
The 4–2–10 partition, ten-sign grouping, nirvāṇa
object relation, non-direction rationale, raft analogy,
and commonality-with-nirvāṇa clause have been checked
against the local research and running source.
The śamākāraiḥ reading remains provisional.

## 10. OWL++ Seed

```text
Class: SamadhiType
Class: TruthAspect
Class: ObjectRelation
Class: ExplanatoryRationale

ObjectProperty: operatesThroughAspect
ObjectProperty: takesAsObject
ObjectProperty: explainedBy

AnimittaSamadhi:
    aspects: FourCessationAspects
    aspectCount: 4
    object: Nirvana
    nameExplanation: ObjectFreeFromTenSigns

SunyataSamadhi:
    aspects: NonSelf, Emptiness
    aspectCount: 2

ApranihitaSamadhi:
    aspects: Impermanence, Suffering, FourOriginAspects, FourPathAspects
    aspectCount: 10
    rationale: RecoilFromSpecifiedConditionedDeterminations,
               EventualRelinquishmentOfPathLikeRaft

TenSigns:
    groups: FiveSensoryObjectFields, FemaleAndMaleSigns, ThreeConditionedMarks
    count: 10

ProjectConstraint: Truth-aspect total is 4 plus 2 plus 10 equals 16.
ProjectConstraint: Ten signs and ten non-directed aspects are different inventories.
ProjectConstraint: Signlessness retains a specified object and four aspects.
ProjectConstraint: Eventual path relinquishment does not negate its present use.
ProjectConstraint: Preserve the provisional verse reading explicitly.
ProjectConstraint: Recognition vocabulary belongs to the labeled Organon layer.
ProjectConstraint: Pure and uncontaminated mode classification continues in VAK 8.25.
```

This is a declarative project seed, not executable OWL.
VAK 8.25 next determines the modes of these samādhis,
the gates of liberation, and the further reflexive triad.
