# VAK 5.52

## Sanskrit

तदन्ये भावनाहेयाः स्वतन्त्राश्च तथा मलाः ।
कामेऽशुभाः त्रयो द्विधा परेणाव्याकृतास्ततः ॥ ५.५२ ॥

## IAST

tad-anye bhāvanā-heyāḥ svatantrāś ca tathā malāḥ /
kāme 'śubhāḥ trayo dvidhā pareṇāvyākṛtās tataḥ // 5.52 //

## Padaccheda

tat-anye | bhāvanā-heyāḥ | svatantrāḥ | ca | tathā | malāḥ | kāme | aśubhāḥ | trayaḥ | dvidhā | pareṇa | avyākṛtāḥ | tataḥ

## Grammar

- **tat-anye** — nominative plural masculine, “the others than those,” referring to the remaining upakleśas after the five stated in VAK 5.51 as twofold.
- **bhāvanā-heyāḥ** — nominative plural masculine, “to be abandoned by cultivation.”
- **svatantrāḥ** — nominative plural masculine, “independent,” here indicating derivative afflictions that arise as distinct mental factors rather than merely as names for another kleśa.
- **ca tathā malāḥ** — “and likewise the stains,” extending the same rule to the six kleśa-malas.
- **kāme** — locative singular, “in the desire-domain.”
- **aśubhāḥ** — nominative plural masculine, “unwholesome.”
- **trayaḥ** — nominative plural masculine, “three.”
- **dvidhā** — indeclinable, “twofold,” here indicating a double ethical determination according to domain.
- **pareṇa** — instrumental singular, “in the higher [domains],” that is, beyond the desire-domain.
- **avyākṛtāḥ** — nominative plural masculine, “indeterminate,” neither wholesome nor unwholesome in karmic classification.
- **tataḥ** — indeclinable, “therefore,” grounding the ethical distinction in domain and function.

## Literal Translation

The others are to be abandoned by cultivation; likewise the independent [upakleśas] and the stains. In the desire-domain, three are unwholesome; they are twofold, since in the higher [domains] they are indeterminate.

## Philosophical Translation

All remaining derivative afflictions are removed through cultivation, and the same holds for those that arise as independent factors and for the six stains. Their ethical determination, however, changes with the domain: three are unwholesome in the desire-domain but become karmically indeterminate in the higher domains.

## Structural Analysis

VAK 5.51 distinguished five upakleśas that may be abandoned by either seeing or cultivation:

```text
āhrīkya
anapatrāpya
styāna
middha
auddhatya
```

VAK 5.52 now states the complementary rule:

```text
all remaining upakleśas
    → abandoned by cultivation
```

and extends it to:

```text
svatantra-upakleśas
kleśa-malas
```

The decisive shift is from the **origin** of the affliction to its **mode of removal** and then to its **ethical status by domain**.

```text
genesis
    ↓
mode of abandonment
    ↓
ethical determination
```

This verse therefore introduces a three-axis classification:

```text
what produces the state
how the state is abandoned
what karmic value it has in a given domain
```

## Technical Vocabulary

### Bhāvanā-heya

A determination to be abandoned through repeated cultivation rather than by a single act of seeing.

```text
bhāvanā
    = sustained transformation of the continuum

heya
    = that which is to be abandoned
```

A bhāvanā-heya affliction persists not merely because of false judgment but because it has become habitual, affective, and embodied in the stream.

### Svatantra

Here **svatantra** does not mean metaphysically self-sufficient. It marks a derivative affliction that functions as a distinct mental factor.

```text
root-dependent in genesis
    but
functionally distinct in manifestation
```

This distinction prevents two opposite errors:

```text
reductionism
    every upakleśa is only another name for its root

independence
    every upakleśa exists without a root
```

### Mala

A stain is an affliction considered through the deformation it imposes upon conduct, appearance, relation, or self-presentation.

### Aśubha

Unwholesome in the karmic sense: ethically charged so as to produce painful result.

### Avyākṛta

Karmically indeterminate: neither wholesome nor unwholesome.

The same named mental factor may change karmic status according to the domain in which it functions.

