# VAK_2.60 — Four Classes by Exclusion

## 1. Sanskrit (Devanāgarī)

```sanskrit
क्लिष्टा विपाकजाः शेषाः प्रथमाऱ्या यथाक्रमम् /
विपाकं सर्वगं हित्वा तौ सभागं च शेषजाः // २.६० //
```

## 2. Sanskrit (IAST)

```text
kliṣṭā vipākajāḥ śeṣāḥ prathamāryā yathākramam /
vipākaṃ sarvagaṃ hitvā tau sabhāgaṃ ca śeṣajāḥ // 2.60 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| kliṣṭāḥ | m. nom. pl. | Afflicted dharmas. |
| vipākajāḥ | m. nom. pl. | Maturation-born dharmas. |
| śeṣāḥ | m. nom. pl. | Remaining dharmas. |
| prathamāryāḥ | m. nom. pl. | First noble dharmas; the Bhāṣya specifies the first uncontaminated. |
| yathākramam | indeclinable | In the stated order; aligns classes with exclusions. |
| vipākam | m. acc. sg. | Maturation cause. |
| sarvagam | m. acc. sg. | Pervasive cause. |
| hitvā | absolutive | Having excluded. |
| tau | m. acc. dual | Those two causes, maturation and pervasive. |
| sabhāgam | m. acc. sg. | Homogeneous cause. |
| ca | conjunction | And. |
| śeṣajāḥ | m. nom. pl. | Arisen from the remaining causes. |

The first verse line has *prathamāryā yathākramam* in the local
[Sanskrit witness](../../Sources/kosabhasya.txt) and the older VAK
study. The former *prathamaṃ cānāsravam* reading in this Organon file
was not supported by either witness. The normalized tokens restore the
plural ending of *prathamāryāḥ* before *yathākramam*.

```text
# tokens: kliṣṭāḥ vipākajāḥ śeṣāḥ prathamāryāḥ yathākramam vipākam sarvagam hitvā tau sabhāgam ca śeṣajāḥ
```

## 4. Grammar

The first five tokens name four classes and mark their order. The
remaining seven express the ordered exclusions and arising from the
remaining causes. The Bhāṣya supplies the counts for each profile.

```nltk-fcfg
% start S
# tokens: kliṣṭāḥ vipākajāḥ śeṣāḥ prathamāryāḥ yathākramam vipākam sarvagam hitvā tau sabhāgam ca śeṣajāḥ
S[SEM=<(?classes & ?exclusions)>] -> CLASSES[SEM=?classes] EXCLUSIONS[SEM=?exclusions]
CLASSES[SEM=<(?aff & ?mat & ?rem & ?first)>] -> AFF[SEM=?aff] MAT[SEM=?mat] REM[SEM=?rem] FIRST[SEM=?first] ORDER
AFF[SEM=<Afflicted(afflicted)>] -> 'kliṣṭāḥ'
MAT[SEM=<MaturationBorn(maturation_born)>] -> 'vipākajāḥ'
REM[SEM=<Remaining(remaining)>] -> 'śeṣāḥ'
FIRST[SEM=<FirstNoble(first_noble)>] -> 'prathamāryāḥ'
ORDER -> 'yathākramam'
EXCLUSIONS[SEM=<(?ex1 & ?ex2 & ?two & ?homo & ?born)>] -> EX1[CASE=acc,SEM=?ex1] EX2[CASE=acc,SEM=?ex2] EXCLUDE TWO[CASE=acc,NUM=du,SEM=?two] HOMO[CASE=acc,SEM=?homo] AND BORN[CASE=nom,NUM=pl,SEM=?born]
EX1[CASE=acc,SEM=<ExcludesCause(afflicted,maturation)>] -> 'vipākam'
EX2[CASE=acc,SEM=<ExcludesCause(maturation_born,pervasive)>] -> 'sarvagam'
EXCLUDE -> 'hitvā'
TWO[CASE=acc,NUM=du,SEM=<(ExcludesCause(remaining,maturation) & ExcludesCause(remaining,pervasive) & ExcludesCause(first_noble,maturation) & ExcludesCause(first_noble,pervasive))>] -> 'tau'
HOMO[CASE=acc,SEM=<ExcludesCause(first_noble,homogeneous)>] -> 'sabhāgam'
AND -> 'ca'
BORN[CASE=nom,NUM=pl,SEM=<(BornFromRemainder(afflicted) & BornFromRemainder(maturation_born) & BornFromRemainder(remaining) & BornFromRemainder(first_noble))>] -> 'śeṣajāḥ'
```

```nltk-dep
'śeṣajāḥ' -> 'kliṣṭāḥ' | 'vipākajāḥ' | 'śeṣāḥ' | 'prathamāryāḥ' | 'yathākramam' | 'vipākam' | 'sarvagam' | 'hitvā' | 'tau' | 'sabhāgam' | 'ca'
```

**Feature chart checkpoints.** The class phrase spans [0, 5), the
exclusion phrase [5, 12), and the root [0, 12). The accusatives and
dual *tau* constrain the cause exclusions. The `SEM` preserves the
ordered pairings, including both exclusions repeated for the fourth
class; the numerical totals come from the Bhāṣya.

## 5. Translation

### Literal Translation

> Afflicted, maturation-born, remaining, and first noble [dharmas], in
> that order, arise from the remaining [causes] after excluding
> maturation, the pervasive, those two, and those two together with
> the homogeneous cause.

### Bhāṣya-informed study translation

> Afflicted, maturation-born, remaining, and first noble dharmas arise,
> in that order, from the causes left after excluding the maturation
> cause, the pervasive cause, both, and both plus the homogeneous cause.

## 6. Philosophical Translation

> The four classes have distinct causal profiles under the six-cause
> inventory. The first two each have five causes, but omit different
> causes; the remaining have four, and the first noble, understood here
> as the first uncontaminated dharmas, have three.

## 7. Technical Vocabulary

| Term | Rendering |
|---|---|
| kliṣṭa | Afflicted; maturation cause excluded. |
| vipākaja | Maturation-born; pervasive cause excluded. |
| śeṣa | Remaining; both of those causes excluded. |
| prathamārya | First noble; the Bhāṣya identifies the first uncontaminated dharmas. |
| yathākramam | In order; maps four classes to four exclusion patterns. |
| śeṣajāḥ | Arisen from the remaining causes. |

## 8. Logical Determination

**Kārikā, derived.** The root `SEM` records the four class predicates,
their ordered exclusion profiles, and arising from remaining causes.
The resulting counts of five, five, four, and three come from the
Bhāṣya. This verse does not yet give the separate rule for material and
mind-dissociated dharmas; that belongs to 2.61.

```nltk-sem
classes : Afflicted(afflicted) & MaturationBorn(maturation_born) & Remaining(remaining) & FirstNoble(first_noble)
exclusions : ExcludesCause(afflicted,maturation) & ExcludesCause(maturation_born,pervasive) & ExcludesCause(remaining,maturation) & ExcludesCause(remaining,pervasive) & ExcludesCause(first_noble,maturation) & ExcludesCause(first_noble,pervasive) & ExcludesCause(first_noble,homogeneous) & BornFromRemainder(afflicted) & BornFromRemainder(maturation_born) & BornFromRemainder(remaining) & BornFromRemainder(first_noble)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(Afflicted(afflicted) & MaturationBorn(maturation_born) & Remaining(remaining) & FirstNoble(first_noble) & ExcludesCause(afflicted,maturation) & ExcludesCause(maturation_born,pervasive) & ExcludesCause(remaining,maturation) & ExcludesCause(remaining,pervasive) & ExcludesCause(first_noble,maturation) & ExcludesCause(first_noble,pervasive) & ExcludesCause(first_noble,homogeneous) & BornFromRemainder(afflicted) & BornFromRemainder(maturation_born) & BornFromRemainder(remaining) & BornFromRemainder(first_noble))

