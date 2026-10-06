# VAK_1.03

## 1. Sanskrit (Devanāgarī)

> धर्माणां प्रविचयमन्तरेण नास्ति क्लेशानां यत उपशान्तयेऽभ्युपायः ।
>
> क्लेशैश्च भ्रमति भवार्णवेऽत्र लोकस्तद्धेतोरत उदितः किलैष शास्त्रः ॥ १.०३ ॥

## 2. Sanskrit (IAST)

> dharmāṇāṃ pravicayam antareṇa nāsti kleśānāṃ yata upaśāntaye 'bhyupāyaḥ /
>
> kleśaiś ca bhramati bhavārṇave 'tra lokas taddhetor ata uditaḥ kilaiṣa śāstraḥ // 1.03 //

The running Sanskrit witness reads `śāstrā` at the end of this verse.
`Śāstraḥ` above is an editorial conjecture, not a reading established by that
witness. It fits `uditaḥ` and `eṣaḥ` formally, but `śāstra` is ordinarily
neuter; the exact ending remains unsettled. The Devanāgarī line reflects the
same conjecture. The translation conveys the contextual sense without
claiming that the transmitted ending has been resolved.

## 3. Lexical Analysis

```text
nāsti → na asti                         kleśaiś ca → kleśaiḥ ca
bhavārṇave → bhava-arṇave              lokas → lokaḥ
taddhetor → tad-dhetoḥ                 kilaiṣa → kila eṣaḥ
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| dharmāṇām | genitive plural | objects of discrimination |
| pravicayam | accusative singular | governed by `antareṇa` |
| antareṇa | indeclinable postposition | without |
| kleśānām | genitive plural | afflictions to be pacified |
| upaśāntaye | dative singular | purpose: for pacification |
| abhyupāyaḥ | nominative singular | adequate means |
| kleśaiḥ | instrumental plural | cause of wandering |
| bhramati | 3rd singular present | wanders |
| bhavārṇave | locative singular | in the ocean of becoming |
| lokaḥ | nominative singular | subject of `bhramati` |
| tad-dhetoḥ / ataḥ | ablatival expressions | for that reason / therefore |
| uditaḥ | past participle, nominative singular | taught, declared |
| kila | particle | reportedly; according to the received account |
| eṣaḥ śāstraḥ | nominative singular in the conjectural reading | this treatise; transmitted `śāstrā` remains unsettled |

## 4. Grammar

The first half states a necessary condition, not a preference:

```text
dharmapravicaya absent
    → no means for kleśa-pacification
```

The instrumental `kleśaiḥ` gives the causal diagnosis; `tad-dhetoḥ` and `ataḥ` return that diagnosis as the reason for teaching the śāstra. `kila` marks the claim as received report and should not disappear in translation.

The Bhāṣya adds the pedagogical mediation:

```text
Abhidharma instruction → disciple's capacity for pravicaya
→ pacification of kleśa → end of wandering
```

It also attributes to the Vaibhāṣikas—not unqualifiedly to Vasubandhu—the account that the Buddha's dispersed teaching was collected and systematized by Kātyāyanīputra and others.

## 5. Literal Translation

### Close syntactic construe

> Since without discrimination of dharmas there is no means for the pacification of the afflictions, and since through the afflictions the world wanders here in the ocean of becoming, for that reason this treatise is said to have been taught.

### Bhāṣya-informed translation

> Because a disciple cannot discriminate dharmas without Abhidharma instruction, and because such discrimination is indispensable to pacifying the afflictions that cause the world to wander in saṃsāra, this śāstra is said to have been taught.

## 6. Philosophical Translation and Techne Reading

> Abhidharma instruction is necessary because liberation requires a capacity the unaided disciple does not yet possess: exact discrimination of dharmas. That capacity makes the pacification of the afflictions possible and answers their causal power to sustain wandering.

Techne reading:

> The larger Yoga Vidyā is the Science of Principles. Here its *dharmapravicaya* becomes a task for the disciple: to learn to discriminate dharmas so that affliction can be pacified. The śāstra serves that formation through instruction. The text gives the practical necessity of this operation; it does not equate the whole Vidyā with a single analytical act.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Determination |
|---|---|---|
| dharmapravicaya | discrimination of dharmas | indispensable operation of *prajñā*, not the whole Vidyā |
| kleśopaśānti | pacification of affliction | practical end of discrimination |
| abhyupāya | adequate means | here denied apart from pravicaya |
| bhavārṇava | ocean of becoming | glossed as the great ocean of saṃsāra |
| abhidharmopadeśa | Abhidharma instruction | Bhāṣya: pedagogical mediation |
| kila | reportedly | preserves distance from received doctrine |
| prakīrṇa | dispersed | Bhāṣya: mode of Buddha's teaching in the Vaibhāṣika account |

## 8. Logical Determination

```text
kleśa → wandering in becoming
kleśa-pacification requires dharmapravicaya
dharmapravicaya requires instruction for the disciple
therefore: Abhidharma śāstra is taught
```

## 9. Interpretive Note

VAK 1.02 defined the treatise as equipment for attaining stainless *prajñā*.
VAK 1.03 identifies why that equipment is needed: the disciple cannot
discriminate dharmas without instruction, and without that discrimination
there is no means for pacifying the afflictions that sustain wandering.

For our Yoga Vidyā, this is the teachable middle of a larger science.
*Prajñā* names the Vidyā; *dharmapravicaya* is its discriminating operation
as the candidate learns it. *Vijñāna*, where the Kośa names it, carries the
Techne's specific force of discriminative Knowing. VAK 1.03 does not name
*vijñāna*, so this distinction governs our reading without being inserted
into the verse.

The proposed relation to Nirbīja Samādhi belongs to the deeper Yoga Vidyā:
the end of this instruction is not exhausted by a taxonomy of dharmas.
Nor does 1.03 itself state a thesis about Aristotle's undemonstrated
principle of science. That comparison can guide our Techne, but its exact
Aristotelian source and its fit with Nirbīja require a separate study.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
vak:VAK_1_03 a vak:Karika ; vak:hasTopic vak:NecessityOfDharmapravicaya ; vak:belongsTo vak:Dhatunirdesa .
vak:AbhidharmaInstruction vak:enables vak:Dharmapravicaya .
vak:Dharmapravicaya vak:necessaryFor vak:KlesaPacification .
vak:Klesa vak:causes vak:WanderingInBecoming .
```
