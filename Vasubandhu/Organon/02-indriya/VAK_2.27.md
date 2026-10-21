# VAK_2.27 — The Limited Ground

## 1. Sanskrit (Devanāgarī)

```sanskrit
क्रोधोपनाहशाठ्येर्ष्याप्रदासम्रक्षमत्सराः ।
मायामदविहिंसाश्च परीत्तक्लेशभूमिकाः ॥ २.२७ ॥
```

## 2. Sanskrit (IAST)

```text
krodhopanāhaśāṭhyerṣyāpradāsamrakṣamatsarāḥ /
māyāmadavihiṃsāś ca parīttakleśabhūmikāḥ // 2.27 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| krodha-upanāha-śāṭhya-īrṣyā-pradāsa-mrakṣa-matsarāḥ | nominative plural masculine coordinated compound; seven members | anger, resentment, crookedness, envy, spite, concealment, stinginess |
| māyā-mada-vihiṃsāḥ | nominative plural feminine coordinated compound; three members | deception, intoxication, harmfulness |
| ca | conjunction | and; joins the two enumerations |
| parītta-kleśa-bhūmikāḥ | nominative plural masculine class adjective | belonging to the limited-affliction ground; predicate of the enumeration |

The English names are provisional; definitions are deferred. Compound
members are not independently inflected singular nominatives.
The grammar retains both compounds and opens only external sandhi.

```text
# tokens: krodhopanāhaśāṭhyerṣyāpradāsamrakṣamatsarāḥ māyāmadavihiṃsāḥ ca parīttakleśabhūmikāḥ
```

## 4. Grammar

Seven plus three yields ten class-members. `Ca` conjoins the two
compound-level membership assertions. A class predicate applies
to every named member; unlike the previous lists, no always-in-every-
consciousness locative is present. The prose then supplies restrictions
on associated ignorance, not additional verse tokens.

```nltk-fcfg
% start S
# tokens: krodhopanāhaśāṭhyerṣyāpradāsamrakṣamatsarāḥ māyāmadavihiṃsāḥ ca parīttakleśabhūmikāḥ
S[SEM=<?members(?class)>] -> MEMBERS[CNT=10,SEM=?members] CLASS[CASE=nom,NUM=pl,SEM=?class]
MEMBERS[CNT=10,SEM=<\P.?and(?seven(P),?three(P))>] -> SEVEN[CASE=nom,NUM=pl,CNT=7,SEM=?seven] THREE[CASE=nom,NUM=pl,CNT=3,SEM=?three] AND[READING=enumeration,SEM=?and]
SEVEN[CASE=nom,NUM=pl,CNT=7,SEM=<\P.(P(anger) & P(resentment) & P(crookedness) & P(envy) & P(spite) & P(concealment) & P(stinginess))>] -> 'krodhopanāhaśāṭhyerṣyāpradāsamrakṣamatsarāḥ'
THREE[CASE=nom,NUM=pl,CNT=3,SEM=<\P.(P(deception) & P(intoxication) & P(harmfulness))>] -> 'māyāmadavihiṃsāḥ'
AND[READING=enumeration,SEM=<\L.\R.(L & R)>] -> 'ca'
CLASS[CASE=nom,NUM=pl,SEM=<\x.LimitedKind(x)>] -> 'parīttakleśabhūmikāḥ'
```

```nltk-dep
'parīttakleśabhūmikāḥ' -> 'krodhopanāhaśāṭhyerṣyāpradāsamrakṣamatsarāḥ' | 'māyāmadavihiṃsāḥ'
'māyāmadavihiṃsāḥ' -> 'ca'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 3) | `MEMBERS` | two compounds, seven plus three |
| [3, 4) | `CLASS` | limited-affliction class predicate |
| [0, 4) | `S` | ten membership assertions, no co-presence assertion |

## 5. Translation

### Literal Translation

> Anger, resentment, crookedness, envy, spite, concealment, stinginess,
> deception, intoxication, and harmfulness belong to the ground of limited
> afflictions.

### Bhāṣya-informed study translation

> Anger, resentment, crookedness, envy, spite, concealment, stinginess,
> deception, intoxication, and harmfulness belong to the ground of limited
> afflictions.

## 6. Philosophical Translation

> Limited-affliction ground is a restricted range, not a universal
> accompanying bundle. The associated ignorance has specified
> qualifications; this does not make it one identical occurrence
> shared by all ten or settle which members can co-occur.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| parītta-kleśa-bhūmika | limited-affliction ground | range, not slightness |
| avidyā-mātreṇa | only with ignorance | among afflictions |
| bhāvanā-heya | abandonable through cultivation | not through seeing |
| mano-bhūmika | of the mental sphere | not the five sensory consciousnesses |
| upakleśa | secondary affliction | where the definitions wait |
| aniyata | unfixed | not ethically indeterminate |

