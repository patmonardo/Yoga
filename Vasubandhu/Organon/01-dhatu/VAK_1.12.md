# VAK_1.12 — The Four Great Elements

## 1. Sanskrit (Devanāgarī)

```sanskrit
भूतानि पृथिवीधातुरप्तेजोवायुधातवः ।
धृत्यादिकर्मसंसिद्धाः खरस्नेहोष्णतेरणाः ॥ १.१२ ॥
```

## 2. Sanskrit (IAST)

```text
bhūtāni pṛthivīdhātur aptejovāyudhātavaḥ /
dhṛtyādikarmasaṃsiddhāḥ kharasnehoṣṇateraṇāḥ // 1.12 //
```

## 3. Lexical Analysis

| Pada | Morphology | Force in this passage |
|---|---|---|
| bhūtāni | nominative neuter plural | the four Elements |
| pṛthivī-dhātuḥ | nominative masculine singular | the Earth Principle |
| ap-tejo-vāyu-dhātavaḥ | nominative masculine plural copulative compound | Water, Fire, Wind Principles |
| dhṛty-ādi-karma-saṃsiddhāḥ | nominative masculine plural compound | established in functions beginning with support |
| khara-sneha-uṣṇatā-īraṇāḥ | nominative masculine plural copulative predicate compound | hardness, cohesion, heat, impulsion |

*Dhātu* is the chapter word for Principle; *bhūta* names an Element. The four
Elements are identified as Earth, Water, Fire, and Wind Principles. In the
commentary’s mass-sentence, *skandha* means a mass, not a technical Base.

**Grammar tokens.** Verse-order IAST with external sandhi opened and
compound boundaries marked. Compounds remain whole leaves: the Bhāṣya
explains their members and order. No covert token is needed.

```text
# tokens: bhūtāni pṛthivī-dhātuḥ ap-tejo-vāyu-dhātavaḥ dhṛty-ādi-karma-saṃsiddhāḥ khara-sneha-uṣṇatā-īraṇāḥ
```

## 4. Grammar

The neuter plural *bhūtāni* names the class. Singular Earth Principle
plus the plural compound Water–Fire–Wind gives a masculine plural
resumption for the second line. This is not gender agreement between
*bhūtāni* and every predicate noun.

```nltk-fcfg
% start S
# tokens: bhūtāni pṛthivī-dhātuḥ ap-tejo-vāyu-dhātavaḥ dhṛty-ādi-karma-saṃsiddhāḥ khara-sneha-uṣṇatā-īraṇāḥ
S[SEM=<?roster(?description)>] -> ROSTER[NUM=?n,GEN=?g,SEM=?roster] DESCRIPTION[NUM=?n,GEN=?g,SEM=?description]
ROSTER[NUM=pl,GEN=m,SEM=<?rest(?earth)(?class)>] -> CATEGORY[CASE=nom,NUM=pl,GEN=n,SEM=?class] EARTH[CASE=nom,NUM=sg,GEN=m,SEM=?earth] OTHERS[CASE=nom,NUM=pl,GEN=m,SEM=?rest]
DESCRIPTION[NUM=?n,GEN=?g,SEM=<?functions(?characters)>] -> FUNCTIONS[CASE=nom,NUM=?n,GEN=?g,SEM=?functions] CHARACTERS[CASE=nom,NUM=?n,GEN=?g,SEM=?characters]
CATEGORY[CASE=nom,NUM=pl,GEN=n,SEM=<\x.GreatElement(x)>] -> 'bhūtāni'
EARTH[CASE=nom,NUM=sg,GEN=m,SEM=<earth>] -> 'pṛthivī-dhātuḥ'
OTHERS[CASE=nom,NUM=pl,GEN=m,SEM=<\e.\C.\P.((all x.(C(x) <-> (x = e | x = water | x = fire | x = wind))) & P(e)(water)(fire)(wind))>] -> 'ap-tejo-vāyu-dhātavaḥ'
FUNCTIONS[CASE=nom,NUM=pl,GEN=m,SEM=<\P.\e.\w.\f.\v.(EstablishedInSupportEtc(e) & EstablishedInSupportEtc(w) & EstablishedInSupportEtc(f) & EstablishedInSupportEtc(v) & P(e)(w)(f)(v))>] -> 'dhṛty-ādi-karma-saṃsiddhāḥ'
CHARACTERS[CASE=nom,NUM=pl,GEN=m,SEM=<\e.\w.\f.\v.(OwnCharacter(e,hardness) & OwnCharacter(w,cohesion) & OwnCharacter(f,heat) & OwnCharacter(v,impulsion))>] -> 'khara-sneha-uṣṇatā-īraṇāḥ'
```

