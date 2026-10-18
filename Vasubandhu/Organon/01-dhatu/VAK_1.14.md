# VAK_1.14 — The Same Ten, Feeling, and Reflection

## 1. Sanskrit (Devanāgarī)

```sanskrit
इन्द्रियार्थास्त एवेष्टा दशायतनधातवः ।
वेदनानुभवः संज्ञा निमित्तोद्ग्रहणात्मिका ॥ १.१४ ॥
```

## 2. Sanskrit (IAST)

```text
indriyārthās ta eveṣṭā daśāyatanadhātavaḥ /
vedanānubhavaḥ saṃjñā nimittodgrahaṇātmikā // 1.14 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| indriya-arthāḥ | nominative masculine plural copulative compound | Faculties and meanings; the ten already stated |
| te | nominative masculine plural pronoun | these same ones |
| eva | restrictive particle | these very ones, not another inventory |
| iṣṭāḥ | nominative masculine plural participle | accepted |
| daśa-āyatana-dhātavaḥ | nominative masculine plural compound | ten Essences and ten Principles |
| vedanā | nominative feminine singular | Feeling |
| anubhavaḥ | nominative masculine singular predicate noun | undergoing |
| saṃjñā | nominative feminine singular | Reflection |
| nimitta-udgrahaṇa-ātmikā | nominative feminine singular adjective | having taking up a mark as its nature |

*Indriya* is Faculty throughout this study. Here the five Faculties are counted
with their meanings. *Ārtha* is meaning; *āyatana* is Essence; *dhātu* is
Principle; *saṃjñā* is Reflection. The reflective mark is the commentary’s
example, not the headword.

**Grammar tokens.** Verse-order IAST with sandhi opened and compound
boundaries marked. The tenfold Essence–Principle compound stays one leaf;
the Bhāṣya resolves its distributed count. No covert copula is inserted.

```text
# tokens: indriya-arthāḥ te eva iṣṭāḥ daśa-āyatana-dhātavaḥ vedanā anubhavaḥ saṃjñā nimitta-udgrahaṇa-ātmikā
```

## 4. Grammar

*Te eva* resumes the already stated Faculties and meanings. Plural
agreement carries that same field through *iṣṭāḥ* and the classification
compound. The two nominal definitions then have different agreement
patterns: Feeling and its predicate noun differ in gender, whereas the
adjective describing Reflection agrees with it.

```nltk-fcfg
% start S
# tokens: indriya-arthāḥ te eva iṣṭāḥ daśa-āyatana-dhātavaḥ vedanā anubhavaḥ saṃjñā nimitta-udgrahaṇa-ātmikā
S[SEM=<(?classification & ?feeling & ?reflection)>] -> CLASSIFICATION[SEM=?classification] FEELINGDEF[SEM=?feeling] REFLECTIONDEF[SEM=?reflection]
CLASSIFICATION[SEM=<?accepted(?members)(?slots)>] -> MEMBERS[CASE=nom,NUM=?n,GEN=?g,SEM=?members] SAME[CASE=nom,NUM=?n,GEN=?g] ONLY ACCEPTED[CASE=nom,NUM=?n,GEN=?g,SEM=?accepted] SLOTS[CASE=nom,NUM=?n,GEN=?g,SEM=?slots]
FEELINGDEF[SEM=<all x.(?feeling(x) <-> ?experience(x))>] -> FEELING[CASE=nom,NUM=?n,SEM=?feeling] EXPERIENCE[CASE=nom,NUM=?n,SEM=?experience]
REFLECTIONDEF[SEM=<all x.(?reflection(x) <-> ?taking(x))>] -> REFLECTION[CASE=nom,NUM=?n,GEN=?g,SEM=?reflection] TAKING[CASE=nom,NUM=?n,GEN=?g,SEM=?taking]
MEMBERS[CASE=nom,NUM=pl,GEN=m,SEM=<\x.FacultyOrMeaning(x)>] -> 'indriya-arthāḥ'
SAME[CASE=nom,NUM=pl,GEN=m] -> 'te'
ONLY -> 'eva'
ACCEPTED[CASE=nom,NUM=pl,GEN=m,SEM=<\P.\Q.all x.(P(x) <-> Q(x))>] -> 'iṣṭāḥ'
SLOTS[CASE=nom,NUM=pl,GEN=m,SEM=<\x.(TenFormEssenceMember(x) & TenFormPrincipleMember(x))>] -> 'daśa-āyatana-dhātavaḥ'
FEELING[CASE=nom,NUM=sg,GEN=f,SEM=<\x.Feeling(x)>] -> 'vedanā'
EXPERIENCE[CASE=nom,NUM=sg,GEN=m,SEM=<\x.Experience(x)>] -> 'anubhavaḥ'
REFLECTION[CASE=nom,NUM=sg,GEN=f,SEM=<\x.Reflection(x)>] -> 'saṃjñā'
TAKING[CASE=nom,NUM=sg,GEN=f,SEM=<\x.MarkTaking(x)>] -> 'nimitta-udgrahaṇa-ātmikā'
```

```nltk-dep
'iṣṭāḥ' -> 'indriya-arthāḥ' | 'te' | 'daśa-āyatana-dhātavaḥ'
'te' -> 'eva'
'vedanā' -> 'anubhavaḥ'
'saṃjñā' -> 'nimitta-udgrahaṇa-ātmikā'
```

**Close construe.** Those very Faculties and meanings are accepted as
ten Essences and Principles. Feeling is undergoing. Reflection has taking
up a mark as its nature.

The classification predicates concern the ten Form members only, not all
twelve Essences or all eighteen Principles. A shared member variable
expresses cross-classification without identifying an Essence slot with
a Principle slot. The classification is represented as an accepted
equivalence; acceptance is not modeled as a separate agent's attitude.
The distributed count and the resumed field are resolved with the Bhāṣya,
not discovered by the parser. Cardinality and exclusion of *avijñapti*
are checked against the explicit roster in §8. The definition predicates
do not derive the commentary's three tones or six contact-groups.

## 5. Translation

### Literal Translation

> These very Faculties and meanings are accepted as the ten Essences and the
> ten Principles. Feeling is undergoing. Reflection has the taking up of the
> mark as its nature.

### Bhāṣya-informed study translation

> The five Faculties and five meanings are accepted as ten Essences and the
> same ten Principles. Feeling is experience; Reflection has taking up a
> mark as its nature.

## 6. Philosophical Translation

Again, two lines. The first carries the ten. The second opens feeling and
reflection.

These very ones. Not a new inventory. The Faculties and the meanings already
counted in the Form Base are accepted as ten Essences, and as the same ten Principles.
Eye Essence, Visible Form Essence, through Body Essence and Tangible Essence.
Eye Principle, Visible Form Principle, through Body Principle and
Tangible Principle. The lists alternate Faculty and meaning. *Yāvat* covers the
middle.

*Avijñapti* is in the Form Base. It is not in these ten. The Form Base account
closes before the new definitions begin.

Feeling is undergoing. Three tones: pleasant, painful, neither painful nor
pleasant. Six groups, born of contact, from the eye through Mind. Three tones
and six groups are not nine Bases.

Reflection takes up the mark. Blue and yellow, long and short, woman and man,
pleasant and painful, and the transmitted *mitramitra*. Friend and enemy is a
possible division, uncertain at the letter. Six groups, as with feeling. The
pattern transfers. The tones do not.

The next verse takes up formations. Not this one.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| indriya | Faculty | one of the five |
| artha | meaning | the five |
| skandha | Base | the Form Base, closed here |
| āyatana | Essence | ten |
| dhātu | Principle | the same ten |
| te eva | these very ones | identity across the arrangements |
| vedanā | feeling | undergoing |
| anubhava | undergoing | three tones |
| saṃsparśa | contact | the six groups |
| saṃjñā | Reflection | not worldly designation |
| nimitta | mark | what is taken up |
| udgrahaṇa | taking up | the operation |
| manas | Mind | Mind-contact; the sixth |

## 8. Logical Determination

**Kārikā, derived.** The same members receive both classifications.
Feeling and Reflection receive distinct functional definitions.

```nltk-sem
# derived by the section 4 parse
((all x.(FacultyOrMeaning(x) <-> (TenFormEssenceMember(x) & TenFormPrincipleMember(x)))) & (all x.(Feeling(x) <-> Experience(x))) & (all x.(Reflection(x) <-> MarkTaking(x))))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((all x.(FacultyOrMeaning(x) <-> (TenFormEssenceMember(x) & TenFormPrincipleMember(x)))) & (all x.(Feeling(x) <-> Experience(x))) & (all x.(Reflection(x) <-> MarkTaking(x))))
# THEORY prose
# EXPECT prose T
all x.(FacultyOrMeaning(x) <-> (SensoryFaculty(x) | SensoryMeaning(x)))
all x.(TenFormEssenceMember(x) <-> FacultyOrMeaning(x))
all x.(TenFormPrincipleMember(x) <-> FacultyOrMeaning(x))
FormBaseMember(avijnapti) & -FacultyOrMeaning(avijnapti)
all x.(Feeling(x) -> exists t.(FeelingTone(t) & HasTone(x,t)))
all x.(FeelingContactGroup(x) <-> ReflectionContactGroup(x))
Reflection(reflection_case) & TakesMark(reflection_case,blue_mark)
# THEORY rejected_avijnapti_in_these_ten
# EXPECT rejected_avijnapti_in_these_ten F
exists x.(x = avijnapti & TenFormEssenceMember(x))
# THEORY rejected_reflection_is_feeling
# EXPECT rejected_reflection_is_feeling F
all x.(Reflection(x) <-> Feeling(x))
# THEORY rejected_six_groups_are_three_tones
# EXPECT rejected_six_groups_are_three_tones F
all x.(FeelingContactGroup(x) <-> FeelingTone(x))
```

```nltk-valuation
avijnapti => avijnapti_case
reflection_case => blue_reflection
blue_mark => blue
SensoryFaculty => {eye,ear,nose,tongue,body}
SensoryMeaning => {visible,sound,odor,taste,tangible}
FacultyOrMeaning => {eye,ear,nose,tongue,body,visible,sound,odor,taste,tangible}
TenFormEssenceMember => {eye,ear,nose,tongue,body,visible,sound,odor,taste,tangible}
TenFormPrincipleMember => {eye,ear,nose,tongue,body,visible,sound,odor,taste,tangible}
FormBaseMember => {eye,ear,nose,tongue,body,visible,sound,odor,taste,tangible,avijnapti_case}
Feeling => {pleasant_case,painful_case,neutral_case}
Experience => {pleasant_case,painful_case,neutral_case}
Reflection => {blue_reflection}
MarkTaking => {blue_reflection}
FeelingTone => {pleasant,painful,neither}
HasTone => {(pleasant_case,pleasant),(painful_case,painful),(neutral_case,neither)}
FeelingContactGroup => {eye_contact,ear_contact,nose_contact,tongue_contact,body_contact,mind_contact}
ReflectionContactGroup => {eye_contact,ear_contact,nose_contact,tongue_contact,body_contact,mind_contact}
TakesMark => {(blue_reflection,blue)}
```

**Model checks.** Five distinct Faculty representatives and five distinct
meaning representatives give ten members, not twenty newly created
Dharmas. Exactly those ten occur under each local classification; the
eleventh Form member, *avijñapti*, is excluded from these ten, not from
every Essence or Principle classification. Removing either classification
of any of the ten fails the derived formula. Adding a spurious member to
only one classification is excluded by the separate prose equivalences,
not by the root formula's conjunction alone.

Three tone labels and six contact-group labels are different axes, not
nine Bases or nine Feeling kinds in one partition. The six labels are
shared grouping criteria, not six simultaneous contacts asserted for
every experience. The Reflection witness takes blue as a mark without
being a Feeling witness; changing either definition's extension must
fail. The finite model tests these distinctions, not a theory of every
possible experience or recognition.

**Bhāṣya determination.** *Vedanāvat* transfers the six-group pattern to
Reflection, not Feeling's three tones. The mark examples remain as
transmitted, including uncertain *mitramitra*. Mark-taking is the local
definition; the passage does not derive a theory of universals from it.

**Organon interpretation.** The proposed case is identifying an instance
as a cat without *vijñapti*, not first disclosing it and then abstracting a
kind from many disclosures. This motivates the One-over-Many inquiry into
*avijñapti*: how is a determination operative without disclosure?
Identifying, disclosing, and retaining a determination must remain
distinguishable. The verse supplies mark-taking as Reflection's definition;
it does not say that mark-taking requires *vijñapti*. Its relation to the
proposed *aviśeṣa–viśeṣa* logic remains to be developed rather than settled
by this grammar. The earlier schematic follows.

```text
Form Base
    five Faculties, five meanings, avijñapti

1.14
    Faculties and meanings
        → ten Essences
        → the same ten Principles
    avijñapti not among the ten

    feeling = undergoing
        three tones
        six groups, by contact
    reflection = taking up the mark
        six groups, as feeling

1.15 not opened
```

## 9. Interpretive Note

**Translation note.** The Bhāṣya identifies the ten as the five Faculties and their five meanings, excluding *avijñapti*. It explains feeling as threefold experience in six contact-groups, from eye-contact through Mind-contact, and Reflection as taking up marks, likewise in six groups.

The hinge is *te eva*. Interpretation of the two arrangements is in the
Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_14 a vak:Karika ;
    vak:hasTopic vak:SameTenFeelingReflection ;
    vak:belongsTo vak:Dhatunirdesa .

vak:FacultiesAndMeanings vak:acceptedAs vak:TenEssences ;
    vak:acceptedAs vak:TenPrinciples .
vak:Feeling vak:is vak:Undergoing .
vak:Reflection vak:nature vak:TakingUpTheMark .
vak:Avijnapti vak:notAmong vak:TheseTen .
```
