# VAK_1.24

## 1. Sanskrit (Devanāgarī)

> विशेषणार्थं प्राधान्याद्बहुधर्माग्रसंग्रहात् ।
>
> एकमायतनं रूपमेकं धर्माख्यमुच्यते ॥ १.२४ ॥

## 2. Sanskrit (IAST)

> viśeṣaṇārthaṃ prādhānyād bahudharmāgrasaṃgrahāt /
>
> ekam āyatanaṃ rūpam ekaṃ dharmākhyam ucyate // 1.24 //

## 3. Lexical Analysis

```text
viśeṣaṇārtham             → viśeṣaṇa-artham
prādhānyāt                → prādhānyāt
bahudharmāgrasaṃgrahāt    → bahu-dharma-agra-saṃgrahāt
ekam āyatanam             → ekam āyatanam
dharmākhyam               → dharma-ākhyam
```

| Form | Morphology | Lexical force here |
|---|---|---|
| viśeṣaṇa-artham | accusative neuter singular used adverbially | for the sake of specification or differentiation |
| prādhānyāt | ablative neuter singular | because of predominance or prominence |
| bahu-dharma | compound member | many heterogeneous dharmas |
| agra | compound member | foremost; the Bhāṣya identifies this as nirvāṇa |
| saṃgrahāt | ablative masculine singular | because of gathering or inclusion |
| ekam | nominative neuter singular | one; agrees with `āyatanam` |
| āyatanam | nominative neuter singular | sphere, relational access-field |
| rūpam | nominative neuter singular | visible form, the rūpa-āyatana |
| dharma-ākhyam | nominative neuter singular | bearing the name “dharma” |
| ucyate | third-person singular present passive | is called |

The Bhāṣya parses the dense compound as two linked inclusions:

```text
bahūnāṃ dharmāṇāṃ saṃgrahaḥ
    gathering of many dharmas

agrasya nirvāṇa-dharmasya saṃgrahaḥ
    gathering of the foremost Dharma, nirvāṇa
```

It does not describe all the included dharmas as “foremost.”

## 4. Grammar

The verse answers two parallel naming problems:

```text
ten āyatanas belong to rūpa-skandha
    but only one is named rūpa-āyatana

all entities have dharma-nature
    but only one is named dharma-āyatana
```

`Viśeṣaṇa-artham` supplies the shared purpose. The special names ensure that
each of the ten material āyatanas is understood individually through the
relation of object and object-possessor (`viṣaya-viṣayin`), rather than all
ten being mistaken for one collective material sphere.

The material faculties have already received the specific names eye, ear,
nose, tongue, and body. The remaining material object-field therefore keeps
the unqualified name `rūpa`.

`Prādhānyāt` supplies a second reason for that name. Visible form is
predominant because it is resistant (`sapratigha`), visible and spatially
indicable (`sanidarśana`), and commonly recognized as rūpa in ordinary
language.

The last causal compound applies especially to dharma-āyatana:

```text
because it includes many dharmas
    +
because it alone among the āyatanas includes nirvāṇa,
the foremost Dharma
```

The singular `ucyate` governs the compact paired construction: one sphere is
called rūpa, and one is called by the name dharma.

## 5. Translation

### Close syntactic construe

> For the sake of specification, because of predominance, and because of gathering many dharmas together with the foremost Dharma, one sphere is called rūpa and one is called by the name dharma.

### Bhāṣya-informed translation

> One material sphere receives the unqualified name rūpa in order to distinguish the ten material spheres individually and because visible form is phenomenally predominant. One sphere receives the general name dharma because it gathers many heterogeneous dharmas and uniquely includes the foremost Dharma, nirvāṇa.

The close translation preserves the compressed distribution of reasons. The
second makes explicit which reasons the Bhāṣya assigns to each technical
name.

## 6. Philosophical Translation

> A single name may mark unity for different reasons. Visible form names one sphere through phenomenal prominence: it is resistant, demonstrable, and ordinarily recognized. Dharma names one sphere through principial inclusion: it gathers heterogeneous mental, subtle-material, and unconditioned determinations, including nirvāṇa.

Organon rendering:

> The Triadic system distinguishes a field named by dominant appearance from a field named by comprehensive scope. Rūpa is prominent because it stands outwardly before cognition; Dharma is comprehensive because it includes determinations that cannot be reduced to outward presentation.

