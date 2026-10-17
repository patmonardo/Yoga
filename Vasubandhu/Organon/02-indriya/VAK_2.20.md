# VAK_2.20 — The Fewest

## 1. Sanskrit (Devanāgarī)

```sanskrit
सर्वाल्पैर्निःशुभोऽष्टाभिर्विन्मनःकायजीवितैः ।
युक्तो बालस्तथारूप्ये उपेक्षायुर्मनःशुभैः ॥ २.२० ॥
```

## 2. Sanskrit (IAST)

```text
sarvālpair niḥśubho 'ṣṭābhir vinmanaḥkāyajīvitaiḥ /
yukto bālas tathārūpye upekṣāyurmanaḥśubhaiḥ // 2.20 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sarva-alpaiḥ | instrumental | with the fewest |
| niḥ-śubhaḥ | nominative | without the wholesome |
| aṣṭābhiḥ | instrumental | with eight |
| vit | compound | feeling; the five |
| manas, kāya, jīvita | compound | mind, body, life |
| yuktaḥ | nominative | endowed with |
| bālaḥ | nominative | ordinary person |
| tathā ārūpye | locative | likewise, in the formless realm |
| upekṣā-āyus-manas-śubhaiḥ | instrumental | neutral feeling, life, mind, the wholesome |

Niḥśubha is severed wholesome roots. Śubha here is the five beginning with faith, not the three.

## 4. Grammar

```text
% start S
S[MIN=8, WHOLESOME=false] -> FiveFeelings Body Mind Life
S[MIN=8, REALM=formless, PERSON=ordinary] -> Neutral Life Mind FiveFaith
```

Path-faculties fail to unify with `PERSON=ordinary` and `MIN=8`.

## 5. Translation

### Literal Translation

> One without the wholesome is endowed, at the least, with eight: feeling,
> mind, body, and life. Likewise an ordinary person in the formless realm,
> with neutral feeling, life, mind, and the wholesome faculties.

### Bhāṣya-informed study translation

> At least, one deprived of the wholesome is endowed with eight: feelings,
> mind, body, and life. Likewise, an ordinary person in the formless realm
> is endowed with neutral feeling, life, mind, and the wholesome Faculties.

## 6. Philosophical Translation

> The minimum is not a bare continuum. It is the continuum that still governs, stripped of the path.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| sarvālpa | the fewest | eight |
| niḥśubha | without the wholesome | severed roots |
| vit | feeling | the five; vedayate |
| bāla | ordinary person | pṛthagjana; not a child |
| śubha | the wholesome | the five, in this count |
| samucchinna-kuśala-mūla | severed wholesome roots | the first case |

## 8. Logical Determination

```text
every living configuration
    ≥ 8

severed roots
    = five feelings, body, mind, life
    wholesome five absent from the minimum

formless ordinary person
    = neutral feeling, life, mind, five
    Form faculties absent from the minimum
    the three not included

same count
    ≠ same set
intersection
    = neutral feeling, life, mind

at the least
    ↛ every such person lacks the rest
```

## 9. Interpretive Note

**Translation note.** Earlier explanatory rendering (moved out of the
verse translation): The fewest is eight. One whose wholesome roots are
severed is endowed with the five feelings, body, mind, and life. An
ordinary person in the formless realm is endowed with neutral feeling,
life, mind, and the five beginning with faith. The path-faculties are
excluded because the subject is eight and the subject is an ordinary
person.

The question has changed. Not what one faculty entails. What is the fewest a possessor can have.

Without the wholesome is not an unwholesome thought, and not no faculties. The first eight still feels. Vit is not a sixth feeling.

At the least does not say every severed-roots person lacks eye, ear, nose, tongue, or the sex faculties. The prose does not list when those are absent.

Wholesome would also take the three. The eight and the ordinary person exclude them. The reply does not deny that the three are wholesome. General extension and local range need not coincide.

Five feelings in the count are not five feelings in one moment.

Interpretation: the floor is typed. The telos is not this verse. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_20
    a vak:Karika ;
    rdfs:label "VAK 2.20" ;
    vak:hasTopic vak:MinimumPossession ;
    vak:belongsTo vak:Indriyanirdesa .

vak:SeveredRootsMinimum vak:hasCount 8 .
vak:FormlessOrdinaryMinimum vak:hasCount 8 .

organon:SameCountOpposed
    organon:notTheVerseEnglish true .
```
