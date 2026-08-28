# VAK_2.34

## 1. Sanskrit (Devanāgarī)

> चित्तं मनोऽथ विज्ञानमेकार्थं चित्तचैतसाः ।
>
> साश्रयालम्बनाकाराः संप्रयुक्ताश्च पञ्चधा ॥ २.३४ ॥

## 2. Sanskrit (IAST)

> cittaṃ mano 'tha vijñānam ekārthaṃ cittacaitasāḥ /
>
> sāśrayālambanākārāḥ saṃprayuktāś ca pañcadhā // 2.34 //

## 3. Padaccheda

```text
cittaṃ              → cittam
mano 'tha           → manaḥ atha
vijñānam            → vijñānam
ekārthaṃ            → eka-artham
cittacaitasāḥ       → citta-caitasāḥ
sāśrayālambanākārāḥ
                    → sa-āśraya-ālambana-ākārāḥ
saṃprayuktāś ca     → saṃprayuktāḥ ca
pañcadhā            → pañcadhā
```

| Form | Morphology | Lexical force here |
|---|---|---|
| cittam | nominative neuter singular | consciousness |
| manaḥ | nominative neuter singular | mind / the supporting mental function |
| vijñānam | nominative neuter singular | differentiated cognition |
| eka-artham | nominative neuter singular compound | having one meaning or referent here |
| citta-caitasāḥ | nominative plural compound | consciousness and associated mental factors |
| sa-āśraya | possessive compound member | possessing a support |
| ālambana | compound member | cognitive support |
| ākāra | compound member | manner / aspect |
| saṃprayuktāḥ | nominative plural past passive participle | associated / conjoined |
| pañcadhā | adverb | fivefold |

`Ekārtha` establishes contextual co-reference, not unrestricted interchange
of all three terms in every doctrinal setting. `Vijñāna` remains
“differentiated cognition” in the controlled project vocabulary; `citta`
remains “consciousness.”

## 4. Grammar

The first half gives one predication over three coordinated subjects:

```text
cittam manaḥ vijñānam
    → consciousness, mind, and differentiated cognition

eka-artham
    → have one meaning / refer to one mental occurrence here
```

The Bhāṣya supplies two explanations. Etymologically:

```text
citta  ← cinoti     gathers or accumulates
manas  ← manute     thinks or considers
vijñāna ← vijānāti  discriminatively cognizes
```

Relationally, the same occurrence is called:

```text
citta
    insofar as it is variegated by wholesome and unwholesome dharmas

manas
    insofar as it functions as support

vijñāna
    insofar as it functions as supported differentiated cognition
```

The second half characterizes consciousness and mental factors:

```text
sa-āśraya
    → possessing a support because dependent upon a faculty

sa-ālambana
    → possessing one registered viṣaya as cognitive support

sa-ākāra
    → taking that registered event in a determinate manner

saṃprayuktāḥ pañcadhā
    → associated through five equalities
```

The Kārikā compresses the fivefold rule; the Bhāṣya enumerates equality of
support, cognitive support, manner, time, and numerical instance.

## 5. Translation

### Close syntactic construe

> Consciousness, mind, and differentiated cognition have one meaning [here]. Consciousness and the mental factors possess support, cognitive support, and manner, and are associated fivefold.

### Bhāṣya-informed translation

> `Citta`, `manas`, and `vijñāna` designate one mental occurrence under different functional descriptions: gathering or variegated consciousness, supporting mind, and supported differentiated cognition. Consciousness and its associated factors constitute one cognition-event through equality of faculty-support, equality of the indriya-registered event serving as cognitive support, equality of the manner in which it is taken, equality of time, and a one-to-one numerical instance of consciousness and each associated factor.

The reference to an indriya-registered event is the project's controlled
rendering of the Bhāṣya's `viṣaya`/`ālambana` relation. It must not be
externalized into a ready-made object standing outside the cognition-event.

## 6. Philosophical Translation

> One cognition is neither a bare consciousness nor a heap of mental factors. Its differentiated members belong together because they share the same faculty-support, registered event, manner, and moment, with one determinate instance of each factor. Unity does not erase functional difference, and difference does not dissolve the event.

Restrained Organon rendering:

> The Kośa defines organic event-unity through five equality constraints. A factor belongs to an event only when its provenance, registered content, manner, time, and numerical instance agree with that event. `Citta`, `manas`, and `vijñāna` are then three functional addresses of this one organized occurrence.

“Organic event-unity,” “provenance,” and “functional address” are project
renderings. The textual rule is fivefold `saṃprayoga`.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination in this unit |
|---|---|---|
| citta | consciousness | one occurrence as gathering or variegated by wholesome and unwholesome dharmas |
| manas | mind / support-function | the same occurrence considered insofar as it supports |
| vijñāna | differentiated cognition | the same occurrence considered insofar as it discriminatively cognizes and is supported |
| ekārtha | one meaning / one referent | contextual equivalence without erasing functional denomination |
| āśraya | faculty-support | indriya upon which consciousness and factors depend |
| viṣaya | indriya-registered event | determinate event registered through faculty-operation |
| ālambana | cognitive support | the registered `viṣaya` insofar as cognition and factors take it up |
| ākāra | manner / aspect | determinate way the registered event is cognitively taken |
| saṃprayoga | association / conjunction | event-unity of consciousness and factors through five equalities |
| āśraya-samatā | equality of support | same faculty-support |
| ālambana-samatā | equality of cognitive support | same registered event functioning as support |
| ākāra-samatā | equality of manner | same way of taking the registered event |
| kāla-samatā | equality of time | occurrence in the same moment (`kṣaṇa`) |
| dravya-samatā | equality of numerical instance | one consciousness and one instance of each associated factor |

