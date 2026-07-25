# VAK_1.46

## 1. Sanskrit (Devanāgarī)

> न कायस्याधरं चक्षुः ऊर्ध्वं रूपं न चक्षुषः ।
>
> विज्ञानं चास्य रूपं तु कायस्योभे च सर्वतः ॥ १.४६ ॥

## 2. Sanskrit (IAST)

> na kāyasyādharaṃ cakṣuḥ ūrdhvaṃ rūpaṃ na cakṣuṣaḥ /
>
> vijñānaṃ cāsya rūpaṃ tu kāyasyobhe ca sarvataḥ // VAkK_1.46 //

Source saṃhitā form:

> na kāyasyādharaṃ cakṣuḥ ūrdhvaṃ rūpaṃ na cakṣuṣaḥ /
>
> vijñānaṃ ca asya rūpaṃ tu kāyasyobhe ca sarvataḥ // VAkK_1.46 //

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| na | na | not |
| kāyasya | kāyasya | of the body / body-domain |
| adharam | adharam | lower |
| cakṣuḥ | cakṣuḥ | eye |
| ūrdhvam | ūrdhvam | higher |
| rūpam | rūpam | visible form |
| na cakṣuṣaḥ | na cakṣuṣaḥ | not of the eye / than the eye |
| vijñānam ca asya | vijñānam ca asya | and its knowledge |
| rūpam tu | rūpam tu | but visible form |
| kāyasya | kāyasya | of the body |
| ubhe ca | ubhe ca | and both |
| sarvataḥ | sarvataḥ | from all / in every way |

## 4. Grammar

This verse classifies eye, visible form, and eye-knowledge by relation to **kāya**, the body-level or bodily plane.

The main constraints are:

```text
cakṣus
    is not lower than the body

rūpa
    is not higher than the eye

cakṣurvijñāna
    follows the level of its support/object relation
```

The phrase **rūpaṃ tu kāyasya ubhe ca sarvataḥ** indicates that visible form, in relation to the body-level, may occur in both ways or in all directions according to plane-relation. This verse is compact and should be reviewed with the bhāṣya, but its function is clear: it begins the classification of domains by vertical plane-relation.

## 5. Literal Translation

> The eye is not lower than the body; visible form is not higher than the eye. Its knowledge also [is so]; but visible form, with respect to the body, and both, are in all ways.

## 6. Philosophical Translation

> The eye-domain cannot belong to a plane lower than the body-domain, and visible form cannot stand higher than the eye-domain. Eye-knowledge follows the determinate relation of its support and object. Visible form and bodily relation admit broader plane-variation.

Organon rendering:

> The domain-system is now verticalized. A faculty, its object, and its knowledge are not placed arbitrarily across levels. Eye, visible form, and eye-knowledge obey a lawful plane-relation: support, object, and disclosure are constrained by the level of embodiment.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| kāya | body / body-domain | bodily level used as reference |
| adhara | lower | lower plane relation |
| ūrdhva | higher | higher plane relation |
| cakṣus | eye-domain | visual faculty |
| rūpa | visible form | visual object-domain |
| vijñāna | knowledge | here eye-knowledge |
| sarvataḥ | in all ways | broad plane-variation; bhāṣya review needed |

## 8. Logical Determination

VAK_1.45 explained why knowledge is named from support. VAK_1.46 now adds plane-relation:

```text
support
    has plane-location

object
    has plane-location

knowledge
    is constrained by support/object relation
```

The core rule:

```text
domain-disclosure
    is not level-free
```

Knowing occurs within a lawful vertical order of embodiment and object-domain.

## 9. Interpretive Note

This verse is difficult in isolation, but its place in the sequence is clear. After defining support, the chapter asks how support, object, and knowledge stand across levels.

The eye cannot simply operate below the bodily basis. Visible form cannot be higher than the eye in the relevant relation. Knowledge is not detached from these constraints.

Organon sequence:

```text
1.45 support determines knowledge
1.46 support/object/knowledge are plane-constrained
```

Kant-Fichte-Hegel note:

```text
knowledge
    is not abstract subjectivity

knowledge
    is the disclosure of an object
    through a support
    within a determinate level of embodiment
```

This is the verticalization of the domain-system.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_46
    a vak:Karika ;
    rdfs:label "VAK 1.46" ;
    vak:hasIAST "na kāyasyādharaṃ cakṣuḥ ūrdhvaṃ rūpaṃ na cakṣuṣaḥ / vijñānaṃ cāsya rūpaṃ tu kāyasyobhe ca sarvataḥ" ;
    vak:hasTopic vak:PlaneRelationOfVisualDomain ;
    vak:belongsTo vak:Dhatunirdesa .

vak:PlaneRelationOfVisualDomain
    a vak:LogicalDetermination ;
    rdfs:label "plane relation of visual domain" ;
    vak:relates vak:CaksusDhatu , vak:RupaDhatu , vak:CaksurVijnanaDhatu , vak:KayaDhatu .
```

## 11. Commit History

- Added Organon analysis for VAK_1.46.
- Establishes plane-relation among body, eye, visible form, and eye-knowledge.
- Marks the verse for bhāṣya review because of compact syntax.
- Adds vertical level-constraint to the chapter sequence after support-determination.
