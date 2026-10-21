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
| mano-'nya-vitti-śraddhādīni | nominative plural neuter coordinated compound | Mind, other feelings, and those beginning with faith; completes 2.10's ten |
| aṣṭakam | nominative singular neuter collective noun | the group of eight, now under the ethical question |
| kuśalam | nominative singular neuter adjective | wholesome; predicates the eight |
| dvidhā | indeclinable | twofold |
| daurmanasyam | nominative singular neuter noun | distress, subject of twofold |
| manaḥ | nominative singular neuter noun | Mind, subject with other feeling |
| anyā | nominative singular feminine adjective | other; excludes distress |
| ca | coordinating particle | and |
| vittiḥ | nominative singular feminine noun, collective in force | feeling; the four other feeling types |
| tredhā | indeclinable | threefold |
| anyat | nominative singular neuter pronoun | the remainder, seven Form Faculties and life |
| ekadhā | indeclinable | onefold |

Vitti is feeling. Other excludes distress: pain, pleasure, gladness, neutral feeling.

**Grammar tokens.** Sandhi is opened, separating the initial Mind member from the rest of the coordinated compound. It completes the preceding verse's ten, rather than supplying the members of the wholesome eight. The boundary remains in the parse.

```text
# tokens: manaḥ anya-vitti-śraddhādīni aṣṭakam kuśalam dvidhā daurmanasyam manaḥ anyā ca vittiḥ tredhā anyat ekadhā
```

## 4. Grammar

The first compound is a carried enumeration. The Bhāṣya begins its new ethical question only at the eight. The singular collective eight agrees with wholesome; twofold applies to distress; Mind and the collectively singular other feeling take the threefold determination. The remainder is onefold. The adverbs themselves do not name the ethical alternatives; the Bhāṣya supplies those alternatives.

```nltk-fcfg
% start S
# tokens: manaḥ anya-vitti-śraddhādīni aṣṭakam kuśalam dvidhā daurmanasyam manaḥ anyā ca vittiḥ tredhā anyat ekadhā
S[SEM=<(?carry & ?eight & ?distress & ?five & ?rest)>] -> CARRY[SEM=?carry] EIGHTCLAUSE[SEM=?eight] DISTRESSCLAUSE[SEM=?distress] FIVECLAUSE[SEM=?five] RESTCLAUSE[SEM=?rest]
CARRY[SEM=<CompletesPreviousTen>] -> 'manaḥ' 'anya-vitti-śraddhādīni'
EIGHTCLAUSE[SEM=<GroupCount(wholesome_eight,eight) & WholesomeOnly(wholesome_eight)>] -> EIGHT WHOLESOME
EIGHT -> 'aṣṭakam'
WHOLESOME -> 'kuśalam'
DISTRESSCLAUSE[SEM=<EthicalOptions(distress_f,two)>] -> TWOFOLD DISTRESS
TWOFOLD -> 'dvidhā'
DISTRESS -> 'daurmanasyam'
FIVECLAUSE[SEM=<EthicalOptions(mind_f,three) & EthicalOptions(other_feelings,three) & OtherFeelingExcludesDistress>] -> MIND OTHER AND FEELING THREEFOLD
MIND -> 'manaḥ'
OTHER -> 'anyā'
AND -> 'ca'
FEELING -> 'vittiḥ'
THREEFOLD -> 'tredhā'
RESTCLAUSE[SEM=<EthicalOptions(remainder,one)>] -> REST ONEFOLD
REST -> 'anyat'
ONEFOLD -> 'ekadhā'
```

```nltk-dep
'aṣṭakam' -> 'kuśalam'
'daurmanasyam' -> 'dvidhā'
'manaḥ' -> 'anya-vitti-śraddhādīni' | 'anyā' | 'ca' | 'vittiḥ' | 'tredhā'
'anyat' -> 'ekadhā'
```

The dependency block records vocabulary coverage only. The opening compound closes the preceding ten; its membership is checked in a separate prose theory, not read as the wholesome eight.

| Span | Constituent | Result |
|---|---|---|
| [0, 2) | `CARRY` | completion of 2.10's ten |
| [2, 4) | `EIGHTCLAUSE` | wholesome eight |
| [4, 6) | `DISTRESSCLAUSE` | two ethical possibilities |
| [6, 11) | `FIVECLAUSE` | Mind and other feelings, each threefold |
| [11, 13) | `RESTCLAUSE` | one ethical possibility |
| [0, 13) | `S` | carried enumeration followed by the new classification |

## 5. Translation

### Literal Translation

> Mind, the other feelings, and those beginning with faith. The eight are wholesome. Distress is twofold. Mind and the other feeling are threefold. The remainder is onefold.

### Bhāṣya-informed study translation

> [The ten are] Mind, the other feelings, and those beginning with faith. The eight are exclusively wholesome. Distress is wholesome or unwholesome; Mind and the other feelings can be wholesome, unwholesome, or indeterminate. The remainder is exclusively indeterminate.

## 6. Philosophical Translation

> Feeling-tone and ethical quality are distinct. Distress can be wholesome; neutral feeling can be wholesome, unwholesome, or indeterminate. Governing efficacy does not by itself establish wholesomeness.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| kuśala | wholesome | the eight exclusively; also possible for distress, Mind, and the other feelings |
| akuśala | unwholesome | distress, and the five, in one way |
| avyākṛta | indeterminate | neither; not neutral feeling |
| anya-vitti | the other feelings | pain, pleasure, gladness, neutral feeling |
| aṣṭaka | the eight | five + three; not the eight with life |
| jīvitāṣṭama | life as eighth | seven of form and life |
| upekṣā | neutral feeling | tone; ethically threefold |

