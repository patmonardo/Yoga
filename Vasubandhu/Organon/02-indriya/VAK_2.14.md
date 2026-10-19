# VAK_2.14 — First Acquired as Maturation

## 1. Sanskrit (Devanāgarī)

```sanskrit
कामेष्वादौ विपाको द्वे लभ्यते नोपपादुकैः ।
तैः षड्वा सप्त वा अष्टौ वा षड् रूपेषु एकमुत्तरे ॥ २.१४ ॥
```

## 2. Sanskrit (IAST)

```text
kāmeṣv ādau vipāko dve labhyate nopapādukaiḥ /
taiḥ ṣaḍ vā sapta vā aṣṭau vā ṣaḍ rūpeṣu ekam uttare // 2.14 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| kāmeṣu | locative plural masculine noun | in the Desire-realm; plural realm designation |
| ādau | locative singular masculine noun, adverbial | initially |
| vipākaḥ | nominative singular masculine noun | as maturation; the classification carried through every count |
| dve | nominative dual neuter numeral | two [Faculties] |
| labhyate | present passive indicative, third person singular | is acquired; witness retains singular with dual two |
| na | negative particle | not; excludes spontaneous birth from the two-count |
| upapādukaiḥ | instrumental plural masculine adjective, substantival | by spontaneously born beings |
| taiḥ | instrumental plural masculine demonstrative | by those spontaneously born beings |
| ṣaṭ | cardinal numeral, nominative plural in context, twice | six [Faculties] |
| vā | disjunctive particle, repeated | or; alternatives within spontaneous Desire-realm birth |
| sapta | cardinal numeral, nominative plural in context | seven [Faculties] |
| aṣṭau | cardinal numeral, nominative plural in context | eight [Faculties] |
| rūpeṣu | locative plural neuter noun | in the Form realm; plural realm designation |
| ekam | nominative singular neuter numeral | one [Faculty] |
| uttare | locative singular adjective, substantival | in the higher [realm], specified as Formless |

The count is faculties first acquired as maturation. It is not every faculty present.

The running Bhāṣya reads *taiḥ*, matching Devanāgarī तैः; the earlier
IAST *teḥ* is corrected. The singular *labhyate* is retained, not silently
regularized.

**Grammar tokens.** External sandhi is opened; ṣaḍ is normalized to ṣaṭ.
The Sanskrit witness above remains unchanged apart from the stated taiḥ
correction.

```text
# tokens: kāmeṣu ādau vipākaḥ dve labhyate na upapādukaiḥ taiḥ ṣaṭ vā sapta vā aṣṭau vā ṣaṭ rūpeṣu ekam uttare
```

## 4. Grammar

The first clause supplies initial acquisition as maturation for all later
numerals. The negative qualifies the birth-agent, not acquisition in
general. *Taiḥ* resumes the excluded spontaneously born beings and
introduces their alternative counts. The Bhāṣya supplies the conditions
for those alternatives and identifies the higher realm as Formless.

```nltk-fcfg
% start S
# tokens: kāmeṣu ādau vipākaḥ dve labhyate na upapādukaiḥ taiḥ ṣaṭ vā sapta vā aṣṭau vā ṣaṭ rūpeṣu ekam uttare
S[SEM=<(?first & ?spontaneous & ?form & ?higher)>] -> FIRST[SEM=?first] SPONTANEOUS[SEM=?spontaneous] FORMCLAUSE[SEM=?form] HIGHER[SEM=?higher]
FIRST[SEM=<(InitialMaturationScope & InitialCount(?case,?count))>] -> DESIRE[CASE=loc] INITIAL RESULT TWO[CNT=2,SEM=?count] ACQUIRE[NUM=sg] NOT BIRTH[CASE=ins,REF=spontaneous,SEM=?case]
SPONTANEOUS[SEM=<(AlternativeCount(spontaneous_desire,?six) & AlternativeCount(spontaneous_desire,?seven) & AlternativeCount(spontaneous_desire,?eight))>] -> THEM[CASE=ins,REF=spontaneous] SIX[CNT=6,SEM=?six] OR SEVEN[CNT=7,SEM=?seven] OR EIGHT[CNT=8,SEM=?eight] OR
FORMCLAUSE[SEM=<InitialCount(?case,?count)>] -> SIX[CNT=6,SEM=?count] FORM[CASE=loc,SEM=?case]
HIGHER[SEM=<InitialCount(?case,?count)>] -> ONE[CNT=1,SEM=?count] HIGHERR[CASE=loc,SEM=?case]
DESIRE[CASE=loc] -> 'kāmeṣu'
INITIAL -> 'ādau'
RESULT -> 'vipākaḥ'
TWO[CNT=2,SEM=<two>] -> 'dve'
ACQUIRE[NUM=sg] -> 'labhyate'
NOT -> 'na'
BIRTH[CASE=ins,REF=spontaneous,SEM=<nonspontaneous_desire>] -> 'upapādukaiḥ'
THEM[CASE=ins,REF=spontaneous] -> 'taiḥ'
SIX[CNT=6,SEM=<six>] -> 'ṣaṭ'
OR -> 'vā'
SEVEN[CNT=7,SEM=<seven>] -> 'sapta'
EIGHT[CNT=8,SEM=<eight>] -> 'aṣṭau'
FORM[CASE=loc,SEM=<form_case>] -> 'rūpeṣu'
ONE[CNT=1,SEM=<one>] -> 'ekam'
HIGHERR[CASE=loc,SEM=<formless_case>] -> 'uttare'
```

The first clause's negative and birth-agent are interpreted jointly as
the non-spontaneous case. The grammar projects the count claims;
it does not derive their biological or cosmological truth.

```nltk-dep
'labhyate' -> 'kāmeṣu' | 'ādau' | 'vipākaḥ' | 'dve' | 'upapādukaiḥ'
'upapādukaiḥ' -> 'na'
'taiḥ' -> 'ṣaṭ' | 'sapta' | 'aṣṭau' | 'vā'
'ṣaṭ' -> 'rūpeṣu'
'ekam' -> 'uttare'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 7) | `FIRST` | two in non-spontaneous Desire-realm birth, under initial maturation scope |
| [7, 14) | `SPONTANEOUS` | resumed birth-agent, six/seven/eight alternatives |
| [14, 16) | `FORMCLAUSE` | six in the Form realm |
| [16, 18) | `HIGHER` | one in the higher realm |
| [0, 18) | `S` | scope carried through all counts |

