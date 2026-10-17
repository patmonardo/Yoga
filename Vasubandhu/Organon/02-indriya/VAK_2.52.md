# VAK_2.52 — Homogeneous Cause

## 1. Sanskrit (Devanāgarī)

```sanskrit
सभागहेतुः सदृशाः स्वनिकायभुवोऽग्रजाः ।
अन्योऽन्यं नवभूमिस्तु मार्गः समविशिष्टयोः ॥ २.५२ ॥
```

## 2. Sanskrit (IAST)

```text
sabhāgahetuḥ sadṛśāḥ svanikāyabhuvo 'grajāḥ /
anyo 'nyaṃ navabhūmis tu mārgaḥ samaviśiṣṭayoḥ // 2.52 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sabhāga-hetuḥ | masculine nominative singular compound | homogeneous cause |
| sadṛśāḥ | masculine nominative plural adjective | similar |
| sva-nikāya-bhuvaḥ | masculine nominative plural compound adjective | of their own class and level |
| agrajāḥ | masculine nominative plural adjective | prior-born |
| anyo 'nyam | reciprocal adverb, accusative singular form | of one another |
| nava-bhūmiḥ mārgaḥ | masculine nominative singular compound + masculine nominative singular | the Path of nine levels |
| sama-viśiṣṭayoḥ | genitive/locative dual compound adjective | of the equal and the superior |

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

> Homogeneous causes are similar, of their own class and level, and
> prior-born. The Path of nine levels is of one another, at the equal and
> superior levels.
### Bhāṣya-informed study translation

> A homogeneous cause is similar, of its own class and level, and
> prior-born. The Path crosses the nine levels as cause for the equal or
> the superior.
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

**Translation note.** The Bhāṣya requires prior arising, not future arising,
and explains that the Path crosses levels without relaxing the prior-born
condition. The Path case is not confined to the same class. The text
distinguishes level or state from substance; the local witness's contrary
“inferior” wording remains a noted uncertainty.

The witness says cause of the inferior. The governing clause is equal or superior. The negative is supplied. Not a collation. Worldly qualities produced by application are the next verse.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_52 a vak:Karika ; vak:hasTopic vak:HomogeneousCause .
vak:PathSabhaga vak:downward false .
```
