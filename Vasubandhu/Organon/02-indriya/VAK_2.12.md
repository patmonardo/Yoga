# VAK_2.12 — Realm-Connection

## 1. Sanskrit (Devanāgarī)

```sanskrit
कामाप्तममलं हित्वा रूपाप्तं स्त्रीपुमिन्द्रिये ।
दुःखे च हित्वा आरूप्याप्तं सुखे चापोह्य रूपि च ॥ २.१२ ॥
```

## 2. Sanskrit (IAST)

```text
kāmāptam amalaṃ hitvā rūpāptaṃ strīpumindriye /
duḥkhe ca hitvā ārūpyāptaṃ sukhe cāpohya rūpi ca // 2.12 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| kāma-āptam | nominative singular neuter adjective | Desire Realm-connected; qualifies the supplied Faculty |
| amalam | accusative singular neuter adjective, substantival | the stainless [triad], excluded by hitvā |
| hitvā | absolutive of √hā | having excluded; used in both first and second clauses |
| rūpa-āptam | nominative singular neuter adjective | Form Realm-connected |
| strī-pum-indriye | accusative dual neuter compound | female and male Faculties, excluded together |
| duḥkhe | accusative dual neuter adjective, substantival | the painful pair: pain and distress |
| ca | coordinating particle, repeated | and; connects exclusions |
| ārūpya-āptam | nominative singular neuter adjective | Formless Realm-connected |
| sukhe | accusative dual neuter adjective, substantival | the pleasant pair: pleasure and gladness |
| apohya | absolutive of apa-√ūh | having removed; governs the added exclusions |
| rūpi | accusative singular neuter adjective, collective in force | what possesses Form; the Form Faculties |

Both duals are exclusions, not locatives. The earlier exclusions carry forward.

**Grammar tokens.** External sandhi is opened, including *ca apohya*.
Compounds remain intact. The Bhāṣya resolves the excluded triad and
pairs without adding their members to the verse stream.

```text
# tokens: kāmāptam amalam hitvā rūpāptam strīpumindriye duḥkhe ca hitvā ārūpyāptam sukhe ca apohya rūpi ca
```

## 4. Grammar

Each clause classifies Faculties by exclusions. The Bhāṣya explicitly
carries the stainless exclusion into the second clause and all prior
exclusions into the third. The inherited exclusions are a prose-resolved
projection, not additional Sanskrit words. Connection here means a type
can have realm-connected instances, not that every instance is so connected.

```nltk-fcfg
% start S
# tokens: kāmāptam amalam hitvā rūpāptam strīpumindriye duḥkhe ca hitvā ārūpyāptam sukhe ca apohya rūpi ca
S[SEM=<(?desire & ?form & ?formless)>] -> DESIRE[SEM=?desire] FORMCLAUSE[SEM=?form] FORMLESS[SEM=?formless]
DESIRE[SEM=<all x.(Faculty(x) -> (?realm(x) <-> -?excluded(x)))>] -> DESIRER[CASE=nom,SEM=?realm] STAINLESS[CASE=acc,SEM=?excluded] OMIT
FORMCLAUSE[INHERITED=stainless,SEM=<all x.(Faculty(x) -> (?realm(x) <-> (-Stainless(x) & -?sex(x) & -?pain(x))))>] -> FORMR[CASE=nom,SEM=?realm] SEX[CASE=acc,NUM=du,CNT=2,SEM=?sex] PAINFUL[CASE=acc,NUM=du,CNT=2,SEM=?pain] AND OMIT
FORMLESS[INHERITED=prior_exclusions,SEM=<all x.(Faculty(x) -> (?realm(x) <-> (-Stainless(x) & -SexFaculty(x) & -PainfulFaculty(x) & -?pleasant(x) & -?form(x))))>] -> FORMLESSR[CASE=nom,SEM=?realm] PLEASANT[CASE=acc,NUM=du,CNT=2,SEM=?pleasant] AND REMOVE FORMF[CASE=acc,SEM=?form] AND
DESIRER[CASE=nom,SEM=<\x.CanConnect(x,desire_realm)>] -> 'kāmāptam'
STAINLESS[CASE=acc,SEM=<\x.Stainless(x)>] -> 'amalam'
OMIT -> 'hitvā'
FORMR[CASE=nom,SEM=<\x.CanConnect(x,form_realm)>] -> 'rūpāptam'
SEX[CASE=acc,NUM=du,CNT=2,SEM=<\x.SexFaculty(x)>] -> 'strīpumindriye'
PAINFUL[CASE=acc,NUM=du,CNT=2,SEM=<\x.PainfulFaculty(x)>] -> 'duḥkhe'
AND -> 'ca'
FORMLESSR[CASE=nom,SEM=<\x.CanConnect(x,formless_realm)>] -> 'ārūpyāptam'
PLEASANT[CASE=acc,NUM=du,CNT=2,SEM=<\x.PleasantFaculty(x)>] -> 'sukhe'
REMOVE -> 'apohya'
FORMF[CASE=acc,SEM=<\x.FormFaculty(x)>] -> 'rūpi'
```

```nltk-dep
'kāmāptam' -> 'amalam' | 'hitvā'
'rūpāptam' -> 'strīpumindriye' | 'duḥkhe' | 'ca' | 'hitvā'
'ārūpyāptam' -> 'sukhe' | 'ca' | 'apohya' | 'rūpi'
```

| Span | Constituent | Result |
|---|---|---|
| [0, 3) | `DESIRE` | stainless triad excluded |
| [3, 8) | `FORMCLAUSE` | triad, sexual pair, and painful pair excluded |
| [8, 14) | `FORMLESS` | earlier exclusions plus pleasant pair and Form Faculties |
| [0, 14) | `S` | three cumulative connection ranges |

## 5. Translation

### Literal Translation

> Excluding the stainless, Desire Realm-connected. Excluding the female and
> male faculties and the two painful faculties, Form Realm-connected.
> Excluding also the two pleasant faculties and what possesses form,
> Formless Realm-connected.

### Bhāṣya-informed study translation

> Except for the stainless triad, the Faculties are connected with the
> desire realm. Excluding the female and male Faculties and the two painful
> Faculties, the remainder are connected with the Form realm. Excluding in
> addition both pleasure and gladness and the Form Faculties, the remainder
> are connected with the Formless realm.

## 6. Philosophical Translation

> The triad is not a higher realm. It is unconnected with all three. A higher conditioned realm is not stainless.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| kāmāpta | Desire Realm-connected | nineteen |
| rūpāpta | Form Realm-connected | fifteen |
| ārūpyāpta | Formless Realm-connected | eight |
| apratisaṃyukta | unconnected | the triad |
| duḥkhe | pain and distress | dual |
| sukhe | pleasure and gladness | dual; not pleasure alone |
| rūpin | possessing form | the seven; not the form realm |
| maithuna-dharma-vairāgya | dispassion toward intercourse | one reason |
| acchatva | clarity of the support | why pain is absent |
| āghāta-vastu | basis for resentment | absent in the form realm |

## 8. Logical Determination

**Kārikā, derived.** The three biconditionals specify possible connection
for Faculty-types, incorporating the Bhāṣya's explicit carry of earlier
exclusions. They do not locate every instance or its bearer in a realm.

```nltk-sem
desire_connection : \x.CanConnect(x,desire_realm)
form_connection : \x.CanConnect(x,form_realm)
formless_connection : \x.CanConnect(x,formless_realm)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.(Faculty(x) -> (CanConnect(x,desire_realm) <-> -Stainless(x))) & all x.(Faculty(x) -> (CanConnect(x,form_realm) <-> (-Stainless(x) & -SexFaculty(x) & -PainfulFaculty(x)))) & all x.(Faculty(x) -> (CanConnect(x,formless_realm) <-> (-Stainless(x) & -SexFaculty(x) & -PainfulFaculty(x) & -PleasantFaculty(x) & -FormFaculty(x)))))

