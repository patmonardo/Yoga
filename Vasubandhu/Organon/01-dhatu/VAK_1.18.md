# VAK_1.18 — The Skandha Theory of Inclusion by Own-Nature

## 1. Sanskrit (Devanāgarī)

> सर्वसंग्रह एकेन स्कन्धेनायतनेन च ।
>
> धातुना च स्वभावेन परभाववियोगतः ॥ १.१८ ॥

## 2. Sanskrit (IAST)

> sarvasaṃgraha ekena skandhenāyatanena ca /
>
> dhātunā ca svabhāvena parabhāvaviyogataḥ // 1.18 //

## 3. Lexical Analysis

```text
sarvasaṃgrahaḥ          → sarva-saṃgrahaḥ
skandhenāyatanena       → skandhena āyatanena
parabhāvaviyogataḥ      → para-bhāva-viyogataḥ
```

| Form | Morphology | Lexical force here |
|---|---|---|
| sarva-saṃgrahaḥ | nominative masculine singular compound | inclusion of all; the Bhāṣya specifies its scope |
| ekena | instrumental masculine/neuter singular | by one; repeated with the three classifications |
| skandhena | instrumental masculine singular | by one base |
| āyatanena | instrumental neuter singular | by one essence |
| ca | conjunction | and |
| dhātunā | instrumental masculine singular | by one principle |
| svabhāvena | instrumental masculine/neuter singular | by own-nature |
| para-bhāva | masculine compound member | another's nature |
| viyogataḥ | ablatival adverbial formation | because of separation or distinction from |

`Saṃgraha` is inclusion or gathering. The verse's threefold classificatory
use is specified by the Bhāṣya; its closing assembly example gives a
practical, conventional use of the same term. The English should preserve
that relation rather than assume both uses mean physical containment or
that conventional gathering is unreal.

## 4. Grammar

`Sarva-saṃgrahaḥ` is the subject. The three instrumental phrases name the
coordinated terms through which all are included:

```text
ekena skandhena
ekena āyatanena
ekena dhātunā
```

The Bhāṣya supplies their referents:

```text
rūpaskandha
    → Form Base

mana-āyatana
    → Mind Essence

dharma-dhātu
    → Dharma Principle
```

The three do not name rival wholes. Together they cover all dharmas; no
single selected member is said to do so alone.

`Svabhāvena` states the ground of inclusion; `parabhāvaviyogataḥ` gives its
negative determination: a dharma is separate from another's nature and
cannot be classified by that alien nature. The contrast is not between
isolated things and all relations. It distinguishes principial membership
from causal, supportive, object-related, and practical relations, which the
earlier verses and the Bhāṣya continue to recognize.

The Bhāṣya's example is exact:

```text
eye faculty
    → rūpa-skandha
    → eye-āyatana
    → eye-dhātu
    → suffering and origin, when sāsrava

eye faculty
    ↛ classifications whose nature it does not have
```

The eye-faculty example and its particular classifications are supplied by
the Bhāṣya. The verse's compact rule should not be expanded into a
metaphysical thesis that every dharma exists in absolute isolation.

## 5. Translation

### Close syntactic construe

> The inclusion of all is by one base, one essence, and one principle, by own-nature, because of separation from another's nature.

### Bhāṣya-informed translation

> All dharmas are included together through the Form Base, Mind Essence, and Dharma Principle. Inclusion is by a dharma's own nature, not by another's nature from which it is distinct.

The Bhāṣya further distinguishes the scopes of the three classifications:

```text
bases                    → all conditioned dharmas
bases of appropriation   → all Impure dharmas
essences and principles  → all dharmas, including the unconditioned
```

## 6. Philosophical Translation

```text
<skandha, āyatana, dhātu>
    = <Base, Essence, Principle>

VAK 1.18
    = Form Base + Mind Essence + Dharma Principle
      jointly including all dharmas
```

The verse compresses the Skandha Theory: all is comprehended through one
base, one essence, and one principle. Own-nature grounds inclusion;
separation from another nature limits it. This is not one container or
three rival wholes. The selected classifications work together, while
their differences remain.

The eye example makes the point concrete: one faculty enters several
classifications because of the nature it has. The assembly example uses
“gathering” in a practical, occasional sense, not as another ground of
principial membership.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| saṃgraha | inclusion / gathering | classificatory and practical senses distinguished by the Bhāṣya |
| sarva-saṃgraha | inclusion of all | joint coverage through the three selected classifications |
| svabhāva | own-nature | ground of inclusion |
| parabhāva | another's nature | the distinct determination from which a dharma is separated |
| parabhāva-viyoga | separation from another's nature | the negative limit that makes inclusion determinate |
| skandha | base | includes conditioned dharmas |
| upādāna-skandha | base of appropriation | includes Impure dharmas |
| āyatana | essence | includes all dharmas with dhātu |
| dhātu | principle | includes all dharmas with āyatana |
| sāṃketika | conventional | practical gathering by shared designation |
| kādācitka | occasional | contingent character of the assembly example |

## 8. Logical Determination

```text
skandhas                  → all conditioned dharmas
upādāna-skandhas          → all Impure dharmas
āyatanas + dhātus         → all dharmas

selected
    form-base
    + mind-essence
    + dharma-principle    → joint inclusion of all dharmas

ground                    → own-nature
limit                     → separation from another's nature

assembly-gathering        → practical, conventional, occasional
                          ↛ inclusion by own-nature
```

## 9. Interpretive Note

The hinge is *svabhāvena*: comprehensive inclusion is grounded in own-nature,
not in another's nature. The selected base, essence, and principle jointly
cover all dharmas without becoming one undifferentiated classification.
Interpretation of that rule and the assembly contrast is in the Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_18
    a vak:Karika ;
    rdfs:label "VAK 1.18" ;
    vak:hasTopic vak:ExhaustiveInclusionByIntrinsicNature ;
    vak:belongsTo vak:Dhatunirdesa .

vak:StrictInclusion
    vak:groundedIn vak:OwnNature ;
    vak:excludes vak:AnotherNature ;
    vak:distinctFrom vak:ConventionalGathering .

vak:SkandhaSystem
    vak:includes vak:AllConditionedDharmas .

vak:UpadanaSkandhaSystem
    vak:includes vak:AllSasravaDharmas .

vak:AyatanaSystem
    vak:includes vak:AllDharmas .

vak:DhatuSystem
    vak:includes vak:AllDharmas ;
    vak:organizesBy vak:Principle .

vak:ExhaustiveDharmaField
    vak:isCrossMappedBy vak:RupaSkandha , vak:ManaAyatana ,
        vak:DharmaDhatu .
```
