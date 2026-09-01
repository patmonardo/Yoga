# VAK_1.15

## 1. Sanskrit (Devanāgarī)

> चतुर्भ्योऽन्ये तु संस्कारस्कन्धः एते पुनस्त्रयः ।
>
> धर्मायतनधात्वाख्याः सहाविज्ञप्त्यसंस्कृतैः ॥ १.१५ ॥

## 2. Sanskrit (IAST)

> caturbhyo 'nye tu saṃskāraskandhaḥ ete punas trayaḥ /
>
> dharmāyatanadhātvākhyāḥ sahāvijñaptyasaṃskṛtaiḥ // 1.15 //

## 3. Lexical Analysis

```text
caturbhyo 'nye              → caturbhyaḥ anye
saṃskāraskandhaḥ            → saṃskāra-skandhaḥ
punaḥ trayaḥ                → punaḥ trayaḥ
dharmāyatanadhātvākhyāḥ    → dharma-āyatana-dhātu-ākhyāḥ
sahāvijñaptyasaṃskṛtaiḥ    → saha avijñapti-asaṃskṛtaiḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| caturbhyaḥ | ablative plural | apart from the four previously distinguished aggregates |
| anye | nominative masculine plural | the other conditioned formations |
| tu | contrastive particle | but; distinguishes the remainder from the four |
| saṃskāra-skandhaḥ | nominative masculine singular | the aggregate of formations |
| ete | nominative masculine plural demonstrative | these; refers to the three aggregates just in view |
| punaḥ | indeclinable | again; under a further classificatory arrangement |
| trayaḥ | nominative masculine plural | the three: vedanā, saṃjñā, and saṃskāra aggregates |
| dharma-āyatana | compound | the dharma-sphere, object-sphere of manas |
| dharma-dhātu | compound | the dharma-domain |
| ākhyāḥ | nominative masculine plural compound ending | called, bearing the names |
| saha | indeclinable governing the instrumental | together with |
| avijñapti | feminine noun in compound | non-disclosive form |
| asaṃskṛtaiḥ | instrumental neuter plural | the unconditioned dharmas |

The “four” are `rūpa`, `vedanā`, `saṃjñā`, and `vijñāna`. The “three” are
`vedanā`, `saṃjñā`, and `saṃskāra`. The Bhāṣya identifies the unconditioned
plural as space, cessation through discernment, and cessation independent of
discernment.

## 4. Grammar

The first pāda defines the saṃskāra aggregate by exhaustive remainder:

```text
[rūpa + vedanā + saṃjñā + vijñāna]
    = the four independently specified aggregates

conditioned formations other than these four
    = saṃskāra-skandha
```

`Caturbhyaḥ` is an ablative of separation. `Anye` supplies the plural
subject—other formations—while the singular `saṃskāra-skandhaḥ` names the
one aggregate under which they are collectively included.

The second construction changes classificatory arrangements. `Ete trayaḥ`
does not refer to three individual dharmas but to the three aggregates of
feeling, recognition, and formations. `Punaḥ` marks their redescription
within the āyatana and dhātu systems.

`Dharma-āyatana-dhātu-ākhyāḥ` distributes two names across the same contents:

```text
these three aggregates
    together with avijñapti
    and the unconditioned dharmas
        are called
    dharma-āyatana
    and dharma-dhātu
```

The compound governed by `saha` is instrumental. The Bhāṣya makes the count
explicit:

```text
3 aggregates
+ 1 avijñapti
+ 3 unconditioned dharmas
= 7 dravyas
```

The same seven contents belong to both arrangements; identity of extension
does not make āyatana and dhātu identical in meaning.

## 5. Translation

### Close syntactic construe

> The formations other than the four constitute the formations aggregate. These three, together with avijñapti and the unconditioned dharmas, are called the dharma-sphere and the dharma-domain.

### Bhāṣya-informed translation

> Every conditioned formation not included in the aggregates of form, feeling, recognition, or cognition belongs to the formations aggregate. The aggregates of feeling, recognition, and formations, together with avijñapti and the three unconditioned dharmas, constitute the seven contents arranged as dharma-āyatana and dharma-dhātu.

The second translation makes the antecedents and the sevenfold count
explicit. “Every conditioned formation” prevents the residual definition
from sounding like an arbitrary miscellaneous category.

## 6. Philosophical Translation

> The system permits no conditioned determination to remain outside classification. The factors not independently specified by the other four aggregates are gathered as formations. When reorganized for mental access and domain analysis, feeling, recognition, formations, non-disclosive form, and the unconditioned together constitute the field of dharmas.

Organon rendering:

> Dharma-domain is not a container filled with one homogeneous kind of thing. It comprehends mental factors, non-disclosive material determination, and the unconditioned according to their common place in the architecture of knowability. Their unity is conceptual and functional, not sensible or material.

The Bhāṣya gives this classification an explicitly practical necessity. A
conditioned factor left outside the aggregates would be left outside the
truths of suffering and origin and therefore outside full comprehension and
abandonment. Systematic completeness is required by liberation.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| saṃskāra | formation | conditioned factor with formative or constructed status |
| saṃskāra-skandha | formations aggregate | exhaustive class of conditioned formations outside the other four aggregates |
| cetanā | volition | predominant formation because it has the nature of karma |
| prādhānya | predominance | reason a principal member may stand for a wider class in scripture |
| abhisaṃskaraṇa | active formation | operation of forming conditioned existence |
| viprayukta-saṃskāra | mind-dissociated formation | conditioned formation not associated with ordinary mental factors |
| dharma-āyatana | dharma-sphere | object-sphere accessible to manas |
| dharma-dhātu | Dharma-domain | determinate domain containing the seven enumerated classes |
| avijñapti | non-disclosive form | rūpa included within the mental object-domain |
| asaṃskṛta | unconditioned dharma | space and the two cessations |
| dravya | distinct real content | unit used by the Bhāṣya in the sevenfold count |
| parijñā | full comprehension | Path-function directed to the truth of suffering |
| prahāṇa | abandonment | Path-function directed to what must be relinquished |

## 8. Logical Determination

The exhaustive definition of the formations aggregate is:

```text
ConditionedDharma(x)
∧ ¬Rupa(x)
∧ ¬Vedana(x)
∧ ¬Samjna(x)
∧ ¬Vijnana(x)
    → SamskaraSkandhaMember(x)
