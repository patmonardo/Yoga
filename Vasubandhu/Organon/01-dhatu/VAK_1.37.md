# VAK_1.37 — Maturation, Reinforcement, and Causal Continuation

## 1. Sanskrit (Devanāgarī)

```sanskrit
विपाकजौपचयिकाः पञ्चाध्यात्मं विपाकजः ।
न शब्दोऽप्रतिघा अष्टौ नैःष्यन्दिकविपाकजाः ॥ १.३७ ॥
```

## 2. Sanskrit (IAST)

```text
vipākajaupacayikāḥ pañcādhyātmaṃ vipākajaḥ /
na śabdo 'pratighā aṣṭau naiḥṣyandika-vipākajāḥ // 1.37 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| vipākaja-aupacayikāḥ | dvandva of two adjectives; nominative masculine plural | maturation-born and upacaya-reinforced |
| pañca | numeral | five |
| adhyātmam | adverbial accusative | internal: the five Faculty Principles |
| vipākajaḥ | vipāka-ja; nominative masculine singular | maturation-born |
| na | negative particle | not |
| śabdaḥ | nominative masculine singular | Sound |
| apratighāḥ | a-pratigha; nominative masculine plural | non-resistant |
| aṣṭau | numeral | eight: the seven consciousness Principles and the Dharma Principle |
| naiḥṣyandika-vipākajāḥ | dvandva of two adjectives; nominative masculine plural | continuity-born and maturation-born |

The line break joins *vipākajaḥ* with *na śabdaḥ*: Sound is not
maturation-born. *Vipākaja* is *vipāka-hetu-ja* with the middle member
dropped, as in *go-ratha*.

`Naiḥṣyandika` should not be confused with `sāsrava`, “with outflows.” Here
it names production through a corresponding causal flow, specified in the
Bhāṣya through `sabhāgahetu` and `sarvatragahetu`.

**Grammar tokens.** Verse-order IAST with sandhi opened
(`vipākajaupacayikāḥ` → *vipākaja-aupacayikāḥ*, `pañcādhyātmaṃ` → *pañca
adhyātmam*, `śabdo 'pratighā` → *śabdaḥ apratighāḥ*) and compound
boundaries marked. *Vipāka-ja* occurs three times: in the first dvandva,
alone, and in the last dvandva.

```text
# tokens: vipākaja-aupacayikāḥ pañca adhyātmam vipākajaḥ na śabdaḥ apratighāḥ aṣṭau naiḥṣyandika-vipākajāḥ
```

## 4. Grammar

Three clauses. The first predicates a plural dvandva of the five internal
Principles; the numeral's count matches the class. The second is
singular: *vipākajaḥ* agrees in number with *śabdaḥ*, and that agreement
is what binds the end of the first line to the beginning of the second.
The third predicates a plural dvandva of the eight non-resistant
Principles; the count matches the class of 1.29, eighteen less ten
resistant.

Each dvandva predicates two modes of a Principle, and a mode is
predicated through its instances: some instance is born that way. The
verse does not say each instance is born both ways.

