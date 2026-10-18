# VAK_1.29 — Visible, Resistant, Indeterminate

## 1. Sanskrit (Devanāgarī)

```sanskrit
सनिदर्शन एकोऽत्र रूपं सप्रतिघा दश ।
रूपिणोऽव्याकृता अष्टौ त एवारूपशब्दकाः ॥ १.२९ ॥
```

## 2. Sanskrit (IAST)

```text
sanidarśana eko 'tra rūpaṃ sapratighā daśa /
rūpiṇo 'vyākṛtā aṣṭau ta evārūpaśabdakāḥ // 1.29 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sa-nidarśanaḥ | sa-nidarśana, bahuvrīhi; nominative masculine singular | visible; can be pointed out; agrees with understood *dhātuḥ* |
| ekaḥ | nominative masculine singular | one |
| atra | indeclinable | here, among the eighteen Principles |
| rūpam | nominative neuter singular | Visible Form; names the one |
| sa-pratighāḥ | sa-pratigha, bahuvrīhi; nominative masculine plural | resistant |
| daśa | numeral | ten |
| rūpiṇaḥ | rūpin; nominative masculine plural | Form-bearing; the ten in the Form Base |
| avyākṛtāḥ | a-vyākṛta; nominative masculine plural | indeterminate |
| aṣṭau | numeral | eight |
| te | nominative masculine plural | those; the same ten |
| eva | particle | the very same |
| a-rūpa-śabdakāḥ | bahuvrīhi; nominative masculine plural | without Visible Form and Sound; excluding those two |

The final compound does not say the eight are without Form. It excludes two of the ten: the Visible Form Principle and the Sound Principle.

**Grammar tokens.** Verse-order IAST with sandhi opened (`sanidarśana
eko 'tra` → *sanidarśanaḥ ekaḥ atra*, `rūpiṇo 'vyākṛtā` → *rūpiṇaḥ
avyākṛtāḥ*, `ta evārūpa-` → *te eva a-rūpa-*) and compound boundaries
marked. The understood *dhātavaḥ* is carried by masculine agreement, not
supplied as a leaf.

```text
# tokens: sa-nidarśanaḥ ekaḥ atra rūpam sa-pratighāḥ daśa rūpiṇaḥ avyākṛtāḥ aṣṭau te eva a-rūpa-śabdakāḥ
```

## 4. Grammar

Three answers to three questions, each scoped to the eighteen by *atra*.
The adjectives are masculine, agreeing with the understood *dhātu*; the
neuter *rūpam* names the one visible. *Rūpiṇaḥ* identifies the ten
resistant. *Te eva* resumes those ten; the bahuvrīhi removes two.

```nltk-fcfg
% start S
# tokens: sa-nidarśanaḥ ekaḥ atra rūpam sa-pratighāḥ daśa rūpiṇaḥ avyākṛtāḥ aṣṭau te eva a-rūpa-śabdakāḥ
S[SEM=<(?visible & ?resistant & ?indeterminate)>] -> VISIBLE[SEM=?visible] RESISTANT[SEM=?resistant] INDETERMINATE[SEM=?indeterminate]
VISIBLE[SEM=<all x.(?here(x) -> (?vis(x) <-> (x = ?name)))>] -> VIS[CASE=nom,NUM=?n,GEN=?g,SEM=?vis] ONE[CASE=nom,NUM=?n,GEN=?g] HERE[SEM=?here] NAME[CASE=nom,NUM=sg,GEN=n,SEM=?name]
RESISTANT[SEM=<all x.(AmongEighteen(x) -> (?res(x) <-> ?formb(x)))>] -> RES[CASE=nom,NUM=pl,GEN=?g,SEM=?res] TEN FORMB[CASE=nom,NUM=pl,GEN=?g,SEM=?formb]
INDETERMINATE[SEM=<all x.(AmongEighteen(x) -> (?ind(x) <-> (?same(x) & ?excl(x))))>] -> IND[CASE=nom,NUM=pl,GEN=?g,SEM=?ind] EIGHT SAME[CASE=nom,NUM=pl,GEN=?g,SEM=?same] EVA EXCL[CASE=nom,NUM=pl,GEN=?g,SEM=?excl]
VIS[CASE=nom,NUM=sg,GEN=m,SEM=<\x.Visible(x)>] -> 'sa-nidarśanaḥ'
ONE[CASE=nom,NUM=sg,GEN=m] -> 'ekaḥ'
HERE[SEM=<\x.AmongEighteen(x)>] -> 'atra'
NAME[CASE=nom,NUM=sg,GEN=n,SEM=<visible_form>] -> 'rūpam'
RES[CASE=nom,NUM=pl,GEN=m,SEM=<\x.Resistant(x)>] -> 'sa-pratighāḥ'
TEN -> 'daśa'
FORMB[CASE=nom,NUM=pl,GEN=m,SEM=<\x.FormBearing(x)>] -> 'rūpiṇaḥ'
IND[CASE=nom,NUM=pl,GEN=m,SEM=<\x.OnlyIndeterminate(x)>] -> 'avyākṛtāḥ'
EIGHT -> 'aṣṭau'
SAME[CASE=nom,NUM=pl,GEN=m,SEM=<\x.Resistant(x)>] -> 'te'
EVA -> 'eva'
EXCL[CASE=nom,NUM=pl,GEN=m,SEM=<\x.(-(x = visible_form) & -(x = sound))>] -> 'a-rūpa-śabdakāḥ'
```

```nltk-dep
'sa-nidarśanaḥ' -> 'ekaḥ' | 'atra' | 'rūpam'
'sa-pratighāḥ' -> 'daśa' | 'rūpiṇaḥ'
'avyākṛtāḥ' -> 'aṣṭau' | 'te'
'te' -> 'eva' | 'a-rūpa-śabdakāḥ'
```

**Close construe.** Here one is visible: Visible Form. Ten are resistant:
the Form-bearing. Eight are indeterminate: those same, without Visible
Form and Sound.

Each clause is a biconditional over the eighteen, so the counts are
extensional: one, ten, and eight are checked against the finite valuation,
not asserted by FOL arithmetic. `OnlyIndeterminate` answers the question
"how many are indeterminate" as the Bhāṣya does: these eight are not
declared wholesome or unwholesome. The ethical status of the remaining ten
is not determined here. `Resistant` in the count is resistance by
obstruction; the other two resistances are prose.

Three questions, three counts. The masculine adjectives agree with the understood Principle. Neuter *rūpam* names the one.

## 5. Translation

### Literal Translation

> One here is visible: Form. Ten are resistant. Eight Form-bearing ones are
> indeterminate: those same, excluding Form and Sound.

### Bhāṣya-informed study translation

> Among the eighteen Principles, one is visible: the Visible Form Principle.
> Ten included in the Form Base are resistant. Eight of those ten are
> indeterminate: those same ten excluding Visible Form and Sound.

## 6. Philosophical Translation

Visibility, resistance, and ethical status are three determinations. They do not collapse.

The one visible is the Visible Form Principle, not the Form Base. The ten resistant are the Form Base as Principles: five Faculties and five meanings. The eight indeterminate are those ten minus Visible Form and Sound.

The Cognition Principles are not in this count. The Mind Principle is not in this count.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| dhātu | Principle | the eighteen |
| sanidarśana | visible | can be pointed out |
| anidarśana | not visible | the other seventeen |
| rūpa-dhātu | Visible Form Principle | the one visible |
| sapratigha | resistant | the ten, by obstruction |
| pratigha | resistance | three kinds; the count uses one |
| āvaraṇa-pratighāta | obstruction | blocking another's arising in one's place |
| viṣaya-pratighāta | Condition-resistance | the Faculty in its Condition |
| ālambana-pratighāta | support-resistance | consciousness and the concomitants |
| rūpin | Form-bearing | the ten in the Form Base |
| avyākṛta | indeterminate | not declared wholesome or unwholesome |
| śabda-dhātu | Sound Principle | excluded from the eight |
| vijñāna | Cognition | not this count |
| citta | consciousness | the seven, in the comparison only |

## 8. Logical Determination

**Kārikā, derived.** Three biconditionals over the eighteen: visible iff
Visible Form; resistant iff Form-bearing; only-indeterminate iff one of
those ten other than Visible Form and Sound.

```nltk-sem
# derived by the section 4 parse
(all x.(AmongEighteen(x) -> (Visible(x) <-> (x = visible_form))) & all x.(AmongEighteen(x) -> (Resistant(x) <-> FormBearing(x))) & all x.(AmongEighteen(x) -> (OnlyIndeterminate(x) <-> (Resistant(x) & -(x = visible_form) & -(x = sound)))))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.(AmongEighteen(x) -> (Visible(x) <-> (x = visible_form))) & all x.(AmongEighteen(x) -> (Resistant(x) <-> FormBearing(x))) & all x.(AmongEighteen(x) -> (OnlyIndeterminate(x) <-> (Resistant(x) & -(x = visible_form) & -(x = sound)))))
# THEORY prose
# EXPECT prose T
-AmongEighteen(form_base) & -Visible(form_base)
all x.(AmongEighteen(x) -> (Resistant(x) <-> ObstructionResistant(x)))
all x.(Item(x) -> ((ConditionResistant(x) & -ObstructionResistant(x)) <-> (CittaPrinciple(x) | x = dharma_associated)))
all x.(Item(x) -> ((ObstructionResistant(x) & -ConditionResistant(x)) <-> ConditionMeaning(x)))
all x.(Item(x) -> ((ConditionResistant(x) & ObstructionResistant(x)) <-> SenseFaculty(x)))
all x.(Item(x) -> ((-ConditionResistant(x) & -ObstructionResistant(x)) <-> (x = dharma_nonassociated)))
all x.(SupportResistant(x) -> ConditionResistant(x))
all x.((ConditionResistant(x) & -SupportResistant(x)) <-> SenseFaculty(x))
PortionOf(dharma_associated,dharma_principle) & PortionOf(dharma_nonassociated,dharma_principle)
AttributedTo(kumaralata_definition,kumaralata) & AttributedToOthers(maturation_account) & OverextendsTo(maturation_account,pure_dharmas)
# THEORY rejected_form_base_is_visible
# EXPECT rejected_form_base_is_visible F
exists x.(x = form_base & Visible(x))
# THEORY rejected_count_by_condition_resistance
# EXPECT rejected_count_by_condition_resistance F
all x.(AmongEighteen(x) -> (Resistant(x) <-> ConditionResistant(x)))
# THEORY rejected_eight_are_formless
# EXPECT rejected_eight_are_formless F
all x.(OnlyIndeterminate(x) -> -FormBearing(x))
# THEORY rejected_sound_only_indeterminate
# EXPECT rejected_sound_only_indeterminate F
exists x.(x = sound & OnlyIndeterminate(x))
# THEORY rejected_mind_is_resistant
# EXPECT rejected_mind_is_resistant F
exists x.(x = mind_principle & Resistant(x))
# THEORY rejected_support_without_condition
# EXPECT rejected_support_without_condition F
exists x.(SupportResistant(x) & -ConditionResistant(x))
```

```nltk-valuation
visible_form => rupa_d
sound => sabda_d
mind_principle => mano_d
dharma_principle => dharma_d
form_base => rupa_skandha
dharma_associated => dharma_samprayukta
dharma_nonassociated => dharma_asamprayukta
kumaralata => bhadanta_kumaralata
kumaralata_definition => kumaralata_def
maturation_account => vipaka_account
pure_dharmas => anasrava_dharmas
AmongEighteen => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d,mano_d,dharma_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d}
Visible => {rupa_d}
FormBearing => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d}
Resistant => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d}
OnlyIndeterminate => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,gandha_d,rasa_d,sprastavya_d}
Item => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d,mano_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d,dharma_samprayukta,dharma_asamprayukta}
ObstructionResistant => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d}
ConditionResistant => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,mano_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d,dharma_samprayukta}
SupportResistant => {mano_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d,dharma_samprayukta}
CittaPrinciple => {mano_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d}
ConditionMeaning => {rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d}
SenseFaculty => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d}
PortionOf => {(dharma_samprayukta,dharma_d),(dharma_asamprayukta,dharma_d)}
AttributedTo => {(kumaralata_def,bhadanta_kumaralata)}
AttributedToOthers => {vipaka_account}
OverextendsTo => {(vipaka_account,anasrava_dharmas)}
```

**Model checks.** Eighteen distinct Principles; exactly one visible, ten
resistant, eight only-indeterminate. Adding the Form Base or Sound to the
wrong extension, or making Mind resistant, falsifies the derived formula.
The four alternatives partition nineteen items (the eighteen with the
Dharma Principle split into its associated and non-associated portions):
seven consciousness Principles plus the associated portion by Condition
alone; five Conditions by obstruction alone; five Faculties by both; the
non-associated portion by neither. Support-resistance implies
Condition-resistance; the five Faculties are Condition-resistant without
support-resistance.

**Bhāṣya determination.** Visible means able to be pointed out: this,
here, there. Condition (*viṣaya*) is where something has its function;
support (*ālambana*) is what consciousness and the concomitants grasp.
The Prajñapti's eye-examples (water and land, night and day) are reported
illustrations of Condition-resistance, not counted. Kumāralāta's
definition is named. The maturation account of "indeterminate" is the
others'; it would make the Pure indeterminate too.

**Organon interpretation.** The engine now runs on the eighteen. Three
determinations, three different cuts: visibility (one), resistance (ten),
ethical indeterminacy (eight). Resistance itself is not one relation: the
tetralemma shows that obstruction and Condition-resistance cross-classify,
and support-resistance nests inside Condition-resistance. The count picks
one of the three. 1.30 is not opened. The earlier schematic follows.

```text
eighteen Principles

