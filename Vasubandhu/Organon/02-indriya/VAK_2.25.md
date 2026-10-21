# VAK_2.25 — Always in the Wholesome

## 1. Sanskrit (Devanāgarī)

```sanskrit
श्रद्धाप्रमादः प्रश्रब्धिरुपेक्षा ह्रीरपत्रपा ।
मूलद्वयमहिंसा च वीर्यं च कुशले सदा ॥ २.२५ ॥
```

## 2. Sanskrit (IAST)

```text
śraddhāpramādaḥ praśrabdhir upekṣā hrīr apatrapā /
mūladvayam ahiṃsā ca vīryaṃ ca kuśale sadā // 2.25 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| śraddhā | nom. sg. f. | faith |
| apramādaḥ | nom. sg. m. | heedfulness |
| praśrabdhiḥ | nom. sg. f. | pliancy |
| upekṣā | nom. sg. f. | equanimity; not neutral feeling |
| hrīḥ | nom. sg. f. | moral shame; explained later |
| apatrapā | nom. sg. f. | moral caution; explained later |
| mūla-dvayam | nom. sg. n.; numeral compound | two roots: non-greed, non-hatred |
| ahiṃsā | nom. sg. f. | non-harming |
| vīryam | nom. sg. n. | vigor |
| ca | conjunction, twice | and; coordinates the list |
| kuśale sadā | loc. sg. n. + adverb | always in the wholesome |

Ten, counting the two roots separately. Non-delusion is prajñā, already in the universal ten. Not counted again.

The opening is faith plus heedfulness, not faith plus negligence.
External sandhi is opened; the two roots remain one compound token.

```text
# tokens: śraddhā apramādaḥ praśrabdhiḥ upekṣā hrīḥ apatrapā mūladvayam ahiṃsā ca vīryam ca kuśale sadā
```

## 4. Grammar

The list is conjunctive. Its nine nominal expressions count ten
factor-kinds because the root-pair contributes two. Always in the
wholesome scopes the whole list; consciousness is supplied by the prose.
`Kuśale` supplies the wholesome condition, and `sadā` quantifies over
every moment in that condition. The two root-names are prose-resolved,
not extra verse tokens.

```nltk-fcfg
% start S
# tokens: śraddhā apramādaḥ praśrabdhiḥ upekṣā hrīḥ apatrapā mūladvayam ahiṃsā ca vīryam ca kuśale sadā
S[SEM=<?always(?wholesome(?list))>] -> TEN[CNT=10,SEM=?list] WHOLESOME[CASE=loc,SCOPE=wholesome_consciousness,SEM=?wholesome] ALWAYS[SCOPE=every_moment,SEM=?always]
TEN[CNT=10,SEM=<\c.(Present(c,?a) & Present(c,?b) & Present(c,?d) & Present(c,?e) & Present(c,?f) & Present(c,?g) & ?roots(c) & Present(c,?h) & Present(c,?i))>] -> FAITH[SEM=?a] HEEDFUL[PRIVATIVE=true,SEM=?b] PLIANCY[SEM=?d] EQUANIMITY[SEM=?e] SHAME[SEM=?f] CAUTION[SEM=?g] ROOTPAIR[CNT=2,SEM=?roots] NONHARM[SEM=?h] AND VIGOR[SEM=?i] AND
FAITH[SEM=<faith>] -> 'śraddhā'
HEEDFUL[PRIVATIVE=true,SEM=<heedfulness>] -> 'apramādaḥ'
PLIANCY[SEM=<pliancy>] -> 'praśrabdhiḥ'
EQUANIMITY[SEM=<equanimity>] -> 'upekṣā'
SHAME[SEM=<shame>] -> 'hrīḥ'
CAUTION[SEM=<caution>] -> 'apatrapā'
ROOTPAIR[CNT=2,SEM=<\c.(Present(c,nongreed) & Present(c,nonhatred))>] -> 'mūladvayam'
NONHARM[SEM=<nonharming>] -> 'ahiṃsā'
AND -> 'ca'
VIGOR[SEM=<vigor>] -> 'vīryam'
WHOLESOME[CASE=loc,SCOPE=wholesome_consciousness,SEM=<\P.\c.(WholesomeMoment(c) -> P(c))>] -> 'kuśale'
ALWAYS[SCOPE=every_moment,SEM=<\P.all c.P(c)>] -> 'sadā'
```

```nltk-dep
'kuśale' -> 'śraddhā' | 'apramādaḥ' | 'praśrabdhiḥ' | 'upekṣā' | 'hrīḥ' | 'apatrapā' | 'mūladvayam' | 'ahiṃsā' | 'vīryam' | 'sadā'
'ahiṃsā' -> 'ca'
'vīryam' -> 'ca'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 11) | `TEN` | ten kinds, including two roots |
| [11, 13) | scope | always in wholesome consciousness |
| [0, 13) | `S` | tenfold co-presence under restricted scope |

