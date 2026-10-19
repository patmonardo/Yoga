# VAK_2.46 — Secondary Marks, and the Restriction

## 1. Sanskrit (Devanāgarī)

```sanskrit
जातिजात्यादयस्तेषां तेऽष्टधर्मैकवृत्तयः ।
जन्यस्य जनिका जातिर्न हेतुप्रत्ययैर्विना ॥ २.४६ ॥
```

## 2. Sanskrit (IAST)

```text
jātijātyādayas teṣāṃ te 'ṣṭadharmaikavṛttayaḥ /
janyasya janikā jātir na hetupratyayair vinā // 2.46 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| jāti-jāti-ādayaḥ | nom. pl. m.; compound | arising-of-arising and the rest |
| teṣām | gen. pl. m. | of those primary marks |
| te | nom. pl. m.; pronoun | the primary and secondary marks, distributed respectively |
| aṣṭa-dharma-eka-vṛttayaḥ | nom. pl. m.; compound adjective | operating on eight, and on one |
| janyasya | gen. sg. n.; past passive participle | of what is to be generated |
| janikā | nom. sg. f. | the generator |
| jātiḥ | nom. sg. f. | arising, the proposed generator |
| na vinā | negation + preposition governing instrumental | not without |
| hetu-pratyayaiḥ | instr. pl. m.; compound | causes and conditions |

Operation is activity, efficacy. Not a third synonym for the mark.

```text
# tokens: jātijātyādayaḥ teṣām te aṣṭadharmaikavṛttayaḥ janyasya janikā jātiḥ na hetupratyayaiḥ vinā
```
## 4. Grammar

The first clause supplies the secondary marks of the four primary
marks. The compound distributes operation: each primary operates
on the other eight members of a nine-member group, each secondary
on its corresponding primary alone. The final instrumental
restriction makes the conjunction of causes and Conditions
necessary for the proposed arising-entity's generating activity;
it does not assert that this entity alone suffices.

```nltk-fcfg
% start S
# tokens: jātijātyādayaḥ teṣām te aṣṭadharmaikavṛttayaḥ janyasya janikā jātiḥ na hetupratyayaiḥ vinā
S[SEM=<(?secondary & ?operation & ?restriction)>] -> SECONDARIES[SEM=?secondary] OPERATIONS[SEM=?operation] RESTRICTION[SEM=?restriction]
SECONDARIES[SEM=<(SecondaryOf(arising_secondary,arising) & SecondaryOf(persistence_secondary,persistence) & SecondaryOf(aging_secondary,aging) & SecondaryOf(impermanence_secondary,impermanence))>] -> SECONDARYLIST[CASE=nom,NUM=pl] OFTHESE[CASE=gen,REF=primary_marks]
OPERATIONS[SEM=<(all x y.((Primary(x) & GroupMember(y) & -(x = y)) -> OperatesOn(x,y)) & all x y.(SecondaryOf(x,y) -> OperatesOn(x,y)))>] -> THEY[REF=both_mark_sets] EIGHTONE[PRIMARY=8,SECONDARY=1]
RESTRICTION[SEM=<all x.(Generates(arising,x) -> CauseConditionConjunction(x))>] -> GENERAND[CASE=gen] GENERATOR[CASE=nom] ARISING[CASE=nom] NOT CAUSES[CASE=ins,NUM=pl] WITHOUT[REQUIRES=conjunction]
SECONDARYLIST[CASE=nom,NUM=pl] -> 'jātijātyādayaḥ'
OFTHESE[CASE=gen,REF=primary_marks] -> 'teṣām'
THEY[REF=both_mark_sets] -> 'te'
EIGHTONE[PRIMARY=8,SECONDARY=1] -> 'aṣṭadharmaikavṛttayaḥ'
GENERAND[CASE=gen] -> 'janyasya'
GENERATOR[CASE=nom] -> 'janikā'
ARISING[CASE=nom] -> 'jātiḥ'
NOT -> 'na'
CAUSES[CASE=ins,NUM=pl] -> 'hetupratyayaiḥ'
WITHOUT[REQUIRES=conjunction] -> 'vinā'
```

```nltk-dep
'jātijātyādayaḥ' -> 'teṣām'
'aṣṭadharmaikavṛttayaḥ' -> 'te'
'jātiḥ' -> 'janyasya' | 'janikā' | 'vinā'
'vinā' -> 'na' | 'hetupratyayaiḥ'
```

The three constituent lengths are 2, 2, and 6. The finite model
represents the proposed operation scheme, not a proof of the
marks' reality. Its exact target sets are regression-tested.

## 5. Translation

### Literal Translation

> The marks of arising and the rest have marks of their own. The primary
> marks operate on eight dharmas, the secondary on one. Arising generates
> what is to be generated, not without causes and conditions.
### Bhāṣya-informed study translation

> Arising-of-arising and the rest belong to those [primary marks]. The
> primary marks operate on eight dharmas, the secondary on one. Arising
> generates what is to be generated only with causes and Conditions.
## 6. Philosophical Translation

> Primary operate on eight, secondary on one. The stipulation stops the regress; it does not show the entities. Arising generates only with causes and conditions. The power seen is the conjunction. Arising is the transition, not a producer beside it. The marks are maintained as real. Not settled.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| anulakṣaṇa | secondary mark | of the primary |
| vṛtti | operation | efficacy |
| janikā | generator | the claimed role |
| hetu-pratyaya | causes and Conditions | the conjunction required for generation |
| abhūtvā-bhāva | existing after not existing | the critical definition |
| prajñapti | designation | not imaginary |

## 8. Logical Determination

```nltk-sem
primary_operation : all x y.((Primary(x) & GroupMember(y) & -(x = y)) -> OperatesOn(x,y))
causal_restriction : all x.(Generates(arising,x) -> CauseConditionConjunction(x))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((SecondaryOf(arising_secondary,arising) & SecondaryOf(persistence_secondary,persistence) & SecondaryOf(aging_secondary,aging) & SecondaryOf(impermanence_secondary,impermanence)) & (all x y.((Primary(x) & GroupMember(y) & -(x = y)) -> OperatesOn(x,y)) & all x y.(SecondaryOf(x,y) -> OperatesOn(x,y))) & all x.(Generates(arising,x) -> CauseConditionConjunction(x)))