```nltk-fcfg
% start S
# tokens: vipākaja-aupacayikāḥ pañca adhyātmam vipākajaḥ na śabdaḥ apratighāḥ aṣṭau naiḥṣyandika-vipākajāḥ
S[SEM=<(?a & ?b & ?c)>] -> FIVECL[SEM=?a] SOUNDCL[SEM=?b] EIGHTCL[SEM=?c]
FIVECL[SEM=<all x.(?k(x) -> ?p(x))>] -> PRED[NUM=pl,SEM=?p] NUMR[CNT=?n] ADHY[CNT=?n,SEM=?k]
SOUNDCL[SEM=<-?p(?s)>] -> PRED[NUM=?num,SEM=?p] NA SABDA[NUM=?num,SEM=?s]
EIGHTCL[SEM=<all x.(?k(x) -> ?p(x))>] -> APRAT[NUM=pl,CNT=?n,SEM=?k] NUMR[CNT=?n] PRED[NUM=pl,SEM=?p]
PRED[NUM=pl,SEM=<\x.(exists i.(InstanceOf(i,x) & Born(i,vipaka)) & exists i.(InstanceOf(i,x) & Born(i,upacaya)))>] -> 'vipākaja-aupacayikāḥ'
PRED[NUM=sg,SEM=<\x.exists i.(InstanceOf(i,x) & Born(i,vipaka))>] -> 'vipākajaḥ'
PRED[NUM=pl,SEM=<\x.(exists i.(InstanceOf(i,x) & Born(i,naisyandika)) & exists i.(InstanceOf(i,x) & Born(i,vipaka)))>] -> 'naiḥṣyandika-vipākajāḥ'
NUMR[CNT=5] -> 'pañca'
NUMR[CNT=8] -> 'aṣṭau'
ADHY[CNT=5,SEM=<\x.InternalFive(x)>] -> 'adhyātmam'
NA -> 'na'
SABDA[NUM=sg,SEM=<sound>] -> 'śabdaḥ'
APRAT[NUM=pl,CNT=8,SEM=<\x.NonResistant(x)>] -> 'apratighāḥ'
```

```nltk-dep
'vipākaja-aupacayikāḥ' -> 'adhyātmam'
'adhyātmam' -> 'pañca'
'vipākajaḥ' -> 'na' | 'śabdaḥ'
'naiḥṣyandika-vipākajāḥ' -> 'apratighāḥ'
'apratighāḥ' -> 'aṣṭau'
```

**Close construe.** The five internal are maturation-born and
upacaya-reinforced. Sound is not maturation-born. The eight non-resistant
are continuity-born and maturation-born.

The negation in the second clause is narrow: it denies one mode to Sound,
not every mode. The Bhāṣya gives Sound upacaya and continuity instances,
and excludes maturation because Sound proceeds from effort. Upacaya is
denied to the eight by the Bhāṣya, not by the verse: the non-resistant
lack accumulation.

## 5. Translation

### Literal Translation

> The five internal [Faculty Principles] are maturation-born and upacaya-
> reinforced. Sound is not maturation-born. The eight non-resistant
> Principles include continuity-born and maturation-born instances.

### Bhāṣya-informed study translation

> The five internal Faculty Principles are maturation-born and reinforced
> through increase. Sound is not maturation-born. The eight non-resistant
> Principles have instances born of causal continuity and of maturation.

## 6. Philosophical Translation

> A Principle is determined not only by its present character but also by the manner in which its continuity is generated. The Faculties possess a maturation-born constitution that can be maintained and reinforced through living conditions. Sound is an event initiated through present effort rather than a direct maturation-result. The non-resistant Cognition and Dharma Principles lack upacaya reinforcement yet remain subject to causal continuity and maturation.

Interpretation:

> The Principle of the Agent now receives a genesis protocol. Its Faculties are inherited capacities whose maturation-continuity is protected and reinforced by living conditions. Cognition Principles are non-resistant without being causally ungrounded. The Agent is therefore not posited outside causality; it is a differentiated system of generated and maintained capacities.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| vipākaja | maturation-born | generated from karma that has reached the time of fruition |
| vipākahetu | maturation Ground | causal basis expanded from the abbreviated compound |
| vipākasantāna | maturation-continuity | karmically generated continuum |
| aupacayika | upacaya-reinforced | increased through nourishment and other living conditions |
| upacayasantāna | reinforcement-continuity | continuity protecting and strengthening maturation like a surrounding wall |
| anupaghāta | non-injury / preservation | absence of damage, distinguished from positive growth |
| naiḥṣyandika | continuity-born | generated through homogeneous or universally operative causes |
| sabhāgahetu | homogeneous Ground | produces corresponding factors in a causal series |
| sarvatragahetu | universally operative Ground | continuity-ground especially relevant to afflicted dharmas |
| īhā | effort / exertion | immediate initiating condition excluding sound from maturation-status |
| paramparā | mediated causal succession | explains how karma can indirectly condition voice without making sound itself vipākaja |
| apratigha | non-resistant | not resistant, not causally unconditioned |

