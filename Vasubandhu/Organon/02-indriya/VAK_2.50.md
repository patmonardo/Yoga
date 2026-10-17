# VAK_2.50 — Co-arisen Cause

## 1. Sanskrit (Devanāgarī)

```sanskrit
स्वतोऽन्ये कारणं हेतुः सहभूर्ये मिथःफलाः ।
भूतवच्चित्तचित्तानुवर्तिलक्षणलक्ष्यवत् ॥ २.५० ॥
```

## 2. Sanskrit (IAST)

```text
svato 'nye kāraṇaṃ hetuḥ sahabhūr ye mithaḥphalāḥ /
bhūtavac cittacittānuvartilakṣaṇalakṣyavat // 2.50 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| svato 'nye | ablative singular + masculine nominative plural adjective | other than itself |
| kāraṇaṃ hetuḥ | neuter nominative singular + masculine nominative singular | conditioning cause |
| sahabhūḥ | masculine nominative singular adjective | co-arisen cause |
| mithaḥ-phalāḥ | masculine nominative plural compound adjective | mutually one another's results |
| bhūtavat | indeclinable comparative adverb | as the Great Elements |
| citta-cittānuvarti | masculine nominative plural compound | consciousness and its followers |
| lakṣaṇa-lakṣya | neuter plural compound members | mark and marked |

## 4. Grammar

```text
% start S
S[CAUSE=co-arisen] -> MutualResult
S[EXAMPLE=elements|citta-followers|marks-marked] -> Mutual
S[QUALIFY=secondary-marks] -> Asymmetric[FROM=dharma, TO=secondary]
```

Co-arisen is mutual result, not simultaneity.  
Elements, consciousness and followers, marks and marked, both ways.  
Secondary marks are asymmetric.

## 5. Translation

### Literal Translation

> Other than itself is the conditioning cause. Co-arisen causes are those
> mutually resulting, as the Great Elements, consciousness and its
> followers, and mark and marked.
### Bhāṣya-informed study translation

> What is other than itself is the conditioning cause. Co-arisen causes
> are mutually resultant: the four Great Elements; consciousness and the
> dharmas that follow it, each of the other; and the marks and what is
> marked, each of the other.
## 6. Philosophical Translation

> Co-arisen is mutual result, not simultaneity. The examples run both ways. Secondary marks are the asymmetric qualification. Not every conditioned dharma of every other.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| sahabhū-hetu | co-arisen cause | mutual result |
| mithaḥphala | mutually resultant | the definition |
| cittānuvartin | follower of consciousness | not yet listed |
| anulakṣaṇa | secondary mark | the asymmetric case |

## 8. Logical Determination

```text
mutually resultant
    → co-arisen, both ways
four elements
    both ways
consciousness and followers
    both ways
marks and marked
    both ways
as appropriate
    ≠ every conditioned of every other
secondary marks
    dharma → them
    not them → dharma
```

## 9. Interpretive Note

**Translation note.** The Bhāṣya also qualifies the reciprocal account: even
without mutual result, a dharma is a co-arisen cause of its secondary marks,
though they are not causes of it. The examples do not make every conditioned
dharma a cause of every other.

Pāraṃparya in the opening prose is not the succession of causes from the nirvāṇa example. Reciprocal, from the examples. Not a collation.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_50 a vak:Karika ; vak:hasTopic vak:CoArisenCause .
vak:SecondaryMark vak:reciprocal false .
```
