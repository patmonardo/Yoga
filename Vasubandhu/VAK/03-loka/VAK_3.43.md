# VAK_3b — VAkK_3.43

## Sanskrit — Devanāgarī

नैकाग्राचित्तयोरेतौ निर्वात्यव्याकृतद्वये ।
क्रमच्युतौ पादनाभिहृदयेषु मनश्च्युतिः ॥ VAkK_3.43 ॥

## Sanskrit — IAST

naikāgrācittayor etau nirvāty avyākṛtadvaye /
kramacyutau pādanābhihṛdayeṣu manaścyutiḥ // VAkK_3.43 //

## Source Caution

The source reads:

```text
naikāgrācittayoretau nirvātyavyākṛtadvaye /
kramacyutau pādanābhihṛdayeṣu manaścyutiḥ // VAkK_3.43 //
```

The sandhi in `nirvātyavyākṛtadvaye` is compact and should be controlled by the Bhāṣya.

## Padaccheda

| Sandhi form | Padaccheda | Basic meaning |
|---|---|---|
| na | na | not |
| ekāgrācittayoḥ | ekāgra-acittayoḥ | in one-pointed and non-mental states |
| etau | etau | these two |
| nirvāti | nirvāti | ceases / is extinguished |
| avyākṛtadvaye | avyākṛta-dvaye | in the two indeterminate states |
| kramacyutau | krama-cyutau | in sequential falling-away |
| pāda | pāda | foot |
| nābhi | nābhi | navel |
| hṛdayeṣu | hṛdayeṣu | in the heart-centers |
| manaścyutiḥ | manaḥ-cyutiḥ | falling-away of mind |

## Grammar

```text
na ekāgra-acittayoḥ etau
    = these two do not occur in one-pointed or non-mental states

nirvāti avyākṛta-dvaye
    = it ceases in the two indeterminate states

krama-cyutau pāda-nābhi-hṛdayeṣu manaḥ-cyutiḥ
    = in sequential falling-away, the falling-away of mind is in feet, navel, and heart
```

## Literal Translation

These two do not occur in one-pointed and non-mental states. It ceases in the two indeterminate states. In sequential falling-away, the falling-away of mind is in the feet, navel, and heart.

## Philosophical Translation

The transition-functions named in the previous verse are further delimited. They do not occur in one-pointed concentration or in a non-mental state. They belong to an indeterminate register, and in sequential falling-away the departure of mental continuity is mapped through feet, navel, and heart.

## Technical Vocabulary

| Sanskrit | Working translation | Note |
|---|---|---|
| ekāgra | one-pointed | Concentrated mental state |
| acitta | non-mental / without mind | State without active mind |
| avyākṛta | indeterminate | Neither wholesome nor unwholesome |
| krama-cyuti | sequential falling-away | Ordered transition process |
| manaḥ-cyuti | falling-away of mind | Transition of mental continuity |
| pāda | foot | Bodily locus |
| nābhi | navel | Bodily locus |
| hṛdaya | heart | Bodily locus |

## Doctrinal Determination

VAkK_3.42 assigned transition-functions to `manovijñāna` and stated that falling-away and arising occur in `upekṣā`.

VAkK_3.43 adds three delimitations:

```text
not in ekāgra
not in acitta
connected with avyākṛta
```

Then it gives a bodily sequence for `krama-cyuti`:

```text
pāda
nābhi
hṛdaya
```

## Logical Determination

The transition is not a metaphysical leap. It is a conditioned function with exclusions and loci.

```text
transition-feature
    has excluded states
    has an indeterminate register
    has bodily loci
```

This keeps the analysis within conditioned continuity, not a permanent self.

## Interpretive Note

The important project point is that transition is being modeled as a functional feature.

```text
not substance-transfer
but conditioned sequence
```

This continues the movement from listed being to functional essence.

## OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_3_43
    a vak:Karika ;
    rdfs:label "VAkK 3.43" ;
    vak:continues vak:VAK_3_42 ;
    vak:hasTopic vak:ManaCyuti ;
    vak:excludesCondition vak:Ekagra ;
    vak:excludesCondition vak:Acitta ;
    vak:hasRegister vak:Avyakrta ;
    vak:hasSequence vak:KramaCyutiSequence .
```

## Commit Note

Committed VAK_3b / VAkK_3.43.

Established:
- the transition does not occur in one-pointed or non-mental states.
- it is connected with an indeterminate register.
- sequential falling-away is mapped through feet, navel, and heart.
