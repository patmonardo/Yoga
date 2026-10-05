# VAK_1.09 — Form Base: faculties, Meanings, and Avijñapti

## 1. Sanskrit (Devanāgarī)

> रूपं पञ्चेन्द्रियाण्यर्थाः पञ्चाविज्ञप्तिरेव च ।
>
> तद्विज्ञानाश्रया रूपप्रसादाश्चक्षुरादयः ॥ १.०९ ॥

## 2. Sanskrit (IAST)

> rūpaṃ pañcendriyāṇy arthāḥ pañcāvijñaptir eva ca /
>
> tadvijñānāśrayā rūpaprasādāś cakṣurādayaḥ // 1.09 //

## 3. Lexical Analysis

| Form | Morphology | Force in this passage |
|---|---|---|
| rūpam | nominative neuter singular | Form |
| pañca indriyāṇi | numeral + nominative/accusative neuter plural | five faculties |
| arthāḥ | nominative masculine plural | meanings |
| pañca | indeclinable numeral | counts the meanings |
| avijñaptiḥ | nominative feminine singular | *avijñapti*, a single listed member |
| eva ca | emphatic and connective particles | and also; includes *avijñapti* |
| tad-vijñāna-āśrayāḥ | nominative masculine plural compound | supports of the corresponding cognitions |
| rūpa-prasādāḥ | nominative masculine plural | Form clarities |
| cakṣus-ādayaḥ | nominative masculine plural | the eye and the remaining faculties |

The first line counts five faculties, five meanings, and one *avijñapti*:
eleven members of the Form Base. The cognitions supported by the faculties
belong to the relation stated in the second line, not to this count.

## 4. Grammar

```text
rūpam (rūpa-skandha)
    = five faculties
    + five meanings
    + avijñapti

eye and the remaining faculties
    = Form clarities
    = supports of corresponding cognitions
```

The first line enumerates the Form Base. The second predicates two
determinations of the eye and the remaining faculties: they are clarities
of Form and supports of the corresponding cognitions. The supported
cognitions are not additional members of the Form Base.

## 5. Translation

### Close syntactic construe

> Form is the five faculties, the five meanings, and *avijñapti* also.
> The Form clarities, beginning with the eye, are supports of the
> corresponding cognitions.

### Bhāṣya-informed translation

> The Form Base consists of five faculties, the five respective meanings
> or conditions (*viṣaya*) of those faculties, and *avijñapti*. The
> meanings are visible form, sound, odor, taste, and the tangible. The
> faculties beginning with the eye are Form clarities and support the
> cognitions corresponding to those meanings. *Avijñapti* is included but
> not defined here; the five meanings are named and remain to be explained.

The Bhāṣya's scriptural citation calls the eye an internal Essence
(*āyatana*) and a Form clarity dependent on the four Great Elements.
Here *upādāya* means “depending on,” not appropriation as in 1.08.

## 6. Philosophical Translation

This verse specifies the Form Base within the Base system of the Dharma
System: five faculties, five meanings, and one *avijñapti*. Its second line
does not enlarge that enumeration. It gives the faculty's support-relation
to the corresponding cognition. The Bhāṣya's citation also names the eye
as an internal Essence, marking another determination without adding
Essence to the eleven Form-Base members.

The complete Dharma Concept is `<Base, Essence, Principle>`. This verse
specifies Form Base, names the eye's Essence classification, and states the
faculty's support-relation to Discriminative Cognition. Read through Kant's
principles, these determinations disclose the Kośa's explicit systematic
unity, guided by Vijñāna.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| rūpa-skandha | Form Base | Form's Base determination |
| rūpa-prasāda | Form clarity | the Form-character of the five faculties |
| indriya | faculty | each of the five supports: eye through body |
| artha | meaning | one of the five meanings named by the verse |
| viṣaya | condition | the Bhāṣya's specification of each respective meaning |
| avijñapti | *avijñapti* | included as one member; not defined here |
| vijñāna | Cognition (Discriminative Cognition) | the sensory cognition corresponding to a meaning; its defining function is discrimination |
| āśraya | support | relation of the faculty to its corresponding cognition |
| āyatana | Essence | named for the eye in the cited scripture |
| upādāya | depending on | dependence on the four Great Elements in this citation |

