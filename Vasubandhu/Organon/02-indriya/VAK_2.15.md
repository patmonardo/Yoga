# VAK_2.15

## 1. Sanskrit (Devanāgarī)

> निरोधयत्युपरमान्नारूप्ये जीवितं मनः ।
>
> उपेक्षां चैव रूपेऽष्टौ कामे दश नवाष्टौ वा ॥ २.१५ ॥

## 2. Sanskrit (IAST)

> nirodhayaty uparamān nārūpye jīvitaṃ manaḥ /
>
> upekṣāṃ caiva rūpe 'ṣṭau kāme daśa navāṣṭau vā // 2.15 //

The transmitted sequence `uparamān nārūpye` is morphologically compressed
and uncertain in isolation. The Bhāṣya unambiguously construes the clause as
the faculties ceased by one dying in the formless realm; that construction
governs the translations below.

## 3. Padaccheda

```text
nirodhayaty        → nirodhayati
uparamān nārūpye  → transmitted phrase; Bhāṣya: at death in the formless realm
jīvitaṃ            → jīvitam
manaḥ              → manaḥ
upekṣāṃ caiva      → upekṣām ca eva
rūpe 'ṣṭau         → rūpe aṣṭau
kāme               → kāme
daśa               → daśa
navāṣṭau vā        → nava aṣṭau vā
```

| Form | Morphology | Lexical force here |
|---|---|---|
| nirodhayati | third-person singular causative present | causes to cease / brings to cessation |
| uparamān nārūpye | transmitted sequence | construed by the Bhāṣya with death in the formless realm |
| jīvitam | accusative neuter singular | life-faculty |
| manaḥ | accusative neuter singular | mind-faculty |
| upekṣām | accusative feminine singular | neutral-feeling faculty |
| ca eva | conjunction plus emphatic particle | and indeed / and also |
| rūpe | locative neuter singular | in the form realm |
| aṣṭau | accusative plural numeral | eight faculties |
| kāme | locative masculine singular | in the desire realm |
| daśa | accusative plural numeral | ten faculties |
| nava | accusative plural numeral | nine faculties |
| vā | alternative particle | or |

Here `nirodha` is terminal cessation of possessed faculties at death. It is
not, without further qualification, the liberative cessation discussed in
other contexts.

## 4. Grammar

The Bhāṣya supplies the governing question:

```text
kasmindhātau mriyamāṇaḥ katīndriyāṇi nirodhayati
    → dying in which realm, how many faculties does one cause to cease?
```

It resolves the first line as:

```text
formless realm:
    jīvitam
    manaḥ
    upekṣām
        → life, mind, and neutral feeling cease
```

The second line gives two further realm counts:

```text
rūpe aṣṭau
    → eight in the form realm

kāme daśa nava aṣṭau vā
    → in the desire realm, ten, nine, or eight
```

The alternatives depend upon sexual configuration:

```text
both sexual faculties present
    → 10

one present
    → 9

neither present
    → 8
```

The Bhāṣya explicitly limits these Kārikā counts to `sakṛn-maraṇa`, death in
which the relevant faculties cease all at once. It introduces gradual death
only with the next Kārikā, so that separate count is not imported here.

## 5. Translation

### Close syntactic construe

