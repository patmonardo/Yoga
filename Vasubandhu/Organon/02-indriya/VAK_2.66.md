# VAK_2.66 — Twelve Kinds of Consciousness

## 1. Sanskrit (Devanāgarī)

```sanskrit
कुशलाकुशलं कामे निवृतानिवृतं मनः /
रूपारूप्येष्वकुशलादन्यत्र अनास्रवं द्विधा // २.६६ //
```

## 2. Sanskrit (IAST)

```text
kuśalākuśalaṃ kāme nivṛtānivṛtaṃ manaḥ /
rūpārūpyeṣv akuśalād anyatra anāsravaṃ dvidhā // 2.66 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| kuśalākuśalam | n. nom. sg. compound | Wholesome and unwholesome kinds. |
| kāme | loc. sg. | In the desire realm. |
| nivṛtānivṛtam | n. nom. sg. compound | Obscured and unobscured kinds. |
| manaḥ | n. nom. sg. | Mind or consciousness. |
| rūpārūpyeṣu | loc. pl. | In the Form and formless realms. |
| akuśalāt | abl. sg. | Apart from the unwholesome kind. |
| anyatra | indeclinable | Except. |
| anāsravam | n. nom. sg. | Uncontaminated consciousness. |
| dvidhā | numeral adverb | Twofold. |

The [running witness](../../Sources/kosabhasya.txt) reads
*kuśalākuśalaṃ kāme* and *akuśalādanyatra*. The former Organon
verse omitted *kuśala* and replaced *anyatra* with *ṛte*. The
normalized tokens open the sandhi before *anyatra*.

```text
# tokens: kuśalākuśalam kāme nivṛtānivṛtam manaḥ rūpārūpyeṣu akuśalāt anyatra anāsravam dvidhā
```

## 4. Grammar

The first four tokens give four kinds of desire-realm mind: wholesome,
unwholesome, obscured, and unobscured. The next three carry the kinds
to Form and formless realms except the unwholesome. The final two say
that uncontaminated mind is twofold. The Bhāṣya names the two
uncontaminated kinds and makes the resulting twelve-count explicit.

```nltk-fcfg
% start S
# tokens: kuśalākuśalam kāme nivṛtānivṛtam manaḥ rūpārūpyeṣu akuśalāt anyatra anāsravam dvidhā
S[SEM=<(?desire & ?higher & ?uncont)>] -> DESIRE[SEM=?desire] HIGHER[SEM=?higher] UNCONT[SEM=?uncont]
DESIRE[SEM=<(KindInRealm(wholesome,desire) & KindInRealm(unwholesome,desire) & KindInRealm(obscured,desire) & KindInRealm(unobscured,desire))>] -> GOOD_BAD[CASE=nom,NUM=sg] IN_DESIRE[CASE=loc,NUM=sg] OBSC_UNOBSC[CASE=nom,NUM=sg] MIND[CASE=nom,NUM=sg]
GOOD_BAD[CASE=nom,NUM=sg] -> 'kuśalākuśalam'
IN_DESIRE[CASE=loc,NUM=sg] -> 'kāme'
OBSC_UNOBSC[CASE=nom,NUM=sg] -> 'nivṛtānivṛtam'
MIND[CASE=nom,NUM=sg] -> 'manaḥ'
HIGHER[SEM=<(KindInRealm(wholesome,form) & KindInRealm(obscured,form) & KindInRealm(unobscured,form) & -KindInRealm(unwholesome,form) & KindInRealm(wholesome,formless) & KindInRealm(obscured,formless) & KindInRealm(unobscured,formless) & -KindInRealm(unwholesome,formless))>] -> IN_HIGHER[CASE=loc,NUM=pl] FROM_BAD[CASE=abl,NUM=sg] EXCEPT
IN_HIGHER[CASE=loc,NUM=pl] -> 'rūpārūpyeṣu'
FROM_BAD[CASE=abl,NUM=sg] -> 'akuśalāt'
EXCEPT -> 'anyatra'
UNCONT[SEM=<TwofoldUncontaminated(uncontaminated)>] -> UNCONT_MIND[CASE=nom,NUM=sg] TWO[COUNT=2]
UNCONT_MIND[CASE=nom,NUM=sg] -> 'anāsravam'
TWO[COUNT=2] -> 'dvidhā'
```

```nltk-dep
'manaḥ' -> 'kuśalākuśalam' | 'kāme' | 'nivṛtānivṛtam'
'rūpārūpyeṣu' -> 'akuśalāt' | 'anyatra'
'anāsravam' -> 'dvidhā'
```

**Feature chart checkpoints.** Desire spans [0, 4), Form and
formless [4, 7), uncontaminated [7, 9), and the root [0, 9). The
locative and ablative features constrain realm scope. The higher
realm exception applies to both Form and formless realms.

## 5. Translation

### Literal Translation

> In the desire realm, mind is wholesome and unwholesome, obscured and
> unobscured. In the Form and formless realms, [it has these kinds]
> except the unwholesome. Uncontaminated mind is twofold.

### Bhāṣya-informed study translation

> Mind is fourfold in the desire realm: wholesome, unwholesome,
> obscured-indeterminate, and unobscured-indeterminate. In Form and
> formless realms it has the other three kinds, without the
> unwholesome. Uncontaminated mind is twofold.

## 6. Philosophical Translation

> The verse sets out the inventory needed to ask which kind of mind
> can follow which. The Bhāṣya counts four desire-realm kinds, three
> in Form, three in formless, and two uncontaminated kinds: trainee
> and beyond-training.

## 7. Technical Vocabulary

| Term | Rendering |
|---|---|
| kuśala | Wholesome; present in all three realm inventories. |
| akuśala | Unwholesome; present only in the desire realm. |
| nivṛta | Obscured; specified as indeterminate in the Bhāṣya. |
| anivṛta | Unobscured; specified as indeterminate in the Bhāṣya. |
| anāsrava | Uncontaminated; trainee and beyond-training in the Bhāṣya. |

## 8. Logical Determination

**Kārikā, derived.** The root `SEM` assigns four kinds to desire,
three to each higher realm with explicit unwholesome exclusions, and
a twofold uncontaminated class. The twelve-count and the identities
of the final two kinds are Bhāṣya determinations. A succession rule
has not yet been stated; this observation stays in prose.

```nltk-sem
desire : KindInRealm(wholesome,desire) & KindInRealm(unwholesome,desire) & KindInRealm(obscured,desire) & KindInRealm(unobscured,desire)
higher : KindInRealm(wholesome,form) & KindInRealm(obscured,form) & KindInRealm(unobscured,form) & -KindInRealm(unwholesome,form) & KindInRealm(wholesome,formless) & KindInRealm(obscured,formless) & KindInRealm(unobscured,formless) & -KindInRealm(unwholesome,formless)
uncontaminated : TwofoldUncontaminated(uncontaminated)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(KindInRealm(wholesome,desire) & KindInRealm(unwholesome,desire) & KindInRealm(obscured,desire) & KindInRealm(unobscured,desire) & KindInRealm(wholesome,form) & KindInRealm(obscured,form) & KindInRealm(unobscured,form) & -KindInRealm(unwholesome,form) & KindInRealm(wholesome,formless) & KindInRealm(obscured,formless) & KindInRealm(unobscured,formless) & -KindInRealm(unwholesome,formless) & TwofoldUncontaminated(uncontaminated))

