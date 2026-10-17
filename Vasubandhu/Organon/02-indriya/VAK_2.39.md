# VAK_2.39 — Form, then Non-Acquisition

## 1. Sanskrit (Devanāgarī)

```sanskrit
निवृतस्य च रूपस्य कामे रूपस्य नाग्रजा ।
अक्लिष्टाव्याकृताप्राप्तिः सातीताजातयोस्त्रिधा ॥ २.३९ ॥
```

## 2. Sanskrit (IAST)

```text
nivṛtasya ca rūpasya kāme rūpasya nāgrajā /
akliṣṭāvyākṛtāprāptiḥ sātītājātayos tridhā // 2.39 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| nivṛtasya rūpasya | gen. sg. n.; compound | of obscured form |
| kāme rūpasya | loc. sg. n. + gen. sg. n. | of form in the desire realm |
| na agrajā | negation + nom. sg. f. | not prior-arisen |
| aprāptiḥ | nom. sg. f. | non-acquisition |
| atīta-ajātayoḥ | gen. dual m. | of past and not-yet-arisen |
| tridhā | adverb | threefold |

Not-yet-arisen is future. Unobscured and indeterminate are two axes.
## 4. Grammar

```text
% start S
S[FORM=obscured-indeterminate, MANIFEST=true] -> Acquisition[COARISE=true]
S[FORM=desire] -> Acquisition[PRIOR=false, COARISE=true, SUBSEQUENT=true]
S[NAME=non-acquisition] -> UnobscuredIndeterminate
S[TIME=past|future] -> NonAcquisition[TIME=past|present|future]
```

Obscured form is co-arisen only.  
Desire-realm form admits co-arisen and subsequent, not prior.  
Non-acquisition is always unobscured-indeterminate.

## 5. Translation

### Literal Translation

> Acquisition of obscured-indeterminate manifest Form is co-arisen only.
> Desire-realm Form has no prior acquisition, but co-arisen and subsequent
> acquisition. Non-acquisition is unobscured-indeterminate; for past and
> future dharmas it is threefold.
### Bhāṣya-informed study translation

> Acquisition of obscured-indeterminate Form is co-arisen only. Desire-realm
> Form has no prior acquisition. Non-acquisition is unobscured-
> indeterminate; for past and future dharmas it is threefold, while for a
> present dharma it is present only on the provisional reading.
## 6. Philosophical Translation

> Non-acquisition does not inherit the class of what is not possessed. Prior acquisition is refused for desire-realm form. The present-only reading is provisional.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| nivṛta | obscured | completed as obscured-indeterminate form |
| agrajā | prior | excluded for desire-realm form |
| aprāpti | non-acquisition | the second half |
| akliṣṭa | unobscured | not the ethical axis |
| ajāta | not yet arisen | future |

## 8. Logical Determination

```text
obscured manifest form
    → co-arisen only
desire-realm form
    → co-arisen or subsequent
    prior out
non-acquisition
    → unobscured and indeterminate
present dharma
    → present non-acquisition, provisional
past or future
    → three times
```

## 9. Interpretive Note

**Translation note.** The commentary distinguishes the co-arisen-only rule for obscured Form from the absence of prior acquisition for desire-realm Form, where co-arisen and subsequent acquisition are admitted for manifest and nonmanifest Form. It reads ajāta as future. The claim that present-dharma non-acquisition is present only is provisional; the uncertainty is retained.

Realm classifications of non-acquisition, and ordinary-person status, are 2.40. The Buddha counterexample belongs there: absence of another lineage is not non-nobility.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_39 a vak:Karika ; vak:hasTopic vak:NonAcquisitionTyped .
```
