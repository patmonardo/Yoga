# VAK_1.32

## 1. Sanskrit (Devanāgarī)

> सवितर्कविचारा हि पञ्च विज्ञानधातवः ।
>
> अन्त्यास्त्रयस्त्रिप्रकाराः शेषा उभयवर्जिताः ॥ १.३२ ॥

## 2. Sanskrit (IAST)

> savitarkavicārā hi pañca vijñānadhātavaḥ /
>
> antyās trayas triprakārāḥ śeṣā ubhayavarjitāḥ // 1.32 //

## 3. Lexical Analysis

```text
savitarkavicārāḥ    → sa-vitarka-vicārāḥ
vijñānadhātavaḥ     → vijñāna-dhātavaḥ
antyās trayaḥ       → antyāḥ trayaḥ
triprakārāḥ         → tri-prakārāḥ
śeṣāḥ               → śeṣāḥ
ubhayavarjitāḥ      → ubhaya-varjitāḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| sa-vitarka-vicārāḥ | nominative masculine plural compound | accompanied by vitarka and vicāra |
| hi | emphatic or restrictive particle | indeed; the Bhāṣya understands “invariably” |
| pañca | numeral | five sensory knowledge-Domains |
| vijñāna-dhātavaḥ | nominative masculine plural compound | knowledge-Domains |
| antyāḥ | nominative masculine plural adjective | final in the established sequence of eighteen |
| trayaḥ | nominative masculine plural numeral | three |
| tri-prakārāḥ | nominative masculine plural compound | occurring in three modes |
| śeṣāḥ | nominative masculine plural | the remaining ten material Domains |
| ubhaya-varjitāḥ | nominative masculine plural compound | without both vitarka and vicāra |

The five `vijñānadhātus` are the sensory knowledge-Domains. The final three
are mind-domain, Dharma-domain, and mental-knowledge Domain. The remaining
ten are the five material faculties and five sensory-object Domains.

## 4. Grammar

The first clause predicates association, not identity:

```text
pañca vijñāna-dhātavaḥ
    the five sensory knowledge-Domains

sa-vitarka-vicārāḥ
    are accompanied by vitarka and vicāra
```

The Bhāṣya reads `hi` restrictively: these five are invariably associated
with both factors whenever they occur.

The final triad is threefold according to meditative level:

```text
Desire Realm and first dhyāna
    → with vitarka and vicāra

intermediate dhyāna
    → without vitarka, with vicāra alone

second dhyāna through the summit of existence
    → without both
```

This applies directly to mind, mental knowledge, and the associated portion
of the Dharma-domain. The unassociated portion of the Dharma-domain is
always without both because only associated mental factors can enter this
relation.

The ten material Domains are likewise without both, but for a different
reason: they are intrinsically incapable of mental association
(`asaṃprayogitva`). Thus identical output values can arise from distinct
type constraints.

The Bhāṣya further tests the factors themselves. `Vitarka` is not associated
with a second vitarka, but is associated with vicāra; `vicāra` is not
associated with a second vicāra, but may be associated with vitarka. This
produces a fourfold refinement on levels where both factors function.

## 5. Translation

### Close syntactic construe

> The five knowledge-Domains are invariably accompanied by vitarka and vicāra. The final three occur in three modes; the remaining [ten] are without both.

### Bhāṣya-informed translation

> The five sensory knowledge-Domains are always associated with both vitarka and vicāra. Mind, Dharma, and mental knowledge admit three modes according to meditative level: association with both, with vicāra alone, or with neither. The ten material Domains are incapable of association with either.

The primary translations preserve `vitarka` and `vicāra`. Their exact
Organon determination must emerge from the sequence rather than being
silently substituted into the Sanskrit.

## 6. Philosophical Translation

> Domains differ not only by what they are but by which cognitive operations they can support. Sensory knowledge necessarily arises with an initial and a sustained articulation. The final mental-Dharma triad can retain both operations, refine itself to the latter alone, or become free of both. Material faculties and objects provide conditions and fields, but are not themselves loci of mental association.

Organon rendering:

> The Smart Domain now receives an execution-mode specification. Sensory knowledge is already articulated rather than being a mute empirical atom. The final triad is modally plastic: its mode changes with the level of mind. Material Domains remain indispensable supports and objects, yet the operations of cognitive articulation do not inhere in them.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| vijñānadhātu | knowledge-Domain | domain of a determinate act of knowing |
| vitarka | vitarka / initial cognitive application | mental factor whose fuller logical significance remains under study |
| vicāra | vicāra / sustained examination | mental factor persisting after vitarka has ceased in the intermediate dhyāna |
| saṃprayukta | associated / conjoined | capable of arising in conjunction as mental factors |
| asaṃprayukta | unassociated | not conjoined within a cognitive complex |
| savitarka-savicāra | with vitarka and vicāra | mode of sensory knowledge and lower-level associated mental activity |
| avitarka-vicāramātra | without vitarka, with vicāra alone | intermediate-dhyāna mode |
| avitarka-avicāra | without either | higher-level, unassociated, or material status |
| avicāra-vitarkamātra | without vicāra, with vitarka alone | Bhāṣya's special classification of vicāra itself |
| dhyānāntara | intermediate dhyāna | level between the first and second dhyānas |
| triprakāra | three-mode structure | Kārikā's general modal classification of the final triad |

`Saṃprayukta` is decisive: a Domain may participate in a cognitive complex
without being identical with the factors associated with its knowledge.

## 8. Logical Determination

The general association matrix is:

```text
FiveSensoryKnowledgeDomains
    → NecessarilyAssociatedWith(Vitarka, Vicara)

