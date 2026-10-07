# VAK_2.28

## 1. Sanskrit (Devanāgarī)

> सवितर्कविचारत्वात् कुशले कामचेतसि ।
>
> द्वाविंशतिश्चैतसिकाः कौकृत्यमधिकं क्वचित् ॥ २.२८ ॥

The research source-form gives *dvāṃviṃśatiḥ*; the normalized numeral
*dvāviṃśatiḥ*, “twenty-two,” is adopted here without
altering the research witness.

## 2. Sanskrit (IAST)

> savitarkavicāratvāt kuśale kāmacetasi /
>
> dvāviṃśatiś caitasikāḥ kaukṛtyam adhikaṃ kvacit // 2.28 //

## 3. Lexical Analysis

```text
savitarkavicāratvāt → sa-vitarka-vicāratvāt
kuśale              → kuśale
kāmacetasi          → kāma-cetasi
dvāviṃśatiś         → dvāviṃśatiḥ
caitasikāḥ          → caitasikāḥ
kaukṛtyam           → kaukṛtyam
adhikaṃ             → adhikam
kvacit              → kvacit
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| sa-vitarka-vicāratvāt | ablative singular abstract compound | because accompanied by *vitarka* and *vicāra* |
| kuśale | locative neuter singular | in wholesome consciousness |
| kāma-cetasi | locative neuter singular compound | in Desire-Principle consciousness |
| dvāviṃśatiḥ | nominative feminine singular numeral | twenty-two |
| caitasikāḥ | nominative masculine plural | mental factors |
| kaukṛtyam | nominative neuter singular | remorse |
| adhikam | nominative neuter singular | additional |
| kvacit | indeclinable | in some cases |

The ablative *-tvāt* states the reason for the base count. *Kvacit*
restricts the addition of remorse: it does not make remorse a necessary
member of the wholesome great-ground class.

## 4. Grammar

The first clause sets the conditions for the base count:

```text
kuśale kāma-cetasi
    → in wholesome Desire-Principle consciousness

sa-vitarka-vicāratvāt
    → because accompanied by vitarka and vicāra

dvāviṃśatiḥ caitasikāḥ
    → twenty-two mental factors
```

The Bhāṣya expands the number:

```text
10 universal great-ground factors
+ 10 wholesome great-ground factors
+ vitarka
+ vicāra
= 22
```

The final clause adds remorse only in some cases. When present with the
wholesome base, it makes twenty-three factors.

## 5. Scientific English Rendering

### Kārikā

> Because wholesome Desire-Principle consciousness is accompanied by
> *vitarka* and *vicāra*, there are twenty-two mental factors; remorse
> is additional in some cases.

### Bhāṣya-informed rendering

> A wholesome Desire-Principle consciousness-event necessarily contains
> ten universal great-ground factors, ten wholesome great-ground factors,
> *vitarka*, and *vicāra*, making twenty-two. Where wholesome remorse is
> also present, it is an additional twenty-third factor.

The Bhāṣya defines wholesome remorse as regret concerning having done
what is unwholesome or having failed to do what is wholesome. Painful
affect or self-criticism alone does not establish that classification.

## 6. Interpretation

The verse moves from class definitions to the count in one specified
consciousness. The universal and wholesome grounds supply twenty factors;
the Desire-Principle setting contributes *vitarka* and *vicāra*. Remorse
is conditional, not part of the required base, and its ethical
classification depends on what is done or omitted and the direction of
the regret.

The Bhāṣya distinguishes the remorse-factor from the act or omission
that occasions it. Its naming discussion offers object-support and
cause-to-effect designation as distinct explanations. The deed or
omission is not itself the mental factor.

In the inner-instrument Techne, the Bhāṣya's identification of *mati*
with *prajñā* from VAK 2.24 bears the project rendering Science of
Principles; that universal factor is already included in the count and
is not added again here.

The Kośa's governing synthesis: Vijñāna is Discriminative Cognition joining
and governing Perception and Conception. Their unity is Inconceivable as a
homogeneous operation; its Idea is disclosed in the Cognition Base. Vijñāna
governs Mind and guides the reading of Dharma Base. Form Base and Dharma
Base both include the same *avijñapti* in distinct classifications, and
Vijñāna bears a *prati* relation to *avijñapti*. This synthesis remains
distinct from the present count of associated mental factors.

## 7. Logical Determination

```text
WholesomeDesireBase =
      UniversalGreatGroundTen
    ∪ WholesomeGreatGroundTen
    ∪ {Vitarka, Vicāra}

Count(WholesomeDesireBase) = 22
```

The conditional extension is:

```text
Factors(e) = WholesomeDesireBase
    when ¬HasRemorse(e)

Factors(e) = WholesomeDesireBase ∪ {Remorse}
    when HasRemorse(e)

Count = 22 or 23 respectively
```

Ethical direction of remorse:

```text
WholesomeRemorse
    = regret for doing the unwholesome
      or omitting the wholesome

UnwholesomeRemorse
    = regret for doing the wholesome
      or omitting the unwholesome
```

The act or omission serving as the basis is not identical with the
remorse-factor.

## 8. Interpretive Note

The Desire-Principle count is tied to the *vitarka* and *vicāra*
accompaniment stated in the verse. The conditional *kaukṛtya* extends
the count only where it occurs. The Bhāṣya further establishes that
regret may be wholesome or unwholesome and may concern an act or an
omission; neither the deed's ethical status alone nor the mere presence
of regret settles the factor's classification.

## 9. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_28
    a vak:Karika ;
    rdfs:label "VAK 2.28" ;
    vak:hasTopic vak:WholesomeDesireCittaFactorCount ;
    vak:belongsTo vak:Indriyanirdesa .

vak:WholesomeDesireCittaFactorCount
    vak:requires vak:UniversalGreatGroundTen,
        vak:WholesomeGreatGroundTen,
        vak:Vitarka,
        vak:Vicara ;
    vak:hasBaseCount 22 ;
    vak:hasConditionalFactor vak:Remorse ;
    vak:hasExtendedCount 23 .

vak:Remorse
    vak:hasCognitiveBasis vak:ActionOrOmission ;
    vak:hasEthicalDirection vak:Wholesome,
        vak:Unwholesome .
```
