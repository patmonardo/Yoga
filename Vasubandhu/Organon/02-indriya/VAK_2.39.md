# VAK_2.39

## 1. Sanskrit (Devanāgarī)

> निवृतस्य च रूपस्य कामे रूपस्य नाग्रजा ।
>
> अक्लिष्टाव्याकृताप्राप्तिः सातीताजातयोस्त्रिधा ॥ २.३९ ॥

## 2. Sanskrit (IAST)

> nivṛtasya ca rūpasya kāme rūpasya nāgrajā /
>
> akliṣṭāvyākṛtāprāptiḥ sātītājātayos tridhā // 2.39 //

Its first half completes VAK 2.38's acquisition discussion. Its second half
begins the classification of non-acquisition.

## 3. Lexical Analysis

```text
nivṛtasya ca        → nivṛtasya ca
kāme rūpasya        → kāme rūpasya
nāgrajā             → na agrajā
akliṣṭāvyākṛtāprāptiḥ → akliṣṭa-avyākṛtā aprāptiḥ
sātītājātayoḥ       → sā atīta-ajātayoḥ
tridhā              → tri-dhā
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| nivṛtasya | genitive singular | of obscured-indeterminate Form |
| kāme | locative singular | in the Desire Principle |
| rūpasya | genitive singular | of Form |
| na agrajā | negation and adjective | not prior-arisen |
| akliṣṭa-avyākṛtā | nominative feminine singular | unobscured and ethically indeterminate |
| aprāptiḥ | nominative feminine singular | non-acquisition |
| atīta-ajātayoḥ | genitive dual | of past and future Dharmas |
| tridhā | adverb | threefold |

## 4. Scientific English Rendering

> Acquisition of obscured-indeterminate manifest Form is also co-arisen;
> acquisition of Desire-Principle Form is not prior-arisen. Non-acquisition
> is unobscured and ethically indeterminate; for past and future Dharmas it
> is threefold.

The Bhāṣya states that a present Dharma's non-acquisition is present on its
provisional reading of the damaged source, while non-acquisition relative to
past or future Dharmas may be past, present, or future.

## 5. Interpretation

Non-acquisition does not inherit the ethical kind of the Dharma not
acquired. It is always unobscured-indeterminate, but remains temporally
indexed and can be classified in any of the three Principle-ranges. No
non-acquisition is itself uncontaminated.

The Bhāṣya uses non-acquisition of noble Dharma to test ordinary-person
status. A mere failure to possess every noble Dharma cannot be the rule:
a Buddha does not thereby lack the lineage-specific Dharmas of disciples
and solitary buddhas. The Sautrāntika account, which the text approves,
defines ordinary-person status as a continuum in which noble Dharmas have
not arisen.

Vijñāna governs a continuum under this determination; ordinary-person
status is not an immutable essence or moral insult. It is the specified
absence of arisen noble Dharma and is therefore transformable.

## 6. Logical Determination

```text
Aprapti(S, D)
    → EthicalKind = Indeterminate
      and AfflictionClass = Unobscured

DharmaTime(D) in {past, future}
    → ApraptiTime(S, D) in {past, present, future}

PrincipleRange(Aprapti(S, D))
    in {Desire, Form, Formless}
```

```text
Vaibhasika:
    OrdinaryPersonStatus(S)
      := RealNonAcquisition(S, NoblePath)

Sautrantika:
    OrdinaryPersonStatus(S)
      := NobleDharmasHaveNotArisen(S)
```

## 7. Interpretive Note

The source's temporal gloss at 66.04 is damaged. The study provisionally
reads it as present non-acquisition for a present Dharma, because that
agrees with the feminine predicate and contrasts with the threefold
past/future rule. It does not claim an independently collated emendation.

## 8. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_39
    a vak:Karika ;
    rdfs:label "VAK 2.39" ;
    vak:hasTopic vak:NonAcquisitionAndOrdinaryPersonStatus ;
    vak:belongsTo vak:Indriyanirdesa .

vak:NonAcquisition
    vak:hasEthicalKind vak:Indeterminate ;
    vak:hasAfflictionClass vak:Unobscured .
```
