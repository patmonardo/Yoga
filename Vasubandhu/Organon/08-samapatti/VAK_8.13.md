# VAK_8.13 — First-Dhyāna Knowledge in Higher Dhyāna Rebirth

## 1. Sanskrit (Devanāgarī)

```sanskrit
कायाक्षिश्रोत्रविज्ञानं विज्ञप्त्युत्थापकं च यत् ।
द्वितीयादौ तदाद्याप्तम् अक्लिष्टाव्याकृतं च तत् ॥ ८.१३ ॥
```

## 2. Sanskrit (IAST)

```text
kāyākṣiśrotravijñānaṃ vijñaptyutthāpakaṃ ca yat |
dvitīyādau tadādyāptam akliṣṭāvyākṛtaṃ ca tat || 8.13 ||
```

The Sanskrit follows the local kārikā witness. The
Bhāṣya resolves “belonging to the first” as belonging
to the first-dhyāna level and locates the question in
beings reborn at the second and higher dhyāna levels.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `kāyākṣiśrotravijñānam` | nominative singular neuter compound, distributively understood | body-, eye-, and ear-knowledge |
| `vijñaptyutthāpakam` | nominative singular neuter adjective, with vijñānam understood | knowledge that initiates manifest action |
| `ca` | conjunction | and |
| `yat` | nominative singular neuter relative pronoun | that which |
| `dvitīyādau` | locative singular compound | in the second and subsequent [dhyānas] |
| `tat` | nominative singular neuter correlative pronoun | that |
| `ādyāptam` | nominative singular neuter compound | belonging to the first [dhyāna] |
| `akliṣṭāvyākṛtam` | nominative singular neuter compound adjective | undefiled and ethically indeterminate |

`Kāya + akṣi` yields `kāyākṣi`; `vijñapti +
utthāpaka` yields `vijñaptyutthāpaka`; `dvitīya +
ādi` yields `dvitīyādi`; `ādya + āpta` yields
`ādyāpta`; `akliṣṭa + avyākṛta` yields
`akliṣṭāvyākṛta`.

## 4. Grammar

The relative and correlative clauses agree in number and gender: the same Cognition belongs to the first-dhyāna level and is ethically indeterminate. The Bhāṣya locates this operation in higher-level rebirth, not an uninterrupted higher-dhyāna sitting.

```nltk-fcfg
% start S
# tokens: kāyākṣiśrotravijñānam vijñaptyutthāpakaṃ ca yat dvitīyādau ∅-upapattiṣu tadādyāptam akliṣṭāvyākṛtam ca tat
S -> CL[K=relative,CASE=?c,NUM=?n,GEN=?g] CL[K=correlative,CASE=?c,NUM=?n,GEN=?g]
CL[K=relative,CASE=?c,NUM=?n,GEN=?g] -> N[CASE=?c,NUM=?n,GEN=?g] ADJ[CASE=?c,NUM=?n,GEN=?g,ROLE=manifestation] CONJ[COORD=yes] REL[CASE=?c,NUM=?n,GEN=?g]
CL[K=correlative,CASE=?c,NUM=?n,GEN=?g] -> LOC[CASE=loc,NUM=sg,GEN=n] N[CASE=loc,NUM=pl,GEN=f,SUPPLIED=prose] ADJ[CASE=?c,NUM=?n,GEN=?g,LEVEL=first,REF=relative] ADJ[CASE=?c,NUM=?n,GEN=?g,ETHICS=indeterminate] CONJ[COORD=yes] PRON[CASE=?c,NUM=?n,GEN=?g,REF=relative]
N[CASE=nom,NUM=sg,GEN=n] -> 'kāyākṣiśrotravijñānam'
ADJ[CASE=nom,NUM=sg,GEN=n,ROLE=manifestation] -> 'vijñaptyutthāpakaṃ'
CONJ[COORD=yes] -> 'ca'
REL[CASE=nom,NUM=sg,GEN=n] -> 'yat'
LOC[CASE=loc,NUM=sg,GEN=n] -> 'dvitīyādau'
N[CASE=loc,NUM=pl,GEN=f,SUPPLIED=prose] -> '∅-upapattiṣu'
PRON[CASE=nom,NUM=sg,GEN=n,REF=relative] -> 'tat'
ADJ[CASE=nom,NUM=sg,GEN=n,LEVEL=first,REF=relative] -> 'tadādyāptam'
ADJ[CASE=nom,NUM=sg,GEN=n,ETHICS=indeterminate] -> 'akliṣṭāvyākṛtam'
PRON[CASE=nom,NUM=sg,GEN=n,REF=relative] -> 'tat'
```

