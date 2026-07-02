# VAK_1.04

## 1. Sanskrit (Devanāgarī)

> सास्रवानास्रवा धर्माः संस्कृता मार्गवर्जिताः ।
>
> सास्रवाः आस्रवास्तेषु यस्मात्समनुशेरते ॥ १.०४ ॥

## 2. Sanskrit (IAST)

> sāsravānāsravā dharmāḥ saṃskṛtā mārgavarjitāḥ /
>
> sāsravāḥ āsravās teṣu yasmāt samanuśerate // VAkK_1.04 //

Source label in GRETIL: `VAkK_1.4`. Project-normalized label: `VAkK_1.04`.

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| sāsravāḥ | sa-āsravāḥ | with outflows |
| anāsravāḥ | an-āsravāḥ | without outflows |
| dharmāḥ | dharmāḥ | dharmas; determinations/laws |
| saṃskṛtāḥ | saṃskṛtāḥ | conditioned, constructed |
| mārga-varjitāḥ | mārga-varjitāḥ | excluding the path |
| āsravāḥ | āsravāḥ | outflows, taints, influxes |
| teṣu | teṣu | in them |
| yasmāt | yasmāt | because |
| samanuśerate | samanuśerate | they lie latent, adhere, follow along |

## 4. Grammar

The verse introduces the first fundamental division of dharmas:

```text
dharmāḥ
    = sāsrava
    + anāsrava
```

Conditioned dharmas are **sāsrava** when they are **mārga-varjita**, excluding the path. The reason is given by the second half:

```text
āsravāḥ teṣu samanuśerate
    the outflows lie latent in them
```

Thus **sāsrava** does not mean merely empirically existing. It means structurally available to the outflows.

## 5. Literal Translation

> Dharmas are with outflows and without outflows. The conditioned dharmas, excluding the path, are with outflows, because the outflows lie latent in them.

## 6. Philosophical Translation

> Dharmas divide into those permeated by outflow and those free from outflow. Conditioned dharmas, except for the path, are sāsrava because they provide the field in which the outflows adhere and remain latent.

Organon rendering:

> The first doctrinal cut is not material versus mental, but contaminated versus uncontaminated determination. A conditioned domain is sāsrava when it can harbor the outflows. The path is conditioned, yet exceptional, because it is not a support of bondage but the movement of release.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| dharma | determination / law | primary object of Abhidharma analysis |
| sāsrava | with outflows | tainted; a support-field for āsrava |
| anāsrava | without outflows | undefiled; not a field of āsrava |
| āsrava | outflow / taint | that which flows into or adheres to conditioned existence |
| saṃskṛta | conditioned | constructed by grounds/conditions |
| mārga | path | conditioned but not sāsrava |
| samanuśerate | lie latent | anusaya-like adherence within the field |

## 8. Logical Determination

VAK_1.04 gives the first classification after the methodological verses:

```text
dharma
    ↓
sāsrava / anāsrava
```

The decisive point is the exception:

```text
conditioned dharma
    normally = sāsrava

conditioned path
    = anāsrava
```

Thus the path is not outside conditioned occurrence, but it is outside the structure of outflow-bondage.

## 9. Interpretive Note

This verse begins the real architecture of Dhātunirdeśa. The system does not start by asking whether something is material or mental. It asks whether the determination belongs to the field of bondage or to the field free of outflow.

This is foundational for the later path-logic. When VAK_1.40 distinguishes what is abandoned by seeing, by cultivation, and what is not abandoned, that structure already depends on this earlier division:

```text
sāsrava
    = domain where outflows adhere

anāsrava
    = domain free from outflow

mārga
    = conditioned release-function
```

Organon note:

```text
Conditioned appearance is not automatically false.
But where outflows adhere, it becomes bondage-field.
The path is conditioned appearance turned toward release.
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_04
    a vak:Karika ;
    rdfs:label "VAK 1.04" ;
    vak:hasSourceLabel "VAkK_1.4" ;
    vak:hasProjectLabel "VAkK_1.04" ;
    vak:hasTopic vak:SasravaAnasravaDivision ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Sasrava
    a vak:DomainStatus ;
    rdfs:label "with outflows" ;
    vak:sanskrit "sāsrava" .

vak:Anasrava
    a vak:DomainStatus ;
    rdfs:label "without outflows" ;
    vak:sanskrit "anāsrava" .
```

## 11. Commit History

- Replaced interrupted stub with expanded Organon analysis for VAK_1.04.
- Normalized project verse numbering to padded lexical form.
- Establishes the first fundamental division: **sāsrava/anāsrava**.
- Marks the path as conditioned but not sāsrava.
