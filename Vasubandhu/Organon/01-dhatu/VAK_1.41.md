# VAK_1.41

## 1. Sanskrit (Devanāgarī)

> चक्षुश्च धर्मधातोश्च प्रदेशौ दृष्टिरष्टधा ।
>
> पञ्चविज्ञानसहजा धीर्न दृष्टिरतीरणात् ॥ १.४१ ॥

## 2. Sanskrit (IAST)

> cakṣuś ca dharmadhātoś ca pradeśau dṛṣṭir aṣṭadhā /
>
> pañcavijñānasahajā dhīr na dṛṣṭir atīraṇāt // 1.41 //

## 3. Lexical Analysis

```text
cakṣuś ca              → cakṣuḥ ca
dharmadhātoś ca        → dharma-dhātoḥ ca
pradeśau               → pradeśau
dṛṣṭir aṣṭadhā         → dṛṣṭiḥ aṣṭadhā
pañcavijñānasahajā     → pañca-vijñāna-sahajā
dhīr na                → dhīḥ na
atīraṇāt               → a-tīraṇāt
```

| Form | Morphology | Lexical force here |
|---|---|---|
| cakṣuḥ | nominative neuter singular | eye-faculty Domain, called seeing through visual disclosure |
| dharma-dhātoḥ | genitive masculine singular | of the Dharma-domain |
| pradeśau | nominative masculine dual | the relevant members or portions counted as seeing/view |
| dṛṣṭiḥ | nominative feminine singular | seeing when applied to eye; ascertainative view when applied to prajñā |
| aṣṭadhā | adverb | in eight modes within the Dharma-domain portion |
| pañca-vijñāna-sahajā | nominative feminine singular compound | co-arisen with the five sensory knowledges |
| dhīḥ | nominative feminine singular | discernment; glossed by the Bhāṣya as prajñā |
| na dṛṣṭiḥ | negative predicate | is not ascertainative view |
| a-tīraṇāt | ablative masculine singular | because of absence of decisive ascertainment |

The compressed first line is best resolved through the Bhāṣya: the eye
counts as seeing, and an eightfold portion of the Dharma-domain counts as
view. The whole Dharma-domain is not `dṛṣṭi`.

## 4. Grammar

The term `dṛṣṭi` carries two coordinated but non-identical functions:

```text
cakṣus as dṛṣṭi
    → visual disclosure or examination of visible form

Dharma-domain prajñā as dṛṣṭi
    → attentive ascertainment of dharmas
```

The eightfold Dharma-domain portion consists of:

```text
five afflicted views beginning with satkāyadṛṣṭi
+ worldly right view
+ trainee's view
+ adept's view
```

Worldly right view is wholesome but still outflow-bound prajñā associated
with mental knowledge. Trainee and adept views are outflow-free and are
distinguished by the path-status of their bearer.

The second line excludes the `dhī` or prajñā arising with the five sensory
knowledges:

```text
pañca-vijñāna-sahajā dhīḥ
    discernment co-arisen with sensory knowledge

na dṛṣṭiḥ
    is not ascertainative view

atīraṇāt
    because it does not decisively ascertain
```

The Bhāṣya explains view as `santīrikā`, ascertainative, because it proceeds
through attentive examination (`upadhyāna`). Not every prajñā therefore
qualifies as view; the predicate follows function rather than the mere
presence of a cognitive factor.

## 5. Translation

### Close syntactic construe

> The eye and an eightfold portion of the Dharma-domain are seeing or view. The discernment co-arisen with the five sensory knowledges is not view, because it does not ascertain.

### Bhāṣya-informed translation

> The eye counts as seeing because it visually discloses forms. Eight kinds of prajñā within the Dharma-domain count as view: five afflicted views, worldly right view, the trainee's view, and the adept's view. Discernment accompanying sensory knowledge is not view because it does not attentively examine and decisively settle its object.

The two English renderings “seeing” and “view” preserve the functional
difference carried by the single Sanskrit term `dṛṣṭi`.

## 6. Philosophical Translation

> Disclosure and ascertainment are distinct powers of seeing. The eye opens visible form without judging its truth. Sensory discernment differentiates within that presentation but does not yet settle its object. View arises only where prajñā performs attentive and decisive ascertainment within the Dharma-domain.

Organon rendering:

> The Agent's visual capacity, sensory discrimination, and ascertainative judgment must not be collapsed. Appearance is disclosed through a faculty; differentiation accompanies knowledge; determination becomes view only through a further act that examines and settles. The Kośa technē therefore gives the Agent a graded science of seeing.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| dṛṣṭi | seeing / view | visual disclosure in the eye; ascertainative determination in the Dharma-domain |
| pradeśa | portion / member | restricts view-status to an eightfold part of the Dharma-domain |
| aṣṭaprakāra-dṛṣṭi | eightfold view | five afflicted views and three forms of right view |
| satkāyadṛṣṭi | view of a real personality-complex | first of the five afflicted views; full treatment deferred |
| laukikī samyagdṛṣṭi | worldly right view | wholesome, outflow-bound prajñā associated with mental knowledge |
| śaikṣī dṛṣṭi | trainee's view | outflow-free view belonging to one still in training |
| aśaikṣī dṛṣṭi | adept's view | outflow-free view belonging to one beyond training |
| dhī | discernment | glossed here through prajñā |
| prajñā | discriminative discernment | becomes view only when it performs ascertainment |
| tīraṇa | ascertainment | decisive determination after examination |
| santīrikā | ascertainative | functional characterization of view |
| upadhyāna | attentive examination | operation through which ascertainment proceeds |
| rūpālocana | visual disclosure or examination of form | sense in which the eye is called seeing |

## 8. Logical Determination

The term `dṛṣṭi` is functionally overloaded:

```text
EyeFaculty(x)
∧ VisuallyDiscloses(x, VisibleForm)
    → Seeing(x)

Prajna(x)
∧ MemberOf(x, EightfoldDharmaDomainPortion)
∧ AttentivelyAscertains(x, Dharma)
    → View(x)
```

The eightfold set is:

```text
EightfoldView
    = FiveAfflictedViews
      ∪ {WorldlyRightView,
         TraineeView,
         AdeptView}
```

Worldly correctness and outflow-freedom are independent:

```text
WorldlyRightView
    → Wholesome
    ∧ Correct
    ∧ Sasrava

TraineeView ∨ AdeptView
    → Anasrava
```

Sensory discernment fails the functional criterion:

```text
PrajnaCoarisenWithSensoryKnowledge(x)
    → Discriminates(x)
    ∧ ¬DecisivelyAscertains(x)
    → ¬View(x)
```

Therefore:

```text
Prajna(x)
    ↛ View(x)

SensoryDiscrimination(x)
    ↛ Ascertainment(x)

VisualDisclosure(x)
    ≠ AscertainativeView(x)
```

## 9. Interpretive Note

VAK 1.40 classified what is abandoned through seeing. VAK 1.41 now prevents
“seeing” from remaining an unanalyzed metaphor. Yet it does not reduce the
term to one operation. The eye sees by disclosing visible form; prajñā is
view when it attentively ascertains dharmas.

The resulting cognitive gradation is:

```text
visual disclosure
    → sensible form appears

sensory prajñā
    → differentiation accompanies the presentation

ascertainative dṛṣṭi
    → attentive determination settles a Dharma-object
```

This extends 1.32–1.33. Sensory knowledge is neither blank nor fully
ascertainative. It possesses cognitive articulation, but the power to settle
an object as determined belongs to a further mental operation.

The three forms of right view are also instructive. Correct determination
need not already be outflow-free. Worldly right view is wholesome and
correct while remaining `sāsrava`. Trainee and adept views are `anāsrava`.
Correctness, purity, and path-status are therefore independently typed.

The cloud, clear sky, night, and day analogy describes different conditions
under which the same Dharma-field is disclosed. It does not establish that
the object is produced by the clarity or obscurity of the view. The Kośa
technē here classifies modes of cognitive access, not the final metaphysics
of their object.

For the Principle of the Agent, 1.41 adds a graded seeing-capacity:

```text
faculty disclosure
    ≠ sensory discernment
    ≠ decisive ascertainment
```

This is strong Agent science. It should remain subordinate to our Yoga and
should not be inflated into a complete theory of the Seer. The next verse
opens the narrower scholastic dispute over whether the eye or the knowledge
dependent upon it is literally the agent of seeing.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_41
    a vak:Karika ;
    rdfs:label "VAK 1.41" ;
    vak:hasTopic vak:SeeingAndAscertainment ;
    vak:belongsTo vak:Dhatunirdesa .

vak:EyeFaculty
    vak:performs vak:VisualDisclosure ;
    vak:hasStatus vak:Seeing .

vak:EightfoldDharmaDomainView
    a vak:DomainPart ;
    vak:hasMemberSet vak:FiveAfflictedViews ;
    vak:hasMember vak:WorldlyRightView,
        vak:TraineeView,
        vak:AdeptView ;
    vak:performs vak:Ascertainment .

vak:SensoryCobornPrajna
    vak:performs vak:SensoryDiscrimination ;
    vak:lacks vak:Ascertainment ;
    vak:notStatus vak:View .

vak:WorldlyRightView
    vak:hasEthicalStatus vak:Wholesome ;
    vak:hasOutflowStatus vak:Sasrava .

organon:AgentSeeingScience
    a vak:AgentSideModel ;
    organon:distinguishes vak:VisualDisclosure,
        vak:SensoryDiscrimination,
        vak:AscertainativeView .
```