## 8. Logical Determination

**Kārikā, derived.** The opening fragment completes the preceding enumeration, not the wholesome eight. The verse gives one explicit quality and three counts of alternatives. The prose fixes the contents of each range; possibilities across instances are not simultaneous qualities of an instance. CompletesPreviousTen marks the verse boundary, while the Bhāṣya resolves the carried and new groups in separate FOL theories.

```nltk-sem
wholesome_group : WholesomeOnly(wholesome_eight)
ethical_range : EthicalOptions(distress_f,two)
previous_enumeration : CompletesPreviousTen
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(CompletesPreviousTen & GroupCount(wholesome_eight,eight) & WholesomeOnly(wholesome_eight) & EthicalOptions(distress_f,two) & EthicalOptions(mind_f,three) & EthicalOptions(other_feelings,three) & OtherFeelingExcludesDistress & EthicalOptions(remainder,one))

# THEORY prose_carried_ten
# EXPECT prose_carried_ten T
all x.(PreviousTenType(x) <-> (ThreefoldType(x) | FaithGroup(x)))
all x.(ThreefoldType(x) <-> ((x = mind_f) | OtherFeelingType(x)))
all x.(OtherFeelingType(x) -> -(x = distress_f))

# THEORY prose_ethical_ranges
# EXPECT prose_ethical_ranges T
all x.(WholesomeEightType(x) <-> (FaithGroup(x) | RealizationFaculty(x)))
all x.(WholesomeEightType(x) -> (CanBeWholesome(x) & -CanBeUnwholesome(x) & -CanBeIndeterminate(x)))
(CanBeWholesome(distress_f) & CanBeUnwholesome(distress_f) & -CanBeIndeterminate(distress_f))
all x.(ThreefoldType(x) -> (CanBeWholesome(x) & CanBeUnwholesome(x) & CanBeIndeterminate(x)))
all x.(RemainderType(x) -> (CanBeIndeterminate(x) & -CanBeWholesome(x) & -CanBeUnwholesome(x)))

# THEORY rejected_distress_only_unwholesome
# EXPECT rejected_distress_only_unwholesome F
-CanBeWholesome(distress_f) & CanBeUnwholesome(distress_f)

# THEORY rejected_neutral_feeling_only_indeterminate
# EXPECT rejected_neutral_feeling_only_indeterminate F
CanBeIndeterminate(neutral_f) & -CanBeWholesome(neutral_f) & -CanBeUnwholesome(neutral_f)

# THEORY rejected_carried_ten_are_wholesome_eight
# EXPECT rejected_carried_ten_are_wholesome_eight F
all x.(PreviousTenType(x) <-> WholesomeEightType(x))
```

```nltk-valuation
wholesome_eight => faith_and_realization_group
distress_f => distress
mind_f => mind
neutral_f => neutral
other_feelings => other_four_feelings
remainder => form_and_life_group
eight => count_eight
two => count_two
three => count_three
one => count_one
CompletesPreviousTen => True
OtherFeelingExcludesDistress => True
GroupCount => {(faith_and_realization_group,count_eight)}
WholesomeOnly => {faith_and_realization_group}
EthicalOptions => {(distress,count_two),(mind,count_three),(other_four_feelings,count_three),(form_and_life_group,count_one)}
WholesomeEightType => {faith,vigor,mindfulness,concentration,comprehension,shall_know,knowledge,one_who_has_known}
ThreefoldType => {mind,pain,pleasure,gladness,neutral}
OtherFeelingType => {pain,pleasure,gladness,neutral}
RemainderType => {eye,ear,nose,tongue,body,female,male,life}
PreviousTenType => {mind,pain,pleasure,gladness,neutral,faith,vigor,mindfulness,concentration,comprehension}
FaithGroup => {faith,vigor,mindfulness,concentration,comprehension}
RealizationFaculty => {shall_know,knowledge,one_who_has_known}
CanBeWholesome => {faith,vigor,mindfulness,concentration,comprehension,shall_know,knowledge,one_who_has_known,distress,mind,pain,pleasure,gladness,neutral}
CanBeUnwholesome => {distress,mind,pain,pleasure,gladness,neutral}
CanBeIndeterminate => {mind,pain,pleasure,gladness,neutral,eye,ear,nose,tongue,body,female,male,life}
```

The four disjoint groups contain 8 + 1 + 5 + 8 = 22 Faculty-types. The carried ten contain Mind, the four other feelings, and the five beginning with faith. The wholesome eight combine that faith-group with the three realization Faculties. They share five members, but they are different enumerations. The model records permitted ethical ranges, not conditions sufficient to make a particular occurrence wholesome.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the verse translation): The eight are wholesome by the very operation that defines them. Distress always bears a quality and is never indeterminate. Mind and the remaining feelings keep one function across the three qualities. The rest govern, yet remain exclusively indeterminate.

The opening closes 2.10. Without that carry, the first words look like the wholesome eight. They are the ten.

Distress can be wholesome. The paragraph does not say when. No example is invented. Pleasant feeling is not therefore wholesome. Pleasure and gladness are in the threefold group.

The two eights are different. Faith and the three are wholesome. Eye through life are indeterminate. Shared wholesome status does not erase the outflow split of 2.09. The five can be either. The three are without outflows.

Interpretation: ethical assessment does not follow from tone, outflow, or maturation alone. The new question preserves those earlier determinations while distinguishing the qualities a Faculty may bear. It does not supply an example or mechanism of wholesome distress.

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

organon:VAK_2_11_Interpretation
    organon:distinguishes vak:FeelingTone, vak:EthicalQuality,
        vak:OutflowStatus, vak:MaturationStatus .
```