## Doctrinal Determination

The verse teaches that removal must correspond to the way an affliction persists.

Those grounded in wrong seeing can be cut by insight. Those maintained as habit must be worn away by cultivation.

```text
false view
    → corrected by seeing

habitual disposition
    → transformed by cultivation
```

The remaining upakleśas and the stains belong mainly to the second class. They have become concrete modes of reaction, conduct, and self-presentation.

The Path must therefore do more than identify them conceptually. It must repeatedly alter the conditions under which they arise.

The second half adds a subtle doctrinal point: ethical determination is not fixed by name alone.

Three factors are:

```text
unwholesome in kāmadhātu
indeterminate in the higher domains
```

The Bhāṣya must identify these three precisely. The likely doctrinal significance is that their coarse desire-domain operation produces unwholesome karma, while their subtler higher-domain forms no longer have the same karmic force.

Thus:

```text
same class-name
    ≠
identical ethical value in every domain
```

## Logical Determination

VAK 5.52 distinguishes **identity of determination** from **identity of function**.

A mental factor may remain nominally the same while its ethical role changes according to domain.

```text
factor F in domain D1
    has karmic value K1

factor F in domain D2
    has karmic value K2
```

Therefore classification is relational:

```text
ethical value
    = function of
factor + domain + mode of operation
```

This is important for the logic of the Path. One cannot infer the needed countermeasure merely from the name of the affliction.

The Path requires a map containing at least:

```text
manifest state
root affliction
domain
ethical value
mode of abandonment
```

The verse thus formalizes the “markers along the way”:

```text
recognize where the determination appears
    ↓
classify how it functions there
    ↓
apply the correct mode of abandonment
```

## Organon Note

This verse suggests that Dharma-dominance should not mean passive submission to a list of prohibitions. It means that experience becomes progressively articulated by a discriminative map.

```text
restricted view
    → marker: darśana-heya

habitual behavior
    → marker: bhāvanā-heya

context-sensitive ethical status
    → marker: domain-dependent valuation
```

A practical reason system modeled on this verse must avoid global labels such as:

```text
this state is always unwholesome
```

and instead represent:

```text
this state
under these conditions
in this domain
has this ethical force
and requires this transformation
```

The Path is therefore not merely a sequence of commands. It is an increasingly exact topology of determinations.

## OWL++ Seed

```ttl
vak:DerivativeAffliction a owl:Class ;
  rdfs:subClassOf vak:AfflictiveDetermination .

vak:IndependentDerivativeAffliction a owl:Class ;
  rdfs:subClassOf vak:DerivativeAffliction .

vak:AfflictiveStain a owl:Class ;
  rdfs:subClassOf vak:DerivativeAffliction .

vak:CultivationAbandonable a owl:Class .
vak:Unwholesome a owl:Class .
vak:Indeterminate a owl:Class .
vak:Domain a owl:Class .

vak:hasAbandonmentMode a owl:ObjectProperty .
vak:hasEthicalValueInDomain a owl:ObjectProperty .
vak:occursInDomain a owl:ObjectProperty .

vak:DesireDomain a vak:Domain .
vak:HigherDomain a vak:Domain .
```

Possible reified valuation pattern:

```ttl
vak:EthicalValuation a owl:Class .

vak:ofMentalFactor a owl:ObjectProperty .
vak:inDomain a owl:ObjectProperty .
vak:hasEthicalValue a owl:ObjectProperty .
```

This avoids assigning one timeless ethical value directly to a mental factor when the verse makes valuation domain-dependent.

## Bhāṣya Questions

1. Which precise factors are included under **tad-anye**?
2. What does the Bhāṣya mean by **svatantra upakleśa**?
3. Are all six **kleśa-malas** exclusively bhāvanā-heya?
4. Which three factors are unwholesome in the desire-domain but indeterminate in the higher domains?
5. Does **dvidhā** refer solely to the ethical twofoldness of those three, or to another classification as well?
6. Why does the same factor change from aśubha to avyākṛta according to domain?
7. What practical distinction follows between abandoning a factor by seeing and abandoning it by cultivation?
