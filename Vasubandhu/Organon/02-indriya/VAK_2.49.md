# VAK_2.49 — Six Causes

## 1. Sanskrit (Devanāgarī)

```sanskrit
कारणं सहभूश्चैव सभागः संप्रयुक्तकः ।
सर्वत्रगो विपाकाख्यः षड्विधो हेतुरिष्यते ॥ २.४९ ॥
```

## 2. Sanskrit (IAST)

```text
kāraṇaṃ sahabhūś caiva sabhāgaḥ saṃprayuktakaḥ /
sarvatrago vipākākhyaḥ ṣaḍvidho hetur iṣyate // 2.49 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| kāraṇam | neuter nominative singular | conditioning [cause]; first member of the sixfold list |
| sahabhūḥ | masculine nominative singular adjective | co-arisen |
| sabhāgaḥ | masculine nominative singular adjective | homogeneous |
| saṃprayuktakaḥ | masculine nominative singular adjective | associated |
| sarvatragaḥ | masculine nominative singular adjective | pervasive |
| vipāka-ākhyaḥ | masculine nominative singular compound adjective | called maturation |
| ṣaḍvidhaḥ hetuḥ | masculine nominative singular phrase | cause as sixfold; closes the enumeration |
| iṣyate | 3rd singular present passive | is held |

**Grammar tokens.** External sandhi is opened at *caiva* and *hetur iṣyate*; the six named cause-types remain distinct tokens. The Bhāṣya's definition of *kāraṇahetu* belongs to the prose, not to the verse parse.

```text
# tokens: kāraṇaṃ sahabhūḥ ca eva sabhāgaḥ saṃprayuktakaḥ sarvatragaḥ vipākākhyaḥ ṣaḍvidhaḥ hetuḥ iṣyate
```

## 4. Grammar

The first eight tokens enumerate six kinds, with *ca eva* joining and emphasizing the second. The masculine singular *ṣaḍvidhaḥ* agrees with *hetuḥ*; *iṣyate* reports that this sixfold classification is held. The grammar makes the six types exhaustive within this stated classification. It does not derive the definition of any one type from the verse.

```nltk-fcfg
% start S
# tokens: kāraṇaṃ sahabhūḥ ca eva sabhāgaḥ saṃprayuktakaḥ sarvatragaḥ vipākākhyaḥ ṣaḍvidhaḥ hetuḥ iṣyate
S[SEM=<(?names & ?six & ?head & ?held)>] -> NAMES[COUNT=6,SEM=?names] SIX[CASE=nom,NUM=sg,GEN=m,CNT=6,SEM=?six] HEAD[CASE=nom,NUM=sg,GEN=m,SEM=?head] HELD[SEM=?held]
NAMES[COUNT=6,SEM=<(?first & ?second & ?third & ?fourth & ?fifth & ?sixth)>] -> FIRST[CASE=nom,NUM=sg,GEN=n,SEM=?first] SECOND[CASE=nom,NUM=sg,GEN=m,SEM=?second] AND EMPH THIRD[CASE=nom,NUM=sg,GEN=m,SEM=?third] FOURTH[CASE=nom,NUM=sg,GEN=m,SEM=?fourth] FIFTH[CASE=nom,NUM=sg,GEN=m,SEM=?fifth] SIXTH[CASE=nom,NUM=sg,GEN=m,SEM=?sixth]
FIRST[CASE=nom,NUM=sg,GEN=n,SEM=<CauseKind(conditioning)>] -> 'kāraṇaṃ'
SECOND[CASE=nom,NUM=sg,GEN=m,SEM=<CauseKind(co_arisen)>] -> 'sahabhūḥ'
AND -> 'ca'
EMPH -> 'eva'
THIRD[CASE=nom,NUM=sg,GEN=m,SEM=<CauseKind(homogeneous)>] -> 'sabhāgaḥ'
FOURTH[CASE=nom,NUM=sg,GEN=m,SEM=<CauseKind(associated)>] -> 'saṃprayuktakaḥ'
FIFTH[CASE=nom,NUM=sg,GEN=m,SEM=<CauseKind(pervasive)>] -> 'sarvatragaḥ'
SIXTH[CASE=nom,NUM=sg,GEN=m,SEM=<CauseKind(maturation)>] -> 'vipākākhyaḥ'
SIX[CASE=nom,NUM=sg,GEN=m,CNT=6,SEM=<all x.(CauseKind(x) -> (x = conditioning | x = co_arisen | x = homogeneous | x = associated | x = pervasive | x = maturation))>] -> 'ṣaḍvidhaḥ'
HEAD[CASE=nom,NUM=sg,GEN=m,SEM=<SixfoldCauseAccount(cause_account)>] -> 'hetuḥ'
HELD[SEM=<Held(cause_account)>] -> 'iṣyate'
```

```nltk-dep
'hetuḥ' -> 'kāraṇaṃ' | 'sahabhūḥ' | 'sabhāgaḥ' | 'saṃprayuktakaḥ' | 'sarvatragaḥ' | 'vipākākhyaḥ' | 'ṣaḍvidhaḥ' | 'iṣyate'
'sahabhūḥ' -> 'ca' | 'eva'
```

**Feature chart checkpoints.** The six-name constituent spans [0, 8); *ṣaḍvidhaḥ hetuḥ iṣyate* spans [8, 11). At the root, the six names, exhaustive scope, sixfold cause-account, and reported status compose into one closed `SEM`. Count and nominative agreement constrain the parse.

| Span | Constituent | Result |
|---|---|
| [0, 8) | `NAMES[COUNT=6]` | six individually named cause-types |
| [8, 9) | `SIX[CNT=6]` | exhaustive scope within the named classification |
| [8, 11) | `SIX HEAD HELD` | a sixfold cause-account is held |
| [0, 11) | `S` | the six-type classification, without a cause-definition |

## 5. Translation

### Literal Translation

> Conditioning, co-arisen, homogeneous, associated, pervasive, and that
> called maturation: these are held to be the six causes.
### Bhāṣya-informed study translation

> Cause is held to be sixfold: conditioning, co-arisen, homogeneous,
> associated, pervasive, and that called maturation.
## 6. Philosophical Translation

> The six causes articulate distinct modes of grounding. The verse names their wheel; the Bhāṣya begins to explain how one mode, conditioning, bears on arising.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| hetu | cause | the sixfold classification is stated as held (*iṣyate*) |
| kāraṇa-hetu | conditioning cause | the first cause; Bhāṣya explains its broad non-obstruction toward what arises |
| sahabhū / sabhāga / saṃprayuktaka | co-arisen / homogeneous / associated | named here; defined in later units |
| sarvatraga / vipāka | pervasive / maturation | named here; defined in later units |
| avighna | non-obstruction | Bhāṣya specification concerning what is arising, not the verse's lexical definition |
| pradhāna kāraṇahetu | principal conditioning cause | can also produce, as in eye and form, food, and seed |
| kāraka | productive agency | not conferred on all conditioning causes by non-obstruction |
| kāraṇa-paraṃparā | succession of causes | the alternative account of mediated efficacy |

## 8. Logical Determination

**Kārikā, derived.** The root `SEM` states the six cause-types as a closed classification and registers *iṣyate* as reported acceptance. It says nothing yet about how each cause works. The Bhāṣya's first definition and the principal-cause examples are separate theories. A finite valuation tests this distinction; it does not prove the Sanskrit from the model.

```nltk-sem
sixfold : all x.(CauseKind(x) -> (x = conditioning | x = co_arisen | x = homogeneous | x = associated | x = pervasive | x = maturation))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((CauseKind(conditioning) & CauseKind(co_arisen) & CauseKind(homogeneous) & CauseKind(associated) & CauseKind(pervasive) & CauseKind(maturation)) & all x.(CauseKind(x) -> (x = conditioning | x = co_arisen | x = homogeneous | x = associated | x = pervasive | x = maturation)) & SixfoldCauseAccount(cause_account) & Held(cause_account))

