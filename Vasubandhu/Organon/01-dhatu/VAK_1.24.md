# VAK_1.24 — Form and Dharma

## 1. Sanskrit (Devanāgarī)

```sanskrit
विशेषणार्थं प्राधान्याद्बहुधर्माग्रसंग्रहात् ।
एकमायतनं रूपमेकं धर्माख्यमुच्यते ॥ १.२४ ॥
```

## 2. Sanskrit (IAST)

```text
viśeṣaṇārthaṃ prādhānyād bahudharmāgrasaṃgrahāt /
ekam āyatanaṃ rūpam ekaṃ dharmākhyam ucyate // 1.24 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| viśeṣaṇa-artham | viśeṣaṇa + artham; accusative neuter singular, adverbial | for the sake of distinction; applies to both names |
| prādhānyāt | ablative singular | because of primacy; grounds the name Form |
| bahu-dharma-agra-saṃgrahāt | bahu-dharma-agra-saṃgrahāt; ablative singular | because many dharmas, and the highest, are gathered; grounds the name Dharma |
| ekam | nominative neuter singular | one; first occurrence |
| āyatanam | nominative neuter singular | Essence; understood again with the second *ekam* |
| rūpam | nominative neuter singular, predicate | called Form |
| ekam | nominative neuter singular | one; second occurrence |
| dharma-ākhyam | dharma + ākhyā, bahuvrīhi; nominative neuter singular | having the designation Dharma |
| ucyate | third person singular present passive | is called; one verb, both names |

The sandhi `prādhānyād` voices `t` before `b`. The compound gathers two things, not one: many dharmas, and the highest dharma. The verse does not call the many highest.

**Grammar tokens.** Verse-order IAST with sandhi opened and compound
boundaries marked. *Āyatanam* is not repeated as a token; the second
*ekam* inherits it through agreement, and the parse supplies the
restrictor in the rule rather than as a covert leaf.

```text
# tokens: viśeṣaṇa-artham prādhānyāt bahu-dharma-agra-saṃgrahāt ekam āyatanam rūpam ekam dharma-ākhyam ucyate
```

## 4. Grammar

Three grounds come first: one adverbial accusative of purpose and two
ablatives of reason. Two nominative neuter singular clauses follow, each
headed by *ekam*. The single passive *ucyate* closes both. Distinction is
distributed to both names; primacy goes with Form; the gathering goes with
Dharma.

```nltk-fcfg
% start S
# tokens: viśeṣaṇa-artham prādhānyāt bahu-dharma-agra-saṃgrahāt ekam āyatanam rūpam ekam dharma-ākhyam ucyate
S[SEM=<(?one1(?essence)(?called(?formname))(\x.(?purpose(x) & ?primacy(x))) & ?one2(?essence)(?called(?dharmaname))(\x.(?purpose(x) & ?gathering(x))))>] -> PURPOSE[CASE=acc,SEM=?purpose] PRIMACY[CASE=abl,SEM=?primacy] GATHERING[CASE=abl,SEM=?gathering] ONE[CASE=nom,NUM=?n,GEN=?g,SEM=?one1] ESSENCE[CASE=nom,NUM=?n,GEN=?g,SEM=?essence] FORMNAME[CASE=nom,NUM=?n,GEN=?g,SEM=?formname] ONE[CASE=nom,NUM=?n,GEN=?g,SEM=?one2] DHARMANAME[CASE=nom,NUM=?n,GEN=?g,SEM=?dharmaname] CALLED[NUM=?n,SEM=?called]
PURPOSE[CASE=acc,SEM=<\x.NamedForDistinction(x)>] -> 'viśeṣaṇa-artham'
PRIMACY[CASE=abl,SEM=<\x.NamedForPrimacy(x)>] -> 'prādhānyāt'
GATHERING[CASE=abl,SEM=<\x.(GathersMany(x) & GathersHighest(x))>] -> 'bahu-dharma-agra-saṃgrahāt'
ONE[CASE=nom,NUM=sg,GEN=n,SEM=<\P Q R.exists x.(P(x) & Q(x) & R(x) & all y.((P(y) & Q(y)) -> (y = x)))>] -> 'ekam'
ESSENCE[CASE=nom,NUM=sg,GEN=n,SEM=<\x.Essence(x)>] -> 'āyatanam'
FORMNAME[CASE=nom,NUM=sg,GEN=n,SEM=<form_name>] -> 'rūpam'
DHARMANAME[CASE=nom,NUM=sg,GEN=n,SEM=<dharma_name>] -> 'dharma-ākhyam'
CALLED[NUM=sg,SEM=<\n x.CalledBy(x,n)>] -> 'ucyate'
```

```nltk-dep
'ucyate' -> 'āyatanam' | 'rūpam' | 'dharma-ākhyam' | 'viśeṣaṇa-artham' | 'prādhānyāt' | 'bahu-dharma-agra-saṃgrahāt'
'āyatanam' -> 'ekam'
'dharma-ākhyam' -> 'ekam'
```

**Close construe.** For the sake of distinction, one Essence is called
Form, because of primacy; and one, having the designation Dharma, is
called so, because many dharmas and the highest are gathered.

*Ekam* is projected as "exactly one Essence bears this name," not as a
count of Essences. Uniqueness is scoped to the name, not to the grounds:
other Essences may share resistance or be dharma by own-nature without
being called Form or Dharma. `CalledBy` is designation, not a speech
event. The ablatives ground the names; they do not define the Essences.

## 5. Translation

### Literal Translation

> For the sake of distinction, because of primacy, and because many dharmas
> and the highest are gathered, one Essence is called Form, and one is
> called Dharma.

### Bhāṣya-informed study translation

> For distinction, one Essence is called Form because of primacy, and one is
> called Dharma because it gathers many dharmas and the highest.

## 6. Philosophical Translation

For distinction, one Essence is called Form, and one is called Dharma.

The Form Base holds ten Essences. Nine already have names: eye, ear, nose, tongue, body, sound, odor, taste, tangible. The one that remains is called Form. Primacy is the other reason. It resists contact. It can be shown. The world already calls it Form.

The other Essence is called Dharma because of what it gathers. Feeling, Reflection, and Formations are gathered there. Nirvāṇa is gathered there, and not in the others. The many are not the highest. The highest is not the many.

Form and Dharma are the two names. The ten are not one Essence called Form. All dharmas are not one Essence called Dharma.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| āyatana | Essence | one called Form; one called Dharma |
| rūpa | Form | the name, and the Form Base that holds the ten |
| dharma | Dharma | the name of the gathering; not a second word for Essence |
| viśeṣaṇārtham | for distinction | both names |
| prādhānya | primacy | the name Form |
| bahu-dharma-saṃgraha | gathering of many dharmas | beginning with Feeling |
| agra | the highest | nirvāṇa; not a name for the many |
| rūpa-skandha | Form Base | includes the ten; is not the one Essence called Form |
| viṣaya-viṣayin | Condition and what has the Condition | how the ten are arranged |
| sapratigha | resistant | shared by the ten; joined with showability for primacy |
| sanidarśana | able to be shown | primacy; only the Form Essence |
| vedanā | Feeling | first of the many gathered |
| saṃjñā | Reflection | gathered under the Dharma name; not manas |
| saṃskāra | Formation | gathered under the Dharma name |
| nirvāṇa | nirvāṇa | the highest dharma |

## 8. Logical Determination

**Kārikā, derived.** Two exactly-one naming claims under one verb.
Distinction belongs to both; primacy and gathering are not exchanged.

```nltk-sem
# derived by the section 4 parse
(exists x.(Essence(x) & CalledBy(x,form_name) & NamedForDistinction(x) & NamedForPrimacy(x) & all y.((Essence(y) & CalledBy(y,form_name)) -> (y = x))) & exists x.(Essence(x) & CalledBy(x,dharma_name) & NamedForDistinction(x) & GathersMany(x) & GathersHighest(x) & all y.((Essence(y) & CalledBy(y,dharma_name)) -> (y = x))))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(exists x.(Essence(x) & CalledBy(x,form_name) & NamedForDistinction(x) & NamedForPrimacy(x) & all y.((Essence(y) & CalledBy(y,form_name)) -> (y = x))) & exists x.(Essence(x) & CalledBy(x,dharma_name) & NamedForDistinction(x) & GathersMany(x) & GathersHighest(x) & all y.((Essence(y) & CalledBy(y,dharma_name)) -> (y = x))))
# THEORY prose
# EXPECT prose T
all x.(InFormBase(x) -> (Essence(x) & Resistant(x)))
all x.((InFormBase(x) & -(x = form_essence)) -> HasSpecificName(x))
exists x.(x = form_essence & InFormBase(x) & -HasSpecificName(x))
all x.(Showable(x) -> (x = form_essence))
Showable(form_essence) & WorldlyForm(form_essence) & Resistant(form_essence)
CorrespondsTo(eye,form_essence) & CorrespondsTo(ear,sound) & CorrespondsTo(nose,odor) & CorrespondsTo(tongue,taste) & CorrespondsTo(body,tangible)
Base(form_base) & -Essence(form_base) & -(form_base = form_essence)
all x.(Essence(x) -> DharmaByNature(x))
Gathers(dharma_essence,feeling) & Gathers(dharma_essence,reflection) & Gathers(dharma_essence,formations) & Gathers(dharma_essence,nirvana)
Base(feeling) & Base(reflection) & Base(formations) & -Base(nirvana)
Highest(nirvana) & -Highest(feeling) & -Highest(reflection) & -Highest(formations)
all x.((Essence(x) & Gathers(x,nirvana)) -> (x = dharma_essence))
AttributedToOthers(three_eye_account) & -GivenInVerse(three_eye_account)
# THEORY rejected_form_base_is_form_essence
# EXPECT rejected_form_base_is_form_essence F
exists x.(x = form_base & x = form_essence)
# THEORY rejected_every_essence_called_dharma
# EXPECT rejected_every_essence_called_dharma F
all x.(Essence(x) -> CalledBy(x,dharma_name))
# THEORY rejected_primacy_names_dharma
# EXPECT rejected_primacy_names_dharma F
exists x.(x = dharma_essence & NamedForPrimacy(x))
# THEORY rejected_many_are_highest
# EXPECT rejected_many_are_highest F
all x.(Gathers(dharma_essence,x) -> Highest(x))
# THEORY rejected_only_faculties_already_named
# EXPECT rejected_only_faculties_already_named F
all x.((InFormBase(x) & HasSpecificName(x)) -> SenseFaculty(x))
# THEORY rejected_resistance_alone_distinguishes
# EXPECT rejected_resistance_alone_distinguishes F
all x.(Resistant(x) -> (x = form_essence))
```

```nltk-valuation
form_name => form_designation
dharma_name => dharma_designation
form_essence => form_ess
dharma_essence => dharma_ess
form_base => form_skandha
eye => eye_ess
ear => ear_ess
nose => nose_ess
tongue => tongue_ess
body => body_ess
sound => sound_ess
odor => odor_ess
taste => taste_ess
tangible => tangible_ess
feeling => feeling_base
reflection => reflection_base
formations => formations_base
nirvana => nirvana_dharma
three_eye_account => others_three_eyes
Essence => {eye_ess,ear_ess,nose_ess,tongue_ess,body_ess,form_ess,sound_ess,odor_ess,taste_ess,tangible_ess,mind_ess,dharma_ess}
CalledBy => {(form_ess,form_designation),(dharma_ess,dharma_designation)}
NamedForDistinction => {form_ess,dharma_ess}
NamedForPrimacy => {form_ess}
GathersMany => {dharma_ess}
GathersHighest => {dharma_ess}
InFormBase => {eye_ess,ear_ess,nose_ess,tongue_ess,body_ess,form_ess,sound_ess,odor_ess,taste_ess,tangible_ess}
HasSpecificName => {eye_ess,ear_ess,nose_ess,tongue_ess,body_ess,sound_ess,odor_ess,taste_ess,tangible_ess}
SenseFaculty => {eye_ess,ear_ess,nose_ess,tongue_ess,body_ess}
Resistant => {eye_ess,ear_ess,nose_ess,tongue_ess,body_ess,form_ess,sound_ess,odor_ess,taste_ess,tangible_ess}
Showable => {form_ess}
WorldlyForm => {form_ess}
CorrespondsTo => {(eye_ess,form_ess),(ear_ess,sound_ess),(nose_ess,odor_ess),(tongue_ess,taste_ess),(body_ess,tangible_ess)}
Base => {form_skandha,feeling_base,reflection_base,formations_base}
DharmaByNature => {eye_ess,ear_ess,nose_ess,tongue_ess,body_ess,form_ess,sound_ess,odor_ess,taste_ess,tangible_ess,mind_ess,dharma_ess}
Gathers => {(dharma_ess,feeling_base),(dharma_ess,reflection_base),(dharma_ess,formations_base),(dharma_ess,nirvana_dharma)}
Highest => {nirvana_dharma}
AttributedToOthers => {others_three_eyes}
GivenInVerse => {}
```

**Model checks.** Ten distinct Essences belong to the Form Base; nine
have specific names, and the remaining one is the Form Essence. The five
sense Faculties correspond one-to-one with five Conditions. A second
Essence called Form, or a second called Dharma, falsifies the derived
formula; so does removing primacy from Form or the highest from the
Dharma gathering. Resistance is shared by the ten; showability alone
singles out the Form Essence. Every Essence is dharma by own-nature, but
only one is called Dharma.

**Bhāṣya determination.** Distinction works by remainder: the nine
specific names leave one Essence to bear the general name Form, and the
Dharma Essence likewise bears the general name of what it gathers. The
gathered Feeling, Reflection, and Formations remain Bases; nirvāṇa is
gathered there and is not a Base. "Beginning with Feeling" is not closed
by this model. The three-eye account stays attributed to others.

**Organon interpretation.** This opens the Dhātu classification machine
at its naming layer: two Essences receive the names of a whole Base and
of all dharmas, by different grounds. Form is named from the side of the
Faculty and its Condition (resistance, showing, worldly usage); Dharma is
named from the side of gathering. The verse does not yet locate further
designations (1.25) or assign by characteristic (1.27). The earlier
schematic follows.

```text
rūpa : dharma
    two Essences
    one verb
    distinction belongs to both

