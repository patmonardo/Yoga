# VAK_2.31 — What the Higher Levels Drop

## 1. Sanskrit (Devanāgarī)

```sanskrit
कौकृत्यमिद्धाकुशलान्याद्ये ध्याने न सन्त्यतः ।
ध्यानान्तरे वितर्कश्च विचारश्चाप्यतः परम् ॥ २.३१ ॥
```

## 2. Sanskrit (IAST)

```text
kaukṛtyamiddhākuśalāny ādye dhyāne na santy ataḥ /
dhyānāntare vitarkaś ca vicāraś cāpy ataḥ param // 2.31 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| kaukṛtya-middha-akuśalāni | nom. pl. n.; coordinated compound | regret, torpor, and the unwholesome |
| ādye dhyāne | loc. sg. n. + loc. sg. n. | in the first dhyāna |
| na santi | negation + 3 pl. present indicative | are not present |
| ataḥ | pronominal adverb in -tas | from the previously stated distribution |
| dhyāna-antare | loc. sg. n. | in the intermediate dhyāna |
| vitarkaḥ ca | nom. sg. m. + particle | initial examination also |
| vicāraḥ ca api | nom. sg. m. + particles | sustained examination also; api additionally resolved in the prose |
| ataḥ param | adverbial phrase | beyond this |

Ataḥ points back to the Desire Realm distribution. Not a cause.

The later ataḥ points to the intermediate level. Sandhi is opened;
the coordinated opening compound remains intact.

```text
# tokens: kaukṛtyamiddhākuśalāni ādye dhyāne na santi ataḥ dhyānāntare vitarkaḥ ca vicāraḥ ca api ataḥ param
```

## 4. Grammar

The first clause excludes three categories relative to the preceding
distribution. The next two carry the negative predicate and prior
exclusions forward. These are distinct levels with cumulative
restrictions, not a chain of level identities. The prose resolves
api as additionally excluding deception and crookedness beyond
the intermediate.

```nltk-fcfg
% start S
# tokens: kaukṛtyamiddhākuśalāni ādye dhyāne na santi ataḥ dhyānāntare vitarkaḥ ca vicāraḥ ca api ataḥ param
S[SEM=<(?first & ?intermediate & ?beyond)>] -> FIRST[SEM=?first] INTERMEDIATE[SEM=?intermediate] BEYOND[SEM=?beyond]
FIRST[SEM=<(Excludes(first,regret) & Excludes(first,torpor) & Excludes(first,unwholesome))>] -> DROPS[CASE=nom,NUM=pl] FIRSTLEVEL[CASE=loc] DHYANA[CASE=loc] NOT ARE[NUM=pl] FROM[REF=desire_distribution]
INTERMEDIATE[SEM=<(CarriesExclusions(intermediate,first) & Excludes(intermediate,initial))>] -> MIDLEVEL[CASE=loc] INITIAL[CASE=nom] AND
BEYOND[SEM=<(CarriesExclusions(beyond,intermediate) & Excludes(beyond,sustained))>] -> SUSTAINED[CASE=nom] AND ALSO[READING=further_exclusion] FROM[REF=intermediate] BEYONDWORD
DROPS[CASE=nom,NUM=pl] -> 'kaukṛtyamiddhākuśalāni'
FIRSTLEVEL[CASE=loc] -> 'ādye'
DHYANA[CASE=loc] -> 'dhyāne'
NOT -> 'na'
ARE[NUM=pl] -> 'santi'
FROM[REF=desire_distribution] -> 'ataḥ'
MIDLEVEL[CASE=loc] -> 'dhyānāntare'
INITIAL[CASE=nom] -> 'vitarkaḥ'
AND -> 'ca'
SUSTAINED[CASE=nom] -> 'vicāraḥ'
ALSO[READING=further_exclusion] -> 'api'
FROM[REF=intermediate] -> 'ataḥ'
BEYONDWORD -> 'param'
```

```nltk-dep
'santi' -> 'kaukṛtyamiddhākuśalāni' | 'ādye' | 'dhyāne' | 'na' | 'ataḥ' | 'dhyānāntare' | 'vitarkaḥ' | 'vicāraḥ' | 'param'
'vitarkaḥ' -> 'ca'
'vicāraḥ' -> 'ca' | 'api'
```

The dependencies cover the carried predicate; the two identical ataḥ
tokens receive their distinct references in the feature grammar.

| Span | Constituent | Result |
|---|---|---|
| [0, 6) | `FIRST` | regret, torpor, unwholesome excluded |
| [6, 9) | `INTERMEDIATE` | prior exclusions plus initial examination |
| [9, 14) | `BEYOND` | prior exclusions plus sustained examination |

## 5. Translation

### Literal Translation

> Regret, torpor, and the unwholesome factors are absent in the first
> dhyāna. In the intermediate dhyāna, vitarka too is absent; beyond it,
> vicāra too.
### Bhāṣya-informed study translation

> Of the previously stated factors, regret, torpor, and all unwholesome
> factors are absent in the first dhyāna. In the intermediate dhyāna,
> initial examination is also absent. Beyond the intermediate—in the
> second and higher dhyānas and the Formless levels—sustained examination
> is also absent, as are deception and crookedness. Prior exclusions
> continue to apply.
## 6. Philosophical Translation

> The higher levels drop factors; they do not invent new ones. Unwholesome is excluded; not every affliction is. The accumulation is the rule.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| ādya-dhyāna | first dhyāna | drops regret, torpor, unwholesome operation |
| dhyānāntara | intermediate dhyāna | drops initial examination; sustained examination remains |
| ataḥ param | beyond this | second and higher, and the formless |
| yathā-pratiṣiddham | as previously excluded | carried upward |
| śāṭhya, mada, māyā | crookedness, intoxication, deception | the three exceptions at the first |
| parṣat-sambandha | connection with an assembly | why crookedness stops at Brahmā |
| kṣepa | evasion | Brahmā's response |

Mada is not conceit. Middha is not sluggishness.

## 8. Logical Determination

**Kārikā, derived.** Excludes relates a level to an excluded category.
CarriesExclusions relates restrictions, not a consciousness's identity.
The prose adds two named exclusions and specifies the first-level
anger-group exceptions.

```nltk-sem
exclusion : \f.\l.Excludes(l,f)
carry : \a.\b.CarriesExclusions(b,a)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((Excludes(first,regret) & Excludes(first,torpor) & Excludes(first,unwholesome)) & (CarriesExclusions(intermediate,first) & Excludes(intermediate,initial)) & (CarriesExclusions(beyond,intermediate) & Excludes(beyond,sustained)))

