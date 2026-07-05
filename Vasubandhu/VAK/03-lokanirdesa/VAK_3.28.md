# VAK_3b — VAkK_3.28

## Sanskrit — Devanāgarī

हेतुरत्र समुत्पादः समुत्पन्नः फलं मतम् ।
विद्याविपक्षो धर्मोऽन्योऽविद्यामित्रानृतादिवत् ॥ VAkK_3.28 ॥

## Sanskrit — IAST

hetur atra samutpādaḥ samutpannaḥ phalaṃ matam /
vidyāvipakṣo dharmo 'nyo 'vidyāmitrānṛtādivat // VAkK_3.28 //

## Source Resolution

The source sandhi is compact:

```text
vidyāvipakṣo dharmo 'nyo 'vidyāmitrānṛtādivat
```

Resolved cautiously:

```text
vidyā-vipakṣaḥ dharmaḥ anyaḥ avidyā-mitra-anṛta-ādi-vat
```

## Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| hetuḥ | hetuḥ | ground / cause |
| atra | atra | here |
| samutpādaḥ | samutpādaḥ | co-arising / arising-together |
| samutpannaḥ | samutpannaḥ | arisen; co-arisen |
| phalam | phalam | fruit / result |
| matam | matam | is regarded / is held |
| vidyāvipakṣaḥ | vidyā-vipakṣaḥ | opposite of knowledge |
| dharmaḥ | dharmaḥ | determination / law / dharma |
| anyaḥ | anyaḥ | other; another |
| avidyā | avidyā | ignorance / non-knowledge |
| mitra | mitra | friend |
| anṛta | anṛta | untruth / falsehood |
| ādivat | ādi-vat | as in examples such as |

## Grammar

```text
hetuḥ atra samutpādaḥ
    = here, samutpāda is the cause / ground

samutpannaḥ phalam matam
    = the arisen is held to be the fruit

vidyā-vipakṣaḥ dharmaḥ anyaḥ
    = another dharma opposed to vidyā

avidyā-mitra-anṛta-ādi-vat
    = as with words such as avidyā, amitra, anṛta, etc.
```

## Literal Translation

Here, co-arising is the cause; the arisen is regarded as the fruit. Ignorance is another dharma opposed to knowledge, as in words such as non-knowledge, non-friend, and untruth.

## Philosophical Translation

In this context, dependent co-arising names the causal side, while the dependently arisen names the resultant side. Avidyā is not merely the absence of knowledge; it is a distinct dharma opposed to vidyā, just as terms like non-friend or untruth indicate a positive contrary rather than simple non-being.

## Technical Vocabulary

| Sanskrit | Working translation | Note |
|---|---|---|
| hetu | ground / cause | Here identified with samutpāda |
| samutpāda | co-arising | Cause-side of dependent co-arising |
| samutpanna | arisen / co-arisen | Result-side of the process |
| phala | fruit / result | The dependently arisen result |
| vidyā | knowledge | Positive knowing / knowledge |
| vipakṣa | opposition / contrary | A positive opposition, not mere privation |
| dharma | determination / law | A real determinate factor in the analysis |
| avidyā | ignorance / non-knowledge | Opposed dharma, not simple absence |
| amitra | non-friend / enemy | Example of privative form indicating contrary |
| anṛta | untruth | Example of negative form as determinate contrary |

## Doctrinal Determination

VAkK_3.28 has two linked tasks.

First, it distinguishes cause and result:

```text
samutpāda
    = hetu / cause-side

samutpanna
    = phala / result-side
```

Second, it begins the analysis of avidyā:

```text
avidyā
    is not mere absence of vidyā

avidyā
    is another dharma opposed to vidyā
```

This matters because avidyā is the first limb of the twelvefold sequence. It must be a real operative condition, not a simple nothing.

## Logical Determination

The first half gives the cause-result distinction:

```text
cause
    = dependent co-arising as productive structure

fruit
    = the dependently arisen result
```

The second half gives a theory of negation:

```text
negative prefix
    does not always mean sheer absence

negative term
    may name a positive contrary
```

Thus:

```text
avidyā
    ≠ mere lack of knowledge

avidyā
    = determinate opposition to knowledge
```

This is very Hegel-clean:

```text
abstract negation
    would be simple absence

determinate negation
    is an opposed determination
```

Avidyā is a determinate negation.

## Interpretive Note

This verse prevents a weak reading of ignorance. Avidyā is not a blank. It is an operative opposed dharma.

That is why it can function as a limb of dependent co-arising. If ignorance were mere absence, it could not be the effective beginning of the wheel. As an opposed determination, it can condition saṃskāra and the whole subsequent series.

The first half of the verse also refines the terminology: `samutpāda` names the causal structure; `samutpanna` names the resultant product.

## Organon Interpretation

Speculatively, this gives the logical rule for the wheel as a self-reproducing system.

```text
samutpāda
    = productive causal structure

samutpanna
    = produced concrete existence

avidyā
    = determinate opposition to knowledge
```

In Organon terms:

```text
The wheel reproduces itself
    because the originating fault is not absence,
    but a determinate contrary that can operate.
```

So avidyā is not zero. It is a negative determination with causal power.

```text
not knowing
    as mere lack
        would be inert

avidyā
    as opposed dharma
        becomes productive condition
```

This remains subordinate to the Sanskrit and Bhāṣya, but it is a strong logical marker.

## OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_28
    a vak:Karika ;
    rdfs:label "VAkK 3.28" ;
    vak:continues vak:VAK_3_27 ;
    vak:hasTopic vak:DependentCoArising ;
    vak:distinguishes vak:Samutpada ;
    vak:distinguishes vak:Samutpanna ;
    vak:analyzes vak:Avidya .

vak:Samutpada
    a logic:CausalStructure ;
    rdfs:label "samutpāda" ;
    vak:hasCanonicalTranslation "co-arising" ;
    logic:hasRole vak:CauseRole .

vak:Samutpanna
    a logic:ResultStructure ;
    rdfs:label "samutpanna" ;
    vak:hasCanonicalTranslation "co-arisen" ;
    logic:hasRole vak:FruitRole .

vak:Avidya
    a vak:Dharma ;
    rdfs:label "avidyā" ;
    vak:hasCanonicalTranslation "ignorance" ;
    logic:opposes vak:Vidya ;
    rdfs:comment "Avidyā is a dharma opposed to vidyā, not a mere absence of knowledge." .

vak:Vidya
    a vak:Dharma ;
    rdfs:label "vidyā" ;
    vak:hasCanonicalTranslation "knowledge" .
```

## Commit Note

Committed VAK_3b / VAkK_3.28.

Established:
- samutpāda is the cause-side / hetu.
- samutpanna is the result-side / phala.
- avidyā is not mere absence of vidyā.
- avidyā is a distinct dharma opposed to vidyā, like amitra or anṛta.

Logical determination:
VAkK_3.28 moves from the wheel-dynamic to the logic of causality and determinate negation. Dependent co-arising is cause; the dependently arisen is fruit. Avidyā is a determinate contrary to knowledge, not empty non-being.
