# VAK_2.15 — What Ceases at Death

## 1. Sanskrit (Devanāgarī)

```sanskrit
निरोधयत्युपरमान्नारूप्ये जीवितं मनः ।
उपेक्षां चैव रूपेऽष्टौ कामे दश नवाष्टौ वा ॥ २.१५ ॥
```

## 2. Sanskrit (IAST)

```text
nirodhayaty uparamān nārūpye jīvitaṃ manaḥ /
upekṣāṃ caiva rūpe 'ṣṭau kāme daśa navāṣṭau vā // 2.15 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| nirodhayati | present causative indicative, third person singular | brings to cessation; subject supplied as the dying person |
| uparamān nārūpye | uncertain transmitted sequence | read through the Bhāṣya's death question as death in the Formless realm; division remains unsettled |
| jīvitam | accusative singular neuter noun | Life-Faculty, object of brings to cessation |
| manaḥ | accusative singular neuter noun | Mind-Faculty |
| upekṣām | accusative singular feminine noun | Neutral-Feeling Faculty |
| ca eva | coordinating and emphatic particles | and; completes the three named objects |
| rūpe | locative singular neuter noun | in the Form realm |
| aṣṭau | cardinal numeral, accusative plural in context | eight [Faculties] |
| kāme | locative singular masculine noun | in the Desire-realm |
| daśa / nava / aṣṭau | cardinal numerals, accusative plural in context | ten, nine, or eight [Faculties] |
| vā | disjunctive particle | or; the conditional alternatives |

Nirodha here is cessation of possessed faculties at death. It is not abandonment, and it is not the deferred identity.

**Grammar tokens.** Sandhi is opened where secure. The uncertain opening
sequence is retained as a single token, `uparamān-nārūpye`; its semantic
projection is explicitly Bhāṣya-resolved, not a settled morphological
analysis. The Sanskrit witness remains unchanged.

```text
# tokens: nirodhayati uparamān-nārūpye jīvitam manaḥ upekṣām ca eva rūpe aṣṭau kāme daśa nava aṣṭau vā
```

## 4. Grammar

The named accusatives identify the Formless terminal set. Later numerals
resume the cessation predicate in the other realms. The prose assigns
the Desire-realm alternatives to sexual characteristics and restricts
the base counts to afflicted or indeterminate consciousness. Gradual
death and the wholesome addition come from the next verse's opening,
not from tokens silently inserted into this verse.

```nltk-fcfg
% start S
# tokens: nirodhayati uparamān-nārūpye jīvitam manaḥ upekṣām ca eva rūpe aṣṭau kāme daśa nava aṣṭau vā
S[SEM=<(?formless & ?form & ?desire)>] -> FORMLESS[SEM=?formless] FORM[SEM=?form] DESIRE[SEM=?desire]
FORMLESS[SEM=<(DeathCessationScope & ?member(?life,?case) & ?member(?mind,?case) & ?member(?neutral,?case))>] -> CEASE[SEM=?member] OPENING[WITNESS=uncertain,SUPPLIED=prose,SEM=?case] LIFE[CASE=acc,SEM=?life] MIND[CASE=acc,SEM=?mind] NEUTRAL[CASE=acc,SEM=?neutral] AND EMPHASIS
FORM[SEM=<TerminalCount(?case,?count)>] -> FORMR[CASE=loc,SEM=?case] EIGHT[CNT=8,SEM=?count]
DESIRE[SEM=<(AlternativeCount(?case,?ten) & AlternativeCount(?case,?nine) & AlternativeCount(?case,?eight))>] -> DESIRER[CASE=loc,SEM=?case] TEN[CNT=10,SEM=?ten] NINE[CNT=9,SEM=?nine] EIGHT[CNT=8,SEM=?eight] OR
CEASE[SEM=<\f.\c.CeasesAt(f,c)>] -> 'nirodhayati'
OPENING[WITNESS=uncertain,SUPPLIED=prose,SEM=<formless_base>] -> 'uparamān-nārūpye'
LIFE[CASE=acc,SEM=<life_f>] -> 'jīvitam'
MIND[CASE=acc,SEM=<mind_f>] -> 'manaḥ'
NEUTRAL[CASE=acc,SEM=<neutral_f>] -> 'upekṣām'
AND -> 'ca'
EMPHASIS -> 'eva'
FORMR[CASE=loc,SEM=<form_base>] -> 'rūpe'
EIGHT[CNT=8,SEM=<eight>] -> 'aṣṭau'
DESIRER[CASE=loc,SEM=<desire_base>] -> 'kāme'
TEN[CNT=10,SEM=<ten>] -> 'daśa'
NINE[CNT=9,SEM=<nine>] -> 'nava'
OR -> 'vā'
```

The causative supplies the cessation relation; the death question and
uncertain opening supply its context, not an intention to cause death.

```nltk-dep
'nirodhayati' -> 'uparamān-nārūpye' | 'jīvitam' | 'manaḥ' | 'upekṣām' | 'ca' | 'eva' | 'rūpe' | 'kāme'
'rūpe' -> 'aṣṭau'
'kāme' -> 'daśa' | 'nava' | 'aṣṭau' | 'vā'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 7) | `FORMLESS` | three named terminal Faculties, uncertain opening retained |
| [7, 9) | `FORM` | eight in the Form realm |
| [9, 14) | `DESIRE` | ten/nine/eight alternatives |
| [0, 14) | `S` | terminal count under death scope |

