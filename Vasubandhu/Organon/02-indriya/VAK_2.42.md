# VAK_2.42 — The Non-Reflecting Attainment

## 1. Sanskrit (Devanāgarī)

> तथासंज्ञिसमापत्तिर्ध्यानेऽन्त्ये निःसृतीच्छया ।
>
> शुभा उपपद्यवेद्यैव नार्यस्यैकाध्विकाप्यते ॥ २.४२ ॥

## 2. Sanskrit (IAST)

> tathāsaṃjñisamāpattir dhyāne 'ntye niḥsṛtīcchayā /
>
> śubhā upapadyavedyaiva nāryasyaikādhvikāpyate // 2.42 //

## 3. Lexical Analysis

```text
tathāsaṃjñisamāpattiḥ → tathā asaṃjñi-samāpattiḥ
dhyāne 'ntye           → dhyāne antye
niḥsṛtīcchayā          → niḥsṛti-icchayā
śubhā                   → śubhā
upapadyavedyaiva        → upapadya-vedyā eva
nāryasya                → na āryasya
ekādhvikāpyate          → eka-adhvikā āpyate
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| tathā | indeclinable | likewise, with a restricted Bhāṣya scope |
| asaṃjñi-samāpattiḥ | nominative feminine singular | Non-Reflecting attainment |
| dhyāne antye | locative phrase | in the final, fourth dhyāna |
| niḥsṛti-icchayā | instrumental compound | through the wish for release |
| śubhā | nominative feminine singular | wholesome |
| upapadya-vedyā | nominative feminine singular | maturing in the immediately following rebirth |
| eva | restrictive particle | only |
| na āryasya | negation with genitive | not belonging to a noble person |
| eka-adhvikā | nominative feminine singular | acquired in one temporal mode |
| āpyate | passive verb | is obtained |

*Asaṃjñi* is the privative of *saṃjñi*. In this project, *saṃjñā* is
read as Reflection; therefore “Non-Reflecting” preserves the term's
determinate negation. It must not be expanded into the modern global label
“unconsciousness.”

## 4. Scientific English Rendering

> Likewise, the Non-Reflecting attainment is in the final dhyāna, through
> the wish for release. It is wholesome, matures only in the immediately
> following rebirth, does not belong to a noble person, and is acquired in
> one temporal mode.

The Bhāṣya restricts “likewise” to one stated feature: the Non-Reflecting
attainment is cessation of consciousness and associated mental factors.
It calls this an attainment either of Non-Reflecting beings or of
Non-Reflection. The name must not weaken the explicit operational
predication, and the predication must not overwrite the lexical force of
the name.

## 5. Interpretation

“Non-Reflecting attainment” works as the controlled rendering because it
preserves the *a-saṃjñi* determination rather than importing a modern
psychological category. It makes clear what the practitioners seek to
suspend: Reflection. It also leaves the Bhāṣya's exact statement visible:
in its account, consciousness and associated mental factors are prevented
from arising during the attainment.

The distinction must be maintained:

```text
Name of the attainment:
    Non-Reflecting

Bhāṣya's operational claim:
    cessation of consciousness and associated mental factors

Maturation-result:
    a five-Base existence among Non-Reflecting Bṛhatphala beings
```

These are not three interchangeable claims. The attainment is wholesome;
its maturation-result is indeterminate. It is entered by ordinary
practitioners who take it as release, but noble persons do not cultivate it,
seeing the result as a place of downfall. “Wholesome” therefore does not
entail that the attainment is liberation.

The Kośa-wide synthesis remains: Vijñāna is Discriminative Cognition joining
and governing Perception and Conception. Their unity is Inconceivable as
homogeneous operation, with its Idea disclosed in the Cognition Base.
Vijñāna governs Mind and guides Dharma Base. This finite conditioned
cessation is not the Hub, not liberation, and not an account of Vijñāna's
abolition.

## 6. Logical Determination

```text
NonReflectingAttainment(S)
    has:
        level = FourthDhyana
        motive = WishForRelease
        ethicalKind = Wholesome
        initialAcquisitionTime = Present
        practitioner = Ordinary
```

```text
NonReflectingAttainment(S)
    → PreventsArising(S, ConsciousnessAndAssociatedFactors)
    → MaturesInNextRebirth(
          NonReflectingBrhatphalaExistence)
```

```text
NoblePractitioner(S)
    → does not cultivate NonReflectingAttainment(S)

PresentAcquisition(A)
    is compatible with
later possession of PastInstance(A)
```

No future instance is cultivated because the attainment is without
consciousness and requires great formative effort.

## 7. Interpretive Note

The Bhāṣya expressly distinguishes the attainment from the preceding
Non-Reflecting maturation-result. “Likewise” carries forward only cessation
of consciousness and associated mental factors. It does not transfer the
result's indeterminate ethical classification to the wholesome attainment.

The source says a practitioner who has produced the attainment and fallen
away will necessarily produce it again and be reborn among the
Non-Reflecting beings; this is marked with reportive *kila*. The claim
requires careful retention, but it is not a general instruction to seek
the attainment.

## 8. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_42
    a vak:Karika ;
    rdfs:label "VAK 2.42" ;
    vak:hasTopic vak:NonReflectingAttainment ;
    vak:belongsTo vak:Indriyanirdesa .

vak:NonReflectingAttainment
    vak:hasLevel vak:FourthDhyana ;
    vak:hasMotive vak:WishForRelease ;
    vak:hasEthicalKind vak:Wholesome ;
    vak:hasMaturationTiming vak:NextRebirthOnly ;
    vak:isNotCultivatedBy vak:NoblePractitioner ;
    vak:preventsArisingOf vak:ConsciousnessAndAssociatedFactors .
```