# THEORY prose_counts
# EXPECT prose_counts T
KindCount(desire,four) & KindCount(form,three) & KindCount(formless,three) & KindCount(uncontaminated,two)

# THEORY prose_uncontaminated_pair
# EXPECT prose_uncontaminated_pair T
Includes(uncontaminated,trainee) & Includes(uncontaminated,beyond_training)

# THEORY rejected_wholesome_absent_in_desire
# EXPECT rejected_wholesome_absent_in_desire F
KindInRealm(unwholesome,desire) & -KindInRealm(wholesome,desire)

# THEORY rejected_unwholesome_in_form
# EXPECT rejected_unwholesome_in_form F
KindInRealm(wholesome,form) & KindInRealm(unwholesome,form)

# THEORY rejected_unwholesome_in_formless
# EXPECT rejected_unwholesome_in_formless F
KindInRealm(wholesome,formless) & KindInRealm(unwholesome,formless)
```

```nltk-valuation
wholesome => good_kind
unwholesome => bad_kind
obscured => obscured_kind
unobscured => unobscured_kind
desire => desire_realm
form => form_realm
formless => formless_realm
uncontaminated => uncontaminated_class
trainee => trainee_kind
beyond_training => beyond_kind
four => four_count
three => three_count
two => two_count
KindInRealm => {(good_kind,desire_realm),(bad_kind,desire_realm),(obscured_kind,desire_realm),(unobscured_kind,desire_realm),(good_kind,form_realm),(obscured_kind,form_realm),(unobscured_kind,form_realm),(good_kind,formless_realm),(obscured_kind,formless_realm),(unobscured_kind,formless_realm)}
TwofoldUncontaminated => {uncontaminated_class}
KindCount => {(desire_realm,four_count),(form_realm,three_count),(formless_realm,three_count),(uncontaminated_class,two_count)}
Includes => {(uncontaminated_class,trainee_kind),(uncontaminated_class,beyond_kind)}
```

The finite valuation witnesses all ten realm-bound kinds and the
twofold uncontaminated class. Removing any positive membership or
adding an unwholesome higher-realm membership makes the verse
formula false.

## 9. Interpretive Note

**Translation note.** The Bhāṣya makes twelve kinds in all: four in
desire, three in Form, three in formless, and two uncontaminated.
The ten realm-bound kinds are contaminated; the two uncontaminated
kinds are trainee and beyond-training. The exclusion of the
unwholesome applies to both higher realms.

The verse supplies the inventory for the ensuing account of mental
succession. It does not yet say which kind can follow which.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_66 a vak:Karika ; vak:hasTopic vak:TwelveKindsOfConsciousness .
vak:DesireConsciousness vak:kinds 4 .
vak:FormConsciousness vak:kinds 3 .
vak:FormlessConsciousness vak:kinds 3 .
vak:UncontaminatedConsciousness vak:kinds 2 .
```