## 8. Logical Determination

**Kārikā, derived.** Every internal Faculty Principle has maturation-born
and upacaya-reinforced instances; Sound has no maturation-born instance;
every non-resistant Principle has continuity-born and maturation-born
instances.

```nltk-sem
# derived by the section 4 parse
(all x.(InternalFive(x) -> (exists i.(InstanceOf(i,x) & Born(i,vipaka)) & exists i.(InstanceOf(i,x) & Born(i,upacaya)))) & -exists i.(InstanceOf(i,sound) & Born(i,vipaka)) & all x.(NonResistant(x) -> (exists i.(InstanceOf(i,x) & Born(i,naisyandika)) & exists i.(InstanceOf(i,x) & Born(i,vipaka)))))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(all x.(InternalFive(x) -> (exists i.(InstanceOf(i,x) & Born(i,vipaka)) & exists i.(InstanceOf(i,x) & Born(i,upacaya)))) & -exists i.(InstanceOf(i,sound) & Born(i,vipaka)) & all x.(NonResistant(x) -> (exists i.(InstanceOf(i,x) & Born(i,naisyandika)) & exists i.(InstanceOf(i,x) & Born(i,vipaka)))))
# THEORY prose
# EXPECT prose T
all i.all m.(Born(i,m) -> ((m = vipaka) | (m = upacaya) | (m = naisyandika)))
all x.(InternalFive(x) <-> SenseFaculty(x))
all x.(NonResistant(x) <-> (CittaPrinciple(x) | (x = dharma_principle)))
all x.(InternalFive(x) -> -exists i.(InstanceOf(i,x) & Born(i,naisyandika)))
all i.(Born(i,vipaka) <-> GeneratedBy(i,vipaka_ground))
all i.(Born(i,naisyandika) <-> (GeneratedBy(i,sabhaga_ground) | GeneratedBy(i,sarvatraga_ground)))
exists i.(InstanceOf(i,sound) & Born(i,upacaya)) & exists i.(InstanceOf(i,sound) & Born(i,naisyandika))
all i.(InstanceOf(i,sound) -> FromEffort(i))
all i.(FromEffort(i) -> -Born(i,vipaka))
all i.all x.((InstanceOf(i,x) & Born(i,upacaya)) -> Accumulated(x))
all x.(NonResistant(x) -> -Accumulated(x))
exists b.(b = brahmacarya & PreventsInjury(b) & -Increases(b))
exists u.(u = upacaya_continuum & Protects(u,vipaka_continuum) & -(u = vipaka_continuum))
all a.(VoiceAccount(a) -> Mediates(a,karma,sound))
exists i.(InstanceOf(i,sound) & KarmaDescended(i) & -Born(i,vipaka))
exists i.(InstanceOf(i,dharma_principle) & Unconditioned(i) & -exists m.Born(i,m))
# THEORY rejected_sound_maturation_born
# EXPECT rejected_sound_maturation_born F
exists i.(InstanceOf(i,sound) & Born(i,vipaka))
# THEORY rejected_sound_without_any_mode
# EXPECT rejected_sound_without_any_mode F
all i.(InstanceOf(i,sound) -> -exists m.Born(i,m))
# THEORY rejected_each_instance_both_ways
# EXPECT rejected_each_instance_both_ways F
all x.(NonResistant(x) -> all i.(InstanceOf(i,x) -> (Born(i,naisyandika) & Born(i,vipaka))))
# THEORY rejected_faculty_continuity_class
# EXPECT rejected_faculty_continuity_class F
exists i.exists x.(InternalFive(x) & InstanceOf(i,x) & Born(i,naisyandika))
# THEORY rejected_eight_reinforced
# EXPECT rejected_eight_reinforced F
exists i.exists x.(NonResistant(x) & InstanceOf(i,x) & Born(i,upacaya))
# THEORY rejected_celibacy_increases
# EXPECT rejected_celibacy_increases F
exists b.(b = brahmacarya & Increases(b))
# THEORY rejected_unconditioned_produced
# EXPECT rejected_unconditioned_produced F
all i.(InstanceOf(i,dharma_principle) -> exists m.Born(i,m))
# THEORY rejected_remote_ancestry_decides
# EXPECT rejected_remote_ancestry_decides F
all i.(KarmaDescended(i) -> Born(i,vipaka))
```

