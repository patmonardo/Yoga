# VAK_1.2

## 1. Sanskrit (Devanāgarī)

> प्रज्ञामला सानुचराभिधर्मः तत्प्राप्तये यापि च यच्च शास्त्रम् ।
>
> तस्यार्थतोऽस्मिन् समनुप्रवेशात् स चाश्रयोऽस्येत्यभिधर्मकोशम् ॥ १.२ ॥

## 2. Sanskrit (IAST)

> prajñāmalā sānucarābhidharmaḥ tatprāptaye yāpi ca yacca śāstram /
>
> tasyārthato 'smin samanupraveśāt sa cāśrayo 'syety abhidharmakośam // VAkK_1.2 //

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| prajñā amalā | prajñā amalā | stainless principle / discriminative knowing |
| sa-anucarā | sa-anucarā | with its attendants |
| abhidharmaḥ | abhidharmaḥ | Abhidharma |
| tat-prāptaye | tat-prāptaye | for the attainment of that |
| yā api ca | yā api ca | and whatever |
| yat ca śāstram | yat ca śāstram | and whatever treatise |
| tasya arthataḥ | tasya arthataḥ | of that, by meaning |
| asmin samanupraveśāt | asmin samanupraveśāt | because of entering into this |
| saḥ ca āśrayaḥ asya | saḥ ca āśrayaḥ asya | and it is its support |
| iti abhidharmakośam | iti abhidharmakośam | therefore Abhidharmakośa |

## 4. Grammar

The verse defines Abhidharma in two senses:

```text
primary Abhidharma
    = stainless prajñā with its attendants

secondary Abhidharma
    = the śāstra that leads to the attainment of that prajñā
```

The Kośa is called a treasury because the meaning of Abhidharma enters into it and because it serves as a support for Abhidharma.

## 5. Literal Translation

> Stainless prajñā, together with its attendants, is Abhidharma; and whatever treatise is for the attainment of that is also [Abhidharma]. Because the meaning of that enters into this, and because this is its support, it is called Abhidharmakośa.

## 6. Philosophical Translation

> Abhidharma is first of all stainless discriminative principle with its accompanying factors. The treatise is Abhidharma in a derivative sense because it supports the attainment of that principle and contains its meaning.

Organon rendering:

> Abhidharma is not first a book. It is pure prajñā as principle, accompanied by its functional attendants. The śāstra becomes Abhidharma because it shelters and transmits that principle. The Kośa is therefore a treasury of the path to stainless knowing.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| prajñā | principle / discriminative knowing | here stainless, not ordinary cognition |
| amala | stainless | without defilement |
| anucara | attendant | accompanying factors of prajñā |
| abhidharma | Abhidharma | pure prajñā and its supporting śāstra |
| prāpti | attainment | realization of prajñā |
| artha | meaning | meaning-content entering the Kośa |
| āśraya | support | the treatise as support for Abhidharma |
| kośa | treasury | repository/support of Abhidharma |

## 8. Logical Determination

The verse distinguishes:

```text
Abhidharma as reality of knowing
    = stainless prajñā

Abhidharma as doctrine
    = śāstra leading to that prajñā

Kośa
    = support and treasury of that meaning
```

This gives a double structure:

```text
principle
    ↓
attainment
    ↓
śāstric support
```

## 9. Interpretive Note

This verse is decisive for the whole project. Abhidharma is not merely scholastic taxonomy. It is stainless prajñā. The treatise is secondary, but not external: it supports access to that prajñā.

Organon note:

```text
prajñā
    = pure principle

śāstra
    = path-support of principle

kośa
    = treasury in which principle is preserved and made available
```

This gives the authority for reading the chapter as a principial architecture rather than as a catalogue.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_2
    a vak:Karika ;
    rdfs:label "VAK 1.2" ;
    vak:hasIAST "prajñāmalā sānucarābhidharmaḥ tatprāptaye yāpi ca yacca śāstram / tasyārthato 'smin samanupraveśāt sa cāśrayo 'syety abhidharmakośam" ;
    vak:hasTopic vak:DefinitionOfAbhidharma ;
    vak:belongsTo vak:Dhatunirdesa .

vak:Abhidharma
    a vak:PrincipialKnowledge ;
    rdfs:label "Abhidharma" ;
    vak:definedAs vak:StainlessPrajna .
```

## 11. Commit History

- Added first-pass expanded Organon analysis for VAK_1.2.
- Defines Abhidharma as stainless prajñā with attendants.
- Distinguishes primary Abhidharma from supporting śāstra.
- Frames Kośa as treasury/support of Abhidharma's meaning.
