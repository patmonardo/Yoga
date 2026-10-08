# VAK_2.43 — The Attainment of Cessation

## 1. Sanskrit (Devanāgarī)

> निरोधाख्या तथैवेयं विहारार्थं भवाग्रजा ।
>
> शुभा द्विवेद्यानियता चार्यस्याप्या प्रयोगतः ॥ २.४३ ॥

## 2. Sanskrit (IAST)

> nirodhākhyā tathaiveyaṃ vihārārthaṃ bhavāgrajā /
>
> śubhā dvivedyāniyatā cāryasyāpyā prayogataḥ // 2.43 //

## 3. Lexical Analysis

```text
nirodhākhyā    → nirodha-ākhyā
tathaiveyam    → tathā eva iyam
vihārārtham    → vihāra-artham
bhavāgrajā     → bhava-agra-jā
dvivedyāniyatā → dvi-vedyā aniyatā
cāryasyāpyā    → ca āryasya āpyā
prayogataḥ     → prayogataḥ
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| nirodha-ākhyā | nominative feminine singular compound | called attainment of cessation |
| tathā eva | adverbial phrase | likewise, with restricted force |
| iyam | nominative feminine singular pronoun | this attainment |
| vihāra-artham | accusative used adverbially | for the sake of abiding |
| bhava-agra-jā | nominative feminine singular compound | belonging to the summit of existence |
| śubhā | nominative feminine singular | wholesome |
| dvi-vedyā | nominative feminine singular | maturing at either of two times |
| aniyatā | nominative feminine singular | maturation can remain unfixed |
| āryasya | genitive singular | of a noble person |
| āpyā | gerundive | acquired or attainable |
| prayogataḥ | adverbial ablative | through deliberate preparation |

## 4. Scientific English Rendering

> This attainment, called cessation, is likewise [a cessation of
> consciousness and associated mental factors]. It is for the sake of
> abiding, belongs to the summit of existence, is wholesome, matures at
> either of two times or remains unfixed, belongs to a noble person, and is
> acquired through deliberate preparation.

The Bhāṣya limits “likewise” to cessation of consciousness and associated
mental factors. It differentiates the attainment of cessation from the
Non-Reflecting attainment by its aim, support, practitioner, maturation,
and manner of acquisition.

## 5. Interpretation

The attainment of cessation must not be translated as unconsciousness. The
Bhāṣya begins with a shared operational description, but it does not use
that description as the whole truth of either attainment:

```text
Shared:
    cessation of consciousness and associated mental factors

Non-Reflecting attainment:
    entered under a conception of escape;
    fourth dhyāna;
    ordinary practitioner;
    fixed next-rebirth maturation

Attainment of cessation:
    entered under a conception of peaceful abiding;
    summit of existence;
    noble practitioner;
    next-life, later-life, or unfixed maturation
```

The source thereby shows that the instrument's presently manifest operation
is not the whole story. A formal similarity at the level of suspended
citta-caitta operation does not establish identity of aim, path-basis,
causal determination, or result. The attainment of cessation is a
conditioned Path determination, not a blank episode and not the abolition
of Vijñāna as the governing relation.

The Kośa-wide synthesis remains: Vijñāna is Discriminative Cognition joining
and governing Perception and Conception. Their unity is Inconceivable as
homogeneous operation, with its Idea disclosed in the Cognition Base.
Vijñāna governs Mind and guides Dharma Base. The Hub is not an empirical
factor which disappears with a factor-profile; it is the governing
relation by which the profile, its cessation, and its transformed Path
possibility are intelligible.

## 6. Logical Determination

```text
CessationAttainment(S)
    has:
        aim = PeacefulAbiding
        support = SummitOfExistence
        ethicalKind = Wholesome
        practitioner = Noble
        acquisition = DeliberatePreparation
        maturation = NextLife | LaterLife | Unfixed
```

```text
SharedCittaCaittaCessation
    does not entail
Identity(NonReflectingAttainment, CessationAttainment)
```

The Bhāṣya states:

```text
OrdinaryPerson(S)
    → cannot produce CessationAttainment(S)

NoblePathPower(S)
    and ResolveTowardNirvanaInThisLife(S)
    → allows its production through preparation
```

For the Buddha, acquisition is simultaneous with awakening and the knowledge
of exhaustion, not acquired through ordinary preparatory practice.

## 7. Interpretive Note

The Bhāṣya preserves a dispute over whether the Bodhisattva previously
produced the attainment while still a trainee. Teachers of the outer regions
affirm this; Kāśmīra teachers deny it, arguing that the thirty-four
consciousness-moments of awakening permit no intervening dissimilar
consciousness in which the attainment could arise. The uncertain line about
the Bodhisattva's resolve remains a textual limit and is not silently
harmonized.

The verse says the attainment is “unfixed” with respect to maturation
because it need not mature if final nirvāṇa occurs in the present life. Its
maturation at the summit of existence is said to comprise four Bases.

## 8. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_43
    a vak:Karika ;
    rdfs:label "VAK 2.43" ;
    vak:hasTopic vak:CessationAttainment ;
    vak:belongsTo vak:Indriyanirdesa .

vak:CessationAttainment
    vak:hasAim vak:PeacefulAbiding ;
    vak:hasSupport vak:SummitOfExistence ;
    vak:hasEthicalKind vak:Wholesome ;
    vak:isAttainableBy vak:NoblePractitioner ;
    vak:isAcquiredThrough vak:DeliberatePreparation ;
    vak:preventsArisingOf vak:ConsciousnessAndAssociatedFactors .
```