```nltk-valuation
vipaka => vipaka_m
upacaya => upacaya_m
naisyandika => naisyandika_m
sound => sabda_d
dharma_principle => dharma_d
vipaka_ground => vipaka_h
sabhaga_ground => sabhaga_h
sarvatraga_ground => sarvatraga_h
brahmacarya => brahmacarya_p
upacaya_continuum => upacaya_santana
vipaka_continuum => vipaka_santana
third_account => parampara_3
fifth_account => parampara_5
karma => karma_k
AmongEighteen => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d,mano_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d,dharma_d}
SenseFaculty => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d}
InternalFive => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d}
CittaPrinciple => {mano_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d}
NonResistant => {mano_d,caksurvijnana_d,srotravijnana_d,ghranavijnana_d,jihvavijnana_d,kayavijnana_d,manovijnana_d,dharma_d}
Accumulated => {caksur_d,srotra_d,ghrana_d,jihva_d,kaya_d,rupa_d,sabda_d,gandha_d,rasa_d,sprastavya_d}
InstanceOf => {(dharma_asamskrta,dharma_d),(caksur_vip,caksur_d),(caksur_upa,caksur_d),(srotra_vip,srotra_d),(srotra_upa,srotra_d),(ghrana_vip,ghrana_d),(ghrana_upa,ghrana_d),(jihva_vip,jihva_d),(jihva_upa,jihva_d),(kaya_vip,kaya_d),(kaya_upa,kaya_d),(sabda_upa,sabda_d),(sabda_nai,sabda_d),(sabda_brahma,sabda_d),(mano_nai,mano_d),(mano_vip,mano_d),(caksurvijnana_nai,caksurvijnana_d),(caksurvijnana_vip,caksurvijnana_d),(srotravijnana_nai,srotravijnana_d),(srotravijnana_vip,srotravijnana_d),(ghranavijnana_nai,ghranavijnana_d),(ghranavijnana_vip,ghranavijnana_d),(jihvavijnana_nai,jihvavijnana_d),(jihvavijnana_vip,jihvavijnana_d),(kayavijnana_nai,kayavijnana_d),(kayavijnana_vip,kayavijnana_d),(manovijnana_nai,manovijnana_d),(manovijnana_vip,manovijnana_d),(dharma_nai,dharma_d),(dharma_vip,dharma_d)}
Born => {(caksur_vip,vipaka_m),(caksur_upa,upacaya_m),(srotra_vip,vipaka_m),(srotra_upa,upacaya_m),(ghrana_vip,vipaka_m),(ghrana_upa,upacaya_m),(jihva_vip,vipaka_m),(jihva_upa,upacaya_m),(kaya_vip,vipaka_m),(kaya_upa,upacaya_m),(sabda_upa,upacaya_m),(sabda_nai,naisyandika_m),(sabda_brahma,naisyandika_m),(mano_nai,naisyandika_m),(mano_vip,vipaka_m),(caksurvijnana_nai,naisyandika_m),(caksurvijnana_vip,vipaka_m),(srotravijnana_nai,naisyandika_m),(srotravijnana_vip,vipaka_m),(ghranavijnana_nai,naisyandika_m),(ghranavijnana_vip,vipaka_m),(jihvavijnana_nai,naisyandika_m),(jihvavijnana_vip,vipaka_m),(kayavijnana_nai,naisyandika_m),(kayavijnana_vip,vipaka_m),(manovijnana_nai,naisyandika_m),(manovijnana_vip,vipaka_m),(dharma_nai,naisyandika_m),(dharma_vip,vipaka_m)}
GeneratedBy => {(caksur_vip,vipaka_h),(srotra_vip,vipaka_h),(ghrana_vip,vipaka_h),(jihva_vip,vipaka_h),(kaya_vip,vipaka_h),(sabda_nai,sabhaga_h),(sabda_brahma,sabhaga_h),(mano_nai,sabhaga_h),(mano_vip,vipaka_h),(caksurvijnana_nai,sabhaga_h),(caksurvijnana_vip,vipaka_h),(srotravijnana_nai,sabhaga_h),(srotravijnana_vip,vipaka_h),(ghranavijnana_nai,sabhaga_h),(ghranavijnana_vip,vipaka_h),(jihvavijnana_nai,sabhaga_h),(jihvavijnana_vip,vipaka_h),(kayavijnana_nai,sabhaga_h),(kayavijnana_vip,vipaka_h),(manovijnana_nai,sabhaga_h),(manovijnana_vip,vipaka_h),(dharma_nai,sabhaga_h),(dharma_vip,vipaka_h),(dharma_nai,sarvatraga_h)}
FromEffort => {sabda_upa,sabda_nai,sabda_brahma}
KarmaDescended => {sabda_brahma}
Unconditioned => {dharma_asamskrta}
PreventsInjury => {brahmacarya_p}
Increases => {}
Protects => {(upacaya_santana,vipaka_santana)}
VoiceAccount => {parampara_3,parampara_5}
Mediates => {(parampara_3,karma_k,sabda_d),(parampara_5,karma_k,sabda_d)}
MemberCount => {(parampara_3,three_n),(parampara_5,five_n)}
```

