# VAK 6.03

## Sanskrit

### Devanāgarī

दुःखास्त्रिदुःखतायोगाद्यथायोगमशेषतः ।
मनापा अमनापाश्च तदन्ये चैव सास्रवाः ॥ ६.३ ॥

### IAST

duḥkhās tri-duḥkhatā-yogād yathāyogam aśeṣataḥ |
manāpā amanāpāś ca tadanye caiva sāsravāḥ || 6.3 ||

## Padaccheda

| Pada | Form | Determination |
|---|---|---|
| duḥkhāḥ | nominative plural masculine | suffering; belonging to the truth of suffering |
| tri-duḥkhatā-yogāt | ablative singular compound | because of connection with the three modes of suffering |
| yathā-yogam | adverb | according to applicability |
| aśeṣataḥ | adverb | without remainder; exhaustively |
| manāpāḥ | nominative plural masculine | agreeable, pleasing |
| amanāpāḥ | nominative plural masculine | disagreeable, displeasing |
| tad-anye | nominative plural masculine | those other than these |
| sāsravāḥ | nominative plural masculine | contaminated; accompanied by influx |

## Grammar

The principal assertion is:

```text
sāsravāḥ
    duḥkhāḥ
```

Contaminated dharmas are suffering because of their connection with the three modes of suffering.

```text
yathā-yogam
    according to what applies in each case

aśeṣataḥ
    without remainder
```

The verse gives an exhaustive division of contaminated dharmas into agreeable, disagreeable, and those other than these.

## Literal Translation

Agreeable, disagreeable, and other contaminated dharmas are, without remainder and according to applicability, suffering because of their connection with the three modes of suffering.

## Philosophical Translation

Every contaminated determination—whether experienced as agreeable, disagreeable, or neutral—belongs without remainder to the truth of suffering, insofar as each is implicated, according to its mode, in one of the three structures of suffering.

## Technical Vocabulary

### tri-duḥkhatā

The three modes of suffering are:

```text
duḥkha-duḥkhatā
    suffering as suffering

vipariṇāma-duḥkhatā
    suffering through transformation

saṃskāra-duḥkhatā
    suffering inherent in conditioned formation
```

### duḥkha-duḥkhatā

This is the suffering-character of what is directly disagreeable and painful.

### vipariṇāma-duḥkhatā

Agreeable experience is connected with suffering because it changes. Its pleasantness depends on conditions that cannot preserve it.

### saṃskāra-duḥkhatā

A contaminated dharma may be neither presently painful nor pleasant. Nevertheless, insofar as it is conditioned and appropriated within the kleśa-karma complex, it remains unstable and non-self-sufficient.

### manāpa and amanāpa

```text
manāpa
    agreeable

amanāpa
    disagreeable
```

The verse refuses to let ordinary affective appraisal determine ultimate valuation.

### sāsrava

```text
sa-āsrava
    accompanied by influx
    providing a basis for afflictive continuation
```

The extension of the truth of suffering is the entire contaminated field.

## Analysis

VAK 6.02 named duḥkha as the first truth. VAK 6.03 determines its full extension:

```text
all sāsrava dharmas
without remainder
```

The three experiential fields are related to the three suffering-modes:

```text
amanāpa
    → duḥkha-duḥkhatā

manāpa
    → vipariṇāma-duḥkhatā

tadanya
    → saṃskāra-duḥkhatā
```

The force of `yathāyogam` is differentiated application; the force of `aśeṣataḥ` is exhaustive inclusion.

## Doctrinal Determination

```text
duḥkha-satya
    = all contaminated dharmas
```

Pain declares itself as suffering. Pleasure disguises its instability. Neutral formation conceals its dependency.

The three modes disclose progressively deeper structures:

```text
immediate suffering
    visible contradiction

suffering through transformation
    concealed contradiction

suffering as conditioned formation
    structural contradiction
```

## Logical Determination

The empirical division is:

```text
agreeable
disagreeable
neither
```

All three are brought under the universal duḥkha through distinct grounds:

```text
agreeable
    because it transforms

disagreeable
    because it is immediately painful

neutral
    because it is conditioned
```

The three modes are the differentiated exhibition of the one truth of suffering.

## Path-of-Knowing Interpretation

The Path must discriminate three errors:

```text
pain
    treated merely as something to repel

pleasure
    treated as stable good

neutral formation
    treated as harmless or self-sufficient
```

Direct knowing of duḥkha is exhaustive discrimination of the entire contaminated field.

## Relation to Sāṃkhya and Yoga

The verse closely parallels the Sāṃkhya-Yoga insistence that what appears pleasant remains implicated in transformation and conditioned formation. Ordinary affective appraisal is therefore inadequate.

## Interpretive Note

```text
aśeṣataḥ
    exhaustive inclusion

yathāyogam
    differentiated inclusion
```

Together they give the scientific form:

```text
everything included
but each according to its determination
```

## Organon Note

```text
Class: SasravaDharma
Class: DuhkhaSatyaObject

SasravaDharma SubClassOf DuhkhaSatyaObject

Class: ManapaDharma
Class: AmanapaDharma
Class: OtherSasravaDharma

Class: DuhkhaDuhkhata
Class: ViparinamaDuhkhata
Class: SamskaraDuhkhata
```

The mapping implied by `yathāyogam` should be represented as constrained rather than as a universal assertion that every instance bears all three modes.

## OWL++ Seed

```text
Class: Dharma
Class: SasravaDharma
Class: DuhkhaSatyaObject
Class: ManapaDharma
Class: AmanapaDharma
Class: OtherSasravaDharma
Class: Duhkhata
Class: DuhkhaDuhkhata
Class: ViparinamaDuhkhata
Class: SamskaraDuhkhata

SasravaDharma SubClassOf Dharma
SasravaDharma SubClassOf DuhkhaSatyaObject
ManapaDharma SubClassOf SasravaDharma
AmanapaDharma SubClassOf SasravaDharma
OtherSasravaDharma SubClassOf SasravaDharma
DuhkhaDuhkhata SubClassOf Duhkhata
ViparinamaDuhkhata SubClassOf Duhkhata
SamskaraDuhkhata SubClassOf Duhkhata

ObjectProperty: hasDuhkhata
    Domain: SasravaDharma
    Range: Duhkhata

ManapaDharma SubClassOf hasDuhkhata some ViparinamaDuhkhata
AmanapaDharma SubClassOf hasDuhkhata some DuhkhaDuhkhata
OtherSasravaDharma SubClassOf hasDuhkhata some SamskaraDuhkhata
```

## Determinate Summary

```text
All contaminated dharmas
belong to the truth of suffering.

Disagreeable dharmas:
    suffering as suffering

Agreeable dharmas:
    suffering through transformation

Other contaminated dharmas:
    suffering as conditioned formation
```

The central result is that duḥkha does not mean every experience feels painful. It means no contaminated determination is ultimately stable, self-sufficient, or free.
