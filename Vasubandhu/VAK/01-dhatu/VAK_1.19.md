# VAK_1.19

## 1. Sanskrit (Devanāgarī)

> जातिगोचरविज्ञानसामान्यादेकधातुता ।
>
> द्वित्वेऽपि चक्षुरादीनां शोभार्थं तु द्वयोद्भवः ॥ १.१९ ॥

## 2. Sanskrit (IAST)

> jātigocaravijñānasāmānyād ekadhātutā /
>
> dvitve 'pi cakṣurādīnāṃ śobhārthaṃ tu dvayodbhavaḥ // VAkK_1.19 //

Source label in GRETIL: `VAkK_1.19`. Project-normalized label: `VAkK_1.19`.

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| jāti | jāti | kind, class |
| gocara | gocara | range, object-field |
| vijñāna | vijñāna | knowledge |
| sāmānyāt | sāmānyāt | because of commonality |
| eka-dhātutā | eka-dhātutā | being one domain |
| dvitve api | dvitve api | even though dual |
| cakṣus-ādīnām | cakṣus-ādīnām | of eye and the others |
| śobhārtham | śobhārtham | for beauty/symmetry |
| tu | tu | but |
| dvaya-udbhavaḥ | dvaya-udbhavaḥ | arising as a pair |

## 4. Grammar

The verse explains why paired faculties such as the two eyes are counted as one domain.

They have commonality of:

```text
jāti       kind
 gocara    object-field
vijñāna    corresponding knowledge
```

Therefore they have **ekadhātutā**, one-domain status, even though they arise as pairs.

## 5. Literal Translation

> Because of commonality of kind, object-field, and knowledge, there is one-domain status, even in the duality of eye and the others. Their arising as pairs is for beauty/symmetry.

## 6. Philosophical Translation

> The paired sense faculties are counted as single domains because each pair shares the same class, object-range, and corresponding knowledge. Their dual occurrence serves bodily symmetry, not a doubling of domain-status.

Organon rendering:

> Domain-unity is not numerical singleness. Two eyes may function as one visual domain because their kind, object-field, and knowledge are common. The domain is determined by function and range, not by anatomical count.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| jāti | kind / class | shared nature of paired faculty |
| gocara | object-range | field of objects |
| vijñāna | knowledge | corresponding knowledge-domain |
| sāmānya | commonality | basis of one-domain status |
| ekadhātutā | one-domain status | unity despite paired occurrence |
| dvitva | duality | paired bodily manifestation |
| śobhā | beauty / symmetry | reason for paired arising |

## 8. Logical Determination

```text
one-domain status
    = common kind
    + common object-range
    + common knowledge
```

Thus:

```text
numerical duality
    ≠
domain duality
```

## 9. Interpretive Note

This verse prevents a crude counting error. Domain is not counted by visible organs but by functional unity. The two eyes are not two visual domains because they share one object-range and one corresponding knowledge-type.

Organon note:

```text
domain
    = functional unity of kind, range, and knowledge
```

This is a strong logical principle for all later modeling.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_19
    a vak:Karika ;
    rdfs:label "VAK 1.19" ;
    vak:hasSourceLabel "VAkK_1.19" ;
    vak:hasProjectLabel "VAkK_1.19" ;
    vak:hasTopic vak:OneDomainStatus ;
    vak:belongsTo vak:Dhatunirdesa .

vak:OneDomainStatus
    vak:groundedIn vak:CommonKind , vak:CommonObjectRange , vak:CommonKnowledge .
```

## 11. Commit History

- Upgraded VAK_1.19 with expanded Organon analysis.
- Explains one-domain status through common kind, object-range, and knowledge.
- Distinguishes paired bodily occurrence from domain plurality.
