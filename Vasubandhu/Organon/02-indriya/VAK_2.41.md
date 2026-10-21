# VAK_2.41 — Same-Class and the Non-Reflective

## 1. Sanskrit (Devanāgarī)

```sanskrit
सभागता सत्त्वसाम्यमासंज्ञिकमसंज्ञिषु ।
निरोधश्चित्तचैत्तानां विपाकः ते बृहत्फलाः ॥ २.४१ ॥
```

## 2. Sanskrit (IAST)

```text
sabhāgatā sattvasāmyam āsaṃjñikam asaṃjñiṣu /
nirodhaś cittacaittānāṃ vipākaḥ te bṛhatphalāḥ // 2.41 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sabhāgatā | nom. sg. f. | same-class |
| sattvasāmyam | nom. sg. n.; compound | sameness among beings |
| āsaṃjñikam | nom. sg. n.; derivative | the non-reflective result, distinguished from its causal attainment |
| asaṃjñiṣu | loc. pl. m. | among non-reflective beings |
| nirodhaś cittacaittānām | nom. sg. m. + gen. pl. m.; compound | cessation of consciousness and the mental factors |
| vipākaḥ | nom. sg. m. | maturation |
| te bṛhatphalāḥ | nom. pl. m. pronoun + compound predicate | those beings belong to the Great Fruit gods |

*Nikāya-sabhāga* is the treatise's name for group same-class.

```text
# tokens: sabhāgatā sattvasāmyam āsaṃjñikam asaṃjñiṣu nirodhaḥ cittacaittānām vipākaḥ te bṛhatphalāḥ
```

## 4. Grammar

The first nominal equation defines same-class without deciding its disputed ontology. The second defines the non-reflective result as cessation of consciousness and mental factors among the specified beings. *Vipākaḥ* identifies that cessation as maturation; the prose names the non-reflective attainment as its cause. The final plural concerns the beings, not an identity of attainment and divine class. The prose specifies a subset in a region of the Great Fruit gods, not that all Great Fruit gods are non-reflective.

```nltk-fcfg
% start S
# tokens: sabhāgatā sattvasāmyam āsaṃjñikam asaṃjñiṣu nirodhaḥ cittacaittānām vipākaḥ te bṛhatphalāḥ
S[SEM=<(?same & ?cessation & ?maturation & ?beings)>] -> SAMECLASS[SEM=?same] CESSATION[SEM=?cessation] MATURATION[SEM=?maturation] BEINGS[SEM=?beings]
SAMECLASS[SEM=<Defines(same_class,sameness_among_beings)>] -> CLASS SAMENESS
CLASS -> 'sabhāgatā'
SAMENESS -> 'sattvasāmyam'
CESSATION[SEM=<CessationOf(nonreflective_result,consciousness_and_factors) & Among(nonreflective_result,nonreflective_beings)>] -> RESULT AMONG STOPPING FACTORS
RESULT -> 'āsaṃjñikam'
AMONG -> 'asaṃjñiṣu'
STOPPING -> 'nirodhaḥ'
FACTORS -> 'cittacaittānām'
MATURATION[SEM=<Maturation(nonreflective_result)>] -> RIPENING
RIPENING -> 'vipākaḥ'
BEINGS[SEM=<IncludedIn(nonreflective_beings,great_fruit_gods)>] -> THEY GREATFRUIT
THEY -> 'te'
GREATFRUIT -> 'bṛhatphalāḥ'
```

```nltk-dep
'sabhāgatā' -> 'sattvasāmyam'
'āsaṃjñikam' -> 'asaṃjñiṣu' | 'nirodhaḥ' | 'vipākaḥ'
'nirodhaḥ' -> 'cittacaittānām'
'bṛhatphalāḥ' -> 'te'
```

The constituent spans are [0, 2), [2, 6), [6, 7), and [7, 9).

## 5. Translation

### Literal Translation

> Same-class is sameness among beings. The non-reflective, among the non-reflective beings, is cessation of consciousness and the mental factors, a maturation; those beings are Great Fruit gods.

### Bhāṣya-informed study translation

> Same-class is sameness among beings. The non-reflective result among non-reflective beings is cessation of consciousness and the mental factors, a maturation. Those beings belong to the Great Fruit gods.

## 6. Philosophical Translation

> Shared recognition and designation do not by themselves establish a distinct real entity of same-class. The non-reflective result is a maturation of an attainment, not that attainment itself; its cessation occupies an interval bounded by reflection.

## 7. Technical Vocabulary

**Sabhāgatā.** Same-class, explained as sameness among beings; the status of an independent entity remains disputed.

**Āsaṃjñika.** The non-reflective result: cessation of consciousness and mental factors among the specified gods, a maturation of non-reflective attainment.

**Asaṃjñi-samāpatti.** Non-reflective attainment, the cause whose maturation is distinguished here; its detailed classification opens in 2.42.

**Bṛhatphala.** Great Fruit gods. Some in a particular region are non-reflective; the prose does not reverse that inclusion.

## 8. Logical Determination

The verse definitions, the four alternatives, and the maturation account are separate claims. No finite valuation decides whether same-class is a distinct real entity.

```nltk-sem
same_class : Defines(same_class,sameness_among_beings)
result : CessationOf(nonreflective_result,consciousness_and_factors) & Maturation(nonreflective_result)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(Defines(same_class,sameness_among_beings) & (CessationOf(nonreflective_result,consciousness_and_factors) & Among(nonreflective_result,nonreflective_beings)) & Maturation(nonreflective_result) & IncludedIn(nonreflective_beings,great_fruit_gods))

