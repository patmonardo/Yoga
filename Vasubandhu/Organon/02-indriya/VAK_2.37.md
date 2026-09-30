# VAK_2.37

## 1. Sanskrit (Devanāgarī)

> त्रैयध्विकानां त्रिविधा शुभादीनां शुभादिका ।
>
> स्वधातुका तदाप्तानां अनाप्तानां चतुर्विधा ॥ २.३७ ॥

## 2. Sanskrit (IAST)

> traiyadhvikānāṃ trividhā śubhādīnāṃ śubhādikā /
>
> svadhātukā tadāptānām anāptānāṃ caturvidhā // 2.37 //

## 3. Padaccheda

```text
traiyadhvikānāṃ     → trai-adhvika-ānām
trividhā            → tri-vidhā
śubhādīnāṃ          → śubha-ādīnām
śubhādikā           → śubha-ādikā
svadhātukā          → sva-dhātukā
tadāptānām         → tad-āptānām
anāptānāṃ          → an-āptānām
caturvidhā          → catur-vidhā
```

| Form | Morphology | Lexical force here |
|---|---|---|
| traiyadhvikānām | genitive masculine/neuter plural | of dharmas belonging to the three times |
| trividhā | nominative feminine singular | threefold |
| śubha-ādīnām | genitive plural | of wholesome [dharmas] and the remaining ethical classes |
| śubha-ādikā | nominative feminine singular | correspondingly wholesome and so forth |
| sva-dhātukā | nominative feminine singular | belonging to the same realm as its dharma |
| tad-āptānām | genitive plural | of dharmas included in that [realm-classification] |
| an-āptānām | genitive plural | of dharmas not included in a realm |
| caturvidhā | nominative feminine singular | fourfold |

The understood feminine subject throughout is `prāpti`. Here `āpta` and
`anāpta` concern inclusion in a `dhātu` or realm, not acquisition and
non-acquisition. Reading them as “acquired/unacquired” would confuse the
classification of `prāpti` with the relation being classified.

## 4. Grammar

The verse consists of four genitive constructions with an understood
`prāpti`:

```text
traiyadhvikānāṃ [prāptiḥ] trividhā
    → the acquisition of three-time dharmas is threefold

śubhādīnāṃ [prāptiḥ] śubhādikā
    → the acquisition of wholesome and other dharmas
      is correspondingly wholesome and so forth

tadāptānāṃ [prāptiḥ] svadhātukā
    → the acquisition of dharmas included in a realm
      belongs to that same realm

anāptānāṃ [prāptiḥ] caturvidhā
    → the acquisition of dharmas not included in a realm
      is fourfold
```

`Traiyadhvika` does not merely divide all acquisition into past, present,
and future once. According to the Bhāṣya, the acquisition of a dharma at
each of the three times may itself be past, future, or present. The time of
the dharma and the time of its acquisition-status are therefore distinct
indices.

## 5. Translation

### Close syntactic construe

> For dharmas belonging to the three times, acquisition is threefold; for wholesome and the other [ethical classes], it is correspondingly wholesome and so forth. For dharmas included in a realm, it belongs to that same realm; for those not included in a realm, it is fourfold.

### Bhāṣya-informed translation

> The acquisition of a past, future, or present dharma may itself be past, future, or present. The acquisition of a wholesome, unwholesome, or indeterminate dharma has the corresponding ethical status. The acquisition of a desire-, form-, or formless-realm dharma belongs to that same realm. The acquisition of a dharma not included in any realm may be desire-realm, form-realm, formless-realm, or uncontaminated.

The Bhāṣya subsequently adds path-stage and abandonment classifications.
Those elaborations explain the matrix but are not separately stated in the
kārikā.

## 6. Philosophical Translation

> Acquisition is not an unqualified link between a continuum and a dharma. It is itself determined by time, ethical character, realm, path-stage, and mode of abandonment. To know that a continuum possesses a dharma is therefore to know a structured and indexed status, not merely to attach a binary label.

The same acquired dharma can receive a different acquisition-status according
to the continuum and path through which it is acquired. This is most evident
with cessation through discriminative comprehension: its acquisition may be
ordinary, trainee, or beyond-training in status according to the relevant
mode of attainment.

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| traiyadhvika | belonging to the three times | past, future, or present; applies independently to dharma and acquisition |
| śubha | wholesome | ethical class corresponding here to wholesome acquisition |
| aśubha | unwholesome | ethical class supplied by the Bhāṣya's threefold expansion |
| avyākṛta | indeterminate | neither wholesome nor unwholesome |
| dhātu | realm | here the desire, form, or formless realm, not the eighteen-domain analysis of Chapter 1 |
| svadhātuka | belonging to the same realm | acquisition mirrors the realm of a realm-bound dharma |
| tadāpta | included in that realm | a dharma belonging to one of the three realms |
| anāpta | not included in a realm | a realm-unbound or uncontaminated dharma; not “unacquired” here |
| anāsrava | uncontaminated | fourth possible status for acquisition of a realm-unbound dharma |
| śaikṣa | trainee | path-status of a trainee's dharmas and their acquisition |
| aśaikṣa | beyond training | path-status of one beyond training and the relevant acquisition |
| naivaśaikṣa-nāśaikṣa | neither trainee nor beyond training | status of contaminated dharmas and the unconditioned, subject to further differentiation |
| darśanaheya | abandoned through seeing | abandonment-class mirrored by acquisition |
| bhāvanāheya | abandoned through cultivation | abandonment-class mirrored by acquisition |
| aheya | not subject to abandonment | uncontaminated status, with the Bhāṣya distinguishing how its acquisition is obtained |