```nltk-dep
'bhūtāni' -> 'pṛthivī-dhātuḥ' | 'ap-tejo-vāyu-dhātavaḥ'
'ap-tejo-vāyu-dhātavaḥ' -> 'dhṛty-ādi-karma-saṃsiddhāḥ' | 'khara-sneha-uṣṇatā-īraṇāḥ'
```

**Close construe.** The Elements are the Earth Principle and the Water,
Fire, and Wind Principles; established in functions beginning with
support, they are hardness, cohesion, heat, and impulsion.

The ordered roster feeds the second line. The Bhāṣya's *yathākramam*
("in order") determines the distributive reading of the character
compound. This ordering is declared in the lexical semantics, not
discovered by the parser. *Ādi* leaves the rest of the function list
compressed: the parse derives `EstablishedInSupportEtc`, not four
unwritten function words. The full ordered functions are prose rules
in §8. Numeral distinctness and actual roster size are tested separately.

## 5. Translation

### Literal Translation

> The Elements are the Earth Principle and the Water, Fire, and Wind Principles.
> They are established in functions beginning with support: hardness,
> cohesion, heat, and impulsion.

### Bhāṣya-informed study translation

> The four Great Elements are the Earth, Water, Fire, and Wind Principles,
> each sustaining its own-character and derived Form. In that order, their
> functions are support, gathering, ripening, and spreading (growth and
> extension), while their own-characters are hardness, cohesion, heat, and
> impulsion.

## 6. Philosophical Translation

Again, two lines. The first names the four. The second is function, then
own-character.

1.11 said depending on the Great Elements. This verse says which. Earth,
Water, Fire, and Wind Principles. Each holds its own-character and derived
Form. Each is a Principle, not a Base or Essence.

They hold their own-character and derived Form. That is why each is a Principle.
Greatness is two readings, both kept. Magnitude, as support of all other
Form. Or a great gathering in the masses, where that Principle operates
prominently. *Skandha* in that sentence is the mass. Not one of the five.

The functions are support, gathering, ripening, and spreading. Spreading is
increase and extension. The own-characters are hardness, cohesion, heat, and
impulsion. Impulsion is that by which the stream of Great Elements is driven to
arise in another place, as a lamp-flame moves.

The treatises say the Wind Principle is lightness of movement. That lightness
is also said to be derived Form. Therefore Wind is the Dharma whose
own-character is impulsion. The function makes the character evident. Not
the reverse, and not a fifth Element.

The next question distinguishes worldly Form from the Principle itself. Not
this verse.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| bhūta | Element | the four |
| mahābhūta | Great Element | magnitude, or gathering in masses |
| dhātu | Principle | here it names the principled determination |
| dhṛti | support | earth |
| saṃgraha | gathering | water |
| pakti | ripening | fire |
| vyūhana | spreading | wind; increase and extension |
| khara | hardness | own-character of earth |
| sneha | cohesion | own-character of water |
| uṣṇatā | heat | own-character of fire |
| īraṇā | impulsion | own-character of wind |
| svabhāva | own-character | the second list |
| laghutva | lightness | derived Form; not the Wind Principle |
| skandha | mass | in the commentary’s heap-sentence; not a technical Base |

## 8. Logical Determination

**Kārikā, derived.** Four named Principles instantiate the Element class.
The function-series and character-series remain distinct predicates.

```nltk-sem
# derived by the section 4 parse
((all x.(GreatElement(x) <-> (x = earth | x = water | x = fire | x = wind))) & (EstablishedInSupportEtc(earth) & EstablishedInSupportEtc(water) & EstablishedInSupportEtc(fire) & EstablishedInSupportEtc(wind) & OwnCharacter(earth,hardness) & OwnCharacter(water,cohesion) & OwnCharacter(fire,heat) & OwnCharacter(wind,impulsion)))
```

```nltk-fol
# THEORY verse
# EXPECT verse T
((all x.(GreatElement(x) <-> (x = earth | x = water | x = fire | x = wind))) & (EstablishedInSupportEtc(earth) & EstablishedInSupportEtc(water) & EstablishedInSupportEtc(fire) & EstablishedInSupportEtc(wind) & OwnCharacter(earth,hardness) & OwnCharacter(water,cohesion) & OwnCharacter(fire,heat) & OwnCharacter(wind,impulsion)))
# THEORY prose
# EXPECT prose T
Function(earth,support) & Function(water,gathering) & Function(fire,ripening) & Function(wind,spreading)
all x.(GreatElement(x) -> (Principle(x) & HoldsOwnCharacter(x) & HoldsDerivedForm(x)))
Elaboration(spreading,growth) & Elaboration(spreading,extension)
DerivedForm(lightness) & -OwnCharacter(wind,lightness)
# THEORY rejected_function_equals_character
# EXPECT rejected_function_equals_character F
support = hardness
# THEORY rejected_wind_is_lightness
# EXPECT rejected_wind_is_lightness F
all x.((GreatElement(x) & x = wind) -> OwnCharacter(x,lightness))
# THEORY rejected_lightness_is_fifth_great_element
# EXPECT rejected_lightness_is_fifth_great_element F
exists x.(GreatElement(x) & x = lightness)
```

