# VAK_2.47 — Groups of Names

## 1. Sanskrit (Devanāgarī)

```sanskrit
नामकायादयः संज्ञावाक्याक्षरसमुक्तयः ।
कामरूपाप्तसत्त्वाख्या निःष्यन्दाव्याकृतास्तथा ॥ २.४७ ॥
```

## 2. Sanskrit (IAST)

```text
nāmakāyādayaḥ saṃjñāvākyākṣarasamuktayaḥ /
kāmarūpāptasattvākhyā niḥṣyandāvyākṛtās tathā // 2.47 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| nāma-kāya-ādayaḥ | nom. pl. m.; compound | groups of names and the rest |
| saṃjñā-vākya-akṣara-samuktayaḥ | nom. pl. f.; compound | collections of designations, sentences, and syllables respectively |
| kāma-rūpa-āpta | nom. pl. m.; compound | included in desire and form realms |
| sattva-ākhyā | nom. pl. m.; compound | classed with sentient beings |
| niḥṣyanda | nom. pl. m.; compound | homogeneous outflow |
| avyākṛta | nom. pl. m.; adjective | indeterminate |
| tathā | adverb | likewise |

Here *saṃjñā* means designation, not a substitution of that gloss
for reflection everywhere. The three collection-kinds correspond
respectively; they are not three synonyms for a single kind.
The final *tathā* carries selected classifications into 2.48's
same-class clause. It does not carry Desire/Form restriction there.

```text
# tokens: nāmakāyādayaḥ saṃjñāvākyākṣarasamuktayaḥ kāmarūpāptasattvākhyāḥ niḥṣyandāvyākṛtāḥ tathā
```

## 4. Grammar

The prose expands “and the rest” to sentence- and syllable-groups.
Its classification assigns the groups to the signifier, not the
signified. The other teachers' Formless/inexpressible extension
is an attributed alternative, not merged into the main Realm range.

```nltk-fcfg
% start S
# tokens: nāmakāyādayaḥ saṃjñāvākyākṣarasamuktayaḥ kāmarūpāptasattvākhyāḥ niḥṣyandāvyākṛtāḥ tathā
S[SEM=<(?definition & ?classification & ?continuation)>] -> DEFINITIONS[SEM=?definition] CLASSIFICATION[SEM=?classification] CONTINUATION[SEM=?continuation]
DEFINITIONS[SEM=<(CollectionOf(name_group,designation) & CollectionOf(sentence_group,sentence) & CollectionOf(syllable_group,syllable))>] -> GROUPS[CASE=nom,NUM=pl,CNT=3] COLLECTIONS[CASE=nom,NUM=pl,MATCH=respectively]
CLASSIFICATION[SEM=<all x.(GroupKind(x) -> (RealmOption(x,desire) & RealmOption(x,form) & SentientClassed(x) & HomogeneousOutflow(x) & Indeterminate(x)))>] -> REALMSENTIENT[CASE=nom,NUM=pl,REALMS=2] OUTFLOWETHICS[CASE=nom,NUM=pl]
CONTINUATION[SEM=<ContinuesTo(likewise,next_verse_same_class)>] -> LIKEWISE[REF=next_verse_selected_classes]
GROUPS[CASE=nom,NUM=pl,CNT=3] -> 'nāmakāyādayaḥ'
COLLECTIONS[CASE=nom,NUM=pl,MATCH=respectively] -> 'saṃjñāvākyākṣarasamuktayaḥ'
REALMSENTIENT[CASE=nom,NUM=pl,REALMS=2] -> 'kāmarūpāptasattvākhyāḥ'
OUTFLOWETHICS[CASE=nom,NUM=pl] -> 'niḥṣyandāvyākṛtāḥ'
LIKEWISE[REF=next_verse_selected_classes] -> 'tathā'
```

```nltk-dep
'nāmakāyādayaḥ' -> 'saṃjñāvākyākṣarasamuktayaḥ' | 'kāmarūpāptasattvākhyāḥ' | 'niḥṣyandāvyākṛtāḥ'
'tathā' -> 'niḥṣyandāvyākṛtāḥ'
```

The three constituent lengths are 2, 2, and 1. The final token's
dependency is local, but its predicate explicitly records the
cross-verse continuation. The co-arising objection in the debate
concerns a proposed name and its meaning, not the claim that
all sounds of a spoken sequence are simultaneous.

## 5. Translation

### Literal Translation

> The groups of names and the rest are collections of designation, sentence,
> and syllable. They are included in the desire and form realms,
> classed with sentient beings, homogeneous outflows, and indeterminate.
### Bhāṣya-informed study translation

> The groups of names and the rest are collections of designation, sentence,
> and syllable respectively. They belong to the Desire and Form Realms,
> are classed with sentient beings, are homogeneous outflows, and are
> indeterminate. Likewise [the classification continues in the next verse].
## 6. Philosophical Translation

> Three groups. Classed with the signifier, not the signified. Homogeneous outflow, unobscured-indeterminate. Succession pressures a single name-entity. The groups are maintained. Not settled.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| nāma-kāya | group of names | not a body |
| akṣara | syllable | not writing |
| kṛtāvadhi | fixed application | the conventional restriction |
| dyotaka | revealer | the claimed function |
| anabhilāpya | inexpressible | the other account of the formless |

## 8. Logical Determination

```nltk-sem
collections : (CollectionOf(name_group,designation) & CollectionOf(sentence_group,sentence) & CollectionOf(syllable_group,syllable))
classification : all x.(GroupKind(x) -> (RealmOption(x,desire) & RealmOption(x,form) & SentientClassed(x) & HomogeneousOutflow(x) & Indeterminate(x)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((CollectionOf(name_group,designation) & CollectionOf(sentence_group,sentence) & CollectionOf(syllable_group,syllable)) & all x.(GroupKind(x) -> (RealmOption(x,desire) & RealmOption(x,form) & SentientClassed(x) & HomogeneousOutflow(x) & Indeterminate(x))) & ContinuesTo(likewise,next_verse_same_class))

# THEORY prose_main_classification
# EXPECT prose_main_classification T
all x.(GroupKind(x) -> Unobscured(x))
all x y.((GroupKind(x) & RealmOption(x,y)) -> (y = desire | y = form))
Possesses(signifier,illustrative_group) & -Possesses(signified,illustrative_group)

# THEORY attributed_alternative
# EXPECT attributed_alternative T
AllowsFormless(other_teachers) & CallsInexpressible(other_teachers)

# THEORY rejected_three_collections_are_interchangeable
# EXPECT rejected_three_collections_are_interchangeable F
CollectionOf(name_group,syllable) & CollectionOf(syllable_group,designation)

# THEORY rejected_main_classification_includes_formless
# EXPECT rejected_main_classification_includes_formless F
exists x.(GroupKind(x) & RealmOption(x,formless))

# THEORY rejected_signified_possesses_signifiers_group
# EXPECT rejected_signified_possesses_signifiers_group F
Possesses(signified,illustrative_group) & Possesses(signifier,illustrative_group)
```

```nltk-valuation
name_group => name_group_kind
sentence_group => sentence_group_kind
syllable_group => syllable_group_kind
designation => designation_kind
sentence => sentence_kind
syllable => syllable_kind
desire => desire_realm
form => form_realm
formless => formless_realm
likewise => likewise_token
next_verse_same_class => next_verse_same_class_clause
signifier => signifying_person
signified => signified_example
illustrative_group => illustrative_group_token
other_teachers => other_teachers_account
GroupKind => {name_group_kind,sentence_group_kind,syllable_group_kind}
CollectionOf => {(name_group_kind,designation_kind),(sentence_group_kind,sentence_kind),(syllable_group_kind,syllable_kind)}
RealmOption => {(name_group_kind,desire_realm),(name_group_kind,form_realm),(sentence_group_kind,desire_realm),(sentence_group_kind,form_realm),(syllable_group_kind,desire_realm),(syllable_group_kind,form_realm)}
SentientClassed => {name_group_kind,sentence_group_kind,syllable_group_kind}
HomogeneousOutflow => {name_group_kind,sentence_group_kind,syllable_group_kind}
Indeterminate => {name_group_kind,sentence_group_kind,syllable_group_kind}
Unobscured => {name_group_kind,sentence_group_kind,syllable_group_kind}
ContinuesTo => {(likewise_token,next_verse_same_class_clause)}
Possesses => {(signifying_person,illustrative_group_token)}
AllowsFormless => {other_teachers_account}
CallsInexpressible => {other_teachers_account}
```

The three kind-labels are not three individual enduring name-entities.
The signifier example distinguishes possession from what is designated,
not an exhaustive theory of reference. The model preserves the main
classification and attributed alternative separately; it does not
settle the distinct-real debate or reconstruct speech comprehension.

## 9. Interpretive Note

**Translation note.** The commentary explains a name as making designation, a sentence as completing meaning, and a syllable as the audible minimum. It records other teachers' formless and inexpressible classifications, and debates whether a succession presupposes a single enduring name-entity. The groups themselves are maintained; the issue is not settled.

The final *tathā* begins a cross-verse transfer of sentient
classification, homogeneous outflow, and unobscured-indeterminate
status to same-class; 2.48 immediately adds further qualifications.
The sound/name debate must retain its production/revelation
alternatives and temporal objections, not a single verdict.

In the Organon reading, Cognition joins and governs Perception and
Conception and guides the Dharma Base, remaining distinct from
consciousness and Mind. Conventional designation, audible sequence,
and a postulated distinct linguistic entity are different explanatory
claims. Their relations must be tested without mistaking a collection
for a simultaneously sounded unit or a signifier for what is signified.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_47 a vak:Karika ; vak:hasTopic vak:NameGroups .
vak:NameEntity vak:settled false .
```
