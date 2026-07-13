# VAK_4d — VAkK_4.66

## 1. Sanskrit — Devanāgarī

विपर्ययात्सुचरितं तदौदारिकसंग्रहात् ।
दश कर्मपथा उक्ता यथायोगं शुभाशुभाः ॥ VAkK_4.66 ॥

## 2. Sanskrit — IAST

viparyayāt sucaritaṃ tad-audārika-saṃgrahāt /
daśa karmapathā uktā yathāyogaṃ śubhāśubhāḥ // VAkK_4.66 //

## 3. Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| viparyayāt | viparyayāt | from the reverse; by opposition |
| sucaritam | su-caritam | good conduct |
| tadaudārika | tat-audārika | the gross forms of that |
| saṃgrahāt | saṃgrahāt | because of inclusion |
| daśa | daśa | ten |
| karmapathāḥ | karma-pathāḥ | courses of karma |
| uktāḥ | uktāḥ | stated |
| yathāyogam | yathā-yogam | as applicable |
| śubhāśubhāḥ | śubhāḥ aśubhāḥ | wholesome and unwholesome |

## 4. Grammar

The first statement is elliptical: good conduct is understood from the reversal of bad conduct. The second explains that the ten karmapathas are obtained by selecting the gross or principal members from the broader conduct-field.

## 5. Literal Translation

By reversal, there is good conduct. Because the gross forms of that are included, ten paths of karma are stated, wholesome and unwholesome as appropriate.

## 6. Philosophical Translation

Good conduct is determined as the contrary of bad conduct. From the wider fields of bodily, verbal, and mental conduct, their more manifest and ethically decisive forms are selected and taught as the ten wholesome and unwholesome courses of karma.

## 7. Technical Vocabulary

- `viparyaya`: reversal, opposition, contrary determination.
- `sucarita`: good conduct, well-conducted activity.
- `audārika`: gross, manifest, sufficiently determinate.
- `saṃgraha`: inclusion, comprehension, grouping.
- `karmapatha`: course of karma, a directed ethical route.
- `yathāyogam`: according to applicability.

## 8. Doctrinal Determination

The verse derives the ten karmapathas from the wider threefold field of conduct. The standard distribution is three bodily, four verbal, and three mental courses. Conduct is the broader field; karmapatha is a selected decisive route within it.

## 9. Logical Determination

The verse performs two operations:

```text
bad conduct
    reversed
        ↓
good conduct

conduct-field
    selective comprehension of gross members
        ↓
ten karmapathas
```

The ten are privileged determinations through which the wider ethical field becomes operationally classifiable.

## 10. Light Organon Interpretation

```text
Conduct
    broad moral state-space

KarmicCourse
    principal directed transition-path
```

Karma becomes intelligible as path: determinate activity receives directionality and becomes discriminable as Path or not-Path.

## 11. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_66
    a vak:Karika ;
    rdfs:label "VAkK 4.66" ;
    vak:continues vak:VAK_4_65 ;
    vak:hasTopic vak:TenKarmicCourses .

vak:KarmicCourse
    rdfs:label "karmapatha" ;
    vak:hasCanonicalTranslation "course of karma" ;
    rdfs:subClassOf vak:Conduct .

vak:TenKarmicCourses
    a vak:CourseClassification ;
    vak:hasMemberCount 10 ;
    vak:drawnFrom vak:ThreefoldConduct ;
    vak:selectionCriterion vak:GrossDetermination .
```

## 12. Commit Note

Committed VAK_4d / VAkK_4.66.

Established:
- good conduct by reversal of bad conduct
- the wider conduct-field versus selected gross members
- ten karmapathas as principal directed courses
- the 3 / 4 / 3 distribution
- karma as directionally classifiable Path / not-Path
