# VAK_8.29 — Four Immeasurables: Objects, Counterforces, and Mental Natures

## 1. Sanskrit (Devanāgarī)

```sanskrit
अप्रमाणानि चत्वारि व्यापादादिविपक्षतः ।
मैत्र्यद्वेषोऽपि करुणा मुदिता सुमनस्कता ॥ ८.२९ ॥
```

## 2. Sanskrit (IAST)

```text
apramāṇāni catvāri vyāpādādivipakṣataḥ |
maitry adveṣo 'pi karuṇā muditā sumanaskatā || 8.29 ||
```

The Sanskrit follows the local kārikā witness. The
Bhāṣya resolves compassion as non-hatred, like friendliness.
A grouping of compassion with gladness is not supported by the prose.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `apramāṇāni` | nominative plural neuter | immeasurables |
| `catvāri` | nominative plural neuter numeral | four |
| `vyāpādādivipakṣataḥ` | causal adverbial compound | because of opposition to ill will and the others |
| `maitrī` | nominative singular feminine | friendliness or loving-kindness |
| `adveṣaḥ` | nominative singular masculine | non-hatred |
| `api` | additive particle | also, likewise |
| `karuṇā` | nominative singular feminine | compassion |
| `muditā` | nominative singular feminine | sympathetic joy |
| `sumanaskatā` | nominative singular feminine abstract | gladness, resolved as saumanasya |

`Maitrī + adveṣaḥ` yields `maitry adveṣaḥ`;
`adveṣaḥ + api` yields `adveṣo 'pi`. The
particle api carries the non-hatred determination
forward to compassion, as the prose makes explicit.

## 4. Grammar

The verse gives the count, the counteractive rationale, and the paired mental natures. `Api` carries non-hatred to compassion; the Bhāṣya restricts `sumanaskatā` to sympathetic joy, not compassion.

```nltk-fcfg
% start S
# tokens: apramāṇāni catvāri vyāpādādivipakṣataḥ maitrī adveṣaḥ api karuṇā muditā sumanaskatā
S -> CL[K=count] CL[K=nonhatred] CL[K=joy]
CL[K=count] -> N[CASE=?c,NUM=?n,GEN=?g] NUMR[CASE=?c,NUM=?n,GEN=?g] ADV[CAUSE=yes]
CL[K=nonhatred] -> N[CASE=nom,NUM=sg,GEN=f] N[CASE=nom,NUM=sg,GEN=m] PTCL[ADD=yes] N[CASE=nom,NUM=sg,GEN=f]
CL[K=joy] -> N[CASE=nom,NUM=sg,GEN=f] N[CASE=nom,NUM=sg,GEN=f,NATURE=gladness]
N[CASE=nom,NUM=pl,GEN=n] -> 'apramāṇāni'
NUMR[CASE=nom,NUM=pl,GEN=n] -> 'catvāri'
ADV[CASE=none,NUM=none,GEN=none,CAUSE=yes] -> 'vyāpādādivipakṣataḥ'
N[CASE=nom,NUM=sg,GEN=f] -> 'maitrī' | 'karuṇā' | 'muditā'
N[CASE=nom,NUM=sg,GEN=m] -> 'adveṣaḥ'
PTCL[CASE=none,NUM=none,GEN=none,ADD=yes] -> 'api'
N[CASE=nom,NUM=sg,GEN=f,NATURE=gladness] -> 'sumanaskatā'
```

```nltk-dep
'apramāṇāni' -> 'catvāri' | 'vyāpādādivipakṣataḥ'
'maitrī' -> 'adveṣaḥ'
'karuṇā' -> 'api' | 'adveṣaḥ'
'muditā' -> 'sumanaskatā'
```

The causal expression gives the four counter-works in corresponding order; it does not imply
every affliction. The Bhāṣya preserves distinct Vaibhāṣika and preferred accounts of
impurity/equanimity, beyond what this verse resolves.


**Close construe.** There are four immeasurables,
because they counter ill will and the corresponding
other tendencies. Friendliness is non-hatred, and
compassion likewise; sympathetic joy is gladness.

## 5. Translation

### Literal Translation

> There are four immeasurables [friendliness, compassion, sympathetic joy,
> and equanimity] because they oppose ill will and the others. Friendliness
> is non-hatred, compassion also; sympathetic joy is gladness.

### Bhāṣya-informed study translation

> There are four immeasurables, because they oppose ill will and the rest:
> friendliness, compassion, sympathetic joy, and equanimity. Friendliness
> is non-hatred, and compassion is so too; sympathetic joy is gladness.

## 6. Philosophical Translation

> The group is determined through both its object
> scope and its counteractive functions. A common
> underlying mental nature does not make friendliness
> and compassion interchangeable: the commentary assigns
> them distinct counteractive roles, and their particular
> contemplative forms are developed next.

Immeasurability here has the explicit basis of
immeasurable beings as object. It is not a
claim of omniscience, nor a denial that beings
are the objects of these cultivations.

## 7. Technical Vocabulary

**`Apramāṇa`.** Immeasurable. The source explains the
name through apramāṇasattvālambanatva, taking immeasurable
beings as object-support. The explanation should
not be replaced with an abstract theory of infinity.

**`Vipakṣa / pratipakṣa`.** Opposing factor / antidote.
These terms specify counteractive function here.
The local discussion should not be expanded into
an assertion that each immeasurable independently
accomplishes irreversible destruction of every associated defilement.

**`Vyāpāda`.** Ill will, opposed by friendliness.
It also occurs in the final paired tendency
addressed by equanimity.

**`Viṃhisā`.** Harmfulness or injurious intention,
opposed by compassion in the ordered list.

**`Arati`.** Discontent or inability to rejoice,
opposed by sympathetic joy. The contextual opposition
is more specific than a generic negative feeling.

