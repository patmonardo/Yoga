# VAK_2.52 — Homogeneous Cause

## 1. Sanskrit (Devanāgarī)

> सभागहेतुः सदृशाः स्वनिकायभुवोऽग्रजाः ।
>
> अन्योऽन्यं नवभूमिस्तु मार्गः समविशिष्टयोः ॥ २.५२ ॥

## 2. Sanskrit (IAST)

> sabhāgahetuḥ sadṛśāḥ svanikāyabhuvo 'grajāḥ /
>
> anyo 'nyaṃ navabhūmis tu mārgaḥ samaviśiṣṭayoḥ // 2.52 //

## 3. Lexical Analysis

| Pada | Force |
|---|---|
| sabhāga-hetuḥ | homogeneous cause |
| sadṛśāḥ | similar |
| sva-nikāya-bhuvaḥ | of their own class and level |
| agrajāḥ | prior-born |
| anyo 'nyam | of one another |
| nava-bhūmiḥ mārgaḥ | the Path of nine levels |
| sama-viśiṣṭayoḥ | of the equal and the superior |

## 4. Grammar

```text
% start S
S[CAUSE=homogeneous] -> Similar[CLASS=own, LEVEL=own, TIME=prior]
S[CAUSE=homogeneous, PATH=true] -> NineLevels[EQUAL=true | SUPERIOR=true]
```

Homogeneous is similar, own class and level, prior-born.  
Future is not.  
Path crosses nine levels, equal or superior only.  
Not same-class.

## 5. Translation

### Literal Translation

Homogeneous cause: similar, of their own class and level, prior-born. But the Path of nine levels, of one another, of the equal and the superior.

### Bhāṣya-informed study translation

> Homogeneous cause is similar, of its own class and level, prior-born. Future is not. The Path of nine levels is homogeneous cause across them, of the equal or the superior only. Not same-class. Prior still required. Not the co-arisen reciprocity.

## 6. Philosophical Translation

> Homogeneous is similar, own class and level, prior-born. Future is not. Path crosses nine levels, equal or superior only. Not same-class. State, not substance.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| sabhāga-hetu | homogeneous cause | prior similar |
| agraja | prior-born | temporal |
| āgantuka | adventitious | not appropriated |
| hetūpacaya | accumulation of causes | superiority, not height |

## 8. Logical Determination

```text
similar + own class + own level + prior
    → homogeneous cause
future
    ≠ this cause
Path
    level relaxed
    prior kept
    equal or superior only
maturation cause
    may be future
    different character
```

## 9. Interpretive Note

The witness says cause of the inferior. The governing clause is equal or superior. The negative is supplied. Not a collation. Worldly qualities produced by application are the next verse.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_52 a vak:Karika ; vak:hasTopic vak:HomogeneousCause .
vak:PathSabhaga vak:downward false .
```
