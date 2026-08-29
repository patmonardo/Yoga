# VAK_2.50

## 1. Sanskrit (Devanāgarī)

> स्वतोऽन्ये कारणं हेतुः सहभूर्ये मिथःफलाः ।
>
> भूतवच्चित्तचित्तानुवर्तिलक्षणलक्ष्यवत् ॥ २.५० ॥

## 2. Sanskrit (IAST)

> svato 'nye kāraṇaṃ hetuḥ sahabhūr ye mithaḥphalāḥ /
>
> bhūtavac cittacittānuvartilakṣaṇalakṣyavat // 2.50 //

## 3. Padaccheda

```text
svato 'nye                         → svataḥ anye
kāraṇam                           → kāraṇam
hetuḥ                             → hetuḥ
sahabhūr                          → sahabhūḥ
ye                                → ye
mithaḥphalāḥ                      → mithaḥ-phalāḥ
bhūtavat                          → bhūta-vat
cittacittānuvartilakṣaṇalakṣyavat
                                  → citta-citta-anuvarti-lakṣaṇa-lakṣya-vat
```

| Form | Morphology | Lexical force here |
|---|---|---|
| svataḥ | ablative singular of reflexive pronoun used adverbially | apart from itself / other than itself |
| anye | nominative masculine plural | the others |
| kāraṇam | nominative neuter singular predicate-name | conditioning [cause] |
| hetuḥ | nominative masculine singular | cause / causal ground |
| sahabhūḥ | nominative masculine singular predicate | co-arisen cause |
| ye | nominative masculine plural relative pronoun | those which |
| mithaḥ-phalāḥ | nominative masculine plural compound | mutually one another's results |
| bhūta-vat | indeclinable comparative expression | as with the great elements |
| citta-citta-anuvarti-vat | comparative compound understood within the series | as with citta and the followers of citta |
| lakṣaṇa-lakṣya-vat | comparative compound | as with mark and what is marked |

The final line compresses three examples under repeated `-vat`: the great
elements; citta with its followers; and conditioned marks with what they
mark. `Bhūta` here means the four great elements, not beings in general.

## 4. Grammar

The first definition resumes `kāraṇa-hetu` from the preceding verse:

```text
svataḥ anye [dharmāḥ]
    → kāraṇam hetuḥ

the dharmas other than the dharma itself
    → are its conditioning causes
```

The number shift between plural `anye` and singular `hetuḥ` is classificatory:
many other dharmas fall under the one causal type called `kāraṇa-hetu`.

The second definition is a relative construction:

```text
ye mithaḥ-phalāḥ
    → [te] sahabhūḥ [hetavaḥ]

those which are mutually one another's results
    → [are] co-arisen causes
```

The second half supplies three analogical instances:

```text
bhūta-vat
    → like the four great elements

citta-citta-anuvarti-vat
    → like citta and the dharmas following citta

lakṣaṇa-lakṣya-vat
    → like conditioned marks and the marked dharma
```

The kārikā asserts these examples compactly. The Bhāṣya supplies both their
technical scope and the objections to taking simultaneity as proof of mutual
causal efficacy.

## 5. Translation

### Close syntactic construe

> The others, apart from itself, are its conditioning cause. Those which are mutually one another's results are co-arisen causes, as with the great elements, citta and the followers of citta, and the marks and what is marked.

### Bhāṣya-informed translation

> Every dharma other than the arising dharma itself falls under conditioning cause. Co-arisen causes are selected members of one simultaneous complex that are held to be mutually causal and mutually resultant: the four great elements, citta and its followers, and conditioned marks with the dharma they mark. Vasubandhu nevertheless asks whether their co-presence demonstrates reciprocal efficacy or merely a common production by antecedent conditions.

## 6. Philosophical Translation

> Causal enclosure cannot be inferred from simultaneity alone. A complex may contain members that genuinely sustain one another, or members jointly produced by an earlier causal configuration. Co-presence gives the phenomenon to be explained; genetic discrimination determines the form of its unity.

The fundamental alternatives are:

```text
simultaneous complex
    ├── reciprocal immanence
    │       members mutually sustain one another
    └── common genesis
            antecedent conditions produce the members together
```

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| kāraṇa-hetu | conditioning cause | every other dharma under the broad non-obstruction definition developed in 2.49 |
| sahabhū-hetu | co-arisen cause | selected simultaneous dharmas asserted to stand in a causal relation |
| mithaḥ-phala | mutually resultant | each member functions as a result relative to the other |
| mahābhūta | great element | earth, water, fire, and wind as a mutually conditioning complex |
| cittānuvartin | follower of citta | dharma corresponding with citta across specified temporal and causal dimensions |
| caitta | mental factor | associated mental operation included among the followers of citta |
| saṃvara | restraint | here the restraint of absorption and uncontaminated restraint |
| lakṣaṇa | conditioned mark | arising, duration, aging, or impermanence |
| lakṣya | what is marked | conditioned dharma characterized by those marks |
| anulakṣaṇa | secondary mark | mark-of-a-mark that exposes an exception to strict mutual resulthood |
| bhāvābhāva-niyama | regularity of presence and absence | criterion offered for causal dependence |

