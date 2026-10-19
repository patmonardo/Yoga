# VAK_2.29 — How Many in the Unwholesome

## 1. Sanskrit (Devanāgarī)

```sanskrit
आवेणिके त्वकुशले दृष्टियुक्ते च विंशतिः ।
क्लेशैश्चतुर्भिः क्रोधाद्यैः कौकृत्येनैकविंशतिः ॥ २.२९ ॥
```

## 2. Sanskrit (IAST)

```text
āveṇike tv akuśale dṛṣṭiyukte ca viṃśatiḥ /
kleśaiś caturbhiḥ krodhādyaiḥ kaukṛtyenaikaviṃśatiḥ // 2.29 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| āveṇike | loc. sg. n. | in the isolated |
| tu / ca | particles | contrast / coordination of the two twenty-count cases |
| akuśale | loc. sg. n. | in unwholesome consciousness |
| dṛṣṭi-yukte | loc. sg. n.; compound participle | associated with a view |
| viṃśatiḥ | nom. sg. f.; numeral | twenty |
| kleśaiḥ caturbhiḥ | instr. pl. m. | with one of four afflictions |
| krodha-ādyaiḥ | instr. pl. m.; compound | with one secondary beginning with anger |
| kaukṛtyena | instr. sg. n. | with regret |
| ekaviṃśatiḥ | nom. sg. f.; numeral | twenty-one |

The instrumentals distribute. Not one joint list.

Desire-Realm scope is carried from 2.28. Sandhi is opened for parsing.

```text
# tokens: āveṇike tu akuśale dṛṣṭiyukte ca viṃśatiḥ kleśaiḥ caturbhiḥ krodhādyaiḥ kaukṛtyena ekaviṃśatiḥ
```

## 4. Grammar

The two locative cases share twenty. The second line distributes
twenty-one across three kinds of single addition. Its four is the
number of alternative afflictions, not four simultaneous increments.
The prose identifies view as a specialization of an already counted
universal factor.

```nltk-fcfg
% start S
# tokens: āveṇike tu akuśale dṛṣṭiyukte ca viṃśatiḥ kleśaiḥ caturbhiḥ krodhādyaiḥ kaukṛtyena ekaviṃśatiḥ
S[SEM=<(?base & ?extra)>] -> BASE[SEM=?base] ADDITIONS[SEM=?extra]
BASE[SEM=<(LocalCount(isolated_case,?count) & LocalCount(view_case,?count))>] -> ISOLATED[CASE=loc] CONTRAST UNWHOLESOME[CASE=loc] VIEW[CASE=loc] AND TWENTY[CNT=20,SEM=?count]
ADDITIONS[SEM=<(LocalCount(four_case,?count) & LocalCount(secondary_case,?count) & LocalCount(regret_case,?count))>] -> AFFLICTIONS[CASE=ins] FOUR[CNT=4,READING=alternatives] SECONDARY[CASE=ins,READING=one] REGRET[CASE=ins] TWENTYONE[CNT=21,SEM=?count]
ISOLATED[CASE=loc] -> 'āveṇike'
CONTRAST -> 'tu'
UNWHOLESOME[CASE=loc] -> 'akuśale'
VIEW[CASE=loc] -> 'dṛṣṭiyukte'
AND -> 'ca'
TWENTY[CNT=20,SEM=<twenty>] -> 'viṃśatiḥ'
AFFLICTIONS[CASE=ins] -> 'kleśaiḥ'
FOUR[CNT=4,READING=alternatives] -> 'caturbhiḥ'
SECONDARY[CASE=ins,READING=one] -> 'krodhādyaiḥ'
REGRET[CASE=ins] -> 'kaukṛtyena'
TWENTYONE[CNT=21,SEM=<twentyone>] -> 'ekaviṃśatiḥ'
```

```nltk-dep
'viṃśatiḥ' -> 'āveṇike' | 'tu' | 'akuśale' | 'dṛṣṭiyukte' | 'ca'
'ekaviṃśatiḥ' -> 'kleśaiḥ' | 'krodhādyaiḥ' | 'kaukṛtyena'
'kleśaiḥ' -> 'caturbhiḥ'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 6) | `BASE` | isolated and view-associated cases, twenty each |
| [6, 11) | `ADDITIONS` | alternative single additions, twenty-one each |
| [0, 11) | `S` | local Desire-Realm unwholesome counts |

