# VAK_2.20 — The Fewest

## 1. Sanskrit (Devanāgarī)

```sanskrit
सर्वाल्पैर्निःशुभोऽष्टाभिर्विन्मनःकायजीवितैः ।
युक्तो बालस्तथारूप्ये उपेक्षायुर्मनःशुभैः ॥ २.२० ॥
```

## 2. Sanskrit (IAST)

```text
sarvālpair niḥśubho 'ṣṭābhir vinmanaḥkāyajīvitaiḥ /
yukto bālas tathārūpye upekṣāyurmanaḥśubhaiḥ // 2.20 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sarva-alpaiḥ | instrumental plural superlative adjective | with the fewest [Faculties] |
| niḥ-śubhaḥ | nominative singular masculine privative compound | one without the wholesome; glossed as severed wholesome roots |
| aṣṭābhiḥ | instrumental plural numeral | with eight [Faculties] |
| vit-manas-kāya-jīvitaiḥ | instrumental plural coordinated compound | the five feelings, Mind, body, and life |
| yuktaḥ | nominative singular masculine past passive participle | endowed; possession, not manifestation |
| bālaḥ | nominative singular masculine noun | ordinary person, explicitly glossed pṛthagjana |
| tathā | comparative adverb | likewise; carries the minimum count, not severed roots |
| ārūpye | locative singular neuter noun | in the Formless realm |
| upekṣā-āyus-manas-śubhaiḥ | instrumental plural coordinated compound | neutral feeling, life, Mind, and the five beginning with faith |

Niḥśubha is severed wholesome roots. Śubha here is the five beginning with faith, not the three.

**Grammar tokens.** External sandhi is opened, including *tathā ārūpye*.
Compounds remain intact; their member-lists are resolved from the Bhāṣya.

```text
# tokens: sarvālpaiḥ niḥśubhaḥ aṣṭābhiḥ vit-manas-kāya-jīvitaiḥ yuktaḥ bālaḥ tathā ārūpye upekṣā-āyus-manas-śubhaiḥ
```

## 4. Grammar

The opening superlative sets the minimum question. Eight and the
first instrumental compound predicate endowment of the root-severed
person. Likewise carries that count to the Formless ordinary person,
whose instrumental compound gives a different membership. It does not
carry severed roots into the second case. The prose restricts wholesome
to the faith-group through both the count and ordinary-person status.

```nltk-fcfg
% start S
# tokens: sarvālpaiḥ niḥśubhaḥ aṣṭābhiḥ vit-manas-kāya-jīvitaiḥ yuktaḥ bālaḥ tathā ārūpye upekṣā-āyus-manas-śubhaiḥ
S[SEM=<(?first & ?second)>] -> FIRST[SEM=?first] SECOND[SEM=?second]
FIRST[SEM=<(?minimum(?case) & MinimumCount(?case,?count) & ?members(?case))>] -> MINIMUM[CASE=ins,SEM=?minimum] ROOTLESS[CASE=nom,GEN=m,SEM=?case] EIGHT[CASE=ins,CNT=8,SEM=?count] FIRSTSET[CASE=ins,SEM=?members] ENDOWED[CASE=nom,GEN=m]
SECOND[SEM=<(MinimumCase(formless_ordinary) & ?same(formless_ordinary) & ?members(formless_ordinary))>] -> ORDINARY[CASE=nom,GEN=m] LIKEWISE[REF=minimum_eight,SEM=?same] FORMLESS[CASE=loc] SECONDSET[CASE=ins,RANGE=faith_five,SEM=?members]
MINIMUM[CASE=ins,SEM=<\c.MinimumCase(c)>] -> 'sarvālpaiḥ'
ROOTLESS[CASE=nom,GEN=m,SEM=<severed_roots>] -> 'niḥśubhaḥ'
EIGHT[CASE=ins,CNT=8,SEM=<eight>] -> 'aṣṭābhiḥ'
FIRSTSET[CASE=ins,SEM=<\c.FeelingsBodyMindLife(c)>] -> 'vit-manas-kāya-jīvitaiḥ'
ENDOWED[CASE=nom,GEN=m] -> 'yuktaḥ'
ORDINARY[CASE=nom,GEN=m] -> 'bālaḥ'
LIKEWISE[REF=minimum_eight,SEM=<\c.MinimumCount(c,eight)>] -> 'tathā'
FORMLESS[CASE=loc] -> 'ārūpye'
SECONDSET[CASE=ins,RANGE=faith_five,SEM=<\c.NeutralLifeMindFaith(c)>] -> 'upekṣā-āyus-manas-śubhaiḥ'
```

```nltk-dep
'yuktaḥ' -> 'sarvālpaiḥ' | 'niḥśubhaḥ' | 'aṣṭābhiḥ' | 'vit-manas-kāya-jīvitaiḥ'
'bālaḥ' -> 'tathā' | 'ārūpye' | 'upekṣā-āyus-manas-śubhaiḥ'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 5) | `FIRST` | root-severed minimum, five feelings plus three |
| [5, 9) | `SECOND` | Formless ordinary-person minimum, triad plus five |
| [0, 9) | `S` | equal minima with different member-sets |

## 5. Translation

### Literal Translation

> One without the wholesome is endowed, at the least, with eight: feeling,
> mind, body, and life. Likewise an ordinary person in the formless realm,
> with neutral feeling, life, mind, and the wholesome faculties.

### Bhāṣya-informed study translation

> At the minimum, one whose wholesome roots are severed possesses eight
> Faculties: the five feelings, Mind, body, and life. Likewise, an ordinary
> person in the Formless realm possesses eight: neutral feeling, life,
> Mind, and the five beginning with faith.

## 6. Philosophical Translation