```nltk-dep
'tadādyāptam' -> 'kāyākṣiśrotravijñānam' | 'vijñaptyutthāpakaṃ' | 'ca' | 'yat' | 'dvitīyādau' | '∅-upapattiṣu'
'tat' -> 'tadādyāptam' | 'akliṣṭāvyākṛtam' | 'ca'
```

The commentary supplies “reborn there” and specifies the first-dhyāna level: non-native does not mean inoperative. It is undefiled because passion is absent, not wholesome because it is inferior; this ethical classification is not neutral feeling or the uncontaminated mode.


**Close construe.** In the second and subsequent dhyāna
rebirths, the body-, eye-, and ear-knowledge, together
with knowledge initiating manifest action, belongs to
the first dhyāna; that knowledge is undefiled-neutral.

## 5. Translation

### Literal Translation

> Body-, eye-, and ear-Cognition, and that which
> initiates manifest action—in the second and subsequent
> [dhyānas], that belongs to the first, and it is
> undefiled and indeterminate.

### Bhāṣya-informed study translation

> In the second and higher dhyāna rebirths, the body-, eye-, and
> ear-Cognition, together with the Cognition that initiates manifest
> action, belongs to the first dhyāna; and that Cognition is
> undefiled and ethically indeterminate.

## 6. Philosophical Translation

> The level at which a being is reborn and the level
> to which an operative knowledge belongs are distinct
> determinations. A sensory capacity need not belong
> to the higher level itself in order to become
> operative for a being reborn there. The passage
> specifies both the first-dhyāna basis of the operation
> and its undefiled-neutral ethical character.

The distinction explains availability without assigning
higher-level status to the lower-level knowledge.
It does not establish a general theory of simultaneous
mental layers or an unchanged higher attainment running
alongside sensory knowledge.

## 7. Technical Vocabulary

**Source.** Pradhan 442|07–442|18, checked against the local Bhāṣya
study and running source. The study translation uses **Cognition**
for *vijñāna*; “knowledge” in the surrounding notes is the older
research rendering of the same term. Brackets in the Bhāṣya
translation make the scope of the final reasons explicit.

**`Kāya / akṣi / śrotra-vijñāna`.** Body-, eye-, and
ear-knowledge: the three sensory kinds named here.
The prose refers to seeing through touching as the
range of functions under discussion.

**`Vijñaptyutthāpaka`.** Initiating manifest action. The
understood subject is knowledge that brings about
bodily or verbal manifestation. Vijñapti is not simply
modern information transmission; the Karmanirdeśa
vocabulary supplies its action context.

**`Svabhūmika`.** Belonging to one's own level. The
prose's denial concerns this membership, not every
possibility of the knowledge becoming operative.

**`Saṃmukhīkurvanti`.** They make present or bring into
operation. This is the positive answer to the problem
of sensory and manifest activity. “Borrowing” may
serve as an explanatory metaphor, but the source
neither describes a transfer between persons nor
posits an external store of knowledge.

**`Nirmāṇacittavat`.** As with a mind for producing a
magical creation. The comparison concerns the operation
of a mind belonging to another level. The local
research's “constructed mind” should not be taken
to mean that the passage treats all cognition as
fabricated or introduces artificial intelligence.

**`Akliṣṭāvyākṛta / anivṛtāvyākṛta`.** Undefiled-neutral /
unobstructed-neutral. The latter is the prose's explicit
classification of the knowledge made present. Ethical
neutrality is distinct from neutral feeling and from
uncontaminated knowledge.

**`Vītarāgatva / hīnatva`.** Freedom from passion /
lower or inferior status. These supply the two local
reasons for excluding defiled and wholesome classifications.
They do not imply that every higher-level being has
abandoned all passion, or that every lower-level
knowledge is universally unwholesome.