> At death in the formless realm [according to the Bhāṣya's construal], one causes life, mind, and neutral feeling to cease; in the form realm, eight; in the desire realm, ten, nine, or eight.

### Bhāṣya-informed translation

> At death in the formless realm, the faculties of life, mind, and neutral feeling cease. At death in the form realm, those three and the five sensory faculties cease, making eight. At simultaneous death in the desire realm, eight, nine, or ten cease according to whether neither, one, or both sexual faculties are present.

The realm profiles are:

```text
formless:
    life + mind + neutral feeling = 3

form:
    life + mind + neutral feeling
    + five sensory faculties = 8

desire:
    base eight
    + no sexual faculty = 8
    + one sexual faculty = 9
    + both sexual faculties = 10
```

## 6. Philosophical Translation

> The end of a continuum is analyzed through the coordinated cessation of its governing faculties. Realm and embodied configuration determine the terminal faculty-set. Even the formless continuum ends through a threefold cessation of life, mind, and neutral feeling; form adds the sensory faculties, while desire may add one or both sexual faculties.

Organon rendering:

> The Kośa gives the Agent a realm-sensitive terminal profile. Termination acts upon the faculties actually possessed at runtime, not merely upon those initially acquired as maturation-result. The shutdown configuration is therefore not the inverse of the constructor: faculties present or acquired under other causal statuses must also be accounted for at cessation.

“Terminal profile” is an Organon rendering. The textual frame is `tyāga`,
loss of faculties at death, and `nirodha`, their cessation.

**Transcendental Time determination (Organon, not translation):** Death marks a terminal relation to the faculties possessed in a particular realm-profile, not the inverse of initial maturation-acquisition or a universal shutdown sequence. Universal Cognition distinguishes simultaneous cessation from the gradual case taken up next; the particular Ideas are the terminal sets of faculties in each realm and sexual configuration. The count is conditional, not an account of every mode of dying.

## 7. Technical Vocabulary

| Sanskrit | Project rendering | Determination |
|---|---|---|
| tyāga | loss / relinquishment | Bhāṣya heading for the inverse topic after acquisition |
| nirodhayati | causes to cease | cessation of possessed faculties at death |
| uparama | stopping / death | terminal context indicated by the Kārikā's compressed phrase |
| maraṇa | death | Bhāṣya's explicit determination of the context |
| ārūpya | formless realm | three-faculty terminal profile |
| rūpa | form realm | eight-faculty terminal profile |
| kāma | desire realm | eight-, nine-, or ten-faculty terminal profile |
| sakṛn-maraṇa | death occurring all at once | mode presupposed by the Kārikā's realm counts |
| samagra-indriya | possessing complete faculties | condition of spontaneously born form-realm beings at arising and death |
| vyañjana | sexual characteristic | determines the desire-realm variation from eight to ten |

The next Bhāṣya unit contrasts gradual death, but its count and inseparable
terminal cluster belong to VAK 2.16 and are not advanced here.

## 8. Logical Determination

Terminal configuration is parameterized by realm and embodiment:

```text
TerminalFacultySet
    = f(Realm, SexualConfiguration, DeathMode)
```

For the Kārikā's simultaneous-death mode:

```text
Realm = Formless
∧ DeathMode = Simultaneous
    → TerminalFacultySet = {Life, Mind, NeutralFeeling}
    → Count = 3
```

```text
Realm = Form
∧ DeathMode = Simultaneous
    → TerminalFacultySet = {Life,
                            Mind,
                            NeutralFeeling,
                            FiveSensoryFaculties}
    → Count = 8
```

```text
Realm = Desire
∧ DeathMode = Simultaneous
    → BaseTerminalSet = {Life,
                         Mind,
                         NeutralFeeling,
                         FiveSensoryFaculties}

SexualConfiguration = None
    → Count = 8

SexualConfiguration = One
    → Count = 9

SexualConfiguration = Both
    → Count = 10
```

Initialization and termination are asymmetric:

```text
InitialVipakaSet(context)
    ≠ TerminalFacultySet(context)
```

For example:

```text
FormlessInitialVipakaSet = {Life}

FormlessTerminalFacultySet
    = {Life, Mind, NeutralFeeling}
```

The difference follows from classification scope:

```text
InitialVipakaSet
    → only faculties first acquired as maturation-result

TerminalFacultySet
    → relevant faculties possessed when the continuum ends
```

## 9. Interpretive Note

**Organon time-reading:** The terminal profile is determined by the configuration that has come to be and by the specified mode of dying. Its symmetry with initialization is not assumed: formless initial `vipāka` acquisition is life alone, whereas the terminal set includes mind and neutral feeling. This is a temporal boundary of one conditioned continuum, not a claim about every possible continuation.

VAK 2.15 answers the inverse question to VAK 2.14, but it does not simply
reverse the preceding lists. Initial acquisition asked which faculties are
first obtained as `vipāka`. Terminal cessation asks which possessed faculties
cease at death. These are different relations over different temporal states.

The formless case makes the difference undeniable. Only life was initially
counted as maturation-result in VAK 2.14; Mind and neutral feeling were
nonetheless present at relinking, though their afflicted instances were not
counted as *vipāka*. At death, all three—Life, Mind, and neutral feeling—are
included in the terminal cessation count.

The form-realm case has the same structure. Its sixfold initial *vipāka*
count consisted of the five sensory Faculties and Life; it did not claim that
Mind and neutral feeling were absent at relinking. At death, all eight are
counted. Desire-realm terminal variation is then determined by the presence
of neither, one, or both sexual Faculties.

**Return to Dhātu at VAK 1.48.** The death profiles do not redraw Dhātu's
typed incidence map: the five sensory Faculties correspond to the five
internal sensory Domains; Mind-Faculty is mapped across the seven Citta
Domains; Female and Male Faculties occupy part of the Body-Domain; and Life
and the feeling Faculties, among others, occupy a portion of the
Essence-Domain. VAK 2.15 applies a temporal predicate—cessation at death—to
the Faculties possessed in each realm-profile. In the formless case, the
non-inclusion of sensory Faculties in the terminal set is a realm-bound
condition, not a denial of their Dhātu loci. The Organon return negates a
merely static reading of the map by reconstructing its Faculties as operative
and relinquished in a specific terminal event; it does not erase or replace
the Dhātu map itself.

The Bhāṣya also guards the scope of the counts. They describe death occurring
all at once. Gradual death follows a different dependency structure, which
the next verse will state. We therefore should not yet treat the present
realm profiles as a universal shutdown algorithm.

For the genetically layered Object Model, the consequence is exact:

```text
construction history
    does not alone determine terminal state

the Agent must preserve
    later acquisitions
    present faculty membership
    causal status
    realm profile
    termination mode
```

This is another reason a complete Bhāṣya study will matter. The Kārikā gives
compact counts; the Bhāṣya reveals the scope condition—simultaneous death—
without which the rule would be overgeneralized.

## 10. OWL++ Seed

```ttl
@prefix vak: <http://127.0.0.1:3000/vak#> .
@prefix organon: <http://127.0.0.1:3000/organon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

vak:VAK_2_15
    a vak:Karika ;
    rdfs:label "VAK 2.15" ;
    vak:hasTopic vak:TerminalFacultyCessation ;
    vak:belongsTo vak:Indriyanirdesa .

vak:FormlessTerminalProfile
    vak:ceases vak:LifeFaculty,
        vak:MindFaculty,
        vak:NeutralFeelingFaculty ;
    vak:hasCount 3 .

vak:FormTerminalProfile
    vak:ceases vak:LifeFaculty,
        vak:MindFaculty,
        vak:NeutralFeelingFaculty,
        vak:FiveSensoryFaculties ;
    vak:hasCount 8 .

vak:DesireTerminalProfile
    vak:hasBaseSet vak:FormTerminalProfile ;
    vak:variesBy vak:SexualConfiguration ;
    vak:hasPossibleCount 8,
        9,
        10 .

vak:TerminalFacultyCessation
    vak:presupposes vak:SimultaneousDeath .

organon:RealmSensitiveTermination
    a organon:InterpretiveReconstruction ;
    organon:operatesOn vak:PossessedFacultySet ;
    organon:variesBy vak:Realm,
        vak:SexualConfiguration,
        vak:DeathMode ;
    organon:inferredFrom vak:TerminalFacultyCessation .
```
