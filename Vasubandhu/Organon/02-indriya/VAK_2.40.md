# VAK_2.40 — Ordinary Status

## 1. Sanskrit (Devanāgarī)

```sanskrit
कामाद्याप्तामलानां च मार्गस्याप्राप्तिरिष्यते ।
पृथग्जनत्वं तत्प्राप्तिभूसंचाराद्विहीयते ॥ २.४० ॥
```

## 2. Sanskrit (IAST)

```text
kāmādyāptāmalānāṃ ca mārgasyāprāptir iṣyate /
pṛthagjanatvaṃ tatprāptibhūsaṃcārād vihīyate // 2.40 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| kāma-ādi-āpta-amalānām | gen. pl. m.; compound | of realm-included and uncontaminated dharmas |
| mārgasya aprāptiḥ | gen. sg. m. + nom. sg. f. | non-acquisition of the path |
| pṛthagjanatvam | nom. sg. n.; abstract noun | ordinary-person status |
| tat-prāpti | nom. sg. f. + genitive demonstrative | acquisition of that |
| bhū-saṃcāra | compound noun, abl. sg. m. | transition of ground |
| vihīyate | 3 sg. passive present indicative | is relinquished |

Ordinary person is the path-status. Not an insult. Not a nature.
## 4. Grammar

```text
% start S
S[NONACQ=realm-included|uncontaminated] -> NonAcquisition[REALM=desire|form|formless]
S[NONACQ=path] -> OrdinaryStatus
S[RELINQUISH=true] -> AcquisitionOfPath | GroundTransition
```

Non-acquisition is never itself uncontaminated.  
Ordinary-person status is non-acquisition of the path, on the Vaibhāṣika account.  
Relinquished by acquisition of that path or by ground-transition.

## 5. Translation

### Literal Translation

> Non-acquisition of dharmas included in the desire realm and the rest, and
> of the uncontaminated, is likewise classified threefold. Non-acquisition
> of the path is ordinary-person status; it is relinquished by acquiring the
> path or by transition of ground.
### Bhāṣya-informed study translation

> Non-acquisition of Desire Realm and other realm-included dharmas, and of
> the uncontaminated, is likewise threefold. Non-acquisition of the path is
> ordinary-person status, relinquished by acquiring the path or by
> transition of ground.
## 6. Philosophical Translation

> Non-acquisition is never uncontaminated. Ordinary status is non-acquisition of the path, or noble dharmas not yet arisen. Relinquished by acquisition or ground-transition. The ontological cost is not settled.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| amala | uncontaminated | the dharma; not the non-acquisition |
| pṛthagjanatva | ordinary-person status | path-status |
| bhūsaṃcāra | ground-transition | the second ground of relinquishment |
| prāpti-prāpti | acquisition of acquisition | the regress |

## 8. Logical Determination

```text
non-acquisition
    realm ∈ {desire, form, formless}
    never uncontaminated
ordinary, Vaibhāṣika
    = real non-acquisition of the noble path
ordinary, critical
    = noble dharmas not yet arisen
relinquished
    by acquisition of that path
    or ground-transition
regress
    mutual possession blocks the line
    multiplies the entities
    not settled
```

## 9. Interpretive Note

**Translation note.** The commentary completes the threefold rule for the non-acquisition in 2.39, distinguishes path-status from an inherent nature, and supplies a genetic account and regress concerning ordinary-person status. It also addresses a Buddha counterexample: absence of another lineage is not non-nobility.

The opening completes the threefold rule of 2.39. The status is the verse. The genetic account and the regress are the commentary. Voices stay apart.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_40 a vak:Karika ; vak:hasTopic vak:OrdinaryStatus .
vak:OrdinaryStatus vak:settled false .
```
