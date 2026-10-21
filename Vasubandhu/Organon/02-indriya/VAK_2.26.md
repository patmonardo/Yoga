# VAK_2.26 — Always in the Afflicted

## 1. Sanskrit (Devanāgarī)

```sanskrit
मोहः प्रमादः कौशीद्यमाश्रद्ध्यं स्त्यानमौद्धत्यम् ।
क्लिष्टे सदैवाकुशले त्वाह्रीक्यमनपत्रपा ॥ २.२६ ॥
```

## 2. Sanskrit (IAST)

```text
mohaḥ pramādaḥ kauśīdyam āśraddhyaṃ styānam auddhatyam /
kliṣṭe sadaivākuśale tv āhrīkyam anapatrapā // 2.26 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| mohaḥ | nom. sg. m. | delusion |
| pramādaḥ | nom. sg. m. | heedlessness |
| kauśīdyam | nom. sg. n. | laziness |
| āśraddhyam | nom. sg. n. | lack of faith |
| styānam | nom. sg. n. | sluggishness |
| auddhatyam | nom. sg. n. | agitation |
| kliṣṭe sadā eva | loc. sg. n. + adverbs | always in the afflicted |
| akuśale tu | loc. sg. n. + particle | but in the unwholesome |
| āhrīkyam | nom. sg. n. | shamelessness |
| anapatrapā | nom. sg. f. | lack of moral caution |

Afflicted and unwholesome are not the same range.

The final locative starts a second clause; consciousness is supplied
in both by the prose. Sandhi is opened, including sadā eva and tu.

```text
# tokens: mohaḥ pramādaḥ kauśīdyam āśraddhyam styānam auddhatyam kliṣṭe sadā eva akuśale tu āhrīkyam anapatrapā
```

## 4. Grammar

The six nominatives are coordinated, not alternatives. Always
scopes the afflicted clause and is resolved as invariably in the
prose for the unwholesome pair. Tu distinguishes the ranges; it
does not replace the six with the two. Only in afflicted consciousness
is an explicit prose conclusion, not the meaning of six. The first
clause composes `kliṣṭe` with `sadā`; the second clause applies the
Bhāṣya-resolved universal scope of `akuśale`.

```nltk-fcfg
% start S
# tokens: mohaḥ pramādaḥ kauśīdyam āśraddhyam styānam auddhatyam kliṣṭe sadā eva akuśale tu āhrīkyam anapatrapā
S[SEM=<(?six & ?two)>] -> AFFLICTEDCLAUSE[SEM=?six] UNWHOLESOMECLAUSE[SEM=?two]
AFFLICTEDCLAUSE[SEM=<?always(?afflicted(?list))>] -> SIX[CNT=6,SEM=?list] AFFLICTED[CASE=loc,SEM=?afflicted] ALWAYS[SCOPE=every,SEM=?always] EMPHASIS
SIX[CNT=6,SEM=<\c.(Present(c,?a) & Present(c,?b) & Present(c,?d) & Present(c,?e) & Present(c,?f) & Present(c,?g))>] -> DELUSION[SEM=?a] HEEDLESS[SEM=?b] LAZY[SEM=?d] FAITHLESS[SEM=?e] SLUGGISH[SEM=?f] AGITATED[SEM=?g]
UNWHOLESOMECLAUSE[SEM=<?unwholesome(\c.(Present(c,?a) & Present(c,?b)))>] -> UNWHOLESOME[CASE=loc,SUPPLIED=prose_universal,SEM=?unwholesome] BUT[READING=scope_contrast] SHAMELESS[SEM=?a] UNCAUTIOUS[SEM=?b]
DELUSION[SEM=<delusion>] -> 'mohaḥ'
HEEDLESS[SEM=<heedlessness>] -> 'pramādaḥ'
LAZY[SEM=<laziness>] -> 'kauśīdyam'
FAITHLESS[SEM=<faithlessness>] -> 'āśraddhyam'
SLUGGISH[SEM=<sluggishness>] -> 'styānam'
AGITATED[SEM=<agitation>] -> 'auddhatyam'
AFFLICTED[CASE=loc,SEM=<\P.\c.(AfflictedMoment(c) -> P(c))>] -> 'kliṣṭe'
ALWAYS[SCOPE=every,SEM=<\P.all c.P(c)>] -> 'sadā'
EMPHASIS -> 'eva'
UNWHOLESOME[CASE=loc,SUPPLIED=prose_universal,SEM=<\P.all c.(UnwholesomeMoment(c) -> P(c))>] -> 'akuśale'
BUT[READING=scope_contrast] -> 'tu'
SHAMELESS[SEM=<shamelessness>] -> 'āhrīkyam'
UNCAUTIOUS[SEM=<lack_caution>] -> 'anapatrapā'
```

```nltk-dep
'kliṣṭe' -> 'mohaḥ' | 'pramādaḥ' | 'kauśīdyam' | 'āśraddhyam' | 'styānam' | 'auddhatyam' | 'sadā'
'sadā' -> 'eva'
'akuśale' -> 'tu' | 'āhrīkyam' | 'anapatrapā'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 9) | `AFFLICTEDCLAUSE` | all six in every afflicted moment |
| [9, 13) | `UNWHOLESOMECLAUSE` | pair in every unwholesome moment |
| [0, 13) | `S` | distinct scopes, not exclusive totals |

