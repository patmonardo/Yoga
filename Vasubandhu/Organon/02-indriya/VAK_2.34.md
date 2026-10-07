# VAK_2.34

## 1. Sanskrit (Devanāgarī)

> चित्तं मनोऽथ विज्ञानमेकार्थं चित्तचैतसाः ।
>
> साश्रयालम्बनाकाराः संप्रयुक्ताश्च पञ्चधा ॥ २.३४ ॥

## 2. Sanskrit (IAST)

> cittaṃ mano 'tha vijñānam ekārthaṃ cittacaitasāḥ /
>
> sāśrayālambanākārāḥ saṃprayuktāś ca pañcadhā // 2.34 //

## 3. Lexical Analysis

```text
cittaṃ              → cittam
mano 'tha           → manaḥ atha
vijñānam            → vijñānam
ekārthaṃ            → eka-artham
cittacaitasāḥ       → citta-caitasāḥ
sāśrayālambanākārāḥ → sa-āśraya-ālambana-ākārāḥ
saṃprayuktāś ca     → saṃprayuktāḥ ca
pañcadhā            → pañcadhā
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| cittam | nominative neuter singular | consciousness |
| manaḥ | nominative neuter singular | Mind |
| vijñānam | nominative neuter singular | Cognition |
| eka-artham | nominative neuter singular compound | having one meaning or referent here |
| citta-caitasāḥ | nominative plural compound | consciousness and its associated mental factors |
| sa-āśraya | possessive compound member | having a support |
| ālambana | compound member | object-support |
| ākāra | compound member | manner or aspect |
| saṃprayuktāḥ | nominative plural past passive participle | associated |
| pañcadhā | adverb | in five ways |

The Bhāṣya explains *ekārtha* contextually and gives the five equalities as
support, object-support, manner, time, and numerical instance.

## 4. Scientific English Rendering

> Consciousness, Mind, and Cognition have one referent here. Consciousness
> and its associated mental factors have support, object-support, and
> manner, and are associated in five ways.

## 5. Interpretation

The verse identifies one referent while preserving distinct terms and
functions. The Bhāṣya explains their contextual unity and specifies the
relation between consciousness and its associated factors through five
equalities: support, object-support, manner, time, and numerical instance.
The one-event structure does not make consciousness and each factor the
same factor.

For the Kośa's governing synthesis, Vijñāna is Discriminative Cognition
joining and governing Perception and Conception. Their unity is
Inconceivable as a homogeneous operation; its Idea is disclosed in the
Cognition Base. Vijñāna governs Mind and guides the reading of Dharma Base.
Form Base and Dharma Base both include the same *avijñapti* in distinct
classifications, and Vijñāna bears a *prati* relation to *avijñapti*. Here
the Bhāṣya's statement that *citta*, *manas*, and *vijñāna* have one
referent is local to this explanation; it does not erase the distinct
project functions of consciousness, Mind, and Cognition.

The project-level Samyama synthesis treats ten Samyama-bhūmis as describing
Path-related operation of mental factors, with Buddha Dharma as the
eleventh Bhūmi. This verse states the conditions of association; it does
not enumerate or assign those levels.

## 6. Logical Determination

The Bhāṣya distinguishes contextual co-reference from functional
explanation:

```text
One referent:
    citta, manas, vijñāna

Explanatory functions:
    citta     → gathering or variegation
    manas     → support
    vijñāna   → supported cognition
```

The fivefold association:

```text
Associated(citta, caittas)
    requires equality of:
        support
        object-support
        manner
        time
        numerical instance
```

The closing explanation specifies numerical equality as one consciousness
and one instance of each associated factor. This does not mean there is only
one mental factor or that the different factors become one entity.

## 7. Interpretive Note

The Bhāṣya offers two explanations of the three terms. The first derives
them respectively from gathering, considering, and cognizing. “Others”
say consciousness is so called because it is variegated by wholesome and
unwholesome Principles; that same occurrence is Mind insofar as it
supports, and Cognition insofar as it is supported. Both are contextual
accounts, not grounds for unrestricted interchange of the terms.

The five equalities specify shared conditions of association, not
successive stages. *Dravya* is clarified by the Bhāṣya's one-instance-each
explanation; it should not be turned into a claim about material
substance. The object-support is not the faculty-support, and the manner
is a distinct predicate concerning how the object-support is taken.

## 8. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_34
    a vak:Karika ;
    rdfs:label "VAK 2.34" ;
    vak:hasTopic vak:FivefoldMentalFactorAssociation ;
    vak:belongsTo vak:Indriyanirdesa .

vak:FivefoldAssociation
    vak:hasEquality vak:SupportEquality,
        vak:ObjectSupportEquality,
        vak:MannerEquality,
        vak:TimeEquality,
        vak:NumericalInstanceEquality .

vak:NumericalInstanceEquality
    vak:means "one consciousness and one instance of each associated factor" .
```
