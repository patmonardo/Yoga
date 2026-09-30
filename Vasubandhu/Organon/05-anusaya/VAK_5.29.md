# VAK_5.29

## 1. Sanskrit (Devanāgarī)

```sanskrit
दुःखहेतुदृगभ्यासप्रहेयाः कामधातुजाः ।
स्वकत्रयैकरूपाप्तामलविज्ञानगोचराः ॥ ५.२९ ॥
```

## 2. Sanskrit (IAST)

```text
duḥkhahetudṛgabhyāsapraheyāḥ kāmadhātujāḥ |
svakatrayaikarūpāptāmalavijñānagocarāḥ || 5.29 ||
```

The Bhāṣya identifies this as the first entry in a condensed exposition
(`piṇḍavibhāṣā`) of the relations between classes of dharmas and classes of
cittas that can take them as object-supports.

## 3. Padaccheda and Lexical Analysis

```text
duḥkha-dṛk-praheyāḥ | hetu-dṛk-praheyāḥ | abhyāsa-praheyāḥ |
kāma-dhātu-jāḥ | svaka-traya | eka-rūpa-āpta | amala-vijñāna-gocarāḥ
```

| Form | Morphology | Contextual sense |
|---|---|---|
| `duḥkha-dṛk-praheyāḥ` | nominative plural compound | dharmas to be abandoned by seeing suffering |
| `hetu-dṛk-praheyāḥ` | nominative plural compound | dharmas to be abandoned by seeing its cause or origination |
| `abhyāsa-praheyāḥ` | nominative plural compound | dharmas to be abandoned by cultivation |
| `kāma-dhātu-jāḥ` | nominative plural compound | belonging to or arisen in the desire-domain |
| `svaka-traya` | compound member | the three [cittas] belonging to their own domain |
| `eka-rūpa-āpta` | compound member | one [citta] belonging to the form-domain |
| `amala-vijñāna` | compound member | undefiled cognition |
| `gocarāḥ` | nominative plural masculine | objects or cognitive ranges |

The tightly compressed first compound distributes `praheyāḥ` across three
path-indexed classes. The Bhāṣya explicitly analyzes `svakatraya` as “their
own three” and `ekarūpāpta` as “one belonging to the form-domain.”

## 4. Grammar

**Subject: three desire-domain dharma-classes**

```text
[duḥkha-dṛk-praheyāḥ
 hetu-dṛk-praheyāḥ
 abhyāsa-praheyāḥ]
    kāma-dhātu-jāḥ
```

These are respectively the desire-domain dharmas abandoned by seeing
suffering, seeing origination, and cultivation. `Hetu-dṛk` is construed by the
Bhāṣya as `samudaya-darśana`, seeing the origination of suffering.

**Predicate: the cittas whose range they are**

```text
[svaka-traya
 eka-rūpa-āpta
 amala-vijñāna]-gocarāḥ
```

The long predicate compound says that those dharmas are objects of five citta-
classes. The Bhāṣya resolves the elliptical counts: three corresponding cittas
of the desire-domain, one cultivation-abandonable citta of the form-domain,
and one undefiled citta.

## 5. Translation

### Literal Translation

> The desire-domain [dharmas] to be abandoned by seeing suffering, by seeing
> its cause, and by cultivation are the objects of their own three [cittas],
> one belonging to the form-domain, and undefiled cognition.

### Bhāṣya-informed study translation

> The desire-domain dharmas abandoned respectively by seeing suffering, seeing
> origination, and cultivation can be taken as objects by five classes of
> citta: the three corresponding classes within the desire-domain, the
> cultivation-abandonable citta of the form-domain, and undefiled citta.

The specification that the single form-domain citta is the cultivation-
abandonable class is supplied by the Bhāṣya.

## 6. Philosophical Translation

> A dharma's place within an afflictive domain does not restrict it to cognition
> of that same status. The three indicated classes of desire-domain dharmas are
> accessible not only to corresponding desire-domain cittas, but also to a
> higher-domain citta and to undefiled cognition. The status of what is known
> and the status of the cognition knowing it must therefore be determined
> separately. By first fixing their admissible object-relations, one can then
> infer where anuśaya-adherence remains possible.

This is not an assertion that every citta capable of cognizing a contaminated
object is thereby contaminated by it. Object-access and afflictive adherence
are distinct relations.

## 7. Technical Vocabulary

**`Piṇḍavibhāṣā` — condensed systematic exposition**

The Bhāṣya's name for the method beginning here. Rather than answer a flood of
individual questions, it compresses them into typed classes and reusable
relations.

**The sixteen dharma- and citta-classes**

The Bhāṣya supplies the governing classification:

```text
5 desire-domain classes
5 form-domain classes
5 formless-domain classes
1 undefiled class
    = 16 dharma-classes

the same division
    = 16 citta-classes
```

The five within each domain are the four classes abandoned by seeing the four
truths and the class abandoned by cultivation. VAK 5.29 begins with three of
the five desire-domain classes.

