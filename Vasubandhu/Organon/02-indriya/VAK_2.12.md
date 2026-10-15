# VAK_2.12 — Realm-Connection

## 1. Sanskrit (Devanāgarī)

> कामाप्तममलं हित्वा रूपाप्तं स्त्रीपुमिन्द्रिये ।
>
> दुःखे च हित्वा आरूप्याप्तं सुखे चापोह्य रूपि च ॥ २.१२ ॥

## 2. Sanskrit (IAST)

> kāmāptam amalaṃ hitvā rūpāptaṃ strīpumindriye /
>
> duḥkhe ca hitvā ārūpyāptaṃ sukhe cāpohya rūpi ca // 2.12 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| kāma-āptam | nominative | desire-realm-connected |
| amalam hitvā | absolutive | excluding the stainless triad |
| rūpa-āptam | nominative | form-realm-connected |
| strī-pum-indriye | dual | female and male |
| duḥkhe | dual | pain and distress |
| ārūpya-āptam | nominative | formless-realm-connected |
| sukhe | dual | pleasure and gladness |
| apohya | absolutive | having removed |
| rūpi | accusative | what possesses form |

Both duals are exclusions, not locatives. The earlier exclusions carry forward.

## 4. Grammar

```text
excluding the stainless triad
    → desire-realm-connected
    19

excluding also female, male, pain, distress
    → form-realm-connected
    15

excluding also pleasure, gladness, and what possesses form
    → formless-realm-connected
    mind, life, neutral feeling, five beginning with faith
    8

triad
    → unconnected with any realm
```

Connection is possible affiliation. It is not occurrence in every being of that realm.

## 5. Translation

### Literal Translation

Excluding the stainless, desire-realm-connected. Excluding the female and male faculties and the two painful faculties, form-realm-connected. Excluding also the two pleasant faculties and what possesses form, formless-realm-connected.

### Bhāṣya-informed study translation

Which faculty is connected with which realm? Excluding the exclusively without-outflow triad beginning with “I shall know,” the rest are connected with the desire realm. That triad is entirely unconnected.

Form-realm-connected, excluding also female and male, and pain and distress. The triad-exclusion continues. Female and male are absent because of dispassion toward sexual intercourse, and because they would be unattractive. How, then, are those beings called males? In the sūtra: it is impossible that a woman should occupy the status of Brahmā. It is possible that a man should. The male-being of men in the desire realm is different. Pain is absent because of the clarity of the support and the absence of the unwholesome. Distress is absent because the continuum is softened by tranquillity, and because bases for resentment are absent.

Formless-realm-connected, removing also pleasure and gladness, and what possesses form. The earlier exclusions continue. What remains is mind, life, neutral feeling, and the five beginning with faith. These, and no others, are found connected with the formless realm.

## 6. Philosophical Translation

Realm-connection is a further axis. Desire admits nineteen. Form excludes sexual differentiation and the two painful faculties. Formless excludes the pleasant faculties and everything that possesses form, and leaves eight: mind, life, neutral feeling, and the five that equip the path. The triad is not a higher realm. It is unconnected with all three.

Organon rendering:

Another predicate the platform has to hold. Realm is not occurrence, not ethical quality, not outflow, not the path. A higher conditioned realm is not stainless. The five can be connected when with outflows, and unconnected when without. Not the verse English.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| kāmāpta | desire-realm-connected | nineteen |
| rūpāpta | form-realm-connected | fifteen |
| ārūpyāpta | formless-realm-connected | eight |
| apratisaṃyukta | unconnected | the triad |
| duḥkhe | pain and distress | dual |
| sukhe | pleasure and gladness | dual; not pleasure alone |
| rūpin | possessing form | the seven; not the form realm |
| maithuna-dharma-vairāgya | dispassion toward intercourse | one reason |
| acchatva | clarity of the support | why pain is absent |
| āghāta-vastu | basis for resentment | absent in the form realm |

## 8. Logical Determination

```text
desire
    = 22 - 3
    = 19

form
    = 19 - female - male - pain - distress
    = 15

formless
    = mind, life, neutral feeling, five
    = 8
    fifteen - five remaining of form - two pleasant

triad
    → no realm-connection

compatible
    ↛ occurs in every being
without outflows
    → unconnected
twofold type
    → connection depends on the instance
```

## 9. Interpretive Note

The axes now include function, feeling, path-name, outflow, maturation, what produces maturation, ethical quality, and realm-connection. None settles the others.

The male of the sūtra is not the male faculty. The reply distinguishes desire-realm male-being and does not specify the other characteristic. Social, symbolic, or anatomical would exceed the sentence. Unattractive is the text's second reason. It does not replace dispassion.

Pain and distress have separate reasons. Clarity and absence of the unwholesome. Tranquillity, and no basis for resentment. Not one claim that a subtler realm is simply happier.

The eight are not a minimum theory of mind, and not liberation. The triad stays unaffiliated with all three.

Organon reading: the platform holds realm as one more predicate. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_12
    a vak:Karika ;
    rdfs:label "VAK 2.12" ;
    vak:hasTopic vak:RealmConnection ;
    vak:belongsTo vak:Indriyanirdesa .

vak:DesireRealm vak:allowsCount 19 .
vak:FormRealm vak:allowsCount 15 .
vak:FormlessRealm vak:allowsCount 8 .
vak:Triad vak:realmConnection vak:None .

organon:RealmAxis
    organon:notThePath true ;
    organon:notTheVerseEnglish true .
```
