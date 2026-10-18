# VAK_1.15 — Formations, and the Dharma Essence and Principle

## 1. Sanskrit (Devanāgarī)

```sanskrit
चतुर्भ्योऽन्ये तु संस्कारस्कन्धः एते पुनस्त्रयः ।
धर्मायतनधात्वाख्याः सहाविज्ञप्त्यसंस्कृतैः ॥ १.१५ ॥
```

## 2. Sanskrit (IAST)

```text
caturbhyo 'nye tu saṃskāraskandhaḥ ete punas trayaḥ /
dharmāyatanadhātvākhyāḥ sahāvijñaptyasaṃskṛtaiḥ // 1.15 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| caturbhyaḥ | ablative plural numeral | apart from the four Bases |
| anye | nominative masculine plural | the others |
| tu | particle | the remainder |
| saṃskāra-skandhaḥ | nominative masculine singular | one Formations Base |
| ete | nominative masculine plural pronoun | these |
| punaḥ | particle | resumes them under the further name |
| trayaḥ | nominative masculine numeral | three |
| dharma-āyatana-dhātu-ākhyāḥ | nominative masculine plural compound | bearing the names Dharma Essence and Dharma Principle |
| saha | governs instrumental | together with |
| avijñaptyasaṃskṛtaiḥ | instrumental plural | the two accompaniments |

*Saṃskāra* is formation. *Asaṃskṛta* is unconditioned, the negation of
conditioned. *Āyatana* is Essence. *Dhātu* is Principle. *Ākhyā* is the name.

**Grammar tokens.** Verse-order IAST with external sandhi opened and
compound boundaries marked. *Saha* is separated from the instrumental
compound it governs. The four and three are resolved with the Bhāṣya;
their names are not inserted into the verse.

```text
# tokens: caturbhyaḥ anye tu saṃskāra-skandhaḥ ete punaḥ trayaḥ dharma-āyatana-dhātu-ākhyāḥ saha avijñapti-asaṃskṛtaiḥ
```

## 4. Grammar

Plural *anye* is gathered under singular *saṃskāra-skandhaḥ*: many
formations, one Base. *Ete trayaḥ* resumes Feeling, Reflection, and
Formations. *Saha* governs the instrumental accompaniments; it does not
make them additional Bases.

```nltk-fcfg
% start S
# tokens: caturbhyaḥ anye tu saṃskāra-skandhaḥ ete punaḥ trayaḥ dharma-āyatana-dhātu-ākhyāḥ saha avijñapti-asaṃskṛtaiḥ
S[SEM=<(?remainder & ?classification)>] -> REMAINDER[SEM=?remainder] CLASSIFICATION[SEM=?classification]
REMAINDER[SEM=<?other(?four)(?base)>] -> FOUR[CASE=abl,NUM=pl,SEM=?four] OTHER[CASE=nom,NUM=pl,GEN=m,SEM=?other] CONTRAST BASE[CASE=nom,NUM=sg,GEN=m,SEM=?base]
CLASSIFICATION[SEM=<?names(?three)(?accomp)>] -> THESE[CASE=nom,NUM=?n,GEN=?g] AGAIN THREE[CASE=nom,NUM=?n,GEN=?g,SEM=?three] NAMES[CASE=nom,NUM=?n,GEN=?g,SEM=?names] ACCOMPANIMENT[SEM=?accomp]
ACCOMPANIMENT[SEM=?members] -> WITH[OBJCASE=?case] ACCOMP[CASE=?case,NUM=pl,SEM=?members]
FOUR[CASE=abl,NUM=pl,SEM=<\x.OtherFourBaseMember(x)>] -> 'caturbhyaḥ'
OTHER[CASE=nom,NUM=pl,GEN=m,SEM=<\P.\Q.all x.(Conditioned(x) -> (Q(x) <-> -P(x)))>] -> 'anye'
CONTRAST -> 'tu'
BASE[CASE=nom,NUM=sg,GEN=m,SEM=<\x.FormationsBaseMember(x)>] -> 'saṃskāra-skandhaḥ'
THESE[CASE=nom,NUM=pl,GEN=m] -> 'ete'
AGAIN -> 'punaḥ'
THREE[CASE=nom,NUM=pl,GEN=m,SEM=<\x.ThreeBaseMember(x)>] -> 'trayaḥ'
NAMES[CASE=nom,NUM=pl,GEN=m,SEM=<\P.\Q.all x.((DharmaEssenceMember(x) <-> (P(x) | Q(x))) & (DharmaPrincipleMember(x) <-> (P(x) | Q(x))))>] -> 'dharma-āyatana-dhātu-ākhyāḥ'
WITH[OBJCASE=ins] -> 'saha'
ACCOMP[CASE=ins,NUM=pl,SEM=<\x.(Avijnapti(x) | Unconditioned(x))>] -> 'avijñapti-asaṃskṛtaiḥ'
```

```nltk-dep
'saṃskāra-skandhaḥ' -> 'anye'
'anye' -> 'caturbhyaḥ' | 'tu'
'dharma-āyatana-dhātu-ākhyāḥ' -> 'ete' | 'saha'
'ete' -> 'punaḥ' | 'trayaḥ'
'saha' -> 'avijñapti-asaṃskṛtaiḥ'
```

**Close construe.** The others, apart from the four, are the Formations
Base. These three, again, together with *avijñapti* and the unconditioned,
bear the names Dharma Essence and Dharma Principle.

The remainder rule is restricted to conditioned Dharmas: "other than
the four" does not sweep the unconditioned into Formations. That domain
restriction comes from the preceding Base classification and is explicit
in the semantics. Plural subject and singular collective predicate do
not require number agreement. Actual agreement connects *ete*, *trayaḥ*,
and *ākhyāḥ*; case government connects *saha* to its complement.
The two names classify the same members without identifying their slots.
The Bhāṣya's sevenfold count is checked separately, not computed from
the numeral *trayaḥ* alone.

## 5. Translation

### Literal Translation

> The others, apart from the four, are the Formations Base. These three,
> again, together with *avijñapti* and the unconditioned, are called the
> Dharma Essence and the Dharma Principle.

### Bhāṣya-informed study translation

> Apart from the four, the others are the Formations Base. These three—
> Feeling, Reflection, and Formations—together with *avijñapti* and the
> unconditioned are also named the Dharma Essence and the Dharma Principle.

## 6. Philosophical Translation

Again, two lines. The first gathers the remainder. The second names the three
under Essence and Principle, and brings two accompaniments with them.

Apart from the four. The commentary names them: Form, feeling, Reflection, and
the Cognition Base. The others are formations, and those formations are one
Base. The unconditioned does not enter this remainder.

The sūtra says six groups of volition. Predominance, not exhaustion. Volition
is predominant in the active forming, because it has the nature of karma. It
actively forms the conditioned; therefore it is called the Formations Base of
appropriation. The name can be taught from the chief member. The Base is not
the chief member alone.

Otherwise the remaining associated factors, and the dissociated formations,
would not be gathered in a Base. They would not be suffering and origin. Full
comprehension and abandonment would not apply to them. The Blessed One does
not declare the ending of suffering without directly knowing and fully
comprehending even a single dharma. Likewise, without abandoning. Their
inclusion must be accepted. The argument is inclusion. It does not make the
classifying itself the abandonment.

These three, again. Feeling, Reflection, formations. Not the Cognition Base.
Together with *avijñapti* and the unconditioned, they bear the names
Dharma Essence and Dharma Principle.

Seven, in the commentary. Three Bases. *Avijñapti*. Space, cessation through
discrimination, cessation without discrimination. *Avijñapti* remains Form,
and remains in the Form Base. The unconditioned has no Base. The shared name
does not make them one kind.

The placement left open at 1.14 is made here. The ten did not include the
continuity. The continuity enters the Dharma Essence and the Dharma Principle,
and does not leave the Form Base.

The next verse defines the Cognition Base. Not this one.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| caturbhyaḥ | apart from the four | Form, feeling, Reflection, Cognition Base |
| saṃskāra | formation | the remainder |
| skandha | Base | one Formations Base |
| cetanā | volition | predominant, not exhaustive |
| abhisaṃskaroti | actively forms | the conditioned |
| caitasika | associated factor | must be included |
| viprayukta | dissociated | must be included |
| ete trayaḥ | these three | feeling, Reflection, formations |
| dharma-āyatana | Dharma Essence | the name |
| dharma-dhātu | Dharma Principle | the name |
| avijñapti | *avijñapti* | remains Form |
| asaṃskṛta | unconditioned | no Base |
| sapta dravyāṇi | seven | the commentary's count |

## 8. Logical Determination

**Kārikā, derived.** The conditioned remainder and the two Dharma
classifications are distinct rules.

```nltk-sem
# derived by the section 4 parse
((all x.(Conditioned(x) -> (FormationsBaseMember(x) <-> -OtherFourBaseMember(x)))) & (all x.((DharmaEssenceMember(x) <-> (ThreeBaseMember(x) | (Avijnapti(x) | Unconditioned(x)))) & (DharmaPrincipleMember(x) <-> (ThreeBaseMember(x) | (Avijnapti(x) | Unconditioned(x)))))))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((all x.(Conditioned(x) -> (FormationsBaseMember(x) <-> -OtherFourBaseMember(x)))) & (all x.((DharmaEssenceMember(x) <-> (ThreeBaseMember(x) | (Avijnapti(x) | Unconditioned(x)))) & (DharmaPrincipleMember(x) <-> (ThreeBaseMember(x) | (Avijnapti(x) | Unconditioned(x)))))))
# THEORY prose
# EXPECT prose T
all x.(ThreeBaseMember(x) <-> (FeelingBaseMember(x) | ReflectionBaseMember(x) | FormationsBaseMember(x)))
all x.(OtherFourBaseMember(x) <-> (FormBaseMember(x) | FeelingBaseMember(x) | ReflectionBaseMember(x) | CognitionBaseMember(x)))
all x.(FormationsBaseMember(x) -> (Conditioned(x) & BaseMember(x)))
all x.(Unconditioned(x) -> (-BaseMember(x) & -Conditioned(x)))
all x.(Avijnapti(x) -> (FormBaseMember(x) & BaseMember(x)))
all x.(Volition(x) -> FormationsBaseMember(x))
exists x.(AssociatedOther(x) & FormationsBaseMember(x) & -Volition(x))
exists x.(DissociatedFormation(x) & FormationsBaseMember(x) & -Volition(x))
exists x.(FormationsBaseMember(x) & Pure(x))
# THEORY rejected_formations_are_only_volition
# EXPECT rejected_formations_are_only_volition F
all x.(FormationsBaseMember(x) -> Volition(x))
# THEORY rejected_unrestricted_remainder
# EXPECT rejected_unrestricted_remainder F
all x.(FormationsBaseMember(x) <-> -OtherFourBaseMember(x))
# THEORY rejected_dharma_members_all_have_a_base
# EXPECT rejected_dharma_members_all_have_a_base F
all x.(DharmaEssenceMember(x) -> BaseMember(x))
# THEORY rejected_cognition_is_one_of_these_three
# EXPECT rejected_cognition_is_one_of_these_three F
all x.(CognitionBaseMember(x) -> ThreeBaseMember(x))
```

```nltk-valuation
Conditioned => {ordinary_form,avijnapti_case,feeling_case,reflection_case,cognition_case,volition_case,associated_case,dissociated_case,pure_path_case}
FormBaseMember => {ordinary_form,avijnapti_case}
FeelingBaseMember => {feeling_case}
ReflectionBaseMember => {reflection_case}
CognitionBaseMember => {cognition_case}
OtherFourBaseMember => {ordinary_form,avijnapti_case,feeling_case,reflection_case,cognition_case}
FormationsBaseMember => {volition_case,associated_case,dissociated_case,pure_path_case}
ThreeBaseMember => {feeling_case,reflection_case,volition_case,associated_case,dissociated_case,pure_path_case}
Avijnapti => {avijnapti_case}
Unconditioned => {space_case,discrimination_cessation,nonarising_cessation}
BaseMember => {ordinary_form,avijnapti_case,feeling_case,reflection_case,cognition_case,volition_case,associated_case,dissociated_case,pure_path_case}
DharmaEssenceMember => {feeling_case,reflection_case,volition_case,associated_case,dissociated_case,pure_path_case,avijnapti_case,space_case,discrimination_cessation,nonarising_cessation}
DharmaPrincipleMember => {feeling_case,reflection_case,volition_case,associated_case,dissociated_case,pure_path_case,avijnapti_case,space_case,discrimination_cessation,nonarising_cessation}
Volition => {volition_case}
AssociatedOther => {associated_case}
DissociatedFormation => {dissociated_case}
Pure => {pure_path_case}
```

**Model checks.** The model deliberately gives Formations several
representatives: volition, another associated factor, a dissociated
formation, and a Pure Path case. Therefore the commentary's seven
constituents cannot mean seven individual Dharmas. Tests construct its
seven disjoint categories: three Base classes, *avijñapti*, and the three
unconditioned representatives. Their union covers the Dharma members.
Every member must receive both classifications, but only the conditioned
members have a Base. *Avijñapti* retains Form membership; Cognition
does not become one of "these three."

**Bhāṣya determination.** Volition predominates in active forming; the
six volition-groups do not exhaust the Base. Inclusion of the other
associated and dissociated formations is defended through the argument
about suffering, origin, full comprehension, and abandonment. That
argument is not a claim that classification itself abandons anything,
nor a denial of the conditioned Pure Path. The full argument remains
in the paired prose; this model tests inclusion rather than deriving
the ending of suffering.

**Organon interpretation.** The same *avijñapti* is Form-classified and
Dharma-classified, not duplicated across two systems. This gives the
Form–Essence inquiry an explicit cross-classification to work with.
The unconditioned shares the Dharma names without acquiring a Base:
one protocol entry must preserve these different statuses. The earlier
schematic follows.

```text
apart from four
    Form, feeling, Reflection, Cognition Base
    → the others are the Formations Base
    volition predominant
    remainder included

these three
    feeling, Reflection, formations
    with avijñapti and the unconditioned
    → Dharma Essence and Dharma Principle

seven
    three Bases
    avijñapti, still Form
    three unconditioned, no Base

Cognition Base not among the three
1.16 not opened
```

## 9. Interpretive Note

**Translation note.** The Bhāṣya identifies the four as Form, feeling, Reflection, and the Cognition Base, and “these three” as feeling, Reflection, and formations. Together with *avijñapti* and the unconditioned, they bear the names Dharma Essence and Dharma Principle. The commentary further counts seven constituents.

The hinges are *anye* and *saha*. Interpretation of the seven is in the
Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_15 a vak:Karika ;
    vak:hasTopic vak:FormationsAndDharmaNames ;
    vak:belongsTo vak:Dhatunirdesa .

vak:FormationsBase vak:apartFrom vak:FourBases .
vak:ThreeBases vak:named vak:DharmaEssence, vak:DharmaPrinciple ;
    vak:togetherWith vak:Avijnapti, vak:Unconditioned .
vak:Avijnapti vak:remains vak:Form .
vak:Unconditioned vak:hasBase false .
vak:CognitionBase vak:notAmong vak:TheseThree .
```
