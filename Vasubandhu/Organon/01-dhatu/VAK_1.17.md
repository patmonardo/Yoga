# VAK_1.17 — Mind Is the Sixth Support

## 1. Sanskrit (Devanāgarī)

```sanskrit
षण्णामनन्तरातीतं विज्ञानं यद्धि तन्मनः ।
षष्ठाश्रयप्रसिद्ध्यर्थं धातवोऽष्टादश स्मृताः ॥ १.१७ ॥
```

## 2. Sanskrit (IAST)

```text
ṣaṇṇām anantarātītaṃ vijñānaṃ yad dhi tan manaḥ /
ṣaṣṭhāśrayaprasiddhyarthaṃ dhātavo 'ṣṭādaśa smṛtāḥ // 1.17 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| ṣaṇṇām | genitive plural | of the six |
| anantara-atītam | nominative neuter | immediately past; just ceased |
| vijñānam | nominative neuter | a cognition, one of the six |
| yat / tat | nominative neuter | whichever, that |
| hi | particle | the reason |
| manaḥ | nominative neuter | mind |
| ṣaṣṭha-āśraya-prasiddhi-artham | accusative of purpose | so that the sixth support be established |
| dhātavaḥ | nominative plural | principles |
| aṣṭādaśa smṛtāḥ | numeral and participle | eighteen are taught |

The commentary tightens *anantarātīta* to *samanantara-niruddha*: ceased immediately before, nothing between.

**Grammar tokens.** Verse-order IAST, with sandhi opened and combined
lexical rows separated. The purpose compound remains one token. No covert
successor is supplied: its actual arising is not required for Mind status.

```text
# tokens: ṣaṇṇām anantara-atītam vijñānam yat hi tat manaḥ ṣaṣṭha-āśraya-prasiddhi-artham dhātavaḥ aṣṭādaśa smṛtāḥ
```

## 4. Grammar

The relative-correlative *yat … tat* restricts the cognition to one of the
six that is immediately past. The neuter adjective agrees with *vijñānam*;
plural *smṛtāḥ* agrees with *dhātavaḥ*. The purpose compound scopes over
the teaching of eighteen, not over the cessation of a cognition.

```nltk-fcfg
% start S
# tokens: ṣaṇṇām anantara-atītam vijñānam yat hi tat manaḥ ṣaṣṭha-āśraya-prasiddhi-artham dhātavaḥ aṣṭādaśa smṛtāḥ
S[SEM=<(?m & ?t)>] -> MINDCLAUSE[SEM=?m] TEACHING[SEM=?t]
MINDCLAUSE[SEM=<?rel(?six(?past(?cog)))(?mind)>] -> SIX[CASE=gen,SEM=?six] PAST[CASE=nom,NUM=?n,GEN=?g,SEM=?past] COG[CASE=nom,NUM=?n,GEN=?g,SEM=?cog] REL[CASE=nom,NUM=?n,GEN=?g,SEM=?rel] HI CORR[CASE=nom,NUM=?n,GEN=?g] MIND[CASE=nom,NUM=?n,GEN=?g,SEM=?mind]
TEACHING[SEM=<?purpose(?taught(?count))>] -> PURPOSE[SEM=?purpose] PRINCIPLES[CASE=nom,NUM=?n,GEN=?g] COUNT[SEM=?count] TAUGHT[CASE=nom,NUM=?n,GEN=?g,SEM=?taught]
SIX[CASE=gen,NUM=pl,SEM=<\P.\x.(P(x) & OfSixCognitions(x))>] -> 'ṣaṇṇām'
PAST[CASE=nom,NUM=sg,GEN=n,SEM=<\P.\x.(P(x) & ImmediatelyPast(x))>] -> 'anantara-atītam'
COG[CASE=nom,NUM=sg,GEN=n,SEM=<\x.Cognition(x)>] -> 'vijñānam'
REL[CASE=nom,NUM=sg,GEN=n,SEM=<\P.\Q.all x.(P(x) -> Q(x))>] -> 'yat'
HI -> 'hi'
CORR[CASE=nom,NUM=sg,GEN=n] -> 'tat'
MIND[CASE=nom,NUM=sg,GEN=n,SEM=<\x.MindRole(x)>] -> 'manaḥ'
PURPOSE[SEM=<\P.(P & ForEstablishing(principle_teaching,sixth_support))>] -> 'ṣaṣṭha-āśraya-prasiddhi-artham'
PRINCIPLES[CASE=nom,NUM=pl,GEN=m] -> 'dhātavaḥ'
COUNT[SEM=<eighteen>] -> 'aṣṭādaśa'
TAUGHT[CASE=nom,NUM=pl,GEN=m,SEM=<\n.TaughtCount(principle_teaching,n)>] -> 'smṛtāḥ'
```

```nltk-dep
'manaḥ' -> 'vijñānam' | 'tat'
'vijñānam' -> 'ṣaṇṇām' | 'anantara-atītam' | 'yat' | 'hi'
'smṛtāḥ' -> 'ṣaṣṭha-āśraya-prasiddhi-artham' | 'dhātavaḥ'
'dhātavaḥ' -> 'aṣṭādaśa'
```

**Close construe.** Of the six, whichever Cognition is immediately past,
that is Mind. Eighteen Principles are taught to establish the sixth support.

This does not add a seventh independent substance to the six Cognitions.
It establishes a relational office. `ImmediatelyPast` is evaluated at a
fixed contextual time in this first-order projection; it is not a
definition of all Mind by a timeless equation. The Bhāṣya's final arhat
case retains Mind status despite the absence of a successor. Support
status therefore does not entail actual production of another Cognition.

## 5. Translation

### Literal Translation

> Whichever cognition among the six is immediately past, that indeed is
> mind. The eighteen principles are taught in order to establish the sixth
> support.

### Bhāṣya-informed study translation

> Of the six Cognitions, whichever has just ceased is Mind. The eighteen
> Principles are taught so that Mind may be established as the sixth support.

## 6. Philosophical Translation

Again, two lines. The first answers 1.16. The second says why the count is eighteen.

The seventh name is not a seventh thing. Whichever of the six has just ceased, that is mind. Present, it is one of the six cognitions. Just ceased, it is the support of the next. Same cognition, two offices. The commentary's pictures are exact: the same person is son to one and father to another; the same fruit is seed to another.

The five have a support each. The sixth, the mental cognition, has none of that kind. Mind is taught so that the sixth support stand in the open. That is why eighteen, and not a reduced substance-count.

Eighteen here is six supports, six supported, and six that are borne. Mind is the sixth support. It is not a sixth eye.

The last test is quiet. If mind meant whatever produces the next, an arhat's final consciousness would fail the name. It does not fail. The office remains. The next does not arise, because another cause is wanting.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| vijñāna | cognition | one of the six; not consciousness; not principle |
| manas | mind | the same cognition, just ceased |
| manodhātu | mind-principle | the office, not a seventh substance |
| manovijñāna-dhātu | mental cognition-principle | the sixth of the six; the supported |
| anantarātīta | immediately past | ceased immediately before |
| āśraya | support | the office mind fills |
| āśrita | the supported | the six cognitions |
| ālambana | the borne | not the support |
| citta | consciousness | the arhat's final consciousness; not mind |
| dravyataḥ | by substance | the objection's count |
| prasiddhi | establishment | so that the sixth support be known |

## 8. Logical Determination

**Kārikā, derived.** A restricted universal assigns Mind status; a separate
purpose-qualified claim explains the eighteenfold teaching.

```nltk-sem
# derived by the section 4 parse
((all x.(((Cognition(x) & ImmediatelyPast(x)) & OfSixCognitions(x)) -> MindRole(x))) & (TaughtCount(principle_teaching,eighteen) & ForEstablishing(principle_teaching,sixth_support)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((all x.(((Cognition(x) & ImmediatelyPast(x)) & OfSixCognitions(x)) -> MindRole(x))) & (TaughtCount(principle_teaching,eighteen) & ForEstablishing(principle_teaching,sixth_support)))
```

```nltk-valuation
principle_teaching => teaching
eighteen => eighteen_count
sixth_support => mind_support
Cognition => {ceased,current,final}
OfSixCognitions => {ceased,current,final}
ImmediatelyPast => {ceased,final}
MindRole => {ceased,final}
TaughtCount => {(teaching,eighteen_count)}
ForEstablishing => {(teaching,mind_support)}
HasSuccessor => {ceased}
```

**Model checks.** `current` prevents the overstatement that every Cognition
is presently Mind. `final` has Mind status without a successor, representing
the commentary's limiting case rather than deriving it from the verse.
Removing Mind status from a just-ceased case must fail. Removing
immediacy from a case removes the rule's warrant; it does not assert that
all earlier Cognitions retain this particular temporal office.

**Bhāṣya determination.** The following support analysis and objection
are commentary elaboration, not extra output of the token parse.

```text
1.16   seven names: six cognitions + mind-principle
       relation not yet said

1.17   of those six, whichever has just ceased
           → mind
           → mind-principle, as support

       present office     one of the six
       just-ceased office mind, the sixth support

       five supports      eye and the rest
       sixth support      mind
       supported          six cognitions
       borne              six
       6 + 6 + 6 = 18

       objection          17, or 12, by substance
       reply              eighteen, for the sixth support

       arhat's last consciousness
           remains mind
           no successor, another cause wanting
           support ≠ production

1.18 not opened
```

The objection's twelve is a substance-count. It is not the twelve essences.

## 9. Interpretive Note

**Translation note.** The Bhāṣya identifies the just-ceased cognition as Mind
in its support-role for Mind-Cognition. The eighteenfold teaching establishes
the sixth support; the commentary contrasts this purpose with substance-counts
of seventeen or twelve and tests the account against an arhat's final
consciousness, which remains Mind although no successor arises because another
cause is wanting.

The hinge is *yat ... tat*: whichever, that. Interpretation of the office, and of the arhat's limit, is in the Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_17 a vak:Karika ;
    vak:hasTopic vak:MindAsSixthSupport ;
    vak:belongsTo vak:Dhatunirdesa ;
    vak:answers vak:VAK_1_16 .

vak:Mind vak:isOneOf vak:SixCognitions ;
    vak:when vak:ImmediatelyPast ;
    vak:functionsAs vak:SixthSupport ;
    vak:distinctFrom vak:SeventhSubstance .

vak:EighteenPrinciples vak:supports 6 ;
    vak:supported 6 ;
    vak:borne 6 .

vak:FinalArhatConsciousness vak:remains vak:Mind ;
    vak:hasSuccessor false ;
    vak:reason vak:AnotherCauseWanting .
```
