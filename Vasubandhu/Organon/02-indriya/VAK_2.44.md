# VAK_2.44 — Support and First Production

## 1. Sanskrit (Devanāgarī)

> बोधिलभ्या मुनेर्न प्राक् चतुस्त्रिंशत्क्षणाप्तितः ।
>
> कामरूपाश्रये भूते निरोधाख्यादितो नृषु ॥ २.४४ ॥

## 2. Sanskrit (IAST)

> bodhilabhyā muner na prāk catustriṃśatkṣaṇāptitaḥ /
>
> kāmarūpāśraye bhūte nirodhākhyādito nṛṣu // 2.44 //

## 3. Lexical Analysis

| Pada | Force |
|---|---|
| bodhi-labhyā | acquired with awakening |
| muneḥ | the Sage |
| na prāk | not beforehand |
| catustriṃśat-kṣaṇa | thirty-four moments |
| kāma-rūpa-āśraye | with a desire- or form-realm support |
| bhūte | when that support is present |
| nirodha-ākhyā | the attainment called cessation |
| āditaḥ | at first |
| nṛṣu | among humans |

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
Both attainments: desire- or form-realm support.  
Cessation first among humans; later in the form realm only after loss.

## 5. Translation

### Literal Translation

For the Sage, acquired with awakening, not beforehand, because attained in thirty-four moments. When a desire- or form-realm support is present. The one called cessation, at first, among humans.

### Bhāṣya-informed study translation

> For the Sage, acquired with awakening, not beforehand. Both attainments arise with a desire- or form-realm support. The attainment of cessation is first produced among humans, and later in the form realm only by those who had lost it. Loss is required; otherwise the Udāyin sūtra is contradicted. The names follow the preparation, not the range of the cessation. Return of consciousness is disputed. Designation from non-operation is not accepted.

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
later form-realm entry
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

The five-destiny reading of the damaged phrase is not adopted. The counterexample concerns form-realm existence. Not a collation. Life begins the next topic.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_44 a vak:Karika ; vak:hasTopic vak:SupportAndFirstProduction .
vak:ReturnOfConsciousness vak:settled false .
```