## 5. Translation

### Literal Translation

> In the desire realm, initially, two are acquired as maturation, not by the
> spontaneously born. By them, six or seven or eight. Six in the form realm.
> One in the higher.

### Bhāṣya-informed study translation

> In the desire realm, two are first acquired as maturation, but not by the
> spontaneously born. By them, six, seven, or eight; in the Form realm, six;
> in the higher, Formless realm, one.

## 6. Philosophical Translation

> The initial maturation-count does not enumerate everything present at
> relinking. Mind and neutral feeling occur there but are afflicted,
> not maturation under this question.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| lābha | acquisition | the new question |
| ādau / prathamataḥ | initially | first of the new continuum |
| vipāka | maturation | the predicate of the count |
| pratisaṃdhi | relinking | where mind and neutral feeling are afflicted |
| upapāduka | spontaneously born | six, seven, or eight |
| aṇḍaja, jarāyuja, saṃsvedaja | egg-born, womb-born, moisture-born | the two |
| vyañjana | sexual characteristic | none, one, both; not a word |
| kliṣṭa | afflicted | why mind and neutral feeling are out of the count |

The birth-modes are the account. They are not rewritten as biology.

## 8. Logical Determination

**Kārikā, derived.** The SEM records the shared initial-maturation scope
and count alternatives. The Bhāṣya assigns each spontaneous count to a
sexual-characteristic condition and supplies the actual Faculty-sets.

```nltk-sem
initial_count : \c.\n.InitialCount(c,n)
alternative_count : \c.\n.AlternativeCount(c,n)
shared_scope : InitialMaturationScope
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(InitialMaturationScope & InitialCount(nonspontaneous_desire,two) & AlternativeCount(spontaneous_desire,six) & AlternativeCount(spontaneous_desire,seven) & AlternativeCount(spontaneous_desire,eight) & InitialCount(form_case,six) & InitialCount(formless_case,one))

# THEORY prose
# EXPECT prose T
(InitialCount(spontaneous_none,six) & InitialCount(spontaneous_one,seven) & InitialCount(spontaneous_both,eight))
all x.(InitiallyMatures(x,nonspontaneous_desire) <-> (x = body_f | x = life_f))
all x.(InitiallyMatures(x,formless_case) <-> (x = life_f))
all x.(InitiallyMatures(x,form_case) <-> InitiallyMatures(x,spontaneous_none))
all x.(AtRelinking(x) -> (Afflicted(x) & -MaturationAtRelinking(x)))
(AtRelinking(mind_f) & AtRelinking(neutral_f))

# THEORY rejected_presence_implies_maturation
# EXPECT rejected_presence_implies_maturation F
all x.(AtRelinking(x) -> MaturationAtRelinking(x))

# THEORY rejected_formless_lacks_mind
# EXPECT rejected_formless_lacks_mind F
-AtRelinking(mind_f) & InitiallyMatures(life_f,formless_case)

# THEORY rejected_initial_six_include_mind
# EXPECT rejected_initial_six_include_mind F
InitiallyMatures(mind_f,form_case) & InitiallyMatures(life_f,form_case)
```

