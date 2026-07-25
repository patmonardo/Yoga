# VAK 6.22

## Sanskrit

### Devanāgarī

आद्ये द्वे परिहाण्या च मौलेस्तत्रैव सत्यदृक् ।
अपूर्वाप्तिर्विहीनेषु हानी द्वे असमन्वितिः ॥ ६.२२ ॥

### IAST

**ādye dve parihāṇyā ca maules tatraiva satyadṛk |**
**apūrvāptir vihīneṣu hānī dve asamanvitiḥ || 6.22 ||**

## Padaccheda

ādye | dve | parihāṇyā | ca | mauleḥ | tatra eva | satya-dṛk | apūrva-āptiḥ | vihīneṣu | hānī | dve | asamanvitiḥ

## Grammar

- **ādye dve** — nominative or accusative dual neuter: “the first two,” namely Heat and the Summits.
- **parihāṇyā** — instrumental singular feminine of *parihāṇi*: “through decline,” “through regression.”
- **ca** — “also,” adding regression to the modes of loss discussed in VAK 6.21.
- **mauleḥ** — genitive singular of *maula*, “principal” or “fundamental”; here referring to the principal dhyānas.
- **tatra eva** — “there itself,” interpreted by the Bhāṣya as within that very birth.
- **satya-dṛk** — nominative singular: “one who sees the Truths.”
- **apūrva-āptiḥ** — nominative singular feminine: “acquisition of what is new.”
- **vihīneṣu** — locative plural past passive participle from *vi-√hā*: “when they have been lost.”
- **hānī dve** — nominative dual feminine: “the two losses.”
- **asamanvitiḥ** — nominative singular feminine: “non-possession,” “non-endowment,” corresponding to *asamanvāgama* in the Bhāṣya.

## Literal Translation

The first two may also be lost through regression. One whose preparations belong to a principal dhyāna sees the Truths in that very birth. When lost preparations are acquired again, the acquisition is new. The two forms of loss are non-possession.

## Philosophical Translation

Heat and the Summits, unlike the two higher preparations, remain vulnerable to regression. But one who produces the preparations upon a principal dhyāna necessarily sees the Truths within that same life. If preparations that have been lost are later obtained again, numerically new preparations are acquired rather than the former ones returning. Both abandonment and regression consist in no longer being endowed with the relevant dharmas.

## The First Two May Regress

The “first two” are Heat and the Summits. An ordinary person may lose these not only through death but also through **parihāṇi**, regression or decline. Acceptance and the Highest Mundane Dharmas are not subject to this regression.

Thus the four stages divide into two groups:

- Heat and Summits: still subject to regression.
- Acceptance and Highest Mundane Dharmas: not subject to regression.

## Preparations Grounded in a Principal Dhyāna

The statement **maules tatraiva satyadṛk** means that one who produces the preparations belonging to a principal dhyāna sees the Truths in that very birth.

Here **maula** distinguishes the four principal dhyānas from the preliminary concentration and the intermediate concentration.

## Reacquisition Is New Acquisition

When lost preparations are later obtained again, the former dharmas do not return. New preparations arise.

This preserves the distinction between continuity of the path-series and numerical identity of its dharmas.

## The Two Forms of Loss

The two forms are:

- **vihāni** — relinquishment or complete loss.
- **parihāṇi** — regression or decline.

Both have the nature of **asamanvāgama**, no longer possessing or being endowed with the relevant dharmas.

The result is the same—non-possession—but the mode and causal structure differ.

## Doctrinal Determination

VAK 6.22 distinguishes:

- which stages may regress: Heat and Summits;
- which stages do not regress: Acceptance and Highest Mundane Dharmas;
- what follows from principal-dhyāna support: Truth-seeing in the same birth;
- what is acquired after loss: numerically new preparations;
- the common nature of both losses: non-possession.

## Logical Determination

```text
Heat {
    mayBeLostThrough: Regression
}

Summits {
    mayBeLostThrough: Regression
}

Acceptance {
    notLostThrough: Regression
}

HighestMundaneDharmas {
    notLostThrough: Regression
}

PrincipalDhyanaPreparation {
    ensures: TruthSeeingInSameLife
}

ReacquisitionAfterLoss {
    acquires: NewPreparation
}

Relinquishment {
    generalNature: NonPossession
}

Regression {
    generalNature: NonPossession
}
```

## OWL++ Seed

```text
Class: Regression
Class: Relinquishment
Class: NonPossession
Class: Reacquisition
Class: NewPreparation
Class: PrincipalDhyanaPreparation
Class: TruthSeeingInSameLife

ObjectProperty: mayBeLostThrough
ObjectProperty: hasGeneralNature
ObjectProperty: reacquires
ObjectProperty: ensures

Heat mayBeLostThrough Regression
Summit mayBeLostThrough Regression

Regression hasGeneralNature NonPossession
Relinquishment hasGeneralNature NonPossession

Reacquisition reacquires NewPreparation

PrincipalDhyanaPreparation
    ensures TruthSeeingInSameLife
```

## Determinate Summary

Heat and Summits may be lost through regression. Acceptance and the Highest Mundane Dharmas are not lost through regression. Preparations based on a principal dhyāna lead to Truth-seeing in the same life. Preparations reacquired after loss are newly arisen preparations. Relinquishment and regression both have non-possession as their nature.