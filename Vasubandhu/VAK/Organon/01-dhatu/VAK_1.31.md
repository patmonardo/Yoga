# VAK_1.31

## 1. Sanskrit (Devanāgarī)

> आरूप्याप्ता मनोधर्ममनोविज्ञानधातवः ।
>
> सास्रवानास्रवा एते त्रयः शेषास्तु सास्रवाः ॥ १.३१ ॥

## 2. Sanskrit (IAST)

> ārūpyāptā manodharmamanovijñānadhātavaḥ /
>
> sāsravānāsravā ete trayaḥ śeṣās tu sāsravāḥ // 1.31 //

## 3. Padaccheda

```text
ārūpyāptāḥ                    → ārūpya-āptāḥ
manodharmamanovijñānadhātavaḥ → mano-dhātu + dharma-dhātu
                                 + mano-vijñāna-dhātu
sāsravānāsravāḥ               → sa-āsravāḥ an-āsravāḥ
śeṣās tu                      → śeṣāḥ tu
```

| Form | Morphology | Lexical force here |
|---|---|---|
| ārūpya-āptāḥ | nominative masculine plural compound | belonging to or connected with the Formless Realm |
| mano-dhātu | compound member | mind-domain |
| dharma-dhātu | compound member | Dharma-domain |
| mano-vijñāna-dhātu | compound member | mental-consciousness Domain |
| sa-āsravāḥ | nominative masculine plural adjective | accompanied by outflows; implicated in conditioned existence |
| an-āsravāḥ | nominative masculine plural adjective | without outflows |
| ete trayaḥ | demonstrative plus numeral, nominative plural | these three Domains |
| śeṣāḥ | nominative masculine plural | the remaining fifteen Domains |
| tu | contrastive particle | but |

The opening compound enumerates exactly three Domains. The second line then
classifies those same three by outflow-status and contrasts them with the
remaining fifteen.

## 4. Grammar

VAK 1.30 began the threefold classification by realm. VAK 1.31 completes it:

```text
ārūpyāptāḥ
    belonging to the Formless Realm

mano-dharma-mano-vijñāna-dhātavaḥ
    are the mind-, Dharma-, and mental-consciousness Domains
```

The Bhāṣya derives this configuration from detachment from form. Ten
material Domains are absent because their intrinsic nature is form. The
five sensory consciousness-Domains are absent because both their material
supports and their material objects are absent. Subtracting these fifteen
from the eighteen leaves the final mental-Dharma triad.

The compact predicate `sāsravānāsravāḥ` is distributive over the three:
they admit both outflow-bound and outflow-free instances. It does not say
that every instance of each Domain possesses both contradictory statuses at
once.

The Bhāṣya supplies the criterion:

```text
included in Path-truth
or included among the unconditioned dharmas
    → anāsrava

otherwise
    → sāsrava
```

The final clause is stronger than a casual “the others have outflows.” The
Bhāṣya calls the remaining fifteen `ekāntasāsrava`: exclusively and without
exception outflow-bound.

## 5. Translation

### Close syntactic construe

> The mind-domain, Dharma-domain, and mental-consciousness Domain belong to the Formless Realm. These three may be with outflows or without outflows; the remaining [fifteen] are with outflows.

### Bhāṣya-informed translation

> Only the mind-domain, Dharma-domain, and mental-consciousness Domain belong to the Formless Realm. The ten material Domains are absent there, as are the five sensory consciousnesses that depend upon material faculties and objects. The final three may be either outflow-bound or outflow-free; the other fifteen are exclusively outflow-bound.

“Only” in the second rendering expresses the Bhāṣya's subtraction, not an
additional word in the Kārikā.

## 6. Philosophical Translation

> When form, material support, and sensory object are withdrawn, the Domain-system contracts to mind, Dharma, and mental consciousness. This triad does not belong intrinsically either to bondage or to freedom: it can bear the outflows of conditioned existence, but it can also carry Path-truth and the outflow-free. The remaining sensory-material configuration belongs wholly to the outflow-bound field.

Organon rendering:

> The final triad is the hinge within the Basis of the System. Mind supplies the cognitive succession, Dharma supplies its determinate object-field—including the Path and the unconditioned—and mental consciousness supplies their act of disclosure. Because this structure can be configured either under outflow or without it, the same conceptual lineage can mediate bondage and liberation without making them identical.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| ārūpya | Formless Realm | configuration in which material supports and objects are absent |
| ārūpyāpta | belonging to the Formless Realm | realm compatibility of the final three Domains |
| rūpavītarāga | detached from form | causal condition for rebirth in the Formless Realm |
| manodhātu | mind-domain | mental support and succession within the eighteen-Domain system |
| dharmadhātu | Dharma-domain | mental object-domain containing conditioned and unconditioned dharmas |
| manovijñānadhātu | mental-consciousness Domain | cognition correlated with mind and Dharma |
| sāsrava | with outflows / outflow-bound | implicated in defilement, appropriation, and conditioned continuation |
| anāsrava | without outflows / outflow-free | includes Path-truth and the unconditioned in the relevant respects |
| ekāntasāsrava | exclusively outflow-bound | strict status of the remaining fifteen Domains |
| mārgasatya | Path-truth | conditioned outflow-free content |
| asaṃskṛta | unconditioned | included within the outflow-free Dharma-domain |

`Anāsrava` is not interchangeable with “formless.” The three formless
compatible Domains can be either outflow-bound or outflow-free.

## 8. Logical Determination

The Formless configuration is obtained relationally:

```text
DetachedFrom(Form)
    → Absent(TenMaterialDomains)

Absent(MaterialFacultySupports)
∧ Absent(MaterialObjects)
    → Absent(FiveSensoryConsciousnessDomains)

18 − 10 − 5
    = {ManoDhatu, DharmaDhatu, ManoVijnanaDhatu}
```

The outflow typing is:

```text
DomainInstance(x)
∧ x ∈ {ManoDhatu, DharmaDhatu, ManoVijnanaDhatu}
    → MayHaveStatus(x, Sasrava)
    ∨ MayHaveStatus(x, Anasrava)

Domain(x)
∧ x ∈ RemainingFifteenDomains
    → NecessarilyHasStatus(x, Sasrava)
```

The Bhāṣya's positive criterion is:

```text
IncludedIn(x, PathTruth)
∨ IncludedIn(x, Unconditioned)
    → Anasrava(x)

Otherwise(x)
    → Sasrava(x)
```

Two invalid inferences are thereby blocked:

```text
Mental(x)
    ↛ Anasrava(x)

FormlessRealmCompatible(x)
    ↛ Anasrava(x)
```

The Smart-Domain capability can therefore be expressed as:

```text
OutflowPolymorphic(x)
    ↔ x ∈ FinalMentalDharmaTriad
```

## 9. Interpretive Note

VAK 1.31 completes the distribution begun in 1.30. The three realms are not
three containers holding progressively fewer objects by accident. Each is a
lawful configuration of possible supports, objects, and cognitions:

```text
Desire Realm
    → all eighteen Domains

Form Realm
    → fourteen Domains

Formless Realm
    → mind, Dharma, and mental consciousness
```

The more important result lies in the second line. The final triad alone
crosses the boundary between outflow-bound and outflow-free determination.
This does not make “mind” inherently Buddha Mind. Ordinary mental activity
remains fully capable of carrying outflows. Nor does it reduce liberation to
a separate substance imported from outside the system. Path-truth and the
unconditioned are available within the scope of the mental-Dharma triad.

In our language of Dharma lineages, the same lineage admits opposed modes of
actualization:

```text
mind–Dharma–mental consciousness
    under outflow
        → conditioned cognition

mind–Dharma–mental consciousness
    without outflow
        → Path and liberating disclosure
```

This is the first genuinely “smart” bifurcation in the Basis. The Domain
does not merely announce what it contains; it specifies which modes of
determination are permitted. The sensory-material fifteen have a fixed
outflow type. The final triad is outflow-polymorphic.

The Organon may see here the conceptual hinge through which Buddha Mind can
eventually become explicit, but the verse itself remains exact and modest:
these three Domains can be sāsrava or anāsrava. Their purity is a
determination, not an automatic consequence of being inward or formless.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_31
    a vak:Karika ;
    rdfs:label "VAK 1.31" ;
    vak:hasTopic vak:FormlessRealmAndOutflowStatus ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Arupyadhatu
    a vak:RealmConfiguration ;
    vak:supports vak:ManoDhatu,
        vak:DharmaDhatu,
        vak:ManoVijnanaDhatu ;
    vak:excludes vak:TenMaterialDomains,
        vak:FiveSensoryConsciousnessDomains .

vak:FinalMentalDharmaTriad
    a vak:DomainSet,
        vak:OutflowPolymorphicDomainSet ;
    vak:hasMember vak:ManoDhatu,
        vak:DharmaDhatu,
        vak:ManoVijnanaDhatu ;
    vak:permitsStatus vak:Sasrava,
        vak:Anasrava .

vak:RemainingFifteenDomains
    a vak:DomainSet ;
    vak:necessarilyHasStatus vak:Sasrava .

vak:Anasrava
    vak:includes vak:PathTruth,
        vak:UnconditionedDharmas .
```