## 5. Translation

### Literal Translation

> Faith, heedfulness, pliancy, equanimity, moral shame and moral caution,
> the two roots, non-harming, and vigor are always present in the wholesome.

### Bhāṣya-informed study translation

> Faith, heedfulness, pliancy, equanimity, moral shame and moral caution,
> the two roots—non-greed and non-hatred—non-harming, and vigor are
> always present together in wholesome consciousness.

## 6. Philosophical Translation

> The wholesome range is narrower than consciousness generally.
> The two roots contribute two members; non-delusion is not counted
> again apart from discriminative comprehension. Equanimity's
> compatibility with attention remains an examined difficulty,
> not a demonstrated reconciliation.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| kuśala-mahābhūmika | wholesome great-ground | every wholesome consciousness |
| śraddhā | faith | clarity; others: conviction |
| apramāda | heedfulness | attentive care; another school: guarding |
| praśrabdhi | pliancy | workability of consciousness |
| upekṣā | equanimity | evenness, non-application; not neutral feeling |
| alobha, adveṣa | non-greed, non-hatred | the two roots counted |
| amoha | non-delusion | prajñā; not counted again |
| ahiṃsā | non-harming | non-injury |
| vīrya | vigor | arousal of consciousness |
| bodhyaṅgānukūlya | favorable to an awakening factor | why the body receives the name |

## 8. Logical Determination

**Kārikā with prose-resolved roots.** `Kuśale` and `sadā` compose
the restricted universal scope: each wholesome moment has the ten
named kinds. The universal ten of 2.24 remain, and the
prose identifies non-delusion with discriminative comprehension
rather than adding an eleventh wholesome-class member.

```nltk-sem
root_pair : \c.(Present(c,nongreed) & Present(c,nonhatred))
wholesome_scope : \P.\c.(WholesomeMoment(c) -> P(c))
always_scope : \P.all c.P(c)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
all c.(WholesomeMoment(c) -> (Present(c,faith) & Present(c,heedfulness) & Present(c,pliancy) & Present(c,equanimity) & Present(c,shame) & Present(c,caution) & (Present(c,nongreed) & Present(c,nonhatred)) & Present(c,nonharming) & Present(c,vigor)))

# THEORY prose_scope
# EXPECT prose_scope T
all c.(WholesomeMoment(c) -> ConsciousnessMoment(c))
all c f.((ConsciousnessMoment(c) & UniversalKind(f)) -> Present(c,f))
nondelusion = comprehension

# THEORY rejected_wholesome_ten_in_every_consciousness
# EXPECT rejected_wholesome_ten_in_every_consciousness F
all c f.((ConsciousnessMoment(c) & WholesomeKind(f)) -> Present(c,f))

# THEORY rejected_nondelusion_is_extra_member
# EXPECT rejected_nondelusion_is_extra_member F
WholesomeKind(nondelusion) & -(nondelusion = comprehension)

# THEORY rejected_equanimity_is_neutral_feeling
# EXPECT rejected_equanimity_is_neutral_feeling F
equanimity = neutral_feeling
```

