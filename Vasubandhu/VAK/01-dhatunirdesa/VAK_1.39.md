# VAK_1.39

## 1. Sanskrit (Devanāgarī)

> द्वादशाध्यात्मिकाः हित्वा रूपादीन् धर्मसंज्ञकः ।
>
> सभागः तत्सभागाश्च शेषाः यो न स्वकर्मकृत् ॥ १.३९ ॥

## 2. Sanskrit (IAST)

> dvādaśādhyātmikāḥ hitvā rūpādīn dharmasaṃjñakaḥ /
>
> sabhāgaḥ tatsabhāgāś ca śeṣāḥ yo na svakarmakṛt // VAkK_1.39 //

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| dvādaśādhyātmikāḥ | dvādaśa adhyātmikāḥ | twelve are internal |
| hitvā | hitvā | excluding, having left aside |
| rūpādīn | rūpa-ādīn | those beginning with rūpa |
| dharmasaṃjñakaḥ | dharma-saṃjñakaḥ | the one called dharma |
| sabhāgaḥ | sa-bhāgaḥ | functioning member, active class-member |
| tat-sabhāgāḥ | tat-sabhāgāḥ | corresponding non-functioning members |
| śeṣāḥ | śeṣāḥ | the remaining ones |
| yaḥ na svakarmakṛt | yaḥ na sva-karma-kṛt | that which does not perform its own function |

## 4. Grammar

The first half marks the **twelve internal domains**. From the eighteen domains, exclude the six external object-domains:

```text
rūpa, śabda, gandha, rasa, spraṣṭavya, dharma
```

The remaining twelve are internal:

```text
six faculty-domains
    cakṣus, śrotra, ghrāṇa, jihvā, kāya, manas

six knowledge-domains
    cakṣurvijñāna, śrotravijñāna, ghrāṇavijñāna,
    jihvāvijñāna, kāyavijñāna, manovijñāna
```

The second half introduces **sabhāga** and **tat-sabhāga**. The compression is severe, but the working sense is:

```text
sabhāga
    = a member that performs its own function

 tat-sabhāga
    = a corresponding member that belongs to the class
      but does not presently perform its own function
```

## 5. Literal Translation

> The twelve are internal, after excluding those beginning with rūpa and the one called dharma. The remaining [domains] are sabhāga and tat-sabhāga; that which does not perform its own function is tat-sabhāga.

## 6. Philosophical Translation

> The eighteen domains divide into twelve internal domains and six external object-domains. The internal domains are the faculties and knowledge-domains; the external domains are the objects beginning with rūpa and ending with dharma. A further distinction then separates domains that actively perform their own function from corresponding members that belong to the same order but are not presently functioning.

Organon rendering:

> A domain is not defined merely by membership in a list. It is defined by whether it is internal or external, and whether it is functionally actual. Sabhāga is active participation in proper function; tat-sabhāga is class-membership without present operation.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| adhyātmika | internal | faculty and knowledge side of the domain-system |
| rūpādi | beginning with rūpa | the external object-domains |
| dharmasaṃjñaka | called dharma | dharmadhātu as the sixth external object-domain |
| sabhāga | functioning member | performs its own function |
| tat-sabhāga | corresponding non-functioning member | belongs but is not presently active |
| sva-karma | own function | characteristic work of a domain |
| svakarmakṛt | performing its own function | functionally actual |

## 8. Logical Determination

VAK_1.38 introduced acquisition. VAK_1.39 adds internality and functional actuality.

```text
Internal twelve
    = six faculties + six knowledge-domains

External six
    = five object-domains + dharmadhātu

sabhāga
    = belongs and functions

tat-sabhāga
    = belongs but does not presently function
```

This distinction is powerful:

```text
membership
    ≠
actual function
```

A domain can be a real member of a class without presently exercising its proper work.

## 9. Interpretive Note

The verse prevents the dhātu-system from becoming a static table. A domain is now determined not only by object-support, appropriation, material constitution, operation, causal genesis, and acquisition, but also by **functional actuality**.

The twelve internal domains are not merely subjective. They are internal because they form the faculty-and-knowledge side of the system. The six external domains are object-domains, including dharmadhātu as the object-domain for manas.

This is compatible with the higher Organon note that dharmadhātu has real-domain status. In the eighteen-domain analysis it functions as the sixth external object-domain; in the deeper theological-logical analysis it is the Island of Truth, the domain of real determination.

Organon sequence:

```text
1.34 object-support / appropriation
1.35 material constitution
1.36 material operation
1.37 causal genesis
1.38 modal status and acquisition
1.39 internality and functional actuality
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_39
    a vak:Karika ;
    rdfs:label "VAK 1.39" ;
    vak:hasIAST "dvādaśādhyātmikāḥ hitvā rūpādīn dharmasaṃjñakaḥ / sabhāgaḥ tatsabhāgāś ca śeṣāḥ yo na svakarmakṛt" ;
    vak:hasTopic vak:InternalExternalAndFunctionalActuality ;
    vak:belongsTo vak:Dhatunirdesa .

vak:InternalTwelveDomains
    a vak:DomainGroup ;
    rdfs:label "twelve internal domains" ;
    vak:hasCount 12 ;
    vak:includes vak:SixFacultyDomains ;
    vak:includes vak:SixKnowledgeDomains .

vak:ExternalSixDomains
    a vak:DomainGroup ;
    rdfs:label "six external object-domains" ;
    vak:hasCount 6 ;
    vak:beginsWith vak:RupaDhatu ;
    vak:endsWith vak:DharmaDhatu .

vak:Sabhaga
    a vak:FunctionalStatus ;
    rdfs:label "sabhāga" ;
    vak:rendering "functioning member" .

vak:Tatsabhaga
    a vak:FunctionalStatus ;
    rdfs:label "tat-sabhāga" ;
    vak:rendering "corresponding non-functioning member" .

vak:SvaKarma
    a vak:DomainFunction ;
    rdfs:label "own function" ;
    vak:sanskrit "sva-karma" .
```

## 11. Commit History

- Added Organon analysis for VAK_1.39.
- Establishes the twelve internal domains as six faculties plus six knowledge-domains.
- Establishes the external six as object-domains beginning with rūpa and ending with dharma.
- Introduces **sabhāga** as functionally active class-membership.
- Introduces **tat-sabhāga** as class-membership without present operation.
- Adds functional actuality to the chapter sequence after acquisition.