## 5. Translation

### Literal Translation

> In isolated unwholesome consciousness, and in unwholesome consciousness
> associated with a view, there are twenty. With one of the four
> afflictions, one of those beginning with anger, or regret, there are
> twenty-one.
### Bhāṣya-informed study translation

> In the Desire Realm, isolated unwholesome consciousness and unwholesome
> consciousness associated with a view each have twenty mental factors.
> With one of the four afflictions—attachment, hostility, conceit, or doubt—
> or one secondary affliction beginning with anger, or regret, the local
> count is twenty-one.
## 6. Philosophical Translation

> Isolated excludes another affliction such as attachment, not the
> established accompanying factors. View specializes discriminative
> comprehension and adds no new factor. A distinct associate does add
> one: identity and addition must be determined before counting.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| āveṇika | isolated | ignorance without another distinct affliction |
| dṛṣṭi-yukta | associated with a view | three named; unwholesome |
| prajñā-viśeṣa | a special form of discriminative comprehension | why the count does not rise |
| rāga, pratigha, māna, vicikitsā | attachment, hostility, conceit, doubt | the four; one at a time |
| krodhādi | secondary beginning with anger | one adds one |
| kaukṛtya | regret | the unwholesome case here |

Not every view is unwholesome. The obscured-indeterminate views are the next unit.

## 8. Logical Determination

**Kārikā, derived; local scope carried from 2.28.** Case constants
denote the stated Desire-Realm unwholesome configurations, not
every consciousness with a view or regret. The four-case constant
represents any one of the four named alternatives.

```nltk-sem
twenty_count : \c.LocalCount(c,twenty)
twentyone_count : \c.LocalCount(c,twentyone)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((LocalCount(isolated_case,twenty) & LocalCount(view_case,twenty)) & (LocalCount(four_case,twentyone) & LocalCount(secondary_case,twentyone) & LocalCount(regret_case,twentyone)))

# THEORY prose_inventory
# EXPECT prose_inventory T
all x.(BaseMember(x) <-> (UniversalKind(x) | AfflictionKind(x) | UnwholesomeKind(x) | ExaminationKind(x)))
all x.(ViewMember(x) <-> BaseMember(x))
all x.(AttachmentMember(x) <-> (BaseMember(x) | x = attachment))
all x.(RegretMember(x) <-> (BaseMember(x) | x = regret))
ViewRealizedAs(view_case,comprehension) & ViewMember(comprehension)

# THEORY rejected_view_is_extra_factor
# EXPECT rejected_view_is_extra_factor F
LocalCount(view_case,twentyone) & ViewMember(comprehension)

# THEORY rejected_isolated_has_only_ignorance
# EXPECT rejected_isolated_has_only_ignorance F
all x.(BaseMember(x) -> x = ignorance)

# THEORY rejected_all_four_are_one_increment
# EXPECT rejected_all_four_are_one_increment F
all x.(FourAffliction(x) -> AttachmentMember(x))
```

