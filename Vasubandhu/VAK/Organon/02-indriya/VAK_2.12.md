# VAK_2.12

## 1. Sanskrit (Devanāgarī)

> कामाप्तममलं हित्वा रूपाप्तं स्त्रीपुमिन्द्रिये ।
>
> दुःखे च हित्वा आरूप्याप्तं सुखे चापोह्य रूपि च ॥ २.१२ ॥

## 2. Sanskrit (IAST)

> kāmāptam amalaṃ hitvā rūpāptaṃ strīpumindriye /
>
> duḥkhe ca hitvā ārūpyāptaṃ sukhe cāpohya rūpi ca // 2.12 //

## 3. Padaccheda

```text
kāmāptam           → kāma-āptam
amalaṃ hitvā       → amalam hitvā
rūpāptam           → rūpa-āptam
strīpumindriye     → strī-pum-indriye
duḥkhe ca hitvā    → duḥkhe ca hitvā
ārūpyāptam         → ārūpya-āptam
sukhe ca apohya    → sukhe ca apohya
rūpi ca            → rūpi ca
```

| Form | Morphology | Lexical force here |
|---|---|---|
| kāma-āptam | nominative neuter singular | connected with or belonging to the desire realm |
| amalam | accusative neuter singular | the stainless triad, treated collectively |
| hitvā | absolutive | having excluded / leaving aside |
| rūpa-āptam | nominative neuter singular | connected with or belonging to the form realm |
| strī-pum-indriye | accusative neuter dual | female and male faculties |
| duḥkhe | accusative neuter dual | the two painful faculties: pain and distress |
| ārūpya-āptam | nominative neuter singular | connected with or belonging to the formless realm |
| sukhe | accusative neuter dual | the two pleasant faculties: pleasure and gladness |
| apohya | absolutive | having removed / excluded |
| rūpi | accusative neuter singular of `rūpin`, collective here | what possesses form; the material faculties |
| ca | conjunction | and |

Both `duḥkhe` and `sukhe` are dual. The Bhāṣya identifies their members:

```text
duḥkhe
    = duḥkha + daurmanasya

sukhe
    = sukha + saumanasya
```

## 4. Grammar

The verse gives three nested exclusion rules. The first is:

```text
amalaṃ hitvā kāmāptam
    → excluding the stainless triad,
      [the remaining faculties may be] desire-realm-connected
```

The Bhāṣya explains that the triad is `apratisaṃyukta`, unconnected with any
realm, because it is exclusively without outflows.

The form-realm rule carries the first exclusion forward:

```text
[amalaṃ] strī-pum-indriye duḥkhe ca hitvā rūpāptam
    → excluding the stainless triad,
      female and male faculties,
      and pain and distress,
      [the remainder may be] form-realm-connected
```

The formless-realm rule carries all previous exclusions forward and adds two
more groups:

```text
[amalaṃ strī-pum-indriye duḥkhe ca hitvā]
sukhe ca rūpi ca apohya
ārūpyāptam

    → excluding also pleasure, gladness,
      and the material faculties,
      [the remainder may be] formless-realm-connected
```

The syntax describes possible realm-connection. It does not say that every
listed faculty must occur in every being of that realm.

## 5. Translation

### Close syntactic construe

> Excluding the stainless [triad], [the remainder may be] desire-realm-connected. Excluding [that triad], the female and male faculties, and the two painful faculties, [the remainder may be] form-realm-connected. Excluding also the two pleasant faculties and what possesses form, [the remainder may be] formless-realm-connected.

### Bhāṣya-informed translation

> Nineteen faculties—the twenty-two apart from the three stainless realization-faculties—can be connected with the desire realm. Fifteen can be connected with the form realm, which additionally excludes the female and male faculties and the faculties of pain and distress. Eight can be connected with the formless realm: mind, life, neutral feeling, and the five beginning with confidence. The three realization-faculties are not connected with any realm.

The counts are:

```text
desire realm:
    22 - 3 = 19

form realm:
    22 - 3 - 2 - 2 = 15

formless realm:
    mind + life + neutral feeling + five path faculties = 8
```

## 6. Philosophical Translation

> Realm-connection constrains which governing faculties can be realized within a given mode of existence. The desire realm permits every realm-connected faculty. The refined embodiment and tranquillity of the form realm exclude sexual differentiation, bodily pain, and mental distress. The formless realm removes every material faculty and both pleasant faculties, leaving only mind, continuity, neutral feeling, and the five faculties that equip the path. The stainless realization-faculties are not members of a superior realm; they are unbound from all three.

Organon rendering:

> The Agent has realm-specific admissible configurations. A realm is not merely an address attached to an otherwise unchanged process: its conditions enable some faculty-operations and exclude others. The formless profile is a minimal nonmaterial configuration, while the stainless realization-operation is realm-unbound rather than another member of that profile.