# THEORY prose_maturation_and_interval
# EXPECT prose_maturation_and_interval T
MaturationOf(nonreflective_result,nonreflective_attainment) & -(nonreflective_result = nonreflective_attainment)
ReflectiveAt(birth_boundary) & -ReflectiveAt(intervening_interval) & ReflectiveAt(death_boundary)
RebirthAfter(nonreflective_beings,desire_realm) & -RebirthAfter(nonreflective_beings,formless_realm)

# THEORY four_alternatives
# EXPECT four_alternatives T
DeathRebirth(same_class_rebirth) & -ClassChange(same_class_rebirth)
-DeathRebirth(entering_certainty) & ClassChange(entering_certainty)
DeathRebirth(destiny_transition) & ClassChange(destiny_transition)
-DeathRebirth(neither_case) & -ClassChange(neither_case)

# THEORY rejected_result_is_its_causal_attainment
# EXPECT rejected_result_is_its_causal_attainment F
Maturation(nonreflective_attainment) & (nonreflective_result = nonreflective_attainment)

# THEORY rejected_all_great_fruit_are_nonreflective
# EXPECT rejected_all_great_fruit_are_nonreflective F
all x.(GreatFruitMember(x) -> NonreflectiveMember(x))
```

```nltk-valuation
same_class => same_class_term
sameness_among_beings => sameness_definition
nonreflective_result => nonreflective_result_term
nonreflective_attainment => nonreflective_attainment_term
consciousness_and_factors => consciousness_factor_group
nonreflective_beings => nonreflective_being_group
great_fruit_gods => great_fruit_group
birth_boundary => birth_stage
intervening_interval => intervening_stage
death_boundary => death_stage
desire_realm => desire_realm_class
formless_realm => formless_realm_class
same_class_rebirth => same_class_rebirth_case
entering_certainty => entering_certainty_case
destiny_transition => destiny_transition_case
neither_case => neither_case_example
Defines => {(same_class_term,sameness_definition)}
CessationOf => {(nonreflective_result_term,consciousness_factor_group)}
Among => {(nonreflective_result_term,nonreflective_being_group)}
Maturation => {nonreflective_result_term}
MaturationOf => {(nonreflective_result_term,nonreflective_attainment_term)}
IncludedIn => {(nonreflective_being_group,great_fruit_group)}
ReflectiveAt => {birth_stage,death_stage}
RebirthAfter => {(nonreflective_being_group,desire_realm_class)}
DeathRebirth => {same_class_rebirth_case,destiny_transition_case}
ClassChange => {entering_certainty_case,destiny_transition_case}
GreatFruitMember => {nonreflective_member,other_great_fruit_member}
NonreflectiveMember => {nonreflective_member}
```

The case labels represent the prose's four alternatives, not a claim that every entry into certainty occurs apart from every possible rebirth context. The depicted case occurs without dying and being reborn. The two Great Fruit examples test the subset distinction, not a population count. Later rebirth in the Desire Realm is not the location of the non-reflective interval itself.

## 9. Interpretive Note

**Translation note.** The extended same-class debate distinguishes the real-entity account, its objections, the Vaiśeṣika comparison, the Vaibhāṣika scriptural appeal, and the designation reply. The second presentation distinguishes the non-reflective result from its causal attainment, the Great Fruit region from later Desire-Realm rebirth, and the intervening cessation from its reflective boundaries.

In the Organon reading, Cognition joins and governs Perception and Conception and guides the Dharma Base while remaining distinct from consciousness and Mind. Recognition of sameness calls for an account of the relation, not an automatic promotion of a common designation into another entity. Equally, the result of a practice must not be identified with the practice that conditions it. Detailed post-translation study of these Dharma presentations remains part of the later specialty pass.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_41 a vak:Karika ;
    vak:hasTopic vak:SameClass, vak:NonReflectiveResult .
vak:NonReflectiveResult vak:maturationOf vak:NonReflectiveAttainment .
vak:NonReflectiveBeings vak:includedAmong vak:GreatFruitGods .
```
