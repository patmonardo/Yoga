# VAK_6.15 Bhāṣya — Prajñā as Own-Nature; Four Counters to Inversion

## 1. Kārikā Anchor

> prajñā śrutādimayī anye saṃsargālambanāḥ kramaḥ |
> yathotpatti catuṣkaṃ tu viparyāsavipakṣataḥ || 6.15 ||

Literal (from the kārikā study):

> Prajñā, produced through hearing and the succeeding modes, [is the intrinsic
> foundation of mindfulness]; the others are [foundations] by association and by
> object-support. Their sequence is according to arising, but the fourfold
> division is because they oppose the inversions.

Kārikā study: [`VAK_6.15.md`](./VAK_6.15.md). Next: 6.16.

## 2. Continuous Sanskrit Witness

> atha smṛtyupasthānānāṃ kaḥ svabhāvaḥ /
> … svabhāva-saṃsarga-ālambana-smṛtyupasthānam /
> tatra svabhāvasmṛtyupasthānam / prajñā /
> kīdṛśī prajñā / śrutādimayī / śrutamayī cintāmayī bhāvanāmayī ca /
> anye tatsahabhuvo dharmāḥ saṃsargasmṛtyupasthānam /
> tadālambanā ālambanasmṛtyupasthānam /
> kasmāt prajñā smṛtyupasthānam ity uktā / smṛtyudrekatvād iti vaibhāṣikāḥ /
> evaṃ tu yujyate / smṛtir anayopatiṣṭhata iti … yathādṛṣṭasyābhilapanāt /
> kramaḥ / yathotpatti /
> catuṣkaṃ tu viparyāsavipakṣataḥ // 6.15 //
> śuci-sukha-nityātma-viparyāsānāṃ caturṇāṃ pratipakṣeṇa …
> trīṇy asaṃbhinnālambanāni caturtham ubhayathā /

**Witness.** Pradhan 341|16–343|04. Voices: Vasubandhu; Vaibhāṣika on name and
order; sūtra citations (irregular). 6.16 at 343|04–05.

## 3. Continuous Conventional Translation

> What is the own-nature of the establishments of recollection? The name is
> used in several ways: by own-nature, by association, by object-support. By
> own-nature it is Prajñā. What kind? Produced from hearing, from reflection,
> from cultivation. The other dharmas that arise with it are the establishment
> by association. What it takes as support is the establishment by object-support.
>
> Why did the Blessed One call Prajñā an establishment *of recollection*?
> Vaibhāṣikas: because recollection predominates — the work runs on recollection’s
> strength, like a wedge holding split wood. This fits better: recollection is
> established *through* this Prajñā, by articulating what has been seen.
>
> The order is according to arising: the coarser is seen first; or, say the
> Vaibhāṣikas, body underlies sensual desire, feeling is wanted on that account,
> citta is undisciplined, affliction unabandoned. Why four? They counter the four
> inversions — purity, pleasure, permanence, self — neither more nor fewer. The
> first three have unmixed supports. The fourth may take dharmas alone or a mixed
> field of two, three, or all four.

## 4. Movement of the Commentary

```text
svabhāva = Prajñā (śruta / cintā / bhāvanā)
name also = associates + ālambana
Vaibhāṣika wedge vs Vasubandhu: smṛti established by seeing
order ≠ number (arising vs four viparyāsas)
```

## 5. Organon Light (typed)

```ts
type Smrtyupasthana =
  | { tag: "svabhava"; core: Prajna; via: "sruta" | "cinta" | "bhavana" }
  | { tag: "samsarga"; with: Dharma[] }
  | { tag: "alambana"; field: Field };

type Counter = ["kaya","asuci"], ["vedana","duhkha"],
               ["citta","anitya"], ["dharma","anatman"];

// not: Spiritualist XOR Materialist
// the four fields stay together or the practice dies
```

Spiritualist and materialist each want one half of the four and call that
medicine. Apart, only death. Not Vasubandhu’s sentence.

## 6. The Bhāṣya's Decisions for the Kārikā

- three senses of the name;
- `evaṃ tu yujyate` prefers establishment *through* Prajñā;
- four = four inversions; fourth field can mix.

## 7. Review Status

Upgrade against kārikā Literal, first-pass parent, running source 341|16–343|04.
Verse-English copied from [`VAK_6.15.md`](./VAK_6.15.md) §5 Literal. Provisional.
Next: 6.16.
