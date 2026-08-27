# VAK_1.30

## 1. Sanskrit (Devanāgarī)

> त्रिधान्ये कामधात्वाप्ताः सर्वे रूपे चतुर्दश ।
>
> विना गन्धरसघ्राणजिह्वाविज्ञानधातुभिः ॥ १.३० ॥

## 2. Sanskrit (IAST)

> tridhānye kāmadhātvāptāḥ sarve rūpe caturdaśa /
>
> vinā gandharasaghrāṇajihvāvijñānadhātubhiḥ // 1.30 //

## 3. Padaccheda

```text
tridhānye             → tridhā anye
kāmadhātvāptāḥ        → kāma-dhātu-āptāḥ
rūpe                   → rūpa-dhātau
gandharasa             → gandha-rasa
ghrāṇajihvāvijñāna-   → ghrāṇa-vijñāna + jihvā-vijñāna
dhātubhiḥ              → dhātubhiḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| tridhā | distributive adverb | in three ways; with respect to the three realms |
| anye | nominative masculine plural | the remaining Domains, after the invariably indeterminate eight of 1.29 |
| kāma-dhātu-āptāḥ | nominative masculine plural compound | belonging to or connected with the Desire Realm |
| sarve | nominative masculine plural | all eighteen Domains |
| rūpe | locative masculine singular, elliptical for `rūpadhātau` | in the Form Realm |
| caturdaśa | numeral | fourteen |
| vinā | indeclinable governing instrumental | without, excluding |
| gandha | compound member | smell-domain |
| rasa | compound member | taste-domain |
| ghrāṇa-vijñāna-dhātu | instrumental plural compound member | olfactory-consciousness Domain |
| jihvā-vijñāna-dhātu | instrumental plural compound member | gustatory-consciousness Domain |

The long closing compound excludes four—not six—Domains. `Ghrāṇa` and
`jihvā` qualify `vijñāna`: the olfactory- and gustatory-consciousness
Domains are absent, but the nose- and tongue-faculty Domains themselves
remain.

## 4. Grammar

`Tridhā anye` begins the classification of the remaining Domains according
to their possible membership in the three realms:

```text
kāmadhātu
    Desire Realm

rūpadhātu
    Form Realm

ārūpyadhātu
    Formless Realm
```

The verse completes the first two distributions; VAK 1.31 supplies the
Formless Realm.

The Bhāṣya glosses `āpta` precisely:

```text
āpta
    = aviyukta
    = pratisaṃyukta
    = not separated from and connected with a realm
```

It therefore marks realm-membership, not merely spatial presence.

The Desire Realm possesses all eighteen Domains. The Form Realm possesses
fourteen:

```text
18
− smell-domain
− taste-domain
− olfactory-consciousness Domain
− gustatory-consciousness Domain
= 14
```

Smell and taste are absent because their enjoyment depends upon gross
ingested nourishment (`kavaḍīkārāhāra`), from which beings born in the Form
Realm are detached. Their two consciousnesses are absent because their
object-supports are absent (`ālambanābhāva`).

## 5. Translation

### Close syntactic construe

> The others are threefold [according to realm]. All [eighteen] belong to the Desire Realm. In the Form Realm there are fourteen, excluding smell, taste, and the olfactory- and gustatory-consciousness Domains.

### Bhāṣya-informed translation

> All eighteen Domains are connected with the Desire Realm. Fourteen belong to the Form Realm: smell and taste are absent because beings there are detached from gross ingested nourishment, and the corresponding olfactory and gustatory consciousnesses are absent because their objects are unavailable. The nose and tongue faculties themselves remain.

The Bhāṣya's debate is needed to prevent the closing compound from being
misread as excluding the faculty-Domains along with their consciousnesses.

## 6. Philosophical Translation

> A realm is a determinate configuration of capacities, objects, and acts of consciousness. Desire sustains the complete eighteenfold configuration. Form preserves fourteen lineages while excluding the smell-and-taste object complex and the cognitions that require it. The disappearance of an object removes its corresponding cognition without necessarily removing the embodied faculty associated with it.

Organon rendering:

> A Dharma lineage belongs to a realm when that realm can support its cause, object, function, and mode of attachment. Realm is therefore not an external container into which finished Domains are placed; it is the systematic configuration under which particular Domain-capabilities can or cannot be actualized.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| tridhā | threefold by realm | distribution across Desire, Form, and Formless Realms |
| kāmadhātu | Desire Realm | configuration containing all eighteen Domains |
| rūpadhātu | Form Realm | refined embodied configuration containing fourteen Domains |
| āpta | belonging to / connected with | non-separation and causal-functional connection, not mere location |
| gandhadhātu | smell-domain | absent from the Form Realm |
| rasadhātu | taste-domain | absent from the Form Realm |
| ghrāṇavijñānadhātu | olfactory-consciousness Domain | absent because its object is absent |
| jihvāvijñānadhātu | gustatory-consciousness Domain | absent because its object is absent |
| kavaḍīkārāhāra | morsel-made food / gross ingested nourishment | function explaining the exclusion of smell and taste |
| ālambanābhāva | absence of object-support | immediate reason the corresponding consciousness cannot arise |
| indriyāśraya | support of a faculty | one reason tangible objects remain in the Form Realm |
| prasrabdhi | meditative pliancy | invoked by an alternative account of the tangible there |
| ātmabhāvamukha | through one's embodied existence | manner in which attachment to internal faculties can remain |

## 8. Logical Determination

The realm configurations are:

```text
DomainsOf(Kamadhatu)
    = AllEighteenDomains

