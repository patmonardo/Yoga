# VAK_4.85

## 1. Sanskrit — Devanāgarī

सर्वेऽधिपतिनिष्यन्दविपाकफलदा मताः ।  
दुःखनान्मारणादोजोनाशनात्त्रिविधं फलम् ॥ ४.८५ ॥

Local source:

```text
sarve 'dhipatiniṣyandavipākaphaladā matāḥ /
duḥkhanānmāraṇādojonāśanāttrividhaṃ phalam // VAkK_4.85 //
```

Cautious normalized segmentation:

```text
sarve adhipati-niṣyanda-vipāka-phala-dāḥ matāḥ |
duḥkhanāt māraṇāt ojas-nāśanāt trividhaṃ phalam ||
```

The transmitted `duḥkhanān` is provisionally understood through the ablative sequence `duḥkhanāt / māraṇāt / ojas-nāśanāt`. This requires confirmation in the Bhāṣya and critical-edition pass.

## 2. Sanskrit — IAST

**sarve ’dhipati-niṣyanda-vipāka-phala-dā matāḥ |**  
**duḥkhanān māraṇād ojo-nāśanāt trividhaṃ phalam || 4.85 ||**

The verse states that the karmic courses produce a threefold result:

```text
adhipati-phala
    dominant result

niṣyanda-phala
    outflow or corresponding result

vipāka-phala
    maturation result
```

The second half gives three grounds for this threefold efficacy: causing suffering, causing death, and destroying vital force. The exact one-to-one distribution between these grounds and the three result-types must be established by the Bhāṣya.

## 3. Padaccheda

```text
sarve
adhipati
niṣyanda
vipāka
phala-dāḥ
matāḥ

duḥkhanāt
māraṇāt
ojas-nāśanāt
trividham
phalam
```

Expanded first statement:

```text
sarve karmapathāḥ

adhipati-phala-dāḥ
niṣyanda-phala-dāḥ
vipāka-phala-dāḥ

matāḥ
```

> All the karmic courses are held to give dominant, outflow, and maturation results.

Expanded second statement:

```text
duḥkhanāt
māraṇāt
ojas-nāśanāt

trividhaṃ phalam
```

> Because they cause suffering, death, and the destruction of vital force, their result is threefold.

## 4. Grammar

- **sarve** — masculine nominative plural, “all”; the understood referent is the karmic courses under discussion.
- **adhipati** — first member of `adhipati-phala`, “dominant result.”
- **niṣyanda** — from `niḥ + √syand`, “flow out”; hence “outflow-result” or “corresponding result.”
- **vipāka** — from `vi + √pac`, “ripen”; hence “maturation result.”
- **phala-dāḥ** — masculine nominative plural, “result-giving.”
- **matāḥ** — past passive participle of `√man`, “held, considered, recognized.”
- **duḥkhanāt** — provisional causal ablative, “because of causing suffering.”
- **māraṇāt** — ablative singular, “because of causing death.”
- **ojas** — vitality, vigor, operative strength.
- **nāśana** — destruction, loss, impairment.
- **trividham phalam** — “threefold result.”

## 5. Literal Translation

> All are held to give dominant, outflow, and maturation results. Because they cause suffering, death, and destruction of vitality, the result is threefold.

A cautious expanded rendering:

> All the karmic courses are regarded as productive of three kinds of result: a dominant result, an outflow-result, and a maturation result. This threefold result is explained through the action’s infliction of suffering, its causing of death, and its destruction or impairment of vital force.

## 6. Philosophical Translation

> Every completed karmic course exceeds the moment of its visible performance. It conditions a broader field, continues in a corresponding causal stream, and matures into a determinate consequence. The kārikā distinguishes these three result-modes without yet supplying their full explanatory articulation.

The movement is:

```text
course-type
    ↓
endowment
    ↓
manifestation
    ↓
threefold result
```

## 7. Technical Vocabulary

### adhipati-phala

```text
adhipati-phala
    dominant result
```

A result in which an action conditions a broader field or set of circumstances.

### niṣyanda-phala

```text
niṣyanda-phala
    outflow-result
    corresponding result
```

A result that continues or corresponds to the qualitative determination of its ground.

### vipāka-phala

```text
vipāka-phala
    maturation result
```

A result produced when karma reaches causal maturity under the required conditions.

### duḥkhana

Provisionally, causing suffering or distress.

### māraṇa

Killing or causing death.

### ojo-nāśana

Destruction or impairment of vitality and operative strength.

## 8. Doctrinal Determination

The karmic courses are not merely classificatory items; they are `phala-dāḥ`, result-giving determinations.

The verse distinguishes:

```text
1. adhipati-phala
2. niṣyanda-phala
3. vipāka-phala
```

These are three causal result-types, not merely three temporal stages. The precise doctrinal mapping of the second pāda must remain provisional until the Bhāṣya pass.

## 9. Logical Determination

Let a completed karmic course be `K`. Its result is structurally plural:

```text
Result(K) = {
    DominantResult(K),
    OutflowResult(K),
    MaturationResult(K)
}
```

The verse therefore denies a simple model:

```text
one act → one undifferentiated result
```

and establishes:

```text
one completed course → three differentiated result-relations
```

The distinctions are causal and modal, not merely verbal.

## 10. Light Organon Interpretation

At the Kernel level, a completed operation should not be represented by one return value alone. It may establish different result-relations with different conditions and temporal profiles.

A restrained first-pass structure is:

```text
KarmicResultSet {
    dominantResult
    outflowResult
    maturationResult
}
```

The kārikā warrants the threefold distinction. Detailed software analogies should wait until the Bhāṣya clarifies the precise relations among the three fruits.

## 11. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_85
    a vak:Karika ;
    rdfs:label "VAkK 4.85" ;
    vak:continues vak:VAK_4_84 ;
    vak:hasTopic vak:ThreefoldKarmicResult .

vak:KarmicCourse
    vak:producesResult
        vak:DominantResult,
        vak:OutflowResult,
        vak:MaturationResult .

vak:DominantResult
    rdfs:label "adhipati-phala" .

vak:OutflowResult
    rdfs:label "niṣyanda-phala" .

vak:MaturationResult
    rdfs:label "vipāka-phala" .

vak:ThreefoldKarmicResult
    vak:includes
        vak:DominantResult,
        vak:OutflowResult,
        vak:MaturationResult .
```

Rule seed:

```text
CompletedKarmicCourse(?course)
    →
Produces(?course, DominantResult)
and Produces(?course, OutflowResult)
and Produces(?course, MaturationResult)
```

Constraint:

```text
CompletedAction(?action)
    does not imply
AllResultsImmediatelyManifest(?action)
```

## 12. Commit Note

```text
VAK_4.85 — Define the threefold result of karmic courses

- identify karmic courses as result-producing determinations
- distinguish dominant, outflow, and maturation results
- preserve the second pāda as provisional pending Bhāṣya clarification
- represent one completed course as producing differentiated result-relations
- keep the Organon interpretation restrained at the Kernel level
```

### First-pass determination

```text
every completed karmic course
    gives three kinds of result:

    dominant result
    outflow-result
    maturation result
```

The exact causal articulation of the three belongs to the Bhāṣya pass.