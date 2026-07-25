# VAK_1.35

## 1. Sanskrit (Devanāgarī)

> स्प्रष्टव्यं द्विविधं शेषा रूपिणो नव भौतिकाः ।
>
> धर्मधात्वेकदेशश्च सञ्चिता दश रूपिणः ॥ १.३५ ॥

## 2. Sanskrit (IAST)

> spraṣṭavyaṃ dvividhaṃ śeṣā rūpiṇo nava bhautikāḥ /
>
> dharmadhātvekadeśaś ca saṃcitā daśa rūpiṇaḥ // VAkK_1.35 //

## 3. Padaccheda

| Saṃhitā form | Padaccheda | Grammar | Working meaning |
|---|---|---|---|
| spraṣṭavyam | spraṣṭavyam | nom./acc.sg.n | tangible / touchable domain |
| dvividham | dvi-vidham | nom./acc.sg.n | twofold |
| śeṣāḥ | śeṣāḥ | nom.pl.m | the remaining ones |
| rūpiṇaḥ | rūpiṇaḥ | nom.pl.m | form-bearing, material |
| nava | nava | numeral | nine |
| bhautikāḥ | bhautikāḥ | nom.pl.m | derivative-material; dependent on the great elements |
| dharmadhātvekadeśaḥ | dharma-dhātu-eka-deśaḥ | nom.sg.m | one part of the dharma-domain |
| ca | ca | particle | and |
| saṃcitāḥ | saṃcitāḥ | nom.pl.m | accumulated, aggregated |
| daśa | daśa | numeral | ten |
| rūpiṇaḥ | rūpiṇaḥ | nom.pl.m | form-bearing, material |

## 4. Grammar

### spraṣṭavyaṃ dvividham

The tangible domain is **twofold**. It includes both the great elements themselves and the tangible qualities derived from them.

```text
spraṣṭavya
    = mahābhūta
    + derivative tangible qualities
```

### śeṣā rūpiṇo nava bhautikāḥ

The remaining nine material domains are **bhautikāḥ**, derivative-material. They are material, but they are not the great elements themselves. They depend upon the great elements.

These nine are:

```text
five sense-faculty domains:
    cakṣus, śrotra, ghrāṇa, jihvā, kāya

four object-domains other than touch:
    rūpa, śabda, gandha, rasa
```

### dharmadhātvekadeśaś ca

A part of the dharma-domain is also form-bearing. This is the place of **avijñapti-rūpa**, non-disclosive form. The dharma-domain is therefore not simply mental or abstract; it includes a subtle material determination.

### saṃcitā daśa rūpiṇaḥ

The ten form-bearing domains are **saṃcita**, accumulated or aggregated. Materiality is here treated as built-up determinate formation, not as isolated inert stuff.

## 5. Literal Translation

> The tangible is twofold. The remaining nine form-bearing domains are derivative-material. And one part of the dharma-domain [is form-bearing]. The ten form-bearing domains are accumulated.

## 6. Philosophical Translation

> The tangible domain is internally doubled: it includes the great elements and what is derived from them. The other nine material domains are derivative materialities. A portion of the dharma-domain is also form-bearing, namely subtle non-disclosive form. The ten material domains are accumulated formations rather than self-enclosed simples.

Hegel-clean working rendering:

> Materiality is not flat immediacy. The tangible is the place where materiality shows its double structure: elemental basis and derivative formation. The remaining material domains are derivative from this basis, and even the dharma-domain contains a subtle material moment. Thus rūpa is accumulated determinate formation.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| spraṣṭavya | tangible / touchable | internally twofold |
| dvi-vidha | twofold | elemental and derivative modes |
| rūpiṇ | form-bearing / material | possessing rūpa |
| bhautika | derivative-material | dependent on the great elements |
| mahābhūta | great element | material basis |
| dharmadhātvekadeśa | one part of the dharma-domain | especially avijñapti-rūpa |
| avijñapti-rūpa | non-disclosive form | subtle form included in dharmadhātu |
| saṃcita | accumulated / aggregated | composite material formation |