Form Base
    ten Essences
    nine already named
    one called Form
        primacy
        resists
        can be shown
        the world already says Form
    the Base is not that one Essence

Dharma Essence
    not every dharma
    gathers the many, beginning with Feeling
        Feeling, Reflection, Formations
    gathers the highest
        nirvāṇa
        not in the others
    the many are not the highest

others
    twentyfold
    three eyes
    not the verse

1.25 not opened
```

## 9. Interpretive Note

**Translation note.** The Bhāṣya distinguishes the naming grounds: Form is
prominent through resistance, visibility, and ordinary usage; Dharma is a
general name because the Essence gathers many dharmas, including feeling,
reflection, and formations, and also the highest dharma, nirvāṇa. An
alternative account based on twentyfold variety and three eyes remains
attributed to 'others.'

The hinge is the repeated *ekam*. Form and Dharma are a dyad of names, not two words for the Essence arrangement. The three that stand between the Form Base and the Cognition Base are what the Dharma Essence gathers. They remain Bases. There is no sixth Base called Dharma.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_24 a vak:Karika ;
    vak:hasTopic vak:RupaDharma ;
    vak:belongsTo vak:Dhatunirdesa .

vak:FormEssence vak:namedBy vak:Distinction, vak:Primacy ;
    vak:memberOf vak:FormBase ;
    vak:notIdenticalTo vak:FormBase .

vak:DharmaEssence vak:namedBy vak:Distinction, vak:Gathering ;
    vak:gathers vak:Feeling, vak:Reflection, vak:Formations, vak:Nirvana .

vak:Rupa vak:dyad vak:Dharma .
```
