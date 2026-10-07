# VAK_2.44

## 1. Sanskrit (Devanāgarī)

> बोधिलभ्या मुनेर्न प्राक् चतुस्त्रिंशत्क्षणाप्तितः ।
>
> कामरूपाश्रये भूते निरोधाख्यादितो नृषु ॥ २.४४ ॥

## 2. Sanskrit (IAST)

> bodhilabhyā muner na prāk catustriṃśatkṣaṇāptitaḥ /
>
> kāmarūpāśraye bhūte nirodhākhyādito nṛṣu // 2.44 //

## 3. Lexical Analysis

```text
bodhilabhyā          → bodhi-labhyā
muner na prāk         → muneḥ na prāk
catustriṃśatkṣaṇāptitaḥ
                    → catuḥ-triṃśat-kṣaṇa-āptitaḥ
kāmarūpāśraye        → kāma-rūpa-āśraye
bhūte                → bhūte
nirodhākhyādito nṛṣu → nirodha-ākhyā āditaḥ nṛṣu
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| bodhi-labhyā | nominative feminine gerundive compound | obtained with awakening |
| muneḥ | genitive singular | of the Sage |
| na prāk | adverbial negation | not beforehand |
| catuḥ-triṃśat-kṣaṇa-āptitaḥ | causal ablative compound | because awakening occurs in thirty-four moments |
| kāma-rūpa-āśraye | locative compound | with Desire- or Form-Principle Faculty-support |
| bhūte | locative participial form | when such support is present |
| nirodha-ākhyā | nominative feminine compound | the attainment called cessation |
| āditaḥ | adverb | initially or at first production |
| nṛṣu | locative plural | among human beings |

## 4. Scientific English Rendering

> For the Sage, the attainment of cessation is obtained with awakening, not
> beforehand, because awakening is attained in thirty-four moments. When
> Desire- or Form-Principle Faculty-support is present, [the two attainments
> may occur]; the attainment called cessation is first produced among human
> beings.

The Bhāṣya attributes the no-prior-production position to Kāśmīra teachers.
Teachers of the outer regions hold that the Bodhisattva produced the
attainment earlier as a trainee.

## 5. Interpretation

VAK 2.44 answers an essential question without treating cessation as death.
The cessation-attainment is first produced in a human life, but may later be
entered in the Form Principle by someone who had previously acquired and
then lost it. This is not a theory that a living continuum has ceased to
exist; it is a question about how the appropriate support and causal
relation allow cognitive operation to resume after an interval of
non-operation.

The Bhāṣya gives the decisive question:

```text
After consciousness has been prevented from operating for a long interval,
how can consciousness arise again?
```

It preserves rival replies:

```text
Vaibhasika:
    past consciousness remains available as immediately preceding condition

Earlier teachers:
    consciousness and embodied Faculty-support are reciprocal seed-capacities;
    consciousness can arise from that Faculty-equipped body

Vasumitra:
    the cessation-attainment is with consciousness

Ghoṣaka and Vaibhasika conclusion:
    it is without consciousness
```

The final critical analysis refuses to posit a separate cessation-entity.
The entry-consciousness conditions a support opposed to later consciousness,
so consciousness does not operate for an interval. The attainment is then a
designation of that non-operation, or of bringing the support into that
condition.

Thus death is not required:

```text
Life-support and Faculty-support remain determinately conditioned;
the prior entry transforms their capacity for present cognitive operation;
the opposed condition ends; consciousness operates again.
```

The Kośa-wide synthesis remains: Vijñāna is Discriminative Cognition joining
and governing Perception and Conception. Its Inconceivable unity is not an
empirical citta-factor that perishes with each profile. The attainment
concerns the finite operation and non-operation of consciousness and
associated factors in the wheel; it does not eliminate the Hub's governing
relation.

## 6. Logical Determination

```text
FirstProduction(S, CessationAttainment)
    → Human(S)

PreviouslyAcquiredAndLost(S, CessationAttainment)
    and RebornWithFormPrincipleSupport(S)
    → MayReenter(S, CessationAttainment)
```

The critical account:

```text
EntryConsciousness(S)
    → ConditionsSupportOpposedToCognitiveOperation(S)
    → NonOperationOfConsciousness(S, interval)
    → Designated CessationAttainment(S, interval)

EndOfOpposedSupportCondition(S)
    → CognitiveOperationMayResume(S)
```

## 7. Interpretive Note

The source distinguishes first production from later re-entry, and it
distinguishes the sequence of attainment from its level of support. The
nine sequential attainments govern the initial acquisition; those with
complete mastery can enter attainments in transposed order. These rules do
not license collapsing the Non-Reflecting and cessation attainments.

The Buddha and Bodhisattva dispute is retained in the Bhāṣya study. The
source's discussion of life-continuity begins only after the explicit close
of the two-attainment inquiry and is not incorporated here.

## 8. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_44
    a vak:Karika ;
    rdfs:label "VAK 2.44" ;
    vak:hasTopic vak:CessationAttainmentReentry ;
    vak:belongsTo vak:Indriyanirdesa .

vak:CessationAttainment
    vak:initiallyProducedBy vak:HumanPractitioner ;
    vak:requires vak:DesireOrFormPrincipleSupport ;
    vak:mayBeDesignatedFrom vak:NonOperationOfConsciousness,
        vak:TransformedSupport .
```
