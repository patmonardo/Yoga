# VAK_6.19 Bhāṣya — Highest Acceptance; Highest Mundane Dharmas

## 1. Kārikā Anchor

> kāmāptaduḥkhaviṣayā tv adhimātrā kṣaṇaṃ ca sā |
> tathāgradharmāḥ sarve tu pañcaskandhā vināptibhiḥ || 6.19 ||

Literal (from the kārikā study):

> But the highest [Acceptance] has suffering belonging to the desire-domain as
> its object, and it [lasts] one moment. The Highest Dharmas are likewise. All,
> however, comprise the five aggregates, without acquisitions.

Kārikā study: [`VAK_6.19.md`](./VAK_6.19.md). Next: 6.20, nirvedhabhāgīya.

## 2. Continuous Sanskrit Witness

> kāmāptaduḥkhaviṣayā tv adhimātrā / kṣāntir iti vartate /
> … kāmāvacaraduḥkhālambanaiva /
> … yāvat kāmāvacaram eva duḥkhaṃ dvābhyāṃ kṣaṇābhyāṃ manasi karoti eṣā … madhyā kṣāntiḥ / yadaikameva kṣaṇaṃ tad adhimātrā /
> kṣaṇaṃ ca sā / kṣaṇikā cāsau na prākarṣikī /
> tathāgradharmāḥ / yathaivādhimātrā kṣāntiḥ /
> te 'pi hi kāmāvacaraduḥkhālambanāḥ kṣaṇikāś ca laukikāś caite 'grāś ca dharmāḥ /
> sarvalaukikaśreṣṭhatvād iti laukikāgradharmāḥ /
> vinā sabhāgahetunā mārgasya tatpuruṣakāreṇākarṣaṇāt /
> ta eta ūṣmagatādayaḥ smṛtyupasthānasvabhāvatvāt prajñātmakā ucyante /
> sarve tu pañcaskandhāḥ / saparivāragrahaṇāt /
> vināptibhiḥ // 6.19 // / prāptayo noṣmagatādibhiḥ saṃgṛhyante /

**Witness.** Pradhan 344|16–345|20. Voice: Vasubandhu. Closing cultivation-matrix
kept in source for later collation. 6.20 at 345|21.

## 3. Continuous Conventional Translation

> “Highest” still means Acceptance. Its support is only desire-domain suffering.
> That restriction shows Heat and the earlier stages may take suffering and the
> rest across three domains, since no such limit was stated for them. When, they
> say, one has dropped the form and formless counters and the several Truths,
> until desire-domain suffering is held for two moments — that is all medium
> Acceptance; when one moment only — highest. Highest Acceptance is momentary,
> not a drawn-out series.
>
> The Highest Dharmas are like that: desire-domain suffering, one moment,
> and mundane. Highest because supreme among mundane dharmas. Without being a
> homogeneous cause of the Path, they draw the Path in by their own efficacy.
>
> Heat and what follows are called Prajñā-natured, because they are establishments
> of recollection by own-nature. All, however, are five aggregates when the
> retinue is counted. Acquisitions are not included: lest an ārya’s possession of
> those acquisitions be taken as present manifestation of Heat and the rest.

The later case-count of present and future establishments and modes is left
for collation. Secure result: last mundane stage has four modes, in likeness
to the Path of Seeing.

## 4. Movement of the Commentary

```text
field contracts → kāma-duḥkha × 1 kṣaṇa
agradharma same object/duration, still laukika, draws Path (not sabhāgahetu)
svabhāva Prajñā / saparivāra five skandhas / minus prāpti
```

## 5. Organon Light (typed)

```ts
type HighestKsanti = { object: "kama_duhkha"; dur: 1; series: false };
type Laukikagradharma = HighestKsanti & { rank: "sarva_laukika_srestha" };
// not Sabhagahetu<Path>
// does Akarshana<Path> via purusakara
type Event = { svabhava: "prajna"; withRetinue: 5; prapti: false };
```

Techne: own-nature ≠ full event. Prajñā does not cancel the five. Prāpti ≠ now-present.

## 6. The Bhāṣya's Decisions for the Kārikā

- `adhimātrā` = kṣānti;
- `agradharmāḥ` = laukikāgradharmāḥ;
- `vināptibhiḥ` = minus prāpti, reason given.

## 7. Review Status

Upgrade against kārikā Literal, first-pass parent, running source 344|16–345|20.
Verse-English from [`VAK_6.19.md`](./VAK_6.19.md) §5 Literal. Matrix provisional.
Next: 6.20.