> The minimum count does not identify one universal eight-member set.
> The two cases share neutral feeling, life, and Mind but differ in
> the five Faculties completing their minima.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| sarvālpa | the fewest | eight |
| niḥśubha | without the wholesome | severed roots |
| vit | feeling | the five; vedayate |
| bāla | ordinary person | pṛthagjana; not a child |
| śubha | the wholesome | the five, in this count |
| samucchinna-kuśala-mūla | severed wholesome roots | the first case |

## 8. Logical Determination

**Kārikā, derived.** The SEM records two minimum cases with different
membership descriptions. The prose supplies the five feelings and
restricts wholesome to the five beginning with faith. These are
possession inventories, not simultaneous feeling-events.

```nltk-sem
minimum_count : \c.MinimumCount(c,eight)
first_members : \c.FeelingsBodyMindLife(c)
second_members : \c.NeutralLifeMindFaith(c)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(MinimumCase(severed_roots) & MinimumCount(severed_roots,eight) & FeelingsBodyMindLife(severed_roots) & MinimumCase(formless_ordinary) & MinimumCount(formless_ordinary,eight) & NeutralLifeMindFaith(formless_ordinary))

# THEORY prose_members
# EXPECT prose_members T
all x.(MinimumMember(severed_roots,x) <-> (FeelingFive(x) | x = mind_f | x = body_f | x = life_f))
all x.(MinimumMember(formless_ordinary,x) <-> (CoreThree(x) | FaithFive(x)))
all x.(LocalWholesome(x) <-> FaithFive(x))
all x.(RealizationFaculty(x) -> -MinimumMember(formless_ordinary,x))
all x.(MinimumMember(severed_roots,x) -> Possesses(rootless_with_extra,x))

# THEORY rejected_equal_count_equal_set
# EXPECT rejected_equal_count_equal_set F
all x.(MinimumMember(severed_roots,x) <-> MinimumMember(formless_ordinary,x))

# THEORY rejected_all_rootless_have_exactly_eight
# EXPECT rejected_all_rootless_have_exactly_eight F
all x.(Possesses(rootless_with_extra,x) <-> MinimumMember(severed_roots,x))

# THEORY rejected_wholesome_includes_realization_here
# EXPECT rejected_wholesome_includes_realization_here F
exists x.(RealizationFaculty(x) & LocalWholesome(x))
```

```nltk-valuation
severed_roots => rootless_minimum
formless_ordinary => formless_minimum
eight => count_eight
mind_f => mind
body_f => body
life_f => life
rootless_with_extra => illustrative_rootless_person
MinimumCase => {rootless_minimum,formless_minimum}
MinimumCount => {(rootless_minimum,count_eight),(formless_minimum,count_eight)}
FeelingsBodyMindLife => {rootless_minimum}
NeutralLifeMindFaith => {formless_minimum}
FeelingFive => {pain,pleasure,gladness,distress,neutral}
CoreThree => {neutral,life,mind}
FaithFive => {faith,vigor,mindfulness,concentration,comprehension}
RealizationFaculty => {shall_know,knowledge,one_who_has_known}
LocalWholesome => {faith,vigor,mindfulness,concentration,comprehension}
MinimumMember => {(rootless_minimum,pain),(rootless_minimum,pleasure),(rootless_minimum,gladness),(rootless_minimum,distress),(rootless_minimum,neutral),(rootless_minimum,mind),(rootless_minimum,body),(rootless_minimum,life),(formless_minimum,neutral),(formless_minimum,life),(formless_minimum,mind),(formless_minimum,faith),(formless_minimum,vigor),(formless_minimum,mindfulness),(formless_minimum,concentration),(formless_minimum,comprehension)}
Possesses => {(illustrative_rootless_person,pain),(illustrative_rootless_person,pleasure),(illustrative_rootless_person,gladness),(illustrative_rootless_person,distress),(illustrative_rootless_person,neutral),(illustrative_rootless_person,mind),(illustrative_rootless_person,body),(illustrative_rootless_person,life),(illustrative_rootless_person,eye)}
```

Each minimum has eight members; their intersection is the possession
triad. The extra-eye case illustrates why the first minimum is not an
exact total for every root-severed person. `LocalWholesome` records
the verse's restricted reference; it does not deny that the three
realization Faculties are wholesome. These finite checks establish
membership and count consistency, not a proof that all possible
possession configurations have at least eight.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): The fewest is eight. One whose wholesome roots are
severed is endowed with the five feelings, body, mind, and life. An
ordinary person in the formless realm is endowed with neutral feeling,
life, mind, and the five beginning with faith. The path-faculties are
excluded because the subject is eight and the subject is an ordinary
person.

The question has changed. Not what one faculty entails. What is the fewest a possessor can have.

Without the wholesome is not an unwholesome thought, and not no faculties. The first eight still feels. Vit is not a sixth feeling.

At the least does not say every severed-roots person lacks eye, ear, nose, tongue, or the sex faculties. The prose does not list when those are absent.

Wholesome would also take the three. The eight and the ordinary person exclude them. The reply does not deny that the three are wholesome. General extension and local range need not coincide.

Five feelings in the count are not five feelings in one moment.

Interpretation: the floor is typed. The telos is not this verse. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_20
    a vak:Karika ;
    rdfs:label "VAK 2.20" ;
    vak:hasTopic vak:MinimumPossession ;
    vak:belongsTo vak:Indriyanirdesa .

vak:SeveredRootsMinimum vak:hasCount 8 .
vak:FormlessOrdinaryMinimum vak:hasCount 8 .

organon:VAK_2_20_Interpretation
    organon:distinguishes vak:MinimumCount, vak:MinimumMembership,
        vak:ActualPossession .
```