The verse's `śubha` is retained in translation rather than silently
normalized to `kuśala`. The Bhāṣya-informed ethical triad is nevertheless
the familiar wholesome, unwholesome, and indeterminate classification.

## 8. Logical Determination

Let `P = Prapti(S, D)` be the acquisition-status of dharma `D` in continuum
`S`. VAK 2.37 makes `P` a typed relation with independent indices:

```text
P = {
    continuum: S,
    dharma: D,
    dharmaTime,
    praptiTime,
    ethicalClass,
    realmClass,
    pathClass,
    abandonmentClass
}
```

Time is a cross-product rather than a simple inherited value:

```text
DharmaTime(D) ∈ {past, future, present}
PraptiTime(P) ∈ {past, future, present}

For each DharmaTime(D):
    PraptiTime(P) may be past, future, or present
```

Ethical status normally mirrors its dharma:

```text
EthicalClass(P) = EthicalClass(D)
```

Realm status branches:

```text
RealmBound(D, R)
    → RealmClass(P) = R

RealmUnbound(D)
    → RealmClass(P) ∈ {
          desireRealm,
          formRealm,
          formlessRealm,
          uncontaminated
      }
```

The Bhāṣya prevents the fourfold rule from being treated as arbitrary:

```text
Prapti(apratisaṃkhyā-nirodha)
    ∈ {desireRealm, formRealm, formlessRealm}

Prapti(pratisaṃkhyā-nirodha)
    ∈ {formRealm, formlessRealm, uncontaminated}

Prapti(pathTruth)
    = uncontaminated
```

Across all realm-unbound dharmas collectively, these possibilities yield
the stated fourfold classification.

## 9. Interpretive Note

VAK 2.37 is the classification matrix presupposed by the simpler language of
“possession.” A bare assertion such as `Possesses(S, D)` is informationally
incomplete. The Kośa requires the status to answer: when is the dharma; when
is its acquisition; what is its ethical quality; in which realm does the
acquisition occur; what path-stage does it express; and how is it related to
abandonment?

The first rule is particularly important for the Kośa's time-schema. A past
dharma may have a present acquisition; a future dharma may have a past
acquisition; and each remaining combination is likewise admitted. The dharma
and its acquisition-status must therefore be tracked independently:

```text
time of determination ≠ time of possession-status
```

The second and third rules mostly propagate constraints: acquisition mirrors
the ethical class and, for realm-bound dharmas, the realm of what is acquired.
The fourth rule introduces controlled polymorphism. A realm-unbound dharma
does not force its acquisition to be realm-unbound, because a continuum
within one of the three realms may acquire certain unconditioned cessations.

The Bhāṣya extends the same discipline to path and abandonment status. A
cessation does not carry one invariant acquisition-class independently of
the Agent. Its status depends on whether it is acquired by an ordinary
person, a trainee, or one beyond training, and through what path.

For the Kośa Technē:

```text
prāpti is not a boolean field
prāpti is an indexed derivation
```

This strengthens the conclusion of VAK 2.36. If possession-status is derived
from the continuum's capacities, then VAK 2.37 specifies the contextual
indices required by that derivation. The verse does not yet supply an
implementation algorithm; it supplies the schema that any adequate
implementation must preserve.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_37
    a vak:Karika ;
    rdfs:label "VAK 2.37" ;
    vak:hasTopic vak:PraptiClassificationMatrix ;
    vak:belongsTo vak:Indriyanirdesa .

vak:PraptiClassificationMatrix
    vak:hasIndependentIndex vak:DharmaTime,
        vak:PraptiTime ;
    vak:hasStatusAxis vak:EthicalClass,
        vak:RealmClass,
        vak:PathClass,
        vak:AbandonmentClass .

vak:RealmBoundPraptiRule
    vak:requires vak:SameRealmAsAcquiredDharma .

vak:RealmUnboundPraptiRule
    vak:permits vak:DesireRealmPrapti,
        vak:FormRealmPrapti,
        vak:FormlessRealmPrapti,
        vak:UncontaminatedPrapti .

organon:IndexedPraptiStatus
    a organon:InterpretiveReconstruction ;
    organon:isDerivedFor vak:Continuum,
        vak:Dharma ;
    organon:requiresIndex vak:DharmaTime,
        vak:PraptiTime,
        vak:EthicalClass,
        vak:RealmClass,
        vak:PathClass,
        vak:AbandonmentClass ;
    organon:isNot organon:BooleanAttachment .
```