# THEORY prose
# EXPECT prose T
all x.(Stainless(x) -> -exists y.CanConnect(x,y))
all x.(Faculty(x) -> (CanConnect(x,formless_realm) <-> FormlessRemainder(x)))
(PleasantFaculty(pleasure_f) & PleasantFaculty(gladness_f))

# THEORY rejected_gladness_in_formless_range
# EXPECT rejected_gladness_in_formless_range F
CanConnect(gladness_f,formless_realm) & Faculty(gladness_f)

# THEORY rejected_stainless_in_form_range
# EXPECT rejected_stainless_in_form_range F
exists x.(Stainless(x) & CanConnect(x,form_realm))

# THEORY rejected_all_form_faculties_in_form_range
# EXPECT rejected_all_form_faculties_in_form_range F
all x.(FormFaculty(x) -> CanConnect(x,form_realm))
```

```nltk-valuation
desire_realm => desire
form_realm => form
formless_realm => formless
pleasure_f => pleasure
gladness_f => gladness
Faculty => {eye,ear,nose,tongue,body,female,male,life,mind,pain,distress,pleasure,gladness,neutral,faith,vigor,mindfulness,concentration,comprehension,shall_know,knowledge,one_who_has_known}
Stainless => {shall_know,knowledge,one_who_has_known}
SexFaculty => {female,male}
PainfulFaculty => {pain,distress}
PleasantFaculty => {pleasure,gladness}
FormFaculty => {eye,ear,nose,tongue,body,female,male}
FormlessRemainder => {mind,life,neutral,faith,vigor,mindfulness,concentration,comprehension}
CanConnect => {(eye,desire),(ear,desire),(nose,desire),(tongue,desire),(body,desire),(female,desire),(male,desire),(life,desire),(mind,desire),(pain,desire),(distress,desire),(pleasure,desire),(gladness,desire),(neutral,desire),(faith,desire),(vigor,desire),(mindfulness,desire),(concentration,desire),(comprehension,desire),(eye,form),(ear,form),(nose,form),(tongue,form),(body,form),(life,form),(mind,form),(pleasure,form),(gladness,form),(neutral,form),(faith,form),(vigor,form),(mindfulness,form),(concentration,form),(comprehension,form),(mind,formless),(life,formless),(neutral,formless),(faith,formless),(vigor,formless),(mindfulness,formless),(concentration,formless),(comprehension,formless)}
```

The ranges contain 19, 15, and 8 types. Female and male are already
excluded before the final removal of Form Faculties, so that removal
subtracts five further types, not seven again. The model checks the
extension of the classifications, not the causal adequacy of the
reported reasons for absence or the sūtra's male designation.

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): Excluding the stainless triad, which is connected with
no realm, the faculties are connected with the desire realm. Excluding
also the female and male faculties and the two painful faculties, pain and
distress, they are connected with the form realm. Excluding in addition
the two pleasant faculties and whatever possesses form, they are connected
with the formless realm: mind, life, neutral feeling, and the five
beginning with faith, and no others.

The axes now include function, feeling, path-name, outflow, maturation, what produces maturation, ethical quality, and realm-connection. None settles the others.

The male of the sūtra is not the male faculty. The reply distinguishes Desire Realm male-being and does not specify the other characteristic. Social, symbolic, or anatomical would exceed the sentence. Unattractive is the text's second reason. It does not replace dispassion.

Pain and distress have separate reasons. Clarity and absence of the unwholesome. Tranquillity, and no basis for resentment. Not one claim that a subtler realm is simply happier.

The eight are not a minimum theory of mind, and not liberation. The triad stays unaffiliated with all three.

Interpretation: realm-connection is a qualified relation, not a location
assigned indiscriminately to a Faculty, its instances, and its bearer.
The stainless Path is not a fourth or higher conditioned realm.

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

organon:VAK_2_12_Interpretation
    organon:distinguishes vak:PossibleRealmConnection, vak:InstanceOccurrence,
        vak:BearerCircumstances .
```
