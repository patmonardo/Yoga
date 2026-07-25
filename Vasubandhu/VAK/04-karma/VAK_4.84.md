# VAK_4.84

## 1. Sanskrit — Devanāgarī

आरूप्यासंज्ञिसत्त्वेषु लाभतः सप्त शेषिते ।  
संमुखीभावतश्चापि हित्वा सनरकान् कुरून् ॥ ४.८४ ॥

Local source:

```text
ārūpyāsaṃjñisattveṣu lābhataḥ sapta śeṣite /
saṃmukhībhāvataścāpi hitvā sanarakān kurūn // VAkK_4.84 //
```

## 2. Sanskrit — IAST

**ārūpyāsaṃjñi-sattveṣu lābhataḥ sapta śeṣite |**  
**saṃmukhībhāvataś cāpi hitvā sa-narakān kurūn || 4.84 ||**

The verse completes the distribution of the seven wholesome bodily and verbal karmic courses.

## 3. Padaccheda

```text
ārūpya
asaṃjñi-sattveṣu
lābhataḥ
sapta
śeṣite
saṃmukhībhāvataḥ
ca
api
hitvā
sa-narakān
kurūn
```

Expanded sense:

```text
ārūpye asaṃjñi-sattveṣu ca
śeṣāḥ sapta lābhataḥ

śeṣiteṣu saṃmukhībhāvataś ca api
hitvā narakān kurūn ca
```

> In the formless domain and among non-percipient beings, the remaining seven exist through acquisition. In the remaining cases they also occur through present manifestation, except among hell beings and the Kurus.

## 4. Grammar

- **ārūpya**: the formless domain; fuller expression `ārūpya-dhātu`, with `dhātu` translated as domain.
- **asaṃjñi-sattveṣu**: locative plural, “among non-percipient beings.”
- **lābhataḥ**: ablative used adverbially, “through acquisition,” hence by way of endowment.
- **sapta**: the seven wholesome bodily and verbal karmic courses.
- **śeṣite**: transmitted compact form, provisionally understood as “in the remaining cases.”
- **saṃmukhībhāvataḥ**: “through present manifestation,” event-level actuality.
- **hitvā**: absolutive, “having excluded,” “excepting.”
- **sa-narakān kurūn**: “hell beings together with the Kurus,” functioning as the exceptions.

## 5. Literal Translation

> In the formless domain and among non-percipient beings, the remaining seven exist through acquisition. In the remaining cases they also occur through present manifestation, excluding hell beings and the Kurus.

## 6. Philosophical Translation

> The seven wholesome bodily and verbal courses may belong to a continuum even where the bodily or verbal conditions necessary for their actual expression are absent. In the formless domain and among non-percipient beings, they persist as acquired restraints but cannot become presently enacted. In the remaining suitable domains, acquisition can pass into manifestation, except where the existential structure of hell or Uttarakuru excludes such active restraint.

The central distinction is:

```text
endowment
    a determination belongs to the continuum

manifestation
    that determination is active in a present event
```

Thus absence of expression is not absence of dharma.

## 7. Technical Vocabulary

### The remaining seven

The three wholesome mental courses were supplied in VAK_4.83. The remaining seven are the wholesome counterparts of the three bodily and four verbal unwholesome courses:

```text
refraining from taking life
refraining from taking what is not given
refraining from sexual misconduct
refraining from false speech
refraining from divisive speech
refraining from harsh speech
refraining from disconnected speech
```

### virati

Though not explicit in the kārikā, the seven are forms of restraint or abstention:

```text
virati
    cessation
    restraint
    abstention
```

### lābha

```text
lābha
    acquisition
    attainment
    continuum-level endowment
```

### saṃmukhībhāva

```text
saṃmukhībhāva
    present actualization
    event-level manifestation
```

### ārūpya

The formless domain lacks the material basis required for bodily and verbal manifestation, though previously acquired restraint can remain an endowment.

### asaṃjñi-sattva

A non-percipient being lacks the presently active ideational process required for intentional exercise of restraint, while prior acquisition may persist.

## 8. Doctrinal Determination

VAK_4.83 supplied three wholesome mental courses; VAK_4.84 supplies the remaining seven bodily and verbal restraints:

```text
3 mental
+
7 bodily and verbal
=
10 wholesome karmic courses
```

In formless existence and among non-percipient beings, the seven occur by acquisition only. The continuum possesses the restraint, but it is not presently exercised through bodily or verbal activity.

In suitable remaining domains, the seven may occur through both acquisition and present manifestation.