# THEORY restricted_operation_scheme
# EXPECT restricted_operation_scheme T
all x y.(OperatesOn(x,y) <-> ((Primary(x) & GroupMember(y) & -(x = y)) | SecondaryOf(x,y)))
exists x.Generates(arising,x)
exists x.(Candidate(x) & -CauseConditionConjunction(x) & -Generates(arising,x))

# THEORY reported_ontology_dispute
# EXPECT reported_ontology_dispute T
DistinctMarkEntities(vaibhasika_account) & -DistinctMarkEntities(sautrantika_account)
StreamInterpretation(sautrantika_account) & MaintainsDoctrine(vaibhasika_account)

# THEORY rejected_self_operation
# EXPECT rejected_self_operation F
exists x.(Primary(x) & OperatesOn(x,x))

# THEORY rejected_secondary_operates_on_all_eight
# EXPECT rejected_secondary_operates_on_all_eight F
all x y.((Secondary(x) & GroupMember(y) & -(x = y)) -> OperatesOn(x,y))

# THEORY rejected_generates_without_conjunction
# EXPECT rejected_generates_without_conjunction F
exists x.(Generates(arising,x) & -CauseConditionConjunction(x))
```

```nltk-valuation
arising => arising_primary
persistence => persistence_primary
aging => aging_primary
impermanence => impermanence_primary
arising_secondary => arising_secondary_token
persistence_secondary => persistence_secondary_token
aging_secondary => aging_secondary_token
impermanence_secondary => impermanence_secondary_token
vaibhasika_account => vaibhasika_position
sautrantika_account => stream_account_position
Primary => {arising_primary,persistence_primary,aging_primary,impermanence_primary}
Secondary => {arising_secondary_token,persistence_secondary_token,aging_secondary_token,impermanence_secondary_token}
GroupMember => {base_dharma,arising_primary,persistence_primary,aging_primary,impermanence_primary,arising_secondary_token,persistence_secondary_token,aging_secondary_token,impermanence_secondary_token}
SecondaryOf => {(arising_secondary_token,arising_primary),(persistence_secondary_token,persistence_primary),(aging_secondary_token,aging_primary),(impermanence_secondary_token,impermanence_primary)}
OperatesOn => {(arising_primary,base_dharma),(arising_primary,persistence_primary),(arising_primary,aging_primary),(arising_primary,impermanence_primary),(arising_primary,arising_secondary_token),(arising_primary,persistence_secondary_token),(arising_primary,aging_secondary_token),(arising_primary,impermanence_secondary_token),(persistence_primary,base_dharma),(persistence_primary,arising_primary),(persistence_primary,aging_primary),(persistence_primary,impermanence_primary),(persistence_primary,arising_secondary_token),(persistence_primary,persistence_secondary_token),(persistence_primary,aging_secondary_token),(persistence_primary,impermanence_secondary_token),(aging_primary,base_dharma),(aging_primary,arising_primary),(aging_primary,persistence_primary),(aging_primary,impermanence_primary),(aging_primary,arising_secondary_token),(aging_primary,persistence_secondary_token),(aging_primary,aging_secondary_token),(aging_primary,impermanence_secondary_token),(impermanence_primary,base_dharma),(impermanence_primary,arising_primary),(impermanence_primary,persistence_primary),(impermanence_primary,aging_primary),(impermanence_primary,arising_secondary_token),(impermanence_primary,persistence_secondary_token),(impermanence_primary,aging_secondary_token),(impermanence_primary,impermanence_secondary_token),(arising_secondary_token,arising_primary),(persistence_secondary_token,persistence_primary),(aging_secondary_token,aging_primary),(impermanence_secondary_token,impermanence_primary)}
Candidate => {ready_case,unready_case}
Generates => {(arising_primary,ready_case)}
CauseConditionConjunction => {ready_case}
DistinctMarkEntities => {vaibhasika_position}
StreamInterpretation => {stream_account_position}
MaintainsDoctrine => {vaibhasika_position}
```

Operation and causally conditioned generation are separate predicates:
the first records the nine-member scheme, the second illustrates
the causal restriction without asserting that all future dharmas
arise together. The ready/unready cases are illustrative, not an
exhaustive causal theory or a sufficiency proof. The Sautrāntika
and Vaibhāṣika positions are indexed rather than merged.

## 9. Interpretive Note

**Translation note.** The commentary lists arising-of-arising, persistence-of-persistence, aging-of-aging, and impermanence-of-impermanence, then uses the eight/one distinction to block an endless regress: arising generates eight, its secondary mark generates one. It explains generation through conjunction of causes and conditions and records, without settling, the dispute over whether the marks are real entities.

The full unit ends at 80.11, not 79.18. Between the two halves
of the verse stand the Sautrāntika stream account and objections
concerning temporal activity, simultaneous persistence/destruction,
and aging. The causal restriction then receives a further critique
of explanatory redundancy and grammatical inference. The
Vaibhāṣikas maintain the distinct entities at the close.

In the Organon reading, Cognition joins and governs Perception and
Conception and guides the Dharma Base, remaining distinct from
consciousness and Mind. A closed operation scheme can answer a
regress objection without establishing its entities. Likewise,
the grammar of a genitive relation cannot alone decide whether
its terms name two distinct real entities.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_46 a vak:Karika ; vak:hasTopic vak:ArisingRestriction .
vak:MarkEntity vak:settled false .
```
