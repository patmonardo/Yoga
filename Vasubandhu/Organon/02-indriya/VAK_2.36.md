# VAK_2.36 — Acquisition

## 1. Sanskrit (Devanāgarī)

> नामकायादयश्चेति प्राप्तिर्लाभः समन्वयः ।
>
> प्राप्त्यप्राप्ती स्वसंतानपतितानां निरोधयोः ॥ २.३६ ॥

## 2. Sanskrit (IAST)

> nāmakāyādayaś ceti prāptir lābhaḥ samanvayaḥ /
>
> prāptyaprāptī svasaṃtānapatitānāṃ nirodhayoḥ // 2.36 //

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| nāma-kāya-ādayaḥ | nominative | groups of names and so forth |
| iti | | thus, the list |
| prāptiḥ | nominative | acquisition |
| lābhaḥ | nominative | obtaining |
| samanvayaḥ | nominative | possession |
| sva-saṃtāna-patitānām | genitive | of what belongs to one's own continuum |
| nirodhayoḥ | genitive dual | of the two cessations |

Two explanations of one word. Gender does not block that.

## 4. Grammar

```text
% start S
S[NAME=acquisition] -> Obtaining | Possession
S[RANGE=conditioned] -> OwnContinuum[OTHER=false, NONSENTIENT=false]
S[RANGE=unconditioned] -> TwoCessations[SPACE=false]
```

Obtaining what was not possessed, or possessing what has been obtained.  
Own continuum only.  
Space has neither acquisition nor non-acquisition.

## 5. Translation

### Literal Translation

And the groups of names and so forth. Acquisition is obtaining and possession. Acquisition and non-acquisition of what belongs to one's own continuum, and of the two cessations.

### Bhāṣya-informed study translation

> And the groups of names and the rest. Acquisition is obtaining and possession: obtaining what was not obtained or had been relinquished, and possessing what has been obtained. Acquisition and non-acquisition concern what belongs to one's own continuum, and the two cessations; not what belongs to another, nor the non-sentient, nor space.

## 6. Philosophical Translation

> Acquisition is obtaining and possession. Own continuum, and the two cessations. Space is neither. Real entity against designation from seed-capacity is not settled.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| prāpti | acquisition | obtaining and possession |
| lābha | obtaining | what was absent or relinquished |
| samanvāgama | possession | what has been obtained |
| aprāpti | non-acquisition | the reverse, inside the range |
| svasaṃtāna | one's own continuum | the conditioned range |
| pratisaṃkhyā-nirodha | cessation through Discrimination | not all beings |
| apratisaṃkhyā-nirodha | cessation not through Discrimination | all sentient beings |
| ākāśa | space | neither |
| bīja | seed | capable name-and-form; not a second entity |
| prajñapti | designation | the critical account |
| dravya | real entity | the Vaibhāṣika account |

Anāsrava in the quotation is uncontaminated. Not unconditioned. Not every uncontaminated dharma.

## 8. Logical Determination

```text
acquisition
    = obtaining or continued possession
non-acquisition
    = reverse, inside the range

own continuum or one of two cessations
    → the pair may apply
another continuum, non-sentient, space
    → neither

no acquisition
    → no non-acquisition

real entity
    attributed, not settled
designation from capacity
    the critical account
    not a named school
seed
    ≠ a hidden extra
abandonment
    = cannot arise again
    ≠ destruction of a possession-object
```

## 9. Interpretive Note

The list is completed and left. The inquiry is acquisition. Scriptural wording, causal work, and noble status are tested in that order. Production is disowned. Status remains the problem, because worldly consciousness does not display the path.

The initial-moment exception is contextual. Fully bound, at the first moment of the noble path. Not a restored collation. The greed sentence is a local use. Tolerating, or not expelling. Not the king's mastery, and not the seed, forced into one gloss.

Organon reading: the pair survives either account. What is stored is the question the next verses take up. Not the verse English.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_36
    a vak:Karika ;
    rdfs:label "VAK 2.36" ;
    vak:hasTopic vak:Acquisition ;
    vak:belongsTo vak:Indriyanirdesa .

vak:Acquisition vak:includes vak:Obtaining, vak:Possession .
vak:Acquisition vak:range vak:OwnContinuum, vak:TwoCessations .
vak:Space vak:neither true .

organon:DisputeNotSettled
    organon:notTheVerseEnglish true .
```
