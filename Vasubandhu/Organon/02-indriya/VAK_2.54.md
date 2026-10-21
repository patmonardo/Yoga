# VAK_2.54 — Pervasive Cause and Maturation Cause

## 1. Sanskrit (Devanāgarī)

```sanskrit
सर्वत्रगाख्यः क्लिष्टानां स्वभूमौ पूर्वसर्वगाः ।
विपाकहेतुरशुभाः कुशलाश्चैव सास्रवाः ॥ २.५४ ॥
```

## 2. Sanskrit (IAST)

```text
sarvatragākhyaḥ kliṣṭānāṃ svabhūmau pūrvasarvagāḥ /
vipākahetur aśubhāḥ kuśalāś caiva sāsravāḥ // 2.54 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sarvatraga-ākhyaḥ | masculine nominative singular compound | the cause named pervasive |
| kliṣṭānām | genitive plural | of later afflicted dharmas, as the Bhāṣya resolves |
| sva-bhūmau | locative singular compound | within the same level as cause and effect |
| pūrva-sarvagāḥ | masculine nominative plural compound | pervasive dharmas arisen earlier than the afflicted result |
| vipāka-hetuḥ | masculine nominative singular compound | maturation cause |
| aśubhāḥ | masculine nominative plural adjective | unwholesome |
| kuśalāḥ sāsravāḥ | masculine nominative plural adjectives | wholesome dharmas qualified by influx |

**Grammar tokens.** Sandhi is opened at *vipākahetur aśubhāḥ* and *kuśalāś caiva*. The Bhāṣya resolves *pūrva-* as earlier arising and *kliṣṭānām* as the later afflicted results. The coordination makes both unwholesome and wholesome-with-influx
dharmas maturation causes. Here *caiva* is additive and emphatic;
the Bhāṣya supplies the explicit exclusions of other classes.

```text
# tokens: sarvatragākhyaḥ kliṣṭānām svabhūmau pūrvasarvagāḥ vipākahetuḥ aśubhāḥ kuśalāḥ ca eva sāsravāḥ
```

## 4. Grammar

```nltk-fcfg
% start S
# tokens: sarvatragākhyaḥ kliṣṭānām svabhūmau pūrvasarvagāḥ vipākahetuḥ aśubhāḥ kuśalāḥ ca eva sāsravāḥ
S[SEM=<(?pervasive & ?maturation)>] -> PERVASIVE[SEM=?pervasive] MATURATION[SEM=?maturation]
PERVASIVE[SEM=<(PervasiveCause(prior_pervasive,later_afflicted) & Prior(prior_pervasive,later_afflicted) & SameLevel(prior_pervasive,later_afflicted))>] -> PHEAD[CASE=nom,NUM=sg] AFFLICTED[CASE=gen,NUM=pl] LEVEL[CASE=loc,NUM=sg,REF=own] PRIORP[CASE=nom,NUM=pl,TIME=prior]
PHEAD[CASE=nom,NUM=sg] -> 'sarvatragākhyaḥ'
AFFLICTED[CASE=gen,NUM=pl] -> 'kliṣṭānām'
LEVEL[CASE=loc,NUM=sg,REF=own] -> 'svabhūmau'
PRIORP[CASE=nom,NUM=pl,TIME=prior] -> 'pūrvasarvagāḥ'
MATURATION[SEM=<(?bad & ?good & ?influx)>] -> MHEAD[CASE=nom,NUM=sg] BAD[CASE=nom,NUM=pl,SEM=?bad] GOOD[CASE=nom,NUM=pl,SEM=?good] AND EMPH INFLUX[CASE=nom,NUM=pl,SEM=?influx]
MHEAD[CASE=nom,NUM=sg] -> 'vipākahetuḥ'
BAD[CASE=nom,NUM=pl,SEM=<(Unwholesome(unwholesome) & MaturationCause(unwholesome))>] -> 'aśubhāḥ'
GOOD[CASE=nom,NUM=pl,SEM=<(Wholesome(wholesome_influx) & MaturationCause(wholesome_influx))>] -> 'kuśalāḥ'
AND -> 'ca'
EMPH -> 'eva'
INFLUX[CASE=nom,NUM=pl,SEM=<HasInflux(wholesome_influx)>] -> 'sāsravāḥ'
```

```nltk-dep
'sarvatragākhyaḥ' -> 'kliṣṭānām' | 'svabhūmau' | 'pūrvasarvagāḥ'
'vipākahetuḥ' -> 'aśubhāḥ' | 'kuśalāḥ' | 'ca' | 'eva' | 'sāsravāḥ'
```

**Feature chart checkpoints.** Pervasive cause spans [0, 4), maturation cause [4, 10), and the root [0, 10). Prior-time, own-level locative, afflicted genitive, and wholesome-with-influx nominative features constrain their constituents. The verse names the two maturation-cause classes. `Eva` marks emphasis
here; the Bhāṣya supplies the explicit exclusions and cross-class scope.

## 5. Translation

### Literal Translation

> The cause called pervasive consists of prior pervasive dharmas of their
> own level, for the afflicted there. Maturation cause is unwholesome and
> wholesome with influx.

### Bhāṣya-informed study translation

> The cause called pervasive is the prior pervasive dharmas of a level,
> for later afflicted dharmas on that same level. Maturation cause is
> unwholesome and wholesome with influx.

## 6. Philosophical Translation

> Pervasive cause names the passage from an earlier pervasive dharma to later affliction on its level. Maturation cause names unwholesome or wholesome-with-influx dharmas under a different causal determination. The Bhāṣya tests the latter through weakness, craving, and the ripening of a continuum.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| sarvatraga-hetu | pervasive cause | earlier pervasive dharma causing later affliction on its level; cross-class reach is Bhāṣya specification |
| vipāka-hetu | maturation cause | unwholesome and wholesome-with-influx causes named in the verse |
| abhiṣyandita | moistened | by craving in the Bhāṣya seed analogy |
| santati-pariṇāma | transformation of a continuum | Bhāṣya account of maturation reaching its result; distinguishes it from other causal results |

## 8. Logical Determination

**Kārikā, derived.** The root `SEM` joins two separate causal definitions. The Bhāṣya then explains why pervasive cause crosses abandonment classes within one level and why indeterminate and uncontaminated dharmas do not qualify as maturation causes. Its exchange about *vipāka* is modeled as an attributed argument, not silently inserted into the verse.

```nltk-sem
pervasive : PervasiveCause(prior_pervasive,later_afflicted) & Prior(prior_pervasive,later_afflicted) & SameLevel(prior_pervasive,later_afflicted)
maturation : Unwholesome(unwholesome) & MaturationCause(unwholesome) & Wholesome(wholesome_influx) & MaturationCause(wholesome_influx) & HasInflux(wholesome_influx)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(PervasiveCause(prior_pervasive,later_afflicted) & Prior(prior_pervasive,later_afflicted) & SameLevel(prior_pervasive,later_afflicted)) & (Unwholesome(unwholesome) & MaturationCause(unwholesome) & Wholesome(wholesome_influx) & MaturationCause(wholesome_influx) & HasInflux(wholesome_influx))