## 8. Logical Determination

The verse answers the objection inherited from VAK 8.12 by separating two
relations that the objection runs together: a cognition's native level, and
its operation by a being reborn at a level. Provenance tags: `[verse]`,
`[prose]`, and a theory name for each attributed position. Constants are ASCII
and longer than one letter (NLTK reads `d1` as a variable).

**Signature.** `Higher(l)` (second, third, fourth), `Covered(k)` (body-, eye-
and ear-Cognition and the Cognition initiating manifestation), `Native(k,l)`
(`k` belongs to level `l` as its own), `LevelOf(k,l)` (the level the Bhāṣya
assigns `k`), `ReachedAt(b,l)` (being `b` is reborn at `l`), `Brought(b,k)`
(`b` brings `k` into operation), `Operates(b,k)`, `FreeOfPassion(k)`,
`Inferior(k,l)` (`k` is inferior relative to level `l`), `Defiled(k)`,
`Wholesome(k)`, `Neutral(k)` (unobstructed-neutral).

**Composition (`yat … tat`).** The relative–correlative pair of §4 is a
restricted universal: `yat` supplies the restrictor, `tat` the scope.

```nltk-sem
# lexicon SEM
yat…tat           : \P.\Q.all x.(P(x) -> Q(x))
yat (restrictor)  : \x.Covered(x)
tat (scope)       : \x.(LevelOf(x,first) & Neutral(x))
# beta-reduction (checked in NLTK):
all x.(Covered(x) -> (LevelOf(x,first) & Neutral(x)))
```

**Theories (never merged).**

```nltk-fol
# THEORY shared
# [prose, from 8.12] the three bodies are not found at second and higher
Higher(second)
all k.all l.((Higher(l) & Covered(k)) -> -Native(k,l))
# the objection's data: a being reborn at second sees (Covered), and operates it
ReachedAt(b2,second)
Covered(sight)
Operates(b2,sight)

# THEORY objection
# bridge assumed by the question: whatever a being operates is native to its level
all b.all k.all l.((ReachedAt(b,l) & Operates(b,k)) -> Native(k,l))

# THEORY answer
# [verse] tadādyāptam: the Cognition belongs to the first-dhyāna level
all k.(Covered(k) -> LevelOf(k,first))
# [prose] ∅-upapattiṣu: reborn there, they bring it into operation
all b.all k.((Brought(b,k) & Covered(k)) -> Operates(b,k))
Brought(b2,sight)
# [verse] akliṣṭāvyākṛtam, with the Bhāṣya's two reasons
all b.all k.((Brought(b,k) & Covered(k)) -> (-Defiled(k) & Neutral(k)))
all k.((Covered(k) & FreeOfPassion(k)) -> -Defiled(k))
all b.all k.all l.((Brought(b,k) & ReachedAt(b,l) & Inferior(k,l)) -> -Wholesome(k))
```

**Results (NLTK).**
- *Objection.* `shared` plus `objection` is contradictory (`ResolutionProver`):
  the shared data give a higher-level being operating `sight` while `Native` is
  denied at that level, yet the bridge demands it. The question's force is
  genuine; the contradiction is in the bridge, not in the facts.
- *Answer.* `shared` plus `answer` is satisfiable, and the finite model below
  is the proof of that: it makes every `shared` and `answer` rule true and the
  `objection` bridge false. The verse removes the bridge, not the 8.12 facts.
  The answer also derives `Operates(b2,sight)` (`TableauProver` and
  `ResolutionProver` agree).
- *Native versus operated.* `LevelOf(sight,first)` with `Native(sight,first)`
  and no native standing at `second` is exactly “non-native does not mean
  inoperative”.

**Facts (a model of `shared` plus `answer`).** The being `b1` is a
first-level being with its own wholesome sight, included to show the
inferiority rule does not overreach.