**`Praheya` — to be abandoned**

A relational determination indexed to a path-operation, not an intrinsic
description detached from that operation.

**`Gocara` — cognitive range or object-field**

What a cognition can range over. The Bhāṣya expresses this relation as the
dharma being the citta's `ālambana`, its object-support.

**`Amala-vijñāna` — undefiled cognition**

The undefiled citta-class in the sixteenfold scheme. Its access to contaminated
dharmas shows that contamination of the object does not by itself contaminate
the cognition.

**`Abhyūhitavya` — to be inferred**

The Bhāṣya's methodological instruction: once the object-support relation is
known, the possible number of anuśayas adhering with respect to that object is
to be reasoned out.

## 8. Logical Determination

The Bhāṣya establishes a two-stage derivation:

```text
1. determine AlambanaOf(DharmaClass, CittaClass)
2. infer possible AnusayaAdherence(DharmaClass, CittaClass)
```

For the present matrix entry:

```text
D = {Kāma-Duḥkha-Dṛk-Praheya,
     Kāma-Hetu-Dṛk-Praheya,
     Kāma-Abhyāsa-Praheya}

C = {the corresponding three Kāma cittas,
     Rūpa-Abhyāsa-Praheya citta,
     Amala citta}

for each d in D:
    ObjectOf(d, c) for the five admissible citta-classes c in C
```

The inferential guard is essential:

```text
ObjectOf(d, c)
    ⇏ AnuśayaAdheres(c, d)

ObjectOf(d, c)
    → candidate relation from which adherence may be inferred
       together with the remaining doctrinal conditions
```

In the project's fourfold architecture, 5.29 concentrates on the middle
relation required for diagnosis:

```text
āśraya   = the domain- and path-typed citta
ālambana = the domain- and path-typed dharma-class

their admissible relation
    constrains which hetu–phala afflictive operations are possible
```

Thus `āśraya–ālambana` is the transactional manifestation through which the
generative structure can be inferred; it is not a bare subject confronting an
independent object.

## 9. Interpretive Note

**Source determination.** The Bhāṣya first classifies dharmas and cittas by the
same sixteenfold scheme. It then makes the `ālambana` relation the lookup key:
determine which citta can take which dharma-class as object, and from that
structured access infer the possible anuśaya relations. VAK 5.29 supplies the
first row-group of this matrix.

**Continuation of VAK 5.28.** The preceding verse showed that an abandoned
dharma may remain the object of a still-unabandoned affliction. The present
verse begins determining exactly which citta-classes can sustain such object-
relations. It replaces the abstract possibility with a typed relational map.

**Yoga–Organon reconstruction.** This is Path rendered as determinate
Objectivity. A path-operation does not merely label a state “abandoned”; it
must know the exact range of cognitive standpoints from which that determination
can still be presented. The bhūmis can therefore display increasingly adequate
rows of transformed relation, while the Path in itself supplies the complete
principle governing their sequence.

**Organon Light.** The extraordinary economy lies in the order of reasoning:

```text
typed classification
    → admissible āśraya–ālambana relations
        → inferred anuśaya determinations
```

This is systematic compression without loss of determinacy. The Bhāṣya does
not abbreviate by omitting the relations; it abbreviates by discovering the
rule from which the many cases can be regenerated.

## 10. OWL++ Seed

```text
Class: DharmaClass
Class: CittaClass
Class: Domain
Class: PathOperation
Class: AnusayaAdherence

ObjectProperty: belongsToDomain
    Domain: DharmaClass or CittaClass
    Range: Domain

ObjectProperty: abandonedBy
    Domain: DharmaClass or CittaClass
    Range: PathOperation

ObjectProperty: takesAsAlambana
    Domain: CittaClass
    Range: DharmaClass

ObjectProperty: permitsInferenceOf
    Domain: AlambanaRelation
    Range: AnusayaAdherence

Individual: KamaSufferingSeeingDharma
    Types: DharmaClass
    belongsToDomain: KamaDhatu
    abandonedBy: SeeingSuffering

Individual: KamaOriginationSeeingDharma
    Types: DharmaClass
    belongsToDomain: KamaDhatu
    abandonedBy: SeeingOrigination

Individual: KamaCultivationDharma
    Types: DharmaClass
    belongsToDomain: KamaDhatu
    abandonedBy: Cultivation

Rule: CorrespondingKamaCitta(?c, ?d)
    -> takesAsAlambana(?c, ?d)

Rule: RupaCultivationCitta(?c)
    AND PresentVerseDharmaClass(?d)
    -> takesAsAlambana(?c, ?d)

Rule: UndefiledCitta(?c)
    AND PresentVerseDharmaClass(?d)
    -> takesAsAlambana(?c, ?d)

Constraint: takesAsAlambana(?c, ?d)
    doesNotEntail ContaminatedBy(?c, ?d)
```

The seed represents the object-support matrix as an inferential interface. It
does not collapse cognition, object, or anuśaya-adherence into one relation.
