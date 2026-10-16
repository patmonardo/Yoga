# VAK_6.05

## 1. Sanskrit (Devanāgarī)

```sanskrit
वृत्तस्थः श्रुतचिन्तावान् भावनायां प्रयुज्यते ।
नामोभयार्थविषयाः श्रुतमय्यादिका धियः ॥ ६.५ ॥
```

## 2. Sanskrit (IAST)

```text
vṛttasthaḥ śrutacintāvān bhāvanāyāṃ prayujyate |
nāmobhayārthaviṣayāḥ śrutamayyādikā dhiyaḥ || 6.5 ||
```

VAK 6.05 begins the practitioner's preparation for seeing the truths. One who
is established in conduct and possesses learning and reflection applies
oneself to cultivation. The three cognitions formed from learning, reflection,
and cultivation are then distinguished by their cognitive fields: name, both name and
Meaning, and Meaning.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `vṛtta-sthaḥ` | nominative singular masculine compound | established in disciplined conduct |
| `śruta-cintā-vān` | nominative singular masculine possessive compound | possessing learning and reflection |
| `bhāvanāyām` | locative singular feminine | in cultivation |
| `prayujyate` | third-person singular present middle/passive of `pra-√yuj` | applies or engages oneself |
| `nāma-ubhaya-artha-viṣayāḥ` | nominative plural feminine distributive compound | ranging over name, both name and Meaning, and Meaning respectively |
| `śruta-mayī-ādikāḥ` | nominative plural feminine | beginning with that formed from learning |
| `dhiyaḥ` | nominative plural feminine of `dhī` | cognitions or understandings |

```text
vṛtta-sthaḥ | śruta-cintā-vān | bhāvanāyām | prayujyate |
nāma-ubhaya-artha-viṣayāḥ | śruta-mayī-ādikāḥ | dhiyaḥ
```

`Ubhaya` abbreviates `nāma-artha`, name and Meaning together. The compact
compound distributes three cognitive fields across the three cognitions in sequence:

```text
nāma
ubhaya = nāma + artha
artha
```

The Bhāṣya consistently names these cognitions as three forms of `prajñā` and
then supplements the field-based distribution with a causal account of how
each is generated.

## 4. Grammar

The first half gives the practitioner's qualification and action:

```text
vṛttasthaḥ
    established in conduct

śrutacintāvān
    possessing learning and reflection

bhāvanāyāṃ prayujyate
    applies oneself to cultivation
```

The Bhāṣya expands the sequence genetically: one who wishes to see the truths
first guards ethical conduct, receives teaching conformable to seeing, hears
the Meaning, reflects without inversion, and then engages in cultivation.

The second half has the plural subject `dhiyaḥ`, qualified by
`śrutamayyādikāḥ`. The compound `nāmobhayārthaviṣayāḥ` supplies three
successive field-relations:

```text
śrutamayī dhī
    nāma-viṣayā

cintāmayī dhī
    nāma-artha-viṣayā

bhāvanāmayī dhī
    artha-viṣayā
```

The Bhāṣya renders these as cognitive Conditions (`ālambana`). It then reports an
objection: alternating between name and Meaning does not securely establish
the intrinsic distinction of reflective Prajñā. Vasubandhu therefore offers a
causal definition based on authoritative teaching, reasoning, and samādhi.

**Feature Grammar direction.** The singular practitioner of the first half
governs `prayujyate`; the feminine plural `dhiyaḥ` governs the second half.
The three members of `nāma-ubhaya-artha-viṣayāḥ` distribute in order over the
three Prajñās:

```text
PRACTITIONER[NUM=sg, HAS=śruta+cintā] → ENGAGES[bhāvanā]
DHĪ[NUM=pl, SERIES=śrutamayī+cintāmayī+bhāvanāmayī]
    → VIṢAYA-SERIES[nāma+(nāma+artha)+artha]
```

This specifies agreement and ordered distribution for a later NLTK Feature
Grammar. The Bhāṣya's causal alternative is a separate semantic relation,
not another parse of the compound.

## 5. Translation

### Literal Translation

> Established in conduct and possessing learning and reflection, one applies
> oneself to cultivation. The cognitions beginning with that formed from
> learning range respectively over name, both [name and Meaning], and Meaning.

### Bhāṣya-informed study translation

> Established in disciplined conduct, having received teaching and reflected
> without inversion, one applies oneself to cultivation. The three forms of
> Prajñā, formed from learning, reflection, and cultivation, range in order
> over name, name together with Meaning, and Meaning without dependence on
> words.

## 6. Philosophical Translation

> The Path does not leap directly from verbal teaching into realization.
> Disciplined conduct sustains reception; reception generates a determination
> that reflection must test; reflection mediates expression and Meaning; and
> samādhi generates a cultivated Prajñā capable of proceeding toward Meaning
> without dependence upon words. Directness is therefore not the absence of
> mediation but the fruit of a completed genetic movement.

