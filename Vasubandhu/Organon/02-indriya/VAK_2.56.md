# VAK_2.56 — Assigning Results to Causes

## 1. Sanskrit (Devanāgarī)

> विपाकफलमन्त्यस्य पूर्वस्याधिपतं फलम् ।
>
> सभागसर्वत्रगयोर्निष्यन्दः पौरुषं द्वयोः ॥ २.५६ ॥

## 2. Sanskrit (IAST)

> vipākaphalam antyasya pūrvasyādhipataṃ phalam /
>
> sabhāgasarvatragayor niṣyandaḥ pauruṣaṃ dvayoḥ // 2.56 //

## 3. Padaccheda

```text
vipākaphalam             → vipāka-phalam
antyasya                 → antyasya
pūrvasyādhipatam         → pūrvasya adhipatam
phalam                   → phalam
sabhāgasarvatragayoḥ     → sabhāga-sarvatragayoḥ
niṣyandaḥ                → niṣyandaḥ
pauruṣam                 → pauruṣam
dvayoḥ                   → dvayoḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| vipāka-phalam | nominative/accusative neuter singular compound | maturation-fruit |
| antyasya | genitive masculine singular | of the last [cause] |
| pūrvasya | genitive masculine singular | of the first [cause] |
| adhipatam phalam | nominative/accusative neuter singular phrase | fruit of predominance |
| sabhāga-sarvatragayoḥ | genitive masculine dual compound | of the homogeneous and pervasive causes |
| niṣyandaḥ | nominative masculine singular | homogeneous-outflow fruit |
| pauruṣam | nominative/accusative neuter singular | fruit of efficacious activity |
| dvayoḥ | genitive masculine dual | of the two [remaining causes] |

`Antya` and `pūrva` point back to the ordering of the six causes in VAK 2.49:
the last is maturation cause and the first is conditioning cause. `Dvayoḥ`
denotes the co-arisen and associated causes left after the other four have
been assigned their principal fruits.

## 4. Grammar

The first half contains two parallel genitive assignments:

```text
antyasya [hetoḥ]
    → vipāka-phalam

pūrvasya [hetoḥ]
    → adhipatam phalam
```

The second half completes the mapping:

```text
sabhāga-sarvatragayoḥ
    → niṣyandaḥ [phalam]

dvayoḥ [sahabhū-saṃprayuktakayoḥ]
    → pauruṣam [phalam]
```

The ellipses are resolved through the sixfold list and the Bhāṣya. The verse
assigns principal fruit-types; it does not grammatically assert that every
cause can have only the one fruit named here.

## 5. Translation

### Close syntactic construe

> The last [cause] has maturation as its fruit; the first has predominance as its fruit. The homogeneous and pervasive [causes] have homogeneous outflow; the two [remaining causes] have the fruit of efficacious activity.

### Bhāṣya-informed translation

> Maturation cause is principally distinguished by maturation-fruit, and conditioning cause by the fruit of predominance. Homogeneous and pervasive causes principally yield homogeneous outflow, while co-arisen and associated causes yield the fruit of operative efficacy. These are defining mappings rather than an exclusive one-to-one table: several causes can also possess a fruit of efficacious activity when their function produces a simultaneous or immediately subsequent result.

## 6. Philosophical Translation

> A cause is not fully comprehended until the form in which its efficacy becomes manifest is determined. Ground may appear in its result as delayed maturation, enabling predominance, homogeneous continuation, or present operative activity. The same event can stand within several such rational relations without those relations becoming interchangeable.

The four modes are:

```text
vipāka:
    delayed, individually appropriated maturation

adhipati:
    enabling, directing, assisting, or not obstructing

niṣyanda:
    continuation through relevant similarity

pauruṣa:
    manifestation of a dharma's operative efficacy
```

**Organon interpretation—not literal Bhāṣya doctrine.** The table assigns
principal fruit-types but does not make each cause exclusive to one result.
The Bhāṣya explicitly allows efficacy-fruit for other causes, while marking
the temporal qualification and preserving the alternative concerning
maturation cause.

## 7. Technical Vocabulary

| Sanskrit | Controlled rendering | Determination in this unit |
|---|---|---|
| vipāka-phala | maturation-fruit | principal fruit assigned here to maturation cause; its definition follows in VAK 2.57 |
| adhipati-phala | fruit of predominance | result enabled, supported, directed, or permitted by conditioning cause |
| niṣyanda-phala | homogeneous-outflow fruit | result similar to its cause in the relevant indexed respects |
| pauruṣa-phala | fruit of efficacious activity | result of a dharma's operative function, normally simultaneous or immediately subsequent |
| puruṣakāra | efficacious activity | figurative person-like activity attributed to a dharma's causal function |
| vipāka-hetu | maturation cause | last member of the six-cause list |
| kāraṇa-hetu | conditioning cause | first member of the six-cause list |
| adhipati | predominance | ranges from non-obstruction to positive direct or indirect assistance |

`Pauruṣa` should not be rendered simply as “human result.” The Bhāṣya marks
the expression as figurative: it concerns operative efficacy analogous to a
person's activity.

`Adhipati` likewise does not require forceful production. Non-obstruction is
already its minimal form; principal conditioning causes may add positive
assistance.

## 8. Logical Determination

The principal mapping table is:

| Cause | Principal fruit |
|---|---|
| `vipāka-hetu` | `vipāka-phala` |
| `kāraṇa-hetu` | `adhipati-phala` |
| `sabhāga-hetu` | `niṣyanda-phala` |
| `sarvatraga-hetu` | `niṣyanda-phala` |
| `sahabhū-hetu` | `pauruṣa-phala` |
| `saṃprayuktaka-hetu` | `pauruṣa-phala` |

This is a principal-role relation:

```text
PrincipalFruitType(causeType, fruitType)
```

It is not an exclusive function:

```text
PrincipalFruitType(c, f)
    ⇏ HasNoOtherFruitType(c)
```

The Bhāṣya's broader activity rule is:

```text
OperativeFunction(c, r)
AND (Simultaneous(r, c) OR ImmediatelyAfter(r, c))
    → PaurushaFruit(r, c)
```

Maturation cause is normally excluded because its defining fruit is delayed:

```text
VipakaHetu(c)
AND TemporallyDistant(r, c)
    → NOT ImmediatePaurushaFruit(r, c)
```

An alternative view admits a distant fruit of activity for maturation cause,
like crops as the fruit of a farmer's work. This is reported, not adopted as
the principal definition.

The definitions of maturation-fruit and the detailed similarity
distinctions are taken up in VAK 2.57, not in this source unit.

## 9. Interpretation

The Bhāṣya unit begins at 94.18 and ends at 95.08, after reporting the
alternative that maturation cause may have a distant fruit of efficacy.
At 95.09 the commentary begins defining the fruit-types; those definitions
belong with VAK 2.57. The present verse assigns principal fruits and then
qualifies, rather than closes, their distribution.

The useful study question is not merely “which fruit belongs in which row?”
It is: **what does the cause contribute in this relation?** Maturation
answers through delayed individualized ripening; predominance through
permission or contribution; homogeneous outflow through relevant similarity;
and efficacy through operative activity. A single Dharma may enter more than
one result-relation, so the table is an articulation of causal perspective,
not an inventory of fixed causal labels.

## 10. Review Status

First extended results pass complete. The verse's principal assignments,
the non-obstruction and positive-contribution distinction, and the reported
alternative concerning distant efficacy are retained at their source boundary.

Textual uncertainties remain marked. No independent manuscript or critical
edition collation has been performed.
