# VAK_1.23 — The Order of the Six

## 1. Sanskrit (Devanāgarī)

```sanskrit
प्राक्पञ्च वार्त्तमानार्थ्यात् भौतिकार्थ्याच्चतुष्टयम् ।
दूराशुतरवृत्त्यान्यत् यथास्थानं क्रमोऽथवा ॥ १.२३ ॥
```

## 2. Sanskrit (IAST)

```text
prāk pañca vārttamānārthyāt bhautikārthyāc catuṣṭayam /
dūrāśutaravṛttyānyat yathāsthānaṃ kramo 'thavā // 1.23 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| prāk | indeclinable | first; carried forward to the second clause |
| pañca | numeral | the five, beginning with the eye |
| vārttamāna-arthyāt | ablative abstract | because their Condition is present |
| bhautika-arthyāt | ablative abstract | because their Condition is Element-dependent Form |
| catuṣṭayam | nominative neuter singular collective | the four |
| dūra-āśutara-vṛttyā | instrumental feminine singular compound | by farther or quicker operation |
| anyat | nominative neuter singular | the remainder |
| yathā-sthānam | adverbial compound | according to site |
| kramaḥ | nominative masculine singular | the order |
| athavā | particle | an alternative |

The long instrumental is kept. The prose repeats it.

**Grammar tokens.** Verse-order IAST with sandhi opened and compound
boundaries marked. *Prāk* is not repeated as a token in the second clause;
the Bhāṣya's *prāg iti vartate* ("first" carries forward) is resolved in
the second reason's semantics.

```text
# tokens: prāk pañca vārttamāna-arthyāt bhautika-arthyāt catuṣṭayam dūra-āśutara-vṛttyā anyat yathā-sthānam kramaḥ athavā
```

## 4. Grammar

Four clauses. Two ablatives give reasons for precedence; an instrumental
gives the ground of the remaining order; *athavā* offers site as an
alternative ground. Case government, not gender agreement, carries the
structure: each reason must be ablative and the operation ground
instrumental.

```nltk-fcfg
% start S
# tokens: prāk pañca vārttamāna-arthyāt bhautika-arthyāt catuṣṭayam dūra-āśutara-vṛttyā anyat yathā-sthānam kramaḥ athavā
S[SEM=<(?first & ?second & ?third & ?alternative)>] -> FIRST[SEM=?first] SECOND[SEM=?second] THIRD[SEM=?third] ALT[SEM=?alternative]
FIRST[SEM=<?reason(?group)>] -> PRIOR GROUP[K=five,SEM=?group] REASON[CASE=abl,K=present,SEM=?reason]
SECOND[SEM=<?reason(?group)>] -> REASON[CASE=abl,K=bhautika,SEM=?reason] GROUP[K=four,SEM=?group]
THIRD[SEM=<?ground(?group)>] -> GROUND[CASE=ins,SEM=?ground] GROUP[K=rest,SEM=?group]
ALT[SEM=<?site(?order)>] -> SITE[SEM=?site] ORDER[CASE=nom,NUM=sg,SEM=?order] ALTERNATIVE
PRIOR -> 'prāk'
GROUP[K=five,SEM=<five_faculties>] -> 'pañca'
REASON[CASE=abl,K=present,SEM=<\g.PrecedesBecause(g,mind,present_conditions)>] -> 'vārttamāna-arthyāt'
REASON[CASE=abl,K=bhautika,SEM=<\g.PrecedesBecause(g,body,element_dependent_conditions)>] -> 'bhautika-arthyāt'
GROUP[K=four,SEM=<first_four>] -> 'catuṣṭayam'
GROUND[CASE=ins,SEM=<\g.(OrderedBy(g,farther_operation) & OrderedBy(g,quicker_operation))>] -> 'dūra-āśutara-vṛttyā'
GROUP[K=rest,SEM=<remaining_order>] -> 'anyat'
SITE[SEM=<\o.AlternativelyOrderedBy(o,site)>] -> 'yathā-sthānam'
ORDER[CASE=nom,NUM=sg,GEN=m,SEM=<six_order>] -> 'kramaḥ'
ALTERNATIVE -> 'athavā'
```

```nltk-dep
'pañca' -> 'prāk' | 'vārttamāna-arthyāt'
'catuṣṭayam' -> 'bhautika-arthyāt'
'anyat' -> 'dūra-āśutara-vṛttyā'
'kramaḥ' -> 'yathā-sthānam' | 'athavā'
```

**Close construe.** The five come first, because their Conditions are
present; the four, because their Conditions are Element-dependent Form;
the rest, by farther or quicker operation. Or the order is according to
site.

The second clause's "first" and its comparison with Body are supplied
from the Bhāṣya's carry-forward, not inserted as a token. The remainder
compound joins two comparisons that apply to different pairs: distance
for eye and ear before nose and tongue, then eye before ear; quickness
for nose before tongue. The parse records both grounds; §8 assigns them.
Site is an alternative account of the same six-fold order, not a fifth
cut in one elimination.

The commentary orders the six, beginning with the eye, among the Essences
and the Principles. The order of their Conditions and of their Cognitions
follows that order. It does not say the Faculties produce the Conditions.

## 5. Translation

### Literal Translation

> The five come first, because their Conditions are present. The four, because
> their Conditions are Element-dependent Form. The rest, by farther or quicker
> operation. Or the order is according to location.

### Bhāṣya-informed study translation

> The five Faculties come first because their Conditions are present. Of
> these, four precede the Body because they take Element-dependent Form as
> Condition. The remaining order follows distance or quicker operation—or,
> alternatively, bodily location.

## 6. Philosophical Translation

Again, two lines. The first is the cut. The second is the remainder, and an alternative.

The five Faculties work in the present. That is why they come first. Mind is not that restriction. Some of its Conditions are present. The rest of the compound is damaged, and it is not repaired. The secure claim is the contrast: present, against an unrestricted range.

Of the five, four take Element-dependent Form. The body is not restricted that way. Sometimes Great Elements, sometimes Element-dependent Form, sometimes both. *Prāk* carries forward. The four Faculties are first among the five, not a new list of six.

Eye and ear Faculties take a distant Condition, so they precede nose and tongue. Of those two, the eye operates farther: a river seen, its sound not heard. Nose and tongue do not operate at a distance. Nose is quicker in the example given: the odor of food before the food reaches the tongue. The phrase is damaged. The example is kept. It is not a measure of speed.

Or the sites. Eye site uppermost, then ear, nose, tongue. The body-site clause is damaged. Mind depends on those Faculties and has no place. That is the alternative. It does not redefine the Faculty as the gross site.

This closes the base, and only the Form System. The Faculties and the meanings are ordered here. The Dharma System is not this verse.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| pañca | the five | eye, ear, nose, tongue, body |
| vārttamāna-viṣaya | present Condition | why the five are first |
| manas | Mind | unrestricted range; no place |
| bhautika | Element-dependent Form | Condition of the four |
| bhūta | Element | possible Condition of Body |
| dūra-vṛtti | farther operation | eye before ear |
| āśutara-vṛtti | quicker operation | nose before tongue |
| adhiṣṭhāna | site | the alternative; not the Faculty |
| viṣaya | Condition | the range; not Object, not a finished thing |
| vijñāna | Cognition | follows the order of the six; not Principle |

## 8. Logical Determination

**Kārikā, derived.** Two precedence reasons, the remaining-order grounds,
and the alternative site ground are separate claims.

```nltk-sem
# derived by the section 4 parse
(PrecedesBecause(five_faculties,mind,present_conditions) & PrecedesBecause(first_four,body,element_dependent_conditions) & (OrderedBy(remaining_order,farther_operation) & OrderedBy(remaining_order,quicker_operation)) & AlternativelyOrderedBy(six_order,site))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(PrecedesBecause(five_faculties,mind,present_conditions) & PrecedesBecause(first_four,body,element_dependent_conditions) & (OrderedBy(remaining_order,farther_operation) & OrderedBy(remaining_order,quicker_operation)) & AlternativelyOrderedBy(six_order,site))
# THEORY prose
# EXPECT prose T
Precedes(eye,ear) & Precedes(ear,nose) & Precedes(nose,tongue) & Precedes(tongue,body) & Precedes(body,mind)
all x.(InGroup(x,five_faculties) -> PresentConditionOnly(x))
-PresentConditionOnly(mind) & TakesNonPresent(mind)
all x.(InGroup(x,first_four) -> InGroup(x,five_faculties))
all x.(InGroup(x,first_four) -> (TakesElementDependent(x) & -TakesGreatElement(x)))
TakesGreatElement(body) & TakesElementDependent(body)
DistantCondition(eye) & DistantCondition(ear) & -DistantCondition(nose) & -DistantCondition(tongue)
FartherOperation(eye,ear) & QuickerOperation(nose,tongue)
SiteAbove(eye,ear) & SiteAbove(ear,nose) & SiteAbove(nose,tongue)
Unlocalized(mind) & DependsOnFaculties(mind) & -Unconditioned(mind)
# THEORY rejected_mind_restricted_to_present
# EXPECT rejected_mind_restricted_to_present F
exists x.(x = mind & PresentConditionOnly(x))
# THEORY rejected_body_only_element_dependent
# EXPECT rejected_body_only_element_dependent F
all x.(x = body -> -TakesGreatElement(x))
# THEORY rejected_nose_operates_at_distance
# EXPECT rejected_nose_operates_at_distance F
exists x.(x = nose & DistantCondition(x))
# THEORY rejected_unlocalized_means_unconditioned
# EXPECT rejected_unlocalized_means_unconditioned F
all x.(Unlocalized(x) -> Unconditioned(x))
```

```nltk-valuation
five_faculties => five_group
first_four => four_group
remaining_order => remainder_comparisons
six_order => sixfold_sequence
present_conditions => present_ground
element_dependent_conditions => element_dependent_ground
farther_operation => farther_ground
quicker_operation => quicker_ground
site => site_ground
eye => eye_faculty
ear => ear_faculty
nose => nose_faculty
tongue => tongue_faculty
body => body_faculty
mind => mind_faculty
PrecedesBecause => {(five_group,mind_faculty,present_ground),(four_group,body_faculty,element_dependent_ground)}
OrderedBy => {(remainder_comparisons,farther_ground),(remainder_comparisons,quicker_ground)}
AlternativelyOrderedBy => {(sixfold_sequence,site_ground)}
Precedes => {(eye_faculty,ear_faculty),(ear_faculty,nose_faculty),(nose_faculty,tongue_faculty),(tongue_faculty,body_faculty),(body_faculty,mind_faculty)}
InGroup => {(eye_faculty,five_group),(ear_faculty,five_group),(nose_faculty,five_group),(tongue_faculty,five_group),(body_faculty,five_group),(eye_faculty,four_group),(ear_faculty,four_group),(nose_faculty,four_group),(tongue_faculty,four_group)}
PresentConditionOnly => {eye_faculty,ear_faculty,nose_faculty,tongue_faculty,body_faculty}
TakesNonPresent => {mind_faculty}
TakesElementDependent => {eye_faculty,ear_faculty,nose_faculty,tongue_faculty,body_faculty}
TakesGreatElement => {body_faculty}
DistantCondition => {eye_faculty,ear_faculty}
FartherOperation => {(eye_faculty,ear_faculty)}
QuickerOperation => {(nose_faculty,tongue_faculty)}
SiteAbove => {(eye_faculty,ear_faculty),(ear_faculty,nose_faculty),(nose_faculty,tongue_faculty)}
Unlocalized => {mind_faculty}
DependsOnFaculties => {mind_faculty}
Unconditioned => {}
```

**Model checks.** Six distinct Faculty constants form one immediate-
neighbor sequence without cycles. The four are a subset of the five;
Body is among the five but not the four; Mind is in neither group.
Removing either precedence reason or any ground fails the derived
formula. Exchanging the distance and quickness comparisons fails the
prose assignments. The site relation stops at tongue because the
body-site clause is damaged; the model does not repair it.

**Bhāṣya determination.** Mind's non-present range is secure; the compound
naming its further range (*vyadhvānadhra-*) is damaged and not
reconstructed. "Quicker" names the priority of odor before food reaches
the tongue, not a measured latency. Mind depends on the Faculties and is
not situated in a place; non-location does not make it unconditioned.

**Organon interpretation.** This closes the Form System's arrangement from
the Faculty outward. The order of Conditions and Cognitions follows the
Faculties' order; the Dharma System's reading from Principle through
Essence to Base is not derived by this verse. The earlier schematic
follows.

```text
six, beginning with the eye
    order of Conditions and Cognitions follows