Hell beings and Uttarakuru inhabitants are excluded from present manifestation, but the grounds differ. Hell lacks the operative conditions for active wholesome restraint; Uttarakuru may lack the occasions requiring formal restraint. The same extension can therefore arise from different grounds.

## 9. Logical Determination

Let:

```text
C = causal continuum
R = wholesome bodily or verbal restraint
D = existential domain
```

Distinguish:

```text
AcquiredBy(C, R)
EndowedWith(C, R)
ManifestableIn(R, D)
PresentlyManifest(C, R, t)
```

Formless domain:

```text
ExistsIn(C, FormlessDomain)
and WholesomeBodilyVerbalRestraint(R)
    →
MayBeEndowedWith(C, R)
and not ManifestableIn(R, FormlessDomain)
```

Non-percipient beings:

```text
NonPercipient(C)
and WholesomeBodilyVerbalRestraint(R)
    →
MayBeEndowedWith(C, R)
and not PresentlyManifest(C, R)
```

Critical constraints:

```text
PossessesRestraint(C, R)
    does not imply
CurrentlyExercisesRestraint(C, R)
```

```text
DoesNotPerformUnwholesomeAct(C, t)
    does not imply
PresentlyManifestsWholesomeRestraint(C, t)
```

Mere absence can arise from lack of opportunity, bodily support, verbal support, ideational support, or environmental possibility.

## 10. Light Organon Interpretation

At the Kernel level, the verse requires at least four states:

```text
undefined
available
acquired
manifest
```

A suitable representation is:

```text
RestraintStatus {
    restraintType
    acquired
    endowed
    manifestableInDomain
    currentlyManifest
    blockingConditions[]
}
```

The Kernel must preserve the grounds of non-manifestation. `NoObservedViolation` may mean active restraint, no opportunity, no capability, no object-support, domain prohibition, or a non-percipient state.

A dharma therefore specifies whether a determination exists as a type, belongs to a continuum, is supported by a domain, can become manifest, and persists despite non-manifestation.

## 11. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix logic: <http://127.0.0.1:3000/logic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_4_84
    a vak:Karika ;
    rdfs:label "VAkK 4.84" ;
    vak:continues vak:VAK_4_83 ;
    vak:hasTopic
        vak:SevenWholesomeBodilyVerbalCourses,
        vak:AcquiredEndowment,
        vak:PresentManifestation .

vak:SevenWholesomeBodilyVerbalCourses
    rdfs:subClassOf vak:WholesomeKarmicCourse ;
    vak:hasCardinality 7 .

vak:FormlessDomain
    vak:supportsEndowmentOf vak:SevenWholesomeBodilyVerbalCourses ;
    vak:doesNotSupportManifestationOf vak:SevenWholesomeBodilyVerbalCourses .

vak:NonPercipientBeing
    vak:mayBeEndowedWith vak:SevenWholesomeBodilyVerbalCourses ;
    vak:doesNotPresentlyManifest vak:SevenWholesomeBodilyVerbalCourses .

vak:SuitableRemainingDomain
    vak:supportsEndowmentOf vak:SevenWholesomeBodilyVerbalCourses ;
    vak:supportsManifestationOf vak:SevenWholesomeBodilyVerbalCourses .

vak:HellDomain
    vak:doesNotSupportPresentManifestationOf vak:SevenWholesomeBodilyVerbalCourses .

vak:UttarakuruDomain
    vak:doesNotSupportPresentManifestationOf vak:SevenWholesomeBodilyVerbalCourses .
```

## 12. Commit Note

```text
VAK_4.84 — Distribute the seven wholesome bodily and verbal courses

- identify the remaining seven as wholesome bodily and verbal restraints
- specify acquisition without manifestation in the formless domain
- specify acquisition without manifestation among non-percipient beings
- allow present manifestation in the remaining suitable modes
- exclude hell beings and Uttarakuru inhabitants from present manifestation
- distinguish possession of restraint from active exercise of restraint
- distinguish positive restraint from mere absence of unwholesome action
- preserve domain-specific grounds of non-manifestation at the Kernel level
```

### First-pass determination

```text
formless domain:
    seven wholesome bodily/verbal courses
        by acquisition only

non-percipient beings:
    seven wholesome bodily/verbal courses
        by acquisition only

remaining suitable domains:
    also by present manifestation

exceptions:
    hell beings
    Uttarakuru inhabitants
```

The central Kernel result is:

```text
a dharma may belong fully
to a causal continuum

while the present domain
withholds the conditions
of its manifestation
```