# VAK_4.102

## 1. Sanskrit — Devanāgarī

आदावन्तेऽर्बुदात्पूर्वं युगाच्चोपरते मुनौ ।
सीमायां चाप्यबद्धायां चक्रभेदो न जायते ॥ ४.१०२ ॥

## 2. Sanskrit — IAST

**ādāv ante ’rbudāt pūrvaṃ yugāc coparate munau |**  
**sīmāyāṃ cāpy abaddhāyāṃ cakrabhedo na jāyate || 4.102 ||**

## 3. Padaccheda

`ādau | ante | arbudāt | pūrvam | yugāt | ca | uparate | munau | sīmāyām | ca | api | abaddhāyām | cakra-bhedaḥ | na | jāyate`

The exact technical referents of `arbuda` and `yuga` remain for Bhāṣya confirmation.

## 4. Grammar

- **ādau** — at the beginning.
- **ante** — at the end.
- **arbudāt pūrvam** — before the arbuda; technical sense reserved for the Bhāṣya.
- **yugāt** — in relation to or after the pair; exact construction reserved for the Bhāṣya.
- **uparate munau** — when the Sage, the Buddha, has passed away.
- **sīmāyām abaddhāyām** — when the formal monastic boundary has not been established.
- **cakrabhedaḥ na jāyate** — division of the Dharma-wheel does not arise.

## 5. Literal Translation

> Division of the wheel does not arise at the beginning, at the end, before the arbuda, in relation to the pair, when the Sage has passed away, or when a monastic boundary has not been established.

## 6. Philosophical Translation

> Complete rupture of the Dharma-wheel arises only within a mature and formally constituted Buddhist dispensation. It cannot occur at the dispensation’s beginning or end, before the relevant internal corruption has developed, after the Buddha has passed away, or where no formal monastic boundary has been established.

## 7. Technical Vocabulary

- **cakrabheda** — division of the Dharma-wheel; rupture of normative unity.
- **arbuda** — literally a swelling or excrescence; here a technical historical condition pending Bhāṣya confirmation.
- **yuga** — pair; likely an authoritative pair of disciples, pending Bhāṣya clarification.
- **muni** — the Sage, the Buddha.
- **sīmā** — formally delimited monastic territory.
- **abaddha** — not bound, not formally established.

## 8. Doctrinal Determination

Cakrabheda requires a mature, historically actual, and institutionally bounded dispensation. It does not arise:

- at the beginning, before the institution is fully developed;
- at the end, when its operative unity is no longer sufficiently actual;
- after the Buddha has passed away;
- where no formal communal boundary exists.

Formal schism therefore presupposes prior determinate unity.

## 9. Logical Determination

`FormalDivision(x)` requires:

- `PriorUnity(x)`;
- `MatureOrganization(x)`;
- `BoundedDomain(x)`;
- the requisite historical and authoritative conditions.

Without a prior whole, there is only multiplicity, not division of that whole.

## 10. Light Organon Interpretation

The verse places cakrabheda in a determinate middle:

- beginning: unity not yet fully developed;
- middle: unity actual and therefore divisible;
- end: unity no longer sufficiently operative.

Division is thus not externally imposed on an indifferent aggregate. It presupposes a living institutional unity capable of generating organized internal opposition.

## 11. OWL++ Seed

```ttl
vak:VAK_4_102 a vak:Karika ;
    rdfs:label "VAK 4.102" ;
    vak:continues vak:VAK_4_101 ;
    vak:hasTopic vak:CakraDivisionPossibilityConditions .

vak:CakraDivision
    vak:requiresHistoricalPhase vak:MatureDispensation ;
    vak:requiresCondition vak:LivingBuddha ;
    vak:requiresCondition vak:EstablishedMonasticBoundary .

vak:BeginningOfDispensation vak:excludes vak:CakraDivision .
vak:EndOfDispensation vak:excludes vak:CakraDivision .
vak:PostBuddhaPeriod vak:excludes vak:TechnicalCakraDivision .
vak:UnboundedMonasticDomain vak:excludes vak:FormalSanghaDivision .
```

## 12. Commit Note

- exclude cakrabheda at the beginning and end of the dispensation;
- preserve `arbuda` and `yuga` for Bhāṣya confirmation;
- exclude technical cakrabheda after the Buddha’s passing;
- require a formally established monastic boundary;
- define formal division as presupposing mature, bounded institutional unity.
