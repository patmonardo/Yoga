# VAK_2.22 — What Arises Together

## 1. Sanskrit (Devanāgarī)

```sanskrit
कामेऽष्टद्रव्यकोऽशब्दः परमाणुरनिन्द्रियः ।
कायेन्द्रियी नवद्रव्यः दशद्रव्योऽपरेन्द्रियः ॥ २.२२ ॥
```

## 2. Sanskrit (IAST)

```text
kāme 'ṣṭadravyako 'śabdaḥ paramāṇur anindriyaḥ /
kāyendriyī navadravyaḥ daśadravyo 'parendriyaḥ // 2.22 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| kāme | locative singular masculine | in the Desire Realm; scope of all three verse counts |
| aṣṭa-dravyakaḥ | nominative singular masculine numeral compound adjective | consisting of eight constituents |
| a-śabdaḥ | nominative singular masculine privative adjective | without sound; carried through the nine and ten |
| paramāṇuḥ | nominative singular masculine noun | minimal cluster, explicitly glossed as the subtlest Form-cluster |
| an-indriyaḥ | nominative singular masculine privative adjective | without a Faculty |
| kāyendriyī | nominative singular masculine possessive adjective in -in | possessing the body-Faculty |
| nava-dravyaḥ | nominative singular masculine numeral compound adjective | consisting of nine constituents |
| daśa-dravyaḥ | nominative singular masculine numeral compound adjective | consisting of ten constituents |
| apara-indriyaḥ | nominative singular masculine possessive compound | possessing another Faculty in addition to body: one of eye, ear, nose, tongue |

Dravya is rendered constituent; the prose examines the mixed counting unit rather than treating it as unproblematic substance. Sandhi is opened for the grammar.

```text
# tokens: kāme aṣṭadravyakaḥ aśabdaḥ paramāṇuḥ anindriyaḥ kāyendriyī navadravyaḥ daśadravyaḥ aparendriyaḥ
```

## 4. Grammar

The locative and soundless qualification govern all three clauses. Their lexical SEM values are shared across the three constituents. The subject minimal cluster is carried into the last two. Another Faculty does not replace body: the prose says those same nine plus one of the four named Faculties. Sound-bearing cases are prose extensions, not a fourth clause in the verse.

```nltk-fcfg
% start S
# tokens: kāme aṣṭadravyakaḥ aśabdaḥ paramāṇuḥ anindriyaḥ kāyendriyī navadravyaḥ daśadravyaḥ aparendriyaḥ
S[SEM=<(?first & ?body & ?other)>] -> FIRST[SEM=?first] BODYCASE[SEM=?body] OTHERCASE[SEM=?other]
FIRST[SEM=<DesireRule(base_cluster) & Soundless(base_cluster) & NoFaculty(base_cluster) & Count(base_cluster,eight)>] -> REALM EIGHT SOUNDLESS CLUSTER NONE
REALM -> 'kāme'
EIGHT -> 'aṣṭadravyakaḥ'
SOUNDLESS -> 'aśabdaḥ'
CLUSTER -> 'paramāṇuḥ'
NONE -> 'anindriyaḥ'
BODYCASE[SEM=<DesireRule(body_cluster) & Soundless(body_cluster) & BodyBearing(body_cluster) & Count(body_cluster,nine)>] -> BODY NINE
BODY -> 'kāyendriyī'
NINE -> 'navadravyaḥ'
OTHERCASE[SEM=<DesireRule(other_cluster) & Soundless(other_cluster) & BodyBearing(other_cluster) & OtherBearing(other_cluster) & Count(other_cluster,ten)>] -> TEN OTHER
TEN -> 'daśadravyaḥ'
OTHER -> 'aparendriyaḥ'
```

```nltk-dep
'paramāṇuḥ' -> 'kāme' | 'aṣṭadravyakaḥ' | 'aśabdaḥ' | 'anindriyaḥ' | 'kāyendriyī' | 'aparendriyaḥ'
'kāyendriyī' -> 'navadravyaḥ'
'aparendriyaḥ' -> 'daśadravyaḥ'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 5) | `FIRST` | soundless, Faculty-free Desire-Realm eight |
| [5, 7) | `BODYCASE` | same scope, body added, nine |
| [7, 9) | `OTHERCASE` | same scope, body and one other Faculty, ten |

## 5. Translation

### Literal Translation

> In the Desire Realm, a soundless minimal cluster without a Faculty consists of eight constituents. One possessing the body-Faculty consists of nine. One possessing another Faculty consists of ten.

### Bhāṣya-informed study translation

> In the Desire Realm, a soundless minimal Form-cluster without a Faculty has eight constituents. A soundless cluster with the body-Faculty has nine; with body and one other Faculty—eye, ear, nose, or tongue—it has ten.

## 6. Philosophical Translation

> Distinct characteristics do not require separate arising. The soundless eight, nine, and ten count differently qualified minimal Form-clusters; the number remains answerable to its counting unit.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| niyata-sahotpāda | necessary co-arising | the new question |
| paramāṇu | minimal cluster | most subtle cluster |
| dravya | constituent | not substance |
| mahābhūta | Great Element | Earth, Water, Fire, Wind |
| upādāya-rūpa | Element-dependent Form | the four in the eight |
| aparendriya | another faculty | eye, ear, nose, or tongue |
| upātta-mahābhūta-hetuka | caused by appropriated Great Elements | the sound that can conjoin |

