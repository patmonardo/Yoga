# VAK_7.07 — Knowledge of Exhaustion and Non-Arising

## Sanskrit

### Devanāgarī

```text
क्षयज्ञानं हि सत्येषु परिज्ञातादिनिश्चयः ।
न परिज्ञेयमित्यादिरनुत्पादमतिर्मता ॥ ७.७ ॥
```

### IAST

```text
kṣayajñānaṃ hi satyeṣu parijñātādiniścayaḥ /
na parijñeyam ity ādir anutpādamatir matā // VAK_7.07 //
```

## Padaccheda

| Pada | Analysis | Working sense |
|---|---|---|
| kṣaya-jñānam | nominative singular neuter | knowledge of exhaustion |
| hi | indeclinable | indeed; for |
| satyeṣu | locative plural neuter | with respect to the truths |
| parijñāta-ādi-niścayaḥ | nominative singular masculine | certainty beginning with “fully known” |
| na | indeclinable negation | not |
| parijñeyam | gerundive, nominative singular neuter | to be fully known |
| iti | quotative particle | thus |
| ādiḥ | nominative singular masculine | beginning with; and so forth |
| anutpāda-matiḥ | nominative singular feminine | cognition of non-arising |
| matā | nominative singular feminine | held, regarded, defined |

## Grammar

The verse defines two terminal knowledges by the form of their certainty regarding the Four Noble Truths.

`parijñātādi-niścayaḥ` is a compressed reference to the completed tasks associated with the truths:

```text
suffering
    has been fully known

origin
    has been abandoned

cessation
    has been realized

path
    has been cultivated
```

`na parijñeyam ity ādiḥ` then repeats the same fourfold structure negatively and prospectively:

```text
nothing further is to be fully known
nothing further is to be abandoned
nothing further is to be realized
nothing further is to be cultivated
```

The verse therefore distinguishes accomplished completion from certainty that the work will not arise again.

## Literal Translation

Knowledge of exhaustion is the certainty, with respect to the truths, beginning with “it has been fully known.”

Knowledge of non-arising is held to be the cognition beginning with “it is not further to be fully known.”

## Philosophical Translation

Knowledge of exhaustion is the determinate certainty that the four tasks belonging to the truths have been completed. Knowledge of non-arising is the further certainty that none of those tasks remains to be performed again.

## Technical Vocabulary

### kṣayajñāna

```text
kṣayajñāna
    = knowledge of exhaustion
    = certainty of accomplished completion
```

It determines the completed fact:

```text
the task has been done
```

### anutpādajñāna

```text
anutpādajñāna
    = knowledge of non-arising
    = certainty of non-recurrence
```

It determines not merely present completion but the impossibility of renewed obligation:

```text
the task need not arise again
```

### niścaya

```text
niścaya
    = certainty
    = determinate ascertainment
```

The verse does not describe a vague confidence or contemplative mood. Both knowledges are exact determinations regarding the status of the path-work.

## Doctrinal Determination

The four truths carry four distinct tasks:

| Truth | Task |
|---|---|
| suffering | to be fully known |
| origin | to be abandoned |
| cessation | to be realized |
| path | to be cultivated |

The two knowledges relate differently to these same tasks.

### Knowledge of exhaustion

```text
completed task
    known as completed
```

### Knowledge of non-arising

```text
completed task
    known as not requiring repetition
```

Thus `anutpādajñāna` is not another object-domain beside `kṣayajñāna`. It is a stronger temporal and modal determination of the accomplished path.

## Logical Determination

The verse gives a precise dyad:

```text
completion
    /
non-recurrence
```

Or:

```text
kṣaya
    the work is exhausted

anutpāda
    the work will not arise again
```

The first is perfect determination of what has occurred. The second is perfect determination of what no longer remains possible as a renewed task.

```text
kṣayajñāna
    accomplished actuality

anutpādajñāna
    secured non-repetition
```

This is not an empirical enumeration. The second determination follows from the first by adding the modal certainty of non-renewal.

## Organon Light

VAK 7.07 gives a remarkably exact distinction between two forms of final knowing:

```text
JÑĀNA OF COMPLETION
    I know what has happened

JÑĀNA OF NON-ARISING
    I know that it need not happen again
```

This supports the project distinction already emerging in Chapter 7:

```text
principial task-structure
    dharma

accomplished determination
    jñāna

secured non-recurrence
    anutpādajñāna
```

Yoga presents Absolute Knowing as the achieved specification of Buddhi. The Kośa now articulates, in rational-empirical detail, what such achievement must know about its own completed work.

The verse therefore moves beyond merely knowing the truths as objects. Knowing now knows the status of its own path-activity:

```text
what was required
what was completed
what cannot become required again
```

No stronger synthesis is imposed in this first pass.

## OWL++ Seed

```turtle
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix jna: <http://127.0.0.1:3000/jnana#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_7_07
    a vak:Karika ;
    rdfs:label "VAK 7.07" ;
    vak:determines jna:ExhaustionKnowledge,
                   jna:NonArisingKnowledge,
                   jna:CompletedPathTask,
                   jna:NonRecurringPathTask .

jna:ExhaustionKnowledge
    a jna:Knowledge ;
    jna:ascertains jna:CompletedPathTask .

jna:NonArisingKnowledge
    a jna:Knowledge ;
    jna:ascertains jna:NonRecurringPathTask .
```

## Commit History

```text
2026-07-23 — Initial kārikā-pass analysis.
```
