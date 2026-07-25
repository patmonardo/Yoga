# VAK_4.95

## 1. Sanskrit — Devanāgarī

एकं जन्माक्षिपत्येकमनेकं परिपूरकम् ।
नाक्षेपिके समापत्ती अचित्ते प्राप्तयो न च ॥ ४.९५ ॥

## 2. Sanskrit — IAST

**ekaṃ janmākṣipaty ekam anekaṃ paripūrakam |**  
**nākṣepike samāpattī acitte prāptayo na ca || 4.95 ||**

## 3. Padaccheda

`ekam | janma | ākṣipati | ekam | anekam | paripūrakam | na | ākṣepike | samāpattī | acitte | prāptayaḥ | na | ca`

Expanded first half:

`ekaṃ karma ekaṃ janma ākṣipati; paripūrakaṃ karma tu anekam.`

One karma projects one birth; the completing karma is multiple.

## 4. Grammar

- **ekam** — one; first understood with `karma`, second with `janma`.
- **janma** — one birth or rebirth-existence.
- **ākṣipati** — projects, propels, determines; from `ā + √kṣip`.
- **anekam** — multiple, many.
- **paripūrakam** — completing, filling out.
- **samāpattī** — dual of `samāpatti`, probably the two non-mental attainments.
- **acitte** — in a non-mental condition.
- **prāptayaḥ** — acquisitions or possession-relations.

The exact grouping of the second half remains for the Bhāṣya.

## 5. Literal Translation

> One karma projects one birth; the karma that completes it is multiple. The two attainments are not projecting, nor are acquisitions in the non-mental state.

## 6. Philosophical Translation

> The determination of a life as one birth-event belongs to a single projecting karma, while the concrete fullness of that life is produced through many completing karmas. Projection establishes the unified existential trajectory; completion supplies its multiple determinations. Non-mental attainments and acquisition-relations do not themselves perform the projecting function.

## 7. Technical Vocabulary

- **ākṣepaka-karma** — projecting or birth-determining karma.
- **paripūraka-karma** — completing karma.
- **janma** — one rebirth-existence.
- **samāpatti** — attainment; the dual probably refers to the attainment of non-perception and attainment of cessation.
- **acitta** — non-mental, without presently active mind.
- **prāpti** — acquisition or possession of a dharma by a continuum.

## 8. Doctrinal Determination

The secure distinction is:

- one projecting karma projects one birth;
- many completing karmas fill out that birth;
- projection and completion are distinct causal roles;
- the two non-mental attainments do not project birth;
- acquisition or possession is not itself projection.

Thus unity of birth and multiplicity of its determinations arise through different karmic functions.

## 9. Logical Determination

Let `Kp` be projecting karma, `Kc` completing karma, and `J` one birth.

`Projects(Kp, J)` with one projector for one projected birth.

`Completes(Kc₁, J)`, `Completes(Kc₂, J)`, …, `Completes(Kcₙ, J)`.

Therefore:

- `Projects(K, J)` does not imply `CompletesEveryFeature(K, J)`;
- `Completes(K, J)` does not imply `Projects(K, J)`;
- acquisition of a dharma does not imply projection of birth.

## 10. Light Organon Interpretation

A Kernel representation may distinguish:

```text
BirthCausalProfile {
    projectedBirth
    projectingKarma
    completingKarmas[]
}
```

The projector establishes the unified instance; completing karmas populate its conditioned determinations. A possession marker such as `prāpti` must not be confused with the operation that projects the instance.

## 11. OWL++ Seed

```ttl
vak:VAK_4_95 a vak:Karika ;
    rdfs:label "VAkK 4.95" ;
    vak:continues vak:VAK_4_94 ;
    vak:hasTopic vak:ProjectingKarma, vak:CompletingKarma .

vak:ProjectingKarma rdfs:subClassOf vak:Karma ;
    rdfs:label "ākṣepaka-karma" ;
    vak:projectsCardinality 1 .

vak:CompletingKarma rdfs:subClassOf vak:Karma ;
    rdfs:label "paripūraka-karma" ;
    vak:mayHaveMultiplicity true .

vak:Acquisition rdfs:label "prāpti" ;
    rdfs:subClassOf logic:ContinuumPossessionRelation .
```

## 12. Commit Note

- distinguish one projecting karma from many completing karmas;
- define projection as determining one birth;
- define completion as filling out that projected birth;
- keep projection and completion as separate causal functions;
- exclude non-mental attainments from birth-projection;
- distinguish acquisition or possession from projection;
- close the planned VAK_4d span at VAK_4.95.
