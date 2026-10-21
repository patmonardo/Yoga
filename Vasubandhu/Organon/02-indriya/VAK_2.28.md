# VAK_2.28 — How Many in the Wholesome

## 1. Sanskrit (Devanāgarī)

```sanskrit
सवितर्कविचारत्वात् कुशले कामचेतसि ।
द्वाविंशतिश्चैतसिकाः कौकृत्यमधिकं क्वचित् ॥ २.२८ ॥
```

## 2. Sanskrit (IAST)

```text
savitarkavicāratvāt kuśale kāmacetasi /
dvāviṃśatiś caitasikāḥ kaukṛtyam adhikaṃ kvacit // 2.28 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sa-vitarka-vicāratvāt | abl. sg. n.; abstract compound in -tva | because accompanied by initial and sustained examination |
| kuśale kāma-cetasi | loc. sg. n. + loc. sg. n. | in wholesome Desire Realm consciousness |
| dvāviṃśatiḥ | nom. sg. f.; numeral | twenty-two |
| caitasikāḥ | nom. pl. m. | mental factors |
| kaukṛtyam | nom. sg. n. | regret |
| adhikam kvacit | adjective + adverb | additional, in some cases |

Kvacit keeps regret out of the wholesome ground. Consciousness itself is not one of the twenty-two.

The two examination factors are counted within twenty-two, not
added to it. External sandhi is opened for parsing.

```text
# tokens: savitarkavicāratvāt kuśale kāmacetasi dvāviṃśatiḥ caitasikāḥ kaukṛtyam adhikam kvacit
```

## 4. Grammar

The ablative gives the reason for the two additions to the inherited
ten-plus-ten. The two locatives jointly restrict the base count and
the conditional addition. `Kvacit` requires at least one local case
with regret; it does not make regret universal or deliberately chosen.
The twenty-third count is supplied by the Bhāṣya.

```nltk-fcfg
% start S
# tokens: savitarkavicāratvāt kuśale kāmacetasi dvāviṃśatiḥ caitasikāḥ kaukṛtyam adhikam kvacit
S[SEM=<(?base & ?addition)>] -> BASE[SEM=?base] ADDITION[SEM=?addition]
BASE[SEM=<all c.(WholesomeDesireMoment(c) -> (InitialExamination(c) & SustainedExamination(c) & BaseCount(c,?count)))>] -> REASON[CASE=abl,PAIR=included] WHOLESOME[CASE=loc] DESIRE[CASE=loc] TWENTYTWO[CNT=22,SEM=?count] FACTORS[CASE=nom,NUM=pl]
ADDITION[SEM=<(all c.((WholesomeDesireMoment(c) & ?regret(c)) -> ?extra(c)) & ?sometimes(\c.(?regret(c) & ?extra(c))))>] -> REGRET[CASE=nom,SEM=?regret] EXTRA[MODE=addition,SUPPLIED=prose_count,SEM=?extra] SOMETIMES[SCOPE=some_cases,SEM=?sometimes]
REASON[CASE=abl,PAIR=included] -> 'savitarkavicāratvāt'
WHOLESOME[CASE=loc] -> 'kuśale'
DESIRE[CASE=loc] -> 'kāmacetasi'
TWENTYTWO[CNT=22,SEM=<twentytwo>] -> 'dvāviṃśatiḥ'
FACTORS[CASE=nom,NUM=pl] -> 'caitasikāḥ'
REGRET[CASE=nom,SEM=<\c.RegretPresent(c)>] -> 'kaukṛtyam'
EXTRA[MODE=addition,SUPPLIED=prose_count,SEM=<\c.LocalCount(c,twentythree)>] -> 'adhikam'
SOMETIMES[SCOPE=some_cases,SEM=<\P.exists c.(WholesomeDesireMoment(c) & P(c))>] -> 'kvacit'
```

```nltk-dep
'caitasikāḥ' -> 'savitarkavicāratvāt' | 'kuśale' | 'kāmacetasi' | 'dvāviṃśatiḥ'
'kaukṛtyam' -> 'adhikam' | 'kvacit'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 5) | `BASE` | wholesome Desire-Realm twenty-two, including the examination pair |
| [5, 8) | `ADDITION` | regret additional only where present in that scope |
| [0, 8) | `S` | necessary base and conditional increment |