## 8. Logical Determination

```text
Form Base
    = five faculties
    + five meanings
    + one avijñapti
    = eleven members

for each faculty:
    Form clarity
    → support of its corresponding cognition

eye
    → named as an internal Essence in the cited scripture

corresponding cognition
    ↛ additional Form-Base member
```

## 9. Interpretive Note

The hinge is the shift from enumeration to support. The first line defines
what is included in the Form Base; the second identifies what the faculties
support. The eye's Essence classification is a cross-classification, not a
change to the Base count. *Avijñapti* is named here without a definition.

The Kośa explicitly presents *rūpaprasāda* (“Form clarities”) as the
transition from the sensory manifold returned by the faculties to the
clarity Saṃjñā presents through Manas, yielding True Meanings. This carries
the analysis beyond Form Base into Dharma Base. The same *avijñapti* is
classified in both; Vijñāna bears a *prati* relation to it and governs Manas.
Vijñāna joins and governs Perception and Conception: their unity is
Inconceivable as a homogeneous operation, while its Idea is disclosed in
Vijñāna-skandha.

## 10. OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_09
    a vak:Karika ;
    rdfs:label "VAK 1.09" ;
    vak:hasSourceLabel "VAkK_1.9" ;
    vak:hasTopic vak:FormBase ;
    vak:belongsTo vak:Dhatunirdesa .

vak:FormBase
    vak:hasFaculty vak:EyeFaculty, vak:EarFaculty, vak:NoseFaculty,
        vak:TongueFaculty, vak:BodyFaculty ;
    vak:hasMeaning vak:VisibleForm, vak:Sound, vak:Odor, vak:Taste,
        vak:Tangible ;
    vak:hasMember vak:Avijnapti ;
    vak:memberCount 11 ;
    vak:isSubsystemOf vak:DharmaSystem .

vak:Faculty rdfs:subClassOf vak:RupaPrasada .

vak:EyeFaculty
    a vak:Faculty ;
    vak:supports vak:EyeCognition ;
    vak:hasEssenceClassification vak:InternalEssence ;
    vak:dependsOn vak:FourGreatElements .

vak:EarFaculty vak:supports vak:EarCognition .
vak:NoseFaculty vak:supports vak:NoseCognition .
vak:TongueFaculty vak:supports vak:TongueCognition .
vak:BodyFaculty vak:supports vak:BodyCognition .

vak:EyeCognition a vak:DiscriminativeCognition ;
    vak:hasMeaning vak:VisibleForm .
vak:EarCognition a vak:DiscriminativeCognition ;
    vak:hasMeaning vak:Sound .
vak:NoseCognition a vak:DiscriminativeCognition ;
    vak:hasMeaning vak:Odor .
vak:TongueCognition a vak:DiscriminativeCognition ;
    vak:hasMeaning vak:Taste .
vak:BodyCognition a vak:DiscriminativeCognition ;
    vak:hasMeaning vak:Tangible .

vak:Vijnana rdfs:label "vijñāna" ;
    vak:rendersAs vak:DiscriminativeCognition .
vak:Dhatu rdfs:label "dhātu" ;
    vak:rendersAs vak:Principle .

vak:TechneReading_1_09
    a vak:OrganonInterpretation ;
    vak:interprets vak:RupaPrasada ;
    vak:transitionsFrom vak:FormBase ;
    vak:transitionsTo vak:DharmaBase ;
    vak:clarityPresentedBy vak:Samjna ;
    vak:mediatedBy vak:Manas .
```