Two structures must be held together:

```text
cognitive-field structure
    name → name-and-Meaning → Meaning

genetic structure
    reliable teaching → reasoning → samādhi
```

The Bhāṣya preserves the middle term by insisting that cognition is determined
not only by what it takes as cognitive field but also by the ground from which it arises.

## 7. Technical Vocabulary

**`Vṛtta` — conduct**

Disciplined ethical comportment, glossed in the Bhāṣya through guarding
`śīla`. It is the first practical condition for one who wishes to see the
truths, not an ornamental moral preface detached from cognition.

**`Śruta` — learning or received teaching**

Teaching received in a form conformable (`anuloma`) to seeing the truths. The
Bhāṣya also speaks of hearing the Meaning. `Śruta` supplies the authoritative
starting determination upon which later Prajñā relies.

**`Cintā` — reflection**

Reasoned examination that must be non-inverted before cultivation begins. In
the field model, it mediates name and Meaning in both directions. In the
causal model, it is Prajñā born from `yukti-nidhyāna`, sustained examination
through reasoning.

**`Bhāvanā` — cultivation**

The stage into which the qualified practitioner enters. The Bhāṣya's strongest
definition is not mere repetition and not Meaning as cognitive field alone:
`bhāvanāmayī prajñā` is born from samādhi.

**`Śrutamayī prajñā` — Prajñā formed from learning**

According to the kārikā model, its cognitive Condition is name. Vasubandhu's causal
definition identifies it as certainty (`niścaya`) born from the authority or
validity of reliable teaching (`āptavacana-prāmāṇya`).

**`Cintāmayī prajñā` — Prajñā formed from reflection**

According to the field model, it moves from expression to Meaning and from
Meaning back to expression. Other teachers object that this alternating
field-relation fails to define it securely. Vasubandhu's causal account
distinguishes it as born from reasoning and examination.

**`Bhāvanāmayī prajñā` — Prajñā formed from cultivation**

It proceeds toward Meaning independently of verbal formulation
(`vyañjana-nirapekṣā arthe pravartate`). Its decisive genetic determination is
`samādhija`, born from samādhi.

**`Nāma` — name**

The verbal designation or linguistic support that first presents the teaching.
It is not discarded as false; its support-function becomes progressively less
necessary as Prajñā is transformed.

**`Artha` — Meaning**

What the teaching is about and what cultivational Prajñā takes independently
of verbal formulation. Capitalized **Meaning** marks our controlled project
usage; it does not add a separate Sanskrit technical term beyond `artha`.

**`Viṣaya / ālambana` — cognitive field / cognitive Condition**

The kārikā says `viṣaya`; the Bhāṣya explains through `ālambana`. This
range of cognitive Conditions is genuine but insufficient by itself to define
all three forms of Prajñā without ambiguity. It is distinct from Object, the
comprehended truth of a Thing.

**`Niśritya` — relying upon**

The Bhāṣya's genetic connective:

```text
śrutamayī prajñā
    relied upon by cintāmayī prajñā

cintāmayī prajñā
    relied upon by bhāvanāmayī prajñā
```

Later Prajñā does not arise independently of the earlier form, even when it no
longer depends upon the same verbal support.

**`Āptavacana-prāmāṇya` — authority of reliable teaching**

The source from which the certainty of learning-born Prajñā arises. This is a
Bhāṣya determination, not wording present in the kārikā.

**`Yukti-nidhyāna` — reasoned examination**

The generating ground of reflective Prajñā. It prevents the middle form from
being reduced to an unstable alternation between two field types.

**`Samādhija` — born from samādhi**

The generating ground of cultivational Prajñā. This is the verse-unit's
strongest determination of how Prajñā proceeds toward Meaning without
verbal dependence.

**`Vyañjana-nirapekṣa` — independent of verbal formulation**

Cultivational Prajñā operates toward Meaning without relying on words. This is
achieved independence from linguistic support, not a rejection of the
learning and reflection through which it was generated.

## 8. Logical Determination

The Path preparation is:

```text
EstablishedIn(person, DisciplinedConduct)
AND Possesses(person, Learning)
AND Possesses(person, NonInvertedReflection)
    → EngagesIn(person, Cultivation)
```

The kārikā's cognitive-field model is:

```text
SrutamayiPrajna
    hasCognitiveField Name

CintamayiPrajna
    hasCognitiveField NameAndMeaning

BhavanamayiPrajna
    hasCognitiveField Meaning
    AND independentOf VerbalFormulation
```

The genetic dependence is:

```text
SrutamayiPrajna
    → basisFor CintamayiPrajna

CintamayiPrajna
    → basisFor BhavanamayiPrajna
```

The objection exposes underdetermination by field alone:

```text
HasCognitiveField(cognition, Name)
    → candidate SrutamayiPrajna

HasCognitiveField(cognition, Meaning)
    → candidate BhavanamayiPrajna

AlternatesBetween(Name, Meaning)
    ↛ SufficientDefinitionOf(CintamayiPrajna)
```

