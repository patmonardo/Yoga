# VAK_4.100 — Who Divides the Saṅgha and When

## 1. Sanskrit (Devanāgarī)

```sanskrit
भिक्षुर्दृक्चरितो वृत्ती भिनत्त्यन्यत्र बालिशान् ।
शास्तृमार्गान्तरक्षान्तौ भिन्नो न विवसत्यसौ ॥ ४.१०० ॥
```

## 2. Sanskrit (IAST)

```iast
bhikṣur dṛkcarito vṛttī bhinatty anyatra bāliśān /
śāstṛmārgāntarakṣāntau bhinno na vivasaty asau // 4.100 //
```

## 3. Lexical Analysis

```text
bhikṣuḥ | dṛk-caritaḥ | vṛttī | bhinatti | anyatra | bāliśān |
śāstṛ-antara-mārga-antara-kṣāntau | bhinnaḥ | na | vivasati | asau
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| `bhikṣuḥ` | nominative masculine singular | the monk who effects the division |
| `dṛk-caritaḥ` | nominative masculine singular compound | governed in conduct by view |
| `vṛttī` | nominative masculine singular, `-in` stem | characterized by conduct; the exact force is clarified by the Bhāṣya |
| `bhinatti` | third-person singular present of `√bhid` | divides |
| `anyatra` | indeclinable adverb | elsewhere than where the Blessed One is present |
| `bāliśān` | accusative masculine plural | the immature persons who are divided |
| `śāstṛ-antara-mārga-antara-kṣāntau` | locative singular compound | upon acceptance of another teacher and another path |
| `bhinnaḥ` | nominative masculine singular past passive participle | divided; said of the Saṅgha |
| `na` | negative particle | negates the duration expressed by `vivasati` |
| `vivasati` | third-person singular present of `vi-√vas` | remains through the night |
| `asau` | nominative masculine singular demonstrative | that divided Saṅgha |

The witness reading around `vṛttī` is damaged; the Bhāṣya's contrast with
broken conduct informs, but does not remove, that uncertainty.

## 4. Grammar

The first clause identifies the agent and recipients:

```text
bhikṣuḥ dṛk-caritaḥ vṛttī
    anyatra bāliśān bhinatti
```

The Bhāṣya specifies that the agent is a monk governed by view rather than
craving, whose conduct is not broken. It explains `anyatra` as away from
the Blessed One's presence and `bāliśān` as ordinary persons, while
excluding noble persons; a reported opinion also excludes ordinary persons
who have attained `kṣānti`.

The second clause gives the condition for completed division:

```text
śāstṛ-antara-mārga-antara-kṣāntau
    [saṃghaḥ] bhinnaḥ
```

The Bhāṣya explains the compound through acceptance of both a teacher other
than the Tathāgata and a path other than the one he taught. The final clause
states that this division does not last through the night; the Saṅgha is
reunited before the night has elapsed.

## 5. Translation

### Scientific English Rendering

> A monk governed by view and established in conduct divides the immature
> elsewhere. Upon acceptance of another teacher and another path, the Saṅgha
> is divided; that division does not last through the night.

### Bhāṣya-informed study translation

> A monk governed by view and established in conduct divides the immature
> elsewhere. Upon acceptance of another teacher and another path, the Saṅgha
> is divided; that division does not last through the night. The Bhāṣya
> specifies that the monk is not governed by craving or of broken conduct,
> that the division occurs away from the Blessed One's presence, and that
> reunion is necessary before the night has passed.

The witness's `bhikṣurdu kvacarito vṛttī` at `[261|09]` is damaged around
`dṛkcarito`; the verse form supplies the normalized anchor above. The
opening prose question's `bhanatti` is normalized to `bhinatti`.

## 6. Philosophical Translation

> A collective division is completed not by the divider's standing or
> utterance alone, but when susceptible members accept both a different
> teacher and a different path. This recognized alternative establishes a
> temporary non-concord in the Saṅgha, which is necessarily repaired before
> the night has passed.

## 7. Technical Vocabulary

- **`Dṛk-carita` / `dṛṣṭi-carita`** — governed in conduct by view; the
  Bhāṣya contrasts this with conduct governed by craving
  (`tṛṣṇā-carita`).
- **`Vṛttī` / `bhinnavṛtta`** — the kārikā's witness is uncertain. The
  Bhāṣya contrasts proper standing with broken conduct and explains that
  the latter's words would not be accepted (`anādeyavākya`).
- **`Bāliśa` / `pṛthagjana`** — the immature, glossed as ordinary persons.
  Noble persons are excluded; a reported view also excludes those who
  have attained `kṣānti`.
- **`Kṣānti`** — in `śāstṛmārgāntarakṣāntau`, acceptance of another
  teacher and another path. Do not conflate this compound with the
  Bhāṣya's separate reference to recipients who have attained `kṣānti`.
- **`Na vivasati`** — the division does not last through the night; the
  Bhāṣya says the Saṅgha is necessarily reunited before it passes.

## 8. Logical Determination

```text
qualified monk
    + action away from the Blessed One's presence
    + susceptible recipients
    + acceptance of another teacher
    + acceptance of another path
    → Saṅgha divided
    → Saṅgha reunited before that night passes
```

The acceptance of both alternatives is the stated completion condition.
This unit does not itself name *cetanā* or restate the action taxonomy.

## 9. Interpretive Note

The source unit runs from the question at `[261|07–08]` through the
reunion statement at `[261|23]`; it stops before the next statement,
`cakrabhedaḥ`, at `[261|24]`. Its focus is the agent, recipients, and
recognition conditions of this form of Saṅgha division. The damaged
`vṛttī` reading and the normalization of `bhanatti` to `bhinatti` are
marked in the paired study. The discussion distinguishes this collective
result from 4.99's culpable verbal action without inserting *cetanā* where
the passage does not name it.

## 10. OWL++ Seed

```text
Class: Monk
Class: ViewGovernedConduct
Class: BrokenConduct
Class: Saṅgha
Class: SaṅghaDivision
Class: SusceptibleRecipient
Class: Teacher
Class: Path

ObjectProperty: divides
  Domain: Monk
  Range: Saṅgha
ObjectProperty: acceptsTeacher
  Domain: SusceptibleRecipient
  Range: Teacher
ObjectProperty: acceptsPath
  Domain: SusceptibleRecipient
  Range: Path
ObjectProperty: occursAwayFrom
  Domain: SaṅghaDivision
  Range: BlessedOnePresence
ObjectProperty: reunitedBefore
  Domain: SaṅghaDivision
  Range: NightElapsed

Rule: CompletedSaṅghaDivision
  agent = Monk
  conduct = ViewGovernedConduct
  conduct != BrokenConduct
  location = AwayFromBlessedOnePresence
  recipients = SusceptibleRecipient
  acceptsTeacher = TeacherOtherThanTathāgata
  acceptsPath = PathOtherThanTathāgataTeaching
  result = SaṅghaDivision
  reunion = BeforeNightElapsed
```
