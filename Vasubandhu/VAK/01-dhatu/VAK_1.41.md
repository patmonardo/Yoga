# VAK_1.41

## 1. Sanskrit (Devanāgarī)

> चक्षुश्च धर्मधातोश्च प्रदेशौ दृष्टिः अष्टधा ।
>
> पञ्चविज्ञानसहजा धीर्न दृष्टिरतीरणात् ॥ १.४१ ॥

## 2. Sanskrit (IAST)

> cakṣuś ca dharmadhātoś ca pradeśau dṛṣṭiḥ aṣṭadhā /
>
> pañcavijñānasahajā dhīr na dṛṣṭir atīraṇāt // VAkK_1.41 //

Source saṃhitā form:

> cakṣuśca dharmadhātośca pradeśau dṛṣṭiḥ aṣṭadhā /
>
> pañcavijñānasahajā dhīrna dṛṣṭiratīraṇāt // VAkK_1.41 //

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| cakṣuḥ ca | cakṣuḥ ca | and the eye |
| dharmadhātoḥ ca | dharma-dhātoḥ ca | and of the dharma-domain |
| pradeśau | pradeśau | two portions / regions |
| dṛṣṭiḥ | dṛṣṭiḥ | seeing, view |
| aṣṭadhā | aṣṭadhā | eightfold |
| pañca-vijñāna-sahajā | pañca-vijñāna-sahajā | co-born with the five knowledge-domains |
| dhīḥ | dhīḥ | intelligence, discernment |
| na dṛṣṭiḥ | na dṛṣṭiḥ | is not seeing/view |
| atīraṇāt | a-tīraṇāt | because of non-ascertainment / non-decisive determination |

## 4. Grammar

The verse defines **dṛṣṭi** after VAK_1.40 has introduced what is abandoned by seeing.

```text
cakṣuḥ-pradeśa
    a portion of the eye-domain

dharmadhātu-pradeśa
    a portion of the dharma-domain
```

These two portions constitute **dṛṣṭi**, eightfold.

The second half excludes the intelligence co-born with the five sensory knowledge-domains:

```text
pañca-vijñāna-sahajā dhīḥ
    intelligence arising together with the five sensory knowledges

na dṛṣṭiḥ
    is not dṛṣṭi

atīraṇāt
    because it does not ascertain / determine decisively
```

Thus sensory co-born intelligence may discriminate, but it does not yet have the determining force of view.

## 5. Literal Translation

> A portion of the eye and a portion of the dharma-domain are seeing, eightfold. The intelligence co-born with the five knowledge-domains is not seeing, because it does not ascertain.

## 6. Philosophical Translation

> Seeing is not identical with every cognition. It belongs to a portion of the eye-domain and a portion of the dharma-domain, and it is eightfold. The intelligence that arises with the five sensory knowledge-domains is not view, because it lacks decisive ascertainment.

Organon rendering:

> Dṛṣṭi is not mere sensory awareness. It is a determined seeing grounded in eye and dharmadhātu. Sensory intelligence accompanies knowledge, but without ascertainment it does not become view. Seeing requires decisive determination.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| cakṣus | eye-domain | visual faculty-domain |
| dharmadhātu | dharma-domain | here a portion bears view-status |
| pradeśa | portion / region | partial domain-status, not the whole domain |
| dṛṣṭi | seeing / view | decisive seeing; context includes path-view |
| aṣṭadhā | eightfold | eightfold view-structure, to be reviewed with bhāṣya |
| dhī | intelligence / discernment | co-born sensory intelligence is not yet dṛṣṭi |
| atīraṇa | non-ascertainment | lack of decisive determination |

## 8. Logical Determination

VAK_1.40 introduced abandonment by seeing. VAK_1.41 asks: what is seeing?

```text
dṛṣṭi
    = portion of eye-domain
    + portion of dharmadhātu
    = eightfold
```

But:

```text
sensory co-born dhī
    ≠ dṛṣṭi

because:
    it lacks tīraṇa, decisive ascertainment
```

The distinction is:

```text
cognition
    may arise

intelligence
    may accompany cognition

but view / seeing
    requires ascertainment
```

## 9. Interpretive Note

This verse is vital because it prevents **seeing** from being confused with sensation.

The five sensory knowledge-domains are cognitively alive; they have co-born intelligence. But they do not ascertain. They do not determine truth as truth. They are not yet dṛṣṭi.

The presence of dharmadhātu is decisive. Seeing is not merely optical. A portion of the eye participates, but a portion of the dharma-domain participates too. Seeing becomes view only where the sensory side and the domain of determinations meet.

Organon sequence:

```text
1.40 path-negation / abandonability
1.41 seeing as ascertainment
```

Kant-Fichte-Hegel note:

```text
intuition alone
    is not seeing in the higher sense

sensory intelligence
    is not yet judgment

dṛṣṭi
    requires determinate ascertainment
    through dharmadhātu
```

Thus the path of seeing is not mere perception. It is the emergence of determined truth-vision.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_41
    a vak:Karika ;
    rdfs:label "VAK 1.41" ;
    vak:hasIAST "cakṣuś ca dharmadhātoś ca pradeśau dṛṣṭiḥ aṣṭadhā / pañcavijñānasahajā dhīr na dṛṣṭir atīraṇāt" ;
    vak:hasTopic vak:SeeingAsAscertainment ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Drsti
    a vak:PathFaculty ;
    rdfs:label "seeing / view" ;
    vak:sanskrit "dṛṣṭi" ;
    vak:hasSourcePortion vak:CaksusDhatuPortion ;
    vak:hasSourcePortion vak:DharmaDhatuPortion ;
    vak:hasModeCount 8 .

vak:SensoryCobornDhi
    a vak:CognitiveFactor ;
    rdfs:label "intelligence co-born with five sensory knowledges" ;
    vak:notEqualTo vak:Drsti ;
    vak:lacks vak:Ascertainment .

vak:Ascertainment
    a vak:Determination ;
    rdfs:label "decisive ascertainment" ;
    vak:sanskrit "tīraṇa" .
```

## 11. Commit History

- Added Organon analysis for VAK_1.41.
- Defines **dṛṣṭi** after VAK_1.40's abandonability structure.
- Establishes seeing as a portion of eye-domain and dharma-domain.
- Marks the eightfold structure for later bhāṣya review.
- Distinguishes co-born sensory intelligence from view because it lacks ascertainment.