The stronger causal model is:

```text
BornFromCertaintyOfReliableTeaching(x)
    → SrutamayiPrajna(x)

BornFromReasonedExamination(x)
    → CintamayiPrajna(x)

BornFromSamadhi(x)
    → BhavanamayiPrajna(x)
```

Thus:

```text
CognitionIdentity
    requires
CognitiveFieldStructure + GeneticGround
```

## 9. Interpretive Note

**Conduct belongs to the genesis of seeing.** The Bhāṣya answers “How are the
truths seen?” by beginning with guarding conduct. Ethical formation is internal
to the preparation of adequate cognition.

**The three Prajñās form a dependent movement.** `Niśritya` prevents their
treatment as three independent learning styles. Each later form arises relying
upon the earlier determination.

**The swimmer analogy expresses achieved independence.** Learning-born Prajñā
holds linguistic support like an untrained swimmer; reflection sometimes
releases and regains it; cultivation crosses without needing that support. The
analogy concerns support, not the erasure of the preceding formation.

**The Bhāṣya criticizes the elegant surface triad.** Name, both, and Meaning
give a useful field progression, but the middle cognition threatens to
collapse. The causal definition restores it through its distinctive genesis in
reasoning.

**Bhāvanā requires samādhi.** Meaning as direct cognitive field does not by itself
constitute cultivation-born Prajñā. Its determining ground is samādhi. This is
the textual basis for speaking of a required cultivation-ground without yet
importing the later Organon term `saṃyama-bhūmi` into Vasubandhu's wording.

**Organon interpretation.** VAK 6.05 gives the first explicit architecture of
Meaning's passage from verbal presentation into Path-capacity. The following
is project synthesis:

```text
nāma
    Meaning presented in linguistic support

nāma + artha
    Meaning reflectively mediated and tested

artha
    Meaning directly cultivated without verbal dependence

samādhi
    the generating ground of bhāvanāmayī Prajñā
```

This sharpens the Ideal Copula. Meaning does not merely sit statically between
Truth and Knowledge. It moves through distinct supports and modes of genesis
until Prajñā becomes capable of bearing Meaning directly. Our prospective
`saṃyama-bhūmi` names a larger Yoga–Organon synthesis; the Kośa's exact term
here is `samādhi`, and that source boundary must remain visible.

## 10. OWL++ Seed

```text
Class: Practitioner
Class: DisciplinedConduct
Class: Prajna
Class: SrutamayiPrajna
    SubClassOf: Prajna
Class: CintamayiPrajna
    SubClassOf: Prajna
Class: BhavanamayiPrajna
    SubClassOf: Prajna
Class: CognitiveField
Class: Name
    SubClassOf: CognitiveField
Class: Meaning
    SubClassOf: CognitiveField
Class: NameMeaningComplex
    SubClassOf: CognitiveField
Class: GeneticGround
Class: ReliableTeaching
    SubClassOf: GeneticGround
Class: ReasonedExamination
    SubClassOf: GeneticGround
Class: Samadhi
    SubClassOf: GeneticGround

ObjectProperty: establishedIn
    Domain: Practitioner
    Range: DisciplinedConduct

ObjectProperty: hasCognitiveField
    Domain: Prajna
    Range: CognitiveField

ObjectProperty: bornFrom
    Domain: Prajna
    Range: GeneticGround

ObjectProperty: reliesUpon
    Domain: Prajna
    Range: Prajna

ObjectProperty: preparesFor
    Domain: Prajna
    Range: PathOperation

Axiom: SrutamayiPrajna SubClassOf hasCognitiveField some Name
Axiom: CintamayiPrajna SubClassOf hasCognitiveField some NameMeaningComplex
Axiom: BhavanamayiPrajna SubClassOf hasCognitiveField some Meaning

Axiom: SrutamayiPrajna SubClassOf bornFrom some ReliableTeaching
Axiom: CintamayiPrajna SubClassOf bornFrom some ReasonedExamination
Axiom: BhavanamayiPrajna SubClassOf bornFrom some Samadhi

Assertion: CintamayiPrajna reliesUpon SrutamayiPrajna
Assertion: BhavanamayiPrajna reliesUpon CintamayiPrajna
Assertion: BhavanamayiPrajna independentOf VerbalFormulation

Constraint: ClassificationByFieldAlone
    insufficientFor DistinguishingAllThreePrajna

View: ThreePrajnaPathGenesis
    Preserves: PractitionerQualification, PrajnaIdentity,
               CognitiveField, GeneticGround, DependenceRelation,
               VerbalSupportStatus, SourceAttribution,
               SourceProvenance
```

The seed keeps cognitive field and genetic ground as distinct dimensions. It
represents the essential Bhāṣya result: cultivational Prajñā is not merely
about Meaning but is generated from samādhi.