# THEORY prose_cross_class
# EXPECT prose_cross_class T
DifferentClass(prior_pervasive,later_afflicted) & PervasiveCause(prior_pervasive,later_afflicted)

# THEORY prose_exclusions
# EXPECT prose_exclusions T
Weak(indeterminate) & -MaturationCause(indeterminate) & Unmoistened(uncontaminated) & -MaturationCause(uncontaminated)

# THEORY rejected_same_class_only
# EXPECT rejected_same_class_only F
SameClass(prior_pervasive,later_afflicted) & PervasiveCause(prior_pervasive,later_afflicted)

# THEORY rejected_indeterminate_matures
# EXPECT rejected_indeterminate_matures F
MaturationCause(indeterminate) & Weak(indeterminate)

# THEORY rejected_uncontaminated_matures
# EXPECT rejected_uncontaminated_matures F
MaturationCause(uncontaminated) & Unmoistened(uncontaminated)

# THEORY rejected_immediate_maturation
# EXPECT rejected_immediate_maturation F
ImmediateResult(unwholesome,result) & MaturationCause(unwholesome)
```

```nltk-valuation
prior_pervasive => pp
later_afflicted => la
unwholesome => uw
wholesome_influx => wi
indeterminate => id
uncontaminated => uc
result => rs
PervasiveCause => {(pp,la)}
Prior => {(pp,la)}
SameLevel => {(pp,la)}
DifferentClass => {(pp,la)}
SameClass => {}
MaturationCause => {uw,wi}
Unwholesome => {uw}
Wholesome => {wi}
HasInflux => {wi}
Weak => {id}
Unmoistened => {uc}
ImmediateResult => {}
```

The finite model witnesses the verse and the Bhāṣya's cross-class and exclusion claims. Its false theories reject a same-class-only pervasive cause, indeterminate or uncontaminated maturation cause, and immediate maturation. The model checks these stated distinctions, not the complete ontology of all dharmas.

## 9. Interpretive Note

The Bhāṣya sets pervasive cause apart from homogeneous cause because prior pervasive dharmas can cause later afflicted dharmas in another abandonment class on the same level. Its discussion of an afflicted noble person's cause includes an attributed Kāśmīrī position and a response about an already-abandoned cause; these are not extra conditions stated by the verse.

For maturation cause, the Bhāṣya excludes indeterminate dharmas as too weak and uncontaminated dharmas as unmoistened by craving. It discusses *vipāka* as dissimilar ripening and records a Vaibhāṣika view allowing two uses, then argues that genuine ripening requires a resulting culmination from transformation of a continuum. Its final temporal claim denies maturation together with the karma or immediately after it and says maturation depends on a stream. These stages of the argument remain attributed rather than collapsed into one unqualified definition. The temporal classification of the six causes begins with 2.55.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_54 a vak:Karika ; vak:hasTopic vak:PervasiveCause, vak:MaturationCause .
vak:VipakaMeaning vak:hasAttributedDebate true .
```
