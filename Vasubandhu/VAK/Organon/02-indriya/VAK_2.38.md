# VAK_2.38

## 1. Sanskrit (Devanāgarī)

> त्रिधा नशैक्षाशैक्षाणामहेयानां द्विधा मता ।
>
> अव्याकृताप्तिः सहजाभिज्ञानैर्माणिकादृते ॥ २.३८ ॥

## 2. Sanskrit (IAST)

> tridhā naśaikṣāśaikṣāṇām aheyānāṃ dvidhā matā /
>
> avyākṛtāptiḥ sahajābhijñānairmāṇikād ṛte // 2.38 //

The research witness leaves the sandhi of the final compound compressed.
The Bhāṣya requires the sense “except the superknowledges and the
magical-creation [mind].” The segmentation adopted below is therefore
Bhāṣya-controlled and remains philologically provisional.

## 3. Padaccheda

```text
tridhā               → tri-dhā
naśaikṣāśaikṣāṇām
                    → na-śaikṣa-aśaikṣāṇām
aheyānāṃ           → a-heyānām
dvidhā matā          → dvi-dhā matā
avyākṛtāptiḥ       → avyākṛta-āptiḥ
sahajā              → saha-jā
abhijñānairmāṇikād ṛte
                    → abhijñā-nairmāṇikāt ṛte
```

| Form | Morphology | Lexical force here |
|---|---|---|
| tridhā | adverb | threefold |
| na-śaikṣa-aśaikṣāṇām | genitive plural compound | of dharmas that are neither trainee nor beyond-training |
| aheyānām | genitive plural | of dharmas not subject to abandonment |
| dvidhā | adverb | twofold |
| matā | nominative feminine singular past passive participle | held / accepted; agrees with understood `prāptiḥ` |
| avyākṛta-āptiḥ | nominative feminine singular compound | acquisition of an indeterminate dharma |
| sahajā | nominative feminine singular | co-arisen / simultaneous |
| ṛte | indeclinable governing the ablative | except / apart from |
| abhijñā-nairmāṇikāt | ablative compound, exact formation provisional | from the superknowledge and magical-creation exception |

`Sahajā` describes temporal co-arising here. It must not be translated as
“innate,” because the issue is whether acquisition arises before, with, or
after its dharma.

## 4. Grammar

The first half supplies two rules with `prāptiḥ` understood:

```text
na-śaikṣa-aśaikṣāṇāṃ [prāptiḥ] tridhā
    → acquisition of dharmas that are neither trainee
      nor beyond-training is threefold

aheyānāṃ [prāptiḥ] dvidhā matā
    → acquisition of dharmas not subject to abandonment
      is held to be twofold
```

The compound `naśaikṣāśaikṣāṇām` is not a free-standing negation of
two separate genitives. It denotes the established third path-class:
`naiva-śaikṣa-nāśaikṣa`, neither trainee nor beyond-training.

The second half states a general temporal restriction and then an exception:

```text
avyākṛta-āptiḥ sahajā
    → acquisition of [unobscured] indeterminate dharmas
      is co-arisen

abhijñā-nairmāṇikāt ṛte
    → except for the superknowledges and magical-creation mind
```

The restriction to unobscured-indeterminate dharmas and the identification
of two indeterminate superknowledges are supplied by the Bhāṣya.

## 5. Translation

### Close syntactic construe

> For dharmas that are neither trainee nor beyond-training, acquisition is threefold; for those not subject to abandonment, it is held to be twofold. Acquisition of the indeterminate is co-arisen, except for the superknowledge and magical-creation case.

### Bhāṣya-informed translation

> The acquisition of a dharma classified as neither trainee nor beyond-training may itself be trainee, beyond-training, or neither. For dharmas not subject to abandonment, acquisition is either subject to abandonment through cultivation or is itself not subject to abandonment. The acquisition of an unobscured-indeterminate dharma ordinarily arises only together with that dharma, except in the case of the two indeterminate superknowledges and the mind producing magical creations, whose acquisition may precede, accompany, and follow their manifestation.

## 6. Philosophical Translation

> The status of an acquired dharma does not mechanically determine the status of its acquisition. The acquisition relation is sensitive to the Agent's path and manner of attainment. Its temporal reach also depends on developed causal power: a weak neutral occurrence is possessed only while manifest, whereas a neutral capacity produced through exceptional cultivation can be available beforehand and retained afterward.

VAK 2.38 therefore adds two independent determinations to the matrix of
VAK 2.37:

```text
status inheritance may be non-identical
temporal persistence depends on causal strength and cultivation
```

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| naivaśaikṣa-nāśaikṣa | neither trainee nor beyond-training | third path-status; includes contaminated dharmas and the unconditioned |
| śaikṣa | trainee | acquisition-status produced through a trainee path |
| aśaikṣa | beyond training | acquisition-status produced through a beyond-training path |
| aheya / apraheya | not subject to abandonment | uncontaminated dharma-status whose acquisition requires further differentiation |
| bhāvanāheya | abandoned through cultivation | status of certain acquisitions of otherwise non-abandonable cessations |
| avyākṛta | indeterminate | neither wholesome nor unwholesome |
| anivṛtāvyākṛta | unobscured-indeterminate | Bhāṣya restriction on the general co-arising rule |
| āpti / prāpti | acquisition-possession | the indexed status whose temporal mode is being classified |
| sahajā prāpti | co-arisen acquisition | acquisition simultaneous with manifestation of its dharma |
| agrajā prāpti | prior acquisition | possession-status arising before manifestation; Bhāṣya term |
| paścātkālajā prāpti | subsequent acquisition | possession-status continuing after manifestation; Bhāṣya term |
| abhijñā | superknowledge | here two ethically indeterminate superknowledges capable of temporally extended acquisition |
| nairmāṇika-citta | magical-creation mind | powerful cultivated neutral cognition that produces magical manifestations |
| prayogaviśeṣa | special preparatory practice | Bhāṣya explanation of the exception's causal power |

