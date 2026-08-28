# VAK_2.39

## 1. Sanskrit (Devanāgarī)

> निवृतस्य च रूपस्य कामे रूपस्य नाग्रजा ।
>
> अक्लिष्टाव्याकृताप्राप्तिः सातीताजातयोस्त्रिधा ॥ २.३९ ॥

## 2. Sanskrit (IAST)

> nivṛtasya ca rūpasya kāme rūpasya nāgrajā /
>
> akliṣṭāvyākṛtāprāptiḥ sātītājātayos tridhā // 2.39 //

This repository witness crosses a doctrinal verse-boundary. Its first half
continues the acquisition rule discussed at the end of the VAK 2.38 Bhāṣya;
its second half opens the `aprāpti` rule quoted at the beginning of the VAK
2.39 Bhāṣya. The official study preserves the supplied kārikā witness and
makes the boundary mismatch explicit rather than silently renumbering it.

## 3. Padaccheda

```text
nivṛtasya ca        → nivṛtasya ca
rūpasya             → rūpasya
kāme                → kāme
rūpasya             → rūpasya
nāgrajā             → na agrajā
akliṣṭāvyākṛtāprāptiḥ
                    → akliṣṭa-avyākṛtā aprāptiḥ
sātītājātayoḥ       → sā atīta-ajātayoḥ
tridhā               → tri-dhā
```

| Form | Morphology | Lexical force here |
|---|---|---|
| nivṛtasya | genitive neuter singular | of obscured [indeterminate] material form |
| ca | conjunction | and / also; continues the preceding co-arising rule |
| rūpasya | genitive neuter singular | of material form |
| kāme | locative masculine singular | in the desire realm |
| na agrajā | negation plus nominative feminine singular compound | [acquisition is] not prior-arisen |
| akliṣṭa-avyākṛtā | nominative feminine singular compound | unobscured and ethically indeterminate |
| aprāptiḥ | nominative feminine singular | non-acquisition / non-possession |
| sā | nominative feminine singular pronoun | it, that non-acquisition |
| atīta-ajātayoḥ | genitive dual | of past and not-yet-arisen dharmas |
| tridhā | adverb | threefold |

The sandhi `akliṣṭāvyākṛtāprāptiḥ` must be divided as
`akliṣṭa-avyākṛtā aprāptiḥ`, not as a compound ending in positive
`prāpti`. The Bhāṣya's question and answer explicitly concern the
classification of non-acquisition.

## 4. Grammar

The first half presupposes the predicate `sahajā [prāptiḥ]` from the
preceding rule:

```text
nivṛtasya ca rūpasya [prāptiḥ sahajā]
    → acquisition of obscured-indeterminate material form
      is also co-arisen

kāme rūpasya [prāptiḥ] na agrajā
    → acquisition of desire-realm material form
      is not prior-arisen
```

The Bhāṣya clarifies that the first rule concerns obscured-indeterminate
manifest material action. The second covers manifest and non-manifest
desire-realm material form: co-arisen and subsequent acquisition exist, but
prior acquisition does not.

The second half changes subject from `prāpti` to `aprāpti`:

```text
aprāptiḥ akliṣṭa-avyākṛtā
    → non-acquisition is unobscured-indeterminate

sā atīta-ajātayoḥ tridhā
    → for past and future dharmas, it is threefold
```

Here `ajāta`, literally “not arisen,” is interpreted temporally by the Bhāṣya
as future.

## 5. Translation

### Close syntactic construe

> For obscured material form also [acquisition is co-arisen]; for material form in the desire realm, it is not prior-arisen. Non-acquisition is unobscured-indeterminate; for past and not-yet-arisen dharmas, it is threefold.

### Bhāṣya-informed translation

> The acquisition of obscured-indeterminate manifest material action arises only together with that action. Desire-realm material form has no acquisition preceding its occurrence, although co-arisen and subsequent acquisition are admitted. Non-acquisition is always unobscured and ethically indeterminate. For a present dharma it is present only; for a past or future dharma, non-acquisition may itself be past, present, or future.

## 6. Philosophical Translation

> Possession cannot precede every kind of determination. Weak or materially enacted capacities may become attributable to a continuum only when they occur, although some leave a retained status afterward. Non-acquisition is even more strictly typed: it carries no affliction or positive ethical quality of its own, yet it has a determinate temporal profile relative to what has not been acquired.

The composite witness therefore presents two complementary constraints:

```text
prāpti:
    temporal reach is limited by the power and kind of its dharma

aprāpti:
    negative status is ethically neutral but temporally indexed
```

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| nivṛta | obscured | here completed by the Bhāṣya as obscured-indeterminate material form |
| nivṛtāvyākṛta rūpa | obscured-indeterminate material form | manifest material action whose acquisition is only co-arisen |
| kāmāvacara rūpa | desire-realm material form | manifest and non-manifest form for which prior acquisition is excluded |
| agrajā prāpti | prior acquisition | possession-status preceding manifestation of its dharma |
| sahajā prāpti | co-arisen acquisition | status arising simultaneously with its dharma |
| paścātkālajā prāpti | subsequent acquisition | status retained after manifestation |
| aprāpti | non-acquisition / non-possession | conditioned negative status in the Vaibhāṣika classification; critically redescribed through continuum-history by Vasubandhu |
| akliṣṭa | unobscured / non-afflicted | free from afflictive obscuration |
| avyākṛta | ethically indeterminate | neither wholesome nor unwholesome |
| atīta | past | time-class of the dharma relative to which non-acquisition is classified |
| ajāta | not yet arisen / future | future dharma in the Bhāṣya's temporal expansion |

`Akliṣṭa` and `avyākṛta` name separate axes: non-afflicted status and
ethical indeterminacy. Neither should be made redundant in translation.

## 8. Logical Determination

The remaining acquisition exceptions are:

```text
ObscuredIndeterminateManifestRupa(D)
    → AcquisitionMode(S, D) = CoArisenOnly

DesireRealmRupa(D)
    → AcquisitionMode(S, D) ⊆ {
          CoArisen,
          Subsequent
      }
    ∧ Prior ∉ AcquisitionMode(S, D)
```

The non-acquisition type invariant is:

```text
Aprapti(S, D)
    → AfflictionClass = Unobscured
      ∧ EthicalClass = Indeterminate
```

Its temporal rule distinguishes present from non-present dharmas:

```text
DharmaTime(D) = Present
    → ApraptiTime(S, D) = Present

DharmaTime(D) ∈ {Past, Future}
    → ApraptiTime(S, D) ∈ {
          Past,
          Present,
          Future
      }
```

Thus structured non-acquisition is not a timeless logical `false`. It is a
status asserted within the temporal history of a continuum:

```text
NOT Prapti(S, D)
    ≠ untyped absence

Aprapti(S, D, time)
    = classified non-possession within the admissible domain
```

Vasubandhu's broader critique still applies: the classification need not be
implemented as an additional negative substance. It may report that the
relevant dharma or capacity has not arisen in the continuum.

## 9. Interpretive Note

The first half closes the question of how far acquisition can extend around
a material occurrence. Obscured-indeterminate manifest action is too weak to
establish possession before or after itself. Desire-realm form permits a
retained acquisition but no acquisition in advance. The difference confirms
the finding of VAK 2.38: temporal reach expresses causal strength and history,
not merely ethical class.

The second half begins the positive classification of a negative status.
Every `aprāpti` is unobscured-indeterminate. This does not mean it is an
indifferent nothing. It means that non-possession does not inherit the
wholesome, unwholesome, or afflicted character of the unpossessed dharma.

The temporal matrix is asymmetric:

```text
present dharma
    → present non-acquisition only

past or future dharma
    → past, present, or future non-acquisition
```

For the Kośa Technē, `aprāpti` is therefore a typed negative judgment:

```text
ApraptiStatus {
    continuum
    dharma
    dharmaTime
    apraptiTime
    afflictionClass: unobscured
    ethicalClass: indeterminate
}
```

But the distinction from VAK 2.36 must remain active:

```text
semantic status
    must be represented

separate negative entity
    need not be reified
```

This is the compulsory method in miniature. A failure of acquisition is not
recorded as an intuition or a blank. It is tested against domain, time, and
continuum-history until its exact status can be reconstructed.

The Bhāṣya witness proceeds to realm classifications, Path non-acquisition,
and ordinary-person status because its quoted kārikā has a different second
half. Those determinations are deferred to VAK 2.40 in the repository's
official sequence.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_39
    a vak:Karika ;
    rdfs:label "VAK 2.39" ;
    vak:hasTopic vak:RupaPraptiExceptions,
        vak:ApraptiClassification ;
    vak:hasWitnessBoundary vak:CompositeVerseBoundary ;
    vak:belongsTo vak:Indriyanirdesa .

vak:RupaPraptiExceptions
    vak:restricts vak:PriorPrapti,
        vak:SubsequentPrapti ;
    vak:isConditionedBy vak:RupaType,
        vak:CausalStrength .

vak:ApraptiClassification
    vak:requiresAfflictionClass vak:Unobscured ;
    vak:requiresEthicalClass vak:Indeterminate ;
    vak:hasIndependentIndex vak:DharmaTime,
        vak:ApraptiTime .

organon:TypedNegativeStatus
    a organon:InterpretiveReconstruction ;
    organon:represents vak:ApraptiClassification ;
    organon:isDerivedFrom vak:ContinuumHistory ;
    organon:isNot organon:UntypedBooleanFalse,
        organon:IndependentNegativeSubstance .
```
