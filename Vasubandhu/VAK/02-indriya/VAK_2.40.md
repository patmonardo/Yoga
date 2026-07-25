# VAK_2.40 — Aprāpti of the Path and Pṛthagjanatva

## 1. Sanskrit — Devanāgarī

```text
कामाद्याप्तामलानां च मार्गस्याप्राप्तिरिष्यते ।
पृथग्जनत्वं तत्प्राप्तिभूसंचाराद्विहीयते ॥ VAkK_2.40 ॥
```

## 2. Sanskrit — IAST

```text
kāmādyāptāmalānāṃ ca mārgasyāprāptir iṣyate /
pṛthagjanatvaṃ tatprāptibhūsaṃcārād vihīyate // VAkK_2.40 //
```

Source form:

```text
kāmādyāptāmalānāṃ ca mārgasyāprāptiriṣyate /
pṛthagjanatvam tatprāptibhūsaṃcārād vihīyate // VAkK_2.40 //
```

## 3. Padaccheda and Grammar

| Sanskrit | Padaccheda | Grammar | Working Sense |
|---|---|---|---|
| kāma-ādi-āpta-amalānām | kāmādyāptāmalānām | genitive plural compound | of those acquired in kāma and so forth, and of the stainless |
| ca | ca | indeclinable | and |
| mārgasya | mārgasya | genitive singular | of the path |
| aprāptiḥ | aprāptiḥ | feminine nominative singular | non-acquisition / non-connection |
| iṣyate | iṣyate | passive, 3rd singular | is accepted / is held |
| pṛthagjanatvam | pṛthagjanatvam | neuter nominative singular | ordinary-personhood / worldling status |
| tat-prāpti-bhū-saṃcārāt | tatprāptibhūsaṃcārāt | ablative compound | from movement to the ground of that acquisition; segmentation to verify |
| vihīyate | vihīyate | passive, 3rd singular | is given up / left behind |

## 4. Literal Translation

```text
Non-acquisition of the path is accepted for those acquired in the desire realm and so forth, and for the stainless.
Pṛthagjanatva is left behind through transition to the ground of that acquisition.
```

## 5. Philosophical Translation

```text
Ordinary-personhood is defined by a structural non-acquisition of the path.
When the ground of path-acquisition is reached, that ordinary status is left behind.
```

## 6. Technical Vocabulary

| Sanskrit | Working Translation | Note |
|---|---|---|
| kāmādi | kāma and so forth | Realm series beginning with desire realm |
| āpta | acquired / attained | Connected by prāpti |
| amala | stainless | Pure / undefiled status |
| mārga | path | Path-structure or liberating route |
| aprāpti | non-acquisition | Structural non-relation |
| pṛthagjanatva | ordinary-personhood | Status of one not yet entered into noble path acquisition |
| bhū | ground / level | Stage or basis |
| saṃcāra | transition / movement | Movement into another ground/status |
| vihīyate | is left behind | Status ceases to apply |

## 7. Logical Determination

VAK_2.40 connects aprāpti with path-status.

```text
pṛthagjanatva
    = ordinary-person status
    = defined by non-acquisition of the path
```

Logical protocol:

```text
if path is not acquired,
then pṛthagjanatva applies.

if the ground of path-acquisition is reached,
then pṛthagjanatva no longer applies.
```

This is structural-status logic, not merely ethical description.

## 8. Relation to Indriya and Citta-Caitta

Indriya and caitta profiles define the operative and appearing field.
Prāpti/aprāpti now define whether the path is structurally connected to the series.

```text
Citta-Caitta may be configured in many ways,
but path-status depends on structural acquisition.
```

Thus the system needs viprayukta operators to explain transformation of status.

## 9. Organon Interpretation

Organon reading:

```text
PathAcquisitionStatus:
    pathAcquired = true | false
    ordinaryPersonStatus = applies | leftBehind
```

Engineering implication:

```text
Learning has threshold states.
A status changes when a structural relation is established.
```

The Agent requires not merely feature-values, but transition rules for status.

## 10. OWL++ Seed

```turtle
@prefix vak: <http://organon.dev/abhidharma/vak/> .

vak:Puthagjanatva a vak:ViprayuktaSamskara ;
    vak:definedBy vak:PathAprapti .

vak:PathAprapti a vak:ApraptiRelation ;
    vak:hasObject vak:Marga .

vak:PathPraptiTransition a rdfs:Class ;
    vak:removesStatus vak:Puthagjanatva .
```

## 11. Commit History

```text
VAK_2.40 opened.
Method: kārikā-first speculative seed.
Theme: aprāpti of the path and pṛthagjanatva as structural status.
Technical compounds marked for later Bhāṣya review.
Organon mapping: threshold transition from ordinary status through path acquisition.
Zero-padded file naming maintained: VAK_2.40.
```