The Bhāṣya mentions certain exceptionally cultivated crafts and bodily
practices as a further attributed extension of the powerful-neutral pattern.
It does not make every learned skill an `abhijñā`.

## 8. Logical Determination

First, dharma-status and acquisition-status are separately typed:

```text
PathClass(D) = NeitherTraineeNorBeyond
    ⇏ PathClass(Prapti(S, D))
       = NeitherTraineeNorBeyond

PathClass(Prapti(S, D)) ∈ {
    Trainee,
    BeyondTraining,
    NeitherTraineeNorBeyond
}
```

For non-abandonable dharmas:

```text
AbandonmentClass(D) = NotAbandonable
    → AbandonmentClass(Prapti(S, D)) ∈ {
          AbandonedThroughCultivation,
          NotAbandonable
      }
```

The Bhāṣya grounds this variation in the mode of acquisition. For example:

```text
OrdinaryAcquisition(pratisaṃkhyā-nirodha)
    → AbandonedThroughCultivation(Prapti)

NoblePathAcquisition(pratisaṃkhyā-nirodha)
    → NotAbandonable(Prapti)
```

The general temporal rule for weak unobscured-indeterminate dharmas is:

```text
UnobscuredIndeterminate(D)
∧ WeakCausalPower(D)
    → AcquisitionMode(S, D) = CoArisenOnly
```

Hence:

```text
PraptiTime(S, D) = DharmaTime(D)
```

The cultivated exception is:

```text
SpecialCultivation(D)
∧ PowerfulNeutralCapacity(D)
    → AcquisitionMode(S, D) ∈ {
          Prior,
          CoArisen,
          Subsequent
      }
```

Ethical neutrality therefore does not entail functional weakness:

```text
EthicallyIndeterminate(D) ⇏ WeakCausalPower(D)
```

## 9. Interpretive Note

VAK 2.38 is an exception engine. VAK 2.37 established broad propagation
rules; this verse prevents those rules from erasing the history and power of
the acquiring continuum.

First, the path-status of a dharma and the path-status of its acquisition
can differ. Cessation through discriminative comprehension is the clearest
case: as an unconditioned dharma it belongs to neither the trainee nor the
beyond-training class in itself, yet its acquisition is classified according
to whether it is obtained through an ordinary, trainee, or completed path.
The relation records how the determination became available to this Agent.

Second, temporal reach measures developed capacity. An ordinary weak neutral
dharma has no possession-status before it manifests and leaves none afterward:

```text
manifestation boundary = possession boundary
```

The indeterminate superknowledges and magical-creation mind break this rule.
Special preparatory practice has transformed the continuum so that the
capacity is available before performance and retained after it:

```text
preparation → available capacity → manifestation → retained capacity
```

This makes `prāpti` a precise record of cultivated power rather than a label
attached to an isolated event. The practical distinction is:

```text
mere occurrence
    operates only while present

acquired capacity
    can precede performance and survive its completion
```

For the Kośa Technē, the rule is functional:

```text
deriveTemporalReach(capacity)
    from causalStrength + cultivationHistory
```

This is especially valuable for an Agent architecture: a trained capability
must not be confused with its current invocation. Yet the study remains
Kośa-clean. It does not identify `prāpti` with Yoga bhūmi-acquisition or read
the superknowledges as Absolute Reason. Those comparisons belong to the
project synthesis after the Kośa mechanism has been learned on its own terms.

The research Bhāṣya continues into obscured-indeterminate material form and
desire-realm material action. Those clauses are excluded here because they
belong to the following kārikā's continuation of the rule.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_38
    a vak:Karika ;
    rdfs:label "VAK 2.38" ;
    vak:hasTopic vak:NonInheritedPraptiStatus,
        vak:TemporalAcquisitionMode ;
    vak:belongsTo vak:Indriyanirdesa .

vak:NonInheritedPraptiStatus
    vak:distinguishes vak:DharmaPathClass,
        vak:PraptiPathClass,
        vak:DharmaAbandonmentClass,
        vak:PraptiAbandonmentClass .

vak:CoArisenOnlyRule
    vak:appliesTo vak:WeakUnobscuredIndeterminateDharma ;
    vak:requires vak:SameDharmaAndPraptiTime .

vak:PowerfulNeutralException
    vak:includes vak:TwoIndeterminateSuperknowledges,
        vak:MagicalCreationMind ;
    vak:isGroundedIn vak:SpecialPreparatoryPractice ;
    vak:permits vak:PriorPrapti,
        vak:CoArisenPrapti,
        vak:SubsequentPrapti .

organon:CultivatedCapacityStatus
    a organon:InterpretiveReconstruction ;
    organon:isDerivedFrom vak:CausalStrength,
        vak:CultivationHistory ;
    organon:distinguishes organon:CapacityAvailability,
        organon:CurrentInvocation .
```
