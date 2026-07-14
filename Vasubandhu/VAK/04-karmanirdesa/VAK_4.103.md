# VAK_4.103

## 1. Sanskrit — Devanāgarī

उपकारिगुणक्षेत्रनिराकृतिविपादनात् ।
व्यञ्जनान्तरितोऽपि स्यान्माता यच्छोणितोद्भवः ॥ ४.१०३ ॥

## 2. Sanskrit — IAST

**upakāriguṇakṣetranirākṛtivipādanāt |**  
**vyañjanāntarito ’pi syāt mātā yacchoṇitodbhavaḥ || 4.103 ||**

## 3. Padaccheda

`upakāri-guṇa-kṣetra-nirākṛti-vipādanāt | vyañjana-antaritaḥ | api | syāt | mātā | yat-śoṇita-udbhavaḥ`

## 4. Grammar

- **upakāri** — benefactor, one who has rendered benefit.
- **guṇakṣetra** — field of qualities or spiritual excellence.
- **nirākṛti** — repudiation, rejection, nullification.
- **vipādana** — destruction or killing.
- **vyañjana** — sexual characteristic.
- **antaritaḥ** — altered or changed.
- **mātā** — mother.
- **yat-śoṇita-udbhavaḥ** — the one from whose maternal generative substance the person arose.

The exact internal coordination of the first compound remains for Bhāṣya confirmation.

## 5. Literal Translation

> Because of the repudiation and destruction of a benefactor or a field of qualities, the act has immediate consequence. Even if the sexual characteristic has changed, the mother is the one from whose blood one arose.

## 6. Philosophical Translation

> The five immediate-consequence karmas are grave because their objects are exceptional relational fields: parents are supreme benefactors, while an arhat, a Buddha, and the Saṃgha are fields of extraordinary spiritual qualities. The parental relation remains determined by causal origination even after a change of sexual characteristic.

## 7. Technical Vocabulary

- **upakārin** — benefactor.
- **guṇakṣetra** — field of spiritual qualities.
- **nirākṛti** — normative repudiation.
- **vipādana** — bodily destruction or killing.
- **vyañjanāntara** — change of sexual characteristic.
- **śoṇita** — maternal reproductive contribution in ancient embryological terminology.

## 8. Doctrinal Determination

The five ānantarya acts arise from two exceptional field-types:

- benefactor-fields: mother and father;
- quality-fields: arhat, Buddha, and Saṃgha.

Karmic gravity therefore depends on the agent’s prior relation to the object and on the qualities embodied by that object. Motherhood is fixed by the causal history of origination rather than by present bodily designation.

## 9. Logical Determination

The karmic magnitude of an act depends on:

- intention;
- mode of action;
- relation to the object;
- benefit conferred by the object;
- qualities possessed by the object.

The karmic field is therefore the individual as relationally and historically determined, not merely the present physical individual.

## 10. Light Organon Interpretation

Karma tracks constitutive history. A present change of bodily characteristic does not erase the generative relation through which the field was constituted. Current attributes do not exhaust causal identity.

## 11. OWL++ Seed

```ttl
vak:VAK_4_103 a vak:Karika ;
    rdfs:label "VAK 4.103" ;
    vak:continues vak:VAK_4_102 ;
    vak:hasTopic vak:ExceptionalKarmicField,
                 vak:MaternalRelation .

vak:BenefactorField rdfs:subClassOf vak:ExceptionalKarmicField .
vak:QualityField rdfs:subClassOf vak:ExceptionalKarmicField .

vak:Mother, vak:Father
    rdfs:subClassOf vak:BenefactorField .

vak:Arhat, vak:Buddha, vak:Sangha
    rdfs:subClassOf vak:QualityField .

vak:MaternalRelation
    vak:groundedIn vak:MaternalOrigination ;
    vak:persistsDespite vak:SexCharacteristicChange .
```

## 12. Commit Note

- distinguish benefactor-fields from fields of spiritual qualities;
- ground parental ānantarya in extraordinary prior benefit;
- ground the remaining acts in exceptional quality-fields;
- distinguish physical destruction from normative repudiation;
- define motherhood through maternal origination;
- preserve the parental relation despite later bodily change;
- model karmic identity as relationally and historically determined.