```nltk-valuation
earth => earth_principle
water => water_principle
fire => fire_principle
wind => wind_principle
support => support_function
gathering => gathering_function
ripening => ripening_function
spreading => spreading_function
hardness => hardness_character
cohesion => cohesion_character
heat => heat_character
impulsion => impulsion_character
lightness => lightness_case
growth => growth_determination
extension => extension_determination
GreatElement => {earth_principle,water_principle,fire_principle,wind_principle}
Principle => {earth_principle,water_principle,fire_principle,wind_principle}
EstablishedInSupportEtc => {earth_principle,water_principle,fire_principle,wind_principle}
OwnCharacter => {(earth_principle,hardness_character),(water_principle,cohesion_character),(fire_principle,heat_character),(wind_principle,impulsion_character)}
Function => {(earth_principle,support_function),(water_principle,gathering_function),(fire_principle,ripening_function),(wind_principle,spreading_function)}
HoldsOwnCharacter => {earth_principle,water_principle,fire_principle,wind_principle}
HoldsDerivedForm => {earth_principle,water_principle,fire_principle,wind_principle}
DerivedForm => {lightness_case}
Elaboration => {(spreading_function,growth_determination),(spreading_function,extension_determination)}
```

**Model checks.** The four Principle constants have distinct denotations,
and exactly four representatives instantiate `GreatElement`. Removing
any character assignment or exchanging two characters fails the derived
formula. Swapping functions fails the separate prose theory. Lightness
remains derived Form, neither Wind's own-character nor a fifth Great
Element. This finite model does not identify all Principles with Elements;
the equality of these two extensions in this local witness is not a
general classification rule.

**Bhāṣya determination.** Holding own-character and derived Form explains
the Principle designation. Greatness has two explanations: magnitude as
support of other Form, or great gathering in masses where the respective
operation is prominent. These explanations are not two additional
Elements. Wind's operation makes impulsion evident; the model records its
character and function without pretending to simulate that disclosure or
the movement of the Element stream.

**Organon interpretation.** Function and character give a local test for
the reciprocal architecture: operation must disclose a determination
without becoming its synonym. The roster below is not itself a derivation
of the syllogistic movement; it supplies determinate content on which that
interpretation must work.

```text
1.11  depending on the Great Elements
1.12  which: four Great Elements, as Principles

Earth    support      hardness
Water    gathering    cohesion
Fire     ripening     heat
Wind     spreading    impulsion

Principle → holds own-character and derived Form
great     → support of all other Form
          or gathering in the masses

lightness → derived Form
Wind      → impulsion
function makes own-character evident

1.13 not opened
```

## 9. Interpretive Note

The hinge is *dhātu*, then the two lists. Interpretation of the function is
in the Bhāṣya.

**Reciprocal architecture.** In our developing Skandha machine,
`S–P–U / P–S–U → S–U–P` articulates the reciprocity of Form and Essence
within one Universal. Form Base names the Intuition side; **Essence Base**
is our logical handle for Dharma Āyatana, the Concept side, not a replacement
translation of *skandha*. Absolute Knowing comprehends their mediation.
Here, the concrete constraint is that function and own-character remain
distinguishable while operation makes character evident. This verse does
not itself enumerate those logical Bases or derive that syllogistic
sequence, nor does Elemental dependence alone establish Knowledge.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_12 a vak:Karika ;
    vak:hasTopic vak:FourGreatElements ;
    vak:belongsTo vak:Dhatunirdesa .

vak:PrincipledEarth vak:function vak:Support ;
    vak:ownCharacter vak:Hardness .
vak:WaterPrinciple vak:function vak:Gathering ;
    vak:ownCharacter vak:Cohesion .
vak:FirePrinciple vak:function vak:Ripening ;
    vak:ownCharacter vak:Heat .
vak:WindPrinciple vak:function vak:Spreading ;
    vak:ownCharacter vak:Impulsion ;
    vak:not vak:Lightness .
vak:Lightness vak:is vak:DerivedForm .
```
