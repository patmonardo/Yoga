# VAK_1.18 — Inclusion by Own-Nature

## 1. Sanskrit (Devanāgarī)

> सर्वसंग्रह एकेन स्कन्धेनायतनेन च ।
>
> धातुना च स्वभावेन परभाववियोगतः ॥ १.१८ ॥॥

## 2. Sanskrit (IAST)

> sarvasaṃgraha ekena skandhenāyatanena ca /
>
> dhātunā ca svabhāvena parabhāvaviyogataḥ // 1.18 //

## 3. Lexical Analysis

```text
sarvasaṃgrahaḥ     → sarva-saṃgrahaḥ
skandhenāyatanena  → skandhena + āyatanena
parabhāvaviyogataḥ → para-bhāva-viyogataḥ
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| sarva-saṃgrahaḥ | nominative masculine singular | the inclusion of all |
| ekena | instrumental singular | by one; carries across the three |
| skandhena | instrumental masculine singular | by a base |
| āyatanena | instrumental neuter singular | by an essence |
| ca | indeclinable | and |
| dhātunā | instrumental masculine singular | by a principle |
| svabhāvena | instrumental singular | by own-nature |
| para-bhāva | compound member | another's nature |
| viyogataḥ | ablatival adverb | because of separation from |

*Saṃgraha* is inclusion. The Bhāṣya also uses it for the gathering of an
assembly. The two uses are not the same ground. The verse's use is the
first.

## 4. Grammar

```text
sarva-saṃgrahaḥ
    = ekena skandhena
    + ekena āyatanena
    + ekena dhātunā

ground
    = svabhāvena
    because parabhāva-viyogataḥ
```

The subject is the inclusion of all. Three instrumentals name the means.
*Ekena* distributes: by one base, by one essence, and by one principle.
The Bhāṣya names them. Form-base, mind-essence, dharma-principle. Jointly.
Not each alone.

*Svabhāvena* is the ground. *Parabhāvaviyogataḥ* is why the other nature
will not serve. A dharma is separate from another's nature. It is not
included by the nature it is separate from.

## 5. Translation

### Literal Translation

The inclusion of all is by one base, and by one essence, and by one
principle, by own-nature, because of separation from another's nature.

### Bhāṣya-informed study translation

All dharmas are included jointly by the form-base, the mind-essence, and
the dharma-principle. The inclusion is by a dharma's own nature, not by
another's nature, from which it is separate.

Bases include the conditioned. Bases of appropriation include the Impure.
Essences and principles include all dharmas, the unconditioned among them.

## 6. Philosophical Translation

Again, two lines. The first names the inclusion. The second names the
ground.

This is the twist of the skandha puzzle, and it is not a fourth list.
One base, one essence, one principle, taken together, include all. The
commentary names the three: form-base, mind-essence, dharma-principle.
Form gathers the faculties, the conditions, and *avijñapti*. Mind-essence
is the principle-base. Dharma-principle takes feeling, reflection,
formations, *avijñapti*, and the unconditioned. Overlap is the point.
*Avijñapti* sits in form and in the dharma-principle. The unconditioned
have no base, and still enter.

Own-nature is the warrant. Not isolation. The eye is included in the
form-base, in the eye-essence and the eye-principle, and, when Impure, in
suffering and origin, because it has that nature. It is not included
where the nature is not its own.

The same word gathers an assembly. That gathering is occasional, and
conventional. It happens. It does not place the gathered in the gatherer's
own nature. Two grounds. The science is the difference.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| saṃgraha | inclusion | also, in the example, a gathering |
| sarva-saṃgraha | inclusion of all | joint, not each alone |
| skandha | base | conditioned only |
| upādāna-skandha | base of appropriation | the Impure |
| āyatana | essence | all dharmas |
| dhātu | principle | all dharmas |
| rūpa-skandha | form-base | one of the three selected |
| mana-āyatana | mind-essence | the principle-base, under essence |
| dharma-dhātu | dharma-principle | feeling, reflection, formations, *avijñapti*, the unconditioned |
| svabhāva | own-nature | the ground of inclusion |
| parabhāva | another's nature | what will not include it |
| sāsrava | Impure | not "with outflows" |
| sāṃketika | conventional | the assembly |
| kādācitka | occasional | why the assembly is conventional |

## 8. Logical Determination

```text
bases                  → all conditioned
bases of appropriation → all Impure
essences and principles → all dharmas

joint inclusion
    form-base
    + mind-essence
    + dharma-principle
    → all dharmas
    not each alone
    overlap at avijñapti
    unconditioned have no base

inclusion
    by own-nature
    not by the nature one is separate from

assembly
    occasional
    conventional
    not this inclusion
```

The eye is the commentary's case. Several determinations, one nature that
it has. Not three identical wholes.

## 9. Interpretive Note

The hinge is *ekena*, distributed, then *svabhāvena*. Interpretation of
the joint inclusion is in the Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_18 a vak:Karika ;
    vak:hasTopic vak:InclusionByOwnNature ;
    vak:belongsTo vak:Dhatunirdesa .

vak:InclusionOfAll vak:by vak:FormBase, vak:MindEssence, vak:DharmaPrinciple ;
    vak:eachAlone false ;
    vak:ground vak:OwnNature ;
    vak:notBy vak:AnothersNature .

vak:Bases vak:include vak:Conditioned .
vak:BasesOfAppropriation vak:include vak:Impure .
vak:Essences vak:include vak:AllDharmas .
vak:Principles vak:include vak:AllDharmas .

vak:Avijnapti vak:in vak:FormBase, vak:DharmaPrinciple .
vak:Unconditioned vak:hasBase false ;
    vak:enters vak:DharmaPrinciple .

vak:AssemblyGathering vak:occasional true ;
    vak:conventional true ;
    vak:isClassificatoryInclusion false .
```
