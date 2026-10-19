# VAK_2.34 — One Meaning, Fivefold Association

## 1. Sanskrit (Devanāgarī)

```sanskrit
चित्तं मनोऽथ विज्ञानमेकार्थं चित्तचैतसाः ।
साश्रयालम्बनाकाराः संप्रयुक्ताश्च पञ्चधा ॥ २.३४ ॥
```

## 2. Sanskrit (IAST)

```text
cittaṃ mano 'tha vijñānam ekārthaṃ cittacaitasāḥ /
sāśrayālambanākārāḥ saṃprayuktāś ca pañcadhā // 2.34 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| cittam | nom. sg. n. | consciousness |
| manaḥ | nom. sg. n. | Mind |
| atha / ca | coordinating particles | and / and |
| vijñānam | nom. sg. n. | Cognition |
| eka-artham | nom. sg. n.; compound | one meaning |
| citta-caitasāḥ | nom. pl. m.; compound | consciousness and the mental factors |
| sa-āśraya-ālambana-ākārāḥ | nom. pl. m.; compound adjective with sa- carried across the members | having Basis, Cognitive Condition, and manner |
| saṃprayuktāḥ | nom. pl. m.; past passive participle | associated |
| pañcadhā | adverb | fivefold |

Artha is meaning. Vijñāna is Cognition. Not Principle.

The compound predicates are not independently inflected singular
nouns. External sandhi is opened for parsing.

```text
# tokens: cittam manaḥ atha vijñānam ekārtham cittacaitasāḥ sāśrayālambanākārāḥ saṃprayuktāḥ ca pañcadhā
```

## 4. Grammar

The first clause predicates one meaning of three designations.
The second gives three having-predicates of consciousness and
factors, then specifies association as fivefold. The prose explains
the naming roles and enumerates the five equalities. Those
explanations are not extra words in the verse.

```nltk-fcfg
% start S
# tokens: cittam manaḥ atha vijñānam ekārtham cittacaitasāḥ sāśrayālambanākārāḥ saṃprayuktāḥ ca pañcadhā
S[SEM=<(?names & ?pair)>] -> NAMES[SEM=?names] PAIR[SEM=?pair]
NAMES[SEM=<(SameReference(citta_name,manas_name) & SameReference(manas_name,vijnana_name))>] -> CITTA[CASE=nom] MANAS[CASE=nom] ANDNAME VIJNANA[CASE=nom] ONE[READING=contextual_reference]
PAIR[SEM=<(HasBasis(consciousness_factors) & HasCondition(consciousness_factors) & HasManner(consciousness_factors) & AssociationModes(consciousness_factors,five))>] -> SUBJECT[CASE=nom,NUM=pl] HAVING[CASE=nom,NUM=pl,CNT=3] ASSOCIATED[CASE=nom,NUM=pl] AND FIVE[CNT=5]
CITTA[CASE=nom] -> 'cittam'
MANAS[CASE=nom] -> 'manaḥ'
ANDNAME -> 'atha'
VIJNANA[CASE=nom] -> 'vijñānam'
ONE[READING=contextual_reference] -> 'ekārtham'
SUBJECT[CASE=nom,NUM=pl] -> 'cittacaitasāḥ'
HAVING[CASE=nom,NUM=pl,CNT=3] -> 'sāśrayālambanākārāḥ'
ASSOCIATED[CASE=nom,NUM=pl] -> 'saṃprayuktāḥ'
AND -> 'ca'
FIVE[CNT=5] -> 'pañcadhā'
```

```nltk-dep
'ekārtham' -> 'cittam' | 'manaḥ' | 'atha' | 'vijñānam'
'cittacaitasāḥ' -> 'sāśrayālambanākārāḥ' | 'saṃprayuktāḥ'
'saṃprayuktāḥ' -> 'ca' | 'pañcadhā'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 5) | `NAMES` | one contextual reference, three designations |
| [5, 10) | `PAIR` | Basis, Condition, manner, and fivefold association |

## 5. Translation

### Literal Translation

> Consciousness, Mind, and Cognition have one meaning. Consciousness and
> mental factors have Basis, Cognitive Condition, and manner, and are
> associated in five ways.
### Bhāṣya-informed study translation

> Consciousness, Mind, and Cognition have one meaning here. Consciousness
> and mental factors have a Basis, a Cognitive Condition, and a manner,
> and are associated through five equalities: Basis, Cognitive Condition,
> manner, time, and individual instance—one consciousness and one of each
> accompanying factor.
## 6. Philosophical Translation

> Contextual common reference preserves different naming roles.
> Association joins distinguishable factors through specified
> equalities; one instance of each does not make all factors one entity.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| citta | consciousness | gathers; or variegated |
| manas | Mind | Basis-role of the same referent in the alternative explanation |
| vijñāna | Cognition | supported Cognition; not Principle |
| ekārtha | one meaning | contextual; not every text |
| āśraya | Basis | the Faculty depended on |
| ālambana | Cognitive Condition | what is apprehended |
| ākāra | manner | how that Cognitive Condition is taken |
| saṃprayoga | association | the five equalities |
| dravya-samatā | equality of instance | one of each; not substance |

