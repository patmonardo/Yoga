# VAK_1.23 — The Order of the Six

## 1. Sanskrit (Devanāgarī)

> प्राक्पञ्च वार्त्तमानार्थ्यात् भौतिकार्थ्याच्चतुष्टयम् ।
>
> दूराशुतरवृत्त्यान्यत् यथास्थानं क्रमोऽथवा ॥ १.२३ ॥॥

## 2. Sanskrit (IAST)

> prāk pañca vārttamānārthyāt bhautikārthyāc catuṣṭayam /
>
> dūrāśutaravṛttyānyat yathāsthānaṃ kramo 'thavā // 1.23 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| prāk | indeclinable | first |
| pañca | numeral | the five, beginning with the eye |
| vārttamāna-arthyāt | ablative | because the object is present |
| bhautika-arthyāt | ablative | because the object is derived form |
| catuṣṭayam | collective | the four |
| dūra-āśutara-vṛttyā | instrumental | by farther or quicker operation |
| anyat | neuter | the remainder |
| yathā-sthānam | adverbial | according to site |
| kramaḥ | nominative singular | the order |
| athavā | particle | an alternative |

The long instrumental is kept. The prose repeats it.

## 4. Grammar

```text
prāk pañca
    vārttamāna-arthyāt

catuṣṭayam
    bhautika-arthyāt
    prāk carries forward

anyat
    dūra-āśutara-vṛttyā

athavā
    yathā-sthānam kramaḥ
```

The commentary orders the six, beginning with the eye, among the essences and the principles. The order of their conditions and of their principles follows that order. It does not say the organs produce the conditions.

## 5. Translation

### Literal Translation

The five come first, because their objects are present. The four, because their objects are derived form. The rest, by farther or quicker operation. Or the order is according to location.

### Bhāṣya-informed study translation

The five Faculties beginning with the eye precede Mind because they take
present Conditions. Of those five, the first four precede Body because their
Conditions are Element-dependent Form. The remaining order follows how far
or how quickly they operate; alternatively, it follows the positions of their
sites in the body.

## 6. Philosophical Translation

Again, two lines. The first is the cut. The second is the remainder, and an alternative.

The five work in the present. That is why they come first. Mind is not that restriction. Some of its objects are present. The rest of the compound is damaged, and it is not repaired. The secure claim is the contrast: present, against an unrestricted range.

Of the five, four take derived form. The body is not restricted that way. Sometimes the great elements, sometimes derived form, sometimes both. *Prāk* carries forward. The four are first among the five, not a new list of six.

Eye and ear take a distant object, so they precede nose and tongue. Of those two, the eye operates farther: a river seen, its sound not heard. Nose and tongue do not operate at a distance. Nose is quicker in the example given: the odor of food before the food reaches the tongue. The phrase is damaged. The example is kept. It is not a measure of speed.

Or the sites. Eye uppermost, then ear, nose, tongue. The body-site clause is damaged. Mind depends on those organs and has no place. That is the alternative. It does not redefine the organ as the gross site.

This closes the base, and only the Form System. The organs and the meanings are ordered here. The Dharma System is not this verse.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| pañca | the five | eye, ear, nose, tongue, body |
| vārttamāna-viṣaya | present object | why the five are first |
| manas | mind | unrestricted range; no place |
| bhautika | derived form | object of the four |
| bhūta | great element | possible object of body |
| dūra-vṛtti | farther operation | eye before ear |
| āśutara-vṛtti | quicker operation | nose before tongue |
| adhiṣṭhāna | site | the alternative; not the organ |
| viṣaya | condition | the object-range; not a finished thing |
| vijñāna | cognition | follows the order of the six; not principle |

## 8. Logical Determination

```text
six, beginning with the eye
    order of conditions and principles follows

five first
    present object
mind
    unrestricted
    compound damaged

four first, among the five
    derived form
body
    element, derived form, or both

eye and ear before nose and tongue
    distant object
eye before ear
    farther: the river
nose before tongue
    quicker: odor before the food arrives
    phrase damaged

alternative
    sites, descending
    body-site clause damaged
    mind depends, and has no place

Form System closed
Dharma System not this verse
1.24 not opened
```

## 9. Interpretive Note

The hinge is *prāk*, then *athavā*. Interpretation of the close of the Form System is in the Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_23 a vak:Karika ;
    vak:hasTopic vak:OrderOfTheSix ;
    vak:belongsTo vak:Dhatunirdesa ;
    vak:closes vak:FormSystem .

vak:FiveOrgans vak:take vak:PresentObject ;
    vak:orderedBefore vak:Mind .
vak:FourOrgans vak:take vak:DerivedForm ;
    vak:orderedBefore vak:BodyOrgan .
vak:LocationOrder vak:alternative true .
```