```nltk-valuation
first => first
second => second
b1 => b1
b2 => b2
sight => sight
sight1 => sight1
Higher => {second}
ReachedAt => {(b1,first), (b2,second)}
Covered => {sight, sight1}
Operates => {(b1,sight1), (b2,sight)}
Brought => {(b2,sight)}
Native => {(sight,first), (sight1,first)}
LevelOf => {(sight,first), (sight1,first)}
FreeOfPassion => {sight}
Inferior => {(sight,second)}
Defiled => {}
Neutral => {sight}
Wholesome => {sight1}
```

In this model `sight1` is wholesome and first-level, and nothing excludes it:
the inferiority rule fires only on `Brought(b,k) & ReachedAt(b,l) &
Inferior(k,l)`, so it is relative to this higher-level use and does not make
wholesome first-dhyāna Cognition impossible for any being.

**Scope cautions.**
- The nirmāṇacitta comparison (“as with a mind for magical creation”) is the
  Bhāṣya's illustration. It is not a rule: nothing asserts that ordinary seeing
  or hearing is created.
- The Defiled exclusion is by `FreeOfPassion`; the Wholesome exclusion is by
  inferiority at the level of use. The two reasons are separate rules and
  neither implies the other.
- `Avasitaṃ dhyānakāryam` closes the treatment of dhyāna only. No rule
  closes Chapter 8; the next question concerns acquisition.
- 8.12's denial is about level membership (`Native`). It is not an
  exhaustive denial of every event involving another level's Cognition.

## 9. Interpretive Note

**The scope needs tightening from the first pass.**
The research kārikā file speaks of “beings or attainments.”
The commentary's rebirth question provides the narrower
basis for this official study. Claims that a higher
attainment remains uninterrupted during sensory activity,
or that functional descent necessarily preserves every
aspect of attained status, exceed this short passage.

**Witness cautions.** The running source includes
`na ve keṣūpapannānāṃ` and `cakṣurvijñānādayona` in
the introductory reply. Its question also has
`cāvijñapti samutthāpayanti`. The repeated positive
`vijñapti` and `vijñaptisamutthāpaka` in the verse and
answer support the manifest-action reading here; the
question's irregular spelling is not silently used
to change the subject to avijñapti. Originals remain
unchanged, and no critical reconstruction is claimed.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates rebirth level, knowledge level,
operation, and ethical quality as distinct but related
determinations. Yoga Technē, its kriyā–karma companion,
concerns the effective exercise of a capacity whose
level need not coincide with the being's rebirth level.

For Organon representation, distinguish “belongs to”
from “is brought into operation by.” The source's
positive account becomes obscured if every available
function is automatically made a native constituent
of the higher level. This is a restrained project
reconstruction; software modules and concurrent execution
are not doctrines attributed to the Bhāṣya.

**Review status.** Provisional, Bhāṣya-controlled study.
The rebirth scope, first-dhyāna affiliation, making-present
verb, nirmāṇacitta comparison, ethical classification,
two reasons, and local closure have been checked
against the local research and running source.

## 10. OWL++ Seed

```text
Class: DhyanaRebirthLevel
Class: KnowledgeOperation
Class: KnowledgeLevel
Class: EthicalClassification

ObjectProperty: rebornAtLevel
ObjectProperty: bringsIntoOperation
ObjectProperty: belongsToKnowledgeLevel
ObjectProperty: hasEthicalClassification

HigherDhyanaRebornBeings:
    rebirthLevels: SecondDhyana, ThirdDhyana, FourthDhyana
    operationsMadePresent: EyeKnowledge, EarKnowledge, BodyKnowledge,
                           ManifestActionInitiatingKnowledge

SpecifiedKnowledgeOperations:
    knowledgeLevel: FirstDhyana
    ethicalClassification: UnobstructedNeutral
    proseComparison: NirmanaCitta

ProjectConstraint: Rebirth level and operative knowledge level remain distinct.
ProjectConstraint: Not native to a level does not mean never operative.
ProjectConstraint: Do not assert uninterrupted higher attainment during operation.
ProjectConstraint: Ethical neutrality is distinct from neutral feeling.
ProjectConstraint: Scope the two ethical reasons to the operation discussed.
ProjectConstraint: The dhyana closure is local, not the end of Chapter 8.
```

This is a declarative project seed, not executable OWL.
VAK 8.14 next begins the account of acquiring dhyānas
and formless attainments.
