# VAK_2.24 — In Every Consciousness

## 1. Sanskrit (Devanāgarī)

```sanskrit
वेदना चेतना संज्ञा छन्दः स्पर्शो मतिः स्मृतिः ।
मनस्कारोऽधिमोक्षश्च समाधिः सर्वचेतसि ॥ २.२४ ॥
```

## 2. Sanskrit (IAST)

```text
vedanā cetanā saṃjñā cchandaḥ sparśo matiḥ smṛtiḥ /
manaskāro 'dhimokṣaś ca samādhiḥ sarvacetasi // 2.24 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| vedanā | nominative singular feminine noun | feeling |
| cetanā | nominative singular feminine noun | volition |
| saṃjñā | nominative singular feminine noun | reflection |
| chandaḥ | nominative singular masculine noun | wish to perform |
| sparśaḥ | nominative singular masculine noun | contact |
| matiḥ | nominative singular feminine noun | discriminative comprehension |
| smṛtiḥ | nominative singular feminine noun | mindfulness |
| manaskāraḥ | nominative singular masculine noun | attention |
| adhimokṣaḥ | nominative singular masculine noun | resolution |
| ca | conjunction | and; coordinates the enumeration, not alternatives |
| samādhiḥ | nominative singular masculine noun | concentration |
| sarva-cetasi | locative singular neuter compound | in every consciousness; prose specifies every moment |

Mati is prajñā: discriminative comprehension. Samādhi is
one-pointedness, not necessarily perfected absorption. Sandhi is opened
for parsing; the ten nominatives remain in their source order.

```text
# tokens: vedanā cetanā saṃjñā chandaḥ sparśaḥ matiḥ smṛtiḥ manaskāraḥ adhimokṣaḥ ca samādhiḥ sarvacetasi
```

## 4. Grammar

The enumeration is conjunctive, not a choice among ten. The final
locative supplies the universal scope over every member. Presence is
supplied as the predicate; the Bhāṣya specifies complete co-presence
in each consciousness-moment.
Its reportive kila is not a verse token.

```nltk-fcfg
% start S
# tokens: vedanā cetanā saṃjñā chandaḥ sparśaḥ matiḥ smṛtiḥ manaskāraḥ adhimokṣaḥ ca samādhiḥ sarvacetasi
S[SEM=<?every(?members)>] -> TEN[CNT=10,SEM=?members] EVERY[CASE=loc,SCOPE=every_moment,SEM=?every]
TEN[CNT=10,SEM=<\c.(Present(c,?a) & Present(c,?b) & Present(c,?d) & Present(c,?e) & Present(c,?f) & Present(c,?g) & Present(c,?h) & Present(c,?i) & Present(c,?j) & Present(c,?k))>] -> FEELING[CASE=nom,SEM=?a] VOLITION[CASE=nom,SEM=?b] REFLECTION[CASE=nom,SEM=?d] WISH[CASE=nom,SEM=?e] CONTACT[CASE=nom,SEM=?f] COMPREHENSION[CASE=nom,SEM=?g] MINDFULNESS[CASE=nom,SEM=?h] ATTENTION[CASE=nom,SEM=?i] RESOLUTION[CASE=nom,SEM=?j] AND[READING=conjunction] CONCENTRATION[CASE=nom,SEM=?k]
FEELING[CASE=nom,SEM=<feeling>] -> 'vedanā'
VOLITION[CASE=nom,SEM=<volition>] -> 'cetanā'
REFLECTION[CASE=nom,SEM=<reflection>] -> 'saṃjñā'
WISH[CASE=nom,SEM=<wish>] -> 'chandaḥ'
CONTACT[CASE=nom,SEM=<contact>] -> 'sparśaḥ'
COMPREHENSION[CASE=nom,SEM=<comprehension>] -> 'matiḥ'
MINDFULNESS[CASE=nom,SEM=<mindfulness>] -> 'smṛtiḥ'
ATTENTION[CASE=nom,SEM=<attention>] -> 'manaskāraḥ'
RESOLUTION[CASE=nom,SEM=<resolution>] -> 'adhimokṣaḥ'
AND[READING=conjunction] -> 'ca'
CONCENTRATION[CASE=nom,SEM=<concentration>] -> 'samādhiḥ'
EVERY[CASE=loc,SCOPE=every_moment,SEM=<\P.all c.(ConsciousnessMoment(c) -> P(c))>] -> 'sarvacetasi'
```

```nltk-dep
'sarvacetasi' -> 'vedanā' | 'cetanā' | 'saṃjñā' | 'chandaḥ' | 'sparśaḥ' | 'matiḥ' | 'smṛtiḥ' | 'manaskāraḥ' | 'adhimokṣaḥ' | 'samādhiḥ'
'adhimokṣaḥ' -> 'ca'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 11) | `TEN` | ten coordinated factor-kinds, with conjunction |
| [11, 12) | `EVERY` | universal consciousness-moment scope |
| [0, 12) | `S` | every listed kind present in each moment |

## 5. Translation

### Literal Translation

> Feeling, volition, reflection, wish to perform, contact, discriminative
> comprehension, mindfulness, attention, resolution, and concentration, in
> every consciousness.

### Bhāṣya-informed study translation

> Feeling, volition, reflection, wish to perform, contact, discriminative
> comprehension, mindfulness, attention, resolution, and concentration are
> all present together in every moment of consciousness.

## 6. Philosophical Translation

