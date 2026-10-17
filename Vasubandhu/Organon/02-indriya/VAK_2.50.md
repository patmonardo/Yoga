# VAK_2.50 — Co-arisen Cause

## 1. Sanskrit (Devanāgarī)

> स्वतोऽन्ये कारणं हेतुः सहभूर्ये मिथःफलाः ।
>
> भूतवच्चित्तचित्तानुवर्तिलक्षणलक्ष्यवत् ॥ २.५० ॥

## 2. Sanskrit (IAST)

> svato 'nye kāraṇaṃ hetuḥ sahabhūr ye mithaḥphalāḥ /
>
> bhūtavac cittacittānuvartilakṣaṇalakṣyavat // 2.50 //

## 3. Lexical Analysis

| Pada | Force |
|---|---|
| svato 'nye | other than itself |
| kāraṇaṃ hetuḥ | conditioning cause |
| sahabhūḥ | co-arisen cause |
| mithaḥ-phalāḥ | mutually one another's results |
| bhūtavat | as the great elements |
| citta-anuvarti | consciousness and its followers |
| lakṣaṇa-lakṣya | mark and marked |

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

Other than itself, the conditioning cause. Co-arisen: those that are mutually results. As the great elements, as consciousness and its followers, as the marks and the marked.

### Bhāṣya-informed study translation

> The conditioning cause is what is other than itself. Co-arisen causes are those that are mutually results: the four great elements, of one another; consciousness, of the dharmas that follow it, and they of it; the marks, of the marked, and it of them. Even without mutual result, a dharma is a co-arisen cause of its secondary marks, though they are not of it.

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

Pāraṃparya in the opening prose is not the succession of causes from the nirvāṇa example. Reciprocal, from the examples. Not a collation.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_50 a vak:Karika ; vak:hasTopic vak:CoArisenCause .
vak:SecondaryMark vak:reciprocal false .
```
