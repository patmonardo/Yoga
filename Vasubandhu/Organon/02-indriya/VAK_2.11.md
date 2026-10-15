# VAK_2.11 — Wholesome, Unwholesome, Indeterminate

## 1. Sanskrit (Devanāgarī)

> मनोऽन्यवित्तिश्रद्धादीन्यष्टकं कुशलं द्विधा ।
>
> दौर्मनस्यं मनोऽन्या च वित्तिस्त्रेधा अन्यदेकधा ॥ २.११ ॥

## 2. Sanskrit (IAST)

> mano 'nyavittiśraddhādīny aṣṭakaṃ kuśalaṃ dvidhā /
>
> daurmanasyaṃ mano 'nyā ca vittis tredhā anyad ekadhā // 2.11 //

The first three members close the ten of 2.10. The ethical question begins at aṣṭakaṃ kuśalam.

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
mind + four feelings other than distress + five beginning with faith
    = the ten of 2.10

eight
    = five beginning with faith + the three
    → wholesome only

distress
    → wholesome or unwholesome

mind and the other feelings
    → wholesome, unwholesome, or indeterminate

remainder
    = seven of form, life as eighth
    → indeterminate only
```

Twofold here is not the twofold of maturation.

## 5. Translation

### Literal Translation

Mind, the other feelings, and those beginning with faith. The eight are wholesome. Distress is twofold. Mind and the other feeling are threefold. The remainder is onefold.

### Bhāṣya-informed study translation

How many are wholesome, how many unwholesome, how many indeterminate? The eight are wholesome: the five beginning with faith, and the three beginning with “I shall know.” Distress is twofold, wholesome and unwholesome. Mind and the other feelings are threefold: wholesome, unwholesome, and indeterminate. The remainder is onefold: those beginning with the eye, life as the eighth. These are exclusively indeterminate.

## 6. Philosophical Translation

Ethical quality is not faculty, and it is not maturation. The eight are wholesome by the operation that defines them. Distress always bears a quality. It is never indeterminate. Mind and four feelings keep one function across three qualities. The seven of form and life govern, and they are indeterminate. Neutral feeling is not that indeterminacy.

Organon rendering:

The platform has to hold the axes apart. Maturation, outflow, tone, and ethical quality are four questions. Wholesome is not without outflows. Neutral feeling is not indeterminate. The received English that folds them is not accepted. Not the verse English.

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

The opening closes 2.10. Without that carry, the first words look like the wholesome eight. They are the ten.

Distress can be wholesome. The paragraph does not say when. No example is invented. Pleasant feeling is not therefore wholesome. Pleasure and gladness are in the threefold group.

The two eights are different. Faith and the three are wholesome. Eye through life are indeterminate. Shared wholesome status does not erase the outflow split of 2.09. The five can be either. The three are without outflows.

Organon reading: four axes, one faculty. The platform copes by not collapsing them. Not the verse English.

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