> Presence in every consciousness is not equal strength, not correctness, and not ethical quality. The ten co-occur; they do not become one.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| vedanā | feeling | three experiences, not together |
| cetanā | volition | cittābhisaṃskāra, mental action |
| saṃjñā | reflection | take-up of the mark; gloss damaged |
| chanda | wish to perform | kartṛkāmatā; not craving |
| sparśa | contact | born of the conjunction of Faculty, Condition, and Cognition |
| mati | discriminative comprehension | prajñā; not every act of discrimination is correct |
| smṛti | mindfulness | non-loss of the Cognitive Condition, not just past-event memory |
| manaskāra | attention | application of consciousness |
| adhimokṣa | resolution | adhimukti, settling upon |
| samādhi | concentration | one-pointedness |
| kila | it is said | reportive |

## 8. Logical Determination

**Kārikā, derived; temporal scope resolved by the Bhāṣya.** The
`sarvacetasi` lexical SEM applies the universal moment-scope to the
ten-factor conjunction. The model uses factor-kinds, not numerically
identical factor-tokens persisting through distinct moments. It tests the reported universal claim,
not an independent proof of that claim.

```nltk-sem
presence : \f.\c.Present(c,f)
every_moment : \P.all c.(ConsciousnessMoment(c) -> P(c))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
all c.(ConsciousnessMoment(c) -> (Present(c,feeling) & Present(c,volition) & Present(c,reflection) & Present(c,wish) & Present(c,contact) & Present(c,comprehension) & Present(c,mindfulness) & Present(c,attention) & Present(c,resolution) & Present(c,concentration)))

# THEORY enumerated_ten
# EXPECT enumerated_ten T
all c f.((ConsciousnessMoment(c) & GreatGroundKind(f)) -> Present(c,f))

# THEORY rejected_only_one_factor_per_moment
# EXPECT rejected_only_one_factor_per_moment F
all c f g.((ConsciousnessMoment(c) & Present(c,f) & Present(c,g)) -> f = g)

# THEORY rejected_presence_guarantees_adequacy
# EXPECT rejected_presence_guarantees_adequacy F
all c f.(Present(c,f) -> Adequate(c,f))

# THEORY rejected_three_feelings_simultaneous
# EXPECT rejected_three_feelings_simultaneous F
exists c.(FeelingMode(c,pleasant) & FeelingMode(c,painful) & FeelingMode(c,neutral))
```

```nltk-valuation
feeling => feeling_kind
volition => volition_kind
reflection => reflection_kind
wish => wish_kind
contact => contact_kind
comprehension => comprehension_kind
mindfulness => mindfulness_kind
attention => attention_kind
resolution => resolution_kind
concentration => concentration_kind
pleasant => pleasant_mode
painful => painful_mode
neutral => neutral_mode
ConsciousnessMoment => {moment_a,moment_b}
GreatGroundKind => {feeling_kind,volition_kind,reflection_kind,wish_kind,contact_kind,comprehension_kind,mindfulness_kind,attention_kind,resolution_kind,concentration_kind}
Present => {(moment_a,feeling_kind),(moment_a,volition_kind),(moment_a,reflection_kind),(moment_a,wish_kind),(moment_a,contact_kind),(moment_a,comprehension_kind),(moment_a,mindfulness_kind),(moment_a,attention_kind),(moment_a,resolution_kind),(moment_a,concentration_kind),(moment_b,feeling_kind),(moment_b,volition_kind),(moment_b,reflection_kind),(moment_b,wish_kind),(moment_b,contact_kind),(moment_b,comprehension_kind),(moment_b,mindfulness_kind),(moment_b,attention_kind),(moment_b,resolution_kind),(moment_b,concentration_kind)}
Adequate => {(moment_a,attention_kind)}
FeelingMode => {(moment_a,pleasant_mode),(moment_b,neutral_mode)}
```

There are exactly ten named kinds, all instantiated in each modeled
moment. This is not a claim that only ten factors can accompany a
consciousness. The illustrative adequacy countermodel shows that
presence alone does not encode correctness or perfected practice;
it does not diagnose a particular source-described moment.

## 9. Interpretive Note

**Translation note.** The study translation makes the prose's complete
co-presence and moment-level scope explicit. Kila reports the claim;
the particle does not by itself establish rejection. The definitions
and the difficulty of distinguishing the factors remain separate
from this universal assertion.

The question was left at 2.23. These are the great-ground factors because the ground is every consciousness. Not because they are exalted.

Volition and wish to perform are different. Reflection and discriminative comprehension are different. The recognition-gloss is damaged. The distinction of the two entries does not depend on restoring it.

Contact is not confined to bodily touch. Its Condition is not thereby
decided as an externally established Thing. Mindfulness is non-loss
of the Cognitive Condition, not only memory of a past event.
Every consciousness is the operating range, not a common Cognitive
Condition substituted for each factor's specific relation.

The plant analogy is difficulty, not impossibility. The universal claim, the definitions, and the difficulty of seeing the differences stay apart. No rival list. No school named. Kila alone is not a rejection.

In the Organon reading, Cognition joins and governs Perception and
Conception while remaining distinct from consciousness and Mind.
Reflection and discriminative comprehension are distinct entries
within the present list, not interchangeable names for that governing
Cognition. Universal presence is not universal adequacy.

In the Organon reading, the `samādhi` named here is a factor in each
consciousness-moment, glossed as one-pointedness. A proposed Samādhi
operator that gathers conditioned sequence into determinate `artha`
would be a further construction; this enumeration does not establish
that return to Principle.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_24
    a vak:Karika ;
    rdfs:label "VAK 2.24" ;
    vak:hasTopic vak:GreatGroundTen ;
    vak:belongsTo vak:Indriyanirdesa .

vak:GreatGroundTen vak:inEveryConsciousness true .
vak:Mati vak:is vak:DiscriminativeComprehension .

organon:VAK_2_24_Interpretation
    organon:distinguishes vak:UniversalPresence, vak:FactorDefinition,
        vak:FunctionalAdequacy .
```