```nltk-valuation
nonspontaneous_desire => desire_nonspontaneous
spontaneous_desire => desire_spontaneous
spontaneous_none => desire_spontaneous_none
spontaneous_one => desire_spontaneous_one
spontaneous_both => desire_spontaneous_both
form_case => form_initial
formless_case => formless_initial
two => count_two
six => count_six
seven => count_seven
eight => count_eight
one => count_one
body_f => body
life_f => life
mind_f => mind
neutral_f => neutral
InitialMaturationScope => True
InitialCount => {(desire_nonspontaneous,count_two),(desire_spontaneous_none,count_six),(desire_spontaneous_one,count_seven),(desire_spontaneous_both,count_eight),(form_initial,count_six),(formless_initial,count_one)}
AlternativeCount => {(desire_spontaneous,count_six),(desire_spontaneous,count_seven),(desire_spontaneous,count_eight)}
InitiallyMatures => {(body,desire_nonspontaneous),(life,desire_nonspontaneous),(eye,desire_spontaneous_none),(ear,desire_spontaneous_none),(nose,desire_spontaneous_none),(tongue,desire_spontaneous_none),(body,desire_spontaneous_none),(life,desire_spontaneous_none),(eye,desire_spontaneous_one),(ear,desire_spontaneous_one),(nose,desire_spontaneous_one),(tongue,desire_spontaneous_one),(body,desire_spontaneous_one),(life,desire_spontaneous_one),(male,desire_spontaneous_one),(eye,desire_spontaneous_both),(ear,desire_spontaneous_both),(nose,desire_spontaneous_both),(tongue,desire_spontaneous_both),(body,desire_spontaneous_both),(life,desire_spontaneous_both),(female,desire_spontaneous_both),(male,desire_spontaneous_both),(eye,form_initial),(ear,form_initial),(nose,form_initial),(tongue,form_initial),(body,form_initial),(life,form_initial),(life,formless_initial)}
AtRelinking => {mind,neutral}
Afflicted => {mind,neutral}
MaturationAtRelinking => {}
```

The one-characteristic case uses Male-Faculty as one representative;
Female-Faculty can replace it without changing the count. The two
characteristics condition which Faculties are counted; they are not
themselves counted as additional entities. The relinking predicates
model the two factors under discussion, not everything present then.
Count-to-set agreement requires separate cardinality tests. These finite
checks do not prove the account's birth-mode claims.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): In the desire realm, at the beginning, two faculties
are acquired as maturation, the body-faculty and the life-faculty, but not
by the spontaneously born. By the spontaneously born, six, seven, or eight
are acquired: six without sexual characteristic, seven with one, eight
with both. In the form realm, six. In the higher, the formless, one: life
alone. Mind and neutral feeling are not among these, because at relinking
both are necessarily afflicted.

2.13 closed the distinctions of kind. This opens acquisition. What can be connected with a realm does not settle what is first acquired there as maturation. The formless eight of 2.12 are another question. One here is the maturation-count, not the absence of mind.

Higher is attainment and rebirth, not a direction, and not liberation. The triad stays unconnected.

Interpretation: consequence is the predicate. Membership is which faculties fall under it. The doctrine is inherited. The analysis is this chapter. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_14
    a vak:Karika ;
    rdfs:label "VAK 2.14" ;
    vak:hasTopic vak:InitialAcquisition ;
    vak:belongsTo vak:Indriyanirdesa .

vak:NonSpontaneousDesire vak:initiallyAcquires vak:Body, vak:Life .
vak:FormlessRealm vak:initiallyAcquires vak:Life .
vak:MindAtRelinking vak:present true ;
    vak:acquiredAsMaturation false .

organon:VAK_2_14_Interpretation
    organon:distinguishes vak:PresenceAtRelinking,
        vak:InitialAcquisitionAsMaturation .
```