## 5. Translation

### Literal Translation

> Delusion, heedlessness, laziness, lack of faith, sluggishness, and
> agitation are always present in the afflicted. But shamelessness and lack
> of moral caution are always present in the unwholesome.

### Bhāṣya-informed study translation

> Delusion, heedlessness, laziness, lack of faith, sluggishness, and
> agitation are always present in afflicted consciousness; shamelessness and
> lack of moral caution are always present in unwholesome consciousness.

## 6. Philosophical Translation

> The six occur always and only in afflicted consciousness; this
> does not make them its only factors. The quoted ten count five
> separate affliction factors and five afflicted modes of universal
> factors. Sluggishness completes the six. Predominance names a
> disposition without separating sluggishness from agitation.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| kleśa-mahābhūmika | affliction great-ground | always, only in the afflicted |
| moha | delusion | avidyā |
| pramāda | heedlessness | opposed to heedfulness |
| kauśīdya | laziness | opposed to vigor |
| āśraddhya | lack of faith | opposed to faith |
| styāna | sluggishness | heaviness, unworkability |
| auddhatya | agitation | non-pacification |
| muṣita-smṛtitā | lost recollection | mindfulness afflicted |
| vikṣepa | distraction | concentration afflicted; disputed |
| akuśala-mahābhūmika | unwholesome great-ground | the two; narrower |

## 8. Logical Determination

**Kārikā with Bhāṣya-resolved second scope.** The lexical SEM
records the six and the pair under their respective scopes. Prose
checks add the six's restriction to afflicted consciousness and the
interpretation of the quoted ten.
Afflicted includes an illustrative non-unwholesome case; unwholesome
is not substituted for the wider range.

```nltk-sem
presence : \f.\c.Present(c,f)
afflicted_condition : \P.\c.(AfflictedMoment(c) -> P(c))
always_scope : \P.all c.P(c)
unwholesome_scope : \P.all c.(UnwholesomeMoment(c) -> P(c))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all c.(AfflictedMoment(c) -> (Present(c,delusion) & Present(c,heedlessness) & Present(c,laziness) & Present(c,faithlessness) & Present(c,sluggishness) & Present(c,agitation))) & all c.(UnwholesomeMoment(c) -> (Present(c,shamelessness) & Present(c,lack_caution))))

# THEORY prose_scope_and_recitation
# EXPECT prose_scope_and_recitation T
all c.(UnwholesomeMoment(c) -> AfflictedMoment(c))
all c f.((Present(c,f) & AfflictionKind(f)) -> AfflictedMoment(c))
all x.(RecitedTen(x) <-> (SeparateFive(x) | AfflictedMode(x)))
all x.(AfflictionKind(x) <-> (SeparateFive(x) | x = sluggishness))
all c.(AfflictedMoment(c) -> (Present(c,sluggishness) & Present(c,agitation)))

# THEORY rejected_afflicted_equals_unwholesome
# EXPECT rejected_afflicted_equals_unwholesome F
all c.(AfflictedMoment(c) <-> UnwholesomeMoment(c))

# THEORY rejected_six_are_only_present_factors
# EXPECT rejected_six_are_only_present_factors F
all c f.((AfflictedMoment(c) & Present(c,f)) -> AfflictionKind(f))

# THEORY rejected_recited_ten_equal_six
# EXPECT rejected_recited_ten_equal_six F
all x.(RecitedTen(x) <-> AfflictionKind(x))

# THEORY rejected_predominance_separates_pair
# EXPECT rejected_predominance_separates_pair F
exists c.(AfflictedMoment(c) & Present(c,sluggishness) & -Present(c,agitation))
```