## 5. Translation

### Literal Translation

> In wholesome Desire Realm consciousness, because it is accompanied by
> initial and sustained examination, there are twenty-two mental factors; regret may be
> additional in some cases.

### Bhāṣya-informed study translation

> In wholesome Desire-Realm consciousness, twenty-two mental factors
> necessarily occur: the ten universal factors, the ten wholesome factors,
> and initial and sustained examination. In some cases regret is additional,
> making twenty-three where it is present.

## 6. Philosophical Translation

> The necessary inventory is inherited ten plus ten and the examination
> pair. Regret is a conditional addition, not a universal wholesome
> factor. Its name can be transferred from its Cognitive Condition
> or, alternatively, from cause to effect; the deed is not the factor.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| kāma-cetas | Desire Realm consciousness | with initial and sustained examination |
| vitarka, vicāra | initial and sustained examination | counted; definitions deferred |
| kaukṛtya | regret | the factor, not the deed |
| vipratisāra | regret in consciousness | the definition |
| kukṛta | badly done | the basis |
| hetūpacāra | cause's name on the effect | the alternative |
| ubhayādhiṣṭhāna | twofold basis | done and not done |
| āveṇika | isolated | not explained until 2.29 |

## 8. Logical Determination

**Kārikā with prose-resolved counts.** BaseCount is the necessary
twenty-two. `Kvacit` supplies an existential case with regret, and
LocalCount records its Bhāṣya-resolved increment. This local count is
not an exclusive ceiling over every later-qualified episode.

```nltk-sem
base_scope : \P.all c.(WholesomeDesireMoment(c) -> P(c))
regret_increment : \c.((WholesomeDesireMoment(c) & RegretPresent(c)) -> LocalCount(c,twentythree))
some_case : \P.exists c.(WholesomeDesireMoment(c) & P(c))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all c.(WholesomeDesireMoment(c) -> (InitialExamination(c) & SustainedExamination(c) & BaseCount(c,twentytwo))) & all c.((WholesomeDesireMoment(c) & RegretPresent(c)) -> LocalCount(c,twentythree)) & exists c.(WholesomeDesireMoment(c) & RegretPresent(c) & LocalCount(c,twentythree)))

# THEORY prose_inventory
# EXPECT prose_inventory T
all f.(BaseMember(f) <-> (UniversalKind(f) | WholesomeKind(f) | ExaminationKind(f)))
all c f.((WholesomeDesireMoment(c) & BaseMember(f)) -> Present(c,f))
all c.(WholesomeDesireMoment(c) -> (RegretPresent(c) <-> Present(c,regret)))
exists c.(WholesomeDesireMoment(c) & RegretPresent(c))
exists c.(WholesomeDesireMoment(c) & -RegretPresent(c))

# THEORY rejected_regret_in_every_wholesome_moment
# EXPECT rejected_regret_in_every_wholesome_moment F
all c.(WholesomeDesireMoment(c) -> RegretPresent(c))

# THEORY rejected_regret_always_means_twenty_three
# EXPECT rejected_regret_always_means_twenty_three F
all c.(RegretPresent(c) -> LocalCount(c,twentythree))

# THEORY rejected_examination_pair_outside_twenty_two
# EXPECT rejected_examination_pair_outside_twenty_two F
all f.(ExaminationKind(f) -> -BaseMember(f))
```

