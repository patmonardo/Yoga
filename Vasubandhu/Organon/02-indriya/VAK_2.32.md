# VAK_2.32 — The Distinctions

## 1. Sanskrit (Devanāgarī)

```sanskrit
अह्रीरगुरुता अवद्ये भयादर्शित्वमत्रपा ।
प्रेम श्रद्धा गुरुत्वं ह्रीः ते पुनः कामरूपयोः ॥ २.३२ ॥
```

## 2. Sanskrit (IAST)

```text
ahrīr agurutā avadye bhayādarśitvam atrapā /
prema śraddhā gurutvaṃ hrīḥ te punaḥ kāmarūpayoḥ // 2.32 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| ahrīḥ | nom. sg. f. | shamelessness |
| a-gurutā | nom. sg. f.; compound | lack of respect |
| avadye | loc. sg. n. | in the blameworthy |
| bhaya-adarśitvam | nom. sg. n.; compound | failure to see danger |
| atrapā | nom. sg. f. | lack of moral caution |
| prema | nom. sg. n. | affection |
| śraddhā | nom. sg. f. | faith |
| gurutvam | nom. sg. n. | respect |
| hrīḥ | nom. sg. f. | moral shame |
| te punaḥ | nominative dual pronoun + particle | those two, however: affection and respect in the restricted sense |
| kāma-rūpayoḥ | loc. dual; compound | in the desire and form realms |

The verse equates. The commentary qualifies.

The dual pronoun does not refer to the negative pair or to all
forms of faith and moral shame. Sandhi is opened for parsing.

```text
# tokens: ahrīḥ agurutā avadye bhayādarśitvam atrapā prema śraddhā gurutvam hrīḥ te punaḥ kāmarūpayoḥ
```

## 4. Grammar

Four nominal clauses: two definitions, two compact identifications,
then a dual anaphor with a dual realm-locative. The prose restricts
the identifications and the realm statement to person-directed forms.
The first definition pair is not withdrawn by the subsequent debate
over how failure to see danger differs from comprehension or ignorance.

```nltk-fcfg
% start S
# tokens: ahrīḥ agurutā avadye bhayādarśitvam atrapā prema śraddhā gurutvam hrīḥ te punaḥ kāmarūpayoḥ
S[SEM=<(?shame & ?caution & ?pair & ?range)>] -> SHAMECLAUSE[SEM=?shame] CAUTIONCLAUSE[SEM=?caution] PAIR[SEM=?pair] RANGE[SEM=?range]
SHAMECLAUSE[SEM=<DefinedAs(shamelessness,lack_respect)>] -> SHAMELESS[CASE=nom] NORESPECT[CASE=nom]
CAUTIONCLAUSE[SEM=<DefinedAs(lack_caution,failure_danger_blameworthy)>] -> BLAMEWORTHY[CASE=loc] FAILURE[CASE=nom] UNCAUTIOUS[CASE=nom]
PAIR[SEM=<(ScopedAs(affection,faith) & ScopedAs(respect,moral_shame))>] -> AFFECTION[CASE=nom] FAITH[CASE=nom] RESPECT[CASE=nom] MORALSHAME[CASE=nom]
RANGE[SEM=<(RealmRange(affection,desire_form) & RealmRange(respect,desire_form))>] -> THOSE[NUM=du,REF=affection_respect] HOWEVER REALMS[CASE=loc,NUM=du]
SHAMELESS[CASE=nom] -> 'ahrīḥ'
NORESPECT[CASE=nom] -> 'agurutā'
BLAMEWORTHY[CASE=loc] -> 'avadye'
FAILURE[CASE=nom] -> 'bhayādarśitvam'
UNCAUTIOUS[CASE=nom] -> 'atrapā'
AFFECTION[CASE=nom] -> 'prema'
FAITH[CASE=nom] -> 'śraddhā'
RESPECT[CASE=nom] -> 'gurutvam'
MORALSHAME[CASE=nom] -> 'hrīḥ'
THOSE[NUM=du,REF=affection_respect] -> 'te'
HOWEVER -> 'punaḥ'
REALMS[CASE=loc,NUM=du] -> 'kāmarūpayoḥ'
```

```nltk-dep
'ahrīḥ' -> 'agurutā'
'atrapā' -> 'avadye' | 'bhayādarśitvam'
'prema' -> 'śraddhā'
'gurutvam' -> 'hrīḥ'
'te' -> 'prema' | 'gurutvam' | 'punaḥ' | 'kāmarūpayoḥ'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 2) | `SHAMECLAUSE` | shamelessness definition |
| [2, 5) | `CAUTIONCLAUSE` | lack-of-caution definition |
| [5, 9) | `PAIR` | compact identifications, prose-restricted |
| [9, 12) | `RANGE` | those two in Desire and Form |

## 5. Translation

### Literal Translation

> Shamelessness is lack of respect. Lack of moral caution is failure to see
> danger in what is blameworthy. Affection is faith; respect is moral shame.
> These occur in the desire and form realms.
### Bhāṣya-informed study translation

> Shamelessness is lack of respect; lack of moral caution is failure to see
> danger in the blameworthy. Affection here is person-directed faith,
> and respect is person-directed moral shame. These two forms occur
> in the Desire and Form Realms, not in the Formless Realm.
## 6. Philosophical Translation

