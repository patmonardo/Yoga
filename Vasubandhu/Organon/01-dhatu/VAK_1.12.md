# VAK_1.12 — The Four Great Elements

## 1. Sanskrit (Devanāgarī)

> भूतानि पृथिवीधातुरप्तेजोवायुधातवः ।
>
> धृत्यादिकर्मसंसिद्धाः खरस्नेहोष्णतेरणाः ॥ १.१२ ॥॥

## 2. Sanskrit (IAST)

> bhūtāni pṛthivīdhātur aptejovāyudhātavaḥ /
>
> dhṛtyādikarmasaṃsiddhāḥ kharasnehoṣṇateraṇāḥ // 1.12 //

## 3. Lexical Analysis

```text
bhūtāni                 → the elements
pṛthivī-dhātuḥ           → the earth-principle
ap-tejo-vāyu-dhātavaḥ  → the water-, fire-, and wind-principles
dhṛti-ādi-karma-saṃsiddhāḥ → established in functions beginning with support
khara-sneha-uṣṇatā-īraṇāḥ → hardness, cohesion, heat, impulsion
```

| Pada | Morphology | Force in this passage |
|---|---|---|
| bhūtāni | nominative neuter plural | the elements; the four |
| pṛthivī-dhātuḥ | nominative | the earth-principle |
| ap-tejo-vāyu-dhātavaḥ | nominative plural | water, fire, wind |
| karma-saṃsiddhāḥ | nominative plural | established in the functions |
| dhṛti-ādi | compound member | beginning with support |
| khara | compound member | hardness |
| sneha | compound member | cohesion |
| uṣṇatā | compound member | heat |
| īraṇā | compound member | impulsion |

*Dhātu* here is the chapter word. The four are principles. *Skandha* in the
commentary's mass-sentence is a mass, not one of the five bases.

## 4. Grammar

```text
bhūtāni
    = pṛthivī-dhātuḥ
    + ap-tejo-vāyu-dhātavaḥ

those four
    = dhṛti-ādi-karma-saṃsiddhāḥ
    = khara-sneha-uṣṇatā-īraṇāḥ
```

The first line names them. The second gives function, then own-character.
The commentary pairs the lists in order.

## 5. Translation

### Literal Translation

The elements are the earth-principle and the water-, fire-, and
wind-principles. They are established in functions beginning with support:
hardness, cohesion, heat, and impulsion.

### Bhāṣya-informed study translation

The four great elements are those four principles. They are called principles
because they hold their own-character and derived form. Their greatness is
magnitude, as support of all other form, or a great gathering in the masses
of earth, water, fire, and wind, where the corresponding principle operates
prominently. The functions, in order, are support, gathering, ripening, and
spreading. The own-characters are hardness, cohesion, heat, and impulsion.
Lightness, named in the treatises, is derived form. Wind is the principle
whose own-character is impulsion. The function makes that character evident.

## 6. Philosophical Translation

Again, two lines. The first names the four. The second is function, then
own-character.

1.11 said depending on the great elements. This verse says which. Earth,
water, fire, wind — and each is a principle. Not a base. Not an essence. The
word is the chapter word.

They hold their own-character and derived form. That is why principle.
Greatness is two readings, both kept. Magnitude, as support of all other
form. Or a great gathering in the masses, where that principle operates
prominently. *Skandha* in that sentence is the mass. Not one of the five.

The functions are support, gathering, ripening, and spreading. Spreading is
increase and extension. The own-characters are hardness, cohesion, heat, and
impulsion. Impulsion is that by which the stream of elements is driven to
arise in another place, as a lamp-flame moves.

The treatises say the wind-principle is lightness of movement. That lightness
is also said to be derived form. Therefore wind is the dharma whose
own-character is impulsion. The function makes the character evident. Not
the reverse, and not a fifth element.

The next question distinguishes worldly form from the principle itself. Not
this verse.

## 7. Technical Vocabulary

| Sanskrit | Rendering | Note |
|---|---|---|
| bhūta | element | the four |
| mahābhūta | great element | magnitude, or gathering in masses |
| dhātu | principle | holds own-character and derived form |
| dhṛti | support | earth |
| saṃgraha | gathering | water |
| pakti | ripening | fire |
| vyūhana | spreading | wind; increase and extension |
| khara | hardness | own-character of earth |
| sneha | cohesion | own-character of water |
| uṣṇatā | heat | own-character of fire |
| īraṇā | impulsion | own-character of wind |
| svabhāva | own-character | the second list |
| laghutva | lightness | derived form; not the wind-principle |
| skandha | mass | in this sentence only; not a base |

## 8. Logical Determination

```text
1.11  depending on the great elements
1.12  which: four principles

earth    support      hardness
water    gathering    cohesion
fire     ripening     heat
wind     spreading    impulsion

principle → holds own-character and derived form
great     → support of all other form
          or gathering in the masses

lightness → derived form
wind      → impulsion
function makes own-character evident

1.13 not opened
```

## 9. Interpretive Note

The hinge is *dhātu*, then the two lists. Interpretation of the function is
in the Bhāṣya.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .

vak:VAK_1_12 a vak:Karika ;
    vak:hasTopic vak:FourGreatElements ;
    vak:belongsTo vak:Dhatunirdesa .

vak:EarthPrinciple vak:function vak:Support ;
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