```nltk-valuation
faith => faith_kind
heedfulness => heedfulness_kind
pliancy => pliancy_kind
equanimity => equanimity_kind
shame => shame_kind
caution => caution_kind
nongreed => nongreed_kind
nonhatred => nonhatred_kind
nonharming => nonharming_kind
vigor => vigor_kind
nondelusion => comprehension_kind
comprehension => comprehension_kind
neutral_feeling => neutral_feeling_mode
WholesomeMoment => {wholesome_moment}
ConsciousnessMoment => {wholesome_moment,other_moment}
WholesomeKind => {faith_kind,heedfulness_kind,pliancy_kind,equanimity_kind,shame_kind,caution_kind,nongreed_kind,nonhatred_kind,nonharming_kind,vigor_kind}
UniversalKind => {feeling_kind,volition_kind,reflection_kind,wish_kind,contact_kind,comprehension_kind,mindfulness_kind,attention_kind,resolution_kind,concentration_kind}
Present => {(wholesome_moment,faith_kind),(wholesome_moment,heedfulness_kind),(wholesome_moment,pliancy_kind),(wholesome_moment,equanimity_kind),(wholesome_moment,shame_kind),(wholesome_moment,caution_kind),(wholesome_moment,nongreed_kind),(wholesome_moment,nonhatred_kind),(wholesome_moment,nonharming_kind),(wholesome_moment,vigor_kind),(wholesome_moment,feeling_kind),(wholesome_moment,volition_kind),(wholesome_moment,reflection_kind),(wholesome_moment,wish_kind),(wholesome_moment,contact_kind),(wholesome_moment,comprehension_kind),(wholesome_moment,mindfulness_kind),(wholesome_moment,attention_kind),(wholesome_moment,resolution_kind),(wholesome_moment,concentration_kind),(other_moment,feeling_kind),(other_moment,volition_kind),(other_moment,reflection_kind),(other_moment,wish_kind),(other_moment,contact_kind),(other_moment,comprehension_kind),(other_moment,mindfulness_kind),(other_moment,attention_kind),(other_moment,resolution_kind),(other_moment,concentration_kind)}
```

The modeled wholesome moment has twenty distinct kinds from the two
lists; this is a required subset, not an exclusive total. The other
moment witnesses narrower scope without asserting that no wholesome
factor can ever occur outside wholesome consciousness. The model
does not solve the attention/equanimity objection or equate a name
received through favorability with identity of nature.

## 9. Interpretive Note

**Translation note.** The commentary explains faith as clarity; heedfulness as cultivation of the wholesome; pliancy as workability; and equanimity as evenness. The two roots are non-greed and non-hatred. Non-delusion is prajñā, already included among the great-ground factors. It also distinguishes a name assigned by favor from a factor's nature. Definitions of shame, caution, non-harming, and vigor remain brief or deferred.

The ground is every wholesome consciousness. Not ten stages. Not a claim that these arise only when a skill is developed.

Faith has two reported definitions. They are not fused. Heedfulness is care toward the wholesome dharmas, not those dharmas again. Guarding is another wording.

The equanimity result is a recorded difficulty and a deferral. Different respects are not a demonstrated solution until the shared support is accounted for.

Shame and caution are not filled from later passages. Non-harming and vigor stay the brief local definitions.

In the Organon reading, Cognition governs Perception and Conception,
remaining distinct from consciousness and Mind. Discriminative
comprehension's presence in the universal list does not make every
consciousness wholesome or every examination correct. The wholesome
determination requires its own accompanying factors and scope.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_25
    a vak:Karika ;
    rdfs:label "VAK 2.25" ;
    vak:hasTopic vak:WholesomeGreatGround ;
    vak:belongsTo vak:Indriyanirdesa .

vak:WholesomeTen vak:inEveryWholesomeConsciousness true .
vak:EquanimityHere vak:distinctFrom vak:NeutralFeeling .

organon:VAK_2_25_Interpretation
    organon:distinguishes vak:WholesomeRange, vak:UniversalRange,
        vak:ReceivedDesignation, vak:FactorNature .
```
