# VAK_4.12 — Ethical Variation Between Initiator and Continuator

## 1. Sanskrit — Devanāgarī

```sanskrit
प्रवर्तके शुभादौ हि स्यात्त्रिधाप्यनुवर्तकम् ।
तुल्यं मुनेः शुभं यावन्नोभयं तु विपाकजम् ॥
```

## 2. Sanskrit — IAST

```iast
pravartake śubhādau hi syāt tridhāpy anuvartakam |
tulyaṃ muneḥ śubhaṃ yāvan nobhayaṃ tu vipākajam ||
```

## 3. Source Caution

External source siglum: VAkK_4.12.

The second half is compressed. A cautious first-pass reading is:

```text
for the Sage,
the continuing consciousness corresponds
to the initiating consciousness
where wholesome action is concerned;

neither initiating nor continuing consciousness
is maturation-born.
```

The exact attachment of `tulyaṃ muneḥ śubhaṃ yāvat` remains for the Bhāṣya pass.

## 4. Padaccheda

| Form | Analysis | Working determination |
|---|---|---|
| `pravartake` | locative singular | when the initiator is present |
| `śubhādau` | `śubha-ādau` | wholesome and the other ethical classes |
| `syāt` | optative of √as | may be |
| `tridhā api` | adverb + particle | even threefold |
| `anuvartakam` | neuter nominative singular | continuing consciousness |
| `tulyam` | neuter nominative singular | corresponding; matching |
| `muneḥ` | genitive singular | of the Sage |
| `śubham` | neuter nominative/accusative singular | wholesome |
| `yāvat` | relative adverb | insofar as; as long as |
| `na ubhayam` | negation + collective dual sense | neither of the two |
| `vipākajam` | `vipāka-ja` | maturation-born |

## 5. Grammar

### `pravartake śubhādau`

The locative gives the circumstance:

> When the initiating consciousness is wholesome and so forth.

`Śubhādi` abbreviates the three ethical classes:

```text
wholesome
unwholesome
indeterminate
```

### `syāt tridhāpy anuvartakam`

> The continuing consciousness may be of any of the three kinds.

Thus the ethical quality of the continuator is not mechanically fixed by the quality of the initiator.

### `tulyaṃ muneḥ`

A provisional rendering is:

> In the Sage, it is corresponding.

The comparison is most likely between `pravartaka` and `anuvartaka`.

### `nobhayaṃ tu vipākajam`

Sandhi:

```iast
na ubhayaṃ tu vipāka-jam
```

> Neither of the two, however, is maturation-born.

The two are the initiating and continuing consciousnesses.

## 6. Literal Translation

> When the initiating consciousness is wholesome and so forth, the continuing consciousness may be threefold. In the Sage it is corresponding, insofar as it is wholesome. Neither of the two, however, is born from maturation.

## 7. Philosophical Translation

> The ethical quality of the consciousness that sustains an action need not simply repeat the quality of the consciousness that initiated it: the continuator may be wholesome, unwholesome, or indeterminate. In the case of the Sage, initiating and continuing consciousness correspond where wholesome action is concerned. Neither function is performed by a consciousness that is merely a product of karmic maturation.

## 8. Technical Vocabulary

| Sanskrit | Working translation | Determination |
|---|---|---|
| `śubhādi` | wholesome and so forth | the three ethical classes |
| `tridhā` | threefold | wholesome, unwholesome, indeterminate |
| `tulya` | corresponding | matching ethical quality |
| `muni` | Sage | exact scope deferred |
| `vipākaja` | maturation-born | produced as karmic maturation |

## 9. Doctrinal Determination

VAK_4.10 distinguished:

```text
pravartaka
    initiator

anuvartaka
    continuator
```

VAK_4.12 states that their ethical qualities need not coincide:

```text
pravartaka
    wholesome / unwholesome / indeterminate

anuvartaka
    independently:
    wholesome / unwholesome / indeterminate
```

An action-series can therefore change ethical character while unfolding.

## 10. Initiation Does Not Determine the Whole Series

The verse blocks the model:

```text
one initial intention
    permanently fixes
    every subsequent moment
```

Instead:

```text
initiating consciousness
    begins the action

continuing consciousness
    may arise with a different ethical quality
```

The action-series must therefore be evaluated moment by moment.

## 11. The Sage Restriction

The phrase `tulyaṃ muneḥ` introduces a special case:

```text
ordinary continuum:
    initiator and continuator may differ

continuum of the Sage:
    wholesome initiator and continuator correspond
```

The stronger significance of this correspondence remains for the Bhāṣya.

## 12. Exclusion of Maturation-Born Consciousness

A `vipākaja` consciousness is a result of prior karma, whereas `pravartaka` and `anuvartaka` function within the present production of action:

```text
vipāka
    receiving the result of prior karma

samutthāna
    generating or sustaining present karma
```

Neither action-function is therefore merely maturation-born.

## 13. Logical Determination

The verse introduces variation within continuity:

```text
one action-series
    does not imply
one unchanging ethical determination
```

Continuity is causally ordered succession, not the numerical persistence of one unchanged consciousness.

## 14. Light Organon Interpretation

```text
initiation
    posits a determinate course

continuation
    preserves the course

but preservation
    does not require complete identity
    of ethical determination
```

The Sage is a special case of correspondence rather than ordinary divergence.

## 15. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_12
    a vak:Karika ;
    rdfs:label "VAK 4.12" ;
    vak:continues vak:VAK_4_11 ;
    vak:hasTopic vak:EthicalVariationWithinAction ;
    vak:hasTopic vak:SageCorrespondence ;
    vak:hasTopic vak:ExclusionOfMaturationBornConsciousness .

vak:Anuvartaka
    vak:hasPossibleEthicalQuality vak:Wholesome ;
    vak:hasPossibleEthicalQuality vak:Unwholesome ;
    vak:hasPossibleEthicalQuality vak:Indeterminate .

vak:Pravartaka
    vak:isDistinctFrom vak:Anuvartaka ;
    vak:excludesOrigin vak:MaturationBorn .

vak:Anuvartaka
    vak:excludesOrigin vak:MaturationBorn .
```

## 16. Verse Summary

```text
VAK_4.12

The continuing consciousness
need not possess the same ethical quality
as the initiating consciousness.

It may be:
    wholesome
    unwholesome
    indeterminate

In the Sage,
the two correspond
where wholesome action is concerned.

Neither initiating
nor continuing consciousness
is merely maturation-born.
```

## 17. Commit Note

Committed VAK_4.12.

Established:
- ethical variation between initiator and continuator;
- a special correspondence in the Sage;
- exclusion of maturation-born consciousness from both functions;
- the second half remains provisional pending the Bhāṣya pass.
