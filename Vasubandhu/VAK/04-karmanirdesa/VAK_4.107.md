# VAK_4.107

## 1. Sanskrit — Devanāgarī

आनन्तर्यसभागानि पञ्चमं स्तूपभेदनम् ।
क्षान्त्यनागामितार्हत्त्वप्राप्तौ कर्मातिविघ्नकृत् ॥ ४.१०७ ॥

## 2. Sanskrit — IAST

**ānantaryasabhāgāni pañcamaṃ stūpabhedanam |**  
**kṣāntyanāgāmitārhattvaprāptau karmātivighnakṛt || 4.107 ||**

## 3. Padaccheda

`ānantarya-sabhāgāni | pañcamam | stūpa-bhedanam | kṣānti-anāgāmitā-arhattva-prāptau | karma | ati-vighna-kṛt`

## 4. Literal Translation

> These are analogous to the immediate-consequence acts; destruction of a stūpa is the fifth. Karma produces an extreme obstruction to the attainment of acceptance, non-returnership, and arhatship.

## 5. Philosophical Translation

> The four acts previously enumerated, together with destruction of a stūpa, reproduce the structure of the five immediate-consequence karmas without technically belonging to that class. Such grave karma strongly obstructs the transformations through which acceptance, non-returnership, and arhatship become actual.

## 6. Technical Vocabulary

- **ānantarya-sabhāga** — structurally analogous to immediate-consequence karma, without strict technical identity.
- **stūpabhedana** — destruction of a stūpa, an attack upon the represented Buddha-field.
- **kṣānti** — technical acceptance or receptive insight.
- **anāgāmitā** — non-returnership.
- **arhattva** — arhatship.
- **ati-vighna-kṛt** — producing an extreme obstacle.

## 7. Doctrinal Determination

The five analogues are:

1. violation of an arhat mother;
2. killing a bodhisattva established in certainty;
3. killing a śaikṣa;
4. depriving the Saṃgha of support;
5. destroying a stūpa.

They attack fields embodying supreme benefit, liberation, assured Buddhahood, the developing Path, communal Dharma, or represented Buddha-presence.

## 8. Logical Determination

Grave karma does not merely attach a later penalty. It changes the transition conditions of the continuum:

`GraveKarma(agent) → TransitionBlocked(agent, target attainment)`

The relevant blocked transitions include acceptance, non-returnership, and arhatship.

## 9. Light Organon Interpretation

Karma functions as a constraint upon becoming: it governs what can become, what must become, and what cannot yet become. The verse therefore presents karma as the ground ordering admissible spiritual transitions.

## 10. OWL++ Seed

```ttl
vak:VAK_4_107 a vak:Karika ;
    rdfs:label "VAK 4.107" ;
    vak:continues vak:VAK_4_106 ;
    vak:hasTopic vak:AnantaryaAnalogues,
                 vak:KarmicPathObstruction .

vak:DestroyingStupa
    rdfs:subClassOf vak:AnantaryaAnalogue ;
    vak:hasField vak:RepresentedBuddhaField .

vak:AnantaryaAnalogue
    vak:mayObstruct vak:KsantiAttainment,
                    vak:NonReturnership,
                    vak:Arhatship .

vak:KarmicPathObstruction
    rdfs:subClassOf vak:TransitionConstraint .
```

## 11. Commit Note

- classify the preceding acts as ānantarya-sabhāga;
- identify destruction of a stūpa as the fifth analogue;
- model the stūpa as a represented Buddha-field;
- identify grave karma as an extreme obstruction to kṣānti, non-returnership, and arhatship;
- interpret karma as a constraint upon admissible spiritual transitions.