## 8. Logical Determination

VAK_1.35 continues the movement from object-support and appropriation into material constitution.

```text
VAK_1.34
    object-support and appropriation

VAK_1.35
    material constitution and accumulation
```

The structure is:

```text
Touchable domain
    = elemental + derivative

Remaining nine material domains
    = derivative from great elements

Part of dharma-domain
    = subtle form / avijñapti-rūpa

Ten material domains
    = accumulated form-bearing formations
```

This gives a precise distinction:

```text
rūpa
    ≠ mere visible form
    ≠ inert physical stuff

rūpa
    = form-bearing determinate materiality
    = accumulated formation grounded in elemental conditions
```

## 9. Interpretive Note

VAK_1.35 deepens the analysis from embodiment to constitution. The material domain is not a simple given. It is generated through the relation between elemental basis, derivative materiality, and accumulation.

The tangible domain is privileged because it includes the great elements themselves. Touch is therefore not merely one object-domain among others. It is the domain in which materiality discloses its elemental basis.

The inclusion of **dharmadhātvekadeśa** prevents the dharma-domain from being treated as purely mental or abstract. The dharma-domain includes subtle material determination: **avijñapti-rūpa**.

Organon sequence:

```text
Elemental basis
    ↓
Derivative materiality
    ↓
Accumulated form-bearing structure
```

This follows directly from 1.34:

```text
object-support
    does not yet equal embodiment

embodiment
    requires appropriation

materiality
    requires accumulated form-bearing determination
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_35
    a vak:Karika ;
    rdfs:label "VAK 1.35" ;
    vak:hasIAST "spraṣṭavyaṃ dvividhaṃ śeṣā rūpiṇo nava bhautikāḥ / dharmadhātvekadeśaś ca saṃcitā daśa rūpiṇaḥ" ;
    vak:hasTopic vak:MaterialConstitution ;
    vak:belongsTo vak:Dhatunirdesa .

vak:MaterialConstitution
    a vak:LogicalDetermination ;
    rdfs:label "material constitution" ;
    vak:distinguishes vak:ElementalMateriality , vak:DerivativeMateriality , vak:AccumulatedMateriality .

vak:SprastavyaDhatu
    a vak:ObjectDomain ;
    rdfs:label "tangible-domain" ;
    vak:sanskrit "spraṣṭavya-dhātu" ;
    vak:hasMode vak:ElementalTangible ;
    vak:hasMode vak:DerivativeTangible .

vak:BhautikaMaterialDomain
    a vak:DomainClass ;
    rdfs:label "derivative-material domain" ;
    vak:sanskrit "bhautika" ;
    vak:dependsOn vak:MahaBhuta .

vak:DharmaDhatuMaterialPart
    a vak:DomainPart ;
    rdfs:label "material part of the dharma-domain" ;
    vak:partOf vak:DharmaDhatu ;
    vak:identifiedWith vak:AvijnaptiRupa .

vak:AvijnaptiRupa
    a vak:SubtleMaterialDetermination ;
    rdfs:label "non-disclosive form" ;
    vak:sanskrit "avijñapti-rūpa" ;
    vak:belongsTo vak:DharmaDhatu .

vak:TenRupinDomains
    a vak:DomainGroup ;
    rdfs:label "ten form-bearing domains" ;
    vak:hasCount 10 ;
    vak:hasDetermination vak:AccumulatedMateriality .
```

## 11. Commit History

- Added full Organon analysis for VAK_1.35.
- Establishes **spraṣṭavya** as the internally twofold tangible domain.
- Distinguishes **mahābhūta** from **bhautika** materiality.
- Includes **dharmadhātvekadeśa** as the material part of the dharma-domain, especially **avijñapti-rūpa**.
- Establishes **saṃcita** as accumulated form-bearing materiality.
- Continues the movement from object-support and appropriation in VAK_1.34 to material constitution in VAK_1.35.
