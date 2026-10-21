# VAK_2.40 — Ordinary Status

## 1. Sanskrit (Devanāgarī)

```sanskrit
कामाद्याप्तामलानां च मार्गस्याप्राप्तिरिष्यते ।
पृथग्जनत्वं तत्प्राप्तिभूसंचाराद्विहीयते ॥ २.४० ॥
```

## 2. Sanskrit (IAST)

```text
kāmādyāptāmalānāṃ ca mārgasyāprāptir iṣyate /
pṛthagjanatvaṃ tatprāptibhūsaṃcārād vihīyate // 2.40 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| kāma-ādi-āpta-amalānām | gen. pl. m.; compound | of realm-included and uncontaminated dharmas |
| mārgasya aprāptiḥ | gen. sg. m. + nom. sg. f. | non-acquisition of the path |
| iṣyate | 3 sg. passive present | is held to be; retains the account's attributed status |
| pṛthagjanatvam | nom. sg. n.; abstract noun | ordinary-person status |
| tat-prāpti-bhū-saṃcārāt | abl. sg.; compound coordinating two grounds | through acquisition of that dharma or transition of level |
| vihīyate | 3 sg. passive present indicative | is relinquished |

Ordinary person is the path-status. Not an insult. Not a nature.

```text
# tokens: kāmādyāptāmalānām ca mārgasya aprāptiḥ iṣyate pṛthagjanatvam tatprāptibhūsaṃcārāt vihīyate
```

## 4. Grammar

The opening inherits “threefold” from 2.39 but now classifies by Realm rather than time. The identification of ordinary-person status retains *iṣyate*, “is held.” The last clause returns to non-acquisition generally: *tat* refers to the dharma not acquired, not only to the path. The prose makes “relinquished” precise as arising of non-acquisition of that non-acquisition and severance of its acquisition, within the account under discussion.

```nltk-fcfg
% start S
# tokens: kāmādyāptāmalānām ca mārgasya aprāptiḥ iṣyate pṛthagjanatvam tatprāptibhūsaṃcārāt vihīyate
S[SEM=<(?realm & ?status & ?relinquishment)>] -> REALMS[SEM=?realm] STATUS[SEM=?status] RELINQUISHMENT[SEM=?relinquishment]
REALMS[SEM=<all x y.((DharmaClass(x) & Realm(y)) -> NonAcquisitionRealm(x,y)) & -Realm(uncontaminated)>] -> CLASSES ALSO
CLASSES -> 'kāmādyāptāmalānām'
ALSO -> 'ca'
STATUS[SEM=<HeldIdentification(path_nonacquisition,ordinary_status)>] -> PATH NONACQUISITION HELD ORDINARY
PATH -> 'mārgasya'
NONACQUISITION -> 'aprāptiḥ'
HELD -> 'iṣyate'
ORDINARY -> 'pṛthagjanatvam'
RELINQUISHMENT[SEM=<RelinquishmentGround(nonacquisition,acquiring_that_dharma) & RelinquishmentGround(nonacquisition,level_transition)>] -> GROUNDS RELINQUISHED
GROUNDS -> 'tatprāptibhūsaṃcārāt'
RELINQUISHED -> 'vihīyate'
```

```nltk-dep
'kāmādyāptāmalānām' -> 'ca'
'iṣyate' -> 'aprāptiḥ' | 'pṛthagjanatvam'
'aprāptiḥ' -> 'mārgasya'
'vihīyate' -> 'tatprāptibhūsaṃcārāt'
```

The constituent spans are [0, 2), [2, 6), and [6, 8). The two grounds are retained as such, not promoted to an exhaustive causal theory. Transition of level relinquishes the relevant level-specific non-acquisition; it is not attainment of the noble path.

## 5. Translation

### Literal Translation

> Of dharmas included in Desire and the other Realms, and of the uncontaminated, [non-acquisition is threefold]. Non-acquisition of the path is held to be ordinary-person status. [Non-acquisition] is relinquished through acquisition of that [dharma] or transition of level.

### Bhāṣya-informed study translation

> Non-acquisition of dharmas included in the Desire, Form, and Formless Realms, and of uncontaminated dharmas, may belong to any of the three Realms. Non-acquisition of the path is held to be ordinary-person status. Non-acquisition is relinquished through acquisition of the dharma concerned or through transition of level.

## 6. Philosophical Translation

> Non-acquisition is never itself uncontaminated. Its identification with ordinary-person status must distinguish having attained no noble dharma from merely lacking some noble dharma. The competing account locates ordinary status in a continuum where noble dharmas have not arisen; the ontological dispute remains open.

## 7. Technical Vocabulary

| Sanskrit | Running word | Determination |
|---|---|---|
| amala | uncontaminated | the dharma; not the non-acquisition |
| pṛthagjanatva | ordinary-person status | path-status |
| bhūsaṃcāra | transition of level | relinquishment of the relevant level-specific non-acquisition |
| vinā lābhenālābha | non-obtaining without obtaining | no attainment, not merely some missing attainment |
| prāpti-prāpti | acquisition of acquisition | mutual-possession reply to regress |
| sautrāntika | Sautrāntika | explicitly named alternative in this passage |

## 8. Logical Determination

```nltk-sem
realm_range : all x y.((DharmaClass(x) & Realm(y)) -> NonAcquisitionRealm(x,y))
ordinary_test : all x.(Person(x) & -exists y.(NobleDharma(y) & HasAttained(x,y)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((all x y.((DharmaClass(x) & Realm(y)) -> NonAcquisitionRealm(x,y)) & -Realm(uncontaminated)) & HeldIdentification(path_nonacquisition,ordinary_status) & (RelinquishmentGround(nonacquisition,acquiring_that_dharma) & RelinquishmentGround(nonacquisition,level_transition)))

# THEORY no_uncontaminated_nonacquisition
# EXPECT no_uncontaminated_nonacquisition T
all x.(DharmaClass(x) -> -NonAcquisitionRealm(x,uncontaminated))

# THEORY qualified_ordinary_test
# EXPECT qualified_ordinary_test T
all x.(Person(x) -> (OrdinaryByAbsence(x) <-> -exists y.(NobleDharma(y) & HasAttained(x,y))))

# THEORY reported_mutual_possession
# EXPECT reported_mutual_possession T
Secures(primary_acquisition,base_dharma) & Secures(primary_acquisition,higher_acquisition) & Secures(higher_acquisition,primary_acquisition)

# THEORY rejected_any_missing_noble_dharma_makes_ordinary
# EXPECT rejected_any_missing_noble_dharma_makes_ordinary F
all x.((Person(x) & exists y.(NobleDharma(y) & -HasAttained(x,y))) -> OrdinaryByAbsence(x))

# THEORY rejected_same_realm_only
# EXPECT rejected_same_realm_only F
all x y.(NonAcquisitionRealm(x,y) -> (x = y))
```

```nltk-valuation
uncontaminated => uncontaminated_class
path_nonacquisition => path_nonacquisition_term
ordinary_status => ordinary_status_term
nonacquisition => nonacquisition_term
acquiring_that_dharma => acquiring_that_dharma_ground
level_transition => level_transition_ground
primary_acquisition => primary_acquisition_token
base_dharma => base_dharma_token
higher_acquisition => higher_acquisition_token
DharmaClass => {desire_realm,form_realm,formless_realm,uncontaminated_class}
Realm => {desire_realm,form_realm,formless_realm}
NonAcquisitionRealm => {(desire_realm,desire_realm),(desire_realm,form_realm),(desire_realm,formless_realm),(form_realm,desire_realm),(form_realm,form_realm),(form_realm,formless_realm),(formless_realm,desire_realm),(formless_realm,form_realm),(formless_realm,formless_realm),(uncontaminated_class,desire_realm),(uncontaminated_class,form_realm),(uncontaminated_class,formless_realm)}
HeldIdentification => {(path_nonacquisition_term,ordinary_status_term)}
RelinquishmentGround => {(nonacquisition_term,acquiring_that_dharma_ground),(nonacquisition_term,level_transition_ground)}
Person => {ordinary_person,buddha}
NobleDharma => {buddha_attainment,disciple_lineage_attainment,solitary_lineage_attainment}
HasAttained => {(buddha,buddha_attainment)}
OrdinaryByAbsence => {ordinary_person}
Secures => {(primary_acquisition_token,base_dharma_token),(primary_acquisition_token,higher_acquisition_token),(higher_acquisition_token,primary_acquisition_token)}
```

The person/attainment inventory is illustrative, not a complete account of the Buddha's attainments. It tests the cited lineage counterexample and quantifier distinction. The three-token mutual-possession graph illustrates the reported reply, not its ontological truth or a bound on later proliferation. The prose's second- and third-moment counts, six and eighteen new acquisitions, are preserved in the Bhāṣya rather than replaced by a fabricated finite proof of the infinite-series critique.

## 9. Interpretive Note

**Translation note.** The commentary completes the threefold rule for non-acquisition in 2.39, now by Realm. It qualifies the absence defining ordinary status, reports another narrower definition, and explicitly names the Sautrāntika alternative. Relinquishment returns to non-acquisition generally before the regress discussion.

In the Organon reading, Cognition joins and governs Perception and Conception and guides the Dharma Base, without becoming consciousness or Mind. The negative side of the acquisition dyad requires scope and quantification: lacking some determination is not lacking every attainment. Mutual possession can answer a linear regress objection without answering the critic's separate objection to proliferation.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_2_40 a vak:Karika ; vak:hasTopic vak:OrdinaryStatus .
vak:OrdinaryStatus vak:requiresQualifiedAbsence true .
vak:NonAcquisition vak:relinquishmentGround
    vak:AcquiringConcernedDharma, vak:LevelTransition .
vak:MutualPossessionReply vak:distinctFrom vak:ProliferationCritique .
```
