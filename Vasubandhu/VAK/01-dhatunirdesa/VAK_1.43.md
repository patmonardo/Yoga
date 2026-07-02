# VAK_1.43

## 1. Sanskrit (Devanāgarī)

> उभाभ्यामपि चक्षुर्भ्यां पश्यति व्यक्तदर्शनात् ।
>
> चक्षुःश्रोत्रमनोऽप्राप्तविषयं त्रयमन्यथा ॥ १.४३ ॥

## 2. Sanskrit (IAST)

> ubhābhyām api cakṣurbhyāṃ paśyati vyaktadarśanāt /
>
> cakṣuḥśrotramano 'prāptaviṣayaṃ trayam anyathā // VAkK_1.43 //

Source saṃhitā form:

> ubhābhyāmapi cakṣurbhyāṃ paśyati vyaktadarśanāt /
>
> cakṣuḥśrotramano 'prāptaviṣayaṃ trayamanyathā // VAkK_1.43 //

## 3. Padaccheda

| Form | Padaccheda | Meaning |
|---|---|---|
| ubhābhyām api | ubhābhyām api | with both also |
| cakṣurbhyām | cakṣurbhyām | with the two eyes |
| paśyati | paśyati | one sees |
| vyakta-darśanāt | vyakta-darśanāt | because of clear seeing |
| cakṣuḥ-śrotra-manas | cakṣuḥ-śrotra-manas | eye, ear, mind |
| aprāpta-viṣayam | a-prāpta-viṣayam | having an unreached / non-contact object |
| trayam | trayam | triad |
| anyathā | anyathā | otherwise |

## 4. Grammar

The first half says that one sees with both eyes because vision is clearer when both eyes are functioning.

The second half classifies three domains:

```text
cakṣus
śrotra
manas
```

These have **aprāpta-viṣaya**, objects not reached by direct physical contact.

The remaining three sensory faculties are otherwise:

```text
ghrāṇa
jihvā
kāya
```

Smell, taste, and touch operate through contact with the object.

## 5. Literal Translation

> One sees with both eyes also, because of clear seeing. Eye, ear, and mind are a triad whose objects are not reached; the others are otherwise.

## 6. Philosophical Translation

> Vision may operate through both eyes, since seeing is clearer in that way. Eye, ear, and mind apprehend objects without direct contact, while smell, taste, and touch operate otherwise, through contact with their objects.

Organon rendering:

> The faculties are not uniform. Some disclose at a distance; others require contact. Eye, ear, and mind operate through non-contact relation; smell, taste, and touch require object-contact. The domain-system therefore distinguishes distance-disclosure from contact-disclosure.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Note |
|---|---|---|
| ubhābhyām cakṣurbhyām | with both eyes | binocular clarity |
| vyakta-darśana | clear seeing | explicit visual disclosure |
| aprāpta-viṣaya | non-contact object | object not physically reached by the faculty |
| cakṣus | eye-domain | non-contact object-domain |
| śrotra | ear-domain | non-contact object-domain |
| manas | mind-domain | non-contact dharma-object relation |
| anyathā | otherwise | contact-object faculties |

## 8. Logical Determination

VAK_1.42 assigned seeing to the functioning eye. VAK_1.43 now distinguishes modes of object-relation.

```text
non-contact object-relation:
    eye
    ear
    mind

contact object-relation:
    nose
    tongue
    body
```

This gives a new axis:

```text
distance-disclosure
    vs.
contact-disclosure
```

Mind is grouped with eye and ear because manas takes dharma as object without physical contact.

## 9. Interpretive Note

This verse expands the logic of ālambana. Object-support does not always mean contact. Some domains disclose objects across distance or non-contact relation.

The inclusion of manas in the non-contact triad is crucial. Mind does not grasp dharma by touching it. It apprehends determinations through a non-contact object-support.

Organon sequence:

```text
1.41 seeing requires ascertainment
1.42 seeing belongs to functional faculty
1.43 faculties differ by contact-mode
```

Kant-Fichte-Hegel note:

```text
object-relation
    is not one flat relation

it has modes:
    contact
    distance
    non-sensible determination
```

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_43
    a vak:Karika ;
    rdfs:label "VAK 1.43" ;
    vak:hasIAST "ubhābhyām api cakṣurbhyāṃ paśyati vyaktadarśanāt / cakṣuḥśrotramano 'prāptaviṣayaṃ trayam anyathā" ;
    vak:hasTopic vak:ContactAndNonContactObjectRelation ;
    vak:belongsTo vak:Dhatunirdesa .

vak:NonContactTriad
    a vak:DomainGroup ;
    rdfs:label "non-contact object triad" ;
    vak:hasMember vak:CaksusDhatu ;
    vak:hasMember vak:SrotraDhatu ;
    vak:hasMember vak:ManoDhatu .

vak:ContactTriad
    a vak:DomainGroup ;
    rdfs:label "contact object triad" ;
    vak:hasMember vak:GhranaDhatu ;
    vak:hasMember vak:JihvaDhatu ;
    vak:hasMember vak:KayaDhatu .
```

## 11. Commit History

- Added Organon analysis for VAK_1.43.
- Establishes binocular clarity as explanation of seeing with both eyes.
- Distinguishes eye, ear, and mind as non-contact object domains.
- Distinguishes nose, tongue, and body as contact-object domains.
- Adds contact-mode to the chapter sequence.
