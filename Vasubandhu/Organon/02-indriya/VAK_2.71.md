# VAK_2.71 — Four and Twenty

## 1. Sanskrit (Devanāgarī)

```sanskrit
तस्माच्चत्वारि चित्तानि द्वादशैतानि विंशतिः /
प्रायोगिकोपपत्त्याप्तं शुभं भित्त्वा त्रिषु द्विधा // २.७१ //
```

## 2. Sanskrit (IAST)

```text
tasmāc catvāri cittāni dvādaśaitāni viṃśatiḥ /
prāyogikopapattyāptaṃ śubhaṃ bhittvā triṣu dvidhā // 2.71 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| tasmāt | ablative singular | from that |
| catvāri | nominative plural | four |
| cittāni | neuter nominative plural | consciousnesses |
| dvādaśa | nominative plural | twelve |
| etāni | neuter nominative plural | these |
| viṃśatiḥ | nominative singular | twenty |
| prāyogika | adjectival | application-produced |
| upapattyāpta | adjectival | obtained through birth |
| śubham | neuter nominative singular | wholesome |
| bhittvā | gerund | having divided |
| triṣu | locative plural | in the three |
| dvidhā | adverbial | twofold |

**Grammar tokens.** Sandhi is opened in *tasmāc* and *dvādaśaitāni*; the compound *prāyogikopapattyāptam* is opened into its two contrasted kinds. The Bhāṣya identifies the antecedent of *tasmāt* as beyond-training.

```text
# tokens: tasmāt catvāri cittāni dvādaśa etāni viṃśatiḥ prāyogika upapattyāpta śubham bhittvā triṣu dvidhā
```

## 4. Grammar

The first clause gives the four following beyond-training; the Bhāṣya supplies that antecedent. The second announces the twenty from the twelve. The third gives this verse's twofold split of wholesome mind in the three realms. Its arithmetic effect is three additional kinds, producing fifteen at this stage; the announced twenty is not yet a completed count.

```nltk-fcfg
% start S
# tokens: tasmāt catvāri cittāni dvādaśa etāni viṃśatiḥ prāyogika upapattyāpta śubham bhittvā triṣu dvidhā
S[SEM=<(?four & ?twenty & ?split)>] -> FOUR[SEM=?four] TWENTY[SEM=?twenty] SPLIT[SEM=?split]
FOUR[SEM=<SuccessorCount(beyond_training,four)>] -> FROM_THAT[CASE=abl] FOUR_NUM[CASE=nom,CNT=4] CITTA[CASE=nom,NUM=pl]
FROM_THAT[CASE=abl] -> 'tasmāt'
FOUR_NUM[CASE=nom,CNT=4] -> 'catvāri'
CITTA[CASE=nom,NUM=pl] -> 'cittāni'
TWENTY[SEM=<AnnouncedCount(twelve_inventory,twenty)>] -> TWELVE[CASE=nom,CNT=12] THESE[CASE=nom,NUM=pl] TWENTY_NUM[CASE=nom,CNT=20]
SPLIT[SEM=<TwofoldWholesome(three_realms,application,birth)>] -> APP[FORCE=adj] BIRTH[FORCE=adj] WHOL[CASE=acc] DIVIDING IN_THREE[CASE=loc,CNT=3] TWOFOLD[FORCE=adv]
TWELVE[CASE=nom,CNT=12] -> 'dvādaśa'
THESE[CASE=nom,NUM=pl] -> 'etāni'
TWENTY_NUM[CASE=nom,CNT=20] -> 'viṃśatiḥ'
APP[FORCE=adj] -> 'prāyogika'
BIRTH[FORCE=adj] -> 'upapattyāpta'
WHOL[CASE=acc] -> 'śubham'
DIVIDING -> 'bhittvā'
IN_THREE[CASE=loc,CNT=3] -> 'triṣu'
TWOFOLD[FORCE=adv] -> 'dvidhā'
```

```nltk-dep
'catvāri' -> 'tasmāt' | 'cittāni'
'viṃśatiḥ' -> 'dvādaśa' | 'etāni'
'śubham' -> 'prāyogika' | 'upapattyāpta' | 'bhittvā' | 'triṣu' | 'dvidhā'
```

**Feature chart checkpoints.** The four-successors span [0, 3), the announced count [3, 6), and the twofold split [6, 12); the root spans [0, 12). Count, case, and the contrasting kind features constrain these spans. The intermediate fifteen is a Bhāṣya-guided arithmetic inference, not an additional phrase in the verse.

## 5. Translation

### Literal Translation

> From that, four consciousnesses. These twelve are twenty, by dividing
> wholesome [consciousness] in the three realms twofold.

### Bhāṣya-informed study translation

> Four minds follow beyond-training. These twelve are reckoned as twenty;
> wholesome mind in the three realms is divided into two kinds, application-produced and birth-acquired.

## 6. Philosophical Translation

> The four successors close the twelvefold inventory. The verse announces a twentyfold inventory and begins its construction by splitting each realm's wholesome mind into two kinds. This first split adds three kinds, giving fifteen as an intermediate count.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| prāyogika | application-produced | one of the two kinds of wholesome |
| upapattyāpta | obtained through birth | the other kind of wholesome |
| śubha | wholesome | divided twofold in the three realms |

## 8. Logical Determination

**Kārikā, derived.** The root SEM states the four-successors claim, the announced twenty, and the twofold division. The Bhāṣya identifies the four and the two kinds. Arithmetic gives an intermediate fifteen; this division alone does not produce twenty.

```nltk-sem
four : SuccessorCount(beyond_training,four)
twenty : AnnouncedCount(twelve_inventory,twenty)
split : TwofoldWholesome(three_realms,application,birth)
```

```nltk-fol
# THEORY verse
# EXPECT verse T
(SuccessorCount(beyond_training,four) & AnnouncedCount(twelve_inventory,twenty) & TwofoldWholesome(three_realms,application,birth))

