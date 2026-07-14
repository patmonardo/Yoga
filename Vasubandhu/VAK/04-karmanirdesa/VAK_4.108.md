# VAK_4.108

## 1. Sanskrit — Devanāgarī

बोधिसत्त्वः कुतो यावत् यतो लक्षणकर्मकृत् ।
सुगतिः कुलजोऽव्यक्षः पुमान् जातिस्मरोऽनिवृत् ॥ ४.१०८ ॥

## 2. Sanskrit — IAST

**bodhisattvaḥ kuto yāvat yato lakṣaṇakarmakṛt |**  
**sugatiḥ kulajo ’vyakṣaḥ pumān jātismaro ’nivṛt || 4.108 ||**

## 3. Padaccheda

`bodhisattvaḥ | kutaḥ | yāvat | yataḥ | lakṣaṇa-karma-kṛt | su-gatiḥ | kula-jaḥ | a-vyakṣaḥ | pumān | jāti-smaraḥ | a-nivṛt`

## 4. Literal Translation

> From what point onward is he a Bodhisattva? From the time when he performs the karma producing the marks. He is in a good destiny, born into a good family, without defective faculties, male, remembering previous births, and not turning back.

## 5. Philosophical Translation

> In the strict Kośa sense, the title “Bodhisattva” applies from the point at which the aspirant begins performing the determinate karma that will produce the bodily marks of a Buddha. From then onward his career possesses a stable causal form: favorable destinies and families, unimpaired capacities, memory of former births, and non-retrogression.

## 6. Technical Vocabulary

- **lakṣaṇa-karma** — activity producing the marks of a Great Person.
- **sugati** — favorable destiny.
- **kulaja** — born into a favorable family.
- **avyakṣa** — probably unimpaired in faculties; preserve for Bhāṣya confirmation.
- **jātismara** — remembering former births.
- **anivṛt** — not turning back; non-retrogressing.

## 7. Doctrinal Determination

The strict Bodhisattva stage is defined not by aspiration alone but by a determinate karmic trajectory. Mark-producing karma organizes the future Buddha-form and constrains subsequent rebirths, capacities, memory, and direction.

The verse groups the Bodhisattva’s determinations as:

- causal: mark-producing karma;
- environmental: good destiny and family;
- embodied: unimpaired capacities and the tradition’s determinate bodily qualification;
- diachronic: memory of births and non-retrogression.

## 8. Logical Determination

`PerformsMarkProducingKarma(agent)` implies `BodhisattvaInStrictSense(agent)` and establishes a corridor of becoming in which certain regressive possibilities are excluded.

Karma here is not merely an isolated cause of an isolated result. It is a modal organizer of a whole developmental sequence.

## 9. Light Organon Interpretation

The Bodhisattva is neither an inert substance passing through lives nor a disconnected series of momentary states. He is a self-maintaining karmic trajectory: recurring orientation, recurring capacity, remembered history, and irreversible direction.

The Buddha marks are form as accumulated activity made manifest. Karma is the ground of the future Buddha-body.

## 10. OWL++ Seed

```ttl
vak:VAK_4_108 a vak:Karika ;
    rdfs:label "VAK 4.108" ;
    vak:continues vak:VAK_4_107 ;
    vak:hasTopic vak:TechnicalBodhisattva,
                 vak:MarkProducingKarma .

vak:TechnicalBodhisattva
    vak:beginsWith vak:MarkProducingKarma ;
    vak:hasDestinyConstraint vak:GoodDestiny ;
    vak:hasBirthCondition vak:FavorableFamily ;
    vak:hasCapacityCondition vak:UnimpairedFaculties ;
    vak:hasContinuityProperty vak:BirthMemory ;
    vak:hasDirectionProperty vak:NonRetrogression .

vak:MarkProducingKarma
    vak:produces vak:BuddhaMarks ;
    vak:organizes vak:BodhisattvaTrajectory .
```

## 11. Commit Note

- define the technical Bodhisattva stage through mark-producing karma;
- identify recurrent environmental, embodied, and diachronic conditions;
- preserve `avyakṣa` for Bhāṣya confirmation;
- define birth-memory as conscious karmic continuity;
- define non-retrogression as irreversible karmic becoming;
- connect karma directly to production of Buddha-form.
