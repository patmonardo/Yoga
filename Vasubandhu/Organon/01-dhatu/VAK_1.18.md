# VAK_1.18 — Inclusion by Own-Nature

## 1. Sanskrit (Devanāgarī)

```sanskrit
सर्वसंग्रह एकेन स्कन्धेनायतनेन च ।
धातुना च स्वभावेन परभाववियोगतः ॥ १.१८ ॥
```

## 2. Sanskrit (IAST)

```text
sarvasaṃgraha ekena skandhenāyatanena ca /
dhātunā ca svabhāvena parabhāvaviyogataḥ // 1.18 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| sarva-saṃgrahaḥ | nominative | the inclusion of all |
| ekena | instrumental | by one; carries across the three |
| skandhena | instrumental | by a base |
| āyatanena | instrumental | by an essence |
| dhātunā | instrumental | by a principle |
| svabhāvena | instrumental | by own-nature |
| parabhāva-viyogataḥ | ablatival adverb | separated from another's nature |

*Saṃgraha* is inclusion. The commentary also uses it for the gathering of an
assembly. The two uses are not the same ground. The verse's use is the first.

**Grammar tokens.** Verse-order IAST with sandhi opened. The two *ca*
tokens are retained. The Bhāṣya names Form Base, Mind Essence, and Dharma
Principle; these referents are lexical semantic resolutions, not additional
overt words or new categories invented by the grammar.

```text
# tokens: sarva-saṃgrahaḥ ekena skandhena āyatanena ca dhātunā ca svabhāvena parabhāva-viyogataḥ
```

## 4. Grammar

*Ekena* distributes over three singular instrumental nouns. Their combined
coverage is universal; it is not a universal claim for each category
separately. *Svabhāvena* specifies the mode of inclusion and the final
ablatival expression gives the ground.

```nltk-fcfg
% start S
# tokens: sarva-saṃgrahaḥ ekena skandhena āyatanena ca dhātunā ca svabhāvena parabhāva-viyogataḥ
S[SEM=<?all(?one(?base)(?essence)(?principle))(?own)(?separate)>] -> ALL[SEM=?all] ONE[CASE=ins,NUM=?n,SEM=?one] BASE[CASE=ins,NUM=?n,SEM=?base] ESSENCE[CASE=ins,NUM=?n,SEM=?essence] AND PRINCIPLE[CASE=ins,NUM=?n,SEM=?principle] AND OWN[CASE=ins,SEM=?own] SEPARATION[SEM=?separate]
ALL[CASE=nom,NUM=sg,SEM=<\P.\O.\R.all x.(Dharma(x) -> (P(x) & O(x) & R(x)))>] -> 'sarva-saṃgrahaḥ'
ONE[CASE=ins,NUM=sg,SEM=<\b.\a.\d.\x.(IncludedByOwnNature(x,b) | IncludedByOwnNature(x,a) | IncludedByOwnNature(x,d))>] -> 'ekena'
BASE[CASE=ins,NUM=sg,GEN=m,SEM=<form_base>] -> 'skandhena'
ESSENCE[CASE=ins,NUM=sg,GEN=n,SEM=<mind_essence>] -> 'āyatanena'
AND -> 'ca'
PRINCIPLE[CASE=ins,NUM=sg,GEN=m,SEM=<dharma_principle>] -> 'dhātunā'
OWN[CASE=ins,SEM=<\x.InclusionByOwnNature(x)>] -> 'svabhāvena'
SEPARATION[SEM=<\x.SeparateFromOtherNature(x)>] -> 'parabhāva-viyogataḥ'
```

```nltk-dep
'sarva-saṃgrahaḥ' -> 'skandhena' | 'āyatanena' | 'dhātunā' | 'svabhāvena' | 'parabhāva-viyogataḥ'
'skandhena' -> 'ekena'
'āyatanena' -> 'ca'
'dhātunā' -> 'ca'
```

**Close construe.** All are included by one Base, one Essence, and one
Principle, jointly: by own-nature, because separated from another's nature.

The disjunction is within the scope of “all”: each Dharma falls within
at least one of the three. It is inclusive, allowing overlap at avijñapti.
The singleton category referents encode *ekena*; no shared grammatical
gender is imposed across the differently gendered nouns. The causal
explanation is retained in the prose, while FOL records the inclusion and
separation claims without pretending to derive one from the other.

## 5. Translation

### Literal Translation

> The inclusion of all is by one base, and by one essence, and by one
> principle, by own-nature, because of separation from another's nature.

### Bhāṣya-informed study translation

> All dharmas are included together by one Base, the Form Base; one Essence,
> the Mind Essence; and one Principle, the Dharma Principle. This inclusion is
> by own-nature, through separation from another's nature.

## 6. Philosophical Translation

Again, two lines. The first names the inclusion. The second names the ground.

One base, one essence, one principle, taken together, include all. The
commentary names the three: form-base, mind-essence, dharma-principle. Form is
the Form System: Faculties, meanings, and *avijñapti*. Mind-essence is the
cognition-base. Dharma-principle takes feeling, reflection, formations,
*avijñapti*, and the unconditioned. Overlap is the point. *Avijñapti* sits in
form and in the dharma-principle. The unconditioned have no base, and still
enter.

Own-nature is the warrant. Not isolation. The eye is included in the form-base,
in the eye-essence and the eye-principle, and, when Impure, in suffering and
origin, because it has that nature. It is not included where the nature is not
its own.

The same word gathers an assembly. That gathering is occasional, and
conventional. It happens. It does not place the gathered in the gatherer's own
nature. Two grounds. The science is the difference.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| saṃgraha | inclusion | also, in the example, a gathering |
| sarva-saṃgraha | inclusion of all | joint, not each alone |
| skandha | base | conditioned only |
| upādāna-skandha | appropriated Base | the Impure |
| āyatana | essence | all dharmas |
| dhātu | principle | all dharmas |
| rūpa-skandha | form-base | the Form System |
| mana-āyatana | mind-essence | the cognition-base, under essence |
| dharma-dhātu | dharma-principle | feeling, reflection, formations, *avijñapti*, the unconditioned |
| svabhāva | own-nature | the ground of inclusion |
| parabhāva | another's nature | what will not include it |
| sāsrava | Impure | |
| sāṃketika | conventional | the assembly |
| kādācitka | occasional | why the assembly is conventional |

## 8. Logical Determination

**Kārikā, derived with Bhāṣya-resolved referents.** Universal coverage
does not make the three projections identical.

```nltk-sem
# derived by the section 4 parse
all x.(Dharma(x) -> (((IncludedByOwnNature(x,form_base) | IncludedByOwnNature(x,mind_essence)) | IncludedByOwnNature(x,dharma_principle)) & InclusionByOwnNature(x) & SeparateFromOtherNature(x)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
all x.(Dharma(x) -> (((IncludedByOwnNature(x,form_base) | IncludedByOwnNature(x,mind_essence)) | IncludedByOwnNature(x,dharma_principle)) & InclusionByOwnNature(x) & SeparateFromOtherNature(x)))
```

```nltk-valuation
form_base => form_class
mind_essence => mind_class
dharma_principle => dharma_class
Dharma => {eye,cognition,feeling,avijnapti,unconditioned}
IncludedByOwnNature => {(eye,form_class),(cognition,mind_class),(feeling,dharma_class),(avijnapti,form_class),(avijnapti,dharma_class),(unconditioned,dharma_class)}
InclusionByOwnNature => {eye,cognition,feeling,avijnapti,unconditioned}
SeparateFromOtherNature => {eye,cognition,feeling,avijnapti,unconditioned}
```

**Model checks.** Removing a Dharma's sole inclusion must fail, but removing
one of avijñapti's two inclusions leaves coverage intact. Tests separately
pin its two classifications as Bhāṣya data. The model refutes “every Dharma
belongs to all three.” Unconditioned dharmas have no Base membership here.

**Dependency on the earlier system.** The valuation uses Form and Dharma
determinations from 1.04–1.15 as declared inputs, not as results proved by
this verse. Those sections still need the Grammar–Logic pass. The following
preserves the commentary's wider census and own-nature explanation.

```text
bases                  → all conditioned
appropriated Bases → all Impure
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

1.19 not opened
```

The eye is the commentary's case. Several determinations, one nature that it
has. Not three identical wholes.

## 9. Interpretive Note

**Translation note.** The Bhāṣya specifies the three as Form Base, Mind
Essence, and Dharma Principle, which jointly include all dharmas rather than
each doing so alone. Own-nature is the classificatory ground; an occasional
gathering of an assembly is a distinct, conventional use of saṃgraha.

The hinge is *ekena*, distributed, then *svabhāvena*. Interpretation of the
joint inclusion is in the Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_18 a vak:Karika ;
    vak:hasTopic vak:InclusionByOwnNature ;
    vak:belongsTo vak:Dhatunirdesa .

vak:InclusionOfAll vak:by vak:FormBase, vak:MindEssence, vak:DharmaPrinciple ;
    vak:eachAlone false ;
    vak:ground vak:OwnNature .
vak:BasesOfAppropriation vak:include vak:Impure .
vak:Avijnapti vak:in vak:FormBase, vak:DharmaPrinciple .
vak:AssemblyGathering vak:isClassificatoryInclusion false .
```