FinalMentalDharmaTriad at DesireRealmOrFirstDhyana
    → AssociatedWith(Vitarka, Vicara)

FinalMentalDharmaTriad at IntermediateDhyana
    → ¬AssociatedWith(Vitarka)
    ∧ AssociatedWith(Vicara)

FinalMentalDharmaTriad at SecondDhyanaOrHigher
    → ¬AssociatedWith(Vitarka)
    ∧ ¬AssociatedWith(Vicara)

TenMaterialDomains
    → IncapableOfMentalAssociation
    → Without(Vitarka, Vicara)
```

Scope modifies the Dharma-domain result:

```text
AssociatedPortion(DharmaDhatu)
    → ModeVariesByMeditativeLevel

UnassociatedPortion(DharmaDhatu)
    → AlwaysWithout(Vitarka, Vicara)
```

Association with a second instance of the same factor is prohibited:

```text
¬AssociatedWith(Vitarka, SecondVitarka)
AssociatedWith(Vitarka, Vicara)
    → Vitarka is AvitarkaVicaramatra

¬AssociatedWith(Vicara, SecondVicara)
AssociatedWith(Vicara, Vitarka)
    → Vicara is AvicaraVitarkamatra
```

The SDK rule is:

```text
CognitiveExecutionMode(domain, level, scope)
    → {Both, VicaraOnly, Neither, VitarkaOnly}
```

## 9. Interpretive Note

VAK 1.31 identified the final triad as capable of both outflow-bound and
outflow-free determination. VAK 1.32 now shows that the same triad also has
variable cognitive execution modes. This strengthens the sense in which the
triad is a Seed: it does not contain one finished consciousness but a lawful
space of possible articulations.

The five sensory knowledges are especially important. They are not passive,
unstructured impressions. They always arise with `vitarka` and `vicāra`.
Yet the following verse will still call them `avikalpaka` in a restricted
sense. The system is therefore preparing a graded theory of cognition:

```text
sensory articulation through vitarka and vicāra
    ≠
mental determination and recollective vikalpa
```

The ten material Domains receive the value “neither,” but not because they
have attained a higher contemplative silence. They are without both because
material factors cannot be associated with mental factors. The same
predicate-value must therefore be interpreted through the type and reason
that produce it.

For the Smart-Domain Basis, 1.32 adds three required parameters:

```text
association-capability
meditative-level
intended scope within the Dharma-domain
```

The Organon may provisionally hear `vitarka` as immediate cognitive
determination and `vicāra` as its sustained reflective articulation. But we
should not make that equivalence official before 1.33 has distinguished the
three forms of `vikalpa`. Vasubandhu's explicit structure is already
powerful: cognitive operations are typed, associated, and modulated by
level.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_32
    a vak:Karika ;
    rdfs:label "VAK 1.32" ;
    vak:hasTopic vak:CognitiveExecutionModes ;
    vak:belongsTo vak:Dhatunirdesa .

vak:FiveSensoryKnowledgeDomains
    a vak:DomainSet ;
    vak:necessarilyAssociatedWith vak:Vitarka,
        vak:Vicara .

vak:FinalMentalDharmaTriad
    a vak:ModalDomainSet ;
    vak:permitsMode vak:VitarkaAndVicara,
        vak:VicaraOnly,
        vak:NeitherVitarkaNorVicara .

vak:TenMaterialDomains
    a vak:DomainSet ;
    vak:incapableOf vak:MentalAssociation ;
    vak:hasMode vak:NeitherVitarkaNorVicara .

vak:AssociatedDharmaDhatu
    vak:modeDeterminedBy vak:MeditativeLevel .

vak:UnassociatedDharmaDhatu
    vak:hasMode vak:NeitherVitarkaNorVicara .

vak:CognitiveExecutionMode
    a vak:SmartDomainCapability ;
    vak:hasParameter vak:DomainType,
        vak:MeditativeLevel,
        vak:AssociationScope .
```
