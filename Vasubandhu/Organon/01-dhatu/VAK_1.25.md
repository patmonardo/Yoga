# VAK_1.25 — Speech or Name

## 1. Sanskrit (Devanāgarī)

```sanskrit
धर्मस्कन्धसहस्राणि यान्यशीतिं जगौ मुनिः ।
तानि वाङ्नाम वेत्येषां रूपसंस्कारसंग्रहः ॥ १.२५ ॥
```

## 2. Sanskrit (IAST)

```text
dharmaskandhasahasrāṇi yāny aśītiṃ jagau muniḥ /
tāni vāṅnāma vety eṣāṃ rūpasaṃskārasaṃgrahaḥ // 1.25 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| dharma-skandha-sahasrāṇi | dharma-skandha-sahasrāṇi; nominative/accusative neuter plural | Dharma-collections, in thousands; antecedent |
| yāni | relative; accusative neuter plural | which; object of *jagau* |
| aśītim | numeral; accusative singular | eighty; with the thousands, eighty thousand |
| jagau | √gai, perfect, third person singular | proclaimed |
| muniḥ | nominative masculine singular | the Sage; agent |
| tāni | correlative; nominative neuter plural | those; resumes *yāni* |
| vāk | nominative feminine singular | speech; first account |
| nāma | nominative neuter singular | name; second account |
| vā | particle | or; keeps the two accounts as alternatives |
| iti | particle | closes the report of the two accounts |
| eṣām | genitive plural | of these; the collections |
| rūpa-saṃskāra-saṃgrahaḥ | rūpa-saṃskāra-saṃgrahaḥ; nominative masculine singular | inclusion in Form and Formations, respectively |

`Skandha` in this compound is the collection of teaching. It is not a sixth Base.

**Grammar tokens.** Verse-order IAST with sandhi opened (`yāny` →
*yāni*, `vāṅnāma` → *vāk nāma*, `vety` → *vā iti*) and compound
boundaries marked. No covert token is supplied.

```text
# tokens: dharma-skandha-sahasrāṇi yāni aśītim jagau muniḥ tāni vāk nāma vā iti eṣām rūpa-saṃskāra-saṃgrahaḥ
```

## 4. Grammar

A relative–correlative frame. *Yāni ... jagau muniḥ* restricts the
antecedent collections; *tāni* resumes them. The two accounts, speech and
name, are joined by *vā* and closed by *iti*. The final nominal clause
assigns inclusion respectively: the first account to Form, the second to
Formations. The genitive *eṣām* agrees in number with the collections.

```nltk-fcfg
% start S
# tokens: dharma-skandha-sahasrāṇi yāni aśītim jagau muniḥ tāni vāk nāma vā iti eṣām rūpa-saṃskāra-saṃgrahaḥ
S[SEM=<all c.((?coll(c) & ?rel(c)) -> ?pred(c))>] -> COLL[NUM=?n,GEN=?g,SEM=?coll] RELCL[NUM=?n,GEN=?g,SEM=?rel] PRED[NUM=?n,GEN=?g,SEM=?pred]
RELCL[NUM=?n,GEN=?g,SEM=<\c.(?num(c) & ?verb(?agent)(c))>] -> REL[CASE=acc,NUM=?n,GEN=?g] NUMBER[SEM=?num] VERB[NUM=?m,SEM=?verb] AGENT[CASE=nom,NUM=?m,SEM=?agent]
PRED[NUM=?n,GEN=?g,SEM=<\c.(?or(?first)(?second) & ?incl(?first)(?second)(c))>] -> CORREL[CASE=nom,NUM=?n,GEN=?g] ACCOUNT[K=speech,SEM=?first] ACCOUNT[K=name,SEM=?second] OR[SEM=?or] QUOTE GEN[CASE=gen,NUM=?n] INCL[CASE=nom,SEM=?incl]
COLL[NUM=pl,GEN=n,SEM=<\c.DharmaCollection(c)>] -> 'dharma-skandha-sahasrāṇi'
REL[CASE=acc,NUM=pl,GEN=n] -> 'yāni'
NUMBER[SEM=<\c.InTotal(c,eighty_thousand)>] -> 'aśītim'
VERB[NUM=sg,SEM=<\a c.Proclaimed(a,c)>] -> 'jagau'
AGENT[CASE=nom,NUM=sg,GEN=m,SEM=<sage>] -> 'muniḥ'
CORREL[CASE=nom,NUM=pl,GEN=n] -> 'tāni'
ACCOUNT[K=speech,SEM=<speech_nature>] -> 'vāk'
ACCOUNT[K=name,SEM=<name_nature>] -> 'nāma'
OR[SEM=<\a b.(ReportedAccount(a) & ReportedAccount(b) & Alternative(a,b))>] -> 'vā'
QUOTE -> 'iti'
GEN[CASE=gen,NUM=pl] -> 'eṣām'
INCL[CASE=nom,SEM=<\a b c.(IncludedUnder(c,a,form_base) & IncludedUnder(c,b,formations_base))>] -> 'rūpa-saṃskāra-saṃgrahaḥ'
```

```nltk-dep
'jagau' -> 'yāni' | 'aśītim' | 'muniḥ'
'dharma-skandha-sahasrāṇi' -> 'jagau'
'tāni' -> 'dharma-skandha-sahasrāṇi'
'rūpa-saṃskāra-saṃgrahaḥ' -> 'tāni' | 'eṣām' | 'iti'
'iti' -> 'vā'
'vā' -> 'vāk' | 'nāma'
```

**Close construe.** The Dharma-collections, which, eighty thousand, the
Sage proclaimed: those are speech or name, so it is said; of these the
inclusion is in Form and Formations.

`IncludedUnder(c,a,b)` is inclusion *relative to an account*: on account
*a*, collection *c* is included in Base *b*. The verse pairs the accounts
with the Bases respectively; it does not assert that any collection is in
both Bases at once. `ReportedAccount` and `Alternative` keep *vā* as a
report of two positions, not a choice. `InTotal` attaches the count to the
whole; the model does not enumerate eighty thousand items.

The relative is resumed by `tāni`. The verse does not say each collection is both. It does not choose.

## 5. Translation

### Literal Translation

> The eighty thousand Dharma-collections which the Sage proclaimed — speech,
> or name — their inclusion is in Form and Formations.

### Bhāṣya-informed study translation

> The Sage proclaimed eighty thousand Dharma-collections: they are included in
> the Form Base if Buddha-word is speech by nature, or in the Formations Base
> if it is name by nature.

## 6. Philosophical Translation

The eighty thousand are speech, or name. Their inclusion is in Form, or in Formations.

Speech by nature: the Form Base. Name by nature: the Formations Base. The verse reports both. It does not decide.

The collection is not a further Base. A name in a sūtra—Base, Essence, or Principle—does not stand apart from the places already stated.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| dharmaskandha | Dharma-collection | a teaching-collection; not a sixth Base |
| aśīti sahasrāṇi | eighty thousand | the number proclaimed |
| muni | the Sage | the one who proclaimed them |
| vāk | speech | one account of Buddha-word |
| nāma | name | the other account |
| buddhavacana | Buddha-word | speech by nature, or name by nature |
| rūpa-skandha | Form Base | inclusion on the speech account |
| saṃskāra-skandha | Formations Base | inclusion on the name account |
| saṃgraha | inclusion | in these very classifications |
| vyatireka | standing apart | denied |

## 8. Logical Determination

**Kārikā, derived.** Every proclaimed collection is reported under two
alternative accounts, and its inclusion is assigned respectively:
speech → Form Base, name → Formations Base.

```nltk-sem
# derived by the section 4 parse
all c.((DharmaCollection(c) & InTotal(c,eighty_thousand) & Proclaimed(sage,c)) -> (ReportedAccount(speech_nature) & ReportedAccount(name_nature) & Alternative(speech_nature,name_nature) & IncludedUnder(c,speech_nature,form_base) & IncludedUnder(c,name_nature,formations_base)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
all c.((DharmaCollection(c) & InTotal(c,eighty_thousand) & Proclaimed(sage,c)) -> (ReportedAccount(speech_nature) & ReportedAccount(name_nature) & Alternative(speech_nature,name_nature) & IncludedUnder(c,speech_nature,form_base) & IncludedUnder(c,name_nature,formations_base)))
# THEORY prose
# EXPECT prose T
all x.(ScripturalDesignation(x) -> (IncludedInEstablished(x) & -StandsApart(x)))
all c.(DharmaCollection(c) -> (-Base(c) & ScripturalDesignation(c)))
all c.(DharmaCollection(c) -> (-IncludedUnder(c,speech_nature,formations_base) & -IncludedUnder(c,name_nature,form_base)))
all h.(HoldsSpeech(h) -> all c.(DharmaCollection(c) -> IncludedFor(h,c,form_base)))
all h.(HoldsName(h) -> all c.(DharmaCollection(c) -> IncludedFor(h,c,formations_base)))
-(form_base = formations_base) & Base(form_base) & Base(formations_base)
all a.-Selected(a)
# THEORY rejected_collection_is_further_base
# EXPECT rejected_collection_is_further_base F
exists c.(DharmaCollection(c) & Base(c))
# THEORY rejected_scriptural_name_stands_apart
# EXPECT rejected_scriptural_name_stands_apart F
exists x.(ScripturalDesignation(x) & StandsApart(x))
# THEORY rejected_cross_assignment
# EXPECT rejected_cross_assignment F
all c.(DharmaCollection(c) -> IncludedUnder(c,speech_nature,formations_base))
# THEORY rejected_one_account_selected
# EXPECT rejected_one_account_selected F
exists a.(ReportedAccount(a) & Selected(a))
# THEORY rejected_each_holder_includes_in_both
# EXPECT rejected_each_holder_includes_in_both F
exists h c.(IncludedFor(h,c,form_base) & IncludedFor(h,c,formations_base))
```

```nltk-valuation
sage => muni
eighty_thousand => eighty_thousand_total
speech_nature => speech_account
name_nature => name_account
form_base => rupa_skandha
formations_base => samskara_skandha
DharmaCollection => {collection_a,collection_b}
InTotal => {(collection_a,eighty_thousand_total),(collection_b,eighty_thousand_total)}
Proclaimed => {(muni,collection_a),(muni,collection_b)}
ReportedAccount => {speech_account,name_account}
Alternative => {(speech_account,name_account)}
IncludedUnder => {(collection_a,speech_account,rupa_skandha),(collection_a,name_account,samskara_skandha),(collection_b,speech_account,rupa_skandha),(collection_b,name_account,samskara_skandha)}
ScripturalDesignation => {collection_a,collection_b,other_sutra_designation}
IncludedInEstablished => {collection_a,collection_b,other_sutra_designation}
StandsApart => {}
Base => {rupa_skandha,samskara_skandha}
HoldsSpeech => {speech_holder}
HoldsName => {name_holder}
IncludedFor => {(speech_holder,collection_a,rupa_skandha),(speech_holder,collection_b,rupa_skandha),(name_holder,collection_a,samskara_skandha),(name_holder,collection_b,samskara_skandha)}
Selected => {}
```

**Model checks.** Two representative collections stand for the proclaimed
whole; the count is an attribute of the whole, not an enumeration. Removing
either account's inclusion, either reported account, or the alternative
falsifies the derived formula. Swapping the respective assignment fails
the prose theory. Each holder includes the collections in exactly one
Base; no holder includes them in both.

**Bhāṣya determination.** The wider question comes first: other things
named Base, Essence, or Principle in the sūtras are included in these very
classifications and do not stand apart. The eighty thousand are the first
example. `Yeṣām ... teṣām` reports holders of the two positions; no group
is named, and neither position is selected.

**Organon interpretation.** This is the closure rule of the classification
engine: a new scriptural designation does not add a Base, Essence, or
Principle; it resolves into the established ones. Here resolution is
parameterized by an account of what the designated thing is (speech or
name), so inclusion is a function from account to Base, not a fixed
location. The measure of a collection (1.26) is not opened. The earlier
schematic follows.

```text
other scriptural names
    Bases, Essences, Principles
    included
    not apart

eighty thousand
    proclaimed by the Sage

speech by nature
    Form Base

name by nature
    Formations Base

vā
    both reported
    neither chosen

not a sixth Base
measure of the collection is the next verse
```

## 9. Interpretive Note

**Translation note.** The two assignments report positions about Buddha-word:
those taking it as speech by nature place the collections in the Form Base;
those taking it as name by nature place them in the Formations Base. Neither
view is selected, and the collections are not an additional Base.

The hinge is `vā`. The classification receives its own teaching. Speech enters Form. Name enters Formations. The disagreement is left standing.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_25 a vak:Karika ;
    vak:hasTopic vak:SpeechOrName ;
    vak:belongsTo vak:Dhatunirdesa .

vak:DharmaCollection vak:notA vak:Base ;
    vak:ifSpeech vak:FormBase ;
    vak:ifName vak:FormationsBase .
vak:ScripturalName vak:standsApart false ;
    vak:resolvesInto vak:EstablishedClassification .
```
