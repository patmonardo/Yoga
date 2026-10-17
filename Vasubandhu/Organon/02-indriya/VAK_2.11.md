# VAK_2.11 — Wholesome, Unwholesome, Indeterminate

## 1. Sanskrit (Devanāgarī)

```sanskrit
मनोऽन्यवित्तिश्रद्धादीन्यष्टकं कुशलं द्विधा ।
दौर्मनस्यं मनोऽन्या च वित्तिस्त्रेधा अन्यदेकधा ॥ २.११ ॥
```

## 2. Sanskrit (IAST)

```text
mano 'nyavittiśraddhādīny aṣṭakaṃ kuśalaṃ dvidhā /
daurmanasyaṃ mano 'nyā ca vittis tredhā anyad ekadhā // 2.11 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| manaḥ | nominative | mind |
| anya-vitti | nominative | the other feelings |
| śraddhā-ādīni | nominative | those beginning with faith |
| aṣṭakam | nominative | the group of eight |
| kuśalam | nominative | wholesome |
| dvidhā | indeclinable | twofold |
| daurmanasyam | nominative | distress |
| anyā vittiḥ | nominative | the other feeling |
| tredhā | indeclinable | threefold |
| anyat | nominative | the remainder |
| ekadhā | indeclinable | onefold |

Vitti is feeling. Other excludes distress: pain, pleasure, gladness, neutral feeling.

## 4. Grammar

```text
% start S
S[ETHICAL=wholesome] -> Eight
S[ETHICAL=?e] -> Distress[ETHICAL=wholesome|unwholesome]
S[ETHICAL=?e] -> Mind | OtherFeeling
S[ETHICAL=indeterminate] -> Remainder
```

Ethical quality is a feature, not the faculty itself.

## 5. Translation

### Literal Translation

> Mind, the other feelings, and those beginning with faith. The eight are
> wholesome. Distress is twofold. Mind and the other feeling are threefold.
> The remainder is onefold.

### Bhāṣya-informed study translation

> Mind, the other feelings, and those beginning with faith: the eight are
> wholesome. Distress is twofold; mind and the other feelings are threefold;
> the remainder is onefold.

## 6. Philosophical Translation

> The eight are wholesome by nature. Distress always bears a quality. Mind and four feelings keep one function across three qualities. The remainder governs, and is indeterminate.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| kuśala | wholesome | the eight, only |
| akuśala | unwholesome | distress, and the five, in one way |
| avyākṛta | indeterminate | neither; not neutral feeling |
| anya-vitti | the other feelings | pain, pleasure, gladness, neutral feeling |
| aṣṭaka | the eight | five + three; not the eight with life |
| jīvitāṣṭama | life as eighth | seven of form and life |
| upekṣā | neutral feeling | tone; ethically threefold |

## 8. Logical Determination

```text
wholesome only
    = five + three
    = 8

distress
    = wholesome or unwholesome
    ≠ indeterminate

mind, pain, pleasure, gladness, neutral feeling
    = three qualities
    = 5

seven of form, life
    = indeterminate only
    = 8

8 + 1 + 5 + 8 = 22

neutral feeling
    ↛ indeterminate
wholesome
    ↛ without outflows
never maturation
    ↛ unwholesome
```

Threefold is the range of instances, not three qualities in one instance.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): The eight are wholesome by the very operation that
defines them. Distress always bears a quality and is never indeterminate.
Mind and the remaining feelings keep one function across the three
qualities. The rest govern, yet remain exclusively indeterminate.

The opening closes 2.10. Without that carry, the first words look like the wholesome eight. They are the ten.

Distress can be wholesome. The paragraph does not say when. No example is invented. Pleasant feeling is not therefore wholesome. Pleasure and gladness are in the threefold group.

The two eights are different. Faith and the three are wholesome. Eye through life are indeterminate. Shared wholesome status does not erase the outflow split of 2.09. The five can be either. The three are without outflows.

Interpretation: four axes, one faculty. The platform copes by not collapsing them. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_11
    a vak:Karika ;
    rdfs:label "VAK 2.11" ;
    vak:hasTopic vak:EthicalQuality ;
    vak:belongsTo vak:Indriyanirdesa .

vak:WholesomeEight vak:requires vak:Wholesome .
vak:DistressFaculty vak:excludes vak:Indeterminate .
vak:NeutralFeeling vak:notIdenticalWith vak:Indeterminate .

organon:FourAxes
    organon:notCollapsed true ;
    organon:notTheVerseEnglish true .
```