```nltk-valuation
delusion => delusion_kind
heedlessness => heedlessness_kind
laziness => laziness_kind
faithlessness => faithlessness_kind
sluggishness => sluggishness_kind
agitation => agitation_kind
shamelessness => shamelessness_kind
lack_caution => lack_caution_kind
AfflictedMoment => {unwholesome_moment,obscured_moment}
UnwholesomeMoment => {unwholesome_moment}
AfflictionKind => {delusion_kind,heedlessness_kind,laziness_kind,faithlessness_kind,sluggishness_kind,agitation_kind}
UnwholesomeKind => {shamelessness_kind,lack_caution_kind}
SeparateFive => {faithlessness_kind,laziness_kind,delusion_kind,agitation_kind,heedlessness_kind}
AfflictedMode => {lost_mindfulness,distraction,unclear_comprehension,improper_attention,false_resolution}
RecitedTen => {faithlessness_kind,laziness_kind,lost_mindfulness,distraction,delusion_kind,unclear_comprehension,improper_attention,false_resolution,agitation_kind,heedlessness_kind}
ModeOf => {(lost_mindfulness,mindfulness_kind),(distraction,concentration_kind),(unclear_comprehension,comprehension_kind),(improper_attention,attention_kind),(false_resolution,resolution_kind)}
Present => {(unwholesome_moment,delusion_kind),(unwholesome_moment,heedlessness_kind),(unwholesome_moment,laziness_kind),(unwholesome_moment,faithlessness_kind),(unwholesome_moment,sluggishness_kind),(unwholesome_moment,agitation_kind),(unwholesome_moment,shamelessness_kind),(unwholesome_moment,lack_caution_kind),(unwholesome_moment,feeling_kind),(obscured_moment,delusion_kind),(obscured_moment,heedlessness_kind),(obscured_moment,laziness_kind),(obscured_moment,faithlessness_kind),(obscured_moment,sluggishness_kind),(obscured_moment,agitation_kind),(obscured_moment,feeling_kind),(clear_moment,feeling_kind)}
```

The presence relation is a partial inventory: it omits the other
universal factors rather than asserting their absence. ModeOf records
the main explanation of the ten-recitation; only the first two
identifications are explicitly glossed before “and so on.” Those
who distinguish distraction from wrong concentration require a
different analysis, not silently incorporated into this valuation.
The fourfold comparison is about the quoted classifications, not
whether feeling can occur in an afflicted episode.

## 9. Interpretive Note

**Translation note.** The commentary identifies delusion with ignorance; heedlessness with failure to cultivate wholesome dharmas; laziness with lack of energetic arousal; lack of faith with lack of clarity; sluggishness with unworkability of body and consciousness; and agitation with non-pacification of consciousness. It discusses whether the first group is only afflicted and records a damaged retort, a recitation example, and a bodily-sluggishness analogy.

Five of the ten are kept as the separately counted afflicted factors, with sluggishness added to make six. The other five are modes. And so on completes them: lack of clear comprehension is discriminative comprehension afflicted, improper attention is attention afflicted, false resolution is resolution afflicted. Not extra definitions spelled out here.

The first alternative does not say feeling cannot occur in afflicted consciousness. It is classification in the comparison. Sluggishness is not silently added to the second row. Its omission is the next question.

The retort is damaged. Recitation against intention is the contrast. Not a restored first compound. Bodily sluggishness is the feeling analogy, not expanded, and not sleep.

In the Organon reading, Cognition governs Perception and Conception
without collapsing into consciousness or Mind. An afflicted mode
of discriminative comprehension does not become a new governing
Cognition. Class membership, occurrence, and predominance must
retain their different logical roles.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_26
    a vak:Karika ;
    rdfs:label "VAK 2.26" ;
    vak:hasTopic vak:AfflictedGround ;
    vak:belongsTo vak:Indriyanirdesa .

vak:AfflictedSix vak:onlyInAfflictedConsciousness true .
vak:UnwholesomeTwo vak:inEveryUnwholesomeConsciousness true .

organon:VAK_2_26_Interpretation
    organon:distinguishes vak:ClassMembership, vak:AfflictedMode,
        vak:PredominantDisposition .
```
