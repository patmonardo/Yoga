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
% start S
S[REALM=desire] -> Faculty[STAINLESS=false]
S[REALM=form] -> Faculty[STAINLESS=false, SEX=false, PAINFUL=false]
S[REALM=formless] -> Faculty[STAINLESS=false, SEX=false, PAINFUL=false, PLEASANT=false, FORM=false]
S[REALM=none] -> Triad[STAINLESS=true]
```

Exclusions are feature constraints. The triad never unifies with a realm.

## 5. Translation

### Literal Translation

Excluding the stainless, desire-realm-connected. Excluding the female and male faculties and the two painful faculties, form-realm-connected. Excluding also the two pleasant faculties and what possesses form, formless-realm-connected.

### Bhāṣya-informed study translation

> Realm-connection is a further axis. The stainless triad is unconnected with all three. The rest are desire-realm-connected. Form excludes sexual differentiation and the two painful faculties. Formless excludes the pleasant faculties and everything that possesses form, leaving only mind, life, neutral feeling, and the five that equip the path. A higher conditioned realm is not stainless.

## 6. Philosophical Translation

> The triad is not a higher realm. It is unconnected with all three. A higher conditioned realm is not stainless.

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

```python
from nltk.sem.logic import LogicParser
lp = LogicParser()

# Desire-realm connection
desire = lp.parse(r'all x.(Faculty(x) & -Stainless(x) -> DesireConnected(x))')

# Form-realm connection
form = lp.parse(r'all x.(Faculty(x) & -Stainless(x) & -Sex(x) & -Painful(x) -> FormConnected(x))')

# Formless-realm connection
formless = lp.parse(r'all x.(Faculty(x) & -Stainless(x) & -Sex(x) & -Painful(x) & -Pleasant(x) & -Form(x) -> FormlessConnected(x))')

# The triad is unconnected
triad = lp.parse(r'all x.(Triad(x) -> -exists y.RealmConnected(x,y))')

# MetaPlan operator
exclude = lp.parse(r'\P \x.(Faculty(x) & P(x))')
```

The Feature Grammar unifications are open formulas.  
The exclusions are universal quantifiers with negated features.  
The stainless triad never unifies with a realm.  
`exclude` is the relational operator the MetaPlan applies.

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
