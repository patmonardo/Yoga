# VAK_2.44 — Support and First Production

## 1. Sanskrit (Devanāgarī)

```sanskrit
बोधिलभ्या मुनेर्न प्राक् चतुस्त्रिंशत्क्षणाप्तितः ।
कामरूपाश्रये भूते निरोधाख्यादितो नृषु ॥ २.४४ ॥
```

## 2. Sanskrit (IAST)

```text
bodhilabhyā muner na prāk catustriṃśatkṣaṇāptitaḥ /
kāmarūpāśraye bhūte nirodhākhyādito nṛṣu // 2.44 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| bodhi-labhyā | nom. sg. f.; compound | acquired with awakening |
| muneḥ | gen. sg. m. | the Sage |
| na prāk | negation + adverb | not beforehand |
| catustriṃśat-kṣaṇa | abl. sg. m.; numeral compound | thirty-four moments |
| kāma-rūpa-āśraye | loc. sg. n.; compound | with a desire- or Form Realm support |
| bhūte | loc. sg. n. past participle | when that support is present |
| nirodha-ākhyā | nom. sg. f.; compound | the attainment called cessation |
| āditaḥ | adverb | at first |
| nṛṣu | loc. pl. m. | among humans |

Support is not the level. The attainment of cessation remains of the summit.
## 4. Grammar

```text
% start S
S[PERSON=sage] -> Acquisition[WITH=awakening, PRIOR=false]
S[ATTAINMENT=both] -> Support[REALM=desire|form]
S[ATTAINMENT=cessation, FIRST=true] -> Human
S[ATTAINMENT=cessation, LATER=true] -> Form[LOSS=true]
```

Sage: with awakening, not beforehand.  
Both attainments: desire- or Form Realm support.  
Cessation first among humans; later in the form realm only after loss.

## 5. Translation

### Literal Translation

> For the Sage, the two attainments are acquired with awakening, not
> beforehand, since awakening is reached in thirty-four moments. They arise
> when a desire- or Form Realm support is present. The attainment called
> cessation is first produced among humans.
### Bhāṣya-informed study translation

> For the Sage, [the attainments] are acquired with awakening, not
> beforehand, since awakening is reached in thirty-four moments. With a
> desire- or Form Realm support present, the attainment called cessation is
> first produced among humans.
## 6. Philosophical Translation

> Support and level stay apart. First production is human; later entry presupposes loss. The names follow the preparation, not the range of the cessation. Return of consciousness is the live dispute. Designation from non-operation is not accepted.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| āśraya | support | desire or form realm; not the level |
| āditaḥ | at first | humans only |
| saṃjñā-vedayita-nirodha | cessation of reflection and feeling | the sūtra name |
| vyutkrānta | out of order | mastery, not the beginner |
| samanantara | immediately preceding | the Vaibhāṣika past |
| anyonya-bījaka | seed of one another | the earlier teachers |
| acittikā | without consciousness | the Vaibhāṣika close |

## 8. Logical Determination

```text
either attainment
    → support in desire or form realm
first production of cessation
    → human
later Form Realm entry
    → prior acquisition and loss
beginner
    → successive
mastery
    → may skip
name
    = preparatory opposition
    ≠ the range of the cessation
return
    disputed
    not settled
```

## 9. Interpretive Note

**Translation note.** The commentary identifies both attainments as arising with a desire- or Form Realm support, while cessation remains an attainment of the summit. It says cessation is later produced in the form realm only by one who has lost it, and examines a sūtra counterexample and competing explanations of support and return to consciousness. The damaged phrase on the support is not expanded beyond the stated alternatives.

The five-destiny reading of the damaged phrase is not adopted. The counterexample concerns Form Realm existence. Not a collation. Life begins the next topic.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_44 a vak:Karika ; vak:hasTopic vak:SupportAndFirstProduction .
vak:ReturnOfConsciousness vak:settled false .
```
