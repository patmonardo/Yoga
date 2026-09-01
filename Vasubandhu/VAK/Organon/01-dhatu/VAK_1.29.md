# VAK_1.29

## 1. Sanskrit (Devanāgarī)

> सनिदर्शन एकोऽत्र रूपं सप्रतिघा दश ।
>
> रूपिणोऽव्याकृता अष्टौ त एवारूपशब्दकाः ॥ १.२९ ॥

## 2. Sanskrit (IAST)

> sanidarśana eko 'tra rūpaṃ sapratighā daśa /
>
> rūpiṇo 'vyākṛtā aṣṭau ta evārūpaśabdakāḥ // 1.29 //

## 3. Lexical Analysis

```text
sanidarśanaḥ       → sa-nidarśanaḥ
eko 'tra            → ekaḥ atra
sapratighāḥ         → sa-pratighāḥ
rūpiṇaḥ             → rūpiṇaḥ
'vyākṛtāḥ           → avyākṛtāḥ
ta eva              → te eva
arūpaśabdakāḥ       → a-rūpa-śabdakāḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| sa-nidarśanaḥ | nominative masculine singular adjective | visible, spatially demonstrable |
| ekaḥ | nominative masculine singular | one alone |
| atra | adverb | here, among these eighteen Domains |
| rūpam | nominative neuter singular | visible form; supplies the identity of the one visible Domain |
| sa-pratighāḥ | nominative masculine plural adjective | resistant, obstructive |
| daśa | numeral | ten |
| rūpiṇaḥ | nominative masculine plural adjective | material, possessing form |
| avyākṛtāḥ | nominative masculine plural adjective | ethically indeterminate; neither wholesome nor unwholesome |
| aṣṭau | nominative masculine plural numeral | eight |
| te eva | demonstrative plus emphatic particle | those very same [ten material Domains] |
| a-rūpa-śabdakāḥ | nominative masculine plural compound | with rūpa and śabda excluded |

The final compound is exceptionally easy to misread. It does **not** mean
that the eight are “non-material.” The Bhāṣya explicitly identifies them as
the previously mentioned ten material Domains after excluding the
visible-form Domain (`rūpa`) and sound Domain (`śabda`).

## 4. Grammar

The verse answers three successive questions about the eighteen Domains:

```text
How many are visible?
    one: visible form

How many are resistant?
    ten: the material Domains

How many are invariably ethically indeterminate?
    eight: those ten minus visible form and sound
```

The opening adjective is masculine because it agrees with understood
`dhātuḥ`; neuter `rūpam` names that Domain:

```text
sanidarśanaḥ ekaḥ [dhātuḥ] atra — rūpam
    one Domain here is visible—visible form
```

Likewise, `rūpiṇaḥ` supplies an explanation of the ten resistant Domains:
the five sensory faculties and five sensory objects are material. The
Bhāṣya nevertheless warns that `pratigha` has three distinct senses:

```text
āvaraṇa-pratighāta
    material resistance through mutual spatial obstruction

viṣaya-pratighāta
    limitation by the field within which a faculty can operate

ālambana-pratighāta
    limitation by the cognitive object apprehended by mind and mental factors
```

Only the first sense grounds the Kārikā's count of ten. They are
`sapratigha` here because material Domains prevent one another from arising
in the same place.

The eight indeterminate Domains are:

```text
five sensory faculties
+ smell
+ taste
+ tangible object
```

Visible form and sound are excluded because bodily and verbal actions
produced by wholesome or unwholesome mind can give them corresponding
ethical determination.

## 5. Translation

### Close syntactic construe

> Among these, one is visible: visible form. Ten are resistant—the material Domains. Eight are ethically indeterminate: those same [ten] with visible form and sound excluded.

### Bhāṣya-informed translation

> Of the eighteen Domains, visible form alone is spatially demonstrable. The five material faculties and five sensory objects are resistant because they mutually obstruct one another. Of these ten, eight—the five faculties together with smell, taste, and tangible objects—are invariably ethically indeterminate; visible form and sound may instead acquire wholesome or unwholesome determination through bodily and verbal action.

The second rendering keeps the Bhāṣya's three explanations distinct:
visibility concerns demonstrability, resistance here concerns material
obstruction, and indeterminacy concerns ethical status.

## 6. Philosophical Translation

> A Domain does not receive one undifferentiate description. Visible form alone can be pointed out as “here” or “there”; ten Domains possess material resistance; only eight of those are invariably neutral with respect to wholesome and unwholesome determination. Manifestation, materiality, resistance, and ethical status are distinct dimensions of the same system.

Organon rendering:

> The Naive Domain becomes a Smart Domain when its predicates are explicitly typed. What can be displayed is not identical with what can obstruct; what can obstruct is not thereby ethically neutral; and a common material basis does not erase the different determinations of its members. Rational classification begins by preventing one property from silently standing in for another.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| sanidarśana | visible / spatially demonstrable | capable of being pointed out as here or there |
| anidarśana | non-visible / non-demonstrable | complementary status of the other seventeen Domains |
| rūpin | material / possessing form | applies to the ten material Domains |
| pratigha / pratighāta | resistance / impediment | general term differentiated into three relations |
| āvaraṇapratighāta | obstructive resistance | prevention of another material thing's arising in the same place |
| viṣayapratighāta | limitation by object-field | restriction of a faculty to the field of its possible activity |
| ālambanapratighāta | limitation by cognitive object | determination of mind and mental factors by what they apprehend |
| viṣaya | functional object-field | that within which a faculty exercises its activity |
| ālambana | apprehended cognitive object | that which mind and mental factors take as object-support |
| avyākṛta | ethically indeterminate | not specified as wholesome or unwholesome |
| arūpaśabdaka | excluding visible form and sound | Bhāṣya-resolved selection of eight from the ten material Domains |

`Viṣaya` and `ālambana` must not be collapsed. A functional range and an
apprehended cognitive object can overlap, but they state different
relations.

## 8. Logical Determination

The first Smart-Domain specification establishes independent predicate
axes:

```text
Visibility(x)
Materiality(x)
ObstructiveResistance(x)
FunctionalObjectRange(x)
CognitiveObjectRelation(x)
EthicalStatus(x)
```

Their extensions are:

```text
Visible(x)
    ↔ x = RupaDhatu