**`Adveṣa`.** Non-hatred, the mental nature assigned
to both friendliness and compassion. The source
makes a positive mental-factor identification, not
merely an observation that overt hostility happens
to be absent.

**`Saumanasya`.** Pleasant-mindedness or gladness, the
nature assigned to muditā. It is not the
nature assigned to compassion in this passage.

## 8. Logical Determination

Four immeasurables are distinguished by counteractive relation; friendliness and compassion share non-hatred as nature, while sympathetic joy is gladness. The Bhāṣya attributes two different impurity/equanimity comparisons, retaining the Vaibhāṣika account separately from the expositor's preferred account. `[verse]` / `[prose]`.

**Signature.** `Immeasurable(x)`; `Counters(x,t)`; `Nature(x,n)`; `VBCounters(x,t)` (Vaibhāṣika report); `PreferredCounters(x,t)` (preferred explanation).

```nltk-valuation
friendliness => friendliness
compassion => compassion
joy => joy
equanimity => equanimity
illWill => illWill
harmfulness => harmfulness
discontent => discontent
desireAndIllWill => desireAndIllWill
nonHatred => nonHatred
gladness => gladness
impurityPractice => impurityPractice
equanimityPractice => equanimityPractice
appearanceAttachment => appearanceAttachment
sexualDesire => sexualDesire
kinAttachment => kinAttachment
Immeasurable => {friendliness, compassion, joy, equanimity}
Counters => {(friendliness,illWill),(compassion,harmfulness),(joy,discontent),(equanimity,desireAndIllWill)}
Nature => {(friendliness,nonHatred),(compassion,nonHatred),(joy,gladness)}
VBCounters => {(impurityPractice,appearanceAttachment),(equanimityPractice,sexualDesire)}
PreferredCounters => {(impurityPractice,sexualDesire),(equanimityPractice,kinAttachment)}
```

```nltk-fol
# THEORY shared
# [verse, prose] the ordered counterworks and mental natures
all x.(Immeasurable(x) -> exists t.Counters(x,t))
Nature(friendliness,nonHatred)
Nature(compassion,nonHatred)
Nature(joy,gladness)
# THEORY vaibhasika
# [prose, Vaibhāṣika account] impurity contemplation / equanimity
VBCounters(impurityPractice,appearanceAttachment)
VBCounters(equanimityPractice,sexualDesire)
# THEORY preferred
# [prose, expositor: "this is fitting"] alternative pairing
PreferredCounters(impurityPractice,sexualDesire)
PreferredCounters(equanimityPractice,kinAttachment)
```

**Results (NLTK).** The checker reports `shared: T`, `vaibhasika: T`, and `preferred: T` in the finite model. These are speaker-attributed relations in separate theories; the check does not decide between them or test their union as an exclusive doctrine.

**Scope cautions.** The fourth counteractive relation is described more fully in 8.30. The preferred kin-attachment account is not a rejection of care for relatives. These rules do not claim irreversible abandonment of all defilements by each immeasurable.

## 9. Interpretive Note

**A Bhāṣya-controlled correction.** The research first
pass translates compassion and sympathetic joy together
as gladness. The commentary explicitly gives compassion
the same non-hatred nature as friendliness. The
original kārikā wording remains intact; its construal
and official translation follow the explanatory prose.

**Source attribution is material.** The impurity/equanimity
comparison includes a named Vaibhāṣika answer and
a preferred alternative. The latter must not be
reported as the former or as an uncontested
single account. The orthographic variation maithuna/maithūna
in the running text does not change the sexual-desire
reference in this comparison.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates object scope, counteractive
relation, and mental nature. Yoga Technē, its
kriyā–karma companion, concerns the cultivation of
those relations toward beings. The shared adveṣa
nature illustrates why systematic meaning cannot be
reduced to giving each term a unique isolated gloss.

The research's Recognition vocabulary can express
the relational extension of cultivation, but the
source does not establish that these qualities
are necessarily the acts of an already liberated
knower. For Organon representation, keep scope,
function, and nature separate, and preserve the
reported disagreement. This is project reconstruction,
not an additional doctrine attributed to Vasubandhu.

**Review status.** Provisional, Bhāṣya-controlled study.
The four names, immeasurable-object explanation,
ordered counterforces, two attributed accounts, and
three mental-nature assignments have been checked
against the local research and running source.
Original files remain untouched.

## 10. OWL++ Seed

```text
Class: Immeasurable
Class: MentalNature
Class: CounteractiveRelation
Class: ReportedAccount

ObjectProperty: takesBeingsAsObject
ObjectProperty: counteracts
ObjectProperty: hasMentalNature
ObjectProperty: attributedToAccount

FourImmeasurables:
    members: Maitri, Karuna, Mudita, Upeksa
    nameExplanation: ImmeasurableBeingsAsObjects

Maitri:
    mentalNature: NonHatred
    counteracts: IllWill

Karuna:
    mentalNature: NonHatred
    counteracts: Harmfulness

Mudita:
    mentalNature: Gladness
    counteracts: Discontent

Upeksa:
    counteracts: PredominanceOfSensualDesireAndIllWill
    mentalNature: ContinuedInVAK8_30

ProjectConstraint: Compassion is not assigned gladness as its nature here.
ProjectConstraint: Shared mental nature does not erase distinct counteractive roles.
ProjectConstraint: Preserve both impurity-equanimity accounts with attribution.
ProjectConstraint: Familial attachment is not identical with compassionate care.
ProjectConstraint: Immeasurable object scope does not imply omniscience.
ProjectConstraint: Do not infer irreversible liberation from the opening counterforce list.
```

This is a declarative project seed, not executable OWL.
VAK 8.30 next determines equanimity's nature and
the contemplative forms of the immeasurables.
