# VAK_1.22 — The Unconditioned, and the Order of the Bases

## 1. Sanskrit (Devanāgarī)

```sanskrit
स्कन्धेष्वसंस्कृतं नोक्तमर्थायोगात् क्रमः पुनः ।
यथौदारिकसंक्लेशभाजनाद्यर्थधातुतः ॥ १.२२ ॥
```

## 2. Sanskrit (IAST)

```text
skandheṣv asaṃskṛtaṃ noktam arthāyogāt kramaḥ punaḥ /
yathaudārikasaṃkleśabhājanādyarthadhātutaḥ // 1.22 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| skandheṣu | locative plural | among the bases |
| asaṃskṛtam | nominative neuter | the unconditioned |
| na | negative particle | not |
| uktam | nominative neuter singular passive participle | stated; agrees with the unconditioned |
| arthāyogāt | ablative | the defining meaning does not apply |
| kramaḥ | nominative | the order |
| punaḥ | indeclinable | a second question |
| yathā-audārika-saṃkleśa-bhājana-ādi-artha-dhātutaḥ | compressed adverbial compound with ablatival ending | according to grossness, affliction, vessel and the other roles, and Realm or level |

The second line names four grounds. The commentary unfolds them. They are not one label.

**Grammar tokens.** Verse-order IAST with sandhi opened and compound
boundaries marked. The final compressed compound stays one leaf; its
fourfold interpretation follows the Bhāṣya. No covert token is supplied.

```text
# tokens: skandheṣu asaṃskṛtam na uktam artha-ayogāt kramaḥ punaḥ yathā-audārika-saṃkleśa-bhājana-ādi-artha-dhātutaḥ
```

## 4. Grammar

The first clause negates inclusion among the Bases and supplies an
ablative reason. Neuter singular *uktam* agrees with *asaṃskṛtam*.
The second clause is nominal: *kramaḥ punaḥ* introduces a further
question, answered by the compressed ordering compound.

```nltk-fcfg
% start S
# tokens: skandheṣu asaṃskṛtam na uktam artha-ayogāt kramaḥ punaḥ yathā-audārika-saṃkleśa-bhājana-ādi-artha-dhātutaḥ
S[SEM=<(?exclusion & ?ordering)>] -> EXCLUSION[SEM=?exclusion] ORDERING[SEM=?ordering]
EXCLUSION[SEM=<all x.(?unconditioned(x) -> (?negative(?stated(?bases))(x) & ?reason(x)))>] -> BASES[CASE=loc,SEM=?bases] UNCONDITIONED[CASE=nom,NUM=?n,GEN=?g,SEM=?unconditioned] NEG[SEM=?negative] STATED[CASE=nom,NUM=?n,GEN=?g,SEM=?stated] REASON[CASE=abl,SEM=?reason]
ORDERING[SEM=<?grounds(?order)>] -> ORDER[CASE=nom,NUM=sg,SEM=?order] RESUME GROUNDS[SEM=?grounds]
BASES[CASE=loc,NUM=pl,SEM=<\x.BaseMember(x)>] -> 'skandheṣu'
UNCONDITIONED[CASE=nom,NUM=sg,GEN=n,SEM=<\x.Unconditioned(x)>] -> 'asaṃskṛtam'
NEG[SEM=<\P.\x.-P(x)>] -> 'na'
STATED[CASE=nom,NUM=sg,GEN=n,SEM=<\P.P>] -> 'uktam'
REASON[CASE=abl,SEM=<\x.CollectionMeaningInapplicable(x)>] -> 'artha-ayogāt'
ORDER[CASE=nom,NUM=sg,GEN=m,SEM=<base_order>] -> 'kramaḥ'
RESUME -> 'punaḥ'
GROUNDS[SEM=<\o.(OrderingGround(o,grossness) & OrderingGround(o,affliction) & OrderingGround(o,meal_roles) & OrderingGround(o,levels))>] -> 'yathā-audārika-saṃkleśa-bhājana-ādi-artha-dhātutaḥ'
```

```nltk-dep
'uktam' -> 'skandheṣu' | 'asaṃskṛtam' | 'na' | 'artha-ayogāt'
'kramaḥ' -> 'punaḥ' | 'yathā-audārika-saṃkleśa-bhājana-ādi-artha-dhātutaḥ'
```

**Close construe.** The unconditioned is not stated among the Bases,
because the meaning does not apply. The order, again, follows grossness,
affliction, the meanings beginning with a vessel, and Realm or level.

`BaseMember` projects being stated among the Bases as classification,
not a speech event. The reason is collection's inapplicability, not
absence of all plurality among the unconditioned. The four grounds are
resolved in the final compound's semantics; the parse does not itself
derive their detailed accounts. The grounds' shared target is one order,
not four competing Base rosters.

*Kramaḥ punaḥ* opens the order. 1.21 promised three ways. This unit gives four accounts. The discrepancy is kept.

## 5. Translation

### Literal Translation

> The unconditioned is not stated among the bases, because the meaning does
> not apply. The order, again, is according to grossness, affliction, the
> meaning beginning with a vessel, and Realm or level.

### Bhāṣya-informed study translation

> The unconditioned is not stated among the Bases, since the meaning of
> collection does not apply. The order, however, is according to grossness,
> affliction, the meanings beginning with a vessel, and the Realms and levels.

## 6. Philosophical Translation

Again, two lines. The first is the exclusion. The second is the order.

The unconditioned belongs to the system. It does not belong to the base. A base gathers a multiplicity across past, future, present, and the rest of the sūtra's list. The unconditioned is not that gathering. A sixth base would keep the word and drop the operation. The pot analogy fails for the same reason: cessation of a pot is not a pot, but the unconditioned is still an essence and a principle. The ranges differ.

The order is four accounts, not one.

Gross first. Form is resistant. Feeling is located: in my hand, in my foot. Reflection is grosser than the two that remain. Formations are grosser than the cognition-base. What is grosser is stated first.

Affliction next, and the direction is not the order of the list. Attraction to form is from greed for the savor of feeling. That greed is from inverted reflection. That inversion is from the afflictions. Consciousness is afflicted by them. The list runs forward. The explanation runs back.

The meal is five roles. Form is the vessel. Feeling is the food. Reflection is the seasoning. Formations are the maker. The cognition is the eater. The closing recap says vessel and seasoning for feeling and reflection. The earlier analogy said food and seasoning. The discrepancy is kept.

The last account is the levels. The Desire Realm is distinguished by the forms of sensual pleasure. The dhyānas by feeling. The first three formless by reflection. The summit by formations alone. These are the stations in which Cognition is established, as seed in a field. The stations are not a deletion of Cognition.

Five, neither fewer nor more. Feeling and reflection are apart from the formations because they are grosser, because they are causes in the affliction sequence, and because two levels are distinguished by them.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| asaṃskṛta | unconditioned | not a base |
| artha-ayoga | the meaning does not apply | collection does not fit |
| rāśi | collection | the meaning of base |
| audārika | gross | first ground of order |
| saṃkleśa | affliction | second ground; direction runs back |
| bhājana | vessel | form |
| bhojana | food | feeling; the recap says vessel |
| vyañjana | seasoning | reflection |
| kartṛ | maker | formations |
| bhoktṛ | eater | the cognition |
| vijñāna-sthiti | station of the cognition | the levels |
| kṣetra-bīja | field and seed | the sequence displays this |
| dhātutaḥ | according to the levels | not the eighteen |
| citta | consciousness | afflicted by the afflictions |
| bhavāgra | summit of existence | formations predominate |

## 8. Logical Determination

**Kārikā, derived.** Exclusion and the four grounds of one order are
separate claims.

```nltk-sem
# derived by the section 4 parse
((all x.(Unconditioned(x) -> (-BaseMember(x) & CollectionMeaningInapplicable(x)))) & (OrderingGround(base_order,grossness) & OrderingGround(base_order,affliction) & OrderingGround(base_order,meal_roles) & OrderingGround(base_order,levels)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((all x.(Unconditioned(x) -> (-BaseMember(x) & CollectionMeaningInapplicable(x)))) & (OrderingGround(base_order,grossness) & OrderingGround(base_order,affliction) & OrderingGround(base_order,meal_roles) & OrderingGround(base_order,levels)))
# THEORY prose
# EXPECT prose T
all x.(Unconditioned(x) -> (DharmaEssenceMember(x) & DharmaPrincipleMember(x)))
Precedes(form,feeling) & Precedes(feeling,reflection) & Precedes(reflection,formations) & Precedes(formations,cognition)
MealRole(form,vessel) & MealRole(feeling,food) & MealRole(reflection,seasoning) & MealRole(formations,maker) & MealRole(cognition,eater)
CharacterizedBy(desire_realm,form) & CharacterizedBy(dhyanas,feeling) & CharacterizedBy(first_three_formless,reflection) & CharacterizedBy(summit,formations)
# THEORY rejected_excluded_from_the_system
# EXPECT rejected_excluded_from_the_system F
all x.(Unconditioned(x) -> -DharmaEssenceMember(x))
# THEORY rejected_sixth_base
# EXPECT rejected_sixth_base F
exists x.(Unconditioned(x) & BaseMember(x))
# THEORY rejected_meal_recap_replaces_food
# EXPECT rejected_meal_recap_replaces_food F
all x.(x = feeling -> MealRole(x,vessel))
```

```nltk-valuation
base_order => five_base_sequence
grossness => grossness_account
affliction => affliction_account
meal_roles => meal_account
levels => realm_level_account
form => form_base
feeling => feeling_base
reflection => reflection_base
formations => formations_base
cognition => cognition_base
vessel => vessel_role
food => food_role
seasoning => seasoning_role
maker => maker_role
eater => eater_role
desire_realm => desire_level
dhyanas => dhyana_levels
first_three_formless => lower_formless_levels
summit => summit_level
Unconditioned => {space_case,discrimination_cessation,nonarising_cessation}
CollectionMeaningInapplicable => {space_case,discrimination_cessation,nonarising_cessation}
BaseMember => {form_case,feeling_case,reflection_case,formation_case,cognition_case}
DharmaEssenceMember => {space_case,discrimination_cessation,nonarising_cessation}
DharmaPrincipleMember => {space_case,discrimination_cessation,nonarising_cessation}
OrderingGround => {(five_base_sequence,grossness_account),(five_base_sequence,affliction_account),(five_base_sequence,meal_account),(five_base_sequence,realm_level_account)}
BaseKind => {form_base,feeling_base,reflection_base,formations_base,cognition_base}
Precedes => {(form_base,feeling_base),(feeling_base,reflection_base),(reflection_base,formations_base),(formations_base,cognition_base)}
MealRole => {(form_base,vessel_role),(feeling_base,food_role),(reflection_base,seasoning_role),(formations_base,maker_role),(cognition_base,eater_role)}
CharacterizedBy => {(desire_level,form_base),(dhyana_levels,feeling_base),(lower_formless_levels,reflection_base),(summit_level,formations_base)}
```

**Model checks.** Three unconditioned representatives remain outside Base
membership while retaining Dharma classifications. Those classifications
are populated only for this local test, not exhaustively enumerated.
`BaseKind` contains five distinct class labels; `BaseMember` contains
representative members, not those labels. Four distinct grounds target
the one sequence. `Precedes` records immediate neighbors only, not a
causal chain or a transitive closure.

The main meal analogy assigns Feeling food, not vessel. The recap's
transmitted vessel is preserved below and in the paired prose as a
discrepancy; it does not overwrite the main analogy's relation.
Level groups are represented as groups, not counts of individual
attainments. Predominance does not delete Cognition from its stations.

**Bhāṣya determination.** The pot-cessation analogy is others' proposal,
rejected because the analogous inference would exclude the unconditioned
from Essences and Principles too. The affliction explanation runs back
through savor, inverted Reflection, and afflictions, with consciousness
afflicted; it does not assert that the Base order is a forward production
chain. Grossness, that explanation, the meal analogy, and levels are four
accounts despite the prior promise of three. Neither discrepancy is
silently repaired.

**Organon interpretation.** One sequence admits different explanatory
relations. Their shared order does not make presentation, affliction,
cooperation, and level-predominance identical operations. The unconditioned
remains accessible through Dharma classifications without being forced
into a collection it does not instantiate. The earlier schematic follows.

```text
unconditioned
    not in the five
    not a sixth base
    still essence and principle
    pot analogy refused

order
    gross to subtle
    affliction, explanation running back
    vessel, food, seasoning, maker, eater
    levels: desire, dhyāna, three formless, summit
        stations of Cognition
        seed in field

five, neither fewer nor more
1.21 promised three; this unit gives four
recap says vessel where the analogy said food
both kept
1.23 not opened
```

## 9. Interpretive Note

**Translation note.** The commentary takes the first order-ground as relative
grossness, the second as an affliction-sequence explained backwards, the third
through the meal-roles (Form as vessel, feeling as food, reflection as
seasoning, formations as maker, Cognition as eater), and the fourth by levels
from desire through the summit. It rejects the pot-cessation argument for
excluding the unconditioned from Essences and Principles, and concludes that
there are five Bases, neither fewer nor more. Though 1.21 promised three
explanations, this passage gives four; its recap also says vessel where the
analogy said food.

The hinge is *arthāyogāt*, then *kramaḥ punaḥ*. Interpretation of the four grounds is in the Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_22 a vak:Karika ;
    vak:hasTopic vak:UnconditionedAndBaseOrder ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Unconditioned vak:notIncludedIn vak:Base ;
    vak:includedIn vak:DharmaEssence, vak:DharmaPrinciple .
vak:BaseOrder vak:justifiedBy vak:Grossness, vak:Affliction,
    vak:VesselAnalogy, vak:Levels ;
    vak:count 5 .
```