Technical naming therefore does not merely attach labels to preclassified
things. It displays the reason a domain is singled out within the completed
system.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| viśeṣaṇa | specification / differentiation | reason one member receives a technically distinctive name |
| viṣaya | object-domain | object-side of an individually established āyatana |
| viṣayin | object-possessor / faculty-side | pole correlated with an object-domain |
| prādhānya | predominance | phenomenal prominence of visible form |
| rūpa-āyatana | visible-form sphere | residual material object-field after the faculties are separately named |
| sapratigha | resistant / obstructive | subject to impact or material interference |
| sanidarśana | visible / demonstrable | spatially indicable as this, here, or there |
| dharma-āyatana | Dharma-sphere | general mental object-field containing heterogeneous dharmas |
| saṃgraha | gathering / inclusion | reason for the comprehensive name dharma |
| agra-dharma | foremost Dharma | nirvāṇa, included in dharma-āyatana alone |
| māṃsa-cakṣus | fleshly eye | one of three ranges in the alternative explanation |
| divya-cakṣus | divine eye | second eye in the alternative explanation |
| ārya-prajñā-cakṣus | noble wisdom-eye | third eye in the alternative explanation |

## 8. Logical Determination

The problem distinguishes class-membership from privileged naming:

```text
MemberOf(x, RupaSkandha)
    ↛ Named(x, RupaAyatana)

HasDharmaNature(x)
    ↛ Named(x, DharmaAyatana)
```

Each material āyatana is individually relational:

```text
Ayatana(a)
    → EstablishedAs(a, FacultyPole | ObjectPole)
    → DistinctRelationalField(a)
```

The naming rule for rūpa is:

```text
RemainingMaterialObjectField(x)
∧ Resistant(x)
∧ VisibleAndIndicable(x)
∧ PredominantlyCalledRupa(x)
    → Named(x, RupaAyatana)
```

The naming rule for Dharma is:

```text
Includes(x, ManyHeterogeneousDharmas)
∧ Includes(x, Nirvana)
    → Named(x, DharmaAyatana)
```

The two unities have different grounds:

```text
RupaAyatanaUnity
    → PhenomenalPredominance

DharmaAyatanaUnity
    → ComprehensiveInclusion
```

The alternative teachers add three proposed grounds for rūpa's singular
designation: twenty varieties, grossness, and being the object-range of the
fleshly, divine, and noble wisdom eyes. These remain reported alternatives,
not Vasubandhu's unmarked conclusion.

## 9. Interpretive Note

VAK 1.24 opens the Problems of the Triadic Abhidharma with a problem of
technical naming. If the ten material spheres all belong to rūpa, why does
only visible form bear the class-name? If everything classified is a dharma,
why does only one sphere bear that universal name? The answer shows that
naming follows systematic function rather than extension alone.

This guards against two common flattenings:

```text
rūpa
    ≠ every material factor under one undifferentiated label

dharma-āyatana
    ≠ an accidental remainder after the five sensory objects
```

Visible form receives its name through outward prominence. Dharma-āyatana
receives its name because its content crosses ordinary ontological divisions:
feeling, recognition, formations, avijñapti, space, and the two cessations.
Its unity cannot be sensible likeness. It is unity through principial
inclusion.

The inclusion of nirvāṇa is decisive. The Dharma-sphere does not merely
collect whatever the sensory system failed to classify. It alone among the
āyatanas includes the foremost Dharma. Its apparent residuality is therefore
the external appearance of its greater systematic reach.

For the Organon, this contrast makes the inward movement visible:

```text
rūpa-āyatana
    = domain named from what appears predominantly

dharma-āyatana
    = domain named from what it can comprehend
```

We should not yet identify dharma-āyatana with the whole Buddha Mind system;
it remains one sphere within the twelvefold arrangement. But its unity
demonstrates that the most comprehensive domain cannot be modeled as a heap
of outward elements.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_24
    a vak:Karika ;
    rdfs:label "VAK 1.24" ;
    vak:hasTopic vak:TechnicalNamingOfRupaAndDharmaAyatanas ;
    vak:belongsTo vak:Dhatunirdesa .

vak:RupaAyatana
    a vak:MaterialObjectSphere ;
    vak:namedBy vak:Specification , vak:PhenomenalPredominance ;
    vak:hasCharacteristic vak:Resistance , vak:Visibility .

vak:DharmaAyatana
    a vak:ComprehensiveMentalObjectSphere ;
    vak:namedBy vak:InclusiveScope ;
    vak:includes vak:ManyHeterogeneousDharmas , vak:Nirvana .

vak:Nirvana
    a vak:ForemostDharma ;
    vak:includedIn vak:DharmaAyatana .

vak:ClassMembership
    vak:distinctFrom vak:PrivilegedTechnicalNaming .
```