# THEORY prose_cumulative_exclusions
# EXPECT prose_cumulative_exclusions T
all a b f.((CarriesExclusions(b,a) & Excludes(a,f)) -> Excludes(b,f))
Excludes(beyond,deception) & Excludes(beyond,crookedness)
all x.(FirstAngerGroupExclusion(x) <-> (AngerGroup(x) & -FirstException(x)))

# THEORY rejected_levels_are_identical
# EXPECT rejected_levels_are_identical F
first = intermediate

# THEORY rejected_three_exceptions_all_drop_later
# EXPECT rejected_three_exceptions_all_drop_later F
all x.(FirstException(x) -> Excludes(beyond,x))

# THEORY rejected_intermediate_already_drops_sustained
# EXPECT rejected_intermediate_already_drops_sustained F
Excludes(intermediate,sustained) & CarriesExclusions(intermediate,first)
```

```nltk-valuation
first => first_level
intermediate => intermediate_level
beyond => higher_levels
regret => regret_kind
torpor => torpor_kind
unwholesome => unwholesome_category
initial => initial_examination
sustained => sustained_examination
deception => deception_kind
crookedness => crookedness_kind
CarriesExclusions => {(intermediate_level,first_level),(higher_levels,intermediate_level)}
Excludes => {(first_level,regret_kind),(first_level,torpor_kind),(first_level,unwholesome_category),(intermediate_level,regret_kind),(intermediate_level,torpor_kind),(intermediate_level,unwholesome_category),(intermediate_level,initial_examination),(higher_levels,regret_kind),(higher_levels,torpor_kind),(higher_levels,unwholesome_category),(higher_levels,initial_examination),(higher_levels,sustained_examination),(higher_levels,deception_kind),(higher_levels,crookedness_kind)}
AngerGroup => {anger_kind,resentment_kind,crookedness_kind,envy_kind,spite_kind,concealment_kind,stinginess_kind,deception_kind,intoxication_kind,harmfulness_kind}
FirstException => {crookedness_kind,intoxication_kind,deception_kind}
FirstAngerGroupExclusion => {anger_kind,resentment_kind,envy_kind,spite_kind,concealment_kind,stinginess_kind,harmfulness_kind}
```

The exclusion table mixes explicitly labeled categories and named
factors; its row lengths are not totals of absent factors. In
particular, unwholesome is not a single factor. Omission from the
further drop does not assert intoxication's occurrence in every
higher consciousness. The model tests the stated cumulative rules,
not the entire distribution of every possible higher-level episode.

## 9. Interpretive Note

**Translation note.** The commentary specifies the omitted unwholesome factors: hostility; the anger-group except crookedness, intoxication, and deception; shamelessness; and lack of moral caution. Crookedness is limited to the company of Brahmā; its narrative is damaged, including titles and parts of the reply. The rule retains the other factors as before.

The Brahmā episode supports the upper limit of crookedness. The question is Aśvajit's. The titles are Brahmā's. The commentary calls the response an evasion made without knowing. Not an assertion of creative authority. The story is not completed from elsewhere. Assembly-dependence is stated for crookedness. Not expanded into a theory of both factors.

The title sequence is damaged. Creator, Producer is provisional. Four and I am are contextual readings.

The close indexes three variables: which level, which consciousness, how many factors. The remainder as before keeps what was not altered.

In the Organon reading, Cognition governs Perception and Conception
without collapsing into consciousness or Mind. A level's inventory
restricts possible accompanying factors; it does not identify that
level with an earlier one or make status itself knowledge.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_31
    a vak:Karika ;
    rdfs:label "VAK 2.31" ;
    vak:hasTopic vak:HigherLevelExclusions ;
    vak:belongsTo vak:Indriyanirdesa .

vak:FirstDhyana vak:excludes vak:Regret, vak:Torpor, vak:Unwholesome .
vak:IntermediateDhyana vak:excludes vak:Vitarka .
vak:BeyondIntermediate vak:excludes vak:Vicara, vak:Deception, vak:Crookedness .

organon:VAK_2_31_Interpretation
    organon:distinguishes vak:LevelIdentity, vak:InheritedExclusion,
        vak:EthicalCharacter, vak:FactorIdentity .
```