# THEORY prose_not_complete
# EXPECT prose_not_complete T
-CompletedByThisCutAlone(twenty_inventory)

# THEORY prose_fifteen
# EXPECT prose_fifteen T
(ThreeWholesomeBecomeSix(three_realms) & IntermediateCount(after_split,fifteen))

# THEORY rejected_completed_by_this_cut
# EXPECT rejected_completed_by_this_cut F
(AnnouncedCount(twelve_inventory,twenty) & CompletedByThisCutAlone(twenty_inventory))
```

```nltk-valuation
beyond_training => beyond
four => four_count
twelve_inventory => twelve_kinds
twenty => twenty_count
twenty_inventory => twenty_kinds
three_realms => three
application => application_kind
birth => birth_kind
after_split => intermediate_inventory
fifteen => fifteen_count
SuccessorCount => {(beyond,four_count)}
AnnouncedCount => {(twelve_kinds,twenty_count)}
TwofoldWholesome => {(three,application_kind,birth_kind)}
CompletedByThisCutAlone => {}
ThreeWholesomeBecomeSix => {three}
IntermediateCount => {(intermediate_inventory,fifteen_count)}
```

The finite model witnesses the distinct claims of an announced twenty and a present twofold split. It rejects completion by that split alone. It tests the arithmetic inference separately; it does not prove the Sanskrit reading.

## 9. Interpretive Note

**Translation note.** The Bhāṣya identifies the four as the wholesome minds of the three realms and beyond-training. It identifies the two kinds of wholesome mind as application-produced and birth-acquired. Each of the three wholesome kinds becomes two, so this operation adds three to twelve. The twenty is announced, not completed, here.

The verse closes the twelve and begins the twenty. The remaining steps are deferred.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_71 a vak:Karika ; vak:hasTopic vak:FourAndTwenty .
vak:Twelve vak:announcedCount 20 .
vak:Wholesome vak:dividedTwofoldIn vak:ThreeRealms .
```
