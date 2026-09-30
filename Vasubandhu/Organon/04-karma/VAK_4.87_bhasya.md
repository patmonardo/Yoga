# VAK 4.87 Bhāṣya — Action Classified by the Five Results

## 1. Kārikā Anchor

```iast
prahāṇamārge samale saphalaṃ karma pañcabhiḥ /
caturbhir amale 'nyac ca sāsravaṃ yac chubhāśubham // 4.87 //
```

> Action in the contaminated path of abandonment has all five results. In the
> uncontaminated path it has four; so too does other contaminated action,
> whether wholesome or unwholesome.

VAK 4.85 used a threefold practical account of results. This verse returns to
the complete Abhidharma taxonomy of five results and asks which result
relations belong to each class of action.

## 2. Continuous Sanskrit

```iast
yāni pūrvaṃ pañca phalāny uktāni, teṣāṃ katamat karma katibhiḥ phalaiḥ
saphalam?

prahāṇamārge samale saphalaṃ karma pañcabhiḥ /

prahāṇārthaṃ mārgaḥ, prahīyante vānena kleśā iti prahāṇamārgaḥ:
ānantaryamārgaḥ. tasmin sāsrave yat karma tat pañcabhiḥ phalaiḥ saphalam.

tasya hi vipākaphalaṃ svabhūmāviṣṭo vipākaḥ; niṣyandaphalaṃ samādhijā
uttare sadṛśā dharmāḥ; visaṃyogaphalaṃ visaṃyoga eva, yat tat prahāṇam;
puruṣakāraphalaṃ tadākṛṣṭā dharmāḥ, tadyathā vimuktimārgas tatsahabhuvaś
ca, yac cānāgataṃ bhāvyate, tac ca prahāṇam; adhipatiphalaṃ svabhāvād
anye sarvasaṃskārāḥ pūrvotpannavarjyāḥ.

caturbhir amale

anāsrave prahāṇamārge yat karma tac caturbhiḥ phalaiḥ saphalaṃ,
vipākaphalaṃ hitvā.

anyac ca sāsravaṃ yac chubhāśubham // 4.87 //

yac cānyat prahāṇamārgāt sāsravaṃ kuśalaṃ karma, yac cākuśalaṃ, tad api
caturbhir visaṃyogaphalaṃ hitvā.
```

The running source marks the opening question `[254|15]`, an impossible
regression after `[255|14]`; it is read as `[255|15]`. The transmitted
`svabhūmāviṣṭo vipākaḥ` is compact; it is retained without imposing a
conjectural compound division. The witness's `karmaṃ` at `[256|01–02]` is
normalized to `karma`.

## 3. Continuous Conventional Translation

Of the five results explained earlier, which kinds of action possess how many
results?

Action within a contaminated path of abandonment possesses all five results.
A path is directed toward abandonment, or the afflictions are abandoned by
means of it; hence “path of abandonment.” This is the uninterrupted path.
Any contaminated action within it possesses all five results.

Its maturation result is the maturation belonging to and entering its own
ground. Its corresponding result consists in later similar dharmas born from
samādhi. Its disconnection result is disconnection itself, the abandonment
in question. Its activity-produced result consists in the dharmas drawn forth
by it, such as the path of liberation and the dharmas arising together with
that path, as well as what is cultivated in the future and the abandonment.
Its dominant result consists in all conditioned dharmas other than itself,
except those that had already arisen.

Action within the uncontaminated path of abandonment possesses four results,
with the maturation result excluded.

Other contaminated action—whether wholesome action apart from the path of
abandonment or unwholesome action—also possesses four results, but here the
disconnection result is excluded.

## 4. The Five Results

The question presupposes the complete result set:

```text
1. vipākaphala       maturation result
2. niṣyandaphala     corresponding or outflow result
3. visaṃyogaphala    disconnection result
4. puruṣakāraphala   activity-produced result
5. adhipatiphala     dominant result
```

The five are not five objects that must appear separately. They are five
relations under which dharmas can stand as results of an action.

## 5. What the Path of Abandonment Is

The Bhāṣya gives two expansions of `prahāṇamārga`:

```text
path whose purpose is abandonment
path by which the afflictions are abandoned
```

It then identifies this with the uninterrupted path, `ānantaryamārga`. This
is the phase that directly removes the affliction. The liberation path that
follows is listed among the dharmas drawn forth by it.

This distinction must remain sharp:

```text
uninterrupted path → performs the abandonment
liberation path    → follows upon and confirms that abandonment
```

## 6. Why the Contaminated Abandonment Path Has Five

The contaminated path of abandonment can enter every result relation:

| Result | Bhāṣya determination |
|---|---|
| maturation | maturation associated with its own ground |
| corresponding | later similar samādhi-born dharmas |
| disconnection | the abandonment or disconnection itself |
| activity-produced | liberation path, co-arising dharmas, future cultivation, and abandonment drawn forth |
| dominant | other conditioned dharmas, excluding what arose previously |

One and the same abandonment can appear under more than one result relation.
As disconnection itself, it is `visaṃyogaphala`; insofar as it is brought
about through the path's activity, it can also enter the activity-produced
relation. The classification tracks causal aspect rather than assigning each
dharma to only one permanent result box.

## 7. Two Different Sets of Four

The two remaining action classes both have four results, but not the same
four:

```text
uncontaminated abandonment-path action
    = all five − maturation

other contaminated wholesome or unwholesome action
    = all five − disconnection
```

Uncontaminated action does not produce maturation because maturation belongs
to the contaminated causal order. Ordinary contaminated action does not
produce the disconnection result because it does not itself perform the
Path's abandonment of affliction.

This yields an important logical caution:

```text
equal cardinality ≠ identical membership
```

Both classes are “four-result” action, yet the omitted relation reveals their
opposite doctrinal characters.

## 8. Wholesome Does Not Mean Uncontaminated

The final phrase explicitly includes other `sāsrava` action that is either
wholesome or unwholesome. Ethical quality and contamination therefore form
independent coordinates:

```text
wholesome / unwholesome
contaminated / uncontaminated
Path / non-Path
```

A wholesome action can remain contaminated and produce maturation. An
uncontaminated action belongs to the Path relation and lacks maturation even
though it is efficacious under four other result modes.

## 9. Organon Contact Point

For the Organon, this passage is a result-interface matrix:

```text
ResultProfile(actionClass) = {
    maturation?,
    correspondence?,
    disconnection?,
    activityProduced?,
    dominance?
}
```

The profile must store exact membership, not merely a count. Two Program
Features may each expose four result channels while differing at the decisive
channel: one cannot generate conditioned maturation; the other cannot perform
release through disconnection.

The Path example also shows that one result can bear several causal aspects.
The schema should therefore model typed relations between an operation and
its results rather than assigning every result object one exclusive label.

These are Organon applications. The five-result ontology, the identification
of the uninterrupted path, and the exact result memberships are source
doctrine.

## 10. Review Status

The complete 4.87 unit `[255|15]–[256|02]` is included. It defines the path
of abandonment, supplies all five results of its contaminated form, excludes
maturation from its uncontaminated form, and excludes disconnection from
other contaminated wholesome and unwholesome action. It stops before the
first phrase of 4.88 at `[256|03]`. The erroneous line marker and witness
irregularities are explicitly recorded.
