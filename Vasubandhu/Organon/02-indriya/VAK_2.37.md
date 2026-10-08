# VAK_2.37 — Five Classifications of Acquisition

## 1. Sanskrit (Devanāgarī)

> त्रैयध्विकानां त्रिविधा शुभादीनां शुभादिका ।
>
> स्वधातुका तदाप्तानां अनाप्तानां चतुर्विधा ॥ २.३७ ॥

## 2. Sanskrit (IAST)

> traiyadhvikānāṃ trividhā śubhādīnāṃ śubhādikā /
>
> svadhātukā tadāptānām anāptānāṃ caturvidhā // 2.37 //

## 3. Lexical Analysis

```text
traiyadhvikānāṃ → trai-adhvika-ānām
trividhā        → tri-vidhā
śubhādīnāṃ      → śubha-ādīnām
śubhādikā       → śubha-ādikā
svadhātukā      → sva-dhātukā
tadāptānām     → tad-āptānām
anāptānāṃ      → an-āptānām
caturvidhā     → catur-vidhā
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| traiyadhvikānām | genitive plural | of Dharmas belonging to the three times |
| trividhā | nominative feminine singular | threefold |
| śubha-ādīnām | genitive plural | of wholesome and other ethical kinds |
| śubhādikā | nominative feminine singular | corresponding in ethical kind |
| sva-dhātukā | nominative feminine singular | belonging to the same Principle-range |
| tad-āptānām | genitive plural | of Dharmas included in that Principle-range |
| anāptānām | genitive plural | of Dharmas not included in the three Principle-ranges |
| caturvidhā | nominative feminine singular | fourfold |

The understood subject is *prāpti*. Here *tadāpta* and *anāpta* concern
inclusion in a Principle-range; *anāpta* is not *aprāpta*, non-acquisition.

## 4. Scientific English Rendering

> Acquisition of Dharmas belonging to the three times is threefold;
> acquisition of wholesome and other Dharmas corresponds to their ethical
> kind. Acquisition of a Dharma included in a Principle-range belongs to
> that same Principle-range; acquisition of a Dharma not so included is
> fourfold.

The Bhāṣya explains: a past, future, or present Dharma may have acquisition
that is itself past, future, or present; wholesome, unwholesome, and
indeterminate Dharmas have the corresponding acquisition; acquisition of
Desire-, Form-, and Formless-Principle Dharmas belongs respectively to
those same Principle-ranges; eligible uncontaminated Dharmas may have
acquisition in the three Principle-ranges or uncontaminated acquisition.

## 5. Interpretation

VAK 2.37 makes *prāpti* a typed relation rather than a binary possession
label. The time, ethical kind, Principle-range, training status, and
abandonment status of the acquired Dharma and of its acquisition must be
kept distinct.

The Bhāṣya gives decisive examples. Cessation independent of discriminative
comprehension has acquisition in the three Principle-ranges; cessation
through discriminative comprehension can have Form-Principle, Formless-
Principle, or uncontaminated acquisition; the truth of the Path has only
uncontaminated acquisition. Space remains outside both acquisition and
non-acquisition under the earlier restriction.

The Kośa-wide synthesis remains: Vijñāna is Discriminative Cognition joining
and governing Perception and Conception. Its unity is Inconceivable as
homogeneous operation, disclosed in the Cognition Base. Vijñāna governs Mind
and guides Dharma Base; *avijñapti* is the same Dharma classified in Form
Base and Dharma Base, with Vijñāna bearing a *prati* relation to it. The
acquisition matrix specifies the continuum-status by which such an impure
or purified Dharma can become available.

## 6. Logical Determination

```text
Prapti(S, D) has independent indices:
    DharmaTime(D)
    AcquisitionTime
    EthicalKind
    PrincipleRange
    TrainingStatus
    AbandonmentStatus
```

```text
DharmaTime(D) in {past, future, present}
    does not fix
AcquisitionTime(S, D)

EthicalKind(Prapti(S, D))
    = EthicalKind(D)
```

```text
IncludedInPrincipleRange(D, R)
    → PrincipleRange(Prapti(S, D)) = R

EligibleUncontaminated(D)
    → PrincipleRange(Prapti(S, D))
      in {Desire, Form, Formless, Uncontaminated}
```

## 7. Interpretive Note

The Bhāṣya continues the account of acquisition after the dispute in VAK
2.36 and marks it with reportive *kila*. It does not silently settle the
earlier disagreement about whether acquisition is a distinct real Dharma.
The opening of VAK 2.38 completes its training and abandonment
classifications; VAK 2.38 proper then begins the exception to this temporal
matrix.

## 8. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_37
    a vak:Karika ;
    rdfs:label "VAK 2.37" ;
    vak:hasTopic vak:AcquisitionClassificationMatrix ;
    vak:belongsTo vak:Indriyanirdesa .

vak:Acquisition
    vak:hasIndex vak:AcquisitionTime,
        vak:EthicalKind,
        vak:PrincipleRange,
        vak:TrainingStatus,
        vak:AbandonmentStatus .
```