**Model checks.** The verse formula holds. The prose closes the modes at
three, ties maturation to the maturation Ground and continuity to the
homogeneous and universal Grounds, gives Sound its upacaya and continuity
instances, excludes maturation from effort, and denies upacaya to the
eight by non-accumulation. The Brahmā-voice instance descends from karma
and is still not maturation-born. The unconditioned instance of the Dharma
Principle has no mode of genesis, which is why the verse is read through
instances. All eight rejected theories are false.

**Bhāṣya determination.** *Vipākahetor jātāḥ*: maturation-born is born
from a maturation Ground. *Īhātaḥ pravṛtteḥ*: Sound is not
maturation-born because it proceeds from effort. *Aupacayikā na santy
apratighānāṃ saṃcayābhāvāt*: no upacaya for the non-resistant, for lack
of accumulation. *Anupaghātamātram*: celibacy is only non-injury.

**Organon interpretation.** The genesis class is fixed by the immediate
Ground, not by remote ancestry. The verse names three modes; 1.38 assigns
the remaining four Principles all three.

The faculty genesis types are:

```text
FiveInternalFacultyPrinciples
    → Vipakaja
    ∧ Aupacayika

Upacaya
    ← Nourishment
    ∨ Conditioning
    ∨ Sleep
    ∨ ConcentrationDifference
```

Preservation and increase are non-equivalent:

```text
PreventsInjury(x)
    ↛ PositivelyIncreases(x)
```

The two faculty continuities cooperate:

```text
VipakaContinuity
    → supplies maturation-born Faculty-capacity

UpacayaContinuity
    → protects and reinforces VipakaContinuity
```

Sound is classified by immediate production:

```text
ProducedThroughPresentEffort(Sound)
    → ¬Vipakaja(Sound)

IndirectlyConditionedByKarma(Sound)
    ↛ DirectlyVipakaja(Sound)
```

The eight non-resistant Principles have causal but non-upacaya genesis:

```text
EightApratighaPrinciples
    → (MayHaveNaisyandikaInstances
        ∨ MayHaveVipakajaInstances)
    ∧ NoAupacayikaInstances
```

The Principle-processor rule is:

```text
GenesisType(x)
    determinedBy ImmediateCausalMode(x)
    not merely RemoteCausalAncestry(x)
```

## 9. Interpretive Note

**Key-term evidence.** Here *hetu* first does work in the chapter. *Vipākaja* is *vipāka-hetu-ja*, and the Bhāṣya keeps the dropped *hetu* by name; *naiḥṣyandika* is generated by *sabhāga-hetu* and *sarvatra-ga-hetu*. The mode of genesis is the Ground. Effort (*īhā*) is not a Ground of this kind but what Sound proceeds from, and it is enough to block maturation; the remote karmic ancestry of the Brahmā voice is not. The Ground in force is the immediate one. 2.49ff will give the six Grounds their protocol.

**Translation note.** The eight non-resistant Principles are the seven Cognition Principles and the Dharma Principle; the Bhāṣya distinguishes their continuity-born and maturation-born instances.

VAK 1.37 adds causal lineage to the Principle. The question is no longer
only what a Principle is capable of doing; it is how that capacity came to
be present and how its continuity is maintained.

The Indriya receives an especially powerful determination:

```text
karma reaching fruition
    → maturation-born Faculty-continuity

nourishment, sleep, conditioning, concentration
    → reinforced Faculty-continuity

Faculty-operation
    → actual apprehensive capacity
```

Thus the Faculty is not reducible to visible configuration, is not an
independent Seer, and is not a merely abstract function. It is an internal
capacity with a causal history and a maintainable continuity. This is part
of the constitution of the Agent, not an incidental biological note.

Sound reveals the difference between remote ancestry and immediate genesis.
A disciplined karmic history may condition the Form-support of a beautiful
voice, yet the actual Sound proceeds through present effort. The Logic must
therefore classify an event by its operative mode of production rather
than assigning the same causal label to everything downstream from karma.

The eight non-resistant Principles make the complementary point. Their
lack of upacaya reinforcement does not imply absence of causal lineage:

```text
not-upacaya-reinforced
    ≠ non-causal
```

Cognition and Dharma flow through homogeneous causal continuities and may
also arise as maturation-results. Inwardness does not exempt a state from
causal genesis.

The Principle of the Agent has consequently acquired a genetic architecture:

```text
Agent capacity
    = inherited causal lineage
    + living reinforcement
    + present operation
```

Later Yoga will work upon this constituted Agent. It will not create its
faculties ex nihilo; it will regulate, reinforce, transform, and eventually
purify modes whose causal structures the Kośa has already made explicit.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_1_37
    a vak:Karika ;
    rdfs:label "VAK 1.37" ;
    vak:hasTopic vak:CausalGenesisOfPrinciples ;
    vak:belongsTo vak:Dhatunirdesa .

vak:FiveInternalFacultyPrinciples
    a vak:PrincipleSet ;
    vak:permitsGenesis vak:Vipakaja,
        vak:Aupacayika .

vak:SoundPrinciple
    vak:notGenesis vak:Vipakaja ;
    vak:immediatelyProducedBy vak:Effort .

vak:EightApratighaPrinciples
    a vak:PrincipleSet ;
    vak:permitsGenesis vak:Naisyandika,
        vak:Vipakaja ;
    vak:notGenesis vak:Aupacayika .

vak:FacultyCapacity
    vak:generatedAs vak:VipakaContinuity ;
    vak:reinforcedBy vak:UpacayaContinuity ;
    vak:actualizedThrough vak:FacultyOperation .

organon:GeneticPrincipleProcessor
    a vak:PrincipleProcessorOperation ;
    organon:requiresParameter vak:ImmediateCausalMode,
        vak:CausalContinuity,
        vak:ReinforcementMode .
```