```nltk-valuation
twentytwo => count_twenty_two
twentythree => count_twenty_three
regret => regret_kind
WholesomeDesireMoment => {base_moment,regret_moment}
InitialExamination => {base_moment,regret_moment}
SustainedExamination => {base_moment,regret_moment}
BaseCount => {(base_moment,count_twenty_two),(regret_moment,count_twenty_two)}
RegretPresent => {regret_moment,unwholesome_regret_moment}
LocalCount => {(base_moment,count_twenty_two),(regret_moment,count_twenty_three)}
UniversalKind => {feeling,volition,reflection,wish,contact,comprehension,mindfulness,attention,resolution,concentration}
WholesomeKind => {faith,heedfulness,pliancy,equanimity,shame,caution,nongreed,nonhatred,nonharming,vigor}
ExaminationKind => {initial_examination,sustained_examination}
BaseMember => {feeling,volition,reflection,wish,contact,comprehension,mindfulness,attention,resolution,concentration,faith,heedfulness,pliancy,equanimity,shame,caution,nongreed,nonhatred,nonharming,vigor,initial_examination,sustained_examination}
Present => {(base_moment,feeling),(base_moment,volition),(base_moment,reflection),(base_moment,wish),(base_moment,contact),(base_moment,comprehension),(base_moment,mindfulness),(base_moment,attention),(base_moment,resolution),(base_moment,concentration),(base_moment,faith),(base_moment,heedfulness),(base_moment,pliancy),(base_moment,equanimity),(base_moment,shame),(base_moment,caution),(base_moment,nongreed),(base_moment,nonhatred),(base_moment,nonharming),(base_moment,vigor),(base_moment,initial_examination),(base_moment,sustained_examination),(regret_moment,feeling),(regret_moment,volition),(regret_moment,reflection),(regret_moment,wish),(regret_moment,contact),(regret_moment,comprehension),(regret_moment,mindfulness),(regret_moment,attention),(regret_moment,resolution),(regret_moment,concentration),(regret_moment,faith),(regret_moment,heedfulness),(regret_moment,pliancy),(regret_moment,equanimity),(regret_moment,shame),(regret_moment,caution),(regret_moment,nongreed),(regret_moment,nonhatred),(regret_moment,nonharming),(regret_moment,vigor),(regret_moment,initial_examination),(regret_moment,sustained_examination),(regret_moment,regret_kind)}
```

The external unwholesome-regret example witnesses a scope error:
regret alone does not imply this verse's twenty-three. Its full
inventory is left unmodeled, not assigned a default count. These
finite inventories test 10 + 10 + 2 and the conditional +1, not the
adequacy of every factor definition or all later additions.

## 9. Interpretive Note

**Translation note.** The commentary enumerates the twenty-two as the ten universal, ten wholesome, vitarka, and vicāra. It explains kaukṛtya through the badly done, while also considering naming through the Cognitive Condition and from cause to effect. Wholesome regret may follow failure to do the wholesome or doing the unwholesome; kvacit marks its unfixed occurrence.

Five cases are announced. This verse is the wholesome one. Isolated is not consciousness without factors. Obscured and unobscured stay apart. Twenty-two faculties were another count. These are mental factors.

Kvacit is the unfixed of 2.27 made local. Regret can be wholesome and still not be in every wholesome consciousness. Further additions may be stated later. This is the local rule.

Two accounts of the name stay alternatives: naming through the
Cognitive Condition, and the cause's name applied to the effect. The direction of the second is from cause to effect. Omission is included without pretending the omitted deed occurred.

In the Organon reading, Cognition governs Perception and Conception
without collapsing into consciousness or Mind. The present inventory
counts mental factors accompanying consciousness, not Cognition
as a twenty-third member. The deed and the regret directed toward
it also remain distinct.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_28
    a vak:Karika ;
    rdfs:label "VAK 2.28" ;
    vak:hasTopic vak:WholesomeDesireCount ;
    vak:belongsTo vak:Indriyanirdesa .

vak:WholesomeDesireCount vak:hasBaseCount 22 .
vak:Regret vak:sometimesAdditional true .

organon:VAK_2_28_Interpretation
    organon:distinguishes vak:NecessaryInventory, vak:ConditionalAddition,
        vak:RegretFactor, vak:RegrettedDeed .
```