# THEORY prose_non_obstruction
# EXPECT prose_non_obstruction T
Conditioned(arising_event) & Arising(arising_event)
all x.((Dharma(x) & -(x = arising_event)) -> ConditioningCauseFor(x,arising_event))
all x.(ConditioningCauseFor(x,arising_event) -> NonObstructs(x,arising_event))
-ConditioningCauseFor(arising_event,arising_event)

# THEORY prose_principal
# EXPECT prose_principal T
PrincipalFor(eye,eye_cognition) & PrincipalFor(visible_form,eye_cognition) & PrincipalFor(food,body) & PrincipalFor(seed,sprout)
all x.all y.(PrincipalFor(x,y) -> (ConditioningCauseFor(x,y) & Produces(x,y)))

# THEORY prose_actual_arising
# EXPECT prose_actual_arising T
WouldAriseWithoutKnowledge(influx) & Obstructs(knowledge,influx) & -Arising(influx)

# THEORY rejected_seven_causes
# EXPECT rejected_seven_causes F
CauseKind(seventh) & Held(cause_account)

# THEORY rejected_self_cause
# EXPECT rejected_self_cause F
ConditioningCauseFor(arising_event,arising_event) & Arising(arising_event)

# THEORY rejected_every_conditioning_cause_produces
# EXPECT rejected_every_conditioning_cause_produces F
all x.(ConditioningCauseFor(x,arising_event) -> Produces(x,arising_event))

