# VAK_8.12 — Feelings in Dhyāna Rebirth

## 1. Sanskrit (Devanāgarī)

```sanskrit
सौमनस्यसुखोपेक्षा उपेक्षासुमनस्कते ।
सुखोपेक्षे उपेक्षा प्रविदो ध्यानोपपत्तिषु ॥ ८.१२ ॥
```

## 2. Sanskrit (IAST)

```text
saumanasyasukhopekṣā upekṣāsumanaskate |
sukhopekṣe upekṣā pravido dhyānopapattiṣu || 8.12 ||
```

The verse follows the local kārikā witness. `Pravido`
remains unresolved here; the prose securely determines
the fourfold distribution without resolving that reading.
The running source's `sukhhopekṣe` is not substituted
for the local verse's `sukhopekṣe`.

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| `saumanasyasukhopekṣāḥ` | coordinated plural, final visarga lost before the following vowel | pleasant-mindedness, pleasure, and neutral feeling |
| `upekṣāsumanaskate` | coordinated dual expression | neutral feeling and pleasant-mindedness |
| `sukhopekṣe` | coordinated dual expression | pleasure and neutral feeling |
| `upekṣā` | nominative singular feminine | neutral feeling alone in the fourth allocation |
| `pravido` | unresolved transmitted form | no independent lexical meaning assigned in this study |
| `dhyānopapattiṣu` | locative plural compound | in rebirths corresponding to the dhyānas |

`Sukha + upekṣā` yields `sukhopekṣā`;
`dhyāna + upapattiṣu` yields `dhyānopapattiṣu`.
The components within the compounds are not separately
inflected nominatives. The prose resolves the verse's
`sumanaskatā` expression through saumanasya.

## 4. Grammar

Four ordered groups of feelings belong to four rebirth levels, not to the corresponding attainment inventories. The prose fixes counts as three, two, two, one; `pravido` remains unresolved and is not assigned an invented gloss.

```nltk-fcfg
% start S
# tokens: saumanasyasukhopekṣā ∅-prathama-dhyānopapattau upekṣāsumanaskate ∅-dvitīya-dhyānopapattau sukhopekṣe ∅-tṛtīya-dhyānopapattau upekṣā ∅-caturtha-dhyānopapattau pravido dhyānopapattiṣu
S -> CL[K=ordered_feelings] CL[K=rebirth_scope]
CL[K=ordered_feelings] -> N[CASE=nom,NUM=pl,GEN=f,COUNT=three] N[CASE=loc,NUM=sg,GEN=f,SUPPLIED=prose,LEVEL=first] N[CASE=nom,NUM=du,GEN=f,COUNT=two] N[CASE=loc,NUM=sg,GEN=f,SUPPLIED=prose,LEVEL=second] N[CASE=nom,NUM=du,GEN=n,COUNT=two] N[CASE=loc,NUM=sg,GEN=f,SUPPLIED=prose,LEVEL=third] N[CASE=nom,NUM=sg,GEN=f] N[CASE=loc,NUM=sg,GEN=f,SUPPLIED=prose,LEVEL=fourth]
CL[K=rebirth_scope] -> UNK[TEXTUAL=uncertain] N[CASE=loc,NUM=pl,GEN=f,DOMAIN=rebirth]
N[CASE=nom,NUM=pl,GEN=f,COUNT=three] -> 'saumanasyasukhopekṣā'
N[CASE=loc,NUM=sg,GEN=f,SUPPLIED=prose,LEVEL=first] -> '∅-prathama-dhyānopapattau'
N[CASE=nom,NUM=du,GEN=f,COUNT=two] -> 'upekṣāsumanaskate'
N[CASE=loc,NUM=sg,GEN=f,SUPPLIED=prose,LEVEL=second] -> '∅-dvitīya-dhyānopapattau'
N[CASE=nom,NUM=du,GEN=n,COUNT=two] -> 'sukhopekṣe'
N[CASE=loc,NUM=sg,GEN=f,SUPPLIED=prose,LEVEL=third] -> '∅-tṛtīya-dhyānopapattau'
N[CASE=nom,NUM=sg,GEN=f] -> 'upekṣā'
N[CASE=loc,NUM=sg,GEN=f,SUPPLIED=prose,LEVEL=fourth] -> '∅-caturtha-dhyānopapattau'
UNK[TEXTUAL=uncertain] -> 'pravido'
N[CASE=loc,NUM=pl,GEN=f,DOMAIN=rebirth] -> 'dhyānopapattiṣu'
```

```nltk-dep
'dhyānopapattiṣu' -> 'pravido' | 'saumanasyasukhopekṣā' | 'upekṣāsumanaskate' | 'sukhopekṣe' | 'upekṣā'
'∅-prathama-dhyānopapattau' -> 'saumanasyasukhopekṣā'
'∅-dvitīya-dhyānopapattau' -> 'upekṣāsumanaskate'
'∅-tṛtīya-dhyānopapattau' -> 'sukhopekṣe'
'∅-caturtha-dhyānopapattau' -> 'upekṣā'
```