## 5. Translation

### Literal Translation

> Brings to cessation, at death in the formless realm, life, mind, and
> neutral feeling. In the form realm, eight. In the desire realm, ten, nine,
> or eight.

### Bhāṣya-informed study translation

> One dying in the Formless realm brings life, Mind, and neutral feeling
> to cessation; in the Form realm, eight Faculties; in the Desire-realm,
> ten, nine, or eight.

## 6. Philosophical Translation

> The terminal count is not initial maturation in reverse. The count
> depends on realm, mode of dying, sexual characteristics, and the
> ethical quality of the final consciousness.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| tyāga | loss | the heading after acquisition |
| nirodhayati | brings to cessation | at death; not abandonment |
| sakṛn-maraṇa | death all at once | the kārikā counts |
| krama-mṛtyu | gradual death | four; the next clause |
| śubha / kuśala citta | wholesome consciousness | next verse's qualification adds the five; not identical to Mind-Faculty |
| samagra-indriya | faculties complete | Form Realm arising and dying |
| vyañjana | sexual characteristic | eight, nine, or ten |

## 8. Logical Determination

**Kārikā, derived.** The named Formless members, Form count, and
Desire-realm alternatives are the verse-derived claims. The base-case
qualification, exact member-sets, gradual case, and wholesome addition
are supplied by the continuous Bhāṣya, including its cross-verse
continuation.

```nltk-sem
terminal_member : \f.\c.CeasesAt(f,c)
terminal_count : \c.\n.TerminalCount(c,n)
death_scope : DeathCessationScope
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(DeathCessationScope & CeasesAt(life_f,formless_base) & CeasesAt(mind_f,formless_base) & CeasesAt(neutral_f,formless_base) & TerminalCount(form_base,eight) & AlternativeCount(desire_base,ten) & AlternativeCount(desire_base,nine) & AlternativeCount(desire_base,eight))

# THEORY prose_base_sets
# EXPECT prose_base_sets T
all x.(CeasesAt(x,formless_base) <-> (x = life_f | x = mind_f | x = neutral_f))
all x.(CeasesAt(x,form_base) <-> (CeasesAt(x,formless_base) | SensoryFive(x)))
all x.(CeasesAt(x,gradual_base) <-> (x = body_f | x = life_f | x = mind_f | x = neutral_f))
(BaseConsciousness(afflicted) & BaseConsciousness(indeterminate))

# THEORY cross_verse_wholesome_addition
# EXPECT cross_verse_wholesome_addition T
all x.(CeasesWholesomely(x,formless_base) <-> (CeasesAt(x,formless_base) | FaithFive(x)))
all x.(CeasesWholesomely(x,form_base) <-> (CeasesAt(x,form_base) | FaithFive(x)))
(AdditionalCount(wholesome,five) & TerminalCount(formless_wholesome,eight) & TerminalCount(form_wholesome,thirteen))

# THEORY rejected_terminal_set_is_initial_maturation_set
# EXPECT rejected_terminal_set_is_initial_maturation_set F
all x.(CeasesAt(x,formless_base) <-> (x = life_f))

# THEORY rejected_gradual_equals_form_set
# EXPECT rejected_gradual_equals_form_set F
all x.(CeasesAt(x,gradual_base) <-> CeasesAt(x,form_base))

# THEORY rejected_wholesome_adds_sensory_five
# EXPECT rejected_wholesome_adds_sensory_five F
all x.(CeasesWholesomely(x,formless_base) <-> (CeasesAt(x,formless_base) | SensoryFive(x)))
```