five first
    present Condition
mind
    unrestricted
    compound damaged

four first, among the five
    Element-dependent Form
body
    Great Elements, Element-dependent Form, or both

eye and ear before nose and tongue
    distant Condition
eye before ear
    farther: the river
nose before tongue
    quicker: odor before the food arrives
    phrase damaged

alternative
    sites, descending
    body-site clause damaged
    mind depends, and has no place

Form System closed
Dharma System not this verse
1.24 not opened
```

## 9. Interpretive Note

**Translation note.** The Bhāṣya identifies the five as Faculties preceding
Mind because their Conditions are present, and the first four as preceding
Body because their Conditions are Element-dependent Form. Mind also takes
non-present Conditions, but the associated compound is damaged; Body may take
Great Elements, Element-dependent Form, or both. Eye and ear have distant
Conditions, with eye operating farther (the river example); nose precedes
tongue because it takes odor before food reaches the tongue, though this
phrase is damaged. Alternatively, the sequence follows bodily sites from eye
through tongue; the body-site phrase is damaged, and Mind depends on the
Faculties without being localized.

The hinge is *prāk*, then *athavā*. Interpretation of the close of the Form System is in the Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_23 a vak:Karika ;
    vak:hasTopic vak:OrderOfTheSix ;
    vak:belongsTo vak:Dhatunirdesa ;
    vak:closes vak:FormSystem .

vak:FiveFaculties vak:take vak:PresentCondition ;
    vak:orderedBefore vak:Mind .
vak:FourFaculties vak:take vak:ElementDependentForm ;
    vak:orderedBefore vak:BodyFaculty .
vak:LocationOrder vak:alternative true .
```