`Dravya` here must not be heard as material substance. The Bhāṣya explains
the equality numerically: one instance of each factor corresponds to the one
consciousness-event.

## 8. Logical Determination

Contextual co-reference is role-indexed:

```text
OneMentalOccurrence(e)

Citta(e)
    = describe(e, GatheringOrVariegatedRole)

Manas(e)
    = describe(e, SupportingRole)

Vijnana(e)
    = describe(e, SupportedDiscriminativeRole)
```

Therefore:

```text
Referent(Citta(e))
    = Referent(Manas(e))
    = Referent(Vijnana(e))

Role(Citta) ≠ Role(Manas) ≠ Role(Vijnana)
```

Let `c` be one consciousness-instance and `F` its associated factor-set.
Fivefold association requires:

```text
ForEvery f in F:
    Support(f) = Support(c)
    ∧ Alambana(f) = Alambana(c)
    ∧ Akara(f) = Akara(c)
    ∧ Time(f) = Time(c)
    ∧ InstanceCount(f, event) = 1
```

The cognitive support is typed through registration:

```text
RegisteredBy(visayaEvent, indriya)
∧ SupportsCognition(visayaEvent, event)
    → Alambana(event) = visayaEvent
```

Numerical equality prevents heap semantics:

```text
One CittaInstance(event)
∧ ForEvery required FactorType T:
      ExactlyOne InstanceOf(T, event)
```

Mere simultaneity is necessary but insufficient:

```text
SameTime(x, y)
    ⇏ Associated(x, y)

Associated(x, y)
    → SameSupport
      ∧ SameAlambana
      ∧ SameAkara
      ∧ SameTime
      ∧ CorrespondingNumericalInstance
```

## 9. Interpretive Note

VAK 2.34 answers the problem generated by the entire mental-factor section:
how can many distinct factors constitute one cognition? The answer is neither
an underlying mental substance nor accidental proximity. The factors belong
to one event through five determinate equalities.

The first three equalities preserve intentional and functional unity. The
same faculty supports consciousness and its factors. The same indriya-
registered `viṣaya` serves as their cognitive support. They take that event
in the same manner. This does not mean the registered event is an external
object imported ready-made into consciousness; it is already determinate as
registered within the cognition-event.

Equality of time now sharpens the `kṣaṇa` discovery from VAK 2.33. A bhūmi
may possess factors across its organized temporal range, but `saṃprayoga`
requires same-moment unity. The moment is therefore the boundary at which
the many associated functions count as one actual cognition.

Equality of numerical instance prevents this unity from becoming an
indefinite aggregate. There is one consciousness-instance and one instance of
each factor belonging to that event. Organic unity is exact cardinality under
shared relations.

The terminology dispute is equally productive. `Citta`, `manas`, and
`vijñāna` have one referent here, but the Bhāṣya preserves different
functional grounds for naming it. The project should therefore not collapse
them into one undifferentiated word:

```text
citta
    consciousness as gathered and qualified occurrence

manas
    the occurrence in its supporting function

vijñāna
    the occurrence as supported differentiated cognition
```

The user's Yoga hypothesis can now be stated more cleanly without asserting
lexical identity:

```text
kṣaṇa
    = event-boundary of actual cognitive Being

krama
    = ordered transition between such event-unities

samāpatti
    = candidate name for achieved or stabilized event-unity
      within the Yoga reconstruction
```

The Kośa does not say `kṣaṇa = samāpatti`. What it supplies is the exact
association structure that makes such a comparative hypothesis intelligible:
a one-moment unity of support, registered event, manner, and differentiated
functions. We should test the Samāpatti identification later rather than make
it a translation premise.

For the Kośa Technē:

```text
CognitionEvent<ksana> = {
    oneCitta,
    oneOfEachRequiredCaitta,
    sharedIndriyaSupport,
    sharedRegisteredVisaya,
    sharedAkara
}
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix yoga: <http://127.0.0.1:3000/yoga#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_34
    a vak:Karika ;
    rdfs:label "VAK 2.34" ;
    vak:hasTopic vak:CittaManasVijnanaEkartha,
        vak:FivefoldAssociation ;
    vak:belongsTo vak:Indriyanirdesa .

vak:CittaManasVijnanaEkartha
    vak:hasOneReferent vak:MentalOccurrence ;
    vak:hasFunctionalAddress vak:CittaRole,
        vak:ManasRole,
        vak:VijnanaRole .

vak:FivefoldAssociation
    vak:requiresEquality vak:SupportEquality,
        vak:AlambanaEquality,
        vak:AkaraEquality,
        vak:TimeEquality,
        vak:NumericalInstanceEquality .

vak:AlambanaEquality
    vak:requires vak:SharedIndriyaRegisteredVisaya .

vak:TimeEquality
    vak:requires vak:SameKsana .

organon:OrganicCognitionEvent
    a organon:InterpretiveReconstruction ;
    organon:requires vak:FivefoldAssociation ;
    organon:distinguishes organon:FunctionalDifference,
        organon:EventUnity .

yoga:KsanaSamapattiHypothesis
    a organon:ComparativeHypothesis ;
    organon:requiresFurtherTesting vak:SameKsana,
        yoga:Samapatti .
```