What is gathered is not specified. No seed-theory is inserted.

## 8. Logical Determination

**Kārikā, derived.** SameReference relates designations in this naming
context, not unrestricted identity of their functions. The association
model uses distinct consciousness and factor tokens with shared
relational values; individual-instance equality means one of each.

```nltk-sem
common_reference : \a.\b.SameReference(b,a)
five_modes : \x.AssociationModes(x,five)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((SameReference(citta_name,manas_name) & SameReference(manas_name,vijnana_name)) & (HasBasis(consciousness_factors) & HasCondition(consciousness_factors) & HasManner(consciousness_factors) & AssociationModes(consciousness_factors,five)))

# THEORY prose_association
# EXPECT prose_association T
all c f.(Associated(c,f) -> (exists b.(Basis(c,b) & Basis(f,b)) & exists a.(Condition(c,a) & Condition(f,a)) & exists m.(Manner(c,m) & Manner(f,m)) & exists t.(Time(c,t) & Time(f,t)) & OneInstanceEach(c,f)))

# THEORY rejected_associated_factors_are_identical
# EXPECT rejected_associated_factors_are_identical F
all c f.(Associated(c,f) -> c = f)

# THEORY rejected_only_one_factor_accompanies
# EXPECT rejected_only_one_factor_accompanies F
all c f g.((Associated(c,f) & Associated(c,g)) -> f = g)
```

```nltk-valuation
citta_name => consciousness_designation
manas_name => mind_designation
vijnana_name => cognition_designation
consciousness_factors => named_pair
five => count_five
SameReference => {(consciousness_designation,mind_designation),(mind_designation,cognition_designation)}
HasBasis => {named_pair}
HasCondition => {named_pair}
HasManner => {named_pair}
AssociationModes => {(named_pair,count_five)}
EqualityMode => {basis_mode,condition_mode,manner_mode,time_mode,instance_mode}
Associated => {(consciousness_token,feeling_token),(consciousness_token,attention_token)}
Basis => {(consciousness_token,shared_faculty),(feeling_token,shared_faculty),(attention_token,shared_faculty)}
Condition => {(consciousness_token,shared_condition),(feeling_token,shared_condition),(attention_token,shared_condition)}
Manner => {(consciousness_token,shared_manner),(feeling_token,shared_manner),(attention_token,shared_manner)}
Time => {(consciousness_token,shared_time),(feeling_token,shared_time),(attention_token,shared_time)}
OneInstanceEach => {(consciousness_token,feeling_token),(consciousness_token,attention_token)}
InstanceOf => {(consciousness_token,consciousness_kind),(feeling_token,feeling_kind),(attention_token,attention_kind)}
```

The two factors illustrate association; they are not an exhaustive
inventory replacing the universal ten. Tests check five modes,
one distinct token per represented kind, and each shared relation.
The equalities do not themselves resolve the previously disputed
attention/equanimity relation or examination co-presence.

## 9. Interpretive Note

**Translation note.** The commentary gives the five relations as equality
of Basis, Cognitive Condition, manner, time, and instance, illustrated
by one consciousness and one of each factor. Manner remains distinct
from Basis and Cognitive Condition. Its fivefold account does not resolve the previously noted questions about shared support or simultaneous occurrence.

The section closes. Distributions and particular distinctions give way to the names. Others are not a named school. The questions introduce explanations, not a developed objection.

Basis is not Cognitive Condition. Manner is not established as a
separate image or a theory of representation. Having manner is
the local function.

Fivefold association does not settle the shared Cognitive Condition
of attention and equanimity, deferred at 2.25. It does not refute the alternative on vitarka and vicāra at 2.33. Level-attribution is still not moment-co-presence. Repeating the relation does not supply the missing explanation.

In the Organon reading, Cognition joins and governs Perception and
Conception and guides the reading of Dharma Base, remaining distinct
in role from consciousness and Mind. The source's contextual naming
claim is retained, not rewritten as three unrelated entities; neither
does it license indiscriminate substitution in every argument.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_34
    a vak:Karika ;
    rdfs:label "VAK 2.34" ;
    vak:hasTopic vak:FivefoldAssociation ;
    vak:belongsTo vak:Indriyanirdesa .

vak:CittaManasVijnana vak:oneReferentHere true .
vak:FiveEqualities vak:includes vak:Basis, vak:CognitiveCondition,
    vak:Manner, vak:Time, vak:Instance .

organon:VAK_2_34_Interpretation
    organon:distinguishes vak:ContextualReference, vak:NamingRole,
        vak:SharedRelation, vak:FactorIdentity .
```