```

Volition is principal without exhausting the class:

```text
Cetanā(x)
    → HasNatureOf(x, Karma)
    ∧ PrincipalIn(x, ActiveFormation)

PrincipalMemberOf(cetanā, SamskaraSkandha)
    ↛ SamskaraSkandha = CetanāAlone
```

The sevenfold domain is:

```text
Dharmayatana = Dharmadhatu in extension here
    = VedanaSkandha
    + SamjnaSkandha
    + SamskaraSkandha
    + Avijnapti
    + Akasa
    + PratisamkhyaNirodha
    + ApratisamkhyaNirodha
```

Its unity cannot be material homogeneity:

```text
mental factors
+ non-disclosive rūpa
+ unconditioned dharmas
    → one Dharma-domain
```

The Bhāṣya's path argument is compulsory:

```text
RelevantConditionedDharma(x)
    → MustBeClassified(x)
    → IncludedInTruthStructure(x)
    → AvailableForComprehensionOrAbandonment(x)
```

Conversely:

```text
Unclassified(x)
    → NotComprehendedOrAbandoned(x)
    → EndingOfSufferingIncomplete
```

## 9. Interpretive Note

VAK 1.15 is the first explicit appearance of `dharma-dhātu` in its decisive
scope. It gathers contents that cannot be reduced to either gross matter or
private mentality: felt and recognitional factors, active formations,
avijñapti, space, and two modes of cessation. Dharma-domain is therefore not
a leftover drawer. It is the formal field in which heterogeneous realities
receive determinate standing as possible dharmas for mind and Path.

This gives “Dharma-controlled reality” a precise systematic meaning:

```text
Dharma does not make every content the same.
Dharma assigns each content its determinate status
within knowledge, suffering, origin, comprehension, and abandonment.
```

Avijñapti is pivotal because it crosses the simple opposition between mental
and material. It remains rūpa, yet it enters dharma-āyatana and dharma-dhātu
as a non-disclosive determination accessible to the mental system rather
than as an ordinary sensory object. The unconditioned enters the same domain
without becoming either matter or a mental event.

The sattvic force lies in this articulation, not in denying the real
differences among the contents. Dharmadhātu is a domain of intelligibility:
it holds mental, subtle-material, and unconditioned determinations together
while preserving exactly what each is. In the comparative Sāṃkhya idiom,
this is luminous differentiation rather than tamasic externalization.

The most radical point of the Bhāṣya is practical. Nothing implicated in
bondage may remain conceptually unclassified, because an unclassified factor
could neither be fully known nor properly abandoned. The completeness of the
Dharma-system is thus internally demanded by the possibility of liberation.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_15
    a vak:Karika ;
    rdfs:label "VAK 1.15" ;
    vak:hasTopic vak:SamskaraSkandhaAndDharmaDomain ;
    vak:belongsTo vak:Dhatunirdesa .

vak:SamskaraSkandha
    a vak:ExhaustiveConditionedClassification ;
    vak:hasPrincipalMember vak:Cetana ;
    vak:includes vak:RemainingMentalFactors ,
        vak:MindDissociatedFormations .

vak:Cetana
    vak:hasNatureOf vak:Karma ;
    vak:isPrincipalIn vak:ActiveFormation .

vak:DharmaAyatana
    vak:hasSameExtensionHereAs vak:DharmaDhatu .

vak:DharmaDhatu
    a vak:DomainOfKnowableDharmas ;
    vak:includes vak:VedanaSkandha , vak:SamjnaSkandha ,
        vak:SamskaraSkandha , vak:Avijnapti , vak:Akasa ,
        vak:PratisamkhyaNirodha , vak:ApratisamkhyaNirodha .

vak:RelevantConditionedDharma
    vak:requiresClassificationFor vak:FullComprehension ,
        vak:Abandonment , vak:EndingOfSuffering .
```