The Bhāṣya defines followers of citta more broadly than “mental factors.” They
include all associated caittas, the two restraints, and the conditioned marks
of citta and those factors.

Their following is indexed across five headings:

```text
time
result
maturation
homogeneous outflow
ethical quality
```

## 8. Logical Determination

The broad conditioning rule remains:

```text
Dharma(x)
AND Dharma(y)
AND y ≠ x
AND NOT Obstructs(y, Arising(x))
    → KaranaHetu(y, x)
```

The strong Vaibhāṣika co-arising rule is:

```text
MutuallyResultant(x, y)
    → SahabhuHetu(x, y)
    AND SahabhuHetu(y, x)
```

Its principal instances are:

```text
MutualCause(FourGreatElements)
MutualCause(Citta, FollowersOfCitta)
MutualCause(ConditionedMarks, MarkedDharma)
```

The secondary-mark qualification blocks a universal biconditional:

```text
SahabhuHetu(Dharma, SecondaryMarks(Dharma))

NOT SahabhuHetu(SecondaryMarks(Dharma), Dharma)
```

Therefore:

```text
SahabhuHetu(x, y)
    ⇏ always SahabhuHetu(y, x)
```

although mutual resulthood remains the principal definition.

The follower relation is multidimensional:

```text
FollowsCitta(x, c) :=
    SameArisingDurationCessation(x, c)
    AND SameTemporalPeriod(x, c)
    AND SameResult(x, c)
    AND SameMaturation(x, c)
    AND SameHomogeneousOutflow(x, c)
    AND SameEthicalQuality(x, c)
```

Mere simultaneity is insufficient:

```text
Simultaneous(x, y)
    ⇏ MutuallyCausal(x, y)
```

The Bhāṣya's genetic test is:

```text
Observed(CoPresence(x, y))
    → test ReciprocalEfficacy(x, y)
    → test CommonAntecedentCause(z, x, y)
    → test HiddenSupportConditions
```

Thus lamp and light, sprout and shadow, or three standing staffs do not by
themselves decide the causal form.

## 9. Interpretive Note

VAK 2.50 begins by completing the formula for `kāraṇa-hetu`: the causal field
excludes only the dharma itself. It then introduces a much stronger relation.
`Sahabhū-hetu` does not mean that two records share a timestamp. It claims
that determinations within one occurrence can be mutually sustaining causes
and results.

The example of citta and its followers is especially important. The Kośa
does not present citta as an isolated substance with detachable properties.
The cognitive occurrence is a structured complex whose members agree in
time, causal consequences, continuity, and ethical determination:

```text
CittaOccurrence {
    citta,
    associatedCaittas,
    restraints,
    conditionedMarks,
    sharedTemporalProfile,
    sharedResultProfile,
    sharedEthicalProfile
}
```

This supplies a real model of reciprocal Citta-formation. It should not,
however, be silently identified with the Yoga reconstruction
`Citta = <Buddhi, Ahaṃkāra, Manas>`. The Kośa relation is horizontal and
conditioned; the Yoga structure distinguishes the internal transcendental
functions that the Kośa does not preserve under those names.

Vasubandhu's objections make the passage even more valuable for an Ocular
Schema. A schema that stores only `coOccursWith` will conceal three possible
logical forms:

```text
CoPresence
CommonGenesis
ReciprocalCausation
```

These must remain different relation types. The three-staff analogy is not a
proof of reciprocity because the configuration may depend upon prior
placement, a cord, a peg, or the earth. The complete causal enclosure must
expose those supports instead of hiding them.

This is also the exact limit of our present analysis. The verse treats
`kāraṇa-hetu` and `sahabhū-hetu`; `pratyaya` remains outside the unit, and no
joining into Samādhi is performed. No Samādhi has been harmed.

The textual layers are:

```text
kārikā
    → defines the two causal types and gives three examples

Vaibhāṣika doctrine
    → asserts reciprocal causality within selected complexes

Vasubandhu's critical Bhāṣya
    → tests whether simultaneity shows reciprocal efficacy
      or only antecedent common production

Organon reconstruction
    → requires distinct Ocular relations for co-presence,
      common genesis, and reciprocal causation
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .

vak:KaranaHetu a organon:CausalRelationType .
vak:SahabhuHetu a organon:CausalRelationType .
vak:CittaFollower a organon:ConditionedDetermination .

organon:CoPresence a organon:RelationType .
organon:CommonGenesis a organon:CausalRelationType .
organon:ReciprocalCausation a organon:CausalRelationType .
organon:MutualResult a organon:ReciprocalCausation .

organon:coPresentWith a organon:SymmetricProperty .
organon:sharesAntecedentCauseWith a organon:SymmetricProperty .
organon:mutuallyConditions a organon:SymmetricProperty .
organon:followsCitta a organon:ObjectProperty .

organon:FollowerProfile a organon:Schema ;
    organon:requires organon:TemporalCorrespondence,
        organon:ResultCorrespondence,
        organon:MaturationCorrespondence,
        organon:OutflowCorrespondence,
        organon:EthicalCorrespondence .

organon:OcularCausalSchema a organon:Schema ;
    organon:distinguishes organon:CoPresence,
        organon:CommonGenesis,
        organon:ReciprocalCausation .

vak:Citta organon:mutuallyConditions vak:CittaFollower .
```