```nltk-valuation
life_f => life
mind_f => mind
neutral_f => neutral
body_f => body
formless_base => formless_terminal
form_base => form_terminal
desire_base => desire_terminal
gradual_base => gradual_terminal
formless_wholesome => formless_wholesome_terminal
form_wholesome => form_wholesome_terminal
eight => count_eight
nine => count_nine
ten => count_ten
five => count_five
thirteen => count_thirteen
afflicted => afflicted_consciousness
indeterminate => indeterminate_consciousness
wholesome => wholesome_consciousness
DeathCessationScope => True
TerminalCount => {(form_terminal,count_eight),(formless_wholesome_terminal,count_eight),(form_wholesome_terminal,count_thirteen)}
AlternativeCount => {(desire_terminal,count_ten),(desire_terminal,count_nine),(desire_terminal,count_eight)}
CeasesAt => {(life,formless_terminal),(mind,formless_terminal),(neutral,formless_terminal),(life,form_terminal),(mind,form_terminal),(neutral,form_terminal),(eye,form_terminal),(ear,form_terminal),(nose,form_terminal),(tongue,form_terminal),(body,form_terminal),(body,gradual_terminal),(life,gradual_terminal),(mind,gradual_terminal),(neutral,gradual_terminal)}
SensoryFive => {eye,ear,nose,tongue,body}
FaithFive => {faith,vigor,mindfulness,concentration,comprehension}
BaseConsciousness => {afflicted_consciousness,indeterminate_consciousness}
AdditionalCount => {(wholesome_consciousness,count_five)}
CeasesWholesomely => {(life,formless_terminal),(mind,formless_terminal),(neutral,formless_terminal),(faith,formless_terminal),(vigor,formless_terminal),(mindfulness,formless_terminal),(concentration,formless_terminal),(comprehension,formless_terminal),(life,form_terminal),(mind,form_terminal),(neutral,form_terminal),(eye,form_terminal),(ear,form_terminal),(nose,form_terminal),(tongue,form_terminal),(body,form_terminal),(faith,form_terminal),(vigor,form_terminal),(mindfulness,form_terminal),(concentration,form_terminal),(comprehension,form_terminal)}
```

The sensory five and the five beginning with faith are different sets.
The Desire-realm base sets add neither, one, or both sexual Faculties
to the Form terminal eight. Wholesome counts are the respective base
counts plus five: 8, 13, 15/14/13, and 9 for gradual death. Only the
Formless eight and Form thirteen are expressly recited; the others
are calculated from the stated addition. These checks do not settle
the uncertain opening wording or prove the account of dying.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): One dying in the formless realm brings to cessation
life, mind, and neutral feeling. In the form realm, eight: those three and
the five beginning with the eye. In the desire realm, ten, nine, or eight,
according to sexual characteristic: ten with both sex faculties, nine with
one, eight with neither.

2.14 asked what is first acquired as maturation. Mind and neutral feeling were present and not in that count. Here they cease. The inventories are not the same list run backward.

All at once is the scope of the verse numbers. Gradual death is a different dependency. The four are not one substance, and a change in one at another time is not thereby a change in the others.

The five cease in a wholesome death and remain wholesome. Cessation of the occurrence is not path-abandonment, and not a denial of future continuation by the word nirodha alone.

Interpretation: the consequence is the terminal membership. The doctrine is inherited. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_15
    a vak:Karika ;
    rdfs:label "VAK 2.15" ;
    vak:hasTopic vak:CessationAtDeath ;
    vak:belongsTo vak:Indriyanirdesa .

vak:FormlessDeath vak:ceases vak:Life, vak:Mind, vak:NeutralFeeling .
vak:FormDeath vak:hasCount 8 .
vak:DesireDeath vak:hasCount 8, 9, 10 .

organon:VAK_2_15_Interpretation
    organon:distinguishes vak:CessationAtDeath, vak:InitialMaturation,
        vak:PathAbandonment .
```
