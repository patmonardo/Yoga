# VAK_6.14 Bhāṣya — Accomplished Śamatha; Two-Lakṣaṇa Examination

## 1. Kārikā Anchor

> niṣpanna-śamathaḥ kuryāt smṛtyupasthāna-bhāvanām |
> kāya-vic-citta-dharmāṇāṃ dvi-lakṣaṇa-parīkṣaṇāt || 6.14 ||

Literal (from the kārikā study):

> One whose śamatha has been accomplished should cultivate the establishments
> of recollection through examination of body, feeling, citta, and dharmas
> according to two determinations.

Kārikā study: [`VAK_6.14.md`](./VAK_6.14.md). Next: 6.15, svabhāva of the four.

## 2. Continuous Sanskrit Witness

> ukte dve avatāramukhe / tābhyāṃ tu samādhilabdhā /
> niṣpannaśamathaḥ kuryāt smṛtyupasthānabhāvanām /
> vipaśyanāyāḥ saṃpādanārtham / kathaṃ ca punaḥ kuryāt /
> kāyaviccittadharmāṇāṃ dvilakṣaṇaparīkṣaṇāt // 6.14 //
> kāyaṃ svasāmānyalakṣaṇābhyāṃ parīkṣate / vedanāṃ cittaṃ dharmāś ca /
> svabhāva evaiṣāṃ svalakṣaṇam /
> sāmānyalakṣaṇaṃ tu anityatā saṃskṛtānāṃ duḥkhatā sāsravāṇāṃ śūnyatā 'nātmatā sarvadharmāṇām /
> kāyasya punaḥ kaḥ svabhāvaḥ / bhūtabhautikatvam /
> dharmās tribhyo 'nye /
> sāmāhitasya kila kāyaṃ paramāṇuśaḥ kṣaṇikataś ca paśyataḥ kāyasmṛtyupasthānaṃ niṣpannaṃ bhavati /

**Witness.** Pradhan 341|07–341|15. Voice: Vasubandhu; `kila` on atom/moment body.
6.15 begins 341|16.

## 3. Continuous Conventional Translation

> The two entrance-gates have been stated. Having gained samādhi through them,
> one whose śamatha is accomplished should cultivate the establishments of
> recollection, for bringing vipaśyanā to completion. How? Through examination
> of body, feeling, citta, and dharmas according to two determinations.
>
> One examines the body by its own-mark and its common-mark; so also feeling,
> citta, and dharmas. Their own-nature is their own-mark. The common-mark:
> impermanence of the conditioned; suffering of the contaminated; emptiness and
> not-self of all dharmas. What is the body’s own-nature? Being great-elements
> and derived form. “Dharmas” here are those other than the first three. For one
> concentrated who sees the body atom by atom and moment by moment, they say,
> the body-establishment is complete.

## 4. Movement of the Commentary

```text
two avatāramukhas closed → samādhi → niṣpanna-śamatha
kuryāt smṛtyupasthāna → vipaśyanā-saṃpādana
sva + sāmānya, scopes not one slogans-bucket
```

## 5. Śamatha Done ≠ Vipaśyanā Done

The optative is work still owed. Universal marks keep their ranges: conditioned
/ contaminated / all. Citta is a field examined, not an untyped spectator.

## 6. Organon Light (typed)

```ts
type Field = "kaya" | "vedana" | "citta" | "dharmaMinusThree";

type Sva = { kaya: "bhuta_bhautika" }; // others deferred to 6.15

type Samanya =
  | { on: "samskrta"; mark: "anitya" }
  | { on: "sasrava"; mark: "duhkha" }
  | { on: "sarva_dharma"; mark: "sunya" | "anatman" };

// not: Mastery<Shamatha> extends Complete<Vipasyana>
```

## 7. The Bhāṣya's Decisions for the Kārikā

- `vit` = vedanā;
- two lakṣaṇas named sva / sāmānya with three scopes;
- dharma-field = remainder of the first three.

## 8. Review Status

Upgrade against kārikā Literal, first-pass parent, running source 341|07–15.
Verse-English copied from [`VAK_6.14.md`](./VAK_6.14.md) §5 Literal. Provisional.
Next: 6.15.