MaterialAndObstructivelyResistant(x)
    ↔ x ∈ FiveSenseFacultyDhatus
       ∪ FiveSensoryObjectDhatus

InvariablyAvyakrta(x)
    ↔ x ∈ FiveSenseFacultyDhatus
       ∪ {SmellDhatu, TasteDhatu, TangibleDhatu}
```

The compound rule is:

```text
EightAvyakrtaMaterialDhatus
    = TenMaterialDhatus
      − {RupaDhatu, SabdaDhatu}
```

The Bhāṣya's four-cornered analysis proves that forms of resistance cannot
be conflated:

```text
ObjectFieldLimited ∧ ¬SpatiallyObstructive
    → seven citta Domains and associated dharmadhātu

SpatiallyObstructive ∧ ¬ObjectFieldLimited
    → five sensory object-Domains

ObjectFieldLimited ∧ SpatiallyObstructive
    → five sensory faculty-Domains

¬ObjectFieldLimited ∧ ¬SpatiallyObstructive
    → unassociated remainder of dharmadhātu
```

Thus:

```text
SharedPredicate(x, y, Material)
    ↛ SharedPredicate(x, y, EthicalStatus)
```

## 9. Interpretive Note

VAK 1.29 begins the Basis of the System by enriching the eighteen Domains
with independently queryable determinations. The earlier verses established
what the Domains are and how additional scriptural classifications are
resolved into them. The present sequence asks what can validly be predicated
of each established Domain.

The first distinction is already philosophically exact. Only visible form
is `sanidarśana`: it alone can be indicated as “this here” or “that there.”
This is not a claim that the remaining seventeen Domains are unknowable.
Visibility is one mode of manifestation, not the universal criterion of
reality.

The analysis of resistance adds a second discipline. Material resistance,
functional limitation, and cognitive object-dependence are three different
relations. The Bhāṣya's four-cornered analysis acts like a type-checker: it
constructs cases possessing either relation, both relations, or neither,
thereby proving that the predicates are not synonyms.

The ethical determination adds a third layer. Materiality does not by itself
decide whether a Domain is wholesome, unwholesome, or indeterminate. The
five faculties, smell, taste, and tangible objects are invariably
indeterminate. Visible form and sound are removed from that set because
bodily and verbal action can be produced by ethically determined mind.

In our provisional SDK image:

```text
Naive Domain
    = named member of the eighteenfold system

Smart Domain
    = member whose independent properties and relations are explicitly typed
```

This is not Vasubandhu's language, but it accurately marks the work now
being performed. The system is acquiring a basis for later applications:
queries about realm, cognition, causation, embodiment, and liberation will
operate over Domains whose predicates can no longer be vaguely exchanged.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_29
    a vak:Karika ;
    rdfs:label "VAK 1.29" ;
    vak:hasTopic vak:IndependentDomainPredicates ;
    vak:belongsTo vak:Dhatunirdesa .

vak:RupaDhatu
    a vak:VisibleDomain,
        vak:MaterialDomain,
        vak:ObstructivelyResistantDomain .

vak:TenMaterialDomains
    a vak:DomainSet ;
    vak:hasMemberSet vak:FiveSenseFacultyDomains,
        vak:FiveSensoryObjectDomains ;
    vak:hasProperty vak:ObstructiveResistance .

vak:EightIndeterminateMaterialDomains
    a vak:DomainSet ;
    vak:derivedFrom vak:TenMaterialDomains ;
    vak:excludes vak:RupaDhatu,
        vak:SabdaDhatu ;
    vak:hasEthicalStatus vak:Avyakrta .

vak:ObstructiveResistance
    vak:distinctFrom vak:ObjectFieldLimitation,
        vak:CognitiveObjectLimitation .

vak:SmartDomain
    a vak:OrganonInterpretiveClass ;
    vak:requiresExplicitTypingOf vak:Visibility,
        vak:Materiality,
        vak:Resistance,
        vak:EthicalStatus .
```