visible
    one
    Visible Form Principle
    the rest not visible

resistant
    ten
    the Form Base as Principles
    obstruction, not the other two

indeterminate
    eight
    those ten
    excluding Visible Form and Sound
    five Faculties, Odor, Taste, Tangible

not this verse
    the Cognition Principle, the seven
    the Dharma Principle
    1.30 not opened
```

## 9. Interpretive Note

**Translation note.** The Bhāṣya counts the ten Faculties and meanings
included in the Form Base as resistant by obstruction. Its eight indeterminate
Principles are those ten without Visible Form and Sound; indeterminate is
glossed as neither wholesome nor unwholesome. The commentary distinguishes
this obstruction-based resistance from condition-resistance and
support-resistance.

The hinge is the three counts. Interpretation of the three resistances is in the Bhāṣya. The eight are not a denial of Form.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_29 a vak:Karika ;
    vak:hasTopic vak:VisibleResistantIndeterminate ;
    vak:belongsTo vak:Dhatunirdesa .

vak:VisibleFormPrinciple vak:visible true ;
    vak:among vak:TenFormPrinciples .
vak:TenFormPrinciples vak:resistantBy vak:Obstruction ;
    vak:includedIn vak:FormBase .
vak:EightIndeterminate vak:derivedFrom vak:TenFormPrinciples ;
    vak:excludes vak:VisibleFormPrinciple, vak:SoundPrinciple .
```