# THEORY prose_counts
# EXPECT prose_counts T
CauseCount(afflicted,five) & CauseCount(maturation_born,five) & CauseCount(remaining,four) & CauseCount(first_noble,three)

# THEORY rejected_same_five_profile
# EXPECT rejected_same_five_profile F
ExcludesCause(afflicted,pervasive) & ExcludesCause(maturation_born,pervasive)

# THEORY rejected_first_keeps_homogeneous
# EXPECT rejected_first_keeps_homogeneous F
FirstNoble(first_noble) & -ExcludesCause(first_noble,homogeneous)
```

```nltk-valuation
afflicted => aff_class
maturation_born => mat_class
remaining => rem_class
first_noble => first_class
maturation => maturation_cause
pervasive => pervasive_cause
homogeneous => homogeneous_cause
five => five_count
four => four_count
three => three_count
Afflicted => {aff_class}
MaturationBorn => {mat_class}
Remaining => {rem_class}
FirstNoble => {first_class}
ExcludesCause => {(aff_class,maturation_cause),(mat_class,pervasive_cause),(rem_class,maturation_cause),(rem_class,pervasive_cause),(first_class,maturation_cause),(first_class,pervasive_cause),(first_class,homogeneous_cause)}
BornFromRemainder => {aff_class,mat_class,rem_class,first_class}
CauseCount => {(aff_class,five_count),(mat_class,five_count),(rem_class,four_count),(first_class,three_count)}
```

The finite valuation is a witness to the ordered exclusions and the
Bhāṣya’s counts. Removing any required exclusion makes the verse
formula false. The two five-cause classes remain distinct because
they exclude different causes.

## 9. Interpretive Note

**Translation note.** The local Sanskrit witnesses read
*prathamāryā yathākramam*. The Bhāṣya glosses this fourth class as
the first uncontaminated dharmas. It defines the remaining class as
indeterminate dharmas other than maturation-born and wholesome
dharmas other than the first uncontaminated moment.

The verse’s *yathākramam* makes the mapping between class and
exclusion decisive. Counting alone would conceal the difference
between the two five-cause profiles. The next verse takes up the
mind–mental factor case and the rule for other dharmas.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_60 a vak:Karika ; vak:hasTopic vak:FourClassesByExclusion .
vak:Afflicted vak:omitsCause vak:Maturation .
vak:FirstNoble vak:omitsCause vak:Homogeneous .
```