`Upapattiṣu` is rebirth scope, not sitting; neutral feeling is neither the equanimity factor nor absence of experience. The second group lacks pleasure because its vijñānakāya is absent; the ordered assignments come from prose, not a gloss of `pravido`.


**Close construe.** In the four dhyāna rebirths occur,
respectively: pleasant-mindedness, pleasure, and neutral
feeling; neutral feeling and pleasant-mindedness; pleasure
and neutral feeling; and neutral feeling alone.

## 5. Translation

### Literal Translation

> In the dhyāna rebirths: pleasant-mindedness, pleasure,
> and neutral feeling; neutral feeling and pleasant-mindedness;
> pleasure and neutral feeling; neutral feeling.

### Bhāṣya-informed study translation

> In the rebirths corresponding to the dhyānas, the feelings are,
> respectively: pleasant-mindedness, pleasure, and neutral feeling in
> the first; neutral feeling and pleasant-mindedness in the second;
> pleasure and neutral feeling in the third; and neutral feeling alone
> in the fourth.

## 6. Philosophical Translation

> The shared name of a dhyāna level does not give
> attainment and rebirth an identical constitution.
> Feeling must be determined according to the mode
> under discussion and its knowledge supports. Even
> pleasure changes its contextual determination: first-level
> pleasure and third-level mental pleasure cannot be
> treated as an undifferentiated item merely because
> both are called sukha.

The sequence is a distribution of feeling types, not
a claim that progressively fewer feelings coexist in
one moment or that neutral feeling amounts to no feeling.

## 7. Technical Vocabulary

**`Dhyānasamāpatti`.** Meditative attainment of a dhyāna.
The preceding discussion locates saumanasya in the
first two attainments, sukha in the third, and neutral
feeling in the fourth.

**`Dhyānopapatti`.** Rebirth corresponding to a dhyāna.
Its feeling inventory is the present subject. Rebirth
at a level does not mean continuous occurrence of
that level's meditative attainment.

**Source.** Pradhan 441|19–442|06, checked against the local
Bhāṣya study and running source.

**`Vijñānakāya`.** Knowledge-body or class of knowledge; it is not an
anatomical body.
The compounds with three and four enumerate classes
with which a feeling is associated. They do not count
three or four simultaneous feelings.

**`Manobhūmika`.** Belonging to the mental level. This
qualifies first-level saumanasya and both listed feelings
in each of the second and third rebirths. In particular,
third-level sukha is explicitly mental in this account.

**`Trivijñānakāyika / caturvijñānakāyikī`.** Associated
with three / four knowledge-bodies. The first qualifies
first-level sukha, the second its neutral feeling.
The present sentence gives their counts; the following
verse explicitly discusses eye-, ear-, and body-knowledge.

**`Upekṣā`.** Neutral feeling in this vedanā inventory.
It should not be rendered as if it were simply the
wholesome equanimity factor discussed in VAK 8.10.
The same term must be determined by its classificatory
setting.

## 8. Logical Determination

The verse's ordered feeling groups concern rebirths corresponding to four dhyānas, not feelings in meditative attainment [verse; prose]. The Bhāṣya supplies the four level assignments and explains one absence through its missing support; `pravido` remains unresolved.

**Signature.** `Rebirth(x)`; `FeelingAt(x,f)`; `Support(x,f,s)`; `SupportAbsent(x,s)`.

**Finite data.** The prose roster has 3/2/2/1 feeling types. First-level support distinctions and the second-level lack are represented without making the count a universal claim about simultaneous feelings.

```nltk-valuation
firstrebirth => firstrebirth
secondrebirth => secondrebirth
thirdrebirth => thirdrebirth
fourthrebirth => fourthrebirth
saumanasya => saumanasya
sukha => sukha
upeksa => upeksa
threebodies => threebodies
fourbodies => fourbodies
mental => mental
sukhakaya => sukhakaya
Rebirth => {firstrebirth, secondrebirth, thirdrebirth, fourthrebirth}
FeelingAt => {(firstrebirth,saumanasya),(firstrebirth,sukha),(firstrebirth,upeksa),(secondrebirth,upeksa),(secondrebirth,saumanasya),(thirdrebirth,sukha),(thirdrebirth,upeksa),(fourthrebirth,upeksa)}
Support => {(firstrebirth,sukha,threebodies),(firstrebirth,saumanasya,mental),(firstrebirth,upeksa,fourbodies),(secondrebirth,saumanasya,mental),(secondrebirth,upeksa,mental),(thirdrebirth,sukha,mental),(thirdrebirth,upeksa,mental)}
SupportAbsent => {(secondrebirth,sukhakaya)}
```

