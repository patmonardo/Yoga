# VAK_4.100

## 1. Sanskrit — Devanāgarī

भिक्षुर्दृक्चरितो वृत्ती भिनत्त्यन्यत्र बालिशान् ।
शास्तृमार्गान्तरक्षान्तौ भिन्नो न विवसत्यसौ ॥ ४.१०० ॥

## 2. Sanskrit — IAST

**bhikṣur dṛkcarito vṛttī bhinatty anyatra bāliśān |**  
**śāstṛmārgāntarakṣāntau bhinno na vivasaty asau || 4.100 ||**

## 3. Padaccheda

`bhikṣuḥ | dṛk-caritaḥ | vṛttī | bhinatti | anyatra | bāliśān | śāstṛ-mārga-antara-kṣāntau | bhinnaḥ | na | vivasati | asau`

## 4. Grammar

- **bhikṣuḥ** — a monk.
- **dṛk-caritaḥ** — governed by a view; one whose conduct proceeds from a view.
- **bhinatti** — divides.
- **bāliśān** — childish, foolish, spiritually immature persons.
- **śāstṛ-mārga-antara-kṣāntau** — upon assent to another teacher and another path.
- **bhinnaḥ** — divided.
- **na vivasati** — does not remain indefinitely; literally, does not remain overnight.

The exact force of `vṛttī` and `anyatra` remains for the Bhāṣya pass.

## 5. Literal Translation

> A monk, one whose conduct is governed by a view, divides the foolish; not otherwise. The division occurs upon their acceptance of another teacher and another path, and that divided state does not remain overnight.

## 6. Philosophical Translation

> A formal division of the Saṃgha is produced by a monk whose activity is governed by a doctrinal view and takes hold among spiritually immature members. The community becomes divided when they assent to a teacher and path opposed to the authentic teacher and path; such division is temporally bounded.

## 7. Technical Vocabulary

- **bhikṣu** — monk; an internal member of the Saṃgha.
- **dṛkcarita** — governed by a view.
- **bāliśa** — spiritually immature, lacking stable discrimination.
- **śāstṛ** — teacher; here, the Buddha as normative source.
- **mārgāntara** — another or alternative path.
- **kṣānti** — acceptance or assent.
- **na vivasati** — does not persist indefinitely.

## 8. Doctrinal Determination

Complete Saṃgha-division requires:

- an internal agent: the divider is a monk;
- doctrinal motivation: conduct governed by an afflicted view;
- susceptible recipients: spiritually immature persons;
- communal assent to another teacher and another path.

False speech alone is not yet full division. The divisive teaching must be accepted and become a competing normative center.

## 9. Logical Determination

The complete mediation is:

`mṛṣāvāda → kṣānti → asāmagrī`

- false speech is the causal act;
- assent is the mediation;
- collective non-concord is the result.

Thus utterance plus recognition produces institutional transformation.

## 10. Light Organon Interpretation

Saṃgha-unity is unity of normative recognition. Saṃgha-division is division of normative recognition around another teacher and another path.

The false teaching becomes institutionally effective only because members accept it. Speech becomes socially actual through recognition.

## 11. OWL++ Seed

```ttl
vak:VAK_4_100 a vak:Karika ;
    rdfs:label "VAK 4.100" ;
    vak:continues vak:VAK_4_99 ;
    vak:hasTopic vak:SanghaDivisionConditions .

vak:SanghaDivider
    rdfs:subClassOf vak:Bhiksu ;
    vak:isGovernedBy some vak:AfflictedView .

vak:FormalSanghaDivision
    vak:requiresMediation vak:DoctrinalAssent ;
    vak:hasAcceptedContent vak:AlternativeTeacher,
                           vak:AlternativePath .
```

## 12. Commit Note

- identify the formal divider as a monk internal to the Saṃgha;
- interpret dṛkcarita as conduct governed by an afflicted view;
- identify spiritually immature persons as susceptible recipients;
- define division through assent to another teacher and another path;
- distinguish utterance from successful institutional transformation;
- model kṣānti as the mediation between false speech and collective non-concord;
- retain the temporally bounded character of the divided state for Bhāṣya confirmation.