# THEORY rejected_causes_are_four_conditions
# EXPECT rejected_causes_are_four_conditions F
all x.(CauseKind(x) -> ConditionKind(x))

# THEORY rejected_every_possible_event_arises
# EXPECT rejected_every_possible_event_arises F
all x.(WouldAriseWithoutKnowledge(x) -> Arising(x))
```

```nltk-valuation
conditioning => conditioning_kind
co_arisen => co_arisen_kind
homogeneous => homogeneous_kind
associated => associated_kind
pervasive => pervasive_kind
maturation => maturation_kind
seventh => seventh_kind
cause_account => six_cause_account
arising_event => arising_dharma
eye => eye_power
visible_form => visible_form_object
eye_cognition => eye_cognition_event
food => food_item
body => body_event
seed => seed_item
sprout => sprout_event
other_dharma => other_dharma_item
knowledge => knowledge_event
influx => obstructed_influx_event
CauseKind => {conditioning_kind,co_arisen_kind,homogeneous_kind,associated_kind,pervasive_kind,maturation_kind}
SixfoldCauseAccount => {six_cause_account}
Held => {six_cause_account}
Dharma => {arising_dharma,eye_power,visible_form_object,food_item,seed_item,other_dharma_item,knowledge_event}
Conditioned => {arising_dharma}
Arising => {arising_dharma}
ConditioningCauseFor => {(eye_power,arising_dharma),(visible_form_object,arising_dharma),(food_item,arising_dharma),(seed_item,arising_dharma),(other_dharma_item,arising_dharma),(knowledge_event,arising_dharma),(eye_power,eye_cognition_event),(visible_form_object,eye_cognition_event),(food_item,body_event),(seed_item,sprout_event)}
NonObstructs => {(eye_power,arising_dharma),(visible_form_object,arising_dharma),(food_item,arising_dharma),(seed_item,arising_dharma),(other_dharma_item,arising_dharma),(knowledge_event,arising_dharma)}
PrincipalFor => {(eye_power,eye_cognition_event),(visible_form_object,eye_cognition_event),(food_item,body_event),(seed_item,sprout_event)}
Produces => {(eye_power,eye_cognition_event),(visible_form_object,eye_cognition_event),(food_item,body_event),(seed_item,sprout_event)}
WouldAriseWithoutKnowledge => {obstructed_influx_event}
Obstructs => {(knowledge_event,obstructed_influx_event)}
ConditionKind => {}
```

The countermodels reject a seventh kind, self-causation, the transfer of productive agency to every conditioning cause, the treatment of every merely possible event as actually arising, and the identification of this six-cause list with the later four conditions. The principal and obstruction examples are Bhāṣya claims; the verse itself only names the six kinds.

## 9. Interpretive Note

**Translation note.** The Bhāṣya defines the conditioning cause as every
dharma other than itself, by non-obstruction toward what is arising. Some
principal cases also produce, including eye and visible Form, food, and
seed. Non-obstruction is not productive agency; another account gives causes
mediated efficacy through a succession of causes.

The first clause of the next verse states the conditioning-cause definition, then turns to the co-arisen cause. Here the Indriya inquiry moves from what governs to the causes of arising. The later four-condition account (2.61) will articulate *pratyaya*; this verse does not yet equate that account with the six causes. Reading this passage beside the relation of Indriya and *artha* belongs to the Organon synthesis, with the local cause distinctions intact.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_49 a vak:Karika ; vak:hasTopic vak:SixCauses .
vak:KaranaHetu vak:broad vak:NonObstruction .
```
