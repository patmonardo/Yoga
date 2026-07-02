# VAK_1.13

## 1. Sanskrit (Devanāgarī)

> पृथिवी वर्णसंस्थानमुच्यते लोकसंज्ञया ।
>
> आपस्तेजश्च वायुस्तु धातुरेव तथापि च ॥ १.१३ ॥

## 2. Sanskrit (IAST)

> pṛthivī varṇasaṃsthānam ucyate lokasaṃjñayā /
>
> āpas tejaś ca vāyus tu dhātur eva tathāpi ca // VAkK_1.13 //

Source label in GRETIL: `VAkK_1.13`. Project-normalized label: `VAkK_1.13`.

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| pṛthivī | pṛthivī | earth |
| varṇa-saṃsthānam | varṇa-saṃsthānam | color and shape/configuration |
| ucyate | ucyate | is called |
| loka-saṃjñayā | loka-saṃjñayā | by worldly designation |
| āpas | āpas | water |
| tejaḥ ca | tejaḥ ca | and fire |
| vāyuḥ tu | vāyuḥ tu | and wind |
| dhātuḥ eva | dhātuḥ eva | just domain |
| tathā api ca | tathā api ca | and likewise |

## 4. Grammar

The verse distinguishes ordinary speech from technical Abhidharma analysis.

Worldly designation calls visible color and shape **earth**:

```text
lokasaṃjñayā
    pṛthivī = varṇa + saṃsthāna
```

But technically, earth, water, fire, and wind are dhātus: functional domains, not merely visible appearances.

## 5. Literal Translation

> Earth is called color-and-shape by worldly designation. But water, fire, and wind likewise are only domains.

## 6. Philosophical Translation

> Ordinary language identifies earth with visible color and configuration, but Abhidharma treats earth, water, fire, and wind as elemental domains rather than as the appearances named by common speech.

Organon rendering:

> The verse separates worldly naming from principial determination. What the world calls earth is visible configuration. What Abhidharma analyzes is the elemental domain: the functional ground of material appearance.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| pṛthivī | earth | worldly name versus technical domain |
| varṇa | color | visible appearance |
| saṃsthāna | configuration / shape | spatial appearance |
| lokasaṃjñā | worldly designation | conventional naming |
| dhātu | domain | technical Abhidharma category |
| āpas / tejas / vāyu | water / fire / wind | functional elemental domains |

## 8. Logical Determination

```text
worldly designation
    = appearance-name

Abhidharma dhātu
    = functional domain
```

Thus:

```text
visible earth
    ≠
earth-domain as functional support
```

## 9. Interpretive Note

This verse is methodologically important. It warns us not to confuse common names with Abhidharma determinations. The world names what appears. Abhidharma analyzes the domain-function behind the appearance.

Organon note:

```text
loka-saṃjñā
    = name at the level of appearance

dhātu
    = principial domain-determination
```

This supports the project rule: dhātu must remain domain, not element in the crude sense.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_13
    a vak:Karika ;
    rdfs:label "VAK 1.13" ;
    vak:hasSourceLabel "VAkK_1.13" ;
    vak:hasProjectLabel "VAkK_1.13" ;
    vak:hasTopic vak:WorldlyDesignationAndDomain ;
    vak:belongsTo vak:Dhatunirdesa .

vak:WorldlyDesignation
    rdfs:label "worldly designation" ;
    vak:notEqualTo vak:DhatuDetermination .
```

## 11. Commit History

- Added expanded Organon analysis for VAK_1.13.
- Distinguishes worldly designation from technical dhātu analysis.
- Reinforces dhātu as domain, not merely element or common-sense substance.