**Rules (verse and prose).**

```nltk-fol
# THEORY shared
# [prose] first rebirth: three feelings and their specified supports
FeelingAt(firstrebirth,saumanasya)
FeelingAt(firstrebirth,sukha)
Support(firstrebirth,sukha,threebodies)
Support(firstrebirth,upeksa,fourbodies)
# [prose] second: two mental feelings; sukha absent with its support
FeelingAt(secondrebirth,saumanasya)
FeelingAt(secondrebirth,upeksa)
-FeelingAt(secondrebirth,sukha)
SupportAbsent(secondrebirth,sukhakaya)
# [verse] third: pleasure and neutral feeling; fourth: neutral alone
FeelingAt(thirdrebirth,sukha)
FeelingAt(thirdrebirth,upeksa)
FeelingAt(fourthrebirth,upeksa)
```

**Results (NLTK).** The checker confirms the listed positive and negative assignments in the finite valuation. The 3/2/2/1 tally is read from this roster; the model check does not establish that feelings co-occur in one moment.

**Scope cautions.** `Upapatti` means rebirth, not sitting in attainment; `upekṣā` here is neutral feeling, not the equanimity factor. The absent support explains the second rebirth's sukha in the prose, not every sensory operation of higher beings. No gloss is assigned to `pravido`.

## 9. Interpretive Note

**Source control over an opaque verse.** The prose
makes the allocation intelligible even though `pravido`
remains philologically unresolved. Confidence in the
inventory should not be confused with confidence in
every transmitted syllable. The literal translation
marks the gap; the study translation gives the secure
prose determination.

**Witness cautions.** The running text has `taskiṃ`,
`sukhhopekṣe`, `prathamadhyānotpatto`, and
`tṛtīyadhyānopapattī` where the local study regularizes
some readings. These forms remain untouched in their
witnesses. The repeated level names, explicit numerals,
and prose feeling lists control the present exposition.

**Neutral feeling is a positive member of the inventory.**
Its exclusive place in the fourth rebirth does not
establish absence of experience or identify that rebirth
with liberation. Nor does this short passage establish
a general theory of progressive purification; it
specifies the feeling distribution and selected supports.

**Organon reconstruction — Yoga Vidyā and Yoga Technē.**
Yoga Vidyā articulates level, mode of occurrence,
feeling type, and knowledge support together. Yoga
Technē, its kriyā–karma companion, concerns effective
exercise; it must distinguish an attainment's operation
from the constitution of rebirth at its corresponding level.

For Organon representation, attach each feeling assertion
to its mode and level. Preserve the different support
determinations of sukha and the feeling sense of upekṣā.
A shared name or equal inventory size cannot substitute
for this relational specification. This is project
reconstruction, not a further doctrine attributed to
the Bhāṣya.

**Review status.** Provisional, Bhāṣya-controlled study.
The attainment/rebirth distinction, four inventories,
three-/four-knowledge-body specifications, mental qualifiers,
and relevant transition to VAK 8.13 have been checked
against the local research and running source. `Pravido`
remains unresolved.

## 10. OWL++ Seed

```text
Class: DhyanaLevel
Class: DhyanaAttainment
Class: DhyanaRebirth
Class: FeelingType
Class: KnowledgeSupportSpecification

ObjectProperty: belongsToLevel
ObjectProperty: hasAvailableFeelingType
ObjectProperty: hasKnowledgeSupportSpecification

FirstDhyanaRebirth:
    feelings: Saumanasya, Sukha, NeutralFeeling
    feelingTypeCount: 3
    sukhaSupport: ThreeKnowledgeBodies
    saumanasyaSupport: Mental
    neutralFeelingSupport: FourKnowledgeBodies

SecondDhyanaRebirth:
    feelings: Saumanasya, NeutralFeeling
    feelingTypeCount: 2
    listedFeelingSupports: Mental

ThirdDhyanaRebirth:
    feelings: Sukha, NeutralFeeling
    feelingTypeCount: 2
    listedFeelingSupports: Mental

FourthDhyanaRebirth:
    feelings: NeutralFeelingOnly
    feelingTypeCount: 1

ProjectConstraint: Keep attainment and rebirth inventories distinct.
ProjectConstraint: Feeling-type counts do not assert simultaneous feelings.
ProjectConstraint: Determine sukha by level and knowledge support.
ProjectConstraint: Upeksha here designates feeling, not the equanimity factor.
ProjectConstraint: Equal counts do not imply equal inventory membership.
ProjectConstraint: Reserve higher-level sensory operation for VAK 8.13.
ProjectConstraint: Preserve pravido as an unresolved witness reading.
```

This is a declarative project seed, not executable OWL.
VAK 8.13 next explains the knowledge operating in beings
reborn in the second and higher dhyānas, including the
first-dhyāna knowledge they bring into activity.