DomainsOf(Rupadhatu)
    = AllEighteenDomains
      − {SmellDhatu,
         TasteDhatu,
         OlfactoryConsciousnessDhatu,
         GustatoryConsciousnessDhatu}
```

The object-consciousness dependency is:

```text
AbsentIn(SmellObject, Rupadhatu)
    → NoAvailableAlambana(OlfactoryConsciousness, Rupadhatu)
    → AbsentIn(OlfactoryConsciousness, Rupadhatu)

AbsentIn(TasteObject, Rupadhatu)
    → NoAvailableAlambana(GustatoryConsciousness, Rupadhatu)
    → AbsentIn(GustatoryConsciousness, Rupadhatu)
```

But object-absence does not automatically eliminate the corresponding
faculty:

```text
AbsentIn(SmellObject, Rupadhatu)
    ↛ AbsentIn(NoseFaculty, Rupadhatu)

AbsentIn(TasteObject, Rupadhatu)
    ↛ AbsentIn(TongueFaculty, Rupadhatu)
```

The Bhāṣya's accepted explanation retains internal attachment through
embodied existence while excluding attachment through those external
objects:

```text
AttachmentThroughEmbodiedBasis(Faculty)
    may persist without
AttachmentThroughExternalObject(FacultyObject)
```

The generalized Smart-Domain rule is:

```text
BelongsToRealm(x, r)
    ↔ CompatibleWith(x,
        CausesOf(r),
        AvailableObjectsOf(r),
        FunctionsOf(r),
        ModesOfAttachmentOf(r))
```

## 9. Interpretive Note

VAK 1.29 typed the individual Domains by visibility, resistance, and ethical
status. VAK 1.30 now types their membership in larger configurations. This
is the first indication that a realm is not simply a cosmic location. It is
a systematic compatibility-structure governing which Domain lineages can
be supported together.

The Form Realm is not merely the Desire Realm with four objects deleted.
The exclusions follow determinate relations:

```text
detachment from ingestion
    → smell and taste lose their function

absence of smell and taste
    → their consciousnesses lack objects

continued embodiment
    → tangible support remains
```

The long Bhāṣya debate concerning nose and tongue is philosophically useful.
It prevents faculty, object, and consciousness from being collapsed into a
single sensory atom. Their relations are lawful, but their presence is not
perfectly coextensive. An object may be absent and its consciousness
therefore impossible while the internal faculty lineage remains as part of
the embodied basis.

For our Basis-of-the-System reading, this adds realm compatibility to the
Smart Domain:

```text
Smart Domain
    = intrinsic predicates
    + lawful relations
    + configuration compatibility
```

Calling the eighteen Domains “lineages of Dharma” is especially productive
here. A lineage can persist through a changed configuration without every
one of its familiar relations being activated. The Form Realm preserves
the nose- and tongue-faculty lineages while withholding the gross object and
consciousness relations associated with ingestion.

The Hegelian comparison belongs to our Organon reconstruction: the Domain
behaves less like an inert element than a Concept whose determinations are
displayed through its relations and possible configurations. Vasubandhu's
explicit claim remains the Abhidharma distribution of the eighteen Domains
across realms.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_30
    a vak:Karika ;
    rdfs:label "VAK 1.30" ;
    vak:hasTopic vak:RealmCompatibilityOfDomains ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Kamadhatu
    a vak:RealmConfiguration ;
    vak:supports vak:AllEighteenDomains .

vak:Rupadhatu
    a vak:RealmConfiguration ;
    vak:supportsDomainCount 14 ;
    vak:excludes vak:SmellDhatu,
        vak:TasteDhatu,
        vak:OlfactoryConsciousnessDhatu,
        vak:GustatoryConsciousnessDhatu .

vak:OlfactoryConsciousnessDhatu
    vak:requiresObject vak:SmellDhatu .

vak:GustatoryConsciousnessDhatu
    vak:requiresObject vak:TasteDhatu .

vak:NoseFacultyDhatu
    vak:persistsIn vak:Rupadhatu .

vak:TongueFacultyDhatu
    vak:persistsIn vak:Rupadhatu .

vak:RealmCompatibleSmartDomain
    a vak:OrganonInterpretiveClass ;
    vak:requiresCompatibilityWith vak:RealmCause,
        vak:RealmObject,
        vak:RealmFunction,
        vak:RealmAttachmentMode .
```