The language of Agent profiles is a project reconstruction. The text
classifies faculties by `pratisaṃyoga`, connection with the three realms.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| kāmāpta / kāma-pratisaṃyukta | desire-realm-connected | capable of connection with the desire realm |
| rūpāpta / rūpa-pratisaṃyukta | form-realm-connected | capable of connection with the form realm |
| ārūpyāpta / ārūpya-pratisaṃyukta | formless-realm-connected | capable of connection with the formless realm |
| apratisaṃyukta | realm-unconnected | Bhāṣya determination of the stainless realization triad |
| amala-traya | stainless triad | three realization-faculties, excluded from all realm-connection |
| strī-pum-indriye | female and male faculties | absent in the form and formless realms |
| duḥkhe | two painful faculties | pain and distress |
| sukhe | two pleasant faculties | pleasure and gladness |
| rūpin | possessing form | seven material faculties collectively |
| maithuna-dharma-vairāgya | freedom from sexual activity | Bhāṣya reason for absence of sex faculties in the form realm |
| acchatva | clarity / refinement | quality of the form-realm bodily basis used to explain absence of pain |
| śamatha-snigdha-santāna | continuum softened by tranquillity | Bhāṣya reason for absence of distress |
| āghāta-vastu | basis for resentment | absent in the form realm according to the Bhāṣya |

Realm-connection and outflow-status remain distinct. A twofold faculty such
as confidence may have a realm-connected instance when with outflows and a
realm-unconnected instance when without outflows.

## 8. Logical Determination

The realm profiles are:

```text
DesireRealmCompatible
    = TwentyTwoFaculties
      - ThreeRealizationFaculties

Count(DesireRealmCompatible) = 19
```

```text
FormRealmCompatible
    = DesireRealmCompatible
      - FemaleFaculty
      - MaleFaculty
      - PainFaculty
      - DistressFaculty

Count(FormRealmCompatible) = 15
```

```text
FormlessRealmCompatible
    = {Mind,
       Life,
       NeutralFeeling,
       Confidence,
       Energy,
       Recollection,
       Concentration,
       Prajna}

Count(FormlessRealmCompatible) = 8
```

The stainless triad forms another status, not a fourth realm-profile:

```text
For each f in ThreeRealizationFaculties:
    RealmConnection(f) = None
```

Compatibility does not imply universal occurrence:

```text
RealmCompatible(f, r)
    ↛ OccursInEveryBeing(f, r)
```

Nor does a faculty-name alone settle realm-connection across every mode:

```text
TwofoldOutflowStatus(f)
    → RealmConnectionDependsOn(InstanceMode(f))

Anasrava(f)
    → RealmUnconnected(f)
```

The formless profile is minimal only with respect to this twenty-two-faculty
classification:

```text
FormlessRealmCompatible
    = CognitiveCoordination
    + LifeContinuity
    + NeutralFeeling
    + FivePathEquipmentFaculties
```

## 9. Interpretive Note

VAK 2.12 adds realm-connection to the growing multidimensional account of a
faculty. The same `indriya` system has now been classified by function,
affective character, path-stage, outflow-status, maturation-status, future
productivity, ethical quality, and realm-compatibility.

The three realization-faculties require the first distinction. They are not
desire-, form-, or formless-realm faculties. Their exclusive without-outflow
status makes them `apratisaṃyukta`, unconnected with every realm. The ascent
through realms must therefore not be confused with the path's realization-
faculties. A higher conditioned realm is still not the stainless Path.

The form realm is not described merely by subtraction of coarse organs. Its
faculty profile expresses an integrated mode of existence. The Bhāṣya links
the absence of pain to refinement of the bodily basis and absence of
unwholesome activity. It links the absence of distress to a continuum softened
by tranquillity and the absence of a basis for resentment. Realm-conditions
alter both embodiment and affective possibility.

The formless realm retains eight faculties:

```text
mind
life
neutral feeling
confidence
energy
recollection
concentration
prajñā
```

This is a minimal faculty configuration for cognitive coordination,
continuity, neutral experience, and path-equipment without material faculties.
Yet it is not identical with the stainless Agent. The five path-equipment
faculties are twofold; only their without-outflow operation is realm-unbound.

For the Agent architecture, the rule is:

```text
validate a proposed faculty configuration against
    the conditions of its execution-realm

but do not confuse
    realm compatibility
with
    realization or purity
```

This gives the Samyama-bhūmi hypothesis an important boundary. Bhūmi may
constrain an Agent's available faculties, but realization cannot be reduced
to residence in a subtler conditioned level. This is a Yoga–Organon
comparison; the Kośa's textual claim is the realm-distribution above.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_12
    a vak:Karika ;
    rdfs:label "VAK 2.12" ;
    vak:hasTopic vak:RealmCompatibility ;
    vak:belongsTo vak:Indriyanirdesa .

vak:DesireRealmProfile
    vak:allowsFacultySet vak:DesireRealmCompatible ;
    vak:hasCount 19 .

vak:FormRealmProfile
    vak:allowsFacultySet vak:FormRealmCompatible ;
    vak:hasCount 15 ;
    vak:excludes vak:FemaleFaculty,
        vak:MaleFaculty,
        vak:PainFaculty,
        vak:DistressFaculty .

vak:FormlessRealmProfile
    vak:allows vak:MindFaculty,
        vak:LifeFaculty,
        vak:NeutralFeelingFaculty,
        vak:ConfidenceFaculty,
        vak:EnergyFaculty,
        vak:RecollectionFaculty,
        vak:ConcentrationFaculty,
        vak:PrajnaFaculty ;
    vak:hasCount 8 .

vak:ThreeRealizationFaculties
    vak:hasRealmConnection vak:None ;
    vak:hasOutflowStatus vak:ExclusivelyAnasrava .

organon:RealmConstrainedAgentProfile
    a organon:InterpretiveReconstruction ;
    organon:constrains vak:FacultyConfiguration ;
    organon:variesBy vak:RealmConnection ;
    organon:inferredFrom vak:RealmCompatibility .
```