> Compact identification is not unrestricted identity of ranges.
> Person-directed forms are restricted; faith and moral shame
> themselves are not thereby removed from wholesome Formless
> consciousness. Alternative accounts distinguish preceding esteem
> or acknowledgment from the attitude that follows.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| āhrīkya | shamelessness | lack of respect; alternatively, reference to oneself |
| anapatrāpya | lack of moral caution | failure to see danger; alternatively, reference to others |
| avadya | blameworthy | what good persons condemn |
| hrī | moral shame | the reverse |
| śraddhā | faith | esteem for qualities |
| prema | affection | craving, or fondness preceded by esteem |
| gaurava | respect | acknowledgment of authority |
| kāma-rūpa | desire and form | range of the person-directed forms |

## 8. Logical Determination

**Kārikā with prose-resolved reference.** DefinedAs records the
definition, not a reduction of lack of caution to ignorance or
comprehension. ScopedAs records the compact identification under
the final person-directed qualification; it does not erase the
alternative accounts. The finite examples below test ranges.

```nltk-sem
definition : \a.\b.DefinedAs(b,a)
scoped_identification : \a.\b.ScopedAs(b,a)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(DefinedAs(shamelessness,lack_respect) & DefinedAs(lack_caution,failure_danger_blameworthy) & (ScopedAs(affection,faith) & ScopedAs(respect,moral_shame)) & (RealmRange(affection,desire_form) & RealmRange(respect,desire_form)))

# THEORY prose_formless_scope
# EXPECT prose_formless_scope T
all x.(FormlessWholesome(x) -> (FaithPresent(x) & ShamePresent(x) & -PersonAffection(x) & -PersonRespect(x)))

# THEORY rejected_all_affection_equals_faith
# EXPECT rejected_all_affection_equals_faith F
all x.(AffectionExample(x) <-> FaithExample(x))

# THEORY rejected_affection_equals_respect_among_persons
# EXPECT rejected_affection_equals_respect_among_persons F
all x.(PersonAffectionExample(x) <-> PersonRespectExample(x))

# THEORY rejected_formless_lacks_faith_and_shame
# EXPECT rejected_formless_lacks_faith_and_shame F
all x.(FormlessWholesome(x) -> (-FaithPresent(x) & -ShamePresent(x)))
```

```nltk-valuation
shamelessness => shamelessness_factor
lack_respect => lack_respect_definition
lack_caution => lack_caution_factor
failure_danger_blameworthy => danger_failure_definition
affection => restricted_affection
faith => faith_factor
respect => restricted_respect
moral_shame => shame_factor
desire_form => desire_and_form_realms
DefinedAs => {(shamelessness_factor,lack_respect_definition),(lack_caution_factor,danger_failure_definition)}
ScopedAs => {(restricted_affection,faith_factor),(restricted_respect,shame_factor)}
RealmRange => {(restricted_affection,desire_and_form_realms),(restricted_respect,desire_and_form_realms)}
FormlessWholesome => {formless_wholesome_episode}
FaithPresent => {formless_wholesome_episode}
ShamePresent => {formless_wholesome_episode}
PersonAffection => {}
PersonRespect => {}
ComparisonExample => {suffering_origin,afflicted_affection,cessation_path,neither_example}
FaithExample => {suffering_origin,cessation_path}
AffectionExample => {afflicted_affection,cessation_path}
PersonExample => {children_companions,other_teachers,own_teacher,neither_person_example}
PersonAffectionExample => {children_companions,own_teacher}
PersonRespectExample => {other_teachers,own_teacher}
```

The fourfold examples are illustrations in the commentary, not
universal judgments about all children or teachers. The two
comparisons use distinct universes. The model does not reconstruct
the damaged positive reversal or decide between the attributed
accounts of affection and respect.
## 9. Interpretive Note

**Translation note.** The commentary qualifies affection and respect as person-directed forms of faith and moral shame, and says the pair is absent from the formless realm. It records alternative accounts and examples in which affection and faith, or respect and shame, may separate. The reversal of the negative pair is textually damaged; disposition is not treated as an extra latent entity.

The counts deferred these definitions. Lack of moral caution was
counted apart from discriminative comprehension and from delusion. The reply keeps that count.

The person examples show the relations can separate. They are not judgments about every parent or teacher. Others are reported. Not a final rejection of the verse's equations.

The reversal of the negative pair is damaged. Seeing danger is the contextual positive construal, not a secure
transcription of the damaged wording following the announced reversal. It wants collation. Disposition does not add a latent entity beside the named factor.

In the Organon reading, Cognition governs Perception and Conception
without collapsing into consciousness or Mind. The comprehension/
ignorance dilemma tests a proposed reduction of a mental factor;
it must not turn every use of seeing into governing Cognition.
Compact identification remains answerable to range and relation.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_32
    a vak:Karika ;
    rdfs:label "VAK 2.32" ;
    vak:hasTopic vak:FactorDistinctions ;
    vak:belongsTo vak:Indriyanirdesa .

vak:PersonDirectedForms vak:absentFrom vak:FormlessRealm .
vak:Faith vak:remainsInFormless true .

organon:VAK_2_32_Interpretation
    organon:distinguishes vak:ScopedIdentification, vak:OccasioningFactor,
        vak:PrecedingAttitude, vak:PersonDirectedForm .
```