## 8. Logical Determination

**Kārikā, derived.** The `ca` SEM joins ten class-members, not ten
simultaneous occurrences. The prose model represents association
restrictions among afflictions separately from other accompanying
dharmas.

```nltk-sem
class_predicate : \x.LimitedKind(x)
compound_conjunction : \L.\R.(L & R)
seven_plus_three : \P.(P(anger) & P(resentment) & P(crookedness) & P(envy) & P(spite) & P(concealment) & P(stinginess) & P(deception) & P(intoxication) & P(harmfulness))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((LimitedKind(anger) & LimitedKind(resentment) & LimitedKind(crookedness) & LimitedKind(envy) & LimitedKind(spite) & LimitedKind(concealment) & LimitedKind(stinginess)) & (LimitedKind(deception) & LimitedKind(intoxication) & LimitedKind(harmfulness)))

# THEORY prose_restriction
# EXPECT prose_restriction T
all f.(LimitedKind(f) -> exists i.(AssociatedAffliction(f,i) & Ignorance(i) & CultivationAbandonable(i) & MentalSphere(i)))
all f i.((LimitedKind(f) & AssociatedAffliction(f,i)) -> (Ignorance(i) & CultivationAbandonable(i) & MentalSphere(i)))

# THEORY rejected_ignorance_only_companion_of_any_kind
# EXPECT rejected_ignorance_only_companion_of_any_kind F
all f x.((LimitedKind(f) & OtherCompanion(f,x)) -> Ignorance(x))

# THEORY rejected_shared_class_forces_bundle
# EXPECT rejected_shared_class_forces_bundle F
all c f.((IllustrativeEpisode(c) & LimitedKind(f)) -> Present(c,f))
```

```nltk-valuation
anger => anger_kind
resentment => resentment_kind
crookedness => crookedness_kind
envy => envy_kind
spite => spite_kind
concealment => concealment_kind
stinginess => stinginess_kind
deception => deception_kind
intoxication => intoxication_kind
harmfulness => harmfulness_kind
LimitedKind => {anger_kind,resentment_kind,crookedness_kind,envy_kind,spite_kind,concealment_kind,stinginess_kind,deception_kind,intoxication_kind,harmfulness_kind}
AssociatedAffliction => {(anger_kind,qualified_ignorance),(resentment_kind,qualified_ignorance),(crookedness_kind,qualified_ignorance),(envy_kind,qualified_ignorance),(spite_kind,qualified_ignorance),(concealment_kind,qualified_ignorance),(stinginess_kind,qualified_ignorance),(deception_kind,qualified_ignorance),(intoxication_kind,qualified_ignorance),(harmfulness_kind,qualified_ignorance)}
Ignorance => {qualified_ignorance}
CultivationAbandonable => {qualified_ignorance}
MentalSphere => {qualified_ignorance}
OtherCompanion => {(anger_kind,consciousness_example),(anger_kind,feeling_example)}
IllustrativeEpisode => {anger_episode,envy_episode}
Present => {(anger_episode,anger_kind),(envy_episode,envy_kind)}
UnfixedExample => {initial_examination,sustained_examination,regret,torpor}
```

Qualified ignorance is a type-level representative, not a single
token occurring simultaneously with all ten. The episodes are partial
countermodels to inference from membership to a universal bundle;
they do not establish the actual mutual-exclusion rules of the ten.
OtherCompanion keeps the restriction from denying consciousness or
universal factors. The four unfixed examples are not an exhaustive
class and are not thereby ethically indeterminate.

## 9. Interpretive Note

**Translation note.** The commentary associates this class only with ignorance abandonable through cultivation in the mental sphere, then names five classes of mental factors and unfixed examples: initial and sustained examination, regret, and torpor. It defers the factors' definitions and leaves the list open.

Anger is not resentment. Crookedness is not deception. Spite is not harmfulness. The distinctions are named. They are not yet explained. Concealment and intoxication are not complete definitions. Intoxication is not settled as a substance.

Secondary affliction is the deferred discussion. It is not identified with this class. Ground remains range of operation.

The unfixed examples leave the list open. Their distributions wait on the count of what must be in a given consciousness.

In the Organon reading, Cognition governs Perception and Conception
without collapsing into consciousness or Mind. The range of this
class restricts associated ignorance; it does not define a new
Cognition or convert all ten factors into one operation. Shared
constraints are not a required bundle.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_27
    a vak:Karika ;
    rdfs:label "VAK 2.27" ;
    vak:hasTopic vak:LimitedAfflictionGround ;
    vak:belongsTo vak:Indriyanirdesa .

vak:LimitedTen vak:hasMemberCount 10 .
vak:FiveClasses vak:exhaustive false .

organon:VAK_2_27_Interpretation
    organon:distinguishes vak:ClassMembership, vak:AssociationRestriction,
        vak:EpisodeComposition .
```
