# VAK_6.30 Bhāṣya — Prior Grades; Which Fruit Is Approached

## 1. Kārikā Anchor

> yāvat pañcaprakāraghnau dvitīye 'rvāṅ navakṣayāt |
> kāmād viraktāv ūrdhvaṃ vā tṛtīyapratipannakau || 6.30 ||

Literal (from the kārikā study):

> The two who have destroyed as many as five grades [remain candidates for the
> first fruit]; short of destruction of the ninth, [they proceed] toward the
> second. When detached from the desire-domain, or [when detachment extends]
> higher, the two are proceeding toward the third [fruit].

Kārikā study: [`VAK_6.30.md`](./VAK_6.30.md). Next: 6.31, sixteenth moment.

## 2. Continuous Sanskrit Witness

> yāvat pañcaprakāraghnau / yadi pūrvaṃ laukikena mārgeṇa … yāvat pañca prakārāḥ prahīṇāḥ … prathamaphalapratipannakāv ucyete /
> dvitīye 'rvāṅ navakṣayāt / … ṣaṭ saptāṣṭau vā … dvitīyaphalapratipannakāv ucyete / sakṛdāgāmiphalam /
> kāmād viraktau ūrdhvaṃ vā tṛtīyapratipannakau / … kāmadhātor vītarāgau … yāvad ākiñcanyāyatanāt … anāgāmiphalam /

**Witness.** Pradhan 353|23–354|08. Voice: Vasubandhu. 6.31 at 354|09.

## 3. Continuous Conventional Translation

> If previously, by a mundane path, as many as five grades of desire-domain
> cultivation-abandonable [defilements] have been abandoned, they are still called
> persons proceeding toward the first fruit.
>
> Toward the second, short of destruction of the nine: if six, seven, or eight
> grades were previously abandoned, they proceed toward the second fruit. The
> second is once-return.
>
> Detached from desire-domain, or higher: if the ninth grade too is gone, they are
> free of attachment to the desire-domain — or if prior detachment runs higher, as
> far as the Essence of Nothingness — they proceed toward the third fruit. The third
> is non-return.

## 4. Movement of the Commentary

```text
0–5 prior grades → stream-entry
6–8 → once-return
9, or higher vairāgya → non-return
Seeing sequence unchanged; input-state maps the fruit
```

## 5. Organon Light (typed)

```ts
type Prior = 0|1|2|3|4|5|6|7|8|9;
type Fruit = Prior extends 0..5 ? "srotaapatti" : Prior extends 6..8 ? "sakrdagami" : "anagami";
```

## 6. The Bhāṣya's Decisions for the Kārikā

- “up to five” stays first fruit;
- arvāk navakṣayāt = 6–8;
- fourth fruit not yet.

## 7. Review Status

Upgrade against kārikā Literal, first-pass parent, running source 353|23–354|08.
Verse-English from [`VAK_6.30.md`](./VAK_6.30.md) §5 Literal. Dense taxonomy, not the 6.34 talk.
Next: 6.31.
