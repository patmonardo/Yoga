# VAK_2.40 — Ordinary Status

## 1. Sanskrit (Devanāgarī)

> कामाद्याप्तामलानां च मार्गस्याप्राप्तिरिष्यते ।
>
> पृथग्जनत्वं तत्प्राप्तिभूसंचाराद्विहीयते ॥ २.४० ॥

## 2. Sanskrit (IAST)

> kāmādyāptāmalānāṃ ca mārgasyāprāptir iṣyate /
>
> pṛthagjanatvaṃ tatprāptibhūsaṃcārād vihīyate // 2.40 //

## 3. Lexical Analysis

| Pada | Force |
|---|---|
| kāma-ādi-āpta-amalānām | of realm-included and uncontaminated dharmas |
| mārgasya aprāptiḥ | non-acquisition of the path |
| pṛthagjanatvam | ordinary-person status |
| tat-prāpti | acquisition of that |
| bhū-saṃcāra | transition of ground |
| vihīyate | is relinquished |

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

Of those included in the desire realm and the rest, and of the uncontaminated, also. Non-acquisition of the path is held to be ordinary-person status. It is relinquished by acquisition of that, or by transition of ground.

### Bhāṣya-informed study translation

> Non-acquisition of realm-included and uncontaminated dharmas is also threefold by realm, and is never itself uncontaminated. Non-acquisition of the path is held to be ordinary-person status. It is relinquished by acquisition of that path, or by transition of ground. The critical account takes an ordinary continuum as one in which noble dharmas have not yet arisen. Not settled.

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

The opening completes the threefold rule of 2.39. The status is the verse. The genetic account and the regress are the commentary. Voices stay apart.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_40 a vak:Karika ; vak:hasTopic vak:OrdinaryStatus .
vak:OrdinaryStatus vak:settled false .
```