```nltk-valuation
isolated_case => isolated_unwholesome_desire
view_case => view_unwholesome_desire
four_case => single_affliction_unwholesome_desire
secondary_case => secondary_unwholesome_desire
regret_case => regret_unwholesome_desire
twenty => count_twenty
twentyone => count_twenty_one
comprehension => comprehension_kind
ignorance => delusion_kind
attachment => attachment_kind
regret => regret_kind
LocalCount => {(isolated_unwholesome_desire,count_twenty),(view_unwholesome_desire,count_twenty),(single_affliction_unwholesome_desire,count_twenty_one),(secondary_unwholesome_desire,count_twenty_one),(regret_unwholesome_desire,count_twenty_one)}
UniversalKind => {feeling,volition,reflection,wish,contact,comprehension_kind,mindfulness,attention,resolution,concentration}
AfflictionKind => {delusion_kind,heedlessness,laziness,faithlessness,sluggishness,agitation}
UnwholesomeKind => {shamelessness,lack_caution}
ExaminationKind => {initial_examination,sustained_examination}
BaseMember => {feeling,volition,reflection,wish,contact,comprehension_kind,mindfulness,attention,resolution,concentration,delusion_kind,heedlessness,laziness,faithlessness,sluggishness,agitation,shamelessness,lack_caution,initial_examination,sustained_examination}
ViewMember => {feeling,volition,reflection,wish,contact,comprehension_kind,mindfulness,attention,resolution,concentration,delusion_kind,heedlessness,laziness,faithlessness,sluggishness,agitation,shamelessness,lack_caution,initial_examination,sustained_examination}
AttachmentMember => {feeling,volition,reflection,wish,contact,comprehension_kind,mindfulness,attention,resolution,concentration,delusion_kind,heedlessness,laziness,faithlessness,sluggishness,agitation,shamelessness,lack_caution,initial_examination,sustained_examination,attachment_kind}
RegretMember => {feeling,volition,reflection,wish,contact,comprehension_kind,mindfulness,attention,resolution,concentration,delusion_kind,heedlessness,laziness,faithlessness,sluggishness,agitation,shamelessness,lack_caution,initial_examination,sustained_examination,regret_kind}
ViewRealizedAs => {(view_unwholesome_desire,comprehension_kind)}
FourAffliction => {attachment_kind,hostility_kind,conceit_kind,doubt_kind}
SecondaryExample => {anger_kind}
```

The inventories check twenty and single additions to twenty-one.
Tests instantiate all four afflictions, an anger example, and regret
independently. The view-associated inventory retains the same twenty,
with comprehension qualified rather than duplicated. These are
local counts before later additions such as torpor, not universal
ceilings or proofs of the underlying factor identities.

## 9. Interpretive Note

**Translation note.** The commentary treats a view as a special form of prajñā already counted among universal factors, so specialization adds no factor. The instrumentals distribute among alternative single additions, not one combined set. It identifies the three views and distinguishes the unwholesome regret here from the wholesome case in 2.28; torpor is addressed later.

Ignorance alone does not remove heedlessness, laziness, lack of faith, sluggishness, and agitation. Those are the afflicted ground. The restriction is another affliction such as attachment.

The three views are wrong view, attachment to views, and attachment to rules and observances. Unwholesome is essential. Prajñā here is not liberating knowledge. A count of its occurrence is not adequacy.

Or distributes the four. Not twenty-four. The singular secondary controls the anger-group. Plurals in the verse are alternatives.

Regret here is the unwholesome case of 2.28. Not all regret is unwholesome. Torpor is a later addition. These totals do not rule it out.

In the Organon reading, Cognition governs Perception and Conception
without collapsing into consciousness or Mind. A view qualifies
discriminative comprehension, not Cognition as a new twenty-first
factor. Labels cannot decide whether a determination is an identity
or a distinct associate.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_29
    a vak:Karika ;
    rdfs:label "VAK 2.29" ;
    vak:hasTopic vak:UnwholesomeCount ;
    vak:belongsTo vak:Indriyanirdesa .

vak:IsolatedUnwholesome vak:hasCount 20 .
vak:ViewAssociated vak:hasCount 20 .
vak:AddedAssociate vak:hasCount 21 .

organon:VAK_2_29_Interpretation
    organon:distinguishes vak:FactorSpecialization, vak:DistinctAssociate,
        vak:LocalCount .
```
