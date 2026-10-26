# VAK 4.88 Bhāṣya — The Result Profile of Wholesome Action

## 1. Kārikā Anchor

> anāsravaṃ punaḥ śeṣaṃ tribhir avyākṛtaṃ ca yat /
> catvāri dve tathā trīṇi kuśalasya śubhādayaḥ // 4.88 //

> Other action without Influx, and indeterminate action, each have three
> results. For wholesome action, dharmas beginning with wholesome have four,
> unwholesome two, and indeterminate three results, respectively.

The first half completes the classification begun in 4.87. The second begins
a new matrix whose rows are the ethical qualities of action and whose columns
are the ethical qualities of the resulting dharmas.

## 2. Continuous Sanskrit

```iast
anāsravaṃ punaḥ śeṣaṃ tribhir avyākṛtaṃ ca yat /

prahāṇamārgād anyad anāsravaṃ karma, avyākṛtaṃ ca karma, tribhir
vipākavisaṃyogaphale hitvā.

catvāri dve tathā trīṇi kuśalasya śubhādayaḥ // 4.88 //

anukramam iti paścād vakṣyati. kuśalasya karmaṇaḥ kuśalā dharmāś
catvāri phalāni, vipākaphalaṃ hitvā; akuśalā dve,
puruṣakārādhipatiphale; avyākṛtās trīṇi, niṣyandavisaṃyogaphale hitvā.
```

The witness reads `kuśalsya` at `[256|06–07]`, normalized above to
`kuśalasya`. Its `strīṇi` at `[256|07–08]` is resolved by segmentation as
`avyākṛtās trīṇi`, “indeterminate dharmas, three.”

## 3. Continuous Translation

Action without Influx outside the Path of Abandonment possesses three results,
with maturation and disconnection excluded. Indeterminate action likewise
possesses three results, with maturation and disconnection excluded.

For wholesome action, the result counts for dharmas beginning with wholesome
are four, two, and three, respectively. The word “respectively” is stated
later.

Wholesome dharmas are related to wholesome action by four results, with the
maturation result excluded. Unwholesome dharmas are related to it by two
results: the activity-produced and dominant results. Indeterminate dharmas
are related to it by three results, with the corresponding and disconnection
results excluded.

## 4. Completion of the Action-class Table

VAK 4.87 classified three action classes. The opening of 4.88 adds two more:

| Class of action | Number | Excluded results |
|---|---:|---|
| action in the Path of Abandonment with stain (with Influx) | 5 | none |
| action in the Path without stain (without Influx) | 4 | maturation |
| other wholesome or unwholesome action with Influx | 4 | disconnection |
| other action without Influx, outside the Path | 3 | maturation and disconnection |
| indeterminate action | 3 | maturation and disconnection |

Again, equal counts do not establish identical causal character. Remaining
action without Influx and indeterminate action happen to omit the same two
relations, but for different doctrinal reasons.

The **remaining action without Influx** lies outside the uninterrupted Path;
it therefore does not perform the abandonment that would yield disconnection,
and without Influx it does not mature. **Indeterminate action** neither
produces maturation nor acts as the Path's direct abandonment.

## 5. A New Matrix: Quality of Action and Result

The second half changes the classificatory question. Previously the subject
was an action class and the issue was its total result profile. Now the
question is:

```text
Given wholesome action,
under how many result relations can
wholesome, unwholesome, and indeterminate dharmas
respectively be its results?
```

The ordered expression `śubhādayaḥ`, “beginning with wholesome,” governs the
three numbers:

```text
wholesome → 4
unwholesome → 2
indeterminate → 3
```

VAK 4.89 will apply the same ordered columns to unwholesome and indeterminate
action.

## 6. Exact Membership of the Wholesome Row

The Bhāṣya supplies the members hidden by the numbers:

| Results of wholesome action | Applicable relations | Excluded relations |
|---|---|---|
| wholesome dharmas | corresponding, disconnection, activity-produced, dominant | maturation |
| unwholesome dharmas | activity-produced, dominant | maturation, corresponding, disconnection |
| indeterminate dharmas | maturation, activity-produced, dominant | corresponding, disconnection |

Wholesome dharmas cannot be the maturation result of wholesome action because
`vipāka` is ethically indeterminate. Indeterminate dharmas can be maturation
results for precisely that reason.

The claim that unwholesome dharmas can be results of wholesome action does not
mean that goodness morally ripens into evil. Only the broad activity-produced
and dominant relations apply. An action can occasion or condition dharmas of
a different ethical quality without those dharmas becoming its maturation or
corresponding result.

## 7. Without Influx and Maturation

The opening determination sharpens our preceding discussion:

```text
action without Influx
    → no vipāka result
```

Action without Influx remains causally powerful. Outside the Path of
Abandonment it retains three result-relations: corresponding,
activity-produced, and dominant. What it does not do is produce a conditioned
maturation through which the agent receives a future karmic identity.

Freedom from Influx is therefore not withdrawal from efficacy:

```text
without maturation
    ≠
free from action or result
```

When action without Influx occurs in the Path of Abandonment, disconnection
is added as the fourth result. Outside that direct operation, the
disconnection relation is absent.

## 8. Interpretation

The full determination requires a typed relation rather than a single moral
label:

```text
ResultRelation {
    actionQuality
    resultQuality
    resultType
    pathContext
    stainStatus
    influxStatus
}
```

For the wholesome row, the matrix is:

```text
                 vipāka  niṣyanda  visaṃyoga  puruṣakāra  adhipati
wholesome           –        +          +           +          +
unwholesome         –        –          –           +          +
indeterminate       +        –          –           +          +
```

This prevents the Cardholder fallacy in our current joke: every consequence
need not become a maturation posted back to the identity account. An action
can produce or condition determinate effects without capitalizing them into
a future self.

The matrix and its Abhidharma exclusions belong to the source. The account
language and Absolute Predicate interpretation are Organon determinations.

## 9. Review Status

The complete 4.88 unit `[256|03]–[256|08]` is included. It completes the
action-class result table and gives the full wholesome-action row of the
quality matrix. It stops before the first phrase of 4.89 at `[256|08]`.
Witness irregularities are marked explicitly, and the source files remain
unchanged.