## 8. Logical Determination

**Kārikā, derived.** The locative and privative adjectives supply shared Desire-Realm and soundless scopes to every clause. The prose inventories below are constituent-kind counts, not numbers of individual particles or Essences. Sound adds one only to the qualified configurations.

```nltk-sem
realm_scope : DesireRule(base_cluster)
soundless_scope : Soundless(base_cluster)
eight_count : Count(base_cluster,eight)
nine_count : Count(body_cluster,nine)
ten_count : Count(other_cluster,ten)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(DesireRule(base_cluster) & Soundless(base_cluster) & NoFaculty(base_cluster) & Count(base_cluster,eight) & DesireRule(body_cluster) & Soundless(body_cluster) & BodyBearing(body_cluster) & Count(body_cluster,nine) & DesireRule(other_cluster) & Soundless(other_cluster) & BodyBearing(other_cluster) & OtherBearing(other_cluster) & Count(other_cluster,ten))

# THEORY prose_members
# EXPECT prose_members T
all x.(BaseMember(x) <-> (GreatElement(x) | DependentFour(x)))
all x.(BodyMember(x) <-> (BaseMember(x) | x = body_f))
all x.(OtherMember(x) <-> (BodyMember(x) | x = eye_f))
all x.(SoundOtherMember(x) <-> (OtherMember(x) | x = sound_f))

# THEORY rejected_other_replaces_body
# EXPECT rejected_other_replaces_body F
all x.(OtherMember(x) <-> (BaseMember(x) | x = eye_f))

# THEORY rejected_sound_already_in_eight
# EXPECT rejected_sound_already_in_eight F
BaseMember(sound_f) & Soundless(base_cluster)

# THEORY rejected_tangible_means_only_great_elements
# EXPECT rejected_tangible_means_only_great_elements F
all x.(DependentFour(x) -> GreatElement(x))
```

```nltk-valuation
base_cluster => soundless_base
body_cluster => soundless_body
other_cluster => soundless_eye
eight => count_eight
nine => count_nine
ten => count_ten
body_f => body
eye_f => eye
sound_f => sound
DesireRule => {soundless_base,soundless_body,soundless_eye}
Soundless => {soundless_base,soundless_body,soundless_eye}
NoFaculty => {soundless_base}
BodyBearing => {soundless_body,soundless_eye}
OtherBearing => {soundless_eye}
Count => {(soundless_base,count_eight),(soundless_body,count_nine),(soundless_eye,count_ten)}
GreatElement => {earth,water,fire,wind}
DependentFour => {visible,odor,taste,dependent_tangible}
BaseMember => {earth,water,fire,wind,visible,odor,taste,dependent_tangible}
BodyMember => {earth,water,fire,wind,visible,odor,taste,dependent_tangible,body}
OtherMember => {earth,water,fire,wind,visible,odor,taste,dependent_tangible,body,eye}
SoundOtherMember => {earth,water,fire,wind,visible,odor,taste,dependent_tangible,body,eye,sound}
```

Eye is one representative of the four alternatives, not their joint addition. Persistent tests instantiate all four and sound's three increments. The Form-Realm six/seven/eight removes odor and taste under its own scope; it does not contradict the Desire-Realm eight. These inventories check the numerical accounting, not the disputed physical presence of every constituent or the seed alternative.

## 9. Interpretive Note

**Translation note.** The study translation supplies the prose's Form-cluster gloss, carries soundlessness through all three cases, and resolves another Faculty as body plus one of the four named senses. Sound's increment remains in the prose analysis, not the verse English.

The faculty-property differentiation closed at 2.21. This asks a different relation.

Hard, fluid, hot, and moving are predominance, not the absence of the others. Activities are offered: holding together, sustaining, ripening, spreading. Others say heat in water is known from greater cold. The reply: greater intensity need not be mixture, as with sound or feeling. Others say presence as seed, not in its own Form, citing the various Principles in a log. Seed is not actual Form under another name.

Visible color in wind is said to be accepted, not inferred. An inference is then offered from odor in moving air. The tension is kept.

Eight is not a count of every individual determination. Grouping solely by Essence would instead give four. Basis is counted as constituent; what is based upon it is counted by Essence. Repeated Elemental quartets are counted by kind. Words may be chosen; meaning is examined. The damaged compounds remain marked in the paired Bhāṣya.

Interpretation: the unit of the count travels with the number. Cognition governs Perception and Conception without collapsing into Mind or consciousness. The fivefold classification's consciousness and the Form co-arising rule retain their distinct functions.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_22
    a vak:Karika ;
    rdfs:label "VAK 2.22" ;
    vak:hasTopic vak:FormCoarising ;
    vak:belongsTo vak:Indriyanirdesa .

vak:SoundlessCluster vak:hasCount 8 .
vak:BodyCluster vak:hasCount 9 .
vak:OtherSenseCluster vak:hasCount 10 .

organon:VAK_2_22_Interpretation
    organon:distinguishes vak:NecessaryCoarising, vak:Possession,
        vak:CountingUnit .
```
